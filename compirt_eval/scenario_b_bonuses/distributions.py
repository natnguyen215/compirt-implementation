"""Fitted bonus-part and synergy parameter distribution diagnostics."""

from __future__ import annotations

import json
from pathlib import Path

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
        for name in ("psi", "phi"):
            columns = numeric_columns(profiles, f"{name}_")
            if not columns:
                continue
            norm = f"{name}_norm"
            profiles[norm] = np.linalg.norm(
                profiles[columns].to_numpy(dtype=float), axis=1
            )
            panels.extend(
                [
                    density_panel_spec(
                        profiles[columns],
                        f"Synergy {name} profile coordinates",
                        name,
                        zero_line=True,
                    ),
                    density_panel_spec(
                        profiles[norm],
                        f"Synergy {name} profile magnitude",
                        f"{name} norm",
                        bounds=(0, None),
                    ),
                ]
            )
            for column in [*columns, norm]:
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
    """Plot saved parameters, resolving the training source for frozen replay.

    Frozen bonus folders contain predictions only. Their sibling training
    branch owns the fitted parameters and training-roster synergy diagnostics.
    """
    results_dir = Path(results_dir)
    parameter_dir = results_dir
    part_path = parameter_dir / "bonus_parts.csv"
    if not part_path.exists():
        summary_path = results_dir / "summary.json"
        summary = json.loads(summary_path.read_text()) if summary_path.exists() else {}
        if summary.get("frozen_predict"):
            if summary.get("train_compositional"):
                parameter_dir = Path(summary["train_compositional"])
            elif results_dir.parent.name == "holdout":
                parameter_dir = results_dir.parent.parent / "train" / results_dir.name
            part_path = parameter_dir / "bonus_parts.csv"
            if not part_path.exists():
                raise FileNotFoundError(f"Frozen bonus parameter source is unavailable: {part_path}")
    if not part_path.exists():
        return
    from_training = parameter_dir != results_dir
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
            ("Training-fit bonus-part parameter distributions" if from_training
             else "Compositional bonus-part parameter distributions"),
            graph_path(
                output_dir, "bonus_part_parameter_distributions.png", "parameters"
            ),
        )

    synergy_panels, synergy_rows = _synergy_panels_and_summary(parameter_dir)
    rows.extend(synergy_rows)
    if synergy_panels:
        distribution_dashboard(
            synergy_panels,
            ("Training-fit synergy parameters and training-roster contributions"
             if from_training else "Synergy parameter and contribution distributions"),
            graph_path(output_dir, "synergy_parameter_distributions.png", "parameters"),
        )
    pd.DataFrame(rows).assign(parameter_source=str(parameter_dir)).to_csv(
        csv_path(output_dir, "bonus_parameter_distribution_summary.csv"), index=False
    )


def bonus_prediction_distribution_plots(parts, output_dir, bonus_aggregation="lse"):
    """Plot evaluated row contributions, separately from fitted entity parameters."""
    panels, rows = [], []
    specs = [
        ("predicted_correct", "Predicted part correctness (per part)", "Probability", "bonus_part_row"),
        ("aggregate", "Aggregate ability (per part)", r"$A_k(T)$", "bonus_part_row"),
        ("synergy_contribution", "Synergy contribution (per response)", r"$\Phi(T)$", "bonus_response"),
    ]
    # Noisy-OR saves the full team logit, difficulty included, as 'aggregate'.
    if bonus_aggregation == "noisy-or":
        specs[1] = ("aggregate", "Noisy-OR team logit (per part)", "logit(p)", "bonus_part_row")
    for column, title, label, entity in specs:
        if column not in parts:
            continue
        frame = parts.drop_duplicates("response_id") if entity == "bonus_response" else parts
        values = frame[column]
        panels.append(density_panel_spec(
            values, title, label, zero_line=column != "predicted_correct",
            bounds=(0, 1) if column == "predicted_correct" else None,
        ))
        summary = distribution_summary(entity, column, values)
        if summary:
            rows.append(summary)
    if panels:
        distribution_dashboard(
            panels, "Evaluated bonus prediction distributions",
            graph_path(output_dir, "bonus_prediction_distributions.png", "bonus"),
        )
        pd.DataFrame(rows).to_csv(
            csv_path(output_dir, "bonus_prediction_distribution_summary.csv"), index=False
        )
