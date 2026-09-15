"""Scenario A: tossup first-buzz evaluation.

Correctness calibration, fitted-versus-empirical buzz timing, difficulty
curves over observed buzz locations, and the fitted pyramidal player/tossup
parameter distributions. 'evaluate_tossups' is the entry point; it sequences
the figure/metric builders, each of which lives in its own module by concern:

* 'parameters' -- shared helpers for reading/reconstructing saved fitted
  parameters (scalar or multidimensional difficulty).
* 'metrics' -- tossup event and buzz-position scoring calculations.
* 'reliability' -- calibration stratified by buzz position.
* 'position' -- buzz-position error summaries and figures.
* 'distributions' -- fitted player/tossup parameter density panels.
* 'difficulty' -- learned difficulty curves over empirical buzz locations.
* 'reconstruction' -- saved inputs and first-buzz probability reconstruction.
* 'survival' -- survival, first-buzzer identity, and marked-outcome scoring.
* 'timing' -- fitted-versus-empirical first-buzz density plots.
* 'outcomes' -- question ownership, tossup-only games, and player PPG.

Import other helpers from their modules directly.
"""

from __future__ import annotations

from compirt_eval.scenario_a_tossups.evaluation import evaluate_tossups
from compirt_eval.scenario_a_tossups.reconstruction import first_buzz_distribution

__all__ = ["evaluate_tossups", "first_buzz_distribution"]
