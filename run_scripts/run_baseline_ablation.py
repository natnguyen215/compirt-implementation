#!/usr/bin/env python3
"""Run a held-out baseline CompIRT grid ablation over skill and synergy dimensions.

Sweeps two axes at once:

* '--dimensions' (m) sets the width of 'theta_i' and the free learned
  discrimination 'alpha_j' in 'theta_i . alpha_j - b_j(t)'. At m=1 this is the
  paper's scalar-skill CompIRT, so 'dim_1' is the genuine reference point.
* '--synergy-dimensions' (s) sets the rank of the pairwise synergy term in the
  bonus stage. s=0 runs the plain compositional model with no synergy branch and
  is the reference column for the synergy axis.

Stage 1 (pyramidal) depends only on m, so it is fit once per dimension and
shared across that dimension's whole synergy row -- a grid of |m| x |s| points
costs |m| pyramidal fits, not |m| x |s|. The consequence for reporting is that
tossup metrics are invariant in s: they are written into every row of the
aggregate CSV but plotted only against m.

The runner calls the training/evaluation entry points directly so it can pick
exactly one bonus branch per point, which the standard holdout driver cannot do.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import sys
from dataclasses import dataclass
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-compirt")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_eval.outputs import csv_path, graph_path, metrics_path
from utils.run_logging import (
    format_run_log_header,
    resolve_result_root,
    run_logged,
    tee_run_output,
)

DEFAULT_ROOT = Path("results/compirt/holdout/baseline-ablation")
DEFAULT_DIMENSIONS = (1, 2, 3, 4, 5)
DEFAULT_SYNERGY_DIMENSIONS = (0, 1, 2, 3)

# Synergy rank is ordinal, so lines are shaded light-to-dark along a single hue
# rather than given categorical colors. The shade is a function of s alone, not
# of its rank among the plotted values, so plotting a subset of the grid never
# repaints the series it kept. Ranks past the cap all take the darkest shade.
SYNERGY_SHADE_CAP = 8
NO_SYNERGY_COLOR = "0.45"
SEQUENTIAL_CMAP = "Blues"


@dataclass(frozen=True)
class Stage:
    """One resumable command in a grid ablation run."""

    name: str
    marker: Path
    command: list[str]


def repo_relative(path: Path) -> Path:
    """Return a stable display path for paths inside the repository."""
    try:
        return path.relative_to(REPO_ROOT)
    except ValueError:
        return path


def path_for_command(path: Path) -> str:
    """Render paths so repository-local outputs stay readable in logs."""
    return str(repo_relative(path))


def repo_path(path: Path | None) -> Path | None:
    """Resolve a path relative to the repository root."""
    if path is None or path.is_absolute():
        return path
    return REPO_ROOT / path


def tournament_args(tournament: str | None) -> list[str]:
    """Return optional tournament-filter CLI args for training stages."""
    return ["--tournament", tournament] if tournament else []


def optional_path_args(flag: str, path: Path | None) -> list[str]:
    """Return an optional path-valued CLI arg."""
    return [flag, path_for_command(path)] if path is not None else []


def run_dir(root: Path, dimension: int) -> Path:
    """Return the output directory shared by one skill dimension's synergy row."""
    return root / f"dim_{dimension}"


def bonus_stage_name(synergy_dimensions: int) -> str:
    """Name the bonus stage after the branch it runs, as the holdout driver does."""
    return "compositional" if synergy_dimensions == 0 else "synergy"


def bonus_dir(root: Path, dimension: int, synergy_dimensions: int) -> Path:
    """Return the output directory for one (dimension, synergy) grid point."""
    return run_dir(root, dimension) / "holdout" / f"syn_{synergy_dimensions}"


