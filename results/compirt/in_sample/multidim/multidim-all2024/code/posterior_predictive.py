"""Small, bounded posterior predictive checks (PPCs) for the two SVI stages.

A PPC asks whether data replicated from the fitted model looks like the data
that was actually observed. Each check draws parameters from the fitted
AutoNormal guide, replays the generative process forward to draw replicated
outcomes, and reduces both the observed and replicated data to a handful of
discrepancy statistics (dead-tossup rate, neg rate, buzz-position mass, bonus
score mass). Comparing the two answers "is the observation a typical draw?".

The two writers run inside their trainers and cap the number of events /
responses so the check stays cheap:

* 'save_pyramidal_ppc' -- Stage 1, replays the Eq. 5 competing-risks first
  buzz forward per event (phase-0 rows only; bounceback phase-1 rows share an
  event_id but are an opponent-only continuation).
* 'save_bonus_ppc' -- Stage 2, replays the Eq. 11 bonus-part Bernoulli.

'evaluate_saved_ppc' is the read-side entry point: it pools the saved draws,
turns each discrepancy into a posterior-predictive p-value, and plots the
observed value against the replicated 5-95% interval.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch

from compirt_race import cell_probabilities

from compirt_eval.common.report_paths import csv_path, graph_path
from compositional_model import posterior_predictions
from multidimensional.multidim_mirt.pyramidal_model import (
    correctness_logit,
    hazard_logit,
)


BUZZ_POSITION_BINS = (0.0, 0.2, 0.4, 0.6, 0.8, 1.0)
BUZZ_POSITION_LABELS = ("Q1", "Q2", "Q3", "Q4", "Q5")


def _discrepancy_row(stage, draw, discrepancy, stratum, value):
    """Build one consistently shaped posterior-predictive discrepancy row."""
    return {
        "stage": stage,
        "draw": draw,
        "discrepancy": discrepancy,
        "stratum": stratum,
        "value": value,
    }


def _observed_stage1_discrepancies(observations):
    """Return the observed Stage 1 discrepancies as (name, stratum, value) rows.

    These are the reference values every replicated draw is scored against: the
    dead-tossup rate, the overall neg rate, the fraction of first buzzes landing
    in each fifth of the question, and a per-player neg rate for players with at
    least three observed buzzes.
    """
    events = observations.drop_duplicates("event_id")
    buzz = observations[observations["z"] == "BUZZ"].copy()
    rows = [
        ("dead_tossup_rate", "all", float((events["z"] == "NO-BUZZ").mean())),
        (
            "neg_rate",
            "all",
            float((buzz["y"] == 0).mean()) if len(buzz) else np.nan,
        ),
    ]
    if len(buzz):
        quintile = pd.cut(
            buzz["relative_position"],
            BUZZ_POSITION_BINS,
            labels=BUZZ_POSITION_LABELS,
            include_lowest=True,
        )
        for label, value in quintile.value_counts(normalize=True, sort=False).items():
            rows.append(("buzz_position_mass", str(label), float(value)))
        for player_id, group in buzz.groupby("player_id"):
            if len(group) >= 3:
                rows.append(
                    (
                        "player_neg_rate",
                        str(player_id),
                        float((group["y"] == 0).mean()),
                    )
                )
    return rows


def save_pyramidal_ppc(
    output_dir,
    observations,
    data,
    guide,
    model_kwargs,
    draws=20,
    max_events=500,
    seed=42,
):
    """Draw capped Stage 1 replications and save discrepancy summaries."""
    if draws <= 0:
        return
    rng = np.random.default_rng(seed)
    event_ids = observations["event_id"].drop_duplicates().to_numpy()
    if len(event_ids) > max_events:
        event_ids = rng.choice(event_ids, size=max_events, replace=False)
    selected = observations[observations["event_id"].isin(event_ids)].copy()
    selected_event_set = set(event_ids)
    event_indices = [
        index
        for index, value in enumerate(data["event_ids"])
        if value in selected_event_set
    ]
    observed = _observed_stage1_discrepancies(selected)
    rows = [
        _discrepancy_row("pyramidal", -1, name, stratum, value)
        for name, stratum, value in observed
    ]
    calibrate = bool(model_kwargs.get("calibrate_correctness", False))
    link = model_kwargs.get("link", "sigmoid")
    # Replay the full-field first buzz, so restrict each event to its phase-0
    # rows; phase-1 bounceback rows (present only when include_bounceback is on)
    # share an event_id but are an opponent-only continuation. Absent
    # 'is_phase0' means every row is phase 0.
    phase0 = data.get("is_phase0")
    event_rows = {}
    for event_index in event_indices:
        indices = torch.nonzero(
            data["event"] == event_index, as_tuple=False
        ).flatten()
        if phase0 is not None:
            indices = indices[phase0[indices]]
        event_rows[event_index] = indices
    for draw in range(draws):
        # One parameter draw from the fitted guide seeds the whole replica.
        with torch.no_grad():
            posterior = guide(**model_kwargs)
        dead = 0
        buzz_positions = []
        player_outcomes = []
        for event_index, indices in event_rows.items():
            first = int(indices[0])
            player = data["player"][indices]
            tossup = int(data["tossup"][first])
            total_tokens = int(data["T_j"][first])
            positions = torch.arange(
                1, total_tokens + 1, device=data["y"].device, dtype=data["y"].dtype
            )
            theta = posterior["theta"][player]
            c = posterior["c"][player]
            r = posterior["r"][tossup]
            beta = posterior["beta"][tossup]
            gamma = posterior["gamma"][tossup]
            mu = posterior["mu"][tossup]
            # Eq. 5 hazard for every (roster player, token position) pair:
            # shape (n_players, total_tokens).
            time = positions.unsqueeze(0).expand(len(player), -1)
            total = torch.full_like(time, float(total_tokens))
            logits = hazard_logit(
                theta.unsqueeze(1),
                r,
                beta,
                gamma,
                mu,
                c.unsqueeze(1),
                time,
                total,
                link,
            )
            no_buzz, team_hazard, attribution = cell_probabilities(logits)
            # First-buzz mass per token = P(nobody buzzed earlier) * team_hazard;
            # the trailing category is the dead-tossup mass (nobody ever buzzes).
            survival = torch.cat(
                [team_hazard.new_ones(1), torch.cumprod(no_buzz[:-1], dim=0)]
            )
            mass = survival * team_hazard
            distribution = torch.cat(
                [mass, no_buzz.prod().reshape(1)]
            )
            # Sample the first-buzz token (or the dead outcome) for this replica.
            chosen = int(torch.multinomial(distribution / distribution.sum(), 1))
            if chosen == total_tokens:
                dead += 1
                continue
            buzz_positions.append((chosen + 1) / total_tokens)
            probabilities = attribution[:, chosen]
            player_choice = int(torch.multinomial(probabilities, 1))
            # Eq. 4 correctness for the sampled buzzer at the sampled token.
            correctness = correctness_logit(
                theta[player_choice],
                r,
                beta,
                gamma,
                mu,
                positions[chosen],
                positions.new_tensor(float(total_tokens)),
                link,
            )
            if calibrate:
                correctness = (
                    posterior["correctness_scale"] * correctness
                    + posterior["correctness_bias"]
                )
            outcome = int(torch.bernoulli(torch.sigmoid(correctness)))
            player_id = data["player_ids"][int(player[player_choice])]
            player_outcomes.append((player_id, outcome))
        n_events = len(event_rows)
        rows.append(
            _discrepancy_row(
                "pyramidal", draw, "dead_tossup_rate", "all", dead / n_events
            )
        )
        neg_rate = (
            float(np.mean([1 - outcome for _, outcome in player_outcomes]))
            if player_outcomes
            else np.nan
        )
        rows.append(_discrepancy_row("pyramidal", draw, "neg_rate", "all", neg_rate))
        counts = np.histogram(buzz_positions, bins=BUZZ_POSITION_BINS)[0]
        for label, count in zip(BUZZ_POSITION_LABELS, counts):
            rows.append(
                _discrepancy_row(
                    "pyramidal",
                    draw,
                    "buzz_position_mass",
                    label,
                    count / max(1, len(buzz_positions)),
                )
            )
        outcome_frame = pd.DataFrame(player_outcomes, columns=["player_id", "correct"])
        if not outcome_frame.empty:
            for player_id, group in outcome_frame.groupby("player_id"):
                if len(group) >= 3:
                    rows.append(
                        _discrepancy_row(
                            "pyramidal",
                            draw,
                            "player_neg_rate",
                            player_id,
                            float((group["correct"] == 0).mean()),
                        )
                    )
    pd.DataFrame(rows).to_csv(
        output_dir / "posterior_predictive_checks.csv", index=False
    )


def save_bonus_ppc(
    output_dir,
    observations,
    data,
    theta,
    guide,
    model_kwargs,
    draws=20,
    max_responses=500,
    seed=42,
):
    """Draw capped Stage 2 replications of bonus-score distributions."""
    if draws <= 0:
        return
    rng = np.random.default_rng(seed)
    response_ids = observations["response_id"].drop_duplicates().to_numpy()
    if len(response_ids) > max_responses:
        response_ids = rng.choice(response_ids, size=max_responses, replace=False)
    selected_mask = observations["response_id"].isin(response_ids).to_numpy()
    indices = np.flatnonzero(selected_mask)
    selected = observations.iloc[indices].copy()
    # Slice every row-aligned tensor down to the sampled responses so
    # posterior_predictions replays Eq. 11 only on the capped subset. Tensors
    # that are not one-per-observation (e.g. per-part parameters) pass through.
    subset = dict(data)
    for key, value in data.items():
        if (
            torch.is_tensor(value)
            and value.ndim > 0
            and value.shape[0] == len(observations)
        ):
            subset[key] = value[torch.as_tensor(indices, device=value.device)]
    observed_scores = selected.groupby("response_id")["correct"].sum().astype(int)
    rows = []
    for score in range(4):
        rows.append(
            _discrepancy_row(
                "compositional",
                -1,
                "bonus_score_mass",
                str(10 * score),
                float((observed_scores == score).mean()),
            )
        )
    for draw in range(draws):
        with torch.no_grad():
            posterior = guide(**model_kwargs)
            probabilities, _, _ = posterior_predictions(
                subset,
                theta,
                posterior,
                model_kwargs.get("use_synergy", False),
                model_kwargs.get("calibrate_correctness", False),
            )
            replicated = torch.bernoulli(probabilities).detach().cpu().numpy()
        replica = selected[["response_id"]].copy()
        replica["correct"] = replicated
        scores = replica.groupby("response_id")["correct"].sum().astype(int)
        for score in range(4):
            rows.append(
                _discrepancy_row(
                    "compositional",
                    draw,
                    "bonus_score_mass",
                    str(10 * score),
                    float((scores == score).mean()),
                )
            )
    pd.DataFrame(rows).to_csv(
        output_dir / "posterior_predictive_checks.csv", index=False
    )


def evaluate_saved_ppc(pyramidal_results, compositional_results, output_dir):
    """Combine saved PPC draws and summarize whether observations look typical."""
    frames = []
    for path in (
        pyramidal_results / "posterior_predictive_checks.csv",
        compositional_results / "posterior_predictive_checks.csv",
    ):
        if path.exists():
            frames.append(pd.read_csv(path))
    if not frames:
        return pd.DataFrame()
    draws = pd.concat(frames, ignore_index=True)
    draws.to_csv(csv_path(output_dir, "posterior_predictive_draws.csv"), index=False)
    rows = []
    groups = draws.groupby(["stage", "discrepancy", "stratum"], dropna=False)
    for (stage, discrepancy, stratum), group in groups:
        observed = group.loc[group["draw"] == -1, "value"]
        replicated = group.loc[group["draw"] >= 0, "value"].dropna()
        if observed.empty or replicated.empty:
            continue
        observed_value = float(observed.iloc[0])
        rows.append(
            {
                "stage": stage,
                "discrepancy": discrepancy,
                "stratum": stratum,
                "observed": observed_value,
                "replicated_mean": replicated.mean(),
                "replicated_p05": replicated.quantile(0.05),
                "replicated_p95": replicated.quantile(0.95),
                "posterior_predictive_p_value": float(
                    (replicated >= observed_value).mean()
                ),
                "draws": len(replicated),
            }
        )
    summary = pd.DataFrame(rows)
    summary.to_csv(csv_path(output_dir, "posterior_predictive_summary.csv"), index=False)
    plot = summary[
        summary["discrepancy"].isin(
            ["dead_tossup_rate", "neg_rate", "buzz_position_mass", "bonus_score_mass"]
        )
    ].copy()
    if not plot.empty:
        labels = (
            plot["stage"]
            + ": "
            + plot["discrepancy"]
            + " / "
            + plot["stratum"].astype(str)
        )
        positions = np.arange(len(plot))
        fig, ax = plt.subplots(figsize=(10, max(4, 0.35 * len(plot))))
        ax.errorbar(
            plot["replicated_mean"],
            positions,
            xerr=np.vstack(
                [
                    plot["replicated_mean"] - plot["replicated_p05"],
                    plot["replicated_p95"] - plot["replicated_mean"],
                ]
            ),
            fmt="o",
            label="Replicated 5-95% interval",
        )
        ax.scatter(
            plot["observed"],
            positions,
            marker="x",
            color="black",
            label="Observed",
        )
        ax.set_yticks(positions, labels)
        ax.set(title="Posterior predictive checks", xlabel="Discrepancy value")
        ax.grid(alpha=0.25, axis="x")
        ax.legend()
        fig.tight_layout()
        fig.savefig(
            graph_path(output_dir, "posterior_predictive_checks.png", "diagnostics"),
            dpi=160,
        )
        plt.close(fig)
    return summary
