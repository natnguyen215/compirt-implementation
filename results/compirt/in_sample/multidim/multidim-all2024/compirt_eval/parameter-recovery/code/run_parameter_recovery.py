#!/usr/bin/env python3
"""Run the bounded synthetic multidimensional parameter-recovery study."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_eval.parameter_recovery import run_parameter_recovery


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--steps", type=int, default=800)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--players", type=int, default=12)
    parser.add_argument("--tossups", type=int, default=16)
    parser.add_argument("--events", type=int, default=160)
    return parser.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)
    run_parameter_recovery(
        args.output_dir,
        steps=args.steps,
        seed=args.seed,
        players=args.players,
        tossups=args.tossups,
        events=args.events,
    )


if __name__ == "__main__":
    main()
