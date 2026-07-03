"""Plot learned difficulty curves against empirical first-buzz locations.

Picks a handful of tossups spanning the observed range of buzz timing and
overlays each one's fitted difficulty curve (Eq. 3) on a histogram of where
players actually buzzed, as a visual sanity check that harder-difficulty
curves line up with later empirical buzzes. 'difficulty_plot' renders the
single effective curve; 'multidim_difficulty_components_plot' additionally
breaks a multidimensional fit down into its per-skill-dimension components.
"""

from __future__ import annotations

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.figures import short_id
from compirt_eval.outputs import graph_path
from compirt_eval.tossups.parameters import (
    _multidim_difficulty_components,
    _parameter_columns,
    _saved_difficulty_curve,
    _validate_tossup_multidim_dimensions,
    difficulty_adjustment_at,
    load_difficulty_adjustment_curves,
)


def tossup_observation_summary(predictions):
    """Summarize event frequency and empirical buzz timing by tossup."""
    summary = (
        predictions.assign(is_buzz=predictions["z"] == "BUZZ")
        .groupby("tossup_id")
        .agg(
            events=("event_id", "nunique"),
            buzzes=("is_buzz", "sum"),
        )
    )
    mean_position = (
        predictions[predictions["z"] == "BUZZ"]
        .groupby("tossup_id")["relative_position"]
        .mean()
        .rename("mean_buzz_position")
    )
    return summary.join(mean_position)


def evenly_spaced_ids(frame, sort_column, count=6):
    """Select IDs across the range of a diagnostic variable."""
    if frame.empty:
        return []
    frame = frame.sort_values(sort_column)
    if len(frame) <= count:
        return frame.index.tolist()
    positions = np.linspace(0, len(frame) - 1, count).round().astype(int)
    return frame.iloc[np.unique(positions)].index.tolist()


def selected_tossups(predictions, count=6):
    """Choose frequently observed tossups across the empirical timing range."""
    summary = tossup_observation_summary(predictions)
    minimum_events = summary["events"].quantile(0.75)
    frequent = summary[summary["events"] >= minimum_events].copy()
    frequent["mean_buzz_position"] = frequent["mean_buzz_position"].fillna(1.0)
    return evenly_spaced_ids(frequent, "mean_buzz_position", count)


def difficulty_plot(results_dir, output_dir):
    """Plot learned difficulty curves over empirical first-buzz locations.

    When the run saved TF-IDF adjustment curves, the plotted difficulty is the
    effective 'd'_j(t) = d_j(t) - A_j(t)' the model actually used, with the
    base sigmoid kept as a dashed reference.
    """
    parameters = pd.read_csv(results_dir / "tossups.csv").set_index("tossup_id")
    predictions = pd.read_csv(results_dir / "tossup_predictions.csv")
    adjustments = load_difficulty_adjustment_curves(results_dir)
    positions = np.linspace(0.0, 1.0, 200)
    selected = [
        tossup_id
        for tossup_id in selected_tossups(predictions)
        if tossup_id in parameters.index
        and _saved_difficulty_curve(parameters.loc[tossup_id], positions) is not None
    ]

    if not selected:
        return
    columns = 2
    rows = math.ceil(len(selected) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(12, 3.7 * rows), squeeze=False)
    for ax, tossup_id in zip(axes.flat, selected):
        row = parameters.loc[tossup_id]
        difficulty = _saved_difficulty_curve(row, positions)
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
        adjustment = difficulty_adjustment_at(adjustments, tossup_id, positions)
        if adjustment is not None:
            curve_ax.plot(
                positions,
                difficulty,
                color="tab:blue",
                linewidth=1.3,
                linestyle="--",
                alpha=0.65,
                label="Base difficulty d(t)",
            )
            curve_ax.plot(
                positions,
                difficulty - adjustment,
                color="black",
                linewidth=2,
                label="Effective difficulty d'(t)",
            )
        else:
            curve_ax.plot(
                positions,
                difficulty,
                color="tab:blue",
                linewidth=2,
                label="Difficulty",
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
        ax.legend(
            handles + curve_handles,
            labels + curve_labels,
            fontsize=7,
            loc="upper right",
        )
    for ax in axes.flat[len(selected):]:
        ax.set_visible(False)
    fig.suptitle("Estimated tossup difficulty and empirical buzz locations")
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, "tossup_difficulty_curves.png"), dpi=160)
    plt.close(fig)


def _multidim_curve_label(alpha_column, alpha_value):
    """Return a readable label for one multidim difficulty coordinate."""
    dimension = int(alpha_column.removeprefix("alpha_"))
    return f"Dimension {dimension} (alpha={alpha_value:.2f})"


def multidim_difficulty_components_plot(results_dir, output_dir):
    """Plot every per-dimension difficulty curve plus alpha-weighted difficulty."""
    required = [
        results_dir / "tossups.csv",
        results_dir / "tossup_predictions.csv",
    ]
    if not all(path.exists() for path in required):
        return
    parameters = pd.read_csv(required[0]).set_index("tossup_id")
    predictions = pd.read_csv(required[1])
    columns = _parameter_columns(parameters)
    if not all(columns[name] for name in ("alpha", "beta", "gamma", "mu")):
        return
    _validate_tossup_multidim_dimensions(
        columns["alpha"], columns["beta"], columns["gamma"], columns["mu"]
    )

    selected = [
        tossup_id
        for tossup_id in selected_tossups(predictions)
        if tossup_id in parameters.index
    ]
    if not selected:
        return

    positions = np.linspace(0.0, 1.0, 100)
    plot_columns = 2
    rows = math.ceil(len(selected) / plot_columns)
    fig, axes = plt.subplots(rows, plot_columns, figsize=(12, 4.2 * rows), squeeze=False)
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    for ax, tossup_id in zip(axes.flat, selected):
        row = parameters.loc[tossup_id]
        per_dimension, difficulty = _multidim_difficulty_components(
            row, columns, positions
        )
        alpha = row[columns["alpha"]].to_numpy(dtype=float)
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
        for index, (alpha_column, alpha_value) in enumerate(
            zip(columns["alpha"], alpha)
        ):
            curve_ax.plot(
                positions,
                per_dimension[index],
                color=colors[index % len(colors)],
                linewidth=1.1,
                alpha=0.75,
                label=_multidim_curve_label(alpha_column, alpha_value),
            )
        curve_ax.plot(
            positions,
            difficulty,
            color="black",
            linewidth=3,
            label="Alpha-weighted difficulty",
            zorder=10,
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
    fig.suptitle("Per-dimension difficulty curves and alpha-weighted difficulty")
    fig.tight_layout()
    fig.savefig(
        graph_path(output_dir, "tossup_difficulty_curves_by_dimension.png"), dpi=160
    )
    plt.close(fig)
