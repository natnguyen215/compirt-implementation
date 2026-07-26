"""Compare fitted versus empirical first-buzz timing.

'first_buzz_distribution' reconstructs the model's competing-risks timing
(Eq. 5 hazard, Eq. 6 survival) for one event using only saved posterior
median parameters, outside of Pyro. 'buzz_density_fit_plot' averages that
reconstruction over every event of a representative sample of tossups and
compares it against the single empirical buzz each event actually produced.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.common.figures import numeric_columns, short_id
from compirt_eval.common.metrics import inverse_logit
from compirt_eval.common.report_paths import csv_path, graph_path
from compirt_eval.scenario_a_tossups.difficulty import selected_tossups
from compirt_eval.scenario_a_tossups.parameters import (
    _parameter_columns,
    _saved_difficulty_curve,
    _saved_effective_mu,
    _supports_first_buzz_reconstruction,
    difficulty_adjustment_at,
    load_difficulty_adjustment_curves,
    load_difficulty_link,
)


DifficultyAdjustments = tuple[dict[str, np.ndarray], np.ndarray]


@dataclass(frozen=True)
class _TimingEvaluationInputs:
    """Saved posterior tables needed for first-buzz evaluation."""

    players: pd.DataFrame
    tossups: pd.DataFrame
    predictions: pd.DataFrame
    adjustments: DifficultyAdjustments | None
    link: str


def event_first_buzz_components(
    event, players, tossups, adjustments=None, link="sigmoid"
):
    """Reconstruct timing, player attribution, and correctness for one event.

    The probability that someone buzzes at a token is conserved exactly.  It is
    divided among players in proportion to the probability that each player is
    the only buzzer at that token, matching the model-analysis convention used
    elsewhere in this repository.  The returned player-token masses plus the
    dead mass sum to one up to floating-point error.
    """
    # First-buzz timing is a full-field phase-0 quantity. Bounceback runs add
    # phase-1 'BOUNCE-*' rows that share an event_id but are an opponent-only
    # continuation; including them would list the opposing players twice and
    # inflate the buzz mass. This single filter covers every caller
    # (buzz-density, first-buzzer identity, replay, and match simulation).
    # Guarded because some callers pass minimal event frames without 'z'; the
    # prefix is likewise absent from pre-bounceback runs.
    if "z" in event.columns:
        event = event[~event["z"].astype(str).str.startswith("BOUNCE")]
    tossup_id = event["tossup_id"].iloc[0]
    tossup = tossups.loc[tossup_id]
    roster = players.loc[event["player_id"].astype(str)]
    theta_columns = numeric_columns(players, "theta_")
    columns = _parameter_columns(tossups)
    alpha_columns = columns["alpha"]
    if not theta_columns or len(theta_columns) != len(alpha_columns):
        raise ValueError(
            "Saved theta and discrimination/relevance dimensions must be present and match"
        )

    total_tokens = int(event["T_j"].iloc[0])
    positions = np.arange(1, total_tokens + 1, dtype=float)
    relative = positions / total_tokens
    difficulty = _saved_difficulty_curve(tossup, relative, link)
    if difficulty is None:
        raise ValueError("Saved tossup parameters cannot reconstruct difficulty")
    adjustment = difficulty_adjustment_at(adjustments, tossup_id, relative)
    if adjustment is not None:
        # TF-IDF runs: replay the effective difficulty d' the model trained on.
        difficulty = difficulty + adjustment
    skill = (
        roster[theta_columns].to_numpy(dtype=float)
        @ tossup[alpha_columns].to_numpy(dtype=float)
    )
    logits = (
        skill[:, None]
        - difficulty[None, :]
        - roster["c"].to_numpy(dtype=float)[:, None]
    )
    hazard = inverse_logit(logits)
    team_hazard = 1.0 - np.prod(1.0 - hazard, axis=0)
    survival_before = np.concatenate(([1.0], np.cumprod(1.0 - team_hazard[:-1])))
    first_buzz_mass = survival_before * team_hazard
    dead_mass = float(np.prod(1.0 - team_hazard))
    no_buzz = np.prod(1.0 - hazard, axis=0)
    weights = hazard * (no_buzz[None, :] / np.clip(1.0 - hazard, 1e-6, None))
    weight_sum = weights.sum(axis=0)
    fallback = hazard / np.clip(hazard.sum(axis=0), 1e-12, None)
    attribution = np.where(
        weight_sum[None, :] > 1e-12,
        weights / np.clip(weight_sum[None, :], 1e-12, None),
        fallback,
    )
    player_first_buzz_mass = (
        survival_before[None, :] * team_hazard[None, :] * attribution
    )
    correctness_probability = inverse_logit(skill[:, None] - difficulty[None, :])
    player_to_team = (
        dict(zip(event["player_id"].astype(str), event["team_id"].astype(str)))
        if "team_id" in event
        else {}
    )
    return {
        "relative_position": relative,
        "first_buzz_mass": first_buzz_mass,
        "dead_mass": dead_mass,
        "player_first_buzz_mass": player_first_buzz_mass,
        "correctness_probability": correctness_probability,
        "player_ids": roster.index.astype(str).to_numpy(),
        "team_ids": np.asarray(
            [player_to_team.get(player_id, "Unknown") for player_id in roster.index.astype(str)]
        ),
    }


def _event_first_buzz_mass(event, players, tossups, adjustments=None, link="sigmoid"):
    """Return per-token relative positions, first-buzz mass, and dead mass."""
    components = event_first_buzz_components(event, players, tossups, adjustments, link)
    return (
        components["relative_position"],
        components["first_buzz_mass"],
        components["dead_mass"],
    )


def first_buzz_distribution(
    event, players, tossups, n_bins=12, adjustments=None, link="sigmoid"
):
    """Reconstruct team first-buzz mass from saved posterior median parameters.

    This replays the fitted Eq. 5 hazards outside Pyro as an end-inclusive
    diagnostic distribution: it returns how much first-buzz probability falls
    in each relative-position bin plus the probability remaining after the
    final token. The training likelihood follows the paper's Eq. 6/13
    convention S(T_j) = product over s < T_j, so this diagnostic should not be
    read as a byte-for-byte replay of its dead-tossup censoring term.
    """
    relative, first_buzz_mass, dead_mass = _event_first_buzz_mass(
        event, players, tossups, adjustments, link
    )
    bin_index = np.clip((relative * n_bins).astype(int), 0, n_bins - 1)
    binned_mass = np.zeros(n_bins)
    np.add.at(binned_mass, bin_index, first_buzz_mass)
    return binned_mass, dead_mass


def conditional_expected_buzz_position(
    event, players, tossups, adjustments=None, link="sigmoid"
):
    """Return E[relative position | a buzz occurs] for one event's roster.

    Matches the trainers' 'expected_first_buzz_positions' convention after the
    buzz-conditioning fix: the expectation is normalized by the fitted buzz
    mass, with a question-end fallback when that mass is numerically zero.
    Used by 'run_scripts/common/replay_buzz_positions.py' to regenerate
    'buzz_event_predictions.csv' for runs trained before the fix.
    """
    relative, first_buzz_mass, _ = _event_first_buzz_mass(
        event, players, tossups, adjustments, link
    )
    buzz_mass = float(first_buzz_mass.sum())
    if buzz_mass <= 1e-9:
        return 1.0
    return float((relative * first_buzz_mass).sum() / buzz_mass)


def _aggregate_buzz_timing(
    predictions, players, tossups, tossup_id, n_bins, adjustments=None, link="sigmoid"
):
    """Average fitted and empirical first-buzz mass over one tossup's events.

    Walks every event for 'tossup_id', sums the model's fitted first-buzz mass
    (from 'first_buzz_distribution') against the single observed buzz bin, then
    normalizes by the event count. Returns the per-event mass arrays, both dead
    rates, or 'None' when no usable event is found (so the caller can blank
    that subplot).
    """
    predicted = np.zeros(n_bins)
    observed = np.zeros(n_bins)
    predicted_dead = 0.0
    observed_dead = 0
    event_count = 0
    for _, event in predictions[predictions["tossup_id"] == tossup_id].groupby("event_id"):
        if not set(event["player_id"]).issubset(players.index):
            continue
        fitted_mass, fitted_dead = first_buzz_distribution(
            event, players, tossups, n_bins, adjustments, link
        )
        predicted += fitted_mass
        predicted_dead += fitted_dead
        buzz = event[event["z"] == "BUZZ"]
        if buzz.empty:
            observed_dead += 1
        else:
            index = min(int(float(buzz["relative_position"].iloc[0]) * n_bins), n_bins - 1)
            observed[index] += 1
        event_count += 1
    if event_count == 0:
        return None
    predicted /= event_count
    predicted_dead /= event_count
    observed /= event_count
    observed_dead_rate = observed_dead / event_count
    return {
        "event_count": event_count,
        "predicted": predicted,
        "observed": observed,
        "predicted_dead": predicted_dead,
        "observed_dead_rate": observed_dead_rate,
    }


def buzz_density_fit_plot(results_dir, output_dir, n_bins=12):
    """Compare empirical and fitted first-buzz timing for representative tossups."""
    inputs = _load_timing_evaluation_inputs(results_dir)
    if inputs is None:
        return

    selected = [
        tossup_id
        for tossup_id in selected_tossups(inputs.predictions)
        if tossup_id in inputs.tossups.index
    ]
    if not selected:
        return
    columns = 2
    rows = math.ceil(len(selected) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(12, 3.8 * rows), squeeze=False)
    centers = (np.arange(n_bins) + 0.5) / n_bins
    summaries = []
    for ax, tossup_id in zip(axes.flat, selected):
        timing = _aggregate_buzz_timing(
            inputs.predictions,
            inputs.players,
            inputs.tossups,
            tossup_id,
            n_bins,
            inputs.adjustments,
            inputs.link,
        )
        if timing is None:
            ax.set_visible(False)
            continue
        event_count = timing["event_count"]
        predicted = timing["predicted"]
        observed = timing["observed"]
        predicted_dead = timing["predicted_dead"]
        observed_dead_rate = timing["observed_dead_rate"]
        summaries.append(
            {
                "tossup_id": tossup_id,
                "events": event_count,
                "observed_dead_rate": observed_dead_rate,
                "predicted_dead_rate": predicted_dead,
            }
        )
        ax.bar(
            centers,
            observed,
            width=0.8 / n_bins,
            alpha=0.35,
            color="tab:orange",
            label="Empirical mass",
        )
        ax.plot(centers, predicted, "o-", color="tab:blue", label="Predicted mass")
        mu = _saved_effective_mu(inputs.tossups.loc[tossup_id])
        if mu is not None:
            ax.axvline(
                mu,
                color="tab:green",
                linestyle="--",
                linewidth=1.5,
                label=f"Difficulty inflection ($\\mu$={mu:.2f})",
            )
        ax.set(
            title=short_id(tossup_id),
            xlabel="Relative position",
            ylabel="Probability mass per event",
            xlim=(0, 1),
        )
        ax.text(
            0.02,
            0.98,
            f"events={event_count}\n"
            f"dead: observed={observed_dead_rate:.2f}, predicted={predicted_dead:.2f}",
            transform=ax.transAxes,
            va="top",
            fontsize=8,
        )
        ax.grid(alpha=0.2)
        ax.legend(fontsize=7, loc="upper right")
    for ax in axes.flat[len(selected):]:
        ax.set_visible(False)
    fig.suptitle("Predicted versus empirical first-buzz timing")
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, "tossup_buzz_density_fit.png", "tossup"), dpi=160)
    plt.close(fig)
    pd.DataFrame(summaries).to_csv(
        csv_path(output_dir, "tossup_buzz_density_metrics.csv"), index=False
    )


def _load_timing_evaluation_inputs(results_dir):
    """Return saved timing inputs, or ``None`` for unsupported result sets."""
    required = [
        results_dir / "players.csv",
        results_dir / "tossups.csv",
        results_dir / "tossup_predictions.csv",
    ]
    if not all(path.exists() for path in required):
        return None

    players = pd.read_csv(required[0], dtype={"player_id": str}).set_index("player_id")
    tossups = pd.read_csv(required[1], dtype={"tossup_id": str}).set_index("tossup_id")
    predictions = pd.read_csv(
        required[2], dtype={"player_id": str, "tossup_id": str}
    )
    if predictions.empty or "c" not in players:
        return None
    if not _supports_first_buzz_reconstruction(players, tossups):
        return None
    return _TimingEvaluationInputs(
        players=players,
        tossups=tossups,
        predictions=predictions,
        adjustments=load_difficulty_adjustment_curves(results_dir),
        link=load_difficulty_link(results_dir),
    )


def _event_buzz_curve(components, grid):
    """Evaluate an event's cumulative first-buzz probability on ``grid``."""
    relative = components["relative_position"]
    cumulative = np.cumsum(components["first_buzz_mass"])
    end_indices = np.searchsorted(relative, grid, side="right")
    predicted = np.zeros_like(grid)
    has_tokens = end_indices > 0
    predicted[has_tokens] = cumulative[end_indices[has_tokens] - 1]
    return predicted


