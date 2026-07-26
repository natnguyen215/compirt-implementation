"""Plot fitted pyramidal player/tossup parameter distributions.

Renders density panels for every fitted Stage 1 parameter (player skill
'theta'/confidence 'c', tossup discrimination 'alpha'/difficulty 'beta' or
biased-tanh 'bias', plus 'gamma'/'mu', polynomial raw-power coefficients, or
monotone-polynomial start/end/drop parameters) and a percentile-band view of
the learned difficulty curves themselves, and writes a matching numeric
summary CSV.
'pyramidal_parameter_distribution_plots' is the entry point, called from
'evaluate_tossups'.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.common.figures import (
    distribution_dashboard,
    distribution_summary,
    numeric_columns,
    vector_weight_name,
)
from compirt_eval.common.report_paths import csv_path, graph_path
from compirt_eval.scenario_a_tossups.parameters import (
    _parameter_columns,
    _positive_log_series,
    _saved_difficulty_curve,
    difficulty_adjustment_at,
    load_difficulty_adjustment_curves,
    load_difficulty_link,
)


def _pyramidal_player_panels(players, theta_columns):
    """Build the density panels for fitted player parameters (c, theta)."""
    panels = []
    if "c" in players:
        panels.append(
            {
                "series": {"c": players["c"]},
                "title": "Confidence threshold",
                "xlabel": "c",
                "zero_line": True,
                "bounds": None,
            }
        )
    if theta_columns:
        panels.append(
            {
                "series": {column: players[column] for column in theta_columns},
                "title": "Skill coordinates",
                "xlabel": "theta",
                "zero_line": True,
                "bounds": None,
            }
        )
    if "theta_norm" in players:
        panels.append(
            {
                "series": {"theta_norm": players["theta_norm"]},
                "title": "Skill magnitude",
                "xlabel": "theta norm",
                "zero_line": False,
                "bounds": (0, None),
            }
        )
    return panels


def _pyramidal_tossup_panels(tossups, alpha_columns):
    """Build density panels for fitted tossup difficulty and weight parameters."""
    panels = []
    columns = _parameter_columns(tossups)
    weight_name = vector_weight_name(alpha_columns)
    norm_column = f"{weight_name}_norm"
    for column, title, xlabel, zero_line in (
        ("beta", "Difficulty amplitude", "beta", True),
        ("mu", "Difficulty transition location", "relative position mu", False),
    ):
        if column in tossups:
            panels.append(
                {
                    "series": {column: tossups[column]},
                    "title": title,
                    "xlabel": xlabel,
                    "zero_line": zero_line,
                    "bounds": (0, 1) if column == "mu" else None,
                }
            )
    if "gamma" in tossups:
        # gamma is positive and heavy-tailed, so plot it on a log10 axis between
        # the amplitude and location panels.
        positive_gamma = tossups.loc[tossups["gamma"] > 0, "gamma"]
        panels.insert(
            1,
            {
                "series": {"log10_gamma": np.log10(positive_gamma)},
                "title": "Difficulty transition sharpness",
                "xlabel": "log10(gamma)",
                "zero_line": True,
                "bounds": None,
            },
        )
    if columns["beta"]:
        panels.append(
            {
                "series": {column: tossups[column] for column in columns["beta"]},
                "title": "Difficulty amplitudes",
                "xlabel": "beta",
                "zero_line": True,
                "bounds": None,
            }
        )
    if columns["bias"]:
        panels.append(
            {
                "series": {column: tossups[column] for column in columns["bias"]},
                "title": "Biased-tanh difficulty shifts",
                "xlabel": "bias",
                "zero_line": True,
                "bounds": None,
            }
        )
    if columns["gamma"]:
        panels.append(
            {
                "series": _positive_log_series(tossups, columns["gamma"]),
                "title": "Difficulty transition sharpness",
                "xlabel": "log10(gamma)",
                "zero_line": True,
                "bounds": None,
            }
        )
    if columns["mu"]:
        panels.append(
            {
                "series": {column: tossups[column] for column in columns["mu"]},
                "title": "Difficulty transition locations",
                "xlabel": "relative position mu",
                "zero_line": False,
                "bounds": (0, 1),
            }
        )
    if columns["polynomial"]:
        degree = len(columns["polynomial"][0]) - 1
        for power in range(degree + 1):
            labels = [
                dimension_columns[power]
                for dimension_columns in columns["polynomial"]
            ]
            panels.append(
                {
                    "series": {column: tossups[column] for column in labels},
                    "title": f"Polynomial coefficients for x^{power}",
                    "xlabel": f"raw coefficient c{power}",
                    "zero_line": True,
                    "bounds": None,
                }
            )
    if columns["monotone"]:
        monotone = columns["monotone"]
        for key, title, xlabel, bounds in (
            (
                "start",
                "Starting difficulty",
                "difficulty at x=0",
                None,
            ),
            (
                "end",
                "Ending difficulty",
                "difficulty at x=1",
                None,
            ),
            (
                "total",
                "Total difficulty drop",
                "start minus end",
                (0, None),
            ),
        ):
            panels.append(
                {
                    "series": {
                        column: tossups[column] for column in monotone[key]
                    },
                    "title": title,
                    "xlabel": xlabel,
                    "zero_line": key != "total",
                    "bounds": bounds,
                }
            )
        for share in range(len(monotone["shares"][0])):
            labels = [
                dimension_columns[share]
                for dimension_columns in monotone["shares"]
            ]
            panels.append(
                {
                    "series": {column: tossups[column] for column in labels},
                    "title": f"Difficulty drop share {share + 1}",
                    "xlabel": "proportion of total drop",
                    "zero_line": False,
                    "bounds": (0, 1),
                }
            )
    if alpha_columns:
        weight_title = (
            "Tossup relevance coordinates"
            if weight_name == "r"
            else "Tossup discrimination coordinates"
        )
        norm_title = (
            "Tossup relevance magnitude"
            if weight_name == "r"
            else "Tossup discrimination magnitude"
        )
        panels.append(
            {
                "series": {column: tossups[column] for column in alpha_columns},
                "title": weight_title,
                "xlabel": weight_name,
                "zero_line": True,
                "bounds": None,
            }
        )
        panels.append(
            {
                "series": {norm_column: tossups[norm_column]},
                "title": norm_title,
                "xlabel": f"{weight_name} norm",
                "zero_line": False,
                "bounds": (0, None),
            }
        )
    return panels


def _difficulty_curve_distribution_plot(tossups, output_dir, adjustments=None, link="sigmoid"):
    """Plot percentile bands across every learned tossup difficulty curve (Eq. 3).

    'adjustments' (saved signed TF-IDF difficulty deltas) shifts each tossup's
    curve to the effective difficulty 'd'' the model actually used.
    """
    positions = np.linspace(0, 1, 150)
    curves = []
    for _, tossup in tossups.iterrows():
        curve = _saved_difficulty_curve(tossup, positions, link)
        if curve is None:
            return
        curves.append(curve)
    if not curves:
        return
    curves = np.asarray(curves)
    columns = _parameter_columns(tossups)
    weight_name = vector_weight_name(columns["alpha"])
    label = (
        f"Median {weight_name}-weighted difficulty"
        if columns["alpha"]
        else "Median difficulty"
    )
    ylabel = (
        f"Estimated {weight_name}-weighted difficulty"
        if columns["alpha"]
        else "Estimated difficulty"
    )
    if adjustments is not None and "tossup_id" in tossups:
        for index, tossup_id in enumerate(tossups["tossup_id"].astype(str)):
            adjustment = difficulty_adjustment_at(adjustments, tossup_id, positions)
            if adjustment is not None:
                curves[index] = curves[index] + adjustment
        label = f"{label} (TF-IDF effective d')"
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
    ax.plot(positions, percentiles[2], linewidth=2, label=label)
    ax.set(
        title="Distribution of learned tossup difficulty curves",
        xlabel="Relative question position",
        ylabel=ylabel,
        xlim=(0, 1),
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(
        graph_path(
            output_dir, "pyramidal_difficulty_curve_distribution.png", "tossup"
        ),
        dpi=160
    )
    plt.close(fig)


def pyramidal_parameter_distribution_plots(results_dir, output_dir):
    """Plot fitted player and tossup parameter distributions.

    Reads the Stage 1 'players.csv' and 'tossups.csv' and writes three
    figures (player panels, tossup panels, difficulty-curve bands) and a summary
    CSV. Panel construction is delegated to the '_pyramidal_*' helpers above.
    """
    player_path = results_dir / "players.csv"
    tossup_path = results_dir / "tossups.csv"
    if not player_path.exists() or not tossup_path.exists():
        return
    players = pd.read_csv(player_path)
    tossups = pd.read_csv(tossup_path)
    theta_columns = numeric_columns(players, "theta_")
    tossup_columns = _parameter_columns(tossups)
    alpha_columns = tossup_columns["alpha"]
    weight_name = vector_weight_name(alpha_columns)
    norm_column = f"{weight_name}_norm"
    if "theta_norm" not in players and theta_columns:
        players["theta_norm"] = np.linalg.norm(
            players[theta_columns].to_numpy(dtype=float), axis=1
        )
    if alpha_columns:
        tossups[norm_column] = np.linalg.norm(
            tossups[alpha_columns].to_numpy(dtype=float), axis=1
        )

    player_panels = _pyramidal_player_panels(players, theta_columns)
    if player_panels:
        distribution_dashboard(
            player_panels,
            "Pyramidal player parameter distributions",
            graph_path(
                output_dir,
                "pyramidal_player_parameter_distributions.png",
                "parameters",
            ),
        )

    tossup_panels = _pyramidal_tossup_panels(tossups, alpha_columns)
    if tossup_panels:
        distribution_dashboard(
            tossup_panels,
            "Pyramidal tossup parameter distributions",
            graph_path(
                output_dir,
                "pyramidal_tossup_parameter_distributions.png",
                "parameters",
            ),
        )

    _difficulty_curve_distribution_plot(
        tossups,
        output_dir,
        load_difficulty_adjustment_curves(results_dir),
        load_difficulty_link(results_dir),
    )

    rows = []
    for group, frame, columns in (
        ("player", players, ["c", *theta_columns, "theta_norm"]),
        (
            "tossup",
            tossups,
            [
                "beta",
                "bias",
                "gamma",
                "mu",
                *tossup_columns["beta"],
                *tossup_columns["bias"],
                *tossup_columns["gamma"],
                *tossup_columns["mu"],
                *[
                    label
                    for dimension in tossup_columns["polynomial"]
                    for label in dimension
                ],
                *(
                    [
                        *tossup_columns["monotone"]["start"],
                        *tossup_columns["monotone"]["end"],
                        *tossup_columns["monotone"]["total"],
                        *[
                            label
                            for dimension in tossup_columns["monotone"]["shares"]
                            for label in dimension
                        ],
                    ]
                    if tossup_columns["monotone"]
                    else []
                ),
                *alpha_columns,
                norm_column,
            ],
        ),
    ):
        for column in columns:
            if column in frame:
                summary = distribution_summary(group, column, frame[column])
                if summary:
                    rows.append(summary)
    pd.DataFrame(rows).to_csv(
        csv_path(output_dir, "pyramidal_parameter_distribution_summary.csv"), index=False
    )
