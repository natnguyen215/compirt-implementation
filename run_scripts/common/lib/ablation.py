"""Shared scaffolding for the resumable ablation sweep runners.

This module handles expected-output resume, repo-relative path rendering,
summary and metric collection, configuration snapshots, plots, and shared
arguments. Each runner defines its own stage matrix, aggregation layout, and
family-specific plots.
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

from compirt_eval.common.report_paths import graph_path, metrics_path
from utils.run_logging import resolve_result_root, run_logged, tee_run_output

REPO_ROOT = Path(__file__).resolve().parents[3]


@dataclass(frozen=True)
class Stage:
    """One resumable command in an ablation run."""

    name: str
    expected_output: Path
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
    """Run one stage unless its expected output already exists."""
    if stage.expected_output.exists() and not rerun:
        print(
            f"skip {stage.name}: {path_for_command(stage.expected_output)}",
            flush=True,
        )
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


def stage_config(stages: list[Stage]) -> list[dict[str, object]]:
    """Return the human-readable command contract for resumable stages."""
    return [
        {
            "name": stage.name,
            "expected_output": path_for_command(stage.expected_output),
            "command": [str(value) for value in stage.command],
        }
        for stage in stages
    ]


def _has_existing_outputs(root: Path, stages: list[Stage]) -> bool:
    """Return whether a previous sweep already left results under ``root``."""
    return any(root.glob("dim_*")) or any(
        stage.expected_output.exists() for stage in stages
    )


def _stage_key(stage: dict[str, object], result_roots: list[str]) -> tuple[str, ...]:
    """Identify a stage by name and command, with the result root masked out.

    A sweep resumed after its output directory moved keeps the same stages, so
    the root prefix is replaced by a placeholder before stages are compared.
    """

    def mask(value: str) -> str:
        for candidate in result_roots:
            if candidate in value:
                return value.replace(candidate, "<ABLATION_ROOT>")
        return value

    command = [str(value) for value in stage["command"]]
    return (str(stage["name"]), *(mask(str(stage["expected_output"])), *map(mask, command)))


def validate_ablation_resume(
    root: Path,
    stages: list[Stage],
    rerun: bool,
    *,
    allow_partial_resume: bool = False,
) -> None:
    """Reject completed outputs produced by a different or unknown command set.

    Dimension sweeps may be resumed with a larger or smaller dimension list, and
    from a moved output directory. With ``allow_partial_resume`` the run is
    accepted as long as it shares at least one stage with the saved sweep;
    shared stages must still match command-for-command, so this lets a stopped
    sweep add missing points without weakening protection against changed model
    settings.
    """
    if rerun:
        return
    config_path = root / "ablation_config.json"
    if not config_path.exists():
        if _has_existing_outputs(root, stages):
            raise RuntimeError(
                f"Existing ablation outputs under {root} have no saved command "
                "metadata; use --rerun or a new --root"
            )
        return

    saved = json.loads(config_path.read_text(encoding="utf-8"))
    saved_stages = saved.get("stages")
    if saved_stages is None and not _has_existing_outputs(root, stages):
        return

    current_stages = stage_config(stages)
    if saved_stages == current_stages:
        return

    if allow_partial_resume and saved_stages is not None:
        # Mask both this run's root and the root the snapshot was written under,
        # longest first so a path that contains the other still masks cleanly.
        saved_root = saved.get("arguments", {}).get("root")
        candidates = {str(root), path_for_command(root)}
        if saved_root:
            candidates.update({str(Path(saved_root)), path_for_command(Path(saved_root))})
        result_roots = sorted(
            (value for value in candidates if value and value != "."),
            key=len,
            reverse=True,
        )
        saved_keys = {_stage_key(stage, result_roots) for stage in saved_stages}
        if saved_keys & {_stage_key(stage, result_roots) for stage in current_stages}:
            return

    raise RuntimeError(
        f"Existing ablation outputs under {root} were produced by different "
        "commands; use --rerun or a new --root"
    )


def save_ablation_config(
    root: Path, args: argparse.Namespace, stages: list[Stage]
) -> Path:
    """Record every resolved runner setting next to the results.

    Lets a sweep be reproduced from its output directory alone, without having to
    recover the invocation from 'run.log'.
    """
    arguments = {
        key: str(value) if isinstance(value, Path) else value
        for key, value in sorted(vars(args).items())
    }
    config = {"arguments": arguments, "stages": stage_config(stages)}
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
    parser.add_argument("--save-synergy-details", action="store_true")
    parser.add_argument(
        "--rerun",
        action="store_true",
        help="Run stages even when their expected output files already exist.",
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