def _first_buzzer_row(event_id, event, tossup_id, buzz, components):
    """Return an identity-prediction row and whether its observed player was absent."""
    if buzz.empty:
        return None, False

    player_mass = components["player_first_buzz_mass"].sum(axis=1)
    buzz_mass = player_mass.sum()
    # A uniform fallback keeps identity metrics defined in a degenerate event.
    probabilities = (
        player_mass / buzz_mass
        if buzz_mass > 1e-12
        else np.full(len(player_mass), 1.0 / len(player_mass))
    )
    actual_player = str(buzz["player_id"].iloc[0])
    matches = np.flatnonzero(components["player_ids"] == actual_player)
    if not len(matches):
        return None, True

    actual_index = int(matches[0])
    order = np.argsort(-probabilities, kind="stable")
    rank = int(np.flatnonzero(order == actual_index)[0]) + 1
    predicted_index = int(order[0])
    return {
        "event_id": event_id,
        "game_id": event["game_id"].iloc[0],
        "tossup_id": tossup_id,
        "actual_player_id": actual_player,
        "predicted_player_id": components["player_ids"][predicted_index],
        "actual_player_probability": probabilities[actual_index],
        "actual_player_rank": rank,
        "dead_probability": components["dead_mass"],
        "roster_size": len(probabilities),
    }, False


