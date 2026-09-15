#!/usr/bin/env python3
"""Sweep latent dimensions for the two unconstrained perception models.

Each point uses the five-fold frozen game matrix-infill protocol.  The scalar
perceived-logit arm reproduces the historical unconstrained prior
``alpha ~ Normal(1, 1)``.  The three-slice perceived-difficulty arm uses
independent ``Normal(0, 1)`` priors for both alpha and beta at every
player/slice/dimension.

The aggregate report applies a plateau rule separately to each model: select
the smallest dimension whose pooled joint event log loss is within a
configurable relative tolerance of that model's best completed dimension.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-compirt")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from holdout.game_splits import game_holdout_split_name
from run_scripts.double_difficulty.run_dd_bernstein_ablation import (
    PRIMARY_METRIC,
    _metric_row,
    _pooled_scores,
)
from run_scripts.double_difficulty.perception_ablation_report import neg_f1, training_diagnostics
from utils.run_logging import resolve_result_root


PYTHON = str(REPO_ROOT / ".venv" / "bin" / "python")
FOLD_COUNT = 5
DEFAULT_ROOT = Path(
    "results/compirt/holdout/double-difficulty/"
    "ablations/perception-dimensions-unconstrained"
)
DEFAULT_DIMENSIONS = tuple(range(1, 11))
DEFAULT_MODELS = ("perceived-logit", "perceived-difficulty-three-slice")
MODEL_SPECS = {
    "perceived-logit": {
        "train_module": (
            "hazard_double_difficulty.perceived_logit_bernstein.train_pyramidal"
        ),
        "alpha_prior": "normal-one",
        "alpha_prior_description": "Normal(1, 1)",
        "beta_prior_description": "Normal(0, 1)",
        "perception_slices": 1,
    },
    "perceived-difficulty-three-slice": {
        "train_module": (
            "hazard_double_difficulty.perceived_difficulty_bernstein."
            "train_pyramidal"
        ),
        "alpha_prior": "normal-zero",
        "alpha_prior_description": "Normal(0, 1)",
        "beta_prior_description": "Normal(0, 1)",
        "perception_slices": 3,
    },
}
EVALUATE_MODULE = "run_scripts.double_difficulty.evaluate_fold"


@dataclass(frozen=True)
class Configuration:
    root: str
    models: list[str]
    dimensions: list[int]
    base_split: str
    folds: list[int]
    split_seed: int
    optimization_seed: int
    degree: int
    relevance_concentration: float
    drop_concentration: float
    steps: int
    lr: float
    device: str
    posterior_draws: int
    plateau_relative_tolerance: float
    survival_chunk_dimension_budget: int
    data_dir: str | None


def point_dir(root: Path, model: str, dimensions: int) -> Path:
    return root / model / f"dim_{dimensions}"


def fold_dir(root: Path, model: str, dimensions: int, fold: int) -> Path:
    return point_dir(root, model, dimensions) / f"fold_{fold}"


def jobs(config: Configuration):
    for model in config.models:
        for dimensions in config.dimensions:
            for fold in config.folds:
                yield model, dimensions, fold


def survival_chunk_rows(config: Configuration, dimensions: int) -> int | None:
    """Keep the survival-grid row x dimension budget approximately fixed."""
    if config.survival_chunk_dimension_budget <= 0:
        return None
    return max(1, config.survival_chunk_dimension_budget // dimensions)


def experiment_commands(
    config: Configuration, model: str, dimensions: int, fold: int
) -> tuple[Path, list[tuple[str, Path, list[str]]]]:
    """Build train, frozen replay, and evaluation commands for one fold."""
    spec = MODEL_SPECS[model]
    run_dir = fold_dir(Path(config.root), model, dimensions, fold)
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
    slice_args = (
        ["--perception-slices", str(spec["perception_slices"])]
        if spec["perception_slices"] != 1
        else []
    )
    train = [
        PYTHON,
        "-m",
        str(spec["train_module"]),
        "--split",
        train_split,
        *data_args,
        "--degree",
        str(config.degree),
        "--dimensions",
        str(dimensions),
        *slice_args,
        "--alpha-prior",
        str(spec["alpha_prior"]),
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
        str(dimensions),
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


def snapshot_configuration(config: Configuration) -> Path:
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
    return path


def run_one(
    config: Configuration,
    model: str,
    dimensions: int,
    fold: int,
    *,
    dry_run: bool,
    rerun: bool,
) -> None:
    run_dir, stages = experiment_commands(config, model, dimensions, fold)
    marker = run_dir / ".complete.json"
    manifest = {
        "model": model,
        "dimensions": dimensions,
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
    command_path = run_dir / "command.json"
    if command_path.exists() and not rerun:
        saved = json.loads(command_path.read_text(encoding="utf-8"))
        if saved != manifest:
            raise RuntimeError(
                f"Existing fold metadata differs at {run_dir}; "
                "use --rerun or another --root."
            )
    else:
        command_path.write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
        )

    chunk_rows = survival_chunk_rows(config, dimensions)
    print(
        f"\n=== model={model} dimensions={dimensions} fold={fold} "
        f"survival_chunk_rows={chunk_rows or 'full'} ===",
        flush=True,
    )
    env = dict(os.environ)
    if chunk_rows is None:
        env.pop("COMPIRT_SURVIVAL_CHUNK", None)
    else:
        env["COMPIRT_SURVIVAL_CHUNK"] = str(chunk_rows)
    for name, expected, command in stages:
        if expected.exists() and not rerun:
            print(f"resume stage {name}: {expected}", flush=True)
            continue
        print("+ " + shlex.join(command), flush=True)
        subprocess.run(command, cwd=REPO_ROOT, env=env, check=True)
    marker.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def collect_per_fold(config: Configuration) -> pd.DataFrame:
    rows = []
    for model, dimensions, fold in jobs(config):
        run_dir = fold_dir(Path(config.root), model, dimensions, fold)
        summary_path = run_dir / "train" / "pyramidal" / "summary.json"
        summary = (
            json.loads(summary_path.read_text(encoding="utf-8"))
            if summary_path.exists()
            else {}
        )
        metrics = _metric_row(run_dir / "evaluation" / "csvs" / "tossup_metrics.csv")
        metrics["neg_f1"] = neg_f1(metrics)
        required_artifacts = [
            summary_path,
            run_dir / "holdout" / "pyramidal" / "tossup_predictions.csv",
            run_dir / "holdout" / "pyramidal" / "buzz_event_predictions.csv",
            run_dir / "evaluation" / "csvs" / "tossup_metrics.csv",
            run_dir / "evaluation" / "csvs" / "tossup_full_pmf_scores.csv",
            run_dir / "evaluation" / "csvs" / "tossup_time_metrics.csv",
        ]
        missing = [str(p.relative_to(run_dir)) for p in required_artifacts if not p.exists()]
        rows.append(
            {
                "model": model,
                "dimensions": dimensions,
                "fold": fold,
                "complete": (run_dir / ".complete.json").exists() and not missing,
                "missing_artifacts": "; ".join(missing),
                "run_path": str(run_dir),
                "alpha_prior": summary.get("alpha_prior"),
                "beta_prior": summary.get("beta_prior"),
                "effective_parameter_count": summary.get(
                    "effective_parameter_count"
                ),
                "final_loss": summary.get("final_loss"),
                "best_loss": summary.get("best_loss"),
                "last_100_loss_slope": summary.get("last_100_loss_slope"),
                "finite_losses": summary.get("finite_losses"),
                **training_diagnostics(summary, run_dir / "train" / "pyramidal"),
                **metrics,
            }
        )
    return pd.DataFrame(rows)


def collect_pooled(config: Configuration, per_fold: pd.DataFrame) -> pd.DataFrame:
    rows = []
    required = len(config.folds)
    metadata = {
        "model",
        "dimensions",
        "fold",
        "complete",
        "run_path",
        "alpha_prior",
        "beta_prior",
        "finite_losses",
        "missing_artifacts",
    }
    for model in config.models:
        spec = MODEL_SPECS[model]
        for dimensions in config.dimensions:
            selected = per_fold[
                (per_fold["model"] == model)
                & (per_fold["dimensions"] == dimensions)
            ]
            complete = selected[selected["complete"].astype(bool)]
            row: dict[str, object] = {
                "model": model,
                "dimensions": dimensions,
                "alpha_prior": spec["alpha_prior_description"],
                "beta_prior": spec["beta_prior_description"],
                "complete_folds": len(complete),
                "required_folds": required,
                PRIMARY_METRIC: np.nan,
            }
            for column in complete.columns:
                if column in metadata:
                    continue
                values = pd.to_numeric(complete[column], errors="coerce").replace(
                    [np.inf, -np.inf], np.nan
                )
                if values.notna().any():
                    row[f"{column}_fold_mean"] = float(values.mean())
                    row[f"{column}_fold_std"] = float(values.std())
                    row[f"{column}_fold_n"] = int(values.notna().sum())
            if len(complete) == required:
                run_dirs = [
                    fold_dir(Path(config.root), model, dimensions, fold)
                    for fold in config.folds
                ]
                row.update(
                    _pooled_scores(run_dirs, include_in_sample_metrics=False)
                )
                row["neg_f1"] = neg_f1(row)
            rows.append(row)

    frame = pd.DataFrame(rows)
    frame["primary_rank"] = np.nan
    frame["within_plateau"] = False
    frame["selected_dimension"] = False
    for model in config.models:
        mask = (
            (frame["model"] == model)
            & (frame["complete_folds"] == required)
            & pd.to_numeric(frame[PRIMARY_METRIC], errors="coerce").notna()
        )
        if not mask.any():
            continue
        values = pd.to_numeric(frame.loc[mask, PRIMARY_METRIC])
        frame.loc[mask, "primary_rank"] = values.rank(
            method="min", ascending=True
        ).astype(float)
        cutoff = float(values.min()) * (1.0 + config.plateau_relative_tolerance)
        plateau_mask = mask & (pd.to_numeric(frame[PRIMARY_METRIC]) <= cutoff)
        frame.loc[plateau_mask, "within_plateau"] = True
        selected_dimension = int(frame.loc[plateau_mask, "dimensions"].min())
        frame.loc[
            (frame["model"] == model)
            & (frame["dimensions"] == selected_dimension),
            "selected_dimension",
        ] = True
    return frame.sort_values(["model", "dimensions"]).reset_index(drop=True)


PLOT_METRICS = {
    PRIMARY_METRIC: "Joint event log loss",
    "log_loss": "Correctness log loss",
    "accuracy": "Correctness accuracy",
    "auc": "Correctness AUC",
    "integrated_brier_score": "Integrated Brier score",
    "buzz_position_mae": "Buzz-position MAE",
}


def save_plots(frame: pd.DataFrame, output_dir: Path) -> None:
    graph_dir = output_dir / "graphs"
    graph_dir.mkdir(parents=True, exist_ok=True)
    complete = frame[frame["complete_folds"] == frame["required_folds"]]
    for metric, label in PLOT_METRICS.items():
        if metric not in complete:
            continue
        fig, ax = plt.subplots(figsize=(8, 5))
        drew_line = False
        for model, rows in complete.groupby("model"):
            values = pd.to_numeric(rows[metric], errors="coerce")
            usable = rows.loc[values.notna()].copy()
            if usable.empty:
                continue
            ax.plot(
                usable["dimensions"],
                pd.to_numeric(usable[metric]),
                marker="o",
                label=model,
            )
            drew_line = True
        if not drew_line:
            plt.close(fig)
            continue
        ax.set(
            xlabel="Latent dimensions",
            ylabel=label,
            title=f"{label} vs latent dimensions",
        )
        ax.set_xticks(sorted(complete["dimensions"].unique()))
        ax.grid(alpha=0.25)
        ax.legend()
        fig.tight_layout()
        fig.savefig(graph_dir / f"{metric}_vs_dimensions.png", dpi=160)
        plt.close(fig)


def write_summary(
    config: Configuration, frame: pd.DataFrame, path: Path,
    per_fold: pd.DataFrame | None = None,
) -> None:
    from run_scripts.double_difficulty.perception_ablation_report import write_report

    if per_fold is None:
        per_fold = collect_per_fold(config)
    write_report(config, frame, per_fold, path, MODEL_SPECS, PLOT_METRICS)


def aggregate(config: Configuration) -> None:
    output_dir = Path(config.root) / "aggregate"
    output_dir.mkdir(parents=True, exist_ok=True)
    per_fold = collect_per_fold(config)
    per_fold.to_csv(output_dir / "per_fold.csv", index=False)
    numeric = [
        column
        for column in per_fold.select_dtypes("number").columns
        if column != "fold"
    ]
    complete = per_fold[per_fold["complete"].astype(bool)]
    if complete.empty:
        statistics = pd.DataFrame()
    else:
        grouped = complete.groupby(["model", "dimensions"])[numeric]
        statistics = pd.concat(
            [grouped.mean().add_suffix("_mean"), grouped.std().add_suffix("_std")],
            axis=1,
        ).reset_index()
    statistics.to_csv(output_dir / "fold_mean_std.csv", index=False)
    pooled = collect_pooled(config, per_fold)
    pooled.to_csv(output_dir / "pooled.csv", index=False)
    save_plots(pooled, output_dir)
    write_summary(config, pooled, output_dir / "summary.md", per_fold)
    print(f"Aggregate results: {output_dir / 'summary.md'}", flush=True)


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument(
        "--models", nargs="+", choices=DEFAULT_MODELS, default=list(DEFAULT_MODELS)
    )
    parser.add_argument(
        "--dimensions", nargs="+", type=int, default=list(DEFAULT_DIMENSIONS)
    )
    parser.add_argument("--base-split", default="year_2024")
    parser.add_argument("--folds", nargs="+", type=int, default=list(range(FOLD_COUNT)))
    parser.add_argument("--split-seed", type=int, default=42)
    parser.add_argument("--optimization-seed", type=int, default=42)
    parser.add_argument("--degree", type=int, default=3)
    parser.add_argument("--relevance-concentration", type=float, default=2.0)
    parser.add_argument("--drop-concentration", type=float, default=2.0)
    parser.add_argument("--steps", type=int, default=3000)
    parser.add_argument("--lr", type=float, default=0.005)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument("--posterior-draws", type=int, default=0)
    parser.add_argument(
        "--plateau-relative-tolerance",
        type=float,
        default=0.01,
        help=(
            "select the smallest dimension within this fraction of the best "
            "joint loss"
        ),
    )
    parser.add_argument(
        "--survival-chunk-dimension-budget",
        type=int,
        default=81920,
        help=(
            "maximum rows times dimensions per survival chunk; 0 uses full "
            "batches (default: 81920, matching 2048 rows at dimension 40)"
        ),
    )
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--collect-only", action="store_true")
    parser.add_argument("--rerun", action="store_true")
    parser.add_argument("--shard-count", type=int, default=1)
    parser.add_argument("--shard-index", type=int, default=0)
    parser.add_argument("--skip-aggregate", action="store_true")
    args = parser.parse_args(argv)
    if not args.models or len(args.models) != len(set(args.models)):
        parser.error("--models must contain distinct model names")
    if not args.dimensions or any(value < 1 for value in args.dimensions):
        parser.error("--dimensions values must all be at least 1")
    if len(args.dimensions) != len(set(args.dimensions)):
        parser.error("--dimensions values must be distinct")
    if not args.folds or any(fold not in range(FOLD_COUNT) for fold in args.folds):
        parser.error("--folds must be selected from 0 1 2 3 4")
    if args.degree not in range(3, 7):
        parser.error("--degree must be selected from 3 4 5 6")
    if args.steps < 1 or args.posterior_draws < 0:
        parser.error("--steps must be positive and --posterior-draws non-negative")
    if args.relevance_concentration <= 0 or args.drop_concentration <= 0:
        parser.error("Dirichlet concentrations must be positive")
    if not 0 <= args.plateau_relative_tolerance < 1:
        parser.error("--plateau-relative-tolerance must be in [0, 1)")
    if args.survival_chunk_dimension_budget < 0:
        parser.error("--survival-chunk-dimension-budget must be non-negative")
    if args.shard_count < 1 or args.shard_index not in range(args.shard_count):
        parser.error("--shard-index must be in [0, --shard-count)")
    if args.collect_only and (args.dry_run or args.rerun or args.skip_aggregate):
        parser.error(
            "--collect-only cannot be combined with --dry-run, --rerun, or "
            "--skip-aggregate"
        )
    return args


def main(argv=None) -> None:
    args = parse_args(argv)
    args.root = Path(resolve_result_root(args.root, "holdout"))
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
        models=args.models,
        dimensions=sorted(args.dimensions),
        base_split=args.base_split,
        folds=args.folds,
        split_seed=args.split_seed,
        optimization_seed=args.optimization_seed,
        degree=args.degree,
        relevance_concentration=args.relevance_concentration,
        drop_concentration=args.drop_concentration,
        steps=args.steps,
        lr=args.lr,
        device=args.device,
        posterior_draws=args.posterior_draws,
        plateau_relative_tolerance=args.plateau_relative_tolerance,
        survival_chunk_dimension_budget=args.survival_chunk_dimension_budget,
        data_dir=data_dir,
    )
    all_jobs = list(jobs(config))
    print(
        f"Perception dimension ablation: {len(config.models)} models x "
        f"{len(config.dimensions)} dimensions x {len(config.folds)} folds = "
        f"{len(all_jobs)} fits; root={config.root}",
        flush=True,
    )
    if (config.device == "cuda" and not torch.cuda.is_available()
            and not args.dry_run and not args.collect_only):
        raise SystemExit(
            "CUDA was requested but torch.cuda.is_available() is false. "
            "Run on a GPU host or explicitly pass --device cpu."
        )
    if not args.dry_run:
        snapshot_configuration(config)
    if not args.collect_only:
        selected = [
            job
            for index, job in enumerate(all_jobs)
            if index % args.shard_count == args.shard_index
        ]
        print(
            f"Worker shard {args.shard_index + 1}/{args.shard_count}: "
            f"{len(selected)} fits",
            flush=True,
        )
        for model, dimensions, fold in selected:
            run_one(
                config,
                model,
                dimensions,
                fold,
                dry_run=args.dry_run,
                rerun=args.rerun,
            )
    if not args.dry_run and not args.skip_aggregate:
        aggregate(config)


if __name__ == "__main__":
    main()
