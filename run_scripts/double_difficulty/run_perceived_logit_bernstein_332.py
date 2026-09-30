#!/usr/bin/env python3
"""Run scalar perceived-logit Bernstein 332 over frozen matrix holdout folds."""

from __future__ import annotations

import json
import shlex
import subprocess
from dataclasses import asdict
from pathlib import Path

from run_scripts.double_difficulty import run_perceived_difficulty_bernstein_332 as shared
from utils.run_logging import resolve_result_root


REPO_ROOT = shared.REPO_ROOT
PYTHON = shared.PYTHON
FOLD_COUNT = shared.FOLD_COUNT
TRAIN_MODULE = (
    "hazard_double_difficulty.perceived_logit_bernstein.train_pyramidal"
)
EVALUATE_MODULE = shared.EVALUATE_MODULE
DEFAULT_ROOT = Path(
    "results/compirt/holdout/double-difficulty/"
    "variants/perception/perceived-logit/positive-alpha"
)
Configuration = shared.Configuration
snapshot_configuration = shared.snapshot_configuration
collect_per_fold = shared.collect_per_fold
aggregate = shared.aggregate


def experiment_commands(config: Configuration, fold: int):
    """Return train, frozen replay, and evaluation stages for one fold."""
    run_dir = Path(config.root) / f"fold_{fold}"
    train_dir = run_dir / "train" / "pyramidal"
    holdout_dir = run_dir / "holdout" / "pyramidal"
    evaluation_dir = run_dir / "evaluation"
    train_split = shared.game_holdout_split_name(
        config.base_split, "train", FOLD_COUNT, fold, config.split_seed
    )
    test_split = shared.game_holdout_split_name(
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


def run_fold(config: Configuration, fold: int, *, dry_run=False, rerun=False):
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


def parse_args(argv=None):
    arguments = list(argv) if argv is not None else None
    if arguments is not None and "--root" not in arguments:
        arguments.extend(["--root", str(DEFAULT_ROOT)])
    args = shared.parse_args(arguments)
    if argv is None and args.root == shared.DEFAULT_ROOT:
        args.root = DEFAULT_ROOT
    return args


def main(argv=None):
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
            run_fold(config, fold, dry_run=args.dry_run, rerun=args.rerun)
    if not args.dry_run:
        aggregate(config)


if __name__ == "__main__":
    main()
