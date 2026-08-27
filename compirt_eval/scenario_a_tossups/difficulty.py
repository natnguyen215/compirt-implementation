"""Plot learned correctness and hazard difficulty curves.

Picks a handful of tossups spanning the observed range of buzz timing and
overlays each fitted curve on a histogram of where players actually buzzed.
For double-difficulty runs the hazard curve is the buzz-timing diagnostic and
the correctness curve is shown separately for comparison. ``difficulty_plot``
renders effective curves; ``multidim_difficulty_components_plot`` also breaks
each family down into its per-skill-dimension components.
"""

from __future__ import annotations

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.common.figures import short_id, vector_weight_name
from compirt_eval.common.report_paths import graph_path
from compirt_eval.scenario_a_tossups.parameters import (
    _difficulty_parameter_columns,
    _has_saved_difficulty,
    _parameter_columns,
    _saved_difficulty_components,
    _saved_difficulty_curve,
    _validate_tossup_multidim_dimensions,
    _validate_monotone_dimensions,
    _validate_polynomial_dimensions,
    _validate_spline_dimensions,
    difficulty_adjustment_at,
    load_difficulty_adjustment_curves,
    load_difficulty_link,
    load_difficulty_scale,
)

DIFFICULTY_FAMILIES = (
    ("", "Correctness difficulty", "tossup_difficulty_curves"),
    ("hazard_", "Hazard difficulty", "tossup_hazard_difficulty_curves"),
)


def _saved_families(parameters):
    """Yield the canonical curve and an optional saved hazard curve."""
    for parameter_prefix, label, filename_stem in DIFFICULTY_FAMILIES:
        if not parameter_prefix or _has_saved_difficulty(
            parameters, parameter_prefix
        ):
            yield parameter_prefix, label, filename_stem


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


def _buzz_histogram_axes(ax, predictions, tossup_id):
    """Draw one tossup's observed buzz histogram and return a difficulty axis.

    Difficulty and buzz counts share an x axis but not a y scale, so the
    returned twin carries the curves.
    """
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
    return ax.twinx()


def _finish_curve_panel(ax, curve_ax, tossup_id, fontsize, family_label="Difficulty"):
    """Label one buzz/difficulty panel and merge both axes into one legend."""
    ax.set(
        title=short_id(tossup_id),
        xlabel="Relative position",
        ylabel="Buzz count",
        xlim=(0, 1),
    )
    curve_ax.set_ylabel(f"Estimated {family_label.lower()}")
    ax.grid(alpha=0.2)
    handles, labels = ax.get_legend_handles_labels()
    curve_handles, curve_labels = curve_ax.get_legend_handles_labels()
    handles += curve_handles
    ax.legend(
        handles,
        labels + curve_labels,
        fontsize=fontsize,
        loc="upper right",
        ncol=2 if len(handles) > 8 else 1,
    )


def difficulty_plot(results_dir, output_dir):
    """Plot correctness and, when saved, hazard difficulty curves.

    When the run saved TF-IDF adjustment curves, they are signed additive
    difficulty deltas, so the plotted curve is 'd'_j(t) = d_j(t) + delta_j(t)'.
    The base sigmoid is kept as a dashed reference.
    """
    parameters = pd.read_csv(results_dir / "tossups.csv").set_index("tossup_id")
    predictions = pd.read_csv(results_dir / "tossup_predictions.csv")
    adjustments = load_difficulty_adjustment_curves(results_dir)
    link = load_difficulty_link(results_dir)
    difficulty_scale = load_difficulty_scale(results_dir)
    for parameter_prefix, family_label, filename_stem in _saved_families(parameters):
        _difficulty_family_plot(
            parameters,
            predictions,
            output_dir,
            adjustments,
            link,
            difficulty_scale,
            parameter_prefix,
            family_label,
            f"{filename_stem}.png",
        )


def _difficulty_family_plot(
    parameters,
    predictions,
    output_dir,
    adjustments,
    link,
    difficulty_scale,
    parameter_prefix,
    family_label,
    filename,
):
    """Render one saved difficulty family over empirical buzz locations."""
    positions = np.linspace(0.0, 1.0, 200)
    selected = [
        tossup_id
        for tossup_id in selected_tossups(predictions)
        if tossup_id in parameters.index
        and _saved_difficulty_curve(
            parameters.loc[tossup_id],
            positions,
            link,
            difficulty_scale,
            parameter_prefix,
        ) is not None
    ]

    if not selected:
        return
    columns = 2
    rows = math.ceil(len(selected) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(12, 3.7 * rows), squeeze=False)
    for ax, tossup_id in zip(axes.flat, selected):
        row = parameters.loc[tossup_id]
        difficulty = _saved_difficulty_curve(
            row, positions, link, difficulty_scale, parameter_prefix
        )
        curve_ax = _buzz_histogram_axes(ax, predictions, tossup_id)
        adjustment = difficulty_adjustment_at(adjustments, tossup_id, positions)
        if adjustment is not None:
            curve_ax.plot(
                positions,
                difficulty,
                color="tab:blue",
                linewidth=1.3,
                linestyle="--",
                alpha=0.65,
                label=f"Base {family_label.lower()} d(t)",
            )
            curve_ax.plot(
                positions,
                difficulty + adjustment,
                color="black",
                linewidth=2,
                label=f"Effective {family_label.lower()} d'(t)",
            )
        else:
            curve_ax.plot(
                positions,
                difficulty,
                color="tab:blue",
                linewidth=2,
                label=family_label,
            )
        _finish_curve_panel(
            ax,
            curve_ax,
            tossup_id,
            fontsize=7,
            family_label=family_label,
        )
    for ax in axes.flat[len(selected):]:
        ax.set_visible(False)
    fig.suptitle(
        f"Estimated tossup {family_label.lower()} and empirical buzz locations"
    )
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, filename, "tossup"), dpi=160)
    plt.close(fig)


