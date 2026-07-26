#!/usr/bin/env python3
"""Compare saved no-synergy and synergy bonus evaluation metrics."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_eval.synergy_comparison import compare_bonus_models


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--compositional-metrics", type=Path, required=True)
    parser.add_argument("--synergy-metrics", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv=None) -> None:
    args = parse_args(argv)
    compare_bonus_models(
        compositional_metrics=args.compositional_metrics,
        synergy_metrics=args.synergy_metrics,
        output_dir=args.output_dir,
    )


if __name__ == "__main__":
    main()