def _time_metric_table(predicted_by_time, observed_by_time, grid):
    """Build per-position calibration and Brier metrics."""
    rows = []
    for index, point in enumerate(grid):
        observed = observed_by_time[:, index]
        probability = predicted_by_time[:, index]
        rows.append(
            {
                "relative_position": point,
                "events": len(observed),
                "observed_buzz_rate": observed.mean(),
                "predicted_buzz_rate": probability.mean(),
                "brier": np.mean((probability - observed) ** 2),
            }
        )
    return pd.DataFrame(rows)


def _survival_summary(time_metrics, identities, event_count, skipped):
    """Aggregate the scalar metrics written to the evaluation summary."""
    summary = {
        "integrated_brier_score": float(
            np.trapezoid(time_metrics["brier"], time_metrics["relative_position"])
        ),
        "survival_events": event_count,
        "survival_events_skipped": skipped,
    }
    if not identities.empty:
        summary.update(
            {
                "first_buzzer_top1_accuracy": float(
                    (identities["actual_player_rank"] == 1).mean()
                ),
                "first_buzzer_mean_reciprocal_rank": float(
                    (1.0 / identities["actual_player_rank"]).mean()
                ),
                "first_buzzer_log_loss": float(
                    -np.log(
                        np.clip(identities["actual_player_probability"], 1e-12, 1.0)
                    ).mean()
                ),
                "first_buzzer_events": len(identities),
            }
        )
    return summary


