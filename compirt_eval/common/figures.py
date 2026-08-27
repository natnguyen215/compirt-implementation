"""Shared plotting primitives and helpers for CompIRT evaluation figures.

Reusable building blocks -- reliability curves, kernel-density panels,
and small dataframe/label utilities -- used by both the tossup
(Scenario A) and bonus (Scenario B) figure modules.
"""

from __future__ import annotations

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.common.metrics import calibration_table, expected_calibration_error


def reliability_plot(y, probability, title, path):
    """Plot average predicted and observed correctness within probability bins."""
    probability = np.asarray(probability, dtype=float)
    calibration = calibration_table(y, probability)
    ece = expected_calibration_error(np.asarray(y, dtype=float), probability)
    fig, (ax, distribution_ax) = plt.subplots(
        2,
        1,
        figsize=(6.5, 7),
        gridspec_kw={"height_ratios": [4, 1]},
        sharex=True,
    )
    ax.plot([0, 1], [0, 1], "--", color="0.5")
    ax.plot(
        calibration["predicted"],
        calibration["observed"],
        "o-",
        label=f"ECE = {ece:.3f}",
    )
    ax.set(title=title, ylabel="Observed", xlim=(0, 1), ylim=(0, 1))
    ax.grid(alpha=0.25)
    ax.legend(loc="upper left")
    distribution_ax.hist(
        probability,
        bins=np.linspace(0, 1, 11),
        color="tab:blue",
        alpha=0.65,
    )
    distribution_ax.set(xlabel="Predicted probability", ylabel="Count", xlim=(0, 1))
    distribution_ax.grid(alpha=0.2, axis="y")
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def stratified_ece_plot(diagnostics, path):
    """Plot per-stratum ECE bars against each scenario's aggregate ECE.

    One panel per scenario; the dashed line is that scenario's aggregate
    value, so a stratum hiding behind a good pooled number stands out. Tick
    labels carry the observation counts the stratum contract says must be
    read alongside any stratum metric.
    """
    scenarios = list(dict.fromkeys(diagnostics["scenario"]))
    height = max(4.0, 0.32 * int(diagnostics.groupby("scenario").size().max()) + 1.5)
    fig, axes = plt.subplots(
        1, len(scenarios), figsize=(6.5 * len(scenarios), height), squeeze=False
    )
    for ax, scenario in zip(axes.flat, scenarios):
        rows = diagnostics[diagnostics["scenario"] == scenario]
        aggregate = rows.loc[rows["stratum"] == "aggregate", "ece"]
        strata = rows[rows["stratum"] != "aggregate"]
        positions = np.arange(len(strata))
        ax.barh(positions, strata["ece"], height=0.62, color="tab:blue", alpha=0.75)
        ax.set_yticks(
            positions,
            [
                f"{stratum}: {value} (n={int(count):,})"
                for stratum, value, count in zip(
                    strata["stratum"], strata["value"], strata["observations"]
                )
            ],
            fontsize=8,
        )
        ax.invert_yaxis()
        if not aggregate.empty:
            ax.axvline(
                float(aggregate.iloc[0]),
                color="tab:orange",
                linestyle="--",
                label=f"aggregate ECE = {float(aggregate.iloc[0]):.3f}",
            )
            ax.legend(fontsize=8)
        ax.set(title=scenario, xlabel="ECE")
        ax.grid(alpha=0.25, axis="x")
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def numeric_columns(frame, prefix):
    """Return numbered labels such as theta_1, theta_2 in numeric order.

    Accepts a DataFrame (whose columns are searched) or a single saved row as
    a Series (whose index is searched), so the same helper reads a whole table
    or one tossup.
    """
    labels = frame.index if isinstance(frame, pd.Series) else frame.columns
    return sorted(
        (
            label
            for label in labels
            if isinstance(label, str)
            and label.startswith(prefix)
            and label.removeprefix(prefix).isdigit()
        ),
        key=lambda label: int(label.removeprefix(prefix)),
    )


def vector_weight_columns(frame):
    """Return saved vector weights, accepting either alpha_* or embedding r_*."""
    alpha_columns = numeric_columns(frame, "alpha_")
    relevance_columns = numeric_columns(frame, "r_")
    if alpha_columns and relevance_columns:
        raise ValueError("Saved vector weights must use either alpha_* or r_*, not both")
    return alpha_columns or relevance_columns


def vector_weight_name(columns):
    """Return the coordinate prefix used by a saved vector-weight family."""
    if columns and columns[0].removeprefix("hazard_").startswith("r_"):
        return "r"
    return "alpha"


def labeled_series(frame, columns, dimension_labels=None):
    """Return column values keyed by display labels.

    'dimension_labels' maps 1-based coordinate numbers to friendly names,
    letting topic-weighted runs label 'theta_1' as a category or topic name
    while preserving the raw column name when no label exists.
    """
    series = {}
    for column in columns:
        suffix = column.rsplit("_", 1)[-1]
        label = column
        if dimension_labels and suffix.isdigit():
            label = dimension_labels.get(int(suffix), column)
        series[label] = frame[column]
    return series