def pyramidal_stages(args: argparse.Namespace, dimension: int) -> list[Stage]:
    """Build the Stage-1 commands shared by every synergy point at this dimension."""
    current_run = run_dir(args.root, dimension)
    train_pyr = current_run / "train" / "pyramidal"
    holdout_pyr = current_run / "holdout" / "pyramidal"

    python = path_for_command(args.python)
    data_args = optional_path_args("--data-dir", args.data_dir)
    train_filter_args = data_args + tournament_args(args.tournament)
    calibration_args = ["--calibrate-correctness"] if args.calibrate_correctness else []
    predict_args = ["--predict-buzz-positions"] if args.predict_buzz_positions else []

    return [
        Stage(
            "train-pyramidal",
            train_pyr / "summary.json",
            [
                python,
                "-m",
                "train_pyramidal",
                "--split",
                args.train_split,
                *train_filter_args,
                "--dimensions",
                str(dimension),
                "--steps",
                str(args.pyramidal_steps),
                "--lr",
                str(args.lr),
                "--seed",
                str(args.seed),
                "--device",
                args.device,
                *predict_args,
                *calibration_args,
                "--output-dir",
                path_for_command(train_pyr),
            ],
        ),
        Stage(
            "holdout-pyramidal",
            holdout_pyr / "summary.json",
            [
                python,
                "-m",
                "train_pyramidal",
                "--split",
                args.test_split,
                *train_filter_args,
                "--dimensions",
                str(dimension),
                "--steps",
                str(args.pyramidal_steps),
                "--lr",
                str(args.lr),
                "--seed",
                str(args.seed),
                "--device",
                args.device,
                "--train-posterior",
                path_for_command(train_pyr / "player_posterior.csv"),
                "--new-player-prior",
                args.new_player_prior,
                *predict_args,
                *calibration_args,
                "--output-dir",
                path_for_command(holdout_pyr),
            ],
        ),
    ]


def bonus_stages(
    args: argparse.Namespace, dimension: int, synergy_dimensions: int
) -> list[Stage]:
    """Build the Stage-2 and evaluation commands for one grid point."""
    holdout_pyr = run_dir(args.root, dimension) / "holdout" / "pyramidal"
    point = bonus_dir(args.root, dimension, synergy_dimensions)
    stage_name = bonus_stage_name(synergy_dimensions)
    bonus_out = point / stage_name
    evaluation_out = point / f"{stage_name}-evaluation"

    python = path_for_command(args.python)
    data_args = optional_path_args("--data-dir", args.data_dir)
    train_filter_args = data_args + tournament_args(args.tournament)
    calibration_args = ["--calibrate-correctness"] if args.calibrate_correctness else []
    if synergy_dimensions == 0:
        synergy_args: list[str] = []
    else:
        synergy_args = ["--use-synergy", "--synergy-dimensions", str(synergy_dimensions)]
        if args.save_synergy_details:
            synergy_args.append("--save-synergy-details")

    return [
        Stage(
            stage_name,
            bonus_out / "summary.json",
            [
                python,
                "-m",
                "train_compositional",
                "--split",
                args.test_split,
                *train_filter_args,
                # train_compositional takes no --dimensions; it reads the skill
                # width off theta_1..K in the pyramidal run's players.csv.
                "--player-skills",
                path_for_command(holdout_pyr / "players.csv"),
                "--steps",
                str(args.bonus_steps),
                "--lr",
                str(args.lr),
                "--seed",
                str(args.seed),
                "--device",
                args.device,
                *synergy_args,
                *calibration_args,
                "--output-dir",
                path_for_command(bonus_out),
            ],
        ),
        Stage(
            f"{stage_name}-evaluation",
            evaluation_out / "experiment_report.md",
            [
                python,
                "-m",
                "evaluate_compirt",
                "--pyramidal-results",
                path_for_command(holdout_pyr),
                "--compositional-results",
                path_for_command(bonus_out),
                "--output-dir",
                path_for_command(evaluation_out),
            ],
        ),
    ]


def run_stage(stage: Stage, rerun: bool) -> None:
    """Run one stage unless its marker already exists."""
    if stage.marker.exists() and not rerun:
        print(f"skip {stage.name}: {path_for_command(stage.marker)}", flush=True)
        return
    print("+ " + shlex.join(stage.command), flush=True)
    run_logged(stage.command, cwd=REPO_ROOT)


