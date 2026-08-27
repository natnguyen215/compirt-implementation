#!/usr/bin/env python3
"""Run the sigmoid, simplex-relevance, terminal double-difficulty model.

This is the sigmoid counterpart to the selected full double-Bernstein arm. It
keeps separate correctness/hazard curves, independent simplex relevance
vectors, three latent dimensions by default, and separate final-cell
intercepts. Each fold trains on whole games, freezes the fitted item/player
parameters, replays the held-out fold, and evaluates the frozen predictions.
"""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path

import pandas as pd

from holdout.game_splits import game_holdout_split_name
from holdout.aggregate_reports import write_correctness_markdown
from run_scripts.bernstein.run_dd_bernstein_ablation import (
    _metric_row,
    _pooled_scores,
)
from utils.run_logging import resolve_result_root


REPO_ROOT = Path(__file__).resolve().parents[3]
PYTHON = str(REPO_ROOT / ".venv" / "bin" / "python")
FOLD_COUNT = 5
TRAIN_MODULE = "hazard_double_difficulty.multidim.train_pyramidal"
EVALUATE_MODULE = "run_scripts.paper_model_selection.evaluate_fold"
DEFAULT_ROOT = Path(
    "results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid"
)


@dataclass(frozen=True)
class Configuration:
    root: str
    base_split: str
    folds: list[int]
    split_seed: int
    optimization_seed: int
    dimensions: int
    steps: int
    lr: float
    device: str
    posterior_draws: int
    data_dir: str | None


def experiment_commands(config: Configuration, fold: int):
    """Build the train, frozen-replay, and evaluation commands for one fold."""
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
        "--dimensions",
        str(config.dimensions),
        "--difficulty-link",
        "sigmoid",
        "--relevance-prior",
        "simplex",
        "--terminal-intercepts",
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
        "--difficulty-link",
        "sigmoid",
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
    """Persist the resume contract and reject incompatible reuse of a root."""
    root = Path(config.root)
    root.mkdir(parents=True, exist_ok=True)
    path = root / "configuration.json"
    expected = asdict(config)
    if path.exists():
        if json.loads(path.read_text(encoding="utf-8")) != expected:
            raise SystemExit(f"Incompatible configuration at {path}; use a new --root.")
    else:
        path.write_text(json.dumps(expected, indent=2) + "\n", encoding="utf-8")


def run_fold(config: Configuration, fold: int, *, dry_run=False, rerun=False) -> None:
    run_dir, stages = experiment_commands(config, fold)
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
        for name, _, command in stages:
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


def aggregate(config: Configuration) -> None:
    """Write per-fold, fold mean/std, and pooled held-out metrics."""
    rows = []
    root = Path(config.root)
    for fold in config.folds:
        run_dir = root / f"fold_{fold}"
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
                "relevance_prior": summary.get("relevance_prior_family"),
                "terminal_intercepts": summary.get("terminal_intercepts"),
                "difficulty_link": summary.get("difficulty_link"),
                "effective_parameter_count": summary.get("effective_parameter_count"),
                **_metric_row(run_dir / "evaluation" / "csvs" / "tossup_metrics.csv"),
            }
        )
    aggregate_dir = root / "aggregate"
    aggregate_dir.mkdir(parents=True, exist_ok=True)
    per_fold = pd.DataFrame(rows)
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
        dimensions=config.dimensions,
        relevance_prior="simplex",
        terminal_intercepts=True,
        difficulty_link="sigmoid",
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


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--base-split", default="year_2024")
    parser.add_argument("--folds", nargs="+", type=int, default=list(range(FOLD_COUNT)))
    parser.add_argument("--split-seed", type=int, default=42)
    parser.add_argument("--optimization-seed", type=int, default=42)
    parser.add_argument("--dimensions", type=int, default=3)
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
    if args.dimensions < 1:
        parser.error("--dimensions must be at least 1")
    if args.steps < 1:
        parser.error("--steps must be at least 1")
    if args.posterior_draws < 0:
        parser.error("--posterior-draws must be non-negative")
    if args.collect_only and (args.dry_run or args.rerun):
        parser.error("--collect-only cannot be combined with --dry-run or --rerun")
    return args


def main(argv=None) -> None:
    args = parse_args(argv)
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
        dimensions=args.dimensions,
        steps=args.steps,
        lr=args.lr,
        device=args.device,
        posterior_draws=args.posterior_draws,
        data_dir=data_dir,
    )
    if args.collect_only:
        aggregate(config)
        return
    if not args.dry_run:
        snapshot_configuration(config)
    print(
        f"double-sigmoid dimensions={config.dimensions} relevance=simplex "
        f"terminal_intercepts=True on {config.base_split}: "
        f"{len(config.folds)} frozen matrix-infill folds",
        flush=True,
    )
    for fold in config.folds:
        run_fold(config, fold, dry_run=args.dry_run, rerun=args.rerun)
    if not args.dry_run:
        aggregate(config)


if __name__ == "__main__":
    main()
