#!/usr/bin/env python3
"""Run the compact double-Bernstein 2x2 paper ablation on frozen folds.

The four arms isolate the two global changes cleanly:

``compact-base``
    Neither learned curve locations nor terminal intercepts.
``compact-locations``
    Learned correctness/hazard population locations only.
``compact-terminal``
    Final-cell correctness/hazard intercepts only.
``compact-selected``
    Both changes: four additional global scalars in total.

Every fold trains only on whole training games, freezes all fitted parameters,
replays held-out games, and evaluates the resulting tossup predictions.  This
is matrix infill, not an in-sample or transductive test fit.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path

import pandas as pd

from compirt_eval.common.metrics import classification_metrics, negative_class_metrics
from holdout.game_splits import game_holdout_split_name


REPO_ROOT = Path(__file__).resolve().parents[2]
PYTHON = str(REPO_ROOT / ".venv" / "bin" / "python")
TRAIN_MODULE = "hazard_double_difficulty.compact_bernstein.train_pyramidal"
EVALUATE_MODULE = "run_scripts.paper_model_selection.evaluate_fold"
FOLD_COUNT = 5
EXPERIMENTS = {
    "compact-base": (),
    "compact-locations": ("--learn-curve-locations",),
    "compact-terminal": ("--terminal-intercepts",),
    "compact-selected": ("--learn-curve-locations", "--terminal-intercepts"),
}


@dataclass(frozen=True)
class Configuration:
    root: str
    base_split: str
    folds: list[int]
    split_seed: int
    optimization_seeds: list[int]
    dimensions: int
    degree: int
    drop_concentration: float
    steps: int
    lr: float
    device: str
    posterior_draws: int
    data_dir: str | None = None
    tournament: str | None = None


def selected_experiments(names):
    if not names or names == ["all"]:
        return list(EXPERIMENTS)
    unknown = sorted(set(names) - set(EXPERIMENTS))
    if unknown:
        raise ValueError(f"Unknown experiments: {', '.join(unknown)}")
    return names


def experiment_commands(config, experiment, seed, fold):
    run_dir = Path(config.root) / experiment / f"seed_{seed}" / f"fold_{fold}"
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
    tournament_args = ["--tournament", config.tournament] if config.tournament else []
    train = [
        PYTHON,
        "-m",
        TRAIN_MODULE,
        "--split",
        train_split,
        *data_args,
        *tournament_args,
        "--degree",
        str(config.degree),
        "--dimensions",
        str(config.dimensions),
        "--drop-concentration",
        str(config.drop_concentration),
        "--steps",
        str(config.steps),
        "--lr",
        str(config.lr),
        "--seed",
        str(seed),
        "--device",
        config.device,
        "--posterior-draws",
        str(config.posterior_draws),
        *EXPERIMENTS[experiment],
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
        *tournament_args,
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
        (train_dir / "summary.json", train),
        (holdout_dir / "summary.json", frozen),
        (evaluation_dir / "csvs" / "tossup_metrics.csv", evaluate),
    ]


def _run(command):
    subprocess.run(command, cwd=REPO_ROOT, check=True)


def run(config, experiments, rerun=False, dry_run=False):
    for experiment in experiments:
        for seed in config.optimization_seeds:
            for fold in config.folds:
                run_dir, stages = experiment_commands(config, experiment, seed, fold)
                print(f"\n=== {experiment} seed={seed} fold={fold} ===", flush=True)
                for marker, command in stages:
                    if marker.exists() and not rerun:
                        print(f"skip: {marker}", flush=True)
                        continue
                    print(" ".join(command), flush=True)
                    if not dry_run:
                        marker.parent.mkdir(parents=True, exist_ok=True)
                        _run(command)
                if not dry_run:
                    (run_dir / ".complete.json").write_text(
                        json.dumps(
                            {
                                "experiment": experiment,
                                "seed": seed,
                                "fold": fold,
                                "configuration": asdict(config),
                            },
                            indent=2,
                        ),
                        encoding="utf-8",
                    )


def aggregate(config, experiments):
    rows = []
    for experiment in experiments:
        for seed in config.optimization_seeds:
            for fold in config.folds:
                root = Path(config.root) / experiment / f"seed_{seed}" / f"fold_{fold}"
                path = root / "evaluation" / "csvs" / "tossup_metrics.csv"
                if not path.exists():
                    continue
                row = pd.read_csv(path).iloc[0].to_dict()
                row.update(experiment=experiment, seed=seed, fold=fold)
                rows.append(row)
    frame = pd.DataFrame(rows)
    output = Path(config.root) / "aggregate"
    output.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output / "per_fold.csv", index=False)
    if frame.empty:
        return frame
    numeric = frame.select_dtypes("number").columns.difference(["seed", "fold"])
    summary = frame.groupby("experiment")[numeric].agg(["mean", "std"])
    summary.columns = [f"{metric}_{stat}" for metric, stat in summary.columns]
    summary.reset_index().to_csv(output / "mean_std.csv", index=False)
    pooled_rows = []
    for experiment in experiments:
        paths = [
            Path(config.root)
            / experiment
            / f"seed_{seed}"
            / f"fold_{fold}"
            / "holdout"
            / "pyramidal"
            / "tossup_predictions.csv"
            for seed in config.optimization_seeds
            for fold in config.folds
        ]
        buzzes = []
        for path in paths:
            if not path.exists():
                continue
            predictions = pd.read_csv(
                path, usecols=["z", "y", "predicted_correct"]
            )
            buzzes.append(predictions[predictions["z"] == "BUZZ"])
        if not buzzes:
            continue
        pooled = pd.concat(buzzes, ignore_index=True).dropna(
            subset=["y", "predicted_correct"]
        )
        y = pooled["y"].to_numpy(dtype=float)
        probability = pooled["predicted_correct"].to_numpy(dtype=float)
        pooled_rows.append(
            {
                "experiment": experiment,
                "buzzes": len(pooled),
                **classification_metrics(y, probability),
                **negative_class_metrics(y, probability),
            }
        )
    pd.DataFrame(pooled_rows).to_csv(output / "pooled_correctness.csv", index=False)
    return frame


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        default="results/compirt/holdout/double-difficulty/model-comparisons/compact-parameterization/paper-compact-2x2",
    )
    parser.add_argument("--base-split", default="year_2024")
    parser.add_argument("--folds", nargs="+", type=int, default=list(range(FOLD_COUNT)))
    parser.add_argument("--split-seed", type=int, default=42)
    parser.add_argument("--optimization-seeds", nargs="+", type=int, default=[42])
    parser.add_argument("--dimensions", type=int, default=3)
    parser.add_argument("--degree", type=int, default=3)
    parser.add_argument("--drop-concentration", type=float, default=2.0)
    parser.add_argument("--steps", type=int, default=3000)
    parser.add_argument("--lr", type=float, default=0.02)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument("--posterior-draws", type=int, default=0)
    parser.add_argument("--data-dir")
    parser.add_argument("--tournament")
    parser.add_argument("--experiments", nargs="+", default=["all"])
    parser.add_argument("--rerun", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--aggregate-only", action="store_true")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    config = Configuration(
        root=args.root,
        base_split=args.base_split,
        folds=args.folds,
        split_seed=args.split_seed,
        optimization_seeds=args.optimization_seeds,
        dimensions=args.dimensions,
        degree=args.degree,
        drop_concentration=args.drop_concentration,
        steps=args.steps,
        lr=args.lr,
        device=args.device,
        posterior_draws=args.posterior_draws,
        data_dir=args.data_dir,
        tournament=args.tournament,
    )
    experiments = selected_experiments(args.experiments)
    if not args.aggregate_only:
        run(config, experiments, rerun=args.rerun, dry_run=args.dry_run)
    if not args.dry_run:
        aggregate(config, experiments)


if __name__ == "__main__":
    main()
