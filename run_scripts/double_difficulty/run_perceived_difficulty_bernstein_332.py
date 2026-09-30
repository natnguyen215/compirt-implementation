#!/usr/bin/env python3
"""Run perceived-difficulty Bernstein 332 over frozen matrix holdout folds."""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from holdout.game_splits import game_holdout_split_name
from holdout.aggregate_reports import write_correctness_markdown
from run_scripts.double_difficulty.run_dd_bernstein_ablation import (
    _metric_row,
    _pooled_scores,
)
from utils.run_logging import resolve_result_root


PYTHON = str(REPO_ROOT / ".venv" / "bin" / "python")
FOLD_COUNT = 5
TRAIN_MODULE = (
    "hazard_double_difficulty.perceived_difficulty_bernstein.train_pyramidal"
)
EVALUATE_MODULE = "run_scripts.double_difficulty.evaluate_fold"
DEFAULT_ROOT = Path(
    "results/compirt/holdout/double-difficulty/"
    "variants/perception/perceived-difficulty/positive-alpha"
)


@dataclass(frozen=True)
class Configuration:
    root: str
    base_split: str
    folds: list[int]
    split_seed: int
    optimization_seed: int
    degree: int
    dimensions: int
    relevance_concentration: float
    drop_concentration: float
    steps: int
    lr: float
    device: str
    posterior_draws: int
    data_dir: str | None


def experiment_commands(
    config: Configuration,
    fold: int,
    *,
    perception_slices: int = 1,
    train_extra_args=(),
):
    run_dir = Path(config.root) / f"fold_{fold}"
    train_dir = run_dir / "train" / "pyramidal"
    holdout_dir = run_dir / "holdout" / "pyramidal"
    evaluation_dir = run_dir / "evaluation"
    train_split = game_holdout_split_name(
        config.base_split, "train", FOLD_COUNT, fold, config.split_seed
    )
    test_split = game_holdout_split_name(
        config.base_split, "test", FOLD_COUNT, fold, config.split_seed
    )
    data_args = ["--data-dir", config.data_dir] if config.data_dir else []
    train = [
        PYTHON,
        "-m",
        TRAIN_MODULE,
        "--split",
        train_split,
        *data_args,
        "--degree",
        str(config.degree),
        "--dimensions",
        str(config.dimensions),
        *(
            ["--perception-slices", str(perception_slices)]
            if perception_slices != 1
            else []
        ),
        "--relevance-concentration",
        str(config.relevance_concentration),
        "--drop-concentration",
        str(config.drop_concentration),
        "--steps",
        str(config.steps),
        "--lr",
        str(config.lr),
        "--seed",
        str(config.optimization_seed),
        "--device",
        config.device,
        "--posterior-draws",
        str(config.posterior_draws),
        *train_extra_args,
        "--output-dir",
        str(train_dir),
    ]
    frozen = [
        PYTHON,
        "-m",
        "holdout.frozen_predict",
        "tossup",
        "--split",
        test_split,
        *data_args,
        "--train-pyramidal",
        str(train_dir),
        "--dimensions",
        str(config.dimensions),
        "--device",
        config.device,
        "--output-dir",
        str(holdout_dir),
    ]
    evaluate = [
        PYTHON,
        "-m",
        EVALUATE_MODULE,
        "--pyramidal-results",
        str(holdout_dir),
        "--output-dir",
        str(evaluation_dir),
    ]
    return run_dir, [
        ("train", train_dir / "summary.json", train),
        ("frozen-replay", holdout_dir / "summary.json", frozen),
        ("evaluation", evaluation_dir / "csvs" / "tossup_metrics.csv", evaluate),
    ]


def snapshot_configuration(config: Configuration) -> None:
    path = Path(config.root) / "configuration.json"
    expected = asdict(config)
    if path.exists():
        if json.loads(path.read_text(encoding="utf-8")) != expected:
            raise SystemExit(
                f"Incompatible resume configuration at {path}; use a new --root."
            )
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(expected, indent=2) + "\n", encoding="utf-8")


def run_fold(
    config: Configuration,
    fold: int,
    *,
    dry_run=False,
    rerun=False,
    perception_slices: int = 1,
    train_extra_args=(),
):
    run_dir, stages = experiment_commands(
        config,
        fold,
        perception_slices=perception_slices,
        train_extra_args=train_extra_args,
    )
    marker = run_dir / ".complete.json"
    manifest = {
        "fold": fold,
        "configuration": asdict(config),
        "stages": [
            {"name": name, "expected_output": str(expected), "command": command}
            for name, expected, command in stages
        ],
    }
    if marker.exists() and not rerun:
        print(f"resume complete: {run_dir}", flush=True)
        return
    if dry_run:
        for name, _expected, command in stages:
            print(f"[{name}] {shlex.join(command)}")
        return
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "command.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    print(f"\n=== fold {fold} ===", flush=True)
    for name, expected, command in stages:
        if expected.exists() and not rerun:
            print(f"resume stage {name}: {expected}", flush=True)
            continue
        print("+ " + shlex.join(command), flush=True)
        subprocess.run(command, cwd=REPO_ROOT, check=True)
    marker.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def collect_per_fold(config: Configuration) -> pd.DataFrame:
    rows = []
    for fold in config.folds:
        run_dir = Path(config.root) / f"fold_{fold}"
        summary_path = run_dir / "train" / "pyramidal" / "summary.json"
        summary = (
            json.loads(summary_path.read_text(encoding="utf-8"))
            if summary_path.exists()
            else {}
        )
        rows.append(
            {
                "fold": fold,
                "complete": (run_dir / ".complete.json").exists(),
                "run_path": str(run_dir),
                "effective_parameter_count": summary.get(
                    "effective_parameter_count"
                ),
                "final_loss": summary.get("final_loss"),
                "best_loss": summary.get("best_loss"),
                "last_100_loss_slope": summary.get("last_100_loss_slope"),
                "finite_losses": summary.get("finite_losses"),
                **_metric_row(
                    run_dir / "evaluation" / "csvs" / "tossup_metrics.csv"
                ),
            }
        )
    return pd.DataFrame(rows)


