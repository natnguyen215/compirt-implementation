"""Evaluation helpers for isolated topic-weighted CompIRT runs."""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, median_absolute_error

from compirt_eval.bonuses import evaluate_bonuses
from compirt_eval.figures import (
    distribution_dashboard,
    distribution_summary,
    labeled_series,
    numeric_columns,
    reliability_plot,
    short_id,
)
from compirt_eval.metrics import classification_metrics, inverse_logit
from compirt_eval.tossups import (
    player_skill_stability_plot,
    selected_tossups,
    stratified_tossup_reliability_plot,
)


def _sigmoid(argument):
    """Return a numerically stable NumPy sigmoid."""
    return 1.0 / (1.0 + np.exp(-np.clip(argument, -60, 60)))


def _topic_columns(frame):
    """Return saved topic-pyramidal parameter columns in dimension order."""
    return {
        "theta": numeric_columns(frame, "theta_"),
        "topic_weight": numeric_columns(frame, "topic_weight_"),
        "beta": numeric_columns(frame, "beta_"),
        "gamma": numeric_columns(frame, "gamma_"),
        "mu": numeric_columns(frame, "mu_"),
    }


def _validate_topic_dimensions(theta_columns, topic_columns, beta_columns, gamma_columns, mu_columns):
    """Validate that saved CAIMIRA topic-pyramidal dimensions line up."""
    dimensions = {
        len(theta_columns),
        len(topic_columns),
        len(beta_columns),
        len(gamma_columns),
        len(mu_columns),
    }
    if not theta_columns or len(dimensions) != 1:
        raise ValueError(
            "Saved theta, topic_weight, beta, gamma, and mu dimensions must be present and match"
        )


def _weighted_topic_difficulty(beta, gamma, mu, topic_weight, relative_positions):
    """Return sum_k r_k * beta_k * sigmoid(gamma_k * (mu_k - position))."""
    beta = np.asarray(beta, dtype=float)
    gamma = np.asarray(gamma, dtype=float)
    mu = np.asarray(mu, dtype=float)
    topic_weight = np.asarray(topic_weight, dtype=float)
    relative_positions = np.asarray(relative_positions, dtype=float)
    per_topic = beta[:, None] * _sigmoid(
        gamma[:, None] * (mu[:, None] - relative_positions[None, :])
    )
    return topic_weight @ per_topic


def _weighted_mu(tossup):
    """Return a topic-weighted average mu for plot annotation."""
    topic_columns = sorted(
        (
            column
            for column in tossup.index
            if column.startswith("topic_weight_")
            and column.removeprefix("topic_weight_").isdigit()
        ),
        key=lambda column: int(column.removeprefix("topic_weight_")),
    )
    mu_columns = sorted(
        (
            column
            for column in tossup.index
            if column.startswith("mu_") and column.removeprefix("mu_").isdigit()
        ),
        key=lambda column: int(column.removeprefix("mu_")),
    )
    if not topic_columns or len(topic_columns) != len(mu_columns):
        return None
    return float(
        np.dot(
            tossup[topic_columns].to_numpy(dtype=float),
            tossup[mu_columns].to_numpy(dtype=float),
        )
    )