def read_summary(path: Path, prefix: str) -> dict[str, object]:
    """Read a stage summary and retain selected fields with a prefix."""
    if not path.exists():
        return {}
    summary = json.loads(path.read_text(encoding="utf-8"))
    fields = {
        f"{prefix}_final_loss": summary.get("final_loss"),
        f"{prefix}_steps": summary.get("steps"),
    }
    if prefix == "bonus":
        fields["bonus_use_synergy"] = summary.get("use_synergy")
        fields["bonus_tau"] = summary.get("tau")
        fields["mean_synergy_contribution"] = summary.get("mean_synergy_contribution")
    return fields


def read_metrics(evaluation_dir: Path, filename: str, prefix: str) -> dict[str, object]:
    """Read one evaluation metrics CSV and prefix every metric column."""
    path = metrics_path(evaluation_dir, filename)
    if not path.exists():
        return {}
    row = pd.read_csv(path).iloc[0].to_dict()
    return {f"{prefix}_{key}": value for key, value in row.items()}


def tossup_accuracy_from_predictions(predictions_path: Path) -> float | None:
    """Compute thresholded tossup correctness accuracy from saved buzz rows."""
    if not predictions_path.exists():
        return None
    predictions = pd.read_csv(predictions_path)
    buzz = predictions[predictions["z"] == "BUZZ"].copy()
    if buzz.empty:
        return None
    matches = (buzz["predicted_correct"] >= 0.5) == buzz["y"].astype(bool)
    return float(matches.mean())


def collect_run(root: Path, dimension: int, synergy_dimensions: int) -> dict[str, object]:
    """Collect summaries and held-out metrics for one grid point."""
    current_run = run_dir(root, dimension)
    train_pyr = current_run / "train" / "pyramidal"
    holdout_pyr = current_run / "holdout" / "pyramidal"
    stage_name = bonus_stage_name(synergy_dimensions)
    point = bonus_dir(root, dimension, synergy_dimensions)
    evaluation = point / f"{stage_name}-evaluation"

    row: dict[str, object] = {
        "dimension": dimension,
        # The grid coordinate is authoritative; the bonus summary reports 0 for
        # every no-synergy run, which cannot distinguish s=0 from a missing run.
        "synergy_dimensions": synergy_dimensions,
        "run_path": path_for_command(point),
    }
    row.update(read_summary(train_pyr / "summary.json", "train_pyramidal"))
    row.update(read_summary(holdout_pyr / "summary.json", "holdout_pyramidal"))
    row.update(read_summary(point / stage_name / "summary.json", "bonus"))
    row.update(read_metrics(evaluation, "bonus_metrics.csv", "bonus"))
    row.update(read_metrics(evaluation, "tossup_metrics.csv", "tossup"))
    if "tossup_accuracy" not in row:
        accuracy = tossup_accuracy_from_predictions(holdout_pyr / "tossup_predictions.csv")
        if accuracy is not None:
            row["tossup_accuracy"] = accuracy
    return row


def collect_results(
    root: Path, dimensions: list[int], synergy_dimensions: list[int]
) -> pd.DataFrame:
    """Collect every grid cell, ordered by dimension then synergy rank."""
    rows = [
        collect_run(root, dimension, synergy)
        for dimension in dimensions
        for synergy in synergy_dimensions
    ]
    frame = pd.DataFrame(rows)
    return frame.sort_values(["dimension", "synergy_dimensions"]).reset_index(drop=True)


def numeric_grid(frame: pd.DataFrame, metric: str) -> pd.DataFrame | None:
    """Pivot one metric into a synergy-by-dimension grid, or None when unusable."""
    if metric not in frame:
        return None
    plot_data = frame[["dimension", "synergy_dimensions", metric]].copy()
    plot_data[metric] = pd.to_numeric(plot_data[metric], errors="coerce")
    plot_data = plot_data.dropna(subset=[metric])
    if plot_data.empty:
        return None
    return plot_data.pivot(
        index="synergy_dimensions", columns="dimension", values=metric
    ).sort_index()


def synergy_color(synergy_dimensions: int):
    """Shade one synergy rank, keyed to the rank itself so subsets keep their color."""
    if synergy_dimensions == 0:
        return NO_SYNERGY_COLOR
    capped = min(synergy_dimensions, SYNERGY_SHADE_CAP)
    position = (capped - 1) / max(SYNERGY_SHADE_CAP - 1, 1)
    return plt.get_cmap(SEQUENTIAL_CMAP)(0.35 + 0.6 * position)


