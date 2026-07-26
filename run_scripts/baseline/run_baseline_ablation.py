#!/usr/bin/env python3
"""Run a held-out baseline CompIRT grid ablation over skill and synergy dimensions.

Sweeps two axes at once:

* '--dimensions' (m) sets the width of 'theta_i' and the free learned
  discrimination 'alpha_j' in 'theta_i . alpha_j - b_j(t)'. At m=1 this is
  scalar-skill CompIRT, so 'dim_1' is the reference point.
* '--synergy-dimensions' (s) sets the rank of the pairwise synergy term in the
  bonus stage. s=0 runs the plain compositional model with no synergy branch and
  is the reference column for the synergy axis.

Stage 1 (pyramidal) depends only on m, so it is fit once per dimension and
shared across that dimension's whole synergy row -- a grid of |m| x |s| points
costs |m| pyramidal fits, not |m| x |s|. The consequence for reporting is that
tossup metrics are invariant in s: they are written into every row of the
aggregate CSV but plotted only against m.

The runner calls the training and evaluation entry points directly, selecting
exactly one bonus branch per grid point.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-compirt")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from compirt_eval.common.report_paths import csv_path, graph_path
from run_scripts.common.lib.ablation import (
    Stage,
    add_shared_sweep_arguments,
    configure_environment,
    finalize_shared_sweep_args,
    optional_path_args,
    path_for_command,
    read_metrics,
    read_summary,
    run_dir,
    run_stage,
    save_ablation_config,
    start_run_log,
    tossup_accuracy_from_predictions,
    tournament_args,
    validate_ablation_resume,
)
from utils.run_logging import format_run_log_header

DEFAULT_ROOT = Path("results/compirt/holdout/baseline/baseline-ablation")
DEFAULT_DIMENSIONS = (1, 2, 3, 4, 5)
DEFAULT_SYNERGY_DIMENSIONS = (0, 1, 2, 3)

# Synergy rank is ordinal, so lines are shaded light-to-dark along a single hue
# rather than given categorical colors. The shade is a function of s alone, not
# of its rank among the plotted values, so plotting a subset of the grid never
# repaints the series it kept. Ranks past the cap all take the darkest shade.
SYNERGY_SHADE_CAP = 8
NO_SYNERGY_COLOR = "0.45"
SEQUENTIAL_CMAP = "Blues"


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
    row.update(
        read_summary(
            point / stage_name / "summary.json",
            "bonus",
            {
                "bonus_use_synergy": "use_synergy",
                "bonus_tau": "tau",
                "mean_synergy_contribution": "mean_synergy_contribution",
            },
        )
    )
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


def parse_args() -> argparse.Namespace:
    """Parse command-line options for the grid ablation runner."""
    parser = argparse.ArgumentParser(description=__doc__)
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
    parser.add_argument("--seed", type=int, default=42)
    add_shared_sweep_arguments(parser, DEFAULT_ROOT)
    args = finalize_shared_sweep_args(parser.parse_args())
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
    return args


def main() -> None:
    """Run the grid ablation, then write aggregate metrics and plots."""
    args = parse_args()
    configure_environment()
    start_run_log(args.root)
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/baseline/run_baseline_ablation.py",
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
        # Fit Stage 1 once per dimension before scheduling every synergy rank
        # that consumes its shared player skills.
        stages = []
        for dimension in args.dimensions:
            stages.extend(pyramidal_stages(args, dimension))
            for synergy in args.synergy_dimensions:
                stages.extend(bonus_stages(args, dimension, synergy))
        validate_ablation_resume(args.root, stages, args.rerun)
        # Record the run configuration before training. Collect-only passes keep
        # the configuration written by the training sweep.
        config_path = save_ablation_config(args.root, args, stages)
        print(f"Wrote run configuration to {path_for_command(config_path)}\n", flush=True)
        for stage in stages:
            run_stage(stage, args.rerun)

    metrics = collect_results(args.root, args.plot_dimensions, args.plot_synergy_dimensions)
    csv_output = save_aggregate_outputs(args.root, metrics)
    print(f"\nWrote aggregate metrics to {path_for_command(csv_output)}")
    print(f"Wrote aggregate graphs to {path_for_command(args.root / 'graphs')}")


if __name__ == "__main__":
    main()
