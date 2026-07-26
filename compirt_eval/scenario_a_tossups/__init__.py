"""Scenario A: tossup first-buzz evaluation.

Correctness calibration, fitted-versus-empirical buzz timing, difficulty
curves over observed buzz locations, and the fitted pyramidal player/tossup
parameter distributions. 'evaluate_tossups' is the entry point; it just
sequences the figure/metric builders below, each of which lives in its own
module by concern:

* 'parameters' -- shared helpers for reading/reconstructing saved fitted
  parameters (scalar or multidimensional difficulty).
* 'metrics' -- tossup event and buzz-position scoring calculations.
* 'reliability' -- calibration stratified by buzz position.
* 'position' -- buzz-position error summaries and figures.
* 'distributions' -- fitted player/tossup parameter density panels.
* 'difficulty' -- learned difficulty curves over empirical buzz locations.
* 'timing' -- fitted-versus-empirical first-buzz timing reconstruction.

The orchestration entry point lives in `evaluation`. The names in `__all__`
define the current supported package-level import surface.
"""

from __future__ import annotations

from compirt_eval.scenario_a_tossups.difficulty import (
    difficulty_plot,
    evenly_spaced_ids,
    multidim_difficulty_components_plot,
    selected_tossups,
    tossup_observation_summary,
)
from compirt_eval.scenario_a_tossups.distributions import pyramidal_parameter_distribution_plots
from compirt_eval.scenario_a_tossups.evaluation import evaluate_tossups
from compirt_eval.scenario_a_tossups.metrics import (
    buzz_position_bias_table,
    tossup_joint_event_scores,
)
from compirt_eval.scenario_a_tossups.reliability import stratified_tossup_reliability_plot
from compirt_eval.scenario_a_tossups.timing import (
    buzz_density_fit_plot,
    evaluate_survival_and_first_buzzer,
    first_buzz_distribution,
)

__all__ = [
    "buzz_density_fit_plot",
    "buzz_position_bias_table",
    "difficulty_plot",
    "evaluate_tossups",
    "evaluate_survival_and_first_buzzer",
    "evenly_spaced_ids",
    "first_buzz_distribution",
    "multidim_difficulty_components_plot",
    "pyramidal_parameter_distribution_plots",
    "selected_tossups",
    "stratified_tossup_reliability_plot",
    "tossup_observation_summary",
    "tossup_joint_event_scores",
]