def _multidim_curve_label(alpha_column, alpha_value):
    """Return a readable label for one multidim difficulty coordinate."""
    dimension = int(alpha_column.rsplit("_", 1)[1])
    name = vector_weight_name([alpha_column])
    return f"Dimension {dimension} ({name}={alpha_value:.2f})"


def multidim_difficulty_components_plot(
    results_dir,
    output_dir,
    count=6,
    panels_per_figure=6,
):
    """Plot every per-dimension correctness and hazard curve.

    The evaluator's default remains one six-tossup diagnostic. Larger opt-in
    galleries are split across numbered files so high-dimensional runs stay
    readable instead of growing into a single extremely tall figure.
    """
    if count < 1:
        raise ValueError("count must be at least 1")
    if panels_per_figure < 1:
        raise ValueError("panels_per_figure must be at least 1")
    required = [
        results_dir / "tossups.csv",
        results_dir / "tossup_predictions.csv",
    ]
    if not all(path.exists() for path in required):
        return
    parameters = pd.read_csv(required[0]).set_index("tossup_id")
    predictions = pd.read_csv(required[1])
    link = load_difficulty_link(results_dir)
    difficulty_scale = load_difficulty_scale(results_dir)
    for parameter_prefix, family_label, filename_stem in _saved_families(parameters):
        _multidim_difficulty_family_plot(
            parameters,
            predictions,
            output_dir,
            count,
            panels_per_figure,
            link,
            difficulty_scale,
            parameter_prefix,
            family_label,
            f"{filename_stem}_by_dimension",
        )


def _multidim_difficulty_family_plot(
    parameters,
    predictions,
    output_dir,
    count,
    panels_per_figure,
    link,
    difficulty_scale,
    parameter_prefix,
    family_label,
    filename_stem,
):
    """Render per-dimension components for one saved difficulty family."""
    graphs_dir = graph_path(
        output_dir, f"{filename_stem}.png", "tossup"
    ).parent
    for previous in graphs_dir.glob(f"{filename_stem}*.png"):
        previous.unlink()
    columns = _parameter_columns(parameters, parameter_prefix)
    parameter_columns = _difficulty_parameter_columns(columns, link)
    has_polynomial = bool(columns["polynomial"])
    has_monotone = bool(columns["monotone"])
    has_spline = bool(columns["spline"])
    if not columns["alpha"]:
        return
    if has_spline:
        _validate_spline_dimensions(columns["alpha"], columns["spline"])
    elif has_monotone:
        _validate_monotone_dimensions(
            columns["alpha"], columns["monotone"]
        )
    elif has_polynomial:
        _validate_polynomial_dimensions(
            columns["alpha"], columns["polynomial"]
        )
    else:
        if not (parameter_columns and columns["gamma"] and columns["mu"]):
            return
        _validate_tossup_multidim_dimensions(
            columns["alpha"], parameter_columns, columns["gamma"], columns["mu"]
        )

    selected = [
        tossup_id
        for tossup_id in selected_tossups(predictions, count=count)
        if tossup_id in parameters.index
    ]
    if not selected:
        return

    positions = np.linspace(0.0, 1.0, 100)
    plot_columns = min(2, panels_per_figure)
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    batches = [
        selected[start : start + panels_per_figure]
        for start in range(0, len(selected), panels_per_figure)
    ]
    weight_name = vector_weight_name(columns["alpha"])
    for batch_index, batch in enumerate(batches, start=1):
        rows = math.ceil(len(batch) / plot_columns)
        fig, axes = plt.subplots(
            rows,
            plot_columns,
            figsize=(12, 4.2 * rows),
            squeeze=False,
        )
        for ax, tossup_id in zip(axes.flat, batch):
            row = parameters.loc[tossup_id]
            components = _saved_difficulty_components(
                row,
                positions,
                link,
                difficulty_scale,
                parameter_prefix,
            )
            if components is None:
                ax.set_visible(False)
                continue
            per_dimension, difficulty = components
            alpha = row[columns["alpha"]].to_numpy(dtype=float)
            curve_ax = _buzz_histogram_axes(ax, predictions, tossup_id)
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
                label=f"{weight_name}-weighted {family_label.lower()}",
                zorder=10,
            )
            _finish_curve_panel(
                ax,
                curve_ax,
                tossup_id,
                fontsize=6,
                family_label=family_label,
            )
        for ax in axes.flat[len(batch):]:
            ax.set_visible(False)
        fig.suptitle(
            f"Per-dimension {family_label.lower()} curves and "
            f"{weight_name}-weighted {family_label.lower()}"
        )
        fig.tight_layout()
        filename = f"{filename_stem}.png"
        if len(batches) > 1:
            filename = f"{filename_stem}_{batch_index:02d}.png"
        fig.savefig(graph_path(output_dir, filename, "tossup"), dpi=160)
        plt.close(fig)
