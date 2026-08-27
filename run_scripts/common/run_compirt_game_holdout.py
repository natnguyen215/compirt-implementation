#!/usr/bin/env python3
"""Frozen matrix-infill CompIRT runner over a stratified whole-game k-fold split.

This is a thin orchestration layer over ``run_compirt_holdout.py``.  It holds
out whole games spread evenly across every tournament and round (see
``holdout.game_splits``) and scores them with **train-frozen** parameters -- no
SVI on the test outcomes -- answering the matrix-infill question: given players
and questions estimated on the training games, can the model fill in the
held-out player x question interactions?

Each of ``N_FOLDS`` folds is run once as its own held-out pass (train on the
other folds, freeze, score the fold) into ``<ROOT>/fold_<k>``, then the
per-fold metric CSVs are aggregated into ``<ROOT>/aggregate`` (mean +/- std
across folds).

Environment variables:

* ``BASE_SPLIT`` (default ``year_2024``)
* ``N_FOLDS`` (default ``5``)
* ``SPLIT_SEED`` (default ``42``)
* every variable accepted by ``run_compirt_holdout.py`` (``MODEL``, ``ROOT``,
  ``DIMENSIONS``, ``RUN_SYNERGY``, training settings, and so on).  ``MODEL`` must
  be ``multidim`` -- the only family the frozen scorer supports.

``TRAIN_SPLIT`` / ``TEST_SPLIT`` and ``FROZEN_PREDICT`` are derived by this
wrapper and may not be set directly.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from holdout.game_splits import game_holdout_split_name
from holdout.aggregate_reports import (
    add_in_sample_correctness_metrics,
    add_in_sample_main_table_fold_means,
    add_main_table_fold_means,
    pooled_correctness_metrics,
    write_correctness_markdown,
)
from utils.run_logging import resolve_result_root

PYTHON = Path(os.environ.get("PYTHON", str(REPO_ROOT / ".venv" / "bin" / "python")))

# (evaluation subdir, metric filename) pairs aggregated across folds.
AGGREGATED_METRICS = [
    ("evaluation", "tossup_metrics.csv"),
    ("evaluation", "bonus_metrics.csv"),
    ("evaluation", "game_metrics.csv"),
    ("synergy-evaluation", "bonus_metrics.csv"),
]


def resolve_settings() -> tuple[str, int, int, str]:
    """Return (base_split, n_folds, seed, root) and reject conflicting env."""
    for forbidden in ("TRAIN_SPLIT", "TEST_SPLIT", "FROZEN_PREDICT"):
        if forbidden in os.environ:
            raise SystemExit(
                "run_compirt_game_holdout derives TRAIN_SPLIT, TEST_SPLIT, and "
                f"FROZEN_PREDICT; do not set {forbidden}"
            )
    model = os.environ.get("MODEL", "baseline")
    if model != "multidim":
        raise SystemExit(
            f"MODEL must be 'multidim' for frozen matrix infill; got {model!r}"
        )
    base_split = os.environ.get("BASE_SPLIT", "year_2024")
    try:
        n_folds = int(os.environ.get("N_FOLDS", "5"))
        seed = int(os.environ.get("SPLIT_SEED", "42"))
    except ValueError as error:
        raise SystemExit(f"N_FOLDS and SPLIT_SEED must be integers: {error}") from error
    if n_folds < 2:
        raise SystemExit("N_FOLDS must be at least 2")
    root = resolve_result_root(
        os.environ.get("ROOT", f"results/compirt/holdout/common/game-infill/{model}"),
        "holdout",
    )
    return base_split, n_folds, seed, root


def run_fold(base_split: str, n_folds: int, fold: int, seed: int, root: str) -> None:
    """Run one held-out frozen fold as its own logged ``run_compirt_holdout``."""
    env = dict(os.environ)
    env["FROZEN_PREDICT"] = "1"
    env["TRAIN_SPLIT"] = game_holdout_split_name(base_split, "train", n_folds, fold, seed)
    env["TEST_SPLIT"] = game_holdout_split_name(base_split, "test", n_folds, fold, seed)
    env["ROOT"] = f"{root}/fold_{fold}"
    # Each fold is its own subprocess so it gets its own run.log tee.
    env.pop("COMPIRT_LOG_ACTIVE", None)
    print(f"=== fold {fold}/{n_folds - 1}: {env['TEST_SPLIT']} ===", flush=True)
    subprocess.run(
        [str(PYTHON), "-m", "run_scripts.common.run_compirt_holdout"],
        cwd=REPO_ROOT,
        env=env,
        check=True,
    )


def aggregate_folds(root: str, n_folds: int) -> None:
    """Stack each fold's single-row metric CSVs and report mean +/- std."""
    aggregate_dir = Path(root) / "aggregate"
    aggregate_dir.mkdir(parents=True, exist_ok=True)
    summary_lines = ["# Game-infill 5-fold aggregate", "", f"Folds: {n_folds}", ""]

    for subdir, filename in AGGREGATED_METRICS:
        rows = []
        for fold in range(n_folds):
            path = Path(root) / f"fold_{fold}" / "holdout" / subdir / "csvs" / filename
            if not path.exists():
                continue
            frame = pd.read_csv(path)
            if frame.empty:
                continue
            rows.append({"fold": fold, **frame.iloc[0].to_dict()})
        if not rows:
            continue
        label = f"{subdir}_{filename[:-4]}"
        by_fold = pd.DataFrame(rows)
        by_fold.to_csv(aggregate_dir / f"byfold_{label}.csv", index=False)

        numeric = by_fold.drop(columns=["fold"]).apply(pd.to_numeric, errors="coerce")
        numeric = numeric.dropna(axis=1, how="all")
        stats = pd.DataFrame(
            {
                "metric": numeric.columns,
                "mean": numeric.mean().to_numpy(),
                "std": numeric.std().to_numpy(),
                "n_folds": numeric.count().to_numpy(),
            }
        )
        stats.to_csv(aggregate_dir / f"stats_{label}.csv", index=False)

        summary_lines.append(f"## {label} ({len(rows)} folds)")
        summary_lines.append("")
        summary_lines.append("| metric | mean | std | n_folds |")
        summary_lines.append("| --- | --- | --- | --- |")
        for _, srow in stats.iterrows():
            summary_lines.append(
                f"| {srow['metric']} | {srow['mean']:.6g} | "
                f"{srow['std']:.6g} | {int(srow['n_folds'])} |"
            )
        summary_lines.append("")

    (aggregate_dir / "summary.md").write_text(
        "\n".join(summary_lines).rstrip() + "\n", encoding="utf-8"
    )
    run_dirs = [
        Path(root) / f"fold_{fold}"
        for fold in range(n_folds)
        if (
            Path(root)
            / f"fold_{fold}"
            / "train"
            / "pyramidal"
            / "tossup_predictions.csv"
        ).exists()
        and (
            Path(root)
            / f"fold_{fold}"
            / "holdout"
            / "pyramidal"
            / "tossup_predictions.csv"
        ).exists()
    ]
    if run_dirs:
        correctness: dict[str, object] = pooled_correctness_metrics(
            run_dirs, split="holdout"
        )
        add_in_sample_correctness_metrics(correctness, run_dirs)
        add_in_sample_main_table_fold_means(correctness, run_dirs)
        add_main_table_fold_means(correctness, run_dirs)
        write_correctness_markdown(
            correctness,
            aggregate_dir / "correctness_metrics.md",
            title=f"{Path(root).name} correctness summary",
        )
    print(f"Aggregated metrics in {aggregate_dir}")


def main() -> None:
    base_split, n_folds, seed, root = resolve_settings()
    Path(root).mkdir(parents=True, exist_ok=True)
    print(
        f"Game-infill matrix holdout: base_split={base_split} n_folds={n_folds} "
        f"seed={seed} root={root}",
        flush=True,
    )
    for fold in range(n_folds):
        run_fold(base_split, n_folds, fold, seed, root)
    aggregate_folds(root, n_folds)
    print(f"Finished {n_folds}-fold frozen matrix-infill run under {root}.")


if __name__ == "__main__":
    main()
