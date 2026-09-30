"""Rescore Team IRT arms on this comparison's matched games; nothing is refit.

Replaces the Team IRT rows of aggregate/metrics*.csv and aggregate/team_irt_*d/,
and prints the in-sample scores (training predictions, teams keyed by fold) used
in RESEARCH_LOG_2.md. `--check` instead recomputes the held-out rows and
compares them with the saved CSVs without writing. Run from the repository root:

    .venv/bin/python -B results/compirt/comparisons/bonuses/dd-bernstein-and-team-irt-5fold/code/rescore_team_irt.py \
        --team-root results/compirt/holdout/common/bonus-team-irt/<run> [--check]
"""

import argparse
import ast
import json
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[6]))

import numpy as np
import pandas as pd

from analysis.bonus_team_irt.report import score, stratify
from compirt_data import load_hf_tables
from compirt_eval.common.categories import top_level_category
from compirt_eval.common.metrics import classification_metrics
from compirt_eval.scenario_b_bonuses.metrics import bonus_metrics

COMPARISON = Path(__file__).resolve().parents[1]
ROSTER_SOURCE = Path("results/compirt/holdout/double-difficulty/compositional/no-synergy-and-dot-additive-1d")
MODELS = ("team_irt_1d", "team_irt_3d")
FOLDS = range(5)


def roster_groups(fold):
    """Familiar when the exact team + active roster appeared in training bonuses."""
    def keys(frame):
        return list(zip(frame.team_id, frame.player_ids.map(lambda v: frozenset(ast.literal_eval(v)))))
    train = pd.read_csv(ROSTER_SOURCE / f"fold_{fold}/train/compositional/bonus_part_predictions.csv")
    test = pd.read_csv(ROSTER_SOURCE / f"fold_{fold}/holdout/compositional/bonus_part_predictions.csv")
    seen = set(keys(train))
    test["roster_group"] = ["Familiar roster" if key in seen else "New roster" for key in keys(test)]
    return test.drop_duplicates("response_id").set_index("response_id").roster_group


def normalized_inversions(team_ppg):
    rates = []
    for _, group in team_ppg.groupby("tournament_id"):
        observed, predicted = group.observed_bonus_ppg.to_numpy(), group.predicted_bonus_ppg.to_numpy()
        pairs = list(combinations(range(len(group)), 2))
        rates.append(np.mean([(observed[i] - observed[j]) * (predicted[i] - predicted[j]) < 0 for i, j in pairs]))
    return float(np.mean(rates))


def minority_prf(parts):
    rows = {}
    for level, positive in (("easy", 0), ("medium", 1), ("hard", 1)):
        group = parts[parts.difficulty == level]
        predicted = (group.predicted_correct >= 0.5).astype(int) == positive
        actual = group.correct.astype(int) == positive
        tp, fp, fn = (predicted & actual).sum(), (predicted & ~actual).sum(), (~predicted & actual).sum()
        rows[level] = (tp / (tp + fp), tp / (tp + fn), 2 * tp / (2 * tp + fp + fn))
    return rows


