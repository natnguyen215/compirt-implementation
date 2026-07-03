"""Scenario B: bonus-part and points-per-bonus evaluation.

Bonus-part calibration, expected-points-by-observed-score figures, the
fitted bonus-part parameter distributions, and the optional synergy
diagnostics. 'evaluate_bonuses' is the entry point.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from compirt_eval.figures import (
    distribution_dashboard,
    distribution_summary,
    numeric_columns,
    reliability_plot,
)
from compirt_eval.metrics import bonus_metrics
from compirt_eval.outputs import csv_path, graph_path


def _bonus_part_panels_and_summary(parts, alpha_columns):
    """Build bonus-part density panels and their distribution-summary rows."""
    panels = []
    if "beta" in parts:
        panels.append(
            {
                "series": {"beta": parts["beta"]},
                "title": "Bonus-part difficulty",
                "xlabel": "beta",
                "zero_line": True,
                "bounds": None,
            }
        )
    if alpha_columns:
        panels.extend(
            [
                {
                    "series": {column: parts[column] for column in alpha_columns},
                    "title": "Bonus discrimination coordinates",
                    "xlabel": "alpha",
                    "zero_line": True,
                    "bounds": None,
                },
                {
                    "series": {"alpha_norm": parts["alpha_norm"]},
                    "title": "Bonus discrimination magnitude",
                    "xlabel": "alpha norm",
                    "zero_line": False,
                    "bounds": (0, None),
                },
            ]
        )
    rows = []
    for column in ["beta", *alpha_columns, "alpha_norm"]:
        if column in parts:
            summary = distribution_summary("bonus_part", column, parts[column])
            if summary:
                rows.append(summary)
    return panels, rows


def _synergy_panels_and_summary(results_dir):
    """Build optional synergy density panels and their summary rows.

    Covers the player-level synergy profiles 'psi' (Eq. 10) plus the derived
    pairwise and team-level synergy contributions, when those files were saved.
    """
    panels = []
    rows = []
    profile_path = results_dir / "player_synergy_profiles.csv"
    if profile_path.exists():
        profiles = pd.read_csv(profile_path)
        psi_columns = numeric_columns(profiles, "psi_")
        if psi_columns:
            profiles["psi_norm"] = np.linalg.norm(
                profiles[psi_columns].to_numpy(dtype=float), axis=1
            )
            panels.extend(
                [
                    {
                        "series": {column: profiles[column] for column in psi_columns},
                        "title": "Synergy profile coordinates",
                        "xlabel": "psi",
                        "zero_line": True,
                        "bounds": None,
                    },
                    {
                        "series": {"psi_norm": profiles["psi_norm"]},
                        "title": "Synergy profile magnitude",
                        "xlabel": "psi norm",
                        "zero_line": False,
                        "bounds": (0, None),
                    },
                ]
            )
            for column in [*psi_columns, "psi_norm"]:
                summary = distribution_summary("synergy_player", column, profiles[column])
                if summary:
                    rows.append(summary)
    for filename, column, title, xlabel in (
        (
            "pairwise_synergy_scores.csv",
            "synergy_score",
            "Observed teammate-pair synergy",
            "pairwise synergy score",
        ),
        (
            "team_synergy_contributions.csv",
            "synergy_contribution",
            "Team synergy contribution",
            "synergy contribution",
        ),
    ):
        path = results_dir / filename
        if path.exists():
            frame = pd.read_csv(path)
            if column in frame:
                panels.append(
                    {
                        "series": {column: frame[column]},
                        "title": title,
                        "xlabel": xlabel,
                        "zero_line": True,
                        "bounds": None,
                    }
                )
                summary = distribution_summary("synergy", column, frame[column])
                if summary:
                    rows.append(summary)
    return panels, rows


def bonus_parameter_distribution_plots(results_dir, output_dir):
    """Plot fitted bonus-part and optional synergy parameter distributions.

    Writes the bonus-part panel figure, the optional synergy panel figure, and a
    combined summary CSV. Panel and summary construction is split between the
    '_bonus_part_*' and '_synergy_*' helpers above.
    """
    part_path = results_dir / "bonus_parts.csv"
    if not part_path.exists():
        return
    parts = pd.read_csv(part_path)
    alpha_columns = numeric_columns(parts, "alpha_")
    if alpha_columns:
        parts["alpha_norm"] = np.linalg.norm(
            parts[alpha_columns].to_numpy(dtype=float), axis=1
        )

    part_panels, rows = _bonus_part_panels_and_summary(parts, alpha_columns)
    if part_panels:
        distribution_dashboard(
            part_panels,
            "Compositional bonus-part parameter distributions",
            graph_path(output_dir, "bonus_part_parameter_distributions.png"),
        )

    synergy_panels, synergy_rows = _synergy_panels_and_summary(results_dir)
    rows.extend(synergy_rows)
    if synergy_panels:
        distribution_dashboard(
            synergy_panels,
            "Synergy parameter and contribution distributions",
            graph_path(output_dir, "synergy_parameter_distributions.png"),
        )
    pd.DataFrame(rows).to_csv(
        csv_path(output_dir, "bonus_parameter_distribution_summary.csv"), index=False
    )


def evaluate_bonuses(results_dir, output_dir, dimension_labels=None):
    """Evaluate binary bonus parts and total expected points per bonus."""
    parts = pd.read_csv(results_dir / "bonus_part_predictions.csv")
    teams = pd.read_csv(results_dir / "team_predictions.csv")
    metrics = bonus_metrics(parts, teams)
    reliability_plot(
        parts["correct"],
        parts["predicted_correct"],
        "Bonus part reliability",
        graph_path(output_dir, "bonus_reliability.png"),
    )
    scores = (0, 10, 20, 30)
    score_groups = [
        (
            score,
            teams.loc[teams["total_points"] == score, "predicted_points"].to_numpy(),
        )
        for score in scores
    ]
    score_groups = [(score, values) for score, values in score_groups if len(values)]
    if not score_groups:
        return metrics

    observed_scores, groups = zip(*score_groups)
    positions = np.arange(len(groups))
    fig, ax = plt.subplots(figsize=(8, 6))
    boxes = ax.boxplot(
        groups,
        positions=positions,
        widths=0.55,
        patch_artist=True,
        showfliers=False,
        medianprops={"color": "black"},
    )
    for box in boxes["boxes"]:
        box.set(facecolor="tab:blue", alpha=0.25)
    rng = np.random.default_rng(0)
    for position, values in zip(positions, groups):
        jitter = rng.normal(position, 0.055, len(values))
        ax.scatter(jitter, values, s=12, alpha=0.2, color="tab:blue")
    means = [values.mean() for values in groups]
    ax.scatter(positions, means, marker="D", color="tab:orange", label="Mean prediction")
    ax.scatter(
        positions,
        observed_scores,
        marker="x",
        s=70,
        color="black",
        label="Ideal prediction",
    )
    tick_labels = [f"{score}\n(n={len(values)})" for score, values in score_groups]
    ax.set_xticks(positions, tick_labels)
    ax.set(
        title="Predicted bonus points by observed score",
        xlabel="Observed bonus points",
        ylabel="Predicted expected bonus points",
        ylim=(-1, 31),
    )
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, "bonus_ppb_predictions.png"), dpi=160)
    plt.close(fig)
    bonus_parameter_distribution_plots(results_dir, output_dir)
    return metrics