def topic_first_buzz_distribution(event, players, tossups, n_bins=12):
    """Reconstruct first-buzz mass with CAIMIRA topic-gap saved parameters."""
    # Pull the saved parameters for this event's tossup and its roster of players.
    tossup_id = event["tossup_id"].iloc[0]
    tossup = tossups.loc[tossup_id]
    roster = players.loc[event["player_id"].astype(str)]
    theta_columns = numeric_columns(players, "theta_")
    topic_columns = numeric_columns(tossups, "topic_weight_")
    beta_columns = numeric_columns(tossups, "beta_")
    gamma_columns = numeric_columns(tossups, "gamma_")
    mu_columns = numeric_columns(tossups, "mu_")
    _validate_topic_dimensions(
        theta_columns, topic_columns, beta_columns, gamma_columns, mu_columns
    )

    # Difficulty curve evaluated at each relative token position.
    total_tokens = int(event["T_j"].iloc[0])
    positions = np.arange(1, total_tokens + 1, dtype=float)
    relative = positions / total_tokens
    topic_weight = tossup[topic_columns].to_numpy(dtype=float)
    difficulty = _weighted_topic_difficulty(
        tossup[beta_columns].to_numpy(dtype=float),
        tossup[gamma_columns].to_numpy(dtype=float),
        tossup[mu_columns].to_numpy(dtype=float),
        topic_weight,
        relative,
    )
    # Per-player buzz hazard = topic-weighted skill - weighted difficulty - threshold.
    skill = roster[theta_columns].to_numpy(dtype=float) @ topic_weight
    logits = (
        skill[:, None]
        - difficulty[None, :]
        - roster["c"].to_numpy(dtype=float)[:, None]
    )
    hazard = inverse_logit(logits)
    # Combine independent player hazards into team first-buzz mass per token + dead mass.
    team_hazard = 1.0 - np.prod(1.0 - hazard, axis=0)
    survival_before = np.concatenate(([1.0], np.cumprod(1.0 - team_hazard[:-1])))
    first_buzz_mass = survival_before * team_hazard
    dead_mass = float(np.prod(1.0 - team_hazard))

    # Bin the first-buzz mass across the question into n_bins by relative position.
    bin_index = np.clip((relative * n_bins).astype(int), 0, n_bins - 1)
    binned_mass = np.zeros(n_bins)
    np.add.at(binned_mass, bin_index, first_buzz_mass)
    return binned_mass, dead_mass


def topic_difficulty_plot(results_dir, output_dir):
    """Plot effective topic-weighted difficulty curves over empirical buzz locations."""
    parameters = pd.read_csv(results_dir / "tossups.csv").set_index("tossup_id")
    predictions = pd.read_csv(results_dir / "tossup_predictions.csv")
    selected = [
        tossup_id
        for tossup_id in selected_tossups(predictions)
        if tossup_id in parameters.index
    ]
    if not selected:
        return
    columns = _topic_columns(parameters)
    _validate_topic_dimensions(
        columns["topic_weight"],
        columns["topic_weight"],
        columns["beta"],
        columns["gamma"],
        columns["mu"],
    )

    positions = np.linspace(0.0, 1.0, 100)
    plot_columns = 2
    rows = math.ceil(len(selected) / plot_columns)
    fig, axes = plt.subplots(rows, plot_columns, figsize=(12, 3.7 * rows), squeeze=False)
    for ax, tossup_id in zip(axes.flat, selected):
        row = parameters.loc[tossup_id]
        difficulty = _weighted_topic_difficulty(
            row[columns["beta"]].to_numpy(dtype=float),
            row[columns["gamma"]].to_numpy(dtype=float),
            row[columns["mu"]].to_numpy(dtype=float),
            row[columns["topic_weight"]].to_numpy(dtype=float),
            positions,
        )
        buzz_positions = predictions.loc[
            (predictions["tossup_id"] == tossup_id) & (predictions["z"] == "BUZZ"),
            "relative_position",
        ]
        ax.hist(
            buzz_positions,
            bins=np.linspace(0, 1, 11),
            color="tab:orange",
            alpha=0.25,
            label=f"Observed buzzes (n={len(buzz_positions)})",
        )
        curve_ax = ax.twinx()
        curve_ax.plot(
            positions,
            difficulty,
            color="tab:blue",
            linewidth=2,
            label="Weighted difficulty",
        )
        ax.set(
            title=short_id(tossup_id),
            xlabel="Relative position",
            ylabel="Buzz count",
            xlim=(0, 1),
        )
        curve_ax.set_ylabel("Estimated weighted difficulty")
        ax.grid(alpha=0.2)
        handles, labels = ax.get_legend_handles_labels()
        curve_handles, curve_labels = curve_ax.get_legend_handles_labels()
        ax.legend(
            handles + curve_handles,
            labels + curve_labels,
            fontsize=7,
            loc="upper right",
        )
    for ax in axes.flat[len(selected):]:
        ax.set_visible(False)
    fig.suptitle("Estimated topic-weighted difficulty and empirical buzz locations")
    fig.tight_layout()
    fig.savefig(output_dir / "tossup_difficulty_curves.png", dpi=160)
    plt.close(fig)


