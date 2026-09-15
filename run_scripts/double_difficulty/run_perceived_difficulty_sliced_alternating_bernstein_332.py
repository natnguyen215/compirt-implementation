#!/usr/bin/env python3
"""Run alternating three-slice perceived-difficulty Bernstein 332 folds."""

from __future__ import annotations

from pathlib import Path

from run_scripts.double_difficulty import run_perceived_difficulty_bernstein_332 as shared


PERCEPTION_SLICES = 3
TRAIN_EXTRA_ARGS = ("--alternate-player-steps",)
DEFAULT_ROOT = Path(
    "results/compirt/holdout/double-difficulty/"
    "variants/perceived-difficulty/three-slice-alternating"
)
Configuration = shared.Configuration


def experiment_commands(config: Configuration, fold: int):
    """Return alternating train, frozen replay, and evaluation commands."""
    return shared.experiment_commands(
        config,
        fold,
        perception_slices=PERCEPTION_SLICES,
        train_extra_args=TRAIN_EXTRA_ARGS,
    )


def main(argv=None):
    shared.main(
        argv,
        default_root=DEFAULT_ROOT,
        perception_slices=PERCEPTION_SLICES,
        train_extra_args=TRAIN_EXTRA_ARGS,
    )


if __name__ == "__main__":
    main()
