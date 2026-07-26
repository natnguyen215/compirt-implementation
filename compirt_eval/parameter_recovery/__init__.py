"""Standalone synthetic parameter-recovery study.

The study generates and refits synthetic data, so it is intentionally separate
from the replay-only standard evaluator and cross-cutting diagnostics.
"""

from .evaluation import generate_recovery_data, run_parameter_recovery

__all__ = ["generate_recovery_data", "run_parameter_recovery"]
