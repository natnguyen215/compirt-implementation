"""Audit, evaluate, and pool saved compositional bonus folds.

These functions read the fits and frozen replays written by
run_scripts/common/run_compositional_from_folds.py, check each fold for
leakage and completeness, score it, and pool held-out predictions across folds.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from compirt_data import DEFAULT_DATA_DIR, load_hf_tables
from compirt_eval.common.bonus_reports import evaluation_dir, write_bonus_fold_reports
from compirt_eval.scenario_b_bonuses.evaluation import evaluate_bonuses
from compirt_eval.scenario_b_bonuses.metrics import bonus_metrics, bonus_parts_with_difficulty
from compirt_eval.scenario_b_bonuses.outcomes import write_bonus_outcomes
from holdout.game_splits import parse_game_holdout_split, select_game_holdout_tables


def evaluation_tables(config, folds):
    """Select the union of evaluated folds, including games with zero bonuses."""
    specs = [parse_game_holdout_split(config["sources"][str(fold)]["test_split"]) for fold in folds]
    tables = load_hf_tables(config.get("data_dir") or DEFAULT_DATA_DIR, specs[0].base_split)
    selected = pd.concat([select_game_holdout_tables(tables, spec)["games"] for spec in specs])
    if selected["game_id"].duplicated().any():
        raise ValueError("Evaluation folds overlap in games")
    tables["games"] = selected
    return tables


def audit_predictions(train_parts, test_parts, stage1_games):
    """Check one fold's predictions and return its audit counts.

    Raises ValueError when held-out games reach either training stage, when
    probabilities are invalid, or when a bonus response lacks any of its three parts.
    """
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


def evaluate_fold(config, fold, arm):
    """Audit and score one fold's saved fit and frozen replay for one arm.

    Writes the fold's evaluation directory and '<arm>_checks.json'.
    """
    run = Path(config["root"]) / f"fold_{fold}"
    train, test = run / "train" / arm, run / "holdout" / arm
    train_parts = pd.read_csv(train / "bonus_part_predictions.csv")
    test_parts = pd.read_csv(test / "bonus_part_predictions.csv")
    source = Path(config["sources"][str(fold)]["path"])
    stage1_games = pd.read_csv(source / "tossup_predictions.csv", usecols=["game_id"])["game_id"]
    audit = audit_predictions(train_parts, test_parts, stage1_games)
    # Every roster member must have a Stage-1 skill in both the fit and the replay.
    for name, directory in (("train", train), ("test", test)):
        summary = json.loads((directory / "summary.json").read_text())
        audit[f"{name}_dropped_rows_unknown_roster"] = summary.get("dropped_rows_unknown_roster", 0)
        if audit[f"{name}_dropped_rows_unknown_roster"]:
            raise ValueError(f"Uncovered players in {directory}")
    summary = json.loads((train / "summary.json").read_text())
    if not summary["finite_losses"]:
        raise ValueError(f"Nonfinite training losses in {train}")
    metrics = evaluate_bonuses(
        test, evaluation_dir(run, arm), tables=evaluation_tables(config, [fold]), write_report=True
    )
    (run / f"{arm}_checks.json").write_text(json.dumps(audit, indent=2) + "\n")
    print(f"Fold {fold} {arm}: AUC={metrics['auc']:.4f}, "
          f"log loss={metrics['log_loss']:.4f}, PPB MAE={metrics['ppb_mae']:.4f}", flush=True)


def aggregate(config):
    """Pool held-out predictions across folds and write the aggregate artifacts.

    'pooled.csv' scores the concatenated predictions of every fold.
    'per_fold.csv' keeps each fold's own metrics, audit, and training loss
    summary, and 'fold_mean_std.csv' summarizes their spread by arm.
    """
    rows, pooled = [], []
    tables = evaluation_tables(config, config["folds"])
    output = Path(config["root"]) / "aggregate"
    output.mkdir(parents=True, exist_ok=True)
    for arm in config["arms"]:
        all_parts, all_teams = [], []
        for fold in config["folds"]:
            run = Path(config["root"]) / f"fold_{fold}"
            test = run / "holdout" / arm
            checks = json.loads((run / f"{arm}_checks.json").read_text())
            metrics = pd.read_csv(evaluation_dir(run, arm) / "csvs" / "bonus_metrics.csv").iloc[0].to_dict()
            summary = json.loads((run / "train" / arm / "summary.json").read_text())
            losses = {k: summary[k] for k in ("tau", "final_loss", "best_loss", "last_100_loss_slope", "finite_losses")}
            rows.append({"fold": fold, "arm": arm, **metrics, **checks, **losses})
            all_parts.append(pd.read_csv(test / "bonus_part_predictions.csv"))
            all_teams.append(pd.read_csv(test / "team_predictions.csv"))
        parts, teams = pd.concat(all_parts, ignore_index=True), pd.concat(all_teams, ignore_index=True)
        parts = bonus_parts_with_difficulty(parts, tables["bonuses"])
        if parts["observation_id"].duplicated().any():
            raise ValueError("A held-out observation was scored in multiple folds")
        # Pooled scores are computed once from every fold's predictions.
        pooled.append({"arm": arm, "folds": len(config["folds"]),
                       "parts": len(parts), "responses": len(teams),
                       "games": teams["game_id"].nunique(), "teams": teams["team_id"].nunique(),
                       **bonus_metrics(parts, teams),
                       **write_bonus_outcomes(parts, tables, output / arm)})
    frame = pd.DataFrame(rows)
    frame.to_csv(output / "per_fold.csv", index=False)
    pd.DataFrame(pooled).to_csv(output / "pooled.csv", index=False)
    numeric = frame.select_dtypes("number").columns.drop("fold")
    frame.groupby("arm")[numeric].agg(["mean", "std"]).to_csv(output / "fold_mean_std.csv")
    (output / "pooled.json").write_text(json.dumps(pooled, indent=2) + "\n")
    write_bonus_fold_reports(config, pooled)
    print(f"Pooled bonus results: {output / 'report.md'}", flush=True)
