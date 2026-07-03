"""Scenario A: tossup first-buzz evaluation.

Correctness calibration, fitted-versus-empirical buzz timing, difficulty
curves over observed buzz locations, and the fitted pyramidal player/tossup
parameter distributions. 'evaluate_tossups' is the entry point; it just
sequences the figure/metric builders below, each of which lives in its own
module by concern:

* 'parameters' -- shared helpers for reading/reconstructing saved fitted
  parameters (scalar or multidimensional difficulty).
* 'reliability' -- calibration stratified by buzz position.
* 'distributions' -- fitted player/tossup parameter density panels.
* 'difficulty' -- learned difficulty curves over empirical buzz locations.
* 'timing' -- fitted-versus-empirical first-buzz timing reconstruction.
* 'stability' -- cross-run player skill stability (used by
  'evaluate_compirt.py' when a comparison run is given, not part of the
  per-run metrics below).

Every public name below is re-exported from this package so existing
'from compirt_eval.tossups import ...' call sites keep working unchanged.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_absolute_error, median_absolute_error

from compirt_eval.figures import reliability_plot
from compirt_eval.metrics import classification_metrics
from compirt_eval.outputs import graph_path
from compirt_eval.tossups.difficulty import (
    difficulty_plot,
    evenly_spaced_ids,
    multidim_difficulty_components_plot,
    selected_tossups,
    tossup_observation_summary,
)
from compirt_eval.tossups.distributions import pyramidal_parameter_distribution_plots
from compirt_eval.tossups.reliability import stratified_tossup_reliability_plot
from compirt_eval.tossups.stability import player_skill_stability_plot
from compirt_eval.tossups.timing import buzz_density_fit_plot, first_buzz_distribution

__all__ = [
    "buzz_density_fit_plot",
    "difficulty_plot",
    "evaluate_tossups",
    "evenly_spaced_ids",
    "first_buzz_distribution",
    "multidim_difficulty_components_plot",
    "player_skill_stability_plot",
    "pyramidal_parameter_distribution_plots",
    "selected_tossups",
    "stratified_tossup_reliability_plot",
    "tossup_observation_summary",
]


def evaluate_tossups(results_dir, output_dir):
    """Evaluate first-buzz correctness and expected first-buzz position."""
    buzz = pd.read_csv(results_dir / "tossup_predictions.csv")
    # Only actual buzzers have an observed correctness outcome.
    buzz = buzz[buzz["z"] == "BUZZ"]
    metrics = classification_metrics(buzz["y"], buzz["predicted_correct"])
    if not buzz.empty:
        reliability_plot(
            buzz["y"],
            buzz["predicted_correct"],
            "Tossup correctness reliability",
            graph_path(output_dir, "tossup_reliability.png"),
        )
        stratified_tossup_reliability_plot(buzz, output_dir)
    difficulty_plot(results_dir, output_dir)
    multidim_difficulty_components_plot(results_dir, output_dir)
    buzz_density_fit_plot(results_dir, output_dir)
    pyramidal_parameter_distribution_plots(results_dir, output_dir)

    position_path = results_dir / "buzz_event_predictions.csv"
    if position_path.exists():
        # Position predictions already contain one row per first-buzz event.
        events = pd.read_csv(position_path)
        metrics.update(
            {
                "buzz_position_mae": mean_absolute_error(
                    events["observed_relative_position"],
                    events["predicted_relative_position"],
                ),
                "buzz_position_median_absolute_error": median_absolute_error(
                    events["observed_relative_position"],
                    events["predicted_relative_position"],
                ),
            }
        )
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.scatter(
            events["observed_relative_position"],
            events["predicted_relative_position"],
            alpha=0.25,
        )
        ax.plot([0, 1], [0, 1], "--", color="0.5")
        ax.set(
            title="Observed versus predicted buzz position",
            xlabel="Observed",
            ylabel="Predicted",
            xlim=(0, 1),
            ylim=(0, 1),
        )
        ax.grid(alpha=0.25)
        fig.tight_layout()
        fig.savefig(graph_path(output_dir, "tossup_position_predictions.png"), dpi=160)
        plt.close(fig)
    return metrics