def in_sample(team_root, model):
    """Pool the five training folds; each game appears in four, teams keyed by fold."""
    pieces = []
    for fold in FOLDS:
        parts = pd.read_csv(team_root / f"fold_{fold}/{model}/train_bonus_part_predictions.csv")
        parts["team_id"], parts["response_id"] = f"{fold}::" + parts.team_id, f"{fold}::" + parts.response_id
        pieces.append(parts)
    parts = pd.concat(pieces, ignore_index=True)
    responses = parts.groupby("response_id", as_index=False).agg(
        team_id=("team_id", "first"), total_points=("total_points", "first"),
        predicted_points=("predicted_correct", "sum"))
    responses.predicted_points *= 10
    metrics = bonus_metrics(parts, responses)
    return {"parts": len(parts), **{key: round(float(metrics[key]), 5)
                                   for key in ("auc", "log_loss", "part_accuracy", "exact_acc", "ppb_mae")}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--team-root", required=True, type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    tables = load_hf_tables(split="year_2024")
    games, fold_rows, strata, extras = [], [], [], {}
    for fold in FOLDS:
        split = json.loads((COMPARISON / f"fold_{fold}/split.json").read_text())
        games.append(tables["games"][tables["games"].game_id.isin(split["scored_game_ids"])].assign(fold=fold))
    games = pd.concat(games, ignore_index=True)
    summaries = []
    for model in MODELS:
        pieces = []
        for fold in FOLDS:
            parts = pd.read_csv(args.team_root / f"fold_{fold}/{model}/bonus_part_predictions.csv")
            parts = parts[parts.game_id.isin(games.loc[games.fold == fold, "game_id"])].copy()
            parts["roster_group"] = parts.response_id.map(roster_groups(fold))
            if parts.roster_group.isna().any():
                raise ValueError("Missing roster group")
            metrics, _ = score(parts, tables, games[games.fold == fold])
            fold_rows.append({"model": model, "fold": fold, **metrics})
            pieces.append(parts)
        parts = pd.concat(pieces, ignore_index=True).sort_values("observation_id").reset_index(drop=True)
        parts["category_group"] = parts.category.map(top_level_category)
        metrics, artifacts = score(parts, tables, games)
        summaries.append({"model": model, **metrics})
        rosters = [{"model": model, "stratum": "roster_group", "roster_group": key, "parts": len(group),
                    "responses": group.response_id.nunique(), "games": group.game_id.nunique(),
                    "teams": group.team_id.nunique(), **classification_metrics(group.correct, group.predicted_correct)}
                   for key, group in parts.groupby("roster_group")]
        strata += [stratify(parts, model), pd.DataFrame(rosters)]
        extras[model] = {"normalized_inversions": normalized_inversions(artifacts[1]),
                         "minority_prf": minority_prf(parts),
                         "artifacts": artifacts}
    summary, byfold, strata = pd.DataFrame(summaries), pd.DataFrame(fold_rows), pd.concat(strata, ignore_index=True)
    aggregate = COMPARISON / "aggregate"
    saved = {name: pd.read_csv(aggregate / name) for name in
             ("metrics.csv", "metrics_by_fold.csv", "metrics_by_question_type.csv")}
    new = {"metrics.csv": summary, "metrics_by_fold.csv": byfold, "metrics_by_question_type.csv": strata}
    if args.check:
        for name, frame in new.items():
            old = saved[name][saved[name].model.isin(MODELS)].reset_index(drop=True)
            frame = frame[old.columns].reset_index(drop=True)
            numeric = old.select_dtypes("number").columns
            gap = np.nanmax(np.abs(old[numeric].to_numpy(float) - frame[numeric].to_numpy(float)))
            same_keys = old.drop(columns=numeric).fillna("").equals(frame.drop(columns=numeric).fillna(""))
            print(f"{name}: rows {len(old)} vs {len(frame)}, keys equal={same_keys}, max abs diff={gap:.2e}")
    else:
        for name, frame in new.items():
            keep = saved[name][~saved[name].model.isin(MODELS)]
            pd.concat([keep, frame[saved[name].columns]], ignore_index=True).to_csv(aggregate / name, index=False)
        for model in MODELS:
            destination = aggregate / model
            for filename, artifact in zip(("team_game_predictions", "team_ppg", "tournament_metrics", "game_margins"),
                                          extras[model]["artifacts"]):
                artifact.to_csv(destination / f"{filename}.csv", index=False)
    for model in MODELS:
        row = summary.set_index("model").loc[model]
        print(model, {key: round(float(row[key]), 5) for key in
                      ("auc", "log_loss", "part_accuracy", "exact_acc", "ppb_mae", "part_accuracy_easy",
                       "part_accuracy_medium", "part_accuracy_hard", "tournament_team_bonus_ppg_mae",
                       "tournament_team_bonus_ppg_spearman", "bonus_game_margin_mae")},
              "inversions", round(extras[model]["normalized_inversions"], 4),
              {k: tuple(round(float(x), 4) for x in v) for k, v in extras[model]["minority_prf"].items()})
        rosters = strata[(strata.model == model) & (strata.stratum == "roster_group")].set_index("roster_group")
        print("   ", {k: (round(v.auc, 5), round(v.log_loss, 5), round(v.accuracy, 4)) for k, v in rosters.iterrows()})
        if (args.team_root / f"fold_0/{model}/train_bonus_part_predictions.csv").exists():
            print("    in-sample", in_sample(args.team_root, model))


if __name__ == "__main__":
    main()