def _plot_first_buzzer_identity(identities, output_dir):
    """Plot first-buzzer top-1 accuracy and MRR against roster size.

    The dashed 1/n curve is the uniform-guess baseline; it moves with the
    number of players racing for the buzz, so each roster size's scores are
    read against their own chance level.
    """
    grouped = identities.groupby("roster_size")
    sizes = np.asarray(sorted(grouped.groups))
    top1 = grouped["actual_player_rank"].apply(lambda ranks: (ranks == 1).mean())
    reciprocal_rank = grouped["actual_player_rank"].apply(
        lambda ranks: (1.0 / ranks).mean()
    )
    counts = grouped.size()
    fig, ax = plt.subplots(figsize=(7.5, 5.5))
    ax.plot(sizes, top1.loc[sizes], "o-", label="Top-1 accuracy")
    ax.plot(sizes, reciprocal_rank.loc[sizes], "s-", label="Mean reciprocal rank")
    ax.plot(sizes, 1.0 / sizes, "--", color="0.5", label="Chance (1 / roster size)")
    ax.set_xticks(
        sizes, [f"{size}\n(n={counts.loc[size]:,})" for size in sizes]
    )
    ax.set(
        title="First-buzzer identification by roster size",
        xlabel="Players present at the event",
        ylabel="Score",
        ylim=(0, 1),
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, "first_buzzer_identity.png", "tossup"), dpi=160)
    plt.close(fig)


