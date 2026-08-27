"""Scenario A orchestration: turn saved tossup predictions into metrics and figures.

'evaluate_tossups' is the entry point. It reads 'tossup_predictions.csv' and
sequences the per-concern builders in this subpackage -- classification
metrics, the joint competing-risks event score, calibration (aggregate and
stratified), difficulty curves, first-buzz timing/identity, and the fitted
parameter distributions -- returning the scalar tossup-metric dict that
'evaluate_compirt.py' writes to 'tossup_metrics.csv'. When the run also saved
'buzz_event_predictions.csv' (one row per first-buzz event), it adds the
buzz-position error metrics and figures. Correctness metrics are scored on
'z == "BUZZ"' rows only, since only actual buzzers have an observed outcome.
"""

from __future__ import annotations

import pandas as pd

from compirt_eval.common.figures import reliability_plot
from compirt_eval.common.metrics import (
    classification_metrics,
    negative_class_metrics,
    stratified_prediction_metrics,
)
from compirt_eval.common.report_paths import csv_path, graph_path
from compirt_eval.scenario_a_tossups.difficulty import (
    difficulty_plot,
    multidim_difficulty_components_plot,
)
from compirt_eval.scenario_a_tossups.distributions import pyramidal_parameter_distribution_plots
from compirt_eval.scenario_a_tossups.metrics import tossup_joint_event_scores
from compirt_eval.scenario_a_tossups.position import evaluate_buzz_positions
from compirt_eval.scenario_a_tossups.reliability import (
    BUZZ_POSITION_EDGES,
    BUZZ_POSITION_LABELS,
    stratified_tossup_reliability_plot,
)
from compirt_eval.scenario_a_tossups.timing import (
    buzz_density_fit_plot,
    evaluate_survival_and_first_buzzer,
)
from topic.utils.categories import top_level_category


def evaluate_tossups(results_dir, output_dir):
    """Evaluate first-buzz correctness and expected first-buzz position."""
    predictions = pd.read_csv(results_dir / "tossup_predictions.csv")
    event_scores = tossup_joint_event_scores(predictions)
    event_scores.to_csv(
        csv_path(output_dir, "tossup_joint_event_scores.csv"), index=False
    )
    # Only actual buzzers have an observed correctness outcome.
    buzz = predictions[predictions["z"] == "BUZZ"].copy()
    metrics = classification_metrics(buzz["y"], buzz["predicted_correct"])
    metrics.update(negative_class_metrics(buzz["y"], buzz["predicted_correct"]))
    metrics["joint_tossup_event_log_loss"] = (
        float(event_scores["joint_event_log_loss"].mean())
        if not event_scores.empty
        else float("nan")
    )
    metrics["joint_tossup_event_log_loss_events"] = len(event_scores)
    if not buzz.empty:
        if "category" in buzz:
            buzz["category_group"] = buzz["category"].map(top_level_category)
        buzz["buzz_position_quintile"] = pd.cut(
            buzz["relative_position"],
            bins=BUZZ_POSITION_EDGES,
            labels=BUZZ_POSITION_LABELS,
            include_lowest=True,
        )
        diagnostics = stratified_prediction_metrics(
            buzz,
            "y",
            "predicted_correct",
            "tossup_correctness",
            {
                "tier": "tier",
                "category": "category_group",
                "buzz_position_quintile": "buzz_position_quintile",
            },
        )
        diagnostics.to_csv(
            csv_path(output_dir, "tossup_prediction_diagnostics_by_stratum.csv"),
            index=False,
        )
        reliability_plot(
            buzz["y"],
            buzz["predicted_correct"],
            "Tossup correctness reliability",
            graph_path(output_dir, "tossup_reliability.png", "tossup"),
        )
        stratified_tossup_reliability_plot(buzz, output_dir)
    difficulty_plot(results_dir, output_dir)
    multidim_difficulty_components_plot(results_dir, output_dir)
    buzz_density_fit_plot(results_dir, output_dir)
    metrics.update(evaluate_survival_and_first_buzzer(results_dir, output_dir))
    pyramidal_parameter_distribution_plots(results_dir, output_dir)

    position_path = results_dir / "buzz_event_predictions.csv"
    if position_path.exists():
        # Position predictions already contain one row per first-buzz event.
        events = pd.read_csv(position_path)
        metrics.update(evaluate_buzz_positions(events, output_dir))
    return metrics
