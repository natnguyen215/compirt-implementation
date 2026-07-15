"""Shared scaffolding for the resumable ablation sweep runners.

The model-family trainers are deliberately self-contained near-copies (see the
root CLAUDE.md), but this module is generic orchestration infrastructure:
marker-file resume, repo-relative path rendering, summary/metric collection,
config snapshots, and the plot and argument boilerplate every sweep runner
shares. Runner-specific stage matrices, aggregation layouts, and plots stay in
the runners themselves.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
from dataclasses import dataclass
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-compirt")

import matplotlib.pyplot as plt
import pandas as pd

from compirt_eval.outputs import graph_path, metrics_path
from utils.run_logging import resolve_result_root, run_logged, tee_run_output

REPO_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Stage:
    """One resumable command in an ablation run."""

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
    """Return the output directory for one swept dimension."""
    return root / f"dim_{dimension}"


def run_stage(stage: Stage, rerun: bool) -> None:
    """Run one stage unless its marker already exists."""
    if stage.marker.exists() and not rerun:
        print(f"skip {stage.name}: {path_for_command(stage.marker)}", flush=True)
        return
    print("+ " + shlex.join(stage.command), flush=True)
    run_logged(stage.command, cwd=REPO_ROOT)


def read_summary(
    path: Path, prefix: str, extra_fields: dict[str, str] | None = None
) -> dict[str, object]:
    """Read a stage summary, keeping loss/steps plus requested extra fields.

    'extra_fields' maps aggregate-CSV column names to summary JSON keys, for
    the stage-specific scalars a runner wants carried into its rows.
    """
    if not path.exists():
        return {}
    summary = json.loads(path.read_text(encoding="utf-8"))
    fields = {
        f"{prefix}_final_loss": summary.get("final_loss"),
        f"{prefix}_steps": summary.get("steps"),
    }
    for column, key in (extra_fields or {}).items():
        fields[column] = summary.get(key)
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


def save_metric_plot(
    frame: pd.DataFrame,
    output_dir: Path,
    metric: str,
    filename: str,
    ylabel: str,
    title: str,
    xlabel: str = "Number of latent dimensions (m)",
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
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    ax.set_xticks(plot_data["dimension"].astype(int).tolist())
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(graph_path(output_dir, filename), dpi=160)
    plt.close(fig)


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


def start_run_log(root: Path) -> None:
    """Create the result root and tee all further output into its run.log."""
    root.mkdir(parents=True, exist_ok=True)
    if os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(root / "run.log")


def add_shared_sweep_arguments(
    parser: argparse.ArgumentParser, default_root: Path
) -> None:
    """Add the CLI options every ablation sweep runner exposes identically.

    Runner-specific options (sweep axes, seeds, model knobs) stay in each
    runner's own 'parse_args'.
    """
    parser.add_argument("--root", type=Path, default=default_root)
    parser.add_argument("--train-split", default="year_2024")
    parser.add_argument("--test-split", default="year_2025")
    parser.add_argument("--tournament")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--pyramidal-steps", type=int, default=3000)
    parser.add_argument("--bonus-steps", type=int, default=2000)
    # One default for every family (not each trainer's own default) so the
    # families' ablation curves stay comparable.
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


def finalize_shared_sweep_args(args: argparse.Namespace) -> argparse.Namespace:
    """Resolve shared paths into the holdout tier and validate step counts."""
    args.root = Path(resolve_result_root(repo_path(args.root), "holdout"))
    args.data_dir = repo_path(args.data_dir)
    if args.pyramidal_steps < 1 or args.bonus_steps < 1:
        raise ValueError("--pyramidal-steps and --bonus-steps must be at least 1")
    return args