def synergy_label(synergy_dimensions: int) -> str:
    """Label one synergy rank for a legend entry."""
    if synergy_dimensions == 0:
        return "no synergy"
    return f"s = {synergy_dimensions}"


def save_grid_line_plot(
    frame: pd.DataFrame,
    output_dir: Path,
    metric: str,
    filename: str,
    ylabel: str,
    title: str,
) -> None:
    """Save one metric against skill dimensions, with a line per synergy rank."""
    grid = numeric_grid(frame, metric)
    if grid is None:
        print(f"skip plot {filename}: no finite values for {metric}", flush=True)
        return

    fig, ax = plt.subplots(figsize=(8, 5))
    for synergy, series in grid.iterrows():
        values = series.dropna()
        ax.plot(
            values.index,
            values.to_numpy(),
            marker="o",
            markersize=5,
            linewidth=2,
            color=synergy_color(int(synergy)),
            label=synergy_label(int(synergy)),
        )
    ax.set(
        title=title,
        xlabel="Number of latent skill dimensions (m)",
        ylabel=ylabel,
    )
    ax.set_xticks([int(dimension) for dimension in grid.columns])
    ax.grid(alpha=0.25)
    ax.legend(title="Synergy rank", frameon=False)
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, filename), dpi=160)
    plt.close(fig)


def save_grid_heatmap(
    frame: pd.DataFrame,
    output_dir: Path,
    metric: str,
    filename: str,
    colorbar_label: str,
    title: str,
) -> None:
    """Save one metric as a synergy-by-dimension heatmap with annotated cells."""
    grid = numeric_grid(frame, metric)
    if grid is None:
        print(f"skip plot {filename}: no finite values for {metric}", flush=True)
        return

    values = grid.to_numpy(dtype=float)
    masked = np.ma.masked_invalid(values)
    colormap = plt.get_cmap(SEQUENTIAL_CMAP).copy()
    colormap.set_bad("0.9")

    fig, ax = plt.subplots(figsize=(1.0 * len(grid.columns) + 3.5, 0.7 * len(grid) + 2.5))
    image = ax.imshow(masked, cmap=colormap, aspect="auto")
    ax.set_xticks(range(len(grid.columns)), [str(int(c)) for c in grid.columns])
    ax.set_yticks(range(len(grid.index)), [synergy_label(int(s)) for s in grid.index])
    ax.set(title=title, xlabel="Number of latent skill dimensions (m)")
    # Annotate each cell, flipping the ink to white once the fill is dark enough
    # for dark text to fall below a readable contrast.
    finite = masked.compressed()
    midpoint = (finite.min() + finite.max()) / 2 if finite.size else 0.0
    for row in range(values.shape[0]):
        for column in range(values.shape[1]):
            value = values[row, column]
            if np.isnan(value):
                continue
            ax.text(
                column,
                row,
                f"{value:.3f}",
                ha="center",
                va="center",
                fontsize=8,
                color="white" if value > midpoint else "0.15",
            )
    fig.colorbar(image, ax=ax, label=colorbar_label)
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, filename), dpi=160)
    plt.close(fig)


def save_tossup_plot(
    frame: pd.DataFrame,
    output_dir: Path,
    metric: str,
    filename: str,
    ylabel: str,
    title: str,
) -> None:
    """Save one tossup metric against skill dimensions.

    Stage 1 never sees the synergy rank, so tossup metrics repeat down each
    dimension's synergy column. Collapse them to one point per dimension rather
    than drawing identical overlapping lines.
    """
    if metric not in frame:
        print(f"skip plot {filename}: missing column {metric}", flush=True)
        return
    plot_data = frame[["dimension", metric]].copy()
    plot_data[metric] = pd.to_numeric(plot_data[metric], errors="coerce")
    plot_data = plot_data.dropna(subset=[metric])
    plot_data = plot_data.groupby("dimension", as_index=False)[metric].first()
    if plot_data.empty:
        print(f"skip plot {filename}: no finite values for {metric}", flush=True)
        return

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        plot_data["dimension"],
        plot_data[metric],
        marker="o",
        markersize=5,
        linewidth=2,
        color=plt.get_cmap(SEQUENTIAL_CMAP)(0.75),
    )
    ax.set(title=title, xlabel="Number of latent skill dimensions (m)", ylabel=ylabel)
    ax.set_xticks(plot_data["dimension"].astype(int).tolist())
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, filename), dpi=160)
    plt.close(fig)


