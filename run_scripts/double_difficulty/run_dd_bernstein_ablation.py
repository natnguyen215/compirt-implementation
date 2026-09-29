#!/usr/bin/env python3
"""Run a frozen matrix-infill grid over full double-Bernstein hyperparameters.

The sweep is tossup-only.  Every grid point is fit on four whole-game folds,
replayed with frozen player and tossup parameters on the fifth fold, and sent
through the shared Scenario A evaluator.  The default grid is:

* Bernstein degree: 3, 4, 5, 6
* correctness/hazard relevance-curve dimensions: 1, 2, 3, 4, 5
* symmetric Dirichlet concentration: 0.67, 1, 1.33, 1.66, 2

That is 100 configurations and 500 fits.  Runs are resumable at each of the
train, frozen-replay, and evaluation stages.
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

from compirt_eval.common.metrics import classification_metrics, negative_class_metrics
from holdout.aggregate_reports import (
    add_in_sample_correctness_metrics,
    add_in_sample_main_table_fold_means,
    add_main_table_fold_means,
)
from holdout.game_splits import game_holdout_split_name
from utils.run_logging import resolve_result_root


DEFAULT_ROOT = Path("results/compirt/holdout/double-difficulty/ablations/capacity/degree-dimensions-drop-prior")
DEFAULT_DEGREES = (3, 4, 5, 6)
DEFAULT_DIMENSIONS = (1, 2, 3, 4, 5)
DEFAULT_CONCENTRATIONS = (0.67, 1.0, 1.33, 1.66, 2.0)
FOLD_COUNT = 5
TRAIN_MODULE = "hazard_double_difficulty.bernstein.train_pyramidal"
EVALUATE_MODULE = "run_scripts.double_difficulty.evaluate_fold"
PRIMARY_METRIC = "joint_tossup_event_log_loss"


@dataclass(frozen=True)
class Configuration:
    root: str
    base_split: str
    folds: list[int]
    split_seed: int
    optimization_seed: int
    degrees: list[int]
    dimensions: list[int]
    drop_concentrations: list[float]
    relevance_prior: str
    learned_curve_locations: bool
    terminal_intercepts: bool
    steps: int
    lr: float
    device: str
    posterior_draws: int
    data_dir: str | None


def concentration_label(value: float) -> str:
    """Return a stable path component for a concentration value."""
    return format(float(value), ".12g").replace(".", "p")


def grid_points(config: Configuration):
    """Yield the requested grid in a deterministic order."""
    for degree in config.degrees:
        for dimensions in config.dimensions:
            for concentration in config.drop_concentrations:
                yield degree, dimensions, concentration


def point_dir(root: Path, degree: int, dimensions: int, concentration: float) -> Path:
    return (
        root
        / f"degree_{degree}"
        / f"curves_{dimensions}"
        / f"dirichlet_{concentration_label(concentration)}"
    )


def fold_dir(
    root: Path,
    degree: int,
    dimensions: int,
    concentration: float,
    fold: int,
) -> Path:
    return point_dir(root, degree, dimensions, concentration) / f"fold_{fold}"


def experiment_commands(
    config: Configuration,
    degree: int,
    dimensions: int,
    concentration: float,
    fold: int,
) -> tuple[Path, list[tuple[str, Path, list[str]]]]:
    """Return the three commands for one frozen matrix-infill fold."""
    root = Path(config.root)
    run_dir = fold_dir(root, degree, dimensions, concentration, fold)
    train_dir = run_dir / "train" / "pyramidal"
    holdout_dir = run_dir / "holdout" / "pyramidal"
    evaluation_dir = run_dir / "evaluation"
    train_split = game_holdout_split_name(
        config.base_split, "train", FOLD_COUNT, fold, config.split_seed
    )
    test_split = game_holdout_split_name(
        config.base_split, "test", FOLD_COUNT, fold, config.split_seed
    )
    python = str(REPO_ROOT / ".venv" / "bin" / "python")
    data_args = ["--data-dir", config.data_dir] if config.data_dir else []

    train = [
        python,
        "-m",
        TRAIN_MODULE,
        "--split",
        train_split,
        *data_args,
        "--degree",
        str(degree),
        "--dimensions",
        str(dimensions),
        "--drop-concentration",
        str(concentration),
        "--relevance-prior",
        config.relevance_prior,
        *(["--learn-curve-locations"] if config.learned_curve_locations else []),
        *([] if config.terminal_intercepts else ["--no-terminal-intercepts"]),
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
        python,
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
        python,
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
    """Write the immutable resume contract for this result root."""
    root = Path(config.root)
    path = root / "configuration.json"
    expected = asdict(config)
    if path.exists():
        saved = json.loads(path.read_text(encoding="utf-8"))
        if saved != expected:
            raise SystemExit(
                f"Incompatible resume configuration at {path}. "
                "Use a different --root for changed grid or training settings."
            )
    else:
        root.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(expected, indent=2) + "\n", encoding="utf-8")
    return path


def run_one(
    config: Configuration,
    degree: int,
    dimensions: int,
    concentration: float,
    fold: int,
    *,
    dry_run: bool,
    rerun: bool,
) -> None:
    """Run or resume one grid-point fold."""
    run_dir, stages = experiment_commands(
        config, degree, dimensions, concentration, fold
    )
    marker = run_dir / ".complete.json"
    manifest = {
        "degree": degree,
        "dimensions": dimensions,
        "drop_concentration": concentration,
        "fold": fold,
        "configuration": asdict(config),
        "stages": [
            {
                "name": name,
                "expected_output": str(expected),
                "command": command,
            }
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

    print(
        f"\n=== degree={degree} curves={dimensions} "
        f"dirichlet={concentration:g} fold={fold} ===",
        flush=True,
    )
    for name, expected, command in stages:
        if expected.exists() and not rerun:
            print(f"resume stage {name}: {expected}", flush=True)
            continue
        print("+ " + shlex.join(command), flush=True)
        subprocess.run(command, cwd=REPO_ROOT, check=True)
    marker.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def _metric_row(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    frame = pd.read_csv(path)
    return {} if frame.empty else frame.iloc[0].to_dict()


def collect_per_fold(config: Configuration) -> pd.DataFrame:
    """Collect every completed fold without hiding partial progress."""
    rows = []
    root = Path(config.root)
    for degree, dimensions, concentration in grid_points(config):
        for fold in config.folds:
            run_dir = fold_dir(root, degree, dimensions, concentration, fold)
            metrics = _metric_row(
                run_dir / "evaluation" / "csvs" / "tossup_metrics.csv"
            )
            summary_path = run_dir / "train" / "pyramidal" / "summary.json"
            summary = (
                json.loads(summary_path.read_text(encoding="utf-8"))
                if summary_path.exists()
                else {}
            )
            rows.append(
                {
                    "degree": degree,
                    "dimensions": dimensions,
                    "drop_concentration": concentration,
                    "relevance_prior": config.relevance_prior,
                    "terminal_intercepts": config.terminal_intercepts,
                    "fold": fold,
                    "complete": (run_dir / ".complete.json").exists(),
                    "run_path": str(run_dir),
                    "effective_item_parameters": summary.get(
                        "effective_item_parameters"
                    ),
                    "effective_parameter_count": summary.get(
                        "effective_parameter_count"
                    ),
                    "final_loss": summary.get("final_loss"),
                    "best_loss": summary.get("best_loss"),
                    "last_100_loss_slope": summary.get("last_100_loss_slope"),
                    "finite_losses": summary.get("finite_losses"),
                    **metrics,
                }
            )
    return pd.DataFrame(rows)


def _pooled_scores(
    run_dirs: list[Path], *, include_in_sample_metrics: bool = True
) -> dict[str, object]:
    """Recompute pooled outcome metrics from complete held-out fold rows.

    The training-side main-table reconstruction is substantially more
    expensive than pooling held-out artifacts. Dimension-only model-selection
    sweeps may disable it without changing any held-out metric.
    """
    predictions, pmfs, positions, time_rows = [], [], [], []
    for run_dir in run_dirs:
        prediction_path = (
            run_dir / "holdout" / "pyramidal" / "tossup_predictions.csv"
        )
        pmf_path = run_dir / "evaluation" / "csvs" / "tossup_full_pmf_scores.csv"
        position_path = (
            run_dir / "holdout" / "pyramidal" / "buzz_event_predictions.csv"
        )
        time_path = run_dir / "evaluation" / "csvs" / "tossup_time_metrics.csv"
        if prediction_path.exists():
            predictions.append(pd.read_csv(prediction_path))
        if pmf_path.exists():
            pmfs.append(pd.read_csv(pmf_path))
        if position_path.exists():
            positions.append(pd.read_csv(position_path))
        if time_path.exists():
            time_rows.append(pd.read_csv(time_path))

    result: dict[str, object] = {}
    if predictions:
        buzz = pd.concat(predictions, ignore_index=True)
        buzz = buzz[buzz["z"] == "BUZZ"]
        result.update(classification_metrics(buzz["y"], buzz["predicted_correct"]))
        result.update(negative_class_metrics(buzz["y"], buzz["predicted_correct"]))
        result["observations"] = int(len(buzz))
    if pmfs:
        pmf = pd.concat(pmfs, ignore_index=True)
        error = pmf["predicted_no_buzz"] - pmf["observed_no_buzz"]
        result.update(
            joint_tossup_event_log_loss=float(pmf["joint_event_log_loss"].mean()),
            full_pmf_events=len(pmf),
            full_pmf_final_decile_mass=float(pmf["final_decile_mass"].mean()),
            no_buzz_observed_rate=float(pmf["observed_no_buzz"].mean()),
            no_buzz_predicted_rate=float(pmf["predicted_no_buzz"].mean()),
            no_buzz_calibration_error=float(error.mean()),
            no_buzz_brier=float(np.mean(error**2)),
            full_pmf_max_mass_error=float(
                np.max(np.abs(pmf["pmf_total_mass"] - 1.0))
            ),
        )
    if positions:
        frame = pd.concat(positions, ignore_index=True)
        error = (
            frame["predicted_relative_position"] - frame["observed_relative_position"]
        )
        result.update(
            buzz_position_mae=float(np.abs(error).mean()),
            buzz_position_median_absolute_error=float(np.abs(error).median()),
            buzz_position_bias=float(error.mean()),
        )
    if time_rows:
        frame = pd.concat(time_rows, ignore_index=True)
        pooled_time = (
            frame.assign(weighted_brier=frame["brier"] * frame["events"])
            .groupby("relative_position", as_index=False)
            .agg(weighted_brier=("weighted_brier", "sum"), events=("events", "sum"))
        )
        pooled_time["brier"] = pooled_time["weighted_brier"] / pooled_time["events"]
        result["integrated_brier_score"] = float(
            np.trapezoid(pooled_time["brier"], pooled_time["relative_position"])
        )
        result["survival_events"] = int(pooled_time["events"].max())
    if include_in_sample_metrics:
        add_in_sample_correctness_metrics(result, run_dirs)
        add_in_sample_main_table_fold_means(result, run_dirs)
    add_main_table_fold_means(result, run_dirs)
    return result


def collect_pooled(config: Configuration, per_fold: pd.DataFrame) -> pd.DataFrame:
    """Build one pooled row per grid point and rank complete configurations."""
    rows = []
    root = Path(config.root)
    required = len(config.folds)
    metadata_columns = {
        "degree",
        "dimensions",
        "drop_concentration",
        "relevance_prior",
        "terminal_intercepts",
        "fold",
        "complete",
        "run_path",
        "finite_losses",
        "effective_item_parameters",
        "effective_parameter_count",
        "final_loss",
        "best_loss",
        "last_100_loss_slope",
    }
    for degree, dimensions, concentration in grid_points(config):
        selected = per_fold[
            (per_fold["degree"] == degree)
            & (per_fold["dimensions"] == dimensions)
            & np.isclose(per_fold["drop_concentration"], concentration)
        ]
        completed = selected[selected["complete"].astype(bool)]
        row: dict[str, object] = {
            "degree": degree,
            "dimensions": dimensions,
            "drop_concentration": concentration,
            "relevance_prior": config.relevance_prior,
            "terminal_intercepts": config.terminal_intercepts,
            "complete_folds": int(len(completed)),
            "required_folds": required,
            "effective_item_parameters": pd.to_numeric(
                completed.get("effective_item_parameters"), errors="coerce"
            ).mean(),
            "effective_parameter_count": pd.to_numeric(
                completed.get("effective_parameter_count"), errors="coerce"
            ).mean(),
            "final_loss_mean": pd.to_numeric(
                completed.get("final_loss"), errors="coerce"
            ).mean(),
            "last_100_loss_slope_mean": pd.to_numeric(
                completed.get("last_100_loss_slope"), errors="coerce"
            ).mean(),
            PRIMARY_METRIC: np.nan,
        }
        if len(completed) == required:
            # Carry every evaluator metric into the grid table.  Exact pooled
            # metrics below replace fold means where row-level artifacts permit
            # a true recomputation.
            for column in completed.columns:
                if column in metadata_columns:
                    continue
                values = pd.to_numeric(completed[column], errors="coerce")
                if values.notna().any():
                    row[column] = float(values.mean())
            dirs = [
                fold_dir(root, degree, dimensions, concentration, fold)
                for fold in config.folds
            ]
            row.update(_pooled_scores(dirs))
        rows.append(row)

    frame = pd.DataFrame(rows)
    frame["primary_rank"] = np.nan
    eligible = (
        (frame["complete_folds"] == required)
        & pd.to_numeric(frame.get(PRIMARY_METRIC), errors="coerce").notna()
    )
    frame.loc[eligible, "primary_rank"] = (
        pd.to_numeric(frame.loc[eligible, PRIMARY_METRIC])
        .rank(method="min", ascending=True)
        .astype(float)
    )
    return frame.sort_values(
        ["primary_rank", "degree", "dimensions", "drop_concentration"],
        na_position="last",
    ).reset_index(drop=True)


def write_fold_statistics(per_fold: pd.DataFrame, path: Path) -> pd.DataFrame:
    """Write fold mean/std columns for all numeric evaluator metrics."""
    keys = [
        "degree",
        "dimensions",
        "drop_concentration",
        "relevance_prior",
        "terminal_intercepts",
    ]
    excluded = {
        *keys,
        "fold",
        "complete",
        "run_path",
        "finite_losses",
    }
    numeric_columns = [
        column
        for column in per_fold.columns
        if column not in excluded
        and pd.api.types.is_numeric_dtype(per_fold[column])
    ]
    complete = per_fold[per_fold["complete"].astype(bool)]
    if complete.empty:
        stats = pd.DataFrame(columns=[*keys, "complete_folds"])
    else:
        grouped = complete.groupby(keys)
        means = grouped[numeric_columns].mean().add_suffix("_mean")
        stds = grouped[numeric_columns].std(ddof=1).add_suffix("_std")
        counts = grouped.size().rename("complete_folds")
        stats = pd.concat([counts, means, stds], axis=1).reset_index()
    stats.to_csv(path, index=False)
    return stats


PLOT_METRICS = {
    "joint_tossup_event_log_loss": ("Joint event log loss", "joint_log_loss"),
    "log_loss": ("Correctness log loss", "correctness_log_loss"),
    "neg_auroc": ("Neg AUROC", "neg_auroc"),
    "integrated_brier_score": ("Integrated Brier score", "integrated_brier"),
    "no_buzz_brier": ("No-buzz Brier score", "no_buzz_brier"),
    "buzz_position_mae": ("Buzz-position MAE", "buzz_position_mae"),
}


def save_heatmaps(frame: pd.DataFrame, output_dir: Path) -> None:
    """Save dimension-by-concentration heatmaps separately for each degree."""
    graph_dir = output_dir / "graphs"
    graph_dir.mkdir(parents=True, exist_ok=True)
    complete = frame[frame["primary_rank"].notna()]
    for metric, (label, slug) in PLOT_METRICS.items():
        if metric not in complete:
            continue
        for degree, degree_rows in complete.groupby("degree"):
            pivot = degree_rows.pivot(
                index="dimensions",
                columns="drop_concentration",
                values=metric,
            ).sort_index(ascending=True)
            if pivot.empty or not np.isfinite(pivot.to_numpy(dtype=float)).any():
                continue
            values = pivot.to_numpy(dtype=float)
            fig, ax = plt.subplots(
                figsize=(1.15 * len(pivot.columns) + 3.2, 0.75 * len(pivot) + 2.4)
            )
            image = ax.imshow(values, cmap="viridis", aspect="auto")
            ax.set_xticks(
                range(len(pivot.columns)),
                [format(value, "g") for value in pivot.columns],
            )
            ax.set_yticks(
                range(len(pivot.index)), [str(value) for value in pivot.index]
            )
            ax.set(
                xlabel="Dirichlet concentration per drop share",
                ylabel="Number of curve dimensions",
                title=f"{label}, Bernstein degree {degree}",
            )
            finite = values[np.isfinite(values)]
            midpoint = float((finite.min() + finite.max()) / 2)
            for row in range(values.shape[0]):
                for column in range(values.shape[1]):
                    value = values[row, column]
                    if np.isfinite(value):
                        ax.text(
                            column,
                            row,
                            f"{value:.3f}",
                            ha="center",
                            va="center",
                            fontsize=8,
                            color="white" if value < midpoint else "black",
                        )
            fig.colorbar(image, ax=ax, label=label)
            fig.tight_layout()
            fig.savefig(graph_dir / f"{slug}_degree_{degree}.png", dpi=160)
            plt.close(fig)


def write_summary(config: Configuration, pooled: pd.DataFrame, output_dir: Path) -> Path:
    """Write a concise ranked result report that remains useful mid-sweep."""
    complete = pooled[pooled["primary_rank"].notna()].sort_values("primary_rank")
    total = len(pooled)
    lines = [
        "# Double-Bernstein grid-search summary",
        "",
        f"Evaluation regime: {len(config.folds)}-fold frozen whole-game matrix "
        "infill, tossups only.",
        f"Primary selection metric: pooled `{PRIMARY_METRIC}` (lower is better).",
        f"Relevance prior: `{config.relevance_prior}`.",
        f"Terminal intercepts: `{config.terminal_intercepts}`.",
        "",
        f"Complete configurations: {len(complete)} / {total}.",
        "",
    ]
    if complete.empty:
        lines.append("No configuration has all requested folds complete yet.")
    else:
        lines += [
            "| rank | degree | curves | Dirichlet | train accuracy | train AUC | "
            "train log loss | held-out accuracy | held-out AUC | "
            "held-out log loss | joint log loss |",
            "| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | "
            "---: | ---: |",
        ]
        for _, row in complete.head(20).iterrows():
            def show(column):
                value = row.get(column)
                return "" if pd.isna(value) else f"{float(value):.6g}"

            lines.append(
                f"| {int(row['primary_rank'])} | {int(row['degree'])} | "
                f"{int(row['dimensions'])} | {row['drop_concentration']:g} | "
                f"{show('in_sample_accuracy')} | {show('in_sample_auc')} | "
                f"{show('in_sample_log_loss')} | {show('accuracy')} | "
                f"{show('auc')} | {show('log_loss')} | "
                f"{show('joint_tossup_event_log_loss')} |"
            )
        best = complete.iloc[0]
        lines += [
            "",
            "## Selected configuration",
            "",
            f"- Degree: {int(best['degree'])}",
            f"- Curves/dimensions: {int(best['dimensions'])}",
            f"- Dirichlet concentration: {best['drop_concentration']:g}",
            f"- Relevance prior: {best['relevance_prior']}",
            f"- Terminal intercepts: {bool(best['terminal_intercepts'])}",
            f"- Pooled joint event log loss: "
            f"{best['joint_tossup_event_log_loss']:.6g}",
            "",
            "This is the CV winner, not an unbiased final-test estimate. "
            "Refit and assess it on an untouched test set, or use nested CV, "
            "before reporting a final generalization number.",
        ]
    path = output_dir / "summary.md"
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return path


def aggregate(config: Configuration) -> None:
    """Collect partial progress and all complete pooled grid scores."""
    aggregate_dir = Path(config.root) / "aggregate"
    aggregate_dir.mkdir(parents=True, exist_ok=True)
    per_fold = collect_per_fold(config)
    per_fold.to_csv(aggregate_dir / "per_fold.csv", index=False)
    write_fold_statistics(per_fold, aggregate_dir / "fold_mean_std.csv")
    pooled = collect_pooled(config, per_fold)
    pooled.to_csv(aggregate_dir / "pooled_rankings.csv", index=False)
    save_heatmaps(pooled, aggregate_dir)
    summary_path = write_summary(config, pooled, aggregate_dir)
    print(f"Aggregate results: {summary_path}", flush=True)


def parse_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--base-split", default="year_2024")
    parser.add_argument("--folds", nargs="+", type=int, default=list(range(FOLD_COUNT)))
    parser.add_argument("--split-seed", type=int, default=42)
    parser.add_argument("--optimization-seed", type=int, default=42)
    parser.add_argument(
        "--degrees", nargs="+", type=int, default=list(DEFAULT_DEGREES)
    )
    parser.add_argument(
        "--dimensions", nargs="+", type=int, default=list(DEFAULT_DIMENSIONS)
    )
    parser.add_argument(
        "--drop-concentrations",
        nargs="+",
        type=float,
        default=list(DEFAULT_CONCENTRATIONS),
    )
    parser.add_argument(
        "--relevance-prior",
        choices=("gamma", "simplex"),
        default="gamma",
        help="prior for both independent correctness/hazard relevance vectors",
    )
    parser.add_argument(
        "--no-terminal-intercepts",
        dest="terminal_intercepts",
        action="store_false",
        help="match the pre-terminal-cell-intercept Bernstein protocol",
    )
    parser.set_defaults(terminal_intercepts=True)
    parser.add_argument(
        "--learn-curve-locations",
        action="store_true",
        help="learn correctness/hazard population locations for curve starts",
    )
    parser.add_argument("--steps", type=int, default=3000)
    parser.add_argument("--lr", type=float, default=0.005)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument(
        "--posterior-draws",
        type=int,
        default=0,
        help="Saved posterior draws; evaluation does not use them (default: 0).",
    )
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--collect-only", action="store_true")
    parser.add_argument("--rerun", action="store_true")
    parser.add_argument(
        "--shard-count",
        type=int,
        default=1,
        help="Split the fold jobs across this many independent workers.",
    )
    parser.add_argument(
        "--shard-index",
        type=int,
        default=0,
        help="Zero-based worker index within --shard-count.",
    )
    parser.add_argument(
        "--skip-aggregate",
        action="store_true",
        help="Do not collect aggregates after this worker finishes.",
    )
    args = parser.parse_args(argv)
    if not args.folds or any(fold not in range(FOLD_COUNT) for fold in args.folds):
        parser.error("--folds must be selected from 0 1 2 3 4")
    if not args.degrees or any(degree not in DEFAULT_DEGREES for degree in args.degrees):
        parser.error("--degrees must be selected from 3 4 5 6")
    if not args.dimensions or any(value < 1 for value in args.dimensions):
        parser.error("--dimensions values must be at least 1")
    if not args.drop_concentrations or any(
        not np.isfinite(value) or value <= 0 for value in args.drop_concentrations
    ):
        parser.error("--drop-concentrations values must be finite and positive")
    if args.steps < 1:
        parser.error("--steps must be at least 1")
    if args.posterior_draws < 0:
        parser.error("--posterior-draws must be non-negative")
    if args.collect_only and (args.dry_run or args.rerun):
        parser.error("--collect-only cannot be combined with --dry-run or --rerun")
    if args.shard_count < 1:
        parser.error("--shard-count must be at least 1")
    if args.shard_index not in range(args.shard_count):
        parser.error("--shard-index must be in [0, --shard-count)")
    if args.collect_only and args.skip_aggregate:
        parser.error("--collect-only and --skip-aggregate are incompatible")
    return args


def main(argv=None) -> None:
    args = parse_args(argv)
    args.root = Path(resolve_result_root(args.root, "holdout"))
    root = args.root if args.root.is_absolute() else REPO_ROOT / args.root
    data_dir = None
    if args.data_dir is not None:
        resolved = (
            args.data_dir
            if args.data_dir.is_absolute()
            else REPO_ROOT / args.data_dir
        )
        data_dir = str(resolved)
    config = Configuration(
        root=str(root),
        base_split=args.base_split,
        folds=args.folds,
        split_seed=args.split_seed,
        optimization_seed=args.optimization_seed,
        degrees=args.degrees,
        dimensions=args.dimensions,
        drop_concentrations=args.drop_concentrations,
        relevance_prior=args.relevance_prior,
        learned_curve_locations=args.learn_curve_locations,
        terminal_intercepts=args.terminal_intercepts,
        steps=args.steps,
        lr=args.lr,
        device=args.device,
        posterior_draws=args.posterior_draws,
        data_dir=data_dir,
    )
    count = (
        len(config.degrees)
        * len(config.dimensions)
        * len(config.drop_concentrations)
    )
    print(
        f"Double-Bernstein grid: {count} configurations x "
        f"{len(config.folds)} folds = {count * len(config.folds)} fits; "
        f"root={config.root}",
        flush=True,
    )
    if config.device == "cuda" and not torch.cuda.is_available() and not args.dry_run:
        raise SystemExit(
            "CUDA was requested but torch.cuda.is_available() is false. "
            "Run on a GPU host or explicitly pass --device cpu."
        )
    if not args.dry_run:
        snapshot_configuration(config)
    if not args.collect_only:
        jobs = [
            (degree, dimensions, concentration, fold)
            for degree, dimensions, concentration in grid_points(config)
            for fold in config.folds
        ]
        selected_jobs = [
            job
            for index, job in enumerate(jobs)
            if index % args.shard_count == args.shard_index
        ]
        print(
            f"Worker shard {args.shard_index + 1}/{args.shard_count}: "
            f"{len(selected_jobs)} fits",
            flush=True,
        )
        for degree, dimensions, concentration, fold in selected_jobs:
            run_one(
                config,
                degree,
                dimensions,
                concentration,
                fold,
                dry_run=args.dry_run,
                rerun=args.rerun,
            )
    if not args.dry_run and not args.skip_aggregate:
        aggregate(config)


if __name__ == "__main__":
    main()
