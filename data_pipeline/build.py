#!/usr/bin/env python3
"""CLI entry point: build and validate the local quizbowl IRT dataset.

Thin wrapper around 'data_pipeline.dataset.build_dataset_directory', which
does the actual reading (SQLite -> 'BuiltRecords'), writing (HuggingFace
tables + response matrix CSV), and validation. See that module's docstring
for the pipeline overview.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from data_pipeline.dataset import build_dataset_directory


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-path", type=Path, default=ROOT / "data" / "database.db")
    parser.add_argument(
        "--output-dir", type=Path, default=ROOT / "data" / "hf" / "quizbowl-irt"
    )
    parser.add_argument(
        "--response-matrix",
        type=Path,
        default=ROOT / "data" / "response_matrix.csv",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Replace existing outputs only after the new build validates.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = build_dataset_directory(
        db_path=args.db_path.expanduser(),
        output_dir=args.output_dir.expanduser(),
        response_matrix_path=args.response_matrix.expanduser(),
        overwrite=args.overwrite,
    )
    print(json.dumps(report["output_counts"], indent=2, sort_keys=True))
    print(f"Wrote and validated dataset at {args.output_dir}")
    print(f"Wrote response matrix at {args.response_matrix}")


if __name__ == "__main__":
    main()