def save_aggregate_outputs(root: Path, frame: pd.DataFrame) -> Path:
    """Write the aggregate CSV and every grid graph."""
    csv_output = csv_path(root, "baseline_ablation_metrics.csv")
    frame.to_csv(csv_output, index=False)

    bonus_metrics = (
        ("bonus_log_loss", "Bonus Val. Log Loss", "Bonus validation loss"),
        ("bonus_part_accuracy", "Bonus Val. Part Accuracy", "Bonus validation accuracy"),
    )
    for metric, ylabel, title in bonus_metrics:
        save_grid_line_plot(
            frame,
            root,
            metric,
            f"{metric}_vs_dimensions.png",
            ylabel,
            f"{title} vs latent dimensions",
        )
        save_grid_heatmap(
            frame,
            root,
            metric,
            f"{metric}_grid.png",
            ylabel,
            f"{title} over the skill x synergy grid",
        )

    tossup_metrics = (
        ("tossup_log_loss", "Tossup Val. Log Loss", "Tossup validation loss"),
        ("tossup_auc", "Tossup Val. AUC", "Tossup validation AUC"),
        ("tossup_accuracy", "Tossup Val. Accuracy", "Tossup validation accuracy"),
    )
    for metric, ylabel, title in tossup_metrics:
        save_tossup_plot(
            frame,
            root,
            metric,
            f"{metric}_vs_dimensions.png",
            ylabel,
            f"{title} vs latent dimensions",
        )
    return csv_output


