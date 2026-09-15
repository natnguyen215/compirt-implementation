#!/usr/bin/env python3
"""Run three-slice perceived-difficulty Bernstein 332 over frozen folds."""

from __future__ import annotations

from pathlib import Path

from run_scripts.double_difficulty import run_perceived_difficulty_bernstein_332 as shared


PERCEPTION_SLICES = 3
DEFAULT_ROOT = Path(
    "results/compirt/holdout/double-difficulty/"
    "variants/perceived-difficulty/three-slice"
)
Configuration = shared.Configuration


def experiment_commands(config: Configuration, fold: int):
    """Return sliced train, frozen replay, and evaluation commands."""
    return shared.experiment_commands(
        config, fold, perception_slices=PERCEPTION_SLICES
    )


def main(argv=None):
    shared.main(
        argv,
        default_root=DEFAULT_ROOT,
        perception_slices=PERCEPTION_SLICES,
    )


if __name__ == "__main__":
    main()
