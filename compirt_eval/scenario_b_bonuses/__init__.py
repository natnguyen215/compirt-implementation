"""Scenario B: bonus-part and points-per-bonus evaluation.

``metrics`` owns pure bonus scoring, ``distributions`` owns fitted-parameter
diagnostics, and ``evaluation`` orchestrates saved predictions and figures.
"""

from compirt_eval.scenario_b_bonuses.distributions import (
    bonus_parameter_distribution_plots,
)
from compirt_eval.scenario_b_bonuses.evaluation import evaluate_bonuses
from compirt_eval.scenario_b_bonuses.metrics import (
    bonus_metrics,
    bonus_ranked_probability_scores,
    bonus_score_distribution,
)

__all__ = [
    "bonus_metrics",
    "bonus_parameter_distribution_plots",
    "bonus_ranked_probability_scores",
    "bonus_score_distribution",
    "evaluate_bonuses",
]
