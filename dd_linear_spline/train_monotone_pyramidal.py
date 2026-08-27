"""Train a clue-aligned linear spline whose difficulty only decreases."""

from __future__ import annotations

from pathlib import Path

from dd_linear_spline.train_pyramidal import (
    DEFAULT_OUTPUT_DIR,
    parse_args as parse_linear_spline_args,
    run_experiment,
)


DEFAULT_MONOTONE_OUTPUT_DIR = (
    DEFAULT_OUTPUT_DIR.parent / "dd-monotone-linear-spline" / "pyramidal"
)


def parse_args(argv=None):
    args = parse_linear_spline_args(argv)
    if args.output_dir == DEFAULT_OUTPUT_DIR:
        args.output_dir = Path(DEFAULT_MONOTONE_OUTPUT_DIR)
    return args


if __name__ == "__main__":
    run_experiment(parse_args(), monotone_decreasing=True)
