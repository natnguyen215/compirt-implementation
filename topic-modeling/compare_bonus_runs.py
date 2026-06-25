#!/usr/bin/env python3
"""Print bonus metrics side by side across CompIRT runs.

Reads each run's synergy-evaluation/bonus_metrics.csv (falling back to
evaluation/bonus_metrics.csv) and prints the columns that matter for the
points-per-bonus question, so the new all-2024 topic+synergy run can be
compared head-to-head with the existing baselines.

Usage:
    python topic-modeling/compare_bonus_runs.py \
        results/compirt/plda-all2024 \
        results/compirt/baseline-all2024 \
        results/compirt/topic_compirt_5d_syn
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

COLUMNS = [
    "ppb_mae",
    "per_bonus_points_mae",
    "exact_score_accuracy",
    "auc",
    "ece",
]
DEFAULT_RUNS = [
    "results/compirt/plda-all2024",
    "results/compirt/baseline-all2024",
    "results/compirt/topic_compirt_5d_syn",
]


def load_run(run_dir: Path) -> dict[str, object]:
    """Return one metrics row for a run, preferring the synergy evaluation."""
    for sub in ("synergy-evaluation", "evaluation"):
        path = run_dir / sub / "bonus_metrics.csv"
        if path.exists():
            row = pd.read_csv(path).iloc[0].to_dict()
            row["run"] = run_dir.name
            row["eval"] = sub
            return row
    return {"run": run_dir.name, "eval": "MISSING"}


def main() -> None:
    """Print the selected bonus metrics for each run directory side by side."""
    runs = [Path(arg) for arg in sys.argv[1:]] or [Path(p) for p in DEFAULT_RUNS]
    frame = pd.DataFrame(load_run(run) for run in runs)
    present = [column for column in COLUMNS if column in frame.columns]
    ordered = frame[["run", "eval", *present]]
    with pd.option_context("display.float_format", "{:.4f}".format):
        print(ordered.to_string(index=False))


if __name__ == "__main__":
    main()
