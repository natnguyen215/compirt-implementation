#!/usr/bin/env python3
"""Run a held-out multidim CompIRT dimension ablation with synergy only.

Each dimension gets its own run directory under the ablation root. The runner
intentionally calls the underlying training/evaluation entry points directly so
it can skip the no-synergy compositional branch used by the standard holdout
driver.

'--pyramidal-module' picks the Stage-1 trainer: the plain multidim MIRT model or
the TF-IDF multidim variant, which take the same dimension and held-out-prior
flags. Stage 2 is the shared root compositional model either way.
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

DEFAULT_ROOT = Path("results/compirt/holdout/multidim-ablation")
DEFAULT_DIMENSIONS = (11, 12, 13, 14, 15)
DEFAULT_PLOT_DIMENSIONS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
LEGACY_METRIC_NAMES = {}

# Both Stage-1 trainers take the same dimension/holdout-prior flags, so the sweep
# only needs to swap the module it invokes.
PYRAMIDAL_MODULES = {
    "multidim": "multidimensional.multidim_mirt.train_pyramidal",
    "tfidf-multidim": "tfidf.multidim.train_pyramidal",
}


@dataclass(frozen=True)
class Stage:
    """One resumable command in a per-dimension ablation run."""

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
    """Return the output directory for one latent-dimension run."""
    return root / f"dim_{dimension}"


def build_stages(args: argparse.Namespace, dimension: int) -> list[Stage]:
    """Build the exact training/evaluation commands for one ablation point."""
    root = args.root
    current_run = run_dir(root, dimension)
    train_pyr = current_run / "train" / "pyramidal"
    holdout_pyr = current_run / "holdout" / "pyramidal"
    holdout_synergy = current_run / "holdout" / "synergy"
    holdout_synergy_eval = current_run / "holdout" / "synergy-evaluation"

    python = path_for_command(args.python)
    data_args = optional_path_args("--data-dir", args.data_dir)
    train_filter_args = data_args + tournament_args(args.tournament)
    calibration_args = ["--calibrate-correctness"] if args.calibrate_correctness else []
    predict_args = ["--predict-buzz-positions"] if args.predict_buzz_positions else []
    synergy_detail_args = ["--save-synergy-details"] if args.save_synergy_details else []
    alpha_prior_args = ["--alpha-prior", args.alpha_prior]

    return [
        Stage(
            "train-pyramidal",
            train_pyr / "summary.json",
            [
                python,
                "-m",
                PYRAMIDAL_MODULES[args.pyramidal_module],
                "--split",
                args.train_split,
                *train_filter_args,
                "--dimensions",
                str(dimension),
                "--steps",
                str(args.pyramidal_steps),
                "--lr",
                str(args.lr),
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
                PYRAMIDAL_MODULES[args.pyramidal_module],
                "--split",
                args.test_split,
                *train_filter_args,
                "--dimensions",
                str(dimension),
                "--steps",
                str(args.pyramidal_steps),
                "--lr",
                str(args.lr),
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
        Stage(
            "synergy",
            holdout_synergy / "summary.json",
            [
                python,
                "-m",
                "train_compositional",
                "--split",
                args.test_split,
                *train_filter_args,
                "--player-skills",
                path_for_command(holdout_pyr / "players.csv"),
                "--steps",
                str(args.bonus_steps),
                "--lr",
                str(args.lr),
                "--device",
                args.device,
                "--use-synergy",
                "--synergy-dimensions",
                str(args.synergy_dimensions),
                *alpha_prior_args,
                *synergy_detail_args,
                *calibration_args,
                "--output-dir",
                path_for_command(holdout_synergy),
            ],
        ),
        Stage(
            "synergy-evaluation",
            holdout_synergy_eval / "experiment_report.md",
            [
                python,
                "-m",
                "evaluate_compirt",
                "--pyramidal-results",
                path_for_command(holdout_pyr),
                "--compositional-results",
                path_for_command(holdout_synergy),
                "--output-dir",
                path_for_command(holdout_synergy_eval),
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
    if prefix == "synergy":
        fields["synergy_dimensions"] = summary.get("synergy_dimensions")
        fields["synergy_tau"] = summary.get("tau")
    return fields


def normalize_metric_row(row: dict[str, object]) -> dict[str, object]:
    """Rename legacy metric keys while keeping current names authoritative."""
    normalized = dict(row)
    for old_name, new_name in LEGACY_METRIC_NAMES.items():
        if old_name in normalized and new_name not in normalized:
            normalized[new_name] = normalized.pop(old_name)
    return normalized


def read_metrics(evaluation_dir: Path, filename: str, prefix: str) -> dict[str, object]:
    """Read one evaluation metrics CSV and prefix every metric column."""
    path = metrics_path(evaluation_dir, filename)
    if not path.exists():
        return {}
    row = pd.read_csv(path).iloc[0].to_dict()
    row = normalize_metric_row(row)
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


def collect_run(root: Path, dimension: int) -> dict[str, object]:
    """Collect summaries and held-out metrics for one dimension."""
    current_run = run_dir(root, dimension)
    train_pyr = current_run / "train" / "pyramidal"
    holdout_pyr = current_run / "holdout" / "pyramidal"
    synergy = current_run / "holdout" / "synergy"
    evaluation = current_run / "holdout" / "synergy-evaluation"

    row: dict[str, object] = {
        "dimension": dimension,
        "run_path": path_for_command(current_run),
    }
    row.update(read_summary(train_pyr / "summary.json", "train_pyramidal"))
    row.update(read_summary(holdout_pyr / "summary.json", "holdout_pyramidal"))
    row.update(read_summary(synergy / "summary.json", "synergy"))
    row.update(read_metrics(evaluation, "bonus_metrics.csv", "bonus"))
    row.update(read_metrics(evaluation, "tossup_metrics.csv", "tossup"))
    if "tossup_accuracy" not in row:
        accuracy = tossup_accuracy_from_predictions(holdout_pyr / "tossup_predictions.csv")
        if accuracy is not None:
            row["tossup_accuracy"] = accuracy
    return row


def collect_results(root: Path, dimensions: list[int]) -> pd.DataFrame:
    """Collect all ablation rows ordered by dimension."""
    rows = [collect_run(root, dimension) for dimension in dimensions]
    return pd.DataFrame(rows).sort_values("dimension").reset_index(drop=True)


def save_metric_plot(
    frame: pd.DataFrame,
    output_dir: Path,
    metric: str,
    filename: str,
    ylabel: str,
    title: str,
) -> None:
    """Save a single metric-vs-dimension line plot."""
    if metric not in frame:
        print(f"skip plot {filename}: missing column {metric}", flush=True)
        return
    plot_data = frame[["dimension", metric]].copy()
    plot_data[metric] = pd.to_numeric(plot_data[metric], errors="coerce")
    plot_data = plot_data.dropna(subset=[metric])
    if plot_data.empty:
        print(f"skip plot {filename}: no finite values for {metric}", flush=True)
        return

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(plot_data["dimension"], plot_data[metric], marker="o", color="tab:blue")
    ax.set(title=title, xlabel="Number of latent dimensions (m)", ylabel=ylabel)
    ax.set_xticks(plot_data["dimension"].astype(int).tolist())
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, filename), dpi=160)
    plt.close(fig)


def save_aggregate_outputs(root: Path, frame: pd.DataFrame) -> Path:
    """Write the aggregate CSV and all ablation graphs."""
    csv_output = csv_path(root, "multidim_ablation_metrics.csv")
    frame.to_csv(csv_output, index=False)
    save_metric_plot(
        frame,
        root,
        "bonus_log_loss",
        "bonus_validation_loss_vs_dimensions.png",
        "Bonus Val. Log Loss",
        "Bonus validation loss vs latent dimensions",
    )
    save_metric_plot(
        frame,
        root,
        "bonus_part_accuracy",
        "bonus_validation_accuracy_vs_dimensions.png",
        "Bonus Val. Part Accuracy",
        "Bonus validation accuracy vs latent dimensions",
    )
    save_metric_plot(
        frame,
        root,
        "tossup_log_loss",
        "tossup_validation_loss_vs_dimensions.png",
        "Tossup Val. Log Loss",
        "Tossup validation loss vs latent dimensions",
    )
    save_metric_plot(
        frame,
        root,
        "tossup_auc",
        "tossup_validation_auc_vs_dimensions.png",
        "Tossup Val. AUC",
        "Tossup validation AUC vs latent dimensions",
    )
    save_metric_plot(
        frame,
        root,
        "tossup_accuracy",
        "tossup_validation_accuracy_vs_dimensions.png",
        "Tossup Val. Accuracy",
        "Tossup validation accuracy vs latent dimensions",
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
    """Parse command-line options for the ablation runner."""
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
        "--plot-dimensions",
        type=int,
        nargs="+",
        default=list(DEFAULT_PLOT_DIMENSIONS),
        help="Latent skill dimensions to include in the aggregate CSV and graphs.",
    )
    parser.add_argument("--synergy-dimensions", type=int, default=3)
    parser.add_argument(
        "--pyramidal-module",
        choices=tuple(PYRAMIDAL_MODULES),
        default="multidim",
        help="Stage-1 trainer to sweep: plain multidim MIRT or its TF-IDF variant.",
    )
    parser.add_argument(
        "--alpha-prior",
        choices=("normal", "gamma"),
        default="gamma",
        help=(
            "Bonus-part discrimination prior. 'gamma' matches the Gamma(2, 2) "
            "relevance vector of the multidim pyramidal stage."
        ),
    )
    parser.add_argument("--train-split", default="year_2024")
    parser.add_argument("--test-split", default="year_2025")
    parser.add_argument("--tournament")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--pyramidal-steps", type=int, default=3000)
    parser.add_argument("--bonus-steps", type=int, default=2000)
    parser.add_argument("--lr", type=float, default=0.01)
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
    if any(dimension < 1 for dimension in args.dimensions):
        raise ValueError("--dimensions values must all be at least 1")
    if any(dimension < 1 for dimension in args.plot_dimensions):
        raise ValueError("--plot-dimensions values must all be at least 1")
    if args.synergy_dimensions < 1:
        raise ValueError("--synergy-dimensions must be at least 1")
    if args.pyramidal_steps < 1 or args.bonus_steps < 1:
        raise ValueError("--pyramidal-steps and --bonus-steps must be at least 1")
    return args


def main() -> None:
    """Run the ablation, then write aggregate metrics and plots."""
    args = parse_args()
    configure_environment()
    args.root.mkdir(parents=True, exist_ok=True)
    if os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(args.root / "run.log")
    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/run_multidim_ablation.py",
                "ROOT": path_for_command(args.root),
                "MODEL": f"{args.pyramidal_module}-ablation",
                "PYRAMIDAL_MODULE": PYRAMIDAL_MODULES[args.pyramidal_module],
                "TRAIN_SPLIT": args.train_split,
                "TEST_SPLIT": args.test_split,
                "TOURNAMENT": args.tournament or "<all>",
                "DEVICE": args.device,
                "GPU": os.environ.get("GPU", "unknown"),
                "DIMENSIONS": args.dimensions,
                "PLOT_DIMENSIONS": args.plot_dimensions,
                "SYNERGY_DIMENSIONS": args.synergy_dimensions,
                "ALPHA_PRIOR": args.alpha_prior,
                "PYRAMIDAL_STEPS": args.pyramidal_steps,
                "BONUS_STEPS": args.bonus_steps,
                "LR": args.lr,
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
            print(f"\n=== multidim ablation: dimension {dimension} ===", flush=True)
            for stage in build_stages(args, dimension):
                run_stage(stage, args.rerun)

    metrics = collect_results(args.root, args.plot_dimensions)
    csv_output = save_aggregate_outputs(args.root, metrics)
    print(f"\nWrote aggregate metrics to {path_for_command(csv_output)}")
    print(f"Wrote aggregate graphs to {path_for_command(args.root / 'graphs')}")


if __name__ == "__main__":
    main()
