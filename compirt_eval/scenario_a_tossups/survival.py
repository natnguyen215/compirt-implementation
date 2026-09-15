"""Score and plot first-buzz survival, player identity, and marked outcomes."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.common.report_paths import csv_path, graph_path
from compirt_eval.scenario_a_tossups.reconstruction import (
    _load_timing_evaluation_inputs,
    event_first_buzz_components,
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


def _full_pmf_score_row(event_id, event, components):
    """Score the observed marked outcome in the complete event PMF."""
    total_mass = float(
        components["dead_mass"] + components["player_first_buzz_mass"].sum()
    )
    buzz = event[event["z"] == "BUZZ"]
    observed_dead = buzz.empty
    if observed_dead:
        probability = float(components["dead_mass"])
        outcome = "no_buzz"
    else:
        observed = buzz.iloc[0]
        if "y" not in observed.index or pd.isna(observed["y"]):
            return None
        player_matches = np.flatnonzero(
            components["player_ids"] == str(observed["player_id"])
        )
        if "t_star" in observed.index:
            token = int(observed["t_star"]) - 1
        else:
            token = int(
                round(float(observed["relative_position"]) * int(observed["T_j"]))
            ) - 1
        if not len(player_matches) or not 0 <= token < len(components["relative_position"]):
            return None
        player = int(player_matches[0])
        event_mass = components["player_first_buzz_mass"][player, token]
        # The saved row already includes any fitted correctness calibration.
        correct = (
            float(observed["predicted_correct"])
            if "predicted_correct" in observed
            and pd.notna(observed["predicted_correct"])
            else components["correctness_probability"][player, token]
        )
        probability = float(
            event_mass * (correct if int(observed["y"]) else 1.0 - correct)
        )
        outcome = "correct_buzz" if int(observed["y"]) else "neg"
    final_decile = float(
        components["first_buzz_mass"][
            components["relative_position"] >= 0.9
        ].sum()
    )
    return {
        "event_id": event_id,
        "observed_outcome": outcome,
        "observed_no_buzz": int(observed_dead),
        "predicted_no_buzz": float(components["dead_mass"]),
        "observed_probability": probability,
        "joint_event_log_loss": float(-np.log(np.clip(probability, 1e-12, 1.0))),
        "final_decile_mass": final_decile,
        "pmf_total_mass": total_mass,
    }


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
        title="Hazard-based first-buzzer identification by roster size",
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
        title="Hazard-based first-buzz Brier score over question",
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
    pmf_rows = []
    skipped = 0
    reconstruction_cache = {}
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
            inputs.buzz_parameter_prefix,
            inputs.difficulty_scale,
            inputs.terminal_intercepts,
            reconstruction_cache=reconstruction_cache,
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
        pmf_row = _full_pmf_score_row(event_id, event, components)
        if pmf_row is not None:
            pmf_rows.append(pmf_row)

    if not predicted_by_time:
        return {}
    predicted_by_time = np.asarray(predicted_by_time)
    observed_by_time = np.asarray(observed_by_time)
    time_metrics = _time_metric_table(predicted_by_time, observed_by_time, grid)
    identities = pd.DataFrame(identity_rows)
    pmf_scores = pd.DataFrame(pmf_rows)
    time_metrics.to_csv(csv_path(output_dir, "tossup_time_metrics.csv"), index=False)
    identities.to_csv(
        csv_path(output_dir, "first_buzzer_predictions.csv"), index=False
    )
    pmf_scores.to_csv(
        csv_path(output_dir, "tossup_full_pmf_scores.csv"), index=False
    )
    summary = _survival_summary(
        time_metrics, identities, len(predicted_by_time), skipped
    )
    # Older/minimal saved prediction fixtures may omit correctness marks. Only
    # publish pooled marked-PMF metrics when every reconstructed event is
    # scoreable; partial denominators would be misleading.
    if len(pmf_scores) == len(predicted_by_time):
        no_buzz_error = (
            pmf_scores["predicted_no_buzz"] - pmf_scores["observed_no_buzz"]
        )
        summary.update(
            {
                "joint_tossup_event_log_loss": float(
                    pmf_scores["joint_event_log_loss"].mean()
                ),
                "full_pmf_events": len(pmf_scores),
                "full_pmf_final_decile_mass": float(
                    pmf_scores["final_decile_mass"].mean()
                ),
                "no_buzz_observed_rate": float(
                    pmf_scores["observed_no_buzz"].mean()
                ),
                "no_buzz_predicted_rate": float(
                    pmf_scores["predicted_no_buzz"].mean()
                ),
                "no_buzz_calibration_error": float(no_buzz_error.mean()),
                "no_buzz_brier": float(np.mean(no_buzz_error**2)),
                "full_pmf_max_mass_error": float(
                    np.max(np.abs(pmf_scores["pmf_total_mass"] - 1.0))
                ),
            }
        )
    _plot_survival_metrics(time_metrics, output_dir)
    if not identities.empty:
        _plot_first_buzzer_identity(identities, output_dir)
    return summary