def _topic_difficulty_curve_distribution_plot(tossups, output_dir):
    """Plot percentile bands for effective topic-weighted difficulty curves."""
    columns = _topic_columns(tossups)
    if not columns["topic_weight"]:
        return
    _validate_topic_dimensions(
        columns["topic_weight"],
        columns["topic_weight"],
        columns["beta"],
        columns["gamma"],
        columns["mu"],
    )
    positions = np.linspace(0, 1, 150)
    beta = tossups[columns["beta"]].to_numpy(dtype=float)[:, :, None]
    gamma = tossups[columns["gamma"]].to_numpy(dtype=float)[:, :, None]
    mu = tossups[columns["mu"]].to_numpy(dtype=float)[:, :, None]
    topic_weight = tossups[columns["topic_weight"]].to_numpy(dtype=float)[:, :, None]
    per_topic = beta * _sigmoid(gamma * (mu - positions[None, None, :]))
    curves = (topic_weight * per_topic).sum(axis=1)
    percentiles = np.percentile(curves, [5, 25, 50, 75, 95], axis=0)
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.fill_between(
        positions,
        percentiles[0],
        percentiles[4],
        alpha=0.15,
        label="5th-95th percentile",
    )
    ax.fill_between(
        positions,
        percentiles[1],
        percentiles[3],
        alpha=0.3,
        label="25th-75th percentile",
    )
    ax.plot(positions, percentiles[2], linewidth=2, label="Median weighted difficulty")
    ax.set(
        title="Distribution of learned topic-weighted difficulty curves",
        xlabel="Relative question position",
        ylabel="Estimated weighted difficulty",
        xlim=(0, 1),
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(output_dir / "pyramidal_difficulty_curve_distribution.png", dpi=160)
    plt.close(fig)


def _positive_log_series(frame, columns, dimension_labels=None):
    """Return labeled log10 series for positive-valued columns."""
    series = {}
    for label, values in labeled_series(frame, columns, dimension_labels).items():
        positive = values[values > 0]
        series[label] = np.log10(positive)
    return series


def topic_pyramidal_parameter_distribution_plots(
    results_dir, output_dir, dimension_labels=None
):
    """Plot saved CAIMIRA topic-pyramidal parameter distributions."""
    player_path = results_dir / "players.csv"
    tossup_path = results_dir / "tossups.csv"
    if not player_path.exists() or not tossup_path.exists():
        return
    players = pd.read_csv(player_path)
    tossups = pd.read_csv(tossup_path)
    theta_columns = numeric_columns(players, "theta_")
    beta_columns = numeric_columns(tossups, "beta_")
    gamma_columns = numeric_columns(tossups, "gamma_")
    mu_columns = numeric_columns(tossups, "mu_")
    topic_columns = numeric_columns(tossups, "topic_weight_")

    if "theta_norm" not in players and theta_columns:
        players["theta_norm"] = np.linalg.norm(
            players[theta_columns].to_numpy(dtype=float), axis=1
        )

    player_panels = []
    if "c" in players:
        player_panels.append(
            {
                "series": {"c": players["c"]},
                "title": "Confidence threshold",
                "xlabel": "c",
                "zero_line": True,
                "bounds": None,
            }
        )
    if theta_columns:
        player_panels.append(
            {
                "series": labeled_series(players, theta_columns, dimension_labels),
                "title": "Skill coordinates",
                "xlabel": "theta",
                "zero_line": True,
                "bounds": None,
            }
        )
    if "theta_norm" in players:
        player_panels.append(
            {
                "series": {"theta_norm": players["theta_norm"]},
                "title": "Skill magnitude",
                "xlabel": "theta norm",
                "zero_line": False,
                "bounds": (0, None),
            }
        )
    if player_panels:
        distribution_dashboard(
            player_panels,
            "Topic-pyramidal player parameter distributions",
            output_dir / "pyramidal_player_parameter_distributions.png",
        )

    tossup_panels = []
    if beta_columns:
        tossup_panels.append(
            {
                "series": labeled_series(tossups, beta_columns, dimension_labels),
                "title": "Per-topic difficulty amplitudes",
                "xlabel": "beta",
                "zero_line": True,
                "bounds": None,
            }
        )
    if gamma_columns:
        tossup_panels.append(
            {
                "series": _positive_log_series(
                    tossups, gamma_columns, dimension_labels
                ),
                "title": "Per-topic difficulty sharpness",
                "xlabel": "log10(gamma)",
                "zero_line": True,
                "bounds": None,
            }
        )
    if mu_columns:
        tossup_panels.append(
            {
                "series": labeled_series(tossups, mu_columns, dimension_labels),
                "title": "Per-topic difficulty transition locations",
                "xlabel": "relative position mu",
                "zero_line": False,
                "bounds": (0, 1),
            }
        )
    if topic_columns:
        tossup_panels.append(
            {
                "series": labeled_series(tossups, topic_columns, dimension_labels),
                "title": "Fixed topic weights",
                "xlabel": "topic weight",
                "zero_line": False,
                "bounds": (0, 1),
            }
        )
    if tossup_panels:
        distribution_dashboard(
            tossup_panels,
            "Topic-pyramidal tossup parameter distributions",
            output_dir / "pyramidal_tossup_parameter_distributions.png",
        )

    _topic_difficulty_curve_distribution_plot(tossups, output_dir)

    rows = []
    for group, frame, columns in (
        ("player", players, ["c", *theta_columns, "theta_norm"]),
        ("tossup", tossups, [*beta_columns, *gamma_columns, *mu_columns, *topic_columns]),
    ):
        for column in columns:
            if column in frame:
                summary = distribution_summary(group, column, frame[column])
                if summary:
                    rows.append(summary)
    pd.DataFrame(rows).to_csv(
        output_dir / "pyramidal_parameter_distribution_summary.csv", index=False
    )


def _aggregate_topic_buzz_timing(predictions, players, tossups, tossup_id, n_bins):
    """Average fitted and empirical first-buzz mass over one tossup's events."""
    predicted = np.zeros(n_bins)
    observed = np.zeros(n_bins)
    predicted_dead = 0.0
    observed_dead = 0
    event_count = 0
    # Accumulate fitted vs observed first-buzz mass across this tossup's events.
    for _, event in predictions[predictions["tossup_id"] == tossup_id].groupby(
        "event_id"
    ):
        # Skip events whose players are missing from the saved players table.
        if not set(event["player_id"]).issubset(players.index):
            continue
        fitted_mass, fitted_dead = topic_first_buzz_distribution(
            event, players, tossups, n_bins
        )
        predicted += fitted_mass
        predicted_dead += fitted_dead
        # Tally the observed buzz bin, or count a dead (no-buzz) event.
        buzz = event[event["z"] == "BUZZ"]
        if buzz.empty:
            observed_dead += 1
        else:
            index = min(
                int(float(buzz["relative_position"].iloc[0]) * n_bins), n_bins - 1
            )
            observed[index] += 1
        event_count += 1
    if event_count == 0:
        return None
    # Average masses per event.
    predicted /= event_count
    predicted_dead /= event_count
    observed /= event_count
    observed_dead_rate = observed_dead / event_count
    # Total-variation distance between predicted and observed timing.
    total_variation = 0.5 * (
        np.abs(predicted - observed).sum() + abs(predicted_dead - observed_dead_rate)
    )
    return {
        "event_count": event_count,
        "predicted": predicted,
        "observed": observed,
        "predicted_dead": predicted_dead,
        "observed_dead_rate": observed_dead_rate,
        "total_variation": total_variation,
    }


def topic_buzz_density_fit_plot(results_dir, output_dir, n_bins=12):
    """Compare empirical and topic-weighted fitted first-buzz timing."""
    # Need players, tossups, and predictions on disk to draw the timing fit.
    required = [
        results_dir / "players.csv",
        results_dir / "tossups.csv",
        results_dir / "tossup_predictions.csv",
    ]
    if not all(path.exists() for path in required):
        return
    # Load the saved tables indexed by their id columns.
    players = pd.read_csv(required[0], dtype={"player_id": str}).set_index("player_id")
    tossups = pd.read_csv(required[1], dtype={"tossup_id": str}).set_index("tossup_id")
    predictions = pd.read_csv(required[2], dtype={"player_id": str, "tossup_id": str})
    if "c" not in players or predictions.empty:
        return

    # Pick representative tossups that are present in the saved tossups table.
    selected = [item for item in selected_tossups(predictions) if item in tossups.index]
    if not selected:
        return
    # Subplot grid: 2 columns, one panel per selected tossup.
    columns = 2
    rows = math.ceil(len(selected) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(12, 3.8 * rows), squeeze=False)
    centers = (np.arange(n_bins) + 0.5) / n_bins
    summaries = []
    for ax, tossup_id in zip(axes.flat, selected):
        timing = _aggregate_topic_buzz_timing(
            predictions, players, tossups, tossup_id, n_bins
        )
        if timing is None:
            ax.set_visible(False)
            continue
        summaries.append(
            {
                "tossup_id": tossup_id,
                "events": timing["event_count"],
                "observed_dead_rate": timing["observed_dead_rate"],
                "predicted_dead_rate": timing["predicted_dead"],
                "timing_total_variation": timing["total_variation"],
            }
        )
        # Empirical mass as bars, fitted mass as a line, difficulty inflection mu as a rule.
        ax.bar(
            centers,
            timing["observed"],
            width=0.8 / n_bins,
            alpha=0.35,
            color="tab:orange",
            label="Empirical mass",
        )
        ax.plot(
            centers,
            timing["predicted"],
            "o-",
            color="tab:blue",
            label="Predicted mass",
        )
        weighted_mu = _weighted_mu(tossups.loc[tossup_id])
        if weighted_mu is not None:
            ax.axvline(
                weighted_mu,
                color="tab:green",
                linestyle="--",
                linewidth=1.5,
                label=f"Weighted $\\mu$={weighted_mu:.2f}",
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
            f"events={timing['event_count']}\n"
            f"dead: observed={timing['observed_dead_rate']:.2f}, "
            f"predicted={timing['predicted_dead']:.2f}\n"
            f"TV distance={timing['total_variation']:.2f}",
            transform=ax.transAxes,
            va="top",
            fontsize=8,
        )
        ax.grid(alpha=0.2)
        ax.legend(fontsize=7, loc="upper right")
    # Hide any leftover axes, then save the figure and per-tossup metrics CSV.
    for ax in axes.flat[len(selected):]:
        ax.set_visible(False)
    fig.suptitle("Predicted versus empirical first-buzz timing")
    fig.tight_layout()
    fig.savefig(output_dir / "tossup_buzz_density_fit.png", dpi=160)
    plt.close(fig)
    pd.DataFrame(summaries).to_csv(
        output_dir / "tossup_buzz_density_metrics.csv", index=False
    )


def evaluate_topic_tossups(results_dir: Path, output_dir: Path, dimension_labels=None):
    """Evaluate topic-weighted tossup correctness and first-buzz timing."""
    # Correctness is scored only on rows that were actual buzzes.
    buzz = pd.read_csv(results_dir / "tossup_predictions.csv")
    buzz = buzz[buzz["z"] == "BUZZ"]
    metrics = classification_metrics(buzz["y"], buzz["predicted_correct"])
    # Reliability, difficulty, topic-weighted density, and parameter-distribution plots.
    if not buzz.empty:
        reliability_plot(
            buzz["y"],
            buzz["predicted_correct"],
            "Tossup correctness reliability",
            output_dir / "tossup_reliability.png",
        )
        stratified_tossup_reliability_plot(buzz, output_dir)
    topic_difficulty_plot(results_dir, output_dir)
    topic_buzz_density_fit_plot(results_dir, output_dir)
    topic_pyramidal_parameter_distribution_plots(
        results_dir, output_dir, dimension_labels
    )

    # If event-level positions exist, add buzz-position errors and an observed/predicted scatter.
    position_path = results_dir / "buzz_event_predictions.csv"
    if position_path.exists():
        events = pd.read_csv(position_path)
        metrics.update(
            {
                "buzz_position_mae": mean_absolute_error(
                    events["observed_relative_position"],
                    events["predicted_relative_position"],
                ),
                "buzz_position_median_absolute_error": median_absolute_error(
                    events["observed_relative_position"],
                    events["predicted_relative_position"],
                ),
            }
        )
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.scatter(
            events["observed_relative_position"],
            events["predicted_relative_position"],
            alpha=0.25,
        )
        ax.plot([0, 1], [0, 1], "--", color="0.5")
        ax.set(
            title="Observed versus predicted buzz position",
            xlabel="Observed",
            ylabel="Predicted",
            xlim=(0, 1),
            ylim=(0, 1),
        )
        ax.grid(alpha=0.25)
        fig.tight_layout()
        fig.savefig(output_dir / "tossup_position_predictions.png", dpi=160)
        plt.close(fig)
    return metrics


def evaluate_topic_compirt(
    pyramidal_results: Path,
    compositional_results: Path,
    output_dir: Path,
    comparison_pyramidal_results: Path | None = None,
    dimension_labels=None,
):
    """Write topic-weighted metrics, plots, and Markdown report.

    'dimension_labels' optionally maps each 1-based latent dimension to a name
    (e.g. a topic/category), used to relabel topic-coordinate legends in the
    parameter-distribution figures.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    # Evaluate the tossup and bonus stages; optionally compare skills to a baseline run.
    tossup = evaluate_topic_tossups(pyramidal_results, output_dir, dimension_labels)
    bonus = evaluate_bonuses(compositional_results, output_dir, dimension_labels)
    if comparison_pyramidal_results:
        player_skill_stability_plot(
            pyramidal_results,
            comparison_pyramidal_results,
            output_dir,
        )
    # Persist the metric tables and a Markdown experiment report.
    pd.DataFrame([tossup]).to_csv(output_dir / "tossup_metrics.csv", index=False)
    pd.DataFrame([bonus]).to_csv(output_dir / "bonus_metrics.csv", index=False)
    report = (
        "# Topic-Weighted CompIRT Experiment Report\n\n"
        "## Tossup Metrics\n\n"
        + pd.DataFrame([tossup]).to_markdown(index=False)
        + "\n\n## Bonus Metrics\n\n"
        + pd.DataFrame([bonus]).to_markdown(index=False)
        + "\n\nGenerated figures match the standard CompIRT evaluation set. "
        "The first-buzz timing replay uses the CAIMIRA topic-gap formula "
        "`sum_k r_jk * (theta_ik - d_jk(t))`.\n"
    )
    (output_dir / "experiment_report.md").write_text(report, encoding="utf-8")
    return tossup, bonus
