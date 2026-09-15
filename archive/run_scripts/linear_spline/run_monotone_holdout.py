#!/usr/bin/env python3
"""Run monotone linear-spline frozen matrix infill over five game folds."""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path

from holdout.game_splits import game_holdout_split_name


REPO_ROOT = Path(__file__).resolve().parents[2]
PYTHON = REPO_ROOT / ".venv" / "bin" / "python"
FOLD_COUNT = 5
DEFAULT_ROOT = Path(
    "results/compirt/holdout/double-difficulty/model-comparisons/curve-family/"
    "monotone-linear-spline"
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
    calibrate_correctness: bool
    include_bounceback: bool


def experiment_commands(config: Configuration, fold: int):
    """Return train, frozen replay, and evaluation commands for one fold."""
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
    shared_flags = []
    if config.calibrate_correctness:
        shared_flags.append("--calibrate-correctness")
    if config.include_bounceback:
        shared_flags.append("--include-bounceback")

    train = [
        str(PYTHON),
        "-m",
        "dd_linear_spline.train_monotone_pyramidal",
        "--split",
        train_split,
        *data_args,
        "--dimensions",
        str(config.dimensions),
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
        *shared_flags,
        "--output-dir",
        str(train_dir),
    ]
    frozen = [
        str(PYTHON),
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
        *shared_flags,
        "--output-dir",
        str(holdout_dir),
    ]
    evaluate = [
        str(PYTHON),
        "-m",
        "run_scripts.paper_model_selection.evaluate_fold",
        "--pyramidal-results",
        str(holdout_dir),
        "--output-dir",
        str(evaluation_dir),
    ]
    return run_dir, [
        ("train", train_dir / "summary.json", train),
        ("frozen-replay", holdout_dir / "summary.json", frozen),
        (
            "evaluation",
            evaluation_dir / "csvs" / "tossup_metrics.csv",
            evaluate,
        ),
    ]


def snapshot_configuration(config: Configuration):
    root = Path(config.root)
    root.mkdir(parents=True, exist_ok=True)
    path = root / "configuration.json"
    expected = asdict(config)
    if path.exists():
        saved = json.loads(path.read_text(encoding="utf-8"))
        if saved != expected:
            raise SystemExit(
                f"Incompatible resume configuration at {path}; use a new --root."
            )
    else:
        path.write_text(json.dumps(expected, indent=2) + "\n", encoding="utf-8")


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
        for name, _, command in stages:
            print(f"[{name}] {shlex.join(command)}")
        return

    run_dir.mkdir(parents=True, exist_ok=True)
    command_path = run_dir / "command.json"
    command_path.write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    for name, expected, command in stages:
        if expected.exists() and not rerun:
            print(f"resume stage {name}: {expected}", flush=True)
            continue
        print("+ " + shlex.join(command), flush=True)
        subprocess.run(command, cwd=REPO_ROOT, check=True)
    marker.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--base-split", default="year_2024")
    parser.add_argument("--folds", nargs="+", type=int, default=list(range(5)))
    parser.add_argument("--split-seed", type=int, default=42)
    parser.add_argument("--optimization-seed", type=int, default=42)
    parser.add_argument("--dimensions", type=int, default=5)
    parser.add_argument("--steps", type=int, default=3000)
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument("--posterior-draws", type=int, default=0)
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--calibrate-correctness", action="store_true")
    parser.add_argument("--include-bounceback", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
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
    return args


def main(argv=None):
    args = parse_args(argv)
    root = args.root if args.root.is_absolute() else REPO_ROOT / args.root
    data_dir = None
    if args.data_dir is not None:
        path = (
            args.data_dir
            if args.data_dir.is_absolute()
            else REPO_ROOT / args.data_dir
        )
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
        calibrate_correctness=args.calibrate_correctness,
        include_bounceback=args.include_bounceback,
    )
    print(
        f"Monotone linear spline: {len(config.folds)} frozen matrix-infill "
        f"folds; root={config.root}",
        flush=True,
    )
    if not args.dry_run:
        snapshot_configuration(config)
    for fold in config.folds:
        run_fold(config, fold, dry_run=args.dry_run, rerun=args.rerun)


if __name__ == "__main__":
    main()
