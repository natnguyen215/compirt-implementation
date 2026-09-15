#!/usr/bin/env python3
"""Run synergy-only in-sample model ranking comparisons for 2024 ACF Nationals.

The batch runner calls the training and evaluation entry points directly. For
each model it fits the pyramidal/player stage and synergy bonus stage, evaluates
the synergy predictions, and compares fitted player rankings with real 2024 ACF
Nationals individual scoring.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import shlex
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from run_scripts.common.lib.ablation import (
    path_for_command,
    repo_path,
    tournament_args as optional_tournament_args,
)
from run_scripts.common.lib.nationals_report import aggregate_markdown
from utils.run_logging import (
    format_run_log_header,
    resolve_result_root,
    run_logged,
    tee_run_output,
)


DEFAULT_TOURNAMENT = "2024-acf-nationals"
DEFAULT_SPLIT = "year_2024"
DEFAULT_MODEL_ROOT = Path("results/compirt/in_sample/common/in_sample_2024nationals")
DEFAULT_RANKING_ROOT = Path("results/ranking_comparison/in_sample_2024nationals")
DEFAULT_DATABASE = Path("data/database.db")


@dataclass(frozen=True)
class ModelSpec:
    """A model family in the Nationals comparison matrix."""

    name: str
    family: str


@dataclass(frozen=True)
class Stage:
    """One resumable command in a model/calibration run."""

    name: str
    kind: str
    markers: tuple[Path, ...]
    command: list[str]


@dataclass(frozen=True)
class ModelRun:
    """One model under one calibration setting."""

    model: str
    run_name: str
    calibrate_correctness: bool
    root: Path
    ranking_root: Path
    stages: tuple[Stage, ...]


MODEL_SPECS: tuple[ModelSpec, ...] = (
    ModelSpec("baseline", "baseline"),
    ModelSpec("multidim", "multidim"),
)
MODEL_BY_NAME = {spec.name: spec for spec in MODEL_SPECS}


def python_for_command(args: argparse.Namespace) -> str:
    return path_for_command(repo_path(args.python))


def optional_data_dir_args(args: argparse.Namespace) -> list[str]:
    return ["--data-dir", path_for_command(repo_path(args.data_dir))] if args.data_dir else []


def calibrate_args(calibrate: bool) -> list[str]:
    return ["--calibrate-correctness"] if calibrate else []


def synergy_detail_args(args: argparse.Namespace) -> list[str]:
    return ["--save-synergy-details"] if args.save_synergy_details else []


def run_name(model_name: str, calibrate: bool) -> str:
    return f"{model_name}-cal" if calibrate else model_name


def add_common_tossup_args(
    command: list[str],
    args: argparse.Namespace,
    dimensions: int,
    output_dir: Path,
    calibrate: bool,
) -> list[str]:
    command.extend(
        [
            "--split",
            args.split,
            *optional_tournament_args(args.tournament),
            *optional_data_dir_args(args),
            "--dimensions",
            str(dimensions),
            "--steps",
            str(args.pyramidal_steps),
            "--lr",
            str(args.lr),
            "--seed",
            str(args.seed),
            "--device",
            args.device,
            *calibrate_args(calibrate),
            "--output-dir",
            path_for_command(output_dir),
        ]
    )
    return command


def root_synergy_stage(
    args: argparse.Namespace,
    root: Path,
    calibrate: bool,
    *,
    module: str | None = None,
    script: str | None = "train_compositional.py",
    extra_args: Iterable[str] = (),
) -> Stage:
    """Build the synergy-only Stage-2 command for a fitted Stage-1 run."""
    python = python_for_command(args)
    if module:
        command = [python, "-m", module]
    else:
        command = [python, script or "train_compositional.py"]
    command.extend(
        [
            "--split",
            args.split,
            *optional_tournament_args(args.tournament),
            *optional_data_dir_args(args),
            "--player-skills",
            path_for_command(root / "pyramidal" / "players.csv"),
            "--steps",
            str(args.bonus_steps),
            "--lr",
            str(args.lr),
            "--seed",
            str(args.seed),
            "--device",
            args.device,
            "--use-synergy",
            "--synergy-dimensions",
            str(args.synergy_dimensions),
            *synergy_detail_args(args),
            *calibrate_args(calibrate),
            *extra_args,
            "--output-dir",
            path_for_command(root / "synergy"),
        ]
    )
    return Stage("synergy", "bonus", (root / "synergy" / "summary.json",), command)


def root_evaluation_stage(
    args: argparse.Namespace,
    root: Path,
) -> Stage:
    command = [
        python_for_command(args),
        "evaluate_compirt.py",
        "--pyramidal-results",
        path_for_command(root / "pyramidal"),
        "--compositional-results",
        path_for_command(root / "synergy"),
        "--output-dir",
        path_for_command(root / "synergy-evaluation"),
    ]
    return Stage(
        "synergy-evaluation",
        "evaluation",
        (root / "synergy-evaluation" / "experiment_report.md",),
        command,
    )


def ranking_stage(args: argparse.Namespace, root: Path, ranking_root: Path) -> Stage:
    command = [
        python_for_command(args),
        "run_scripts/common/run_player_rankings.py",
        "--tournament",
        args.tournament,
        "--database",
        path_for_command(repo_path(args.database)),
        "--player-summary",
        path_for_command(root / "pyramidal" / "player_buzz_summary.csv"),
        "--predictions",
        path_for_command(root / "pyramidal" / "tossup_predictions.csv"),
        "--output-dir",
        path_for_command(ranking_root),
        "--min-games",
        str(args.min_games),
        "--min-tuh",
        str(args.min_tuh),
        "--min-game-tossups",
        str(args.min_game_tossups),
        "--actual-top",
        str(args.actual_top),
        "--actual-rank-mode",
        args.actual_rank_mode,
    ]
    return Stage(
        "ranking-comparison",
        "ranking",
        (ranking_root / args.tournament / "summary.json",),
        command,
    )


def baseline_stages(
    args: argparse.Namespace, root: Path, ranking_root: Path, calibrate: bool
) -> tuple[Stage, ...]:
    """Build Stage 1, synergy, evaluation, and ranking for baseline CompIRT."""
    dimensions = args.dimensions
    pyramidal = Stage(
        "pyramidal",
        "pyramidal",
        (root / "pyramidal" / "summary.json",),
        add_common_tossup_args(
            [python_for_command(args), "train_pyramidal.py"],
            args,
            dimensions,
            root / "pyramidal",
            calibrate,
        ),
    )
    return (
        pyramidal,
        root_synergy_stage(args, root, calibrate),
        root_evaluation_stage(args, root),
        ranking_stage(args, root, ranking_root),
    )


def multidim_stages(
    args: argparse.Namespace, root: Path, ranking_root: Path, calibrate: bool
) -> tuple[Stage, ...]:
    pyramidal = Stage(
        "pyramidal",
        "pyramidal",
        (root / "pyramidal" / "summary.json",),
        add_common_tossup_args(
            [
                python_for_command(args),
                "-m",
                "multidimensional.multidim_mirt.train_pyramidal",
            ],
            args,
            args.dimensions,
            root / "pyramidal",
            calibrate,
        ),
    )
    return (
        pyramidal,
        root_synergy_stage(args, root, calibrate),
        root_evaluation_stage(args, root),
        ranking_stage(args, root, ranking_root),
    )


def build_model_run(
    args: argparse.Namespace, spec: ModelSpec, calibrate: bool
) -> ModelRun:
    current_run_name = run_name(spec.name, calibrate)
    root = repo_path(args.model_root) / current_run_name
    ranking_root = repo_path(args.ranking_root) / current_run_name
    if spec.family == "baseline":
        stages = baseline_stages(args, root, ranking_root, calibrate)
    elif spec.family == "multidim":
        stages = multidim_stages(args, root, ranking_root, calibrate)
    else:
        raise ValueError(f"Unknown model family: {spec.family}")
    return ModelRun(spec.name, current_run_name, calibrate, root, ranking_root, stages)


def selected_calibrations(args: argparse.Namespace) -> tuple[bool, ...]:
    """Return calibration settings in the established no-cal, cal order."""
    if args.calibration == "both":
        return (False, True)
    return (True,) if args.calibration == "cal" else (False,)


def build_model_runs(args: argparse.Namespace) -> list[ModelRun]:
    """Build the model/calibration command matrix, model-major."""
    return [
        build_model_run(args, spec, calibrate)
        for spec in selected_model_specs(args)
        for calibrate in selected_calibrations(args)
    ]


def build_setup_stages(args: argparse.Namespace) -> list[Stage]:
    if args.skip_validation:
        return []
    return [
        Stage(
            "validate-data",
            "setup",
            (),
            [python_for_command(args), "-m", "data_pipeline.validate"],
        ),
        Stage(
            "inspect-data",
            "setup",
            (),
            [
                python_for_command(args),
                "compirt_data.py",
                "--split",
                args.split,
                *optional_tournament_args(args.tournament),
                *optional_data_dir_args(args),
            ],
        ),
    ]


def stage_complete(stage: Stage) -> bool:
    return bool(stage.markers) and all(marker.exists() for marker in stage.markers)


def print_command(command: Iterable[str]) -> None:
    print("+ " + shlex.join([str(part) for part in command]), flush=True)


def run_stage(stage: Stage, *, dry_run: bool, rerun: bool) -> bool:
    if stage_complete(stage) and not rerun:
        markers = ", ".join(path_for_command(marker) for marker in stage.markers)
        print(f"skip {stage.name}: {markers}", flush=True)
        return False
    print_command(stage.command)
    if dry_run:
        return False
    run_logged(stage.command, cwd=REPO_ROOT)
    return True


def check_tournament_exists(database: Path, tournament: str) -> None:
    if not tournament:
        return
    database = repo_path(database)
    if not database.exists():
        raise FileNotFoundError(f"Database not found: {database}")
    connection = sqlite3.connect(database)
    try:
        row = connection.execute(
            "select 1 from tournament where slug = ? limit 1", (tournament,)
        ).fetchone()
    finally:
        connection.close()
    if row is None:
        raise ValueError(f"Tournament slug not found in {database}: {tournament}")


def read_ranking_summary(run: ModelRun, tournament: str) -> dict[str, object] | None:
    path = run.ranking_root / tournament / "summary.json"
    if not path.exists():
        return None
    row = json.loads(path.read_text(encoding="utf-8"))
    row.update(
        {
            "model": run.model,
            "run_name": run.run_name,
            "calibration": "cal" if run.calibrate_correctness else "no_cal",
            "result_root": path_for_command(run.root),
            "ranking_root": path_for_command(run.ranking_root / tournament),
        }
    )
    return row


def overlap_from_ranking_csv(
    run: ModelRun, tournament: str, *, actual_top: int, model_top: int
) -> str | None:
    """Return actual-top-N players captured by the model top-N ranking."""
    path = run.ranking_root / tournament / "player_ranking_comparison.csv"
    if not path.exists():
        return None
    overlap = 0
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            model_rank = row.get("tournament_model_rank")
            if not model_rank:
                continue
            if int(row["actual_rank"]) <= actual_top and int(model_rank) <= model_top:
                overlap += 1
    return f"{overlap}/{actual_top}"


def write_aggregate_outputs(
    args: argparse.Namespace, runs: list[ModelRun]
) -> tuple[Path, Path, Path] | None:
    """Collect completed ranking summaries and write CSV, JSON, and Markdown."""
    run_rows = [
        (run, row)
        for run in runs
        if (row := read_ranking_summary(run, args.tournament)) is not None
    ]
    rows = [row for _, row in run_rows]
    if not rows:
        return None
    for run, row in run_rows:
        top20 = overlap_from_ranking_csv(
            run, args.tournament, actual_top=20, model_top=20
        )
        if top20 is not None:
            row["actual_top_20_in_tournament_model_rank_top_20"] = top20
        top50 = overlap_from_ranking_csv(
            run, args.tournament, actual_top=50, model_top=50
        )
        if top50 is not None:
            row["actual_top_50_in_tournament_model_rank_top_50"] = top50
    for row in rows:
        kept_overlap_keys = {
            "actual_top_20_in_tournament_model_rank_top_20",
            "actual_top_50_in_tournament_model_rank_top_50",
        }
        for key in list(row):
            if (
                key == "global_rank_correlation"
                or key == "global_model_matches"
                or (key.startswith("actual_top_") and "_in_global_model_rank_" in key)
                or (
                    key.startswith("actual_top_")
                    and "_in_tournament_model_rank_" in key
                    and key not in kept_overlap_keys
                )
            ):
                row.pop(key, None)

    output_root = repo_path(args.ranking_root)
    output_root.mkdir(parents=True, exist_ok=True)
    preferred_columns = [
        "run_name",
        "model",
        "calibration",
        "tournament_rank_correlation",
        "actual_top_20_in_tournament_model_rank_top_20",
        "actual_top_50_in_tournament_model_rank_top_50",
        "tournament_model_matches",
        "actual_players_after_floor",
        "ranking_root",
        "result_root",
    ]
    extra_columns = sorted({key for row in rows for key in row} - set(preferred_columns))
    columns = preferred_columns + extra_columns

    csv_path = output_root / "model_ranking_summary.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    json_path = output_root / "model_ranking_summary.json"
    json_path.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")

    md_path = output_root / "model_ranking_summary.md"
    md_path.write_text(aggregate_markdown(args, rows), encoding="utf-8")
    return csv_path, md_path, json_path


def normalize_model_tokens(values: list[str] | None) -> list[str]:
    if not values:
        return [spec.name for spec in MODEL_SPECS]
    tokens: list[str] = []
    for value in values:
        tokens.extend(token for token in value.split(",") if token)
    return tokens


def selected_model_specs(args: argparse.Namespace) -> list[ModelSpec]:
    names = normalize_model_tokens(args.models)
    unknown = sorted(set(names) - set(MODEL_BY_NAME))
    if unknown:
        valid = ", ".join(MODEL_BY_NAME)
        raise ValueError(f"Unknown model(s): {', '.join(unknown)}. Valid models: {valid}")
    seen: set[str] = set()
    selected: list[ModelSpec] = []
    for name in names:
        if name in seen:
            continue
        seen.add(name)
        selected.append(MODEL_BY_NAME[name])
    return selected


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--models", nargs="*", help="Model names, space or comma separated")
    parser.add_argument(
        "--calibration",
        choices=("both", "no-cal", "cal"),
        default="both",
        help="Which correctness-calibration variants to run",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--rerun", action="store_true")
    parser.add_argument("--continue-on-error", action="store_true")
    parser.add_argument("--skip-validation", action="store_true")
    parser.add_argument("--python", type=Path, default=Path(".venv/bin/python"))
    parser.add_argument("--database", type=Path, default=DEFAULT_DATABASE)
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--model-root", type=Path, default=DEFAULT_MODEL_ROOT)
    parser.add_argument("--ranking-root", type=Path, default=DEFAULT_RANKING_ROOT)
    parser.add_argument("--split", default=DEFAULT_SPLIT)
    parser.add_argument("--tournament", default=DEFAULT_TOURNAMENT)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument("--gpu", default="0")
    parser.add_argument("--dimensions", type=int, default=5)
    parser.add_argument("--pyramidal-steps", type=int, default=5000)
    parser.add_argument("--bonus-steps", type=int, default=3000)
    parser.add_argument("--lr", type=float, default=0.005)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--synergy-dimensions", type=int, default=3)
    parser.add_argument("--no-save-synergy-details", dest="save_synergy_details", action="store_false")
    parser.set_defaults(save_synergy_details=True)
    parser.add_argument(
        "--actual-rank-mode", choices=("ppg", "pp20"), default="ppg"
    )
    parser.add_argument("--min-games", type=int, default=1)
    parser.add_argument("--min-tuh", type=int, default=1)
    parser.add_argument("--min-game-tossups", type=int, default=20)
    parser.add_argument("--actual-top", type=int, default=20)
    args = parser.parse_args(argv)

    if args.dimensions < 1:
        raise ValueError("--dimensions must be at least 1")
    if args.pyramidal_steps < 1:
        raise ValueError("--pyramidal-steps must be at least 1")
    if args.bonus_steps < 1:
        raise ValueError("--bonus-steps must be at least 1")
    if args.lr <= 0:
        raise ValueError("--lr must be positive")
    if args.synergy_dimensions < 1:
        raise ValueError("--synergy-dimensions must be at least 1")
    if (
        args.min_games < 0
        or args.min_tuh < 0
        or args.min_game_tossups < 1
        or args.actual_top < 1
    ):
        raise ValueError(
            "Player thresholds must be non-negative, min-game-tossups and actual-top positive"
        )
    # Place model outputs under results/compirt/in_sample/ while keeping the
    # ranking root outside results/compirt/.
    args.model_root = Path(resolve_result_root(args.model_root, "in_sample"))
    # Validate model names during parsing so dry-runs fail early and clearly.
    selected_model_specs(args)
    return args


def configure_environment(args: argparse.Namespace) -> None:
    os.environ["CUDA_VISIBLE_DEVICES"] = args.gpu
    os.environ.setdefault("PYTHONUNBUFFERED", "1")
    os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-compirt")
    os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")


def main(argv: list[str] | None = None) -> int:
    """Run the selected model matrix and aggregate completed ranking outputs."""
    args = parse_args(argv)
    configure_environment(args)
    check_tournament_exists(args.database, args.tournament)

    # Expand model and calibration choices into independently resumable runs.
    runs = build_model_runs(args)
    if not args.dry_run and os.environ.get("COMPIRT_LOG_ACTIVE") != "1":
        os.environ["COMPIRT_LOG_ACTIVE"] = "1"
        tee_run_output(repo_path(args.ranking_root) / "run.log")

    print(
        format_run_log_header(
            {
                "RUNNER": "run_scripts/common/run_2024_nationals_in_sample_ranking_comparison.py",
                "MODEL_ROOT": path_for_command(repo_path(args.model_root)),
                "RANKING_ROOT": path_for_command(repo_path(args.ranking_root)),
                "MODELS": [run.run_name for run in runs],
                "SPLIT": args.split,
                "TOURNAMENT": args.tournament,
                "DEVICE": args.device,
                "GPU": args.gpu,
                "CALIBRATION": args.calibration,
                "DIMENSIONS": args.dimensions,
                "PYRAMIDAL_STEPS": args.pyramidal_steps,
                "BONUS_STEPS": args.bonus_steps,
                "LR": args.lr,
                "SEED": args.seed,
                "RUN_SYNERGY": "1",
                "SYNERGY_DIMENSIONS": args.synergy_dimensions,
                "SAVE_SYNERGY_DETAILS": args.save_synergy_details,
                "DRY_RUN": args.dry_run,
                "RERUN": args.rerun,
                "CONTINUE_ON_ERROR": args.continue_on_error,
                "PYTHON": path_for_command(repo_path(args.python)),
            }
        ),
        flush=True,
    )

    # Run shared setup once, followed by each model's ordered stage sequence.
    failures: list[str] = []
    for setup_stage in build_setup_stages(args):
        try:
            run_stage(setup_stage, dry_run=args.dry_run, rerun=args.rerun)
        except Exception as error:
            if not args.continue_on_error:
                raise
            failures.append(f"{setup_stage.name}: {error}")

    for run in runs:
        print(f"\n## {run.run_name}", flush=True)
        for stage in run.stages:
            try:
                run_stage(stage, dry_run=args.dry_run, rerun=args.rerun)
            except Exception as error:
                failures.append(f"{run.run_name}/{stage.name}: {error}")
                print(f"failed {run.run_name}/{stage.name}: {error}", file=sys.stderr)
                if not args.continue_on_error:
                    raise
                break

    # Aggregate only materialized runs; dry runs print commands without outputs.
    aggregate = None
    if not args.dry_run:
        aggregate = write_aggregate_outputs(args, runs)
        if aggregate is not None:
            csv_path, md_path, json_path = aggregate
            print(f"\nWrote {path_for_command(csv_path)}")
            print(f"Wrote {path_for_command(md_path)}")
            print(f"Wrote {path_for_command(json_path)}")

    if failures:
        print("\nFailed stages:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
