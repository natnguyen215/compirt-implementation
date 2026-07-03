"""Plot fitted pyramidal player/tossup parameter distributions.

Renders density panels for every fitted Stage 1 parameter (player skill
'theta'/confidence 'c', tossup discrimination 'alpha'/difficulty
'beta'/'gamma'/'mu') plus a percentile-band view of the learned
difficulty curves themselves, and writes a matching numeric summary CSV.
'pyramidal_parameter_distribution_plots' is the entry point, called from
'evaluate_tossups'.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.figures import (
    distribution_dashboard,
    distribution_summary,
    numeric_columns,
)
from compirt_eval.metrics import difficulty_curve
from compirt_eval.outputs import csv_path, graph_path
from compirt_eval.tossups.parameters import (
    _parameter_columns,
    _positive_log_series,
    _validate_tossup_multidim_dimensions,
    difficulty_adjustment_at,
    load_difficulty_adjustment_curves,
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
    """Build the density panels for fitted tossup parameters (beta, gamma, mu, alpha)."""
    panels = []
    columns = _parameter_columns(tossups)
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
    if alpha_columns:
        panels.append(
            {
                "series": {column: tossups[column] for column in alpha_columns},
                "title": "Tossup discrimination coordinates",
                "xlabel": "alpha",
                "zero_line": True,
                "bounds": None,
            }
        )
        panels.append(
            {
                "series": {"alpha_norm": tossups["alpha_norm"]},
                "title": "Tossup discrimination magnitude",
                "xlabel": "alpha norm",
                "zero_line": False,
                "bounds": (0, None),
            }
        )
    return panels


def _difficulty_curve_distribution_plot(tossups, output_dir, adjustments=None):
    """Plot percentile bands across every learned tossup difficulty curve (Eq. 3).

    'adjustments' (saved TF-IDF adjustment curves) shifts each tossup's curve
    to the effective difficulty 'd'' the model actually used.
    """
    positions = np.linspace(0, 1, 150)
    if {"beta", "gamma", "mu"}.issubset(tossups):
        curves = difficulty_curve(
            tossups["beta"].to_numpy()[:, None],
            tossups["gamma"].to_numpy()[:, None],
            tossups["mu"].to_numpy()[:, None],
            positions[None, :],
        )
        label = "Median difficulty"
        ylabel = "Estimated difficulty"
    else:
        columns = _parameter_columns(tossups)
        if not all(columns[name] for name in ("alpha", "beta", "gamma", "mu")):
            return
        _validate_tossup_multidim_dimensions(
            columns["alpha"], columns["beta"], columns["gamma"], columns["mu"]
        )
        alpha = tossups[columns["alpha"]].to_numpy(dtype=float)[:, :, None]
        per_dimension = difficulty_curve(
            tossups[columns["beta"]].to_numpy(dtype=float)[:, :, None],
            tossups[columns["gamma"]].to_numpy(dtype=float)[:, :, None],
            tossups[columns["mu"]].to_numpy(dtype=float)[:, :, None],
            positions[None, None, :],
        )
        curves = (alpha * per_dimension).sum(axis=1)
        label = "Median alpha-weighted difficulty"
        ylabel = "Estimated alpha-weighted difficulty"
    if adjustments is not None and "tossup_id" in tossups:
        for index, tossup_id in enumerate(tossups["tossup_id"].astype(str)):
            adjustment = difficulty_adjustment_at(adjustments, tossup_id, positions)
            if adjustment is not None:
                curves[index] = curves[index] - adjustment
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
        graph_path(output_dir, "pyramidal_difficulty_curve_distribution.png"), dpi=160
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
    alpha_columns = numeric_columns(tossups, "alpha_")
    tossup_columns = _parameter_columns(tossups)
    if "theta_norm" not in players and theta_columns:
        players["theta_norm"] = np.linalg.norm(
            players[theta_columns].to_numpy(dtype=float), axis=1
        )
    if alpha_columns:
        tossups["alpha_norm"] = np.linalg.norm(
            tossups[alpha_columns].to_numpy(dtype=float), axis=1
        )

    player_panels = _pyramidal_player_panels(players, theta_columns)
    if player_panels:
        distribution_dashboard(
            player_panels,
            "Pyramidal player parameter distributions",
            graph_path(output_dir, "pyramidal_player_parameter_distributions.png"),
        )

    tossup_panels = _pyramidal_tossup_panels(tossups, alpha_columns)
    if tossup_panels:
        distribution_dashboard(
            tossup_panels,
            "Pyramidal tossup parameter distributions",
            graph_path(output_dir, "pyramidal_tossup_parameter_distributions.png"),
        )

    _difficulty_curve_distribution_plot(
        tossups, output_dir, load_difficulty_adjustment_curves(results_dir)
    )

    rows = []
    for group, frame, columns in (
        ("player", players, ["c", *theta_columns, "theta_norm"]),
        (
            "tossup",
            tossups,
            [
                "beta",
                "gamma",
                "mu",
                *tossup_columns["beta"],
                *tossup_columns["gamma"],
                *tossup_columns["mu"],
                *alpha_columns,
                "alpha_norm",
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
