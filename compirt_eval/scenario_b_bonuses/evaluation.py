"""Scenario B: bonus-part and points-per-bonus evaluation.

Bonus-part calibration and prediction figures are orchestrated here.
Scenario-owned scoring and parameter-distribution diagnostics live in the
neighboring ``metrics`` and ``distributions`` modules.
"""

from __future__ import annotations

import pandas as pd

from compirt_eval.common.figures import reliability_plot
from compirt_eval.common.metrics import stratified_prediction_metrics
from compirt_eval.common.report_paths import csv_path, graph_path
from compirt_eval.scenario_b_bonuses.distributions import (
    bonus_parameter_distribution_plots,
    bonus_prediction_distribution_plots,
)
from compirt_eval.scenario_b_bonuses.figures import (
    bonus_score_by_observed_plot,
    team_ppb_plot,
)
from compirt_eval.scenario_b_bonuses.metrics import (
    bonus_accuracy_by_difficulty,
    bonus_metrics,
    bonus_parts_with_difficulty,
    bonus_ranked_probability_scores,
)
from compirt_eval.common.categories import top_level_category
from compirt_eval.scenario_b_bonuses.outcomes import write_bonus_outcomes


def evaluate_bonuses(results_dir, output_dir, dimension_labels=None, *, tables=None):
    """Evaluate binary bonus parts and total expected points per bonus."""
    parts = pd.read_csv(results_dir / "bonus_part_predictions.csv")
    parts = bonus_parts_with_difficulty(parts, tables["bonuses"] if tables is not None else None)
    teams = pd.read_csv(results_dir / "team_predictions.csv")
    response_scores = bonus_ranked_probability_scores(parts)
    metrics = bonus_metrics(parts, teams, response_scores)
    if tables is not None:
        metrics.update(write_bonus_outcomes(parts, tables, csv_path(output_dir, "bonus_metrics.csv").parent))
    bonus_accuracy_by_difficulty(parts).to_csv(
        csv_path(output_dir, "bonus_part_accuracy_by_difficulty.csv"), index=False
    )
    response_scores.to_csv(
        csv_path(output_dir, "bonus_score_probability_predictions.csv"), index=False
    )
    diagnostic_parts = parts.copy()
    if "category" in diagnostic_parts:
        diagnostic_parts["category_group"] = diagnostic_parts["category"].map(
            top_level_category
        )
    diagnostics = stratified_prediction_metrics(
        diagnostic_parts,
        "correct",
        "predicted_correct",
        "bonus_part_correctness",
        {"tier": "tier", "category": "category_group", "difficulty": "difficulty"},
    )
    diagnostics.to_csv(
        csv_path(output_dir, "bonus_prediction_diagnostics_by_stratum.csv"),
        index=False,
    )
    reliability_plot(
        parts["correct"],
        parts["predicted_correct"],
        "Bonus part reliability",
        graph_path(output_dir, "bonus_reliability.png", "bonus"),
    )
    bonus_parameter_distribution_plots(results_dir, output_dir, dimension_labels)
    bonus_prediction_distribution_plots(parts, output_dir)
    team_ppb_plot(teams, output_dir)
    bonus_score_by_observed_plot(teams, output_dir)
    return metrics
