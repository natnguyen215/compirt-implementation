"""Fit and score bonus models using existing whole-game Stage-1 training folds.

Each source fold must contain train/pyramidal/{summary.json,players.csv,
tossup_predictions.csv}. Its summary determines the train/test split. Player
skills stay frozen; training-game bonuses fit the bonus-part parameters and
optional pairwise synergy. The 'compositional' arm fits without synergy and the
'synergy' arm adds it; both use the root compositional model.

This runner owns the training and replay commands. Fold audits, evaluation,
and pooling live in compirt_eval/scenario_b_bonuses/folds.py.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import sys

from compirt_eval.common.bonus_reports import write_bonus_fold_reports
from compirt_eval.scenario_b_bonuses.folds import aggregate, evaluate_fold
from compositional_model import (
    BONUS_AGGREGATIONS,
    BONUS_DIFFICULTIES,
    SYNERGY_FORMS,
    SYNERGY_LINKS,
    validate_bonus_settings,
)
from holdout.game_splits import game_holdout_split_name, parse_game_holdout_split
from utils.run_logging import resolve_result_root, run_logged

REPO_ROOT = Path(__file__).resolve().parents[2]
ARMS = ("compositional", "synergy")

# Command-line options that choose how to run, kept out of the saved configuration.
EXECUTION_OPTIONS = (
    "dry_run", "collect_only", "evaluate_only", "report_only", "prepare_only",
    "worker_fold", "worker_arm", "worker_stage",
)

# Source files whose hashes are saved; resuming requires the same code.
HASHED_SOURCES = (
    "compositional_model.py", "train_compositional.py", "holdout/frozen_predict.py",
    "compirt_data.py", "lineup.py", "holdout/game_splits.py", "utils/training.py",
    "compirt_eval/scenario_b_bonuses/metrics.py", "compirt_eval/common/metrics.py",
    "compirt_eval/scenario_b_bonuses/folds.py", "compirt_eval/common/bonus_reports.py",
    "run_scripts/common/run_compositional_from_folds.py",
)


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def source_fold(stage1_root, fold):
    """Describe one saved Stage-1 training fold: its splits, hashes, and settings.

    The test split is derived from the fit's own training split, so a fold
    saved under the wrong index raises ValueError.
    """
    source = stage1_root / f"fold_{fold}" / "train" / "pyramidal"
    summary = json.loads((source / "summary.json").read_text())
    spec = parse_game_holdout_split(summary["split"])
    if spec is None or spec.part != "train" or spec.fold_index != fold:
        raise ValueError(f"Expected a whole-game training fit for fold {fold}: {source}")
    if summary.get("tournament"):
        raise ValueError("Tournament-filtered source fits are not supported")
    test_split = game_holdout_split_name(
        spec.base_split, "test", spec.n_folds, fold, spec.seed
    )
    return {
        "path": str(source.resolve()),
        "train_split": summary["split"],
        "test_split": test_split,
        "players_sha256": sha256(source / "players.csv"),
        "summary_sha256": sha256(source / "summary.json"),
        "tossup_predictions_sha256": sha256(source / "tossup_predictions.csv"),
        "model": summary.get("model"),
        "dimensions": summary.get("dimensions"),
        "degree": summary.get("polynomial_degree"),
        "relevance_prior": summary.get("relevance_prior_family"),
        "learned_curve_locations": summary.get("learned_curve_locations"),
        "terminal_intercepts": summary.get("terminal_intercepts"),
    }


def commands(config, fold, arm):
    """Return (stage, output directory, command) for training and frozen replay."""
    source = config["sources"][str(fold)]
    run = Path(config["root"]) / f"fold_{fold}"
    train = run / "train" / arm
    test = run / "holdout" / arm
    data_args = ["--data-dir", config["data_dir"]] if config["data_dir"] else []
    common = [*data_args, "--device", config["device"]]
    # Configurations saved before an option existed used its default.
    training = [
        sys.executable, "-u", str(REPO_ROOT / "train_compositional.py"),
        "--split", source["train_split"], *common,
        "--player-skills", str(Path(source["path"]) / "players.csv"),
        "--steps", str(config["steps"]), "--lr", str(config["lr"]),
        "--seed", str(config["seed"]), "--alpha-prior", config["alpha_prior"],
        "--bonus-difficulty", config.get("bonus_difficulty", "scalar"),
        "--bonus-aggregation", config.get("bonus_aggregation", "lse"),
        "--posterior-draws", "0", "--output-dir", str(train),
    ]
    # Replay reads the bonus settings from the training summary.
    replay = [
        sys.executable, "-u", "-m", "holdout.frozen_predict", "bonus",
        "--split", source["test_split"], *common,
        "--train-pyramidal", source["path"],
        "--train-compositional", str(train), "--output-dir", str(test),
        "--on-missing", "error",
    ]
    if arm == "synergy":
        training += [
            "--use-synergy", "--save-synergy-details",
            "--synergy-dimensions", str(config.get("synergy_dimensions", 1)),
            "--synergy-form", config.get("synergy_form", "dot"),
            "--synergy-link", config.get("synergy_link", "additive"),
        ]
        replay += ["--use-synergy"]
    return [("train", train, training), ("replay", test, replay)]


def run_arm(config, fold, arm, dry_run=False, only_stage=None):
    """Train, replay, and evaluate one fold and arm, skipping completed stages.

    Each stage streams to the console and to its own run.log. 'only_stage'
    limits the call to one of "train", "replay", or "evaluate".
    """
    run = Path(config["root"]) / f"fold_{fold}"
    stages = commands(config, fold, arm)
    if only_stage is not None:
        stages = [stage for stage in stages if stage[0] == only_stage]
    if dry_run:
        for _, _, command in stages:
            print(shlex.join(command))
        return
    suffix = f"_{only_stage}" if only_stage else ""
    write_json(run / f"{arm}{suffix}_commands.json", [c for _, _, c in stages])
    for name, output, command in stages:
        # A stage's summary.json marks it complete.
        if (output / "summary.json").exists():
            print(f"Fold {fold} | {arm} | {name}: already complete, skipping", flush=True)
            continue
        output.mkdir(parents=True, exist_ok=True)
        detail = f" ({config['steps']:,} steps)" if name == "train" else ""
        print(f"\nFold {fold} | {arm} | {name}{detail}", flush=True)
        env = {**os.environ, "OMP_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
        run_logged(command, cwd=REPO_ROOT, env=env, log_path=output / "run.log")
    if only_stage in ("train", "replay"):
        return
    print(f"\nFold {fold} | {arm} | evaluate", flush=True)
    evaluate_fold(config, fold, arm)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage1-root", type=Path)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--folds", nargs="+", type=int, default=list(range(5)))
    parser.add_argument("--arms", nargs="+", choices=ARMS, default=list(ARMS))
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--alpha-prior", choices=("normal", "gamma"), default="gamma")
    parser.add_argument("--bonus-difficulty", choices=BONUS_DIFFICULTIES, default="scalar")
    parser.add_argument("--bonus-aggregation", choices=BONUS_AGGREGATIONS, default="lse")
    parser.add_argument("--synergy-form", choices=SYNERGY_FORMS, default="dot")
    parser.add_argument("--synergy-link", choices=SYNERGY_LINKS, default="additive")
    parser.add_argument("--synergy-dimensions", type=int, default=1)
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--collect-only", action="store_true",
                        help="re-pool saved fold predictions and metrics, then rewrite reports")
    parser.add_argument("--report-only", action="store_true",
                        help="rewrite Markdown reports from saved metrics")
    parser.add_argument("--evaluate-only", action="store_true",
                        help="rescore saved predictions and redraw figures, then re-pool and rewrite reports")
    parser.add_argument("--prepare-only", action="store_true",
                        help="validate sources and save the configuration")
    parser.add_argument("--worker-fold", type=int,
                        help="run one configured fold; pool afterwards with --collect-only")
    parser.add_argument("--worker-arm", choices=ARMS)
    parser.add_argument("--worker-stage", choices=("train", "replay", "evaluate"))
    return parser, parser.parse_args(argv)


def refresh_saved_run(args):
    """Rescore, re-pool, or rewrite reports for a saved run using its configuration."""
    manifest = args.root / "configuration.json"
    config = json.loads(manifest.read_text())
    if Path(config["root"]).resolve() != args.root.resolve():
        raise ValueError(f"Saved root differs from --root: {manifest}")
    if args.stage1_root is not None and args.stage1_root.resolve() != Path(config["stage1_root"]).resolve():
        raise ValueError("--stage1-root differs from the saved configuration")
    if args.report_only:
        write_bonus_fold_reports(config)
        print(f"Bonus report: {args.root / 'aggregate/report.md'}")
        return
    for fold in config["folds"]:
        # Compare resolved paths so a saved symlinked source still matches.
        saved_source = dict(config["sources"][str(fold)])
        if "path" in saved_source:
            saved_source["path"] = str(Path(saved_source["path"]).resolve())
        if source_fold(Path(config["stage1_root"]), fold) != saved_source:
            raise ValueError(f"Source artifacts changed for fold {fold}; cannot refresh this evaluation")
    if args.evaluate_only:
        for fold in config["folds"]:
            for arm in config["arms"]:
                run_arm(config, fold, arm, only_stage="evaluate")
    aggregate(config)


def check_training_args(parser, args):
    """Report invalid training options through the argument parser."""
    if args.stage1_root is None:
        parser.error("--stage1-root is required for training")
    validate_bonus_settings(args.bonus_aggregation, args.bonus_difficulty,
                            use_synergy="synergy" in args.arms)
    if args.steps < 1 or not math.isfinite(args.lr) or args.lr <= 0:
        parser.error("steps and learning rate must be positive and finite")
    if args.bonus_difficulty == "multidim" and args.alpha_prior != "gamma":
        parser.error("--bonus-difficulty multidim requires --alpha-prior gamma")
    if args.synergy_dimensions < 1:
        parser.error("synergy dimensions must be positive")
    if len(set(args.folds)) != len(args.folds) or len(set(args.arms)) != len(args.arms):
        parser.error("duplicate folds or arms are not allowed")
    worker = args.worker_fold is not None
    if worker and args.worker_fold not in args.folds:
        parser.error("--worker-fold must belong to --folds")
    if args.worker_arm is not None and (not worker or args.worker_arm not in args.arms):
        parser.error("--worker-arm requires a worker fold and must belong to --arms")
    if args.worker_stage is not None and args.worker_arm is None:
        parser.error("--worker-stage requires --worker-arm")
    if (worker and args.prepare_only) or (args.prepare_only and args.dry_run):
        parser.error("worker, prepare-only, and dry-run modes cannot be combined")


def training_config(args):
    """Return the saved configuration: settings, source folds, and code hashes."""
    config = {k: (str(v.resolve()) if isinstance(v, Path) else v)
              for k, v in vars(args).items() if k not in EXECUTION_OPTIONS}
    config["sources"] = {str(fold): source_fold(args.stage1_root, fold) for fold in args.folds}
    specs = [parse_game_holdout_split(s["train_split"]) for s in config["sources"].values()]
    if len({(s.base_split, s.n_folds, s.seed) for s in specs}) != 1:
        raise ValueError("Source folds must use the same base split, fold count and split seed")
    config["code_sha256"] = {p: sha256(REPO_ROOT / p) for p in HASHED_SOURCES}
    return config


def main(argv=None):
    parser, args = parse_args(argv)
    args.root = Path(resolve_result_root(args.root, "holdout"))

    refresh_modes = (args.evaluate_only, args.collect_only, args.report_only)
    if any(refresh_modes):
        if sum(refresh_modes) > 1 or args.dry_run or args.prepare_only or any(
            value is not None for value in (args.worker_fold, args.worker_arm, args.worker_stage)
        ):
            parser.error("refresh modes cannot be combined with other execution modes")
        refresh_saved_run(args)
        return

    check_training_args(parser, args)
    worker = args.worker_fold is not None
    config = training_config(args)
    manifest = args.root / "configuration.json"
    if manifest.exists():
        if json.loads(manifest.read_text()) != config:
            raise ValueError(f"Resume configuration or source files changed: use a new --root ({manifest})")
    elif not args.dry_run:
        # Workers resume a configuration their launcher already saved.
        if worker:
            raise ValueError(f"No saved configuration at {manifest}")
        write_json(manifest, config)
    if args.prepare_only:
        return

    if not args.dry_run:
        print(f"Bonus results: {args.root}", flush=True)
        print(f"Steps: {args.steps:,} | Learning rate: {args.lr} | "
              f"Seed: {args.seed} | Device: {args.device}", flush=True)
        print(f"Difficulty: {args.bonus_difficulty} | Alpha prior: {args.alpha_prior}", flush=True)
        if "synergy" in args.arms:
            print(f"Synergy: {args.synergy_link} {args.synergy_form}, "
                  f"{args.synergy_dimensions}D", flush=True)
    for fold in ([args.worker_fold] if worker else args.folds):
        for arm in ([args.worker_arm] if args.worker_arm else args.arms):
            run_arm(config, fold, arm, args.dry_run, args.worker_stage)
    if not args.dry_run and not worker:
        print(f"\nPooling {len(args.folds)} folds", flush=True)
        aggregate(config)


if __name__ == "__main__":
    main()