def aggregate(config: Configuration) -> None:
    aggregate_dir = Path(config.root) / "aggregate"
    aggregate_dir.mkdir(parents=True, exist_ok=True)
    per_fold = collect_per_fold(config)
    per_fold.to_csv(aggregate_dir / "per_fold.csv", index=False)
    complete = per_fold[per_fold["complete"]]
    numeric = complete.select_dtypes("number").drop(columns=["fold"], errors="ignore")
    if not numeric.empty:
        pd.DataFrame(
            {"metric": numeric.columns, "mean": numeric.mean(), "std": numeric.std()}
        ).to_csv(aggregate_dir / "fold_mean_std.csv", index=False)
    pooled = _pooled_scores([Path(path) for path in complete["run_path"]])
    pooled.update(
        base_split=config.base_split,
        degree=config.degree,
        dimensions=config.dimensions,
        relevance_concentration=config.relevance_concentration,
        drop_concentration=config.drop_concentration,
        complete_folds=int(len(complete)),
        requested_folds=len(config.folds),
    )
    pd.DataFrame([pooled]).to_csv(aggregate_dir / "pooled.csv", index=False)
    write_correctness_markdown(
        pooled,
        aggregate_dir / "correctness_metrics.md",
        title=f"{Path(config.root).name} correctness summary",
    )
    print(f"Aggregate results: {aggregate_dir}", flush=True)


def parse_args(argv=None, *, default_root=DEFAULT_ROOT):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument("--base-split", default="year_2024")
    parser.add_argument("--folds", nargs="+", type=int, default=list(range(5)))
    parser.add_argument("--split-seed", type=int, default=42)
    parser.add_argument("--optimization-seed", type=int, default=42)
    parser.add_argument("--degree", type=int, default=3)
    parser.add_argument("--dimensions", type=int, default=3)
    parser.add_argument("--relevance-concentration", type=float, default=2.0)
    parser.add_argument("--drop-concentration", type=float, default=2.0)
    parser.add_argument("--steps", type=int, default=3000)
    parser.add_argument("--lr", type=float, default=0.005)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument("--posterior-draws", type=int, default=0)
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--collect-only", action="store_true")
    parser.add_argument("--rerun", action="store_true")
    args = parser.parse_args(argv)
    if not args.folds or any(fold not in range(FOLD_COUNT) for fold in args.folds):
        parser.error("--folds must be selected from 0 1 2 3 4")
    if args.dimensions < 1 or args.steps < 1:
        parser.error("--dimensions and --steps must be positive")
    if args.posterior_draws < 0:
        parser.error("--posterior-draws must be non-negative")
    if args.relevance_concentration <= 0 or args.drop_concentration <= 0:
        parser.error("Dirichlet concentrations must be positive")
    if args.collect_only and (args.dry_run or args.rerun):
        parser.error("--collect-only cannot be combined with --dry-run or --rerun")
    return args


def main(
    argv=None,
    *,
    default_root=DEFAULT_ROOT,
    perception_slices: int = 1,
    train_extra_args=(),
):
    args = parse_args(argv, default_root=default_root)
    args.root = Path(resolve_result_root(args.root, "holdout"))
    root = args.root if args.root.is_absolute() else REPO_ROOT / args.root
    data_dir = None
    if args.data_dir is not None:
        path = args.data_dir if args.data_dir.is_absolute() else REPO_ROOT / args.data_dir
        data_dir = str(path)
    config = Configuration(
        root=str(root),
        base_split=args.base_split,
        folds=args.folds,
        split_seed=args.split_seed,
        optimization_seed=args.optimization_seed,
        degree=args.degree,
        dimensions=args.dimensions,
        relevance_concentration=args.relevance_concentration,
        drop_concentration=args.drop_concentration,
        steps=args.steps,
        lr=args.lr,
        device=args.device,
        posterior_draws=args.posterior_draws,
        data_dir=data_dir,
    )
    if not args.dry_run:
        snapshot_configuration(config)
    if not args.collect_only:
        for fold in config.folds:
            run_fold(
                config,
                fold,
                dry_run=args.dry_run,
                rerun=args.rerun,
                perception_slices=perception_slices,
                train_extra_args=train_extra_args,
            )
    if not args.dry_run:
        aggregate(config)


if __name__ == "__main__":
    main()