def density_estimate(values, points=256, max_samples=10000, bounds=None):
    """Return a deterministic Gaussian kernel density estimate.

    'points' is the number of x-grid points returned; 'max_samples' caps the
    inputs (evenly subsampled above that for speed); 'bounds' is an optional
    '(lower, upper)' clamp on the grid for parameters with a natural support,
    such as '(0, 1)' for 'mu' or '(0, None)' for a norm.
    """
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    if len(values) < 2:
        return np.asarray([]), np.asarray([])
    values.sort()
    if len(values) > max_samples:
        selected = np.linspace(0, len(values) - 1, max_samples).round().astype(int)
        values = values[selected]
    standard_deviation = values.std(ddof=1)
    interquartile_range = np.subtract(*np.percentile(values, [75, 25]))
    scale_candidates = [
        candidate
        for candidate in (standard_deviation, interquartile_range / 1.34)
        if np.isfinite(candidate) and candidate > 0
    ]
    scale = min(scale_candidates) if scale_candidates else max(abs(values.mean()) * 0.05, 0.1)
    # Scott's rule: bandwidth = 0.9 * scale * n^(-1/5); the 1e-6 floor keeps the
    # Gaussian kernel from collapsing when every value is (nearly) identical.
    bandwidth = max(0.9 * scale * len(values) ** (-1 / 5), 1e-6)
    lower = values.min() - 3 * bandwidth
    upper = values.max() + 3 * bandwidth
    if bounds:
        if bounds[0] is not None:
            lower = max(lower, bounds[0])
        if bounds[1] is not None:
            upper = min(upper, bounds[1])
    grid = np.linspace(lower, upper, points)
    standardized = (grid[:, None] - values[None, :]) / bandwidth
    density = np.exp(-0.5 * standardized**2).mean(axis=1) / (
        bandwidth * np.sqrt(2 * np.pi)
    )
    return grid, density


def distribution_summary(group, parameter, values):
    """Return robust descriptive statistics for one plotted distribution."""
    values = np.asarray(values, dtype=float)
    values = values[np.isfinite(values)]
    if not len(values):
        return None
    percentiles = np.percentile(values, [5, 25, 50, 75, 95])
    return {
        "group": group,
        "parameter": parameter,
        "observations": len(values),
        "mean": values.mean(),
        "standard_deviation": values.std(ddof=1) if len(values) > 1 else 0.0,
        "minimum": values.min(),
        "p05": percentiles[0],
        "p25": percentiles[1],
        "median": percentiles[2],
        "p75": percentiles[3],
        "p95": percentiles[4],
        "maximum": values.max(),
    }


def density_panel(ax, series, title, xlabel, zero_line=False, bounds=None):
    """Draw histogram-backed density curves for one or more parameters.

    'series' maps a legend label to its values; a single series also gets a
    filled histogram, while multiple series share the axis with a legend.
    'zero_line' draws a reference line at x=0 (useful for signed parameters),
    and 'bounds' is forwarded to 'density_estimate' to clamp the grid.
    """
    colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    multiple = len(series) > 1
    for index, (label, values) in enumerate(series.items()):
        values = np.asarray(values, dtype=float)
        values = values[np.isfinite(values)]
        if not len(values):
            continue
        color = colors[index % len(colors)]
        if not multiple:
            bins = min(40, max(8, int(np.sqrt(len(values)))))
            ax.hist(values, bins=bins, density=True, color=color, alpha=0.2)
        grid, density = density_estimate(values, bounds=bounds)
        if len(grid):
            ax.plot(grid, density, color=color, linewidth=2, label=label)
            if not multiple:
                ax.fill_between(grid, density, color=color, alpha=0.12)
        ax.axvline(np.median(values), color=color, linestyle=":", alpha=0.8)
    if zero_line:
        ax.axvline(0, color="0.45", linestyle="--", linewidth=1)
    ax.set(title=title, xlabel=xlabel, ylabel="Density")
    ax.grid(alpha=0.2)
    if multiple:
        ax.legend(fontsize=7)


def density_panel_spec(series, title, xlabel, *, zero_line=False, bounds=None):
    """Build one `distribution_dashboard` panel, keyed for `density_panel`.

    `series` may already be the label-to-values mapping `density_panel` wants,
    or a DataFrame slice / single column, which is the common case and reads
    better than spelling the comprehension out at every call site.
    """
    if isinstance(series, pd.DataFrame):
        series = {column: series[column] for column in series.columns}
    elif isinstance(series, pd.Series):
        series = {series.name: series}
    return {
        "series": series,
        "title": title,
        "xlabel": xlabel,
        "zero_line": zero_line,
        "bounds": bounds,
    }


def distribution_dashboard(panels, title, path):
    """Plot a compact dashboard of related parameter distributions."""
    columns = min(3, len(panels))
    rows = math.ceil(len(panels) / columns)
    fig, axes = plt.subplots(rows, columns, figsize=(4.5 * columns, 3.6 * rows), squeeze=False)
    for ax, panel in zip(axes.flat, panels):
        density_panel(ax, **panel)
    for ax in axes.flat[len(panels):]:
        ax.set_visible(False)
    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def short_id(identifier, width=28):
    """Keep long compound IDs readable in plot labels."""
    identifier = str(identifier)
    return identifier if len(identifier) <= width else f"...{identifier[-(width - 3):]}"
