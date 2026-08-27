"""Fitted bonus-part and synergy parameter distribution diagnostics."""

from __future__ import annotations

import numpy as np
import pandas as pd

from compirt_eval.common.figures import (
    density_panel_spec,
    distribution_dashboard,
    distribution_summary,
    labeled_series,
    numeric_columns,
    vector_weight_columns,
    vector_weight_name,
)
from compirt_eval.common.report_paths import csv_path, graph_path


def _bonus_part_panels_and_summary(
    parts, beta_columns, weight_columns, dimension_labels=None
):
    """Build bonus-part density panels and their distribution-summary rows."""
    panels = []
    weight_name = vector_weight_name(weight_columns)
    norm_column = f"{weight_name}_norm"
    if "beta" in parts:
        panels.append(
            density_panel_spec(
                parts["beta"], "Bonus-part difficulty", "beta", zero_line=True
            )
        )
    if beta_columns:
        panels.append(
            density_panel_spec(
                labeled_series(parts, beta_columns, dimension_labels),
                "Bonus-part difficulty coordinates",
                "beta",
                zero_line=True,
            )
        )
    if weight_columns:
        role = "relevance" if weight_name == "r" else "discrimination"
        panels.extend(
            [
                density_panel_spec(
                    labeled_series(parts, weight_columns, dimension_labels),
                    f"Bonus {role} coordinates",
                    weight_name,
                    zero_line=True,
                ),
                density_panel_spec(
                    parts[norm_column],
                    f"Bonus {role} magnitude",
                    f"{weight_name} norm",
                    bounds=(0, None),
                ),
            ]
        )
    rows = []
    summary_columns = ["beta", *beta_columns, *weight_columns]
    if weight_columns:
        summary_columns.append(norm_column)
    for column in summary_columns:
        if column in parts:
            summary = distribution_summary("bonus_part", column, parts[column])
            if summary:
                rows.append(summary)
    return panels, rows


def _synergy_panels_and_summary(results_dir):
    """Build optional synergy density panels and their summary rows."""
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
                    density_panel_spec(
                        profiles[psi_columns],
                        "Synergy profile coordinates",
                        "psi",
                        zero_line=True,
                    ),
                    density_panel_spec(
                        profiles["psi_norm"],
                        "Synergy profile magnitude",
                        "psi norm",
                        bounds=(0, None),
                    ),
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
                    density_panel_spec(frame[column], title, xlabel, zero_line=True)
                )
                summary = distribution_summary("synergy", column, frame[column])
                if summary:
                    rows.append(summary)
    return panels, rows


def bonus_parameter_distribution_plots(
    results_dir, output_dir, dimension_labels=None
):
    """Plot fitted bonus-part and optional synergy parameter distributions."""
    part_path = results_dir / "bonus_parts.csv"
    if not part_path.exists():
        return
    parts = pd.read_csv(part_path)
    beta_columns = numeric_columns(parts, "beta_")
    weight_columns = vector_weight_columns(parts)
    weight_name = vector_weight_name(weight_columns)
    norm_column = f"{weight_name}_norm"
    if weight_columns:
        parts[norm_column] = np.linalg.norm(
            parts[weight_columns].to_numpy(dtype=float), axis=1
        )

    part_panels, rows = _bonus_part_panels_and_summary(
        parts, beta_columns, weight_columns, dimension_labels
    )
    if part_panels:
        distribution_dashboard(
            part_panels,
            "Compositional bonus-part parameter distributions",
            graph_path(
                output_dir, "bonus_part_parameter_distributions.png", "parameters"
            ),
        )

    synergy_panels, synergy_rows = _synergy_panels_and_summary(results_dir)
    rows.extend(synergy_rows)
    if synergy_panels:
        distribution_dashboard(
            synergy_panels,
            "Synergy parameter and contribution distributions",
            graph_path(output_dir, "synergy_parameter_distributions.png", "parameters"),
        )
    pd.DataFrame(rows).to_csv(
        csv_path(output_dir, "bonus_parameter_distribution_summary.csv"), index=False
    )