def save_ablation_config(root: Path, args: argparse.Namespace) -> Path:
    """Record every resolved runner setting next to the results.

    Lets a sweep be reproduced from its output directory alone, without having to
    recover the invocation from 'run.log'.
    """
    config = {
        key: str(value) if isinstance(value, Path) else value
        for key, value in sorted(vars(args).items())
    }
    config_path = root / "ablation_config.json"
    config_path.write_text(json.dumps(config, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return config_path


def configure_environment() -> None:
    """Set runtime defaults used by the existing experiment runners."""
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-compirt")
    os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")


def parse_args() -> argparse.Namespace:
    """Parse command-line options for the grid ablation runner."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument(
        "--dimensions",
        type=int,
        nargs="+",
        default=list(DEFAULT_DIMENSIONS),
        help="Latent skill dimensions to run.",
    )
    parser.add_argument(
        "--synergy-dimensions",
        type=int,
        nargs="+",
        default=list(DEFAULT_SYNERGY_DIMENSIONS),
        help="Synergy ranks to run; 0 runs the no-synergy compositional branch.",
    )
    parser.add_argument(
        "--plot-dimensions",
        type=int,
        nargs="+",
        help="Skill dimensions to include in the aggregate CSV and graphs "
        "(defaults to --dimensions).",
    )
    parser.add_argument(
        "--plot-synergy-dimensions",
        type=int,
        nargs="+",
        help="Synergy ranks to include in the aggregate CSV and graphs "
        "(defaults to --synergy-dimensions).",
    )
    parser.add_argument("--train-split", default="year_2024")
    parser.add_argument("--test-split", default="year_2025")
    parser.add_argument("--tournament")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--pyramidal-steps", type=int, default=3000)
    parser.add_argument("--bonus-steps", type=int, default=2000)
    # Matches the committed multidim ablation rather than the trainer's own 0.02
    # default, so the two families' curves stay comparable.
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument("--new-player-prior", choices=("tier", "flat"), default="tier")
    parser.add_argument(
        "--python",
        type=Path,
        default=Path(os.environ.get("PYTHON", REPO_ROOT / ".venv" / "bin" / "python")),
    )
    parser.add_argument("--calibrate-correctness", action="store_true")
    parser.add_argument(
        "--predict-buzz-positions",
        action=argparse.BooleanOptionalAction,
        default=True,
    )
    parser.add_argument("--save-synergy-details", action="store_true")
    parser.add_argument(
        "--rerun",
        action="store_true",
        help="Run stages even when their marker files already exist.",
    )
    parser.add_argument(
        "--collect-only",
        action="store_true",
        help="Only rebuild the aggregate CSV and graphs from existing run folders.",
    )
    args = parser.parse_args()
    args.root = Path(resolve_result_root(repo_path(args.root), "holdout"))
    args.data_dir = repo_path(args.data_dir)
    if args.plot_dimensions is None:
        args.plot_dimensions = list(args.dimensions)
    if args.plot_synergy_dimensions is None:
        args.plot_synergy_dimensions = list(args.synergy_dimensions)
    if any(dimension < 1 for dimension in args.dimensions + args.plot_dimensions):
        raise ValueError("skill dimension values must all be at least 1")
    if any(
        synergy < 0
        for synergy in args.synergy_dimensions + args.plot_synergy_dimensions
    ):
        raise ValueError("synergy dimension values must all be at least 0")
    if args.pyramidal_steps < 1 or args.bonus_steps < 1:
        raise ValueError("--pyramidal-steps and --bonus-steps must be at least 1")
    return args


def main() -> None:
    """Run the grid ablation, then write aggregate metrics and plots."""
    args = parse_args()
    configure_environment()
    args.root.mkdir(parents=True, exist_ok=True)
    if os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(args.root / "run.log")
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/run_baseline_ablation.py",
                "ROOT": path_for_command(args.root),
                "MODEL": "baseline-ablation",
                "TRAIN_SPLIT": args.train_split,
                "TEST_SPLIT": args.test_split,
                "TOURNAMENT": args.tournament or "<all>",
                "DEVICE": args.device,
                "GPU": os.environ.get("GPU", "unknown"),
                "DIMENSIONS": args.dimensions,
                "SYNERGY_DIMENSIONS": args.synergy_dimensions,
                "PLOT_DIMENSIONS": args.plot_dimensions,
                "PLOT_SYNERGY_DIMENSIONS": args.plot_synergy_dimensions,
                "PYRAMIDAL_STEPS": args.pyramidal_steps,
                "BONUS_STEPS": args.bonus_steps,
                "LR": args.lr,
                "SEED": args.seed,
                "NEW_PLAYER_PRIOR": args.new_player_prior,
                "CALIBRATE_CORRECTNESS": args.calibrate_correctness,
                "PREDICT_BUZZ_POSITIONS": args.predict_buzz_positions,
                "SAVE_SYNERGY_DETAILS": args.save_synergy_details,
                "COLLECT_ONLY": args.collect_only,
                "RERUN": args.rerun,
                "PYTHON": path_for_command(args.python),
                "DATA_DIR": path_for_command(args.data_dir)
                if args.data_dir is not None
                else "",
            }
        ),
        flush=True,
    )

    if not args.collect_only:
        # Written before training so a crashed sweep still records what it tried,
        # and never on a --collect-only pass, which would otherwise overwrite the
        # real sweep's settings with the aggregation run's defaults.
        config_path = save_ablation_config(args.root, args)
        print(f"Wrote run configuration to {path_for_command(config_path)}\n", flush=True)
        for dimension in args.dimensions:
            print(f"\n=== baseline ablation: skill dimension {dimension} ===", flush=True)
            # Fit Stage 1 once per dimension. Running it inside the synergy loop
            # would refit it under --rerun and silently change the theta that the
            # already-finished synergy points were trained against.
            for stage in pyramidal_stages(args, dimension):
                run_stage(stage, args.rerun)
            for synergy in args.synergy_dimensions:
                print(f"\n--- synergy rank {synergy} (m={dimension}) ---", flush=True)
                for stage in bonus_stages(args, dimension, synergy):
                    run_stage(stage, args.rerun)

    metrics = collect_results(args.root, args.plot_dimensions, args.plot_synergy_dimensions)
    csv_output = save_aggregate_outputs(args.root, metrics)
    print(f"\nWrote aggregate metrics to {path_for_command(csv_output)}")
    print(f"Wrote aggregate graphs to {path_for_command(args.root / 'graphs')}")


if __name__ == "__main__":
    main()
