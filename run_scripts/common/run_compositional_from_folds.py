"""Fit and score bonus models using existing whole-game Stage-1 training folds.

Each source fold must contain train/pyramidal/{summary.json,players.csv,
tossup_predictions.csv}. Its summary determines the train/test split. Player
skills stay frozen; only training-game bonuses fit alpha, beta, tau and optional
rank-one synergy. The two arms share the root compositional implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import shlex
import subprocess
import sys

import numpy as np
import pandas as pd

from compirt_eval.common.report_paths import csv_path, evaluation_output_dirs
from compirt_eval.common.reports import experiment_report_markdown, write_eval_docs_summary
from compirt_eval.scenario_b_bonuses.evaluation import evaluate_bonuses
from compirt_eval.scenario_b_bonuses.metrics import bonus_metrics
from holdout.game_splits import game_holdout_split_name, parse_game_holdout_split
from utils.run_logging import resolve_result_root

REPO_ROOT = Path(__file__).resolve().parents[2]
ARMS = ("compositional", "synergy")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def source_fold(stage1_root, fold):
    """Derive scoring splits from the actual source fit, rejecting wrong folds."""
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
    source = config["sources"][str(fold)]
    run = Path(config["root"]) / f"fold_{fold}"
    train = run / "train" / arm
    test = run / "holdout" / arm
    data_args = ["--data-dir", config["data_dir"]] if config["data_dir"] else []
    common = [*data_args, "--device", config["device"]]
    training = [
        sys.executable, "-u", str(REPO_ROOT / "train_compositional.py"),
        "--split", source["train_split"], *common,
        "--player-skills", str(Path(source["path"]) / "players.csv"),
        "--steps", str(config["steps"]), "--lr", str(config["lr"]),
        "--seed", str(config["seed"]), "--alpha-prior", config["alpha_prior"],
        "--posterior-draws", "0", "--output-dir", str(train),
    ]
    replay = [
        sys.executable, "-u", "-m", "holdout.frozen_predict", "bonus",
        "--split", source["test_split"], *common,
        "--train-pyramidal", source["path"],
        "--train-compositional", str(train), "--output-dir", str(test),
        "--on-missing", "error",
    ]
    if arm == "synergy":
        training += ["--use-synergy", "--synergy-dimensions", "1", "--save-synergy-details"]
        replay += ["--use-synergy"]
    return [("train", train, training), ("replay", test, replay)]


def audit_predictions(train_parts, test_parts, stage1_games):
    """Fail on leakage, invalid probabilities, or incomplete bonus responses."""
    train_games = set(train_parts["game_id"])
    test_games = set(test_parts["game_id"])
    if train_games & test_games or set(stage1_games) & test_games:
        raise ValueError("Held-out bonus games overlap a training stage")
    if not train_games <= set(stage1_games):
        raise ValueError("Bonus training games are absent from the saved Stage-1 fit")
    if set(train_parts["response_id"]) & set(test_parts["response_id"]):
        raise ValueError("Bonus responses overlap between train and test")
    for parts in (train_parts, test_parts):
        if parts.empty or parts["observation_id"].duplicated().any():
            raise ValueError("Empty or duplicate bonus-part predictions")
        p = parts["predicted_correct"].to_numpy()
        if not np.isfinite(p).all() or not ((0 <= p) & (p <= 1)).all():
            raise ValueError("Invalid bonus probabilities")
        if not (parts.groupby("response_id").size() == 3).all():
            raise ValueError("Expected complete three-part bonus responses")
    return {
        "train_games": len(train_games), "test_games": len(test_games),
        "train_responses": train_parts["response_id"].nunique(),
        "test_responses": test_parts["response_id"].nunique(),
        "test_parts": len(test_parts), "disjoint_games": True,
        "finite_probabilities": True,
    }


def run_arm(config, fold, arm, dry_run=False, only_stage=None):
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
        if (output / "summary.json").exists():
            print(f"Resume fold {fold} {arm} {name}", flush=True)
            continue
        output.mkdir(parents=True, exist_ok=True)
        print(f"Fold {fold} {arm} {name}: {shlex.join(command)}", flush=True)
        env = {**os.environ, "OMP_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"}
        with (output / "run.log").open("w") as log:
            subprocess.run(command, cwd=REPO_ROOT, env=env, stdout=log,
                           stderr=subprocess.STDOUT, check=True)
    if only_stage in ("train", "replay"):
        return
    train, test = run / "train" / arm, run / "holdout" / arm
    train_parts = pd.read_csv(train / "bonus_part_predictions.csv")
    test_parts = pd.read_csv(test / "bonus_part_predictions.csv")
    source = Path(config["sources"][str(fold)]["path"])
    stage1_games = pd.read_csv(source / "tossup_predictions.csv", usecols=["game_id"])["game_id"]
    audit = audit_predictions(train_parts, test_parts, stage1_games)
    for name, directory in (("train", train), ("test", test)):
        summary = json.loads((directory / "summary.json").read_text())
        audit[f"{name}_dropped_rows_unknown_roster"] = summary.get("dropped_rows_unknown_roster", 0)
        if audit[f"{name}_dropped_rows_unknown_roster"]:
            raise ValueError(f"Uncovered players in {directory}")
    summary = json.loads((train / "summary.json").read_text())
    if not summary["finite_losses"]:
        raise ValueError(f"Nonfinite training losses in {train}")
    evaluation = run / ("evaluation" if arm == "compositional" else "synergy-evaluation")
    evaluation_output_dirs(evaluation)
    metrics = evaluate_bonuses(test, evaluation)
    pd.DataFrame([metrics]).to_csv(csv_path(evaluation, "bonus_metrics.csv"), index=False)
    report = experiment_report_markdown(
        evaluation, tossup=None, bonus=metrics, title="Frozen Bonus Evaluation"
    )
    report += (
        "\n## Distributions\n\n"
        "[Evaluated probabilities, aggregate ability, and synergy contributions]"
        "(graphs/bonus/bonus_prediction_distributions.png). "
        "Aggregate ability is part-weighted; synergy is response-weighted.\n\n"
        "[Fitted bonus parameters](graphs/parameters/bonus_part_parameter_distributions.png) "
        "describe the training fit. These distributions are across entities, "
        "not posterior uncertainty intervals.\n"
    )
    if arm == "synergy":
        report += "\n[Synergy parameters](graphs/parameters/synergy_parameter_distributions.png).\n"
    (evaluation / "experiment_report.md").write_text(report, encoding="utf-8")
    write_eval_docs_summary(evaluation)
    write_json(run / f"{arm}_checks.json", audit)
    print(f"Fold {fold} {arm}: AUC={metrics['auc']:.4f}, "
          f"log loss={metrics['log_loss']:.4f}, PPB MAE={metrics['ppb_mae']:.4f}", flush=True)


def aggregate(config):
    rows, pooled = [], []
    for arm in config["arms"]:
        all_parts, all_teams = [], []
        for fold in config["folds"]:
            run = Path(config["root"]) / f"fold_{fold}"
            test = run / "holdout" / arm
            checks = json.loads((run / f"{arm}_checks.json").read_text())
            evaluation = run / ("evaluation" if arm == "compositional" else "synergy-evaluation")
            metrics = pd.read_csv(evaluation / "csvs" / "bonus_metrics.csv").iloc[0].to_dict()
            summary = json.loads((run / "train" / arm / "summary.json").read_text())
            rows.append({"fold": fold, "arm": arm, **metrics, **checks,
                         **{k: summary[k] for k in ("tau", "final_loss", "best_loss", "last_100_loss_slope", "finite_losses")}})
            all_parts.append(pd.read_csv(test / "bonus_part_predictions.csv"))
            all_teams.append(pd.read_csv(test / "team_predictions.csv"))
        parts, teams = pd.concat(all_parts, ignore_index=True), pd.concat(all_teams, ignore_index=True)
        if parts["observation_id"].duplicated().any():
            raise ValueError("A held-out observation was scored in multiple folds")
        pooled.append({"arm": arm, "folds": len(config["folds"]),
                       "parts": len(parts), "responses": len(teams),
                       "games": teams["game_id"].nunique(), "teams": teams["team_id"].nunique(),
                       **bonus_metrics(parts, teams)})
    output = Path(config["root"]) / "aggregate"
    output.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows)
    frame.to_csv(output / "per_fold.csv", index=False)
    pd.DataFrame(pooled).to_csv(output / "pooled.csv", index=False)
    numeric = frame.select_dtypes("number").columns.drop("fold")
    frame.groupby("arm")[numeric].agg(["mean", "std"]).to_csv(output / "fold_mean_std.csv")
    write_json(output / "pooled.json", pooled)
    lines = ["# Compositional bonuses from frozen Stage-1 folds", "",
             f"Source: `{config['stage1_root']}`.", "",
             f"{config['steps']} SVI steps, learning rate {config['lr']}, seed {config['seed']}; "
             f"bonus discrimination prior `{config['alpha_prior']}`. Skills are fixed at the saved Stage-1 medians. "
             "Synergy uses one latent coordinate per player.", "",
             "All bonus parameters are fit on training games and frozen for held-out replay. "
             "The source Stage-1 fits are reused without refitting. Coverage requires familiar players and parts; "
             "lineups are inferred from the observed game buzzes. These are matrix-infill results, "
             "not cold-start or recombined-team validation.", "",
             "Pooled PPB MAE averages each team's observed and predicted points across all its held-out bonuses, "
             "then averages absolute errors equally across teams. Exact accuracy requires all three part labels to match.", "",
             "| Model | Part AUC | Part log loss | Part accuracy | Brier | ECE | Exact accuracy | PPB MAE |",
             "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for row in pooled:
        names = ("auc", "log_loss", "part_accuracy", "brier", "ece", "exact_acc", "ppb_mae")
        lines.append(f"| {row['arm']} | " + " | ".join(f"{row[k]:.4f}" for k in names) + " |")
    lines += ["", f"Scored {pooled[0]['parts']:,} parts / {pooled[0]['responses']:,} bonuses / "
              f"{pooled[0]['games']:,} games / {pooled[0]['teams']:,} teams in {pooled[0]['folds']} folds.", "",
              "See `per_fold.csv` and `fold_mean_std.csv` for fold variation; one optimization seed was used. "
              "All folds passed checks for disjoint training/test games, unique complete bonus responses, "
              "finite losses and probabilities, and zero uncovered roster rows."]
    (output / "report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines), flush=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage1-root", type=Path)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--folds", nargs="+", type=int, default=list(range(5)))
    parser.add_argument("--arms", nargs="+", choices=ARMS, default=list(ARMS))
    parser.add_argument("--steps", type=int, default=2000)
    parser.add_argument("--lr", type=float, default=0.01)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--alpha-prior", choices=("normal", "gamma"), default="gamma")
    parser.add_argument("--device", choices=("cpu", "cuda"), default="cuda")
    parser.add_argument("--data-dir", type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--collect-only", action="store_true")
    parser.add_argument("--evaluate-only", action="store_true",
                        help="refresh saved predictions' graphs, metrics and reports without fitting or replay")
    parser.add_argument("--prepare-only", action="store_true",
                        help="validate sources and save the configuration without fitting")
    parser.add_argument("--worker-fold", type=int,
                        help="run one configured fold without aggregating shared outputs")
    parser.add_argument("--worker-arm", choices=ARMS)
    parser.add_argument("--worker-stage", choices=("train", "replay", "evaluate"))
    args = parser.parse_args(argv)
    if args.evaluate_only or args.collect_only:
        if (args.evaluate_only and args.collect_only) or args.dry_run or args.prepare_only or any(
            value is not None for value in (args.worker_fold, args.worker_arm, args.worker_stage)
        ):
            parser.error("evaluate-only and collect-only cannot be combined with other execution modes")
        manifest = args.root / "configuration.json"
        config = json.loads(manifest.read_text())
        if Path(config["root"]).resolve() != args.root.resolve():
            raise ValueError(f"Saved root differs from --root: {manifest}")
        if args.stage1_root is not None and args.stage1_root.resolve() != Path(config["stage1_root"]).resolve():
            raise ValueError("--stage1-root differs from the saved configuration")
        for fold in config["folds"]:
            if source_fold(Path(config["stage1_root"]), fold) != config["sources"][str(fold)]:
                raise ValueError(f"Source artifacts changed for fold {fold}; cannot refresh this evaluation")
        if args.evaluate_only:
            for fold in config["folds"]:
                for arm in config["arms"]:
                    run_arm(config, fold, arm, only_stage="evaluate")
        aggregate(config)
        return
    if args.stage1_root is None:
        parser.error("--stage1-root is required for training")
    args.root = Path(resolve_result_root(args.root, "holdout"))
    if args.steps < 1 or not math.isfinite(args.lr) or args.lr <= 0:
        parser.error("steps and learning rate must be positive and finite")
    if len(set(args.folds)) != len(args.folds) or len(set(args.arms)) != len(args.arms):
        parser.error("duplicate folds or arms are not allowed")
    if args.collect_only and args.dry_run:
        parser.error("--collect-only and --dry-run are mutually exclusive")
    worker = args.worker_fold is not None
    if worker and args.worker_fold not in args.folds:
        parser.error("--worker-fold must belong to --folds")
    if args.worker_arm is not None and (not worker or args.worker_arm not in args.arms):
        parser.error("--worker-arm requires a worker fold and must belong to --arms")
    if args.worker_stage is not None and args.worker_arm is None:
        parser.error("--worker-stage requires --worker-arm")
    if (worker and (args.collect_only or args.prepare_only)) or (
        args.prepare_only and (args.collect_only or args.dry_run)
    ):
        parser.error("worker, prepare-only, and collect-only modes cannot be combined")
    config = {k: (str(v.resolve()) if isinstance(v, Path) else v)
              for k, v in vars(args).items() if k not in (
                  "dry_run", "collect_only", "evaluate_only", "prepare_only", "worker_fold",
                  "worker_arm", "worker_stage",
              )}
    config["sources"] = {str(fold): source_fold(args.stage1_root, fold) for fold in args.folds}
    specs = [parse_game_holdout_split(s["train_split"]) for s in config["sources"].values()]
    if len({(s.base_split, s.n_folds, s.seed) for s in specs}) != 1:
        raise ValueError("Source folds must use the same base split, fold count and split seed")
    config["code_sha256"] = {p: sha256(REPO_ROOT / p) for p in (
        "compositional_model.py", "train_compositional.py", "holdout/frozen_predict.py",
        "compirt_data.py", "lineup.py", "holdout/game_splits.py", "utils/training.py",
        "compirt_eval/scenario_b_bonuses/metrics.py", "compirt_eval/common/metrics.py",
        "run_scripts/common/run_compositional_from_folds.py",
    )}
    manifest = args.root / "configuration.json"
    if manifest.exists():
        if json.loads(manifest.read_text()) != config:
            raise ValueError(f"Resume configuration or source files changed: use a new --root ({manifest})")
    elif not args.dry_run:
        if args.collect_only or worker:
            raise ValueError(f"No saved configuration at {manifest}")
        write_json(manifest, config)
    if args.prepare_only:
        return
    if not args.collect_only:
        for fold in ([args.worker_fold] if worker else args.folds):
            for arm in ([args.worker_arm] if args.worker_arm else args.arms):
                run_arm(config, fold, arm, args.dry_run, args.worker_stage)
    if not args.dry_run and not worker:
        aggregate(config)


if __name__ == "__main__":
    main()