def _plot_survival_metrics(time_metrics, output_dir):
    """Render the Brier score over the question."""
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.plot(
        time_metrics["relative_position"],
        time_metrics["brier"],
        "o-",
        color="tab:orange",
    )
    ax.set(
        title="Brier score over question",
        xlabel="Relative position",
        ylabel="Brier score",
        ylim=(0, None),
    )
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, "tossup_survival_metrics.png", "tossup"), dpi=160)
    plt.close(fig)


def evaluate_survival_and_first_buzzer(results_dir, output_dir, n_time_points=20):
    """Score full first-buzz curves and the identity of the first buzzer.

    At each relative token position this asks whether an event has buzzed by
    that point. The Brier score measures probability error, and integrating it
    over the normalized question gives IBS. No inverse-censoring weighting is
    needed here because every reconstructed event has a known endpoint: either
    an observed first buzz or a recovered dead tossup.
    """
    inputs = _load_timing_evaluation_inputs(results_dir)
    if inputs is None:
        return {}

    grid = np.linspace(0.0, 1.0, n_time_points + 1)
    predicted_by_time = []
    observed_by_time = []
    identity_rows = []
    skipped = 0
    for event_id, event in inputs.predictions.groupby("event_id", sort=False):
        tossup_id = str(event["tossup_id"].iloc[0])
        if tossup_id not in inputs.tossups.index or not set(
            event["player_id"]
        ).issubset(
            inputs.players.index
        ):
            skipped += 1
            continue
        components = event_first_buzz_components(
            event,
            inputs.players,
            inputs.tossups,
            inputs.adjustments,
            inputs.link,
        )
        buzz = event[event["z"] == "BUZZ"]
        observed_position = (
            float(buzz["relative_position"].iloc[0]) if not buzz.empty else np.inf
        )
        predicted_by_time.append(_event_buzz_curve(components, grid))
        observed_by_time.append((grid >= observed_position).astype(float))
        identity_row, missing_observed_player = _first_buzzer_row(
            event_id, event, tossup_id, buzz, components
        )
        skipped += missing_observed_player
        if identity_row is not None:
            identity_rows.append(identity_row)

    if not predicted_by_time:
        return {}
    predicted_by_time = np.asarray(predicted_by_time)
    observed_by_time = np.asarray(observed_by_time)
    time_metrics = _time_metric_table(predicted_by_time, observed_by_time, grid)
    identities = pd.DataFrame(identity_rows)
    time_metrics.to_csv(csv_path(output_dir, "tossup_time_metrics.csv"), index=False)
    identities.to_csv(
        csv_path(output_dir, "first_buzzer_predictions.csv"), index=False
    )
    summary = _survival_summary(
        time_metrics, identities, len(predicted_by_time), skipped
    )
    _plot_survival_metrics(time_metrics, output_dir)
    if not identities.empty:
        _plot_first_buzzer_identity(identities, output_dir)
    return summary
