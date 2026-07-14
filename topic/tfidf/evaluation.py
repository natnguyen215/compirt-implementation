"""Evaluation replay for the dedicated topic-specific TF-IDF experiment.

The baseline topic evaluator is reused for its common metrics, bonus reports,
and parameter dashboards. This module supplies the two text-conditioned pieces
that baseline runs do not need: effective-difficulty curves and first-buzz
timing reconstructed from saved aggregate TF-IDF adjustments.
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.figures import numeric_columns, short_id
from compirt_eval.metrics import inverse_logit
from compirt_eval.outputs import graph_path
from compirt_eval.tossups import selected_tossups
from compirt_eval.tossups.parameters import (
    difficulty_adjustment_at,
    load_difficulty_adjustment_curves,
)
from topic.fixed.topic_compirt import evaluation as base_evaluation
from topic.tfidf.outputs import TOPIC_TFIDF_LAMBDAS_FILENAME


def topic_first_buzz_distribution(event, players, tossups, adjustments, n_bins=12):
    """Reconstruct first-buzz mass using saved TF-IDF-adjusted difficulty.

    Same math as the baseline 'topic_first_buzz_distribution', except the saved
    signed adjustment is interpolated onto each token and added to the weighted
    difficulty before hazards are formed.
    """
    tossup_id = event["tossup_id"].iloc[0]
    tossup = tossups.loc[tossup_id]
    roster = players.loc[event["player_id"].astype(str)]
    theta_columns = numeric_columns(players, "theta_")
    topic_columns = numeric_columns(tossups, "topic_weight_")
    beta_columns = numeric_columns(tossups, "beta_")
    gamma_columns = numeric_columns(tossups, "gamma_")
    mu_columns = numeric_columns(tossups, "mu_")
    base_evaluation._validate_topic_dimensions(
        theta_columns, topic_columns, beta_columns, gamma_columns, mu_columns
    )

    total_tokens = int(event["T_j"].iloc[0])
    positions = np.arange(1, total_tokens + 1, dtype=float)
    relative = positions / total_tokens
    topic_weight = tossup[topic_columns].to_numpy(dtype=float)
    difficulty = base_evaluation._weighted_topic_difficulty(
        tossup[beta_columns].to_numpy(dtype=float),
        tossup[gamma_columns].to_numpy(dtype=float),
        tossup[mu_columns].to_numpy(dtype=float),
        topic_weight,
        relative,
    )
    adjustment = difficulty_adjustment_at(adjustments, tossup_id, relative)
    if adjustment is not None:
        difficulty = difficulty + adjustment
    # Per-player buzz hazard = topic-weighted skill - adjusted difficulty - c.
    skill = roster[theta_columns].to_numpy(dtype=float) @ topic_weight
    logits = (
        skill[:, None]
        - difficulty[None, :]
        - roster["c"].to_numpy(dtype=float)[:, None]
    )
    hazard = inverse_logit(logits)
    # Combine independent player hazards into team first-buzz mass + dead mass.
    team_hazard = 1.0 - np.prod(1.0 - hazard, axis=0)
    survival_before = np.concatenate(([1.0], np.cumprod(1.0 - team_hazard[:-1])))
    first_buzz_mass = survival_before * team_hazard
    dead_mass = float(np.prod(1.0 - team_hazard))
    bin_index = np.clip((relative * n_bins).astype(int), 0, n_bins - 1)
    binned_mass = np.zeros(n_bins)
    np.add.at(binned_mass, bin_index, first_buzz_mass)
    return binned_mass, dead_mass


def topic_difficulty_plot(results_dir, output_dir, adjustments):
    """Plot TF-IDF-adjusted weighted difficulty over observed buzz positions."""
    parameters = pd.read_csv(results_dir / "tossups.csv").set_index("tossup_id")
    predictions = pd.read_csv(results_dir / "tossup_predictions.csv")
    selected = [
        tossup_id
        for tossup_id in selected_tossups(predictions)
        if tossup_id in parameters.index
    ]
    if not selected:
        return
    columns = base_evaluation._topic_columns(parameters)
    # _validate_topic_dimensions' first argument is normally theta_columns, but
    # this plot only needs tossup-level columns to line up, so topic_weight is
    # passed again in that slot rather than reading player theta columns.
    base_evaluation._validate_topic_dimensions(
        columns["topic_weight"],
        columns["topic_weight"],
        columns["beta"],
        columns["gamma"],
        columns["mu"],
    )
    positions = np.linspace(0.0, 1.0, 100)
    plot_columns = 2
    rows = math.ceil(len(selected) / plot_columns)
    fig, axes = plt.subplots(
        rows, plot_columns, figsize=(12, 3.7 * rows), squeeze=False
    )
    for axis, tossup_id in zip(axes.flat, selected):
        row = parameters.loc[tossup_id]
        difficulty = base_evaluation._weighted_topic_difficulty(
            row[columns["beta"]].to_numpy(dtype=float),
            row[columns["gamma"]].to_numpy(dtype=float),
            row[columns["mu"]].to_numpy(dtype=float),
            row[columns["topic_weight"]].to_numpy(dtype=float),
            positions,
        )
        adjustment = difficulty_adjustment_at(adjustments, tossup_id, positions)
        if adjustment is not None:
            difficulty = difficulty + adjustment
        buzz_positions = predictions.loc[
            (predictions["tossup_id"] == tossup_id) & (predictions["z"] == "BUZZ"),
            "relative_position",
        ]
        axis.hist(
            buzz_positions,
            bins=np.linspace(0, 1, 11),
            color="tab:orange",
            alpha=0.25,
            label=f"Observed buzzes (n={len(buzz_positions)})",
        )
        curve_axis = axis.twinx()
        curve_axis.plot(
            positions,
            difficulty,
            color="tab:blue",
            linewidth=2,
            label="TF-IDF-adjusted weighted difficulty",
        )
        axis.set(
            title=short_id(tossup_id),
            xlabel="Relative position",
            ylabel="Buzz count",
            xlim=(0, 1),
        )
        curve_axis.set_ylabel("Estimated weighted difficulty")
        axis.grid(alpha=0.2)
        # The buzz histogram and difficulty curve live on separate twinx axes,
        # so merge their legend handles into one box drawn on the base axis.
        handles, labels = axis.get_legend_handles_labels()
        curve_handles, curve_labels = curve_axis.get_legend_handles_labels()
        axis.legend(
            handles + curve_handles,
            labels + curve_labels,
            fontsize=7,
            loc="upper right",
        )
    for axis in axes.flat[len(selected):]:
        axis.set_visible(False)
    fig.suptitle("TF-IDF-adjusted topic-weighted difficulty and empirical buzzes")
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, "tossup_difficulty_curves.png"), dpi=160)
    plt.close(fig)


def load_topic_lambdas(results_dir):
    """Return the fitted per-topic lambda vector, ordered by topic dimension."""
    path = results_dir / TOPIC_TFIDF_LAMBDAS_FILENAME
    if not path.exists():
        return None
    lambdas = pd.read_csv(path).sort_values("topic_dimension")
    return lambdas["lambda_tfidf"].to_numpy(dtype=float)


def tfidf_prefix_at(adjustments, tossup_id, positions, topic_weight, lambdas):
    """Recover this tossup's cumulative TF-IDF prefix mass from saved outputs.

    ``save_adjustment_curves`` stores only the aggregate signed adjustment
    ``-tfidf_prefix_j(t) * sum_k r_jk * lambda_k``. Since ``r_j`` (tossups.csv)
    and ``lambda`` (topic_tfidf_lambdas.csv) are both saved, dividing the
    aggregate back out by the topic-weighted lambda recovers ``tfidf_prefix_j(t)``
    itself -- which is what lets each topic's own adjusted curve be drawn without
    reconstructing the text corpus. A tossup whose weighted lambda is ~0 gets no
    adjustment to invert, so its prefix is reported as absent.
    """
    adjustment = difficulty_adjustment_at(adjustments, tossup_id, positions)
    if adjustment is None:
        return None
    weighted_lambda = float(topic_weight @ lambdas)
    if abs(weighted_lambda) <= 1e-8:
        return None
    return -adjustment / weighted_lambda


def topic_difficulty_components_plot(
    results_dir, output_dir, adjustments, dimension_labels=None
):
    """Per-topic curves + weighted difficulty, both raw and TF-IDF-adjusted.

    Mirrors the baseline ``topic_difficulty_components_plot``, but each topic's
    curve is drawn twice: solid for the raw difficulty ``d_jk(t)`` and dashed for
    the TF-IDF-adjusted ``d_jk(t) - lambda_k * tfidf_prefix_j(t)``. The heavy
    black pair is the topic-weighted aggregate of each. Because the per-topic
    adjustments weight up to the saved aggregate, the dashed black curve equals
    the raw weighted curve plus the saved signed adjustment -- the same effective
    difficulty the timing replay uses.
    """
    parameters = pd.read_csv(results_dir / "tossups.csv").set_index("tossup_id")
    predictions = pd.read_csv(results_dir / "tossup_predictions.csv")
    selected = [
        tossup_id
        for tossup_id in selected_tossups(predictions)
        if tossup_id in parameters.index
    ]
    if not selected:
        return
    columns = base_evaluation._topic_columns(parameters)
    base_evaluation._validate_topic_dimensions(
        columns["topic_weight"],
        columns["topic_weight"],
        columns["beta"],
        columns["gamma"],
        columns["mu"],
    )

    lambdas = load_topic_lambdas(results_dir)
    if lambdas is not None and len(lambdas) != len(columns["topic_weight"]):
        raise ValueError(
            f"{TOPIC_TFIDF_LAMBDAS_FILENAME} has {len(lambdas)} lambdas but "
            f"tossups.csv has {len(columns['topic_weight'])} topic dimensions"
        )

    positions = np.linspace(0.0, 1.0, 100)
    plot_columns = 2
    rows = math.ceil(len(selected) / plot_columns)
    fig, axes = plt.subplots(
        rows, plot_columns, figsize=(12, 4.2 * rows), squeeze=False
    )
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    for ax, tossup_id in zip(axes.flat, selected):
        row = parameters.loc[tossup_id]
        topic_weight = row[columns["topic_weight"]].to_numpy(dtype=float)
        per_topic, difficulty = base_evaluation._topic_difficulty_components(
            row[columns["beta"]].to_numpy(dtype=float),
            row[columns["gamma"]].to_numpy(dtype=float),
            row[columns["mu"]].to_numpy(dtype=float),
            topic_weight,
            positions,
        )
        prefix = None
        if lambdas is not None:
            prefix = tfidf_prefix_at(
                adjustments, tossup_id, positions, topic_weight, lambdas
            )
        # Each topic's curve is lowered by its own lambda times the shared prefix.
        adjusted_per_topic = (
            per_topic - lambdas[:, None] * prefix[None, :]
            if prefix is not None
            else None
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
        for index, (topic_column, weight) in enumerate(
            zip(columns["topic_weight"], topic_weight)
        ):
            color = colors[index % len(colors)]
            curve_ax.plot(
                positions,
                per_topic[index],
                color=color,
                linewidth=1.1,
                alpha=0.75,
                label=base_evaluation._topic_curve_label(
                    topic_column, weight, dimension_labels
                ),
            )
            if adjusted_per_topic is not None:
                curve_ax.plot(
                    positions,
                    adjusted_per_topic[index],
                    color=color,
                    linestyle="--",
                    linewidth=1.1,
                    alpha=0.75,
                )
        curve_ax.plot(
            positions,
            difficulty,
            color="black",
            linewidth=3,
            label="Weighted difficulty",
            zorder=10,
        )
        if adjusted_per_topic is not None:
            curve_ax.plot(
                positions,
                topic_weight @ adjusted_per_topic,
                color="black",
                linestyle="--",
                linewidth=2.5,
                label="TF-IDF-adjusted (dashed = per topic)",
                zorder=11,
            )
        ax.set(
            title=short_id(tossup_id),
            xlabel="Relative position",
            ylabel="Buzz count",
            xlim=(0, 1),
        )
        curve_ax.set_ylabel("Estimated difficulty")
        ax.grid(alpha=0.2)
        handles, labels = ax.get_legend_handles_labels()
        curve_handles, curve_labels = curve_ax.get_legend_handles_labels()
        legend_handles = handles + curve_handles
        ax.legend(
            legend_handles,
            labels + curve_labels,
            fontsize=6,
            loc="upper right",
            ncol=2 if len(legend_handles) > 8 else 1,
        )
    for ax in axes.flat[len(selected):]:
        ax.set_visible(False)
    fig.suptitle(
        "Per-topic difficulty curves (solid = raw, dashed = TF-IDF-adjusted) "
        "and their weighted aggregate"
    )
    fig.tight_layout()
    fig.savefig(
        graph_path(output_dir, "tossup_difficulty_curves_by_topic.png"), dpi=160
    )
    plt.close(fig)


def _append_lambda_report(pyramidal_results, output_dir):
    """Append the fitted per-topic TF-IDF lambda table to the parameter report."""
    lambda_path = pyramidal_results / "topic_tfidf_lambdas.csv"
    if not lambda_path.exists():
        return
    lambdas = pd.read_csv(lambda_path)
    report_path = output_dir / "experiment_report.md"
    with report_path.open("a", encoding="utf-8") as handle:
        handle.write(
            "\n## TF-IDF Cumulative-Difficulty Lambdas\n\n"
            "One nonnegative `lambda_k` per topic coordinate scales the cumulative "
            "TF-IDF prefix mass that lowers effective difficulty "
            "(`d'_jk(t) = d_jk(t) - lambda_k * tfidf_prefix_j(t)`).\n\n"
            "| topic_dimension | topic_label | lambda_tfidf |\n"
            "| --- | --- | --- |\n"
        )
        for _, entry in lambdas.iterrows():
            handle.write(
                f"| {entry['topic_dimension']} | {entry['topic_label']} "
                f"| {float(entry['lambda_tfidf']):.6g} |\n"
            )


def evaluate_topic_tfidf(
    pyramidal_results: Path,
    compositional_results: Path,
    output_dir: Path,
    comparison_pyramidal_results: Path | None = None,
    dimension_labels=None,
):
    """Run full topic evaluation, replaying saved text-conditioned adjustments."""
    adjustments = load_difficulty_adjustment_curves(pyramidal_results)
    if adjustments is None:
        return base_evaluation.evaluate_topic_compirt(
            pyramidal_results,
            compositional_results,
            output_dir,
            comparison_pyramidal_results,
            dimension_labels,
        )

    # The baseline evaluator's aggregate timing routine resolves this global at
    # runtime. Temporarily substituting the TF-IDF replay keeps its plotting and
    # metric schema identical while supplying the dedicated difficulty curve.
    original_distribution = base_evaluation.topic_first_buzz_distribution

    def adjusted_distribution(event, players, tossups, n_bins=12):
        return topic_first_buzz_distribution(
            event, players, tossups, adjustments, n_bins
        )

    base_evaluation.topic_first_buzz_distribution = adjusted_distribution
    try:
        result = base_evaluation.evaluate_topic_compirt(
            pyramidal_results,
            compositional_results,
            output_dir,
            comparison_pyramidal_results,
            dimension_labels,
        )
    finally:
        base_evaluation.topic_first_buzz_distribution = original_distribution

    # Replace the baseline effective-difficulty view with the same adjusted
    # curve used for timing replay. Other baseline diagnostic panels remain
    # useful descriptions of the underlying topic parameters.
    topic_difficulty_plot(pyramidal_results, output_dir, adjustments)
    topic_difficulty_components_plot(
        pyramidal_results, output_dir, adjustments, dimension_labels
    )
    report_path = output_dir / "experiment_report.md"
    with report_path.open("a", encoding="utf-8") as handle:
        handle.write(
            "\nThe dedicated TF-IDF replay applies saved signed adjustments "
            "`-tfidf_prefix_j(t) * sum_k r_jk lambda_k` to both effective "
            "difficulty and first-buzz timing.\n"
        )
    _append_lambda_report(pyramidal_results, output_dir)
    return result
