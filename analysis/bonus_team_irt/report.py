"""Existing bonus metrics and question strata on matched whole-game folds."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

import pandas as pd
from compirt_eval.common.categories import top_level_category
from compirt_eval.common.metrics import classification_metrics
from compirt_eval.scenario_b_bonuses.metrics import bonus_metrics
from compirt_eval.scenario_b_bonuses.outcomes import bonus_team_outcomes


def score(parts, tables, games):
    responses = parts.groupby("response_id", as_index=False).agg(
        team_id=("team_id", "first"), total_points=("total_points", "first"),
        predicted_points=("predicted_correct", "sum"),
    )
    responses.predicted_points *= 10
    metrics = bonus_metrics(parts, responses)
    outcomes, team_games, leaderboard, tournaments, margins = bonus_team_outcomes(
        parts, games, tables["bonus_responses"])
    return {"parts": len(parts), "responses": len(responses), **metrics, **outcomes}, (
        team_games, leaderboard, tournaments, margins)


def stratify(parts, model):
    rows = []
    for columns in (("category_group",), ("difficulty",), ("category_group", "difficulty")):
        for key, group in parts.groupby(list(columns), sort=True):
            values = key if isinstance(key, tuple) else (key,)
            rows.append({
                "model": model, "stratum": " x ".join(columns),
                **dict(zip(columns, values)), "parts": len(group),
                "responses": group.response_id.nunique(), "games": group.game_id.nunique(),
                "teams": group.team_id.nunique(),
                **classification_metrics(group.correct, group.predicted_correct),
            })
    return pd.DataFrame(rows)


def markdown_table(frame, columns, digits=4):
    rows = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for record in frame[columns].itertuples(index=False, name=None):
        rows.append("| " + " | ".join(f"{value:.{digits}f}" if isinstance(value, float) else str(value) for value in record) + " |")
    return "\n".join(rows)


def evaluate(root, args, tables, selected_games):
    output = root / "aggregate"
    output.mkdir(exist_ok=True)
    models = [*[f"team_irt_{dimension}d" for dimension in args.dimensions],
              "dd_compositional", "dd_synergy", "multidim_compositional", "multidim_synergy"]
    summaries, byfold, strata = [], [], []
    scored_observations = None
    all_games = []
    for fold in args.folds:
        split = json.loads((root / f"fold_{fold}" / "split.json").read_text())
        games = selected_games[selected_games.game_id.isin(split["scored_game_ids"])].copy()
        games["fold"] = fold
        all_games.append(games)
    games = pd.concat(all_games, ignore_index=True)
    for model in models:
        pieces = []
        for fold in args.folds:
            parts = pd.read_csv(root / f"fold_{fold}" / model / "bonus_part_predictions.csv")
            parts["fold"] = fold
            fold_games = games[games.fold == fold]
            metrics, _ = score(parts, tables, fold_games)
            byfold.append({"model": model, "fold": fold, **metrics})
            pieces.append(parts)
        parts = pd.concat(pieces, ignore_index=True).sort_values("observation_id").reset_index(drop=True)
        if parts.observation_id.duplicated().any():
            raise ValueError("Duplicate pooled predictions")
        observations = parts[["observation_id", "correct"]]
        if scored_observations is not None and not observations.equals(scored_observations):
            raise ValueError("Models do not share identical scored observations")
        scored_observations = observations
        parts["category_group"] = parts.category.map(top_level_category)
        metrics, artifacts = score(parts, tables, games)
        if metrics["bonus_ppg_incomplete_games"]:
            raise ValueError("Matched evaluation must contain only complete games")
        summaries.append({"model": model, **metrics})
        destination = output / model
        destination.mkdir(exist_ok=True)
        for filename, artifact in zip(("team_game_predictions", "team_ppg", "tournament_metrics", "game_margins"), artifacts):
            artifact.to_csv(destination / f"{filename}.csv", index=False)
        strata.append(stratify(parts, model))
    summary = pd.DataFrame(summaries)
    strata = pd.concat(strata, ignore_index=True)
    summary.to_csv(output / "metrics.csv", index=False)
    pd.DataFrame(byfold).to_csv(output / "metrics_by_fold.csv", index=False)
    strata.to_csv(output / "metrics_by_question_type.csv", index=False)
    exclusions = pd.concat([pd.read_csv(root / f"fold_{fold}" / "excluded_games.csv").assign(fold=fold) for fold in args.folds])
    exclusions.to_csv(output / "excluded_games.csv", index=False)
    write_report(root, args)
    print(summary[["model", "log_loss", "part_accuracy", "ppb_mae", "bonus_game_margin_mae"]].to_string(index=False), flush=True)


def write_report(root, args):
    """Render cached scores in the existing compositional-report layout."""
    output = root / "aggregate"
    summary = pd.read_csv(output / "metrics.csv")
    strata = pd.read_csv(output / "metrics_by_question_type.csv")
    exclusions = pd.read_csv(output / "excluded_games.csv")
    labels = {
        "model": "Model", "auc": "Part AUC", "log_loss": "Part log loss",
        "part_accuracy": "Part accuracy", "accuracy": "Part accuracy", "brier": "Brier",
        "ece": "ECE", "exact_acc": "Exact accuracy", "ppb_mae": "PPB MAE",
        "part_accuracy_easy": "Easy acc.", "part_accuracy_medium": "Medium acc.",
        "part_accuracy_hard": "Hard acc.", "tournament_team_bonus_ppg_mae": "PPG MAE",
        "tournament_team_bonus_ppg_spearman": "PPG Spearman", "bonus_game_margin_mae": "Margin MAE",
        "category_group": "Category", "parts": "Parts",
    }
    display = summary.rename(columns=labels)
    text = [
        "# Bonus-only team IRT", "",
        f"{args.steps:,} AutoNormal SVI steps, learning rate {args.lr}, fit seed {args.seed}; "
        f"{args.n_folds} {args.split} whole-game folds, split seed {args.split_seed}.", "",
        "Team parameters use tournament-specific team IDs. "
        "P(correct) = sigmoid(theta_team dot alpha_part - beta_part), with independent "
        "theta ~ Normal(0,1), alpha ~ Gamma(2,2) (shape/rate), beta ~ Normal(0,1). "
        "Both team and part parameters are learned only from training bonuses and frozen at posterior medians.", "",
        f"All arms score the same {int(summary.iloc[0].bonus_ppg_games):,} games and {int(summary.iloc[0].parts):,} parts. "
        f"{len(exclusions):,} whole games were excluded for missing training entity coverage or saved predictions. "
        "See excluded_games.csv and fold split manifests. Zero-bonus games remain in the game denominator.", "",
        "Saved DD and multidimensional compositional arms are reused without refitting. "
        "Training summaries and prediction hashes are recorded in ../configuration.json; "
        "their optimization budgets and player-skill sources differ from this bonus-only study.", "",
        "## Overall", "",
        markdown_table(display, ["Model", "Part AUC", "Part log loss", "Part accuracy", "Brier", "ECE", "Exact accuracy", "PPB MAE"]), "",
        "## Difficulty, bonus-only team PPG and game margins", "",
        "Bonus margins condition on recorded bonus opportunities and use expected points (10 * sum probabilities). "
        "They exclude tossup points. Team PPB and PPG pool held-out predictions across folds before scoring. "
        "Tournament PPG summaries weight tournaments equally; margin MAE weights games equally.", "",
        markdown_table(display, ["Model", "Easy acc.", "Medium acc.", "Hard acc.", "PPG MAE", "PPG Spearman", "Margin MAE"]), "",
        "Difficulty accuracy includes correctly predicted misses; declared-label counts and observed conversion "
        "rates are in metrics_by_question_type.csv. Each difficulty gives one vote per observed part.", "",
        "## Subject category", "",
        markdown_table(strata[strata.stratum == "category_group"].rename(columns=labels),
                       ["Model", "Category", "Parts", "Part accuracy", "Part AUC", "Part log loss"]), "",
        "Category x difficulty results, counts, conversion rates, AUC and calibration diagnostics "
        "are in metrics_by_question_type.csv. Missing/unmapped categories remain Unknown. "
        "Difficulty is joined from source labels, never inferred from part position.", "",
        "These are reused development folds with familiar teams and questions, not an untouched test or "
        "a new-team/new-question transfer estimate. Team vectors ignore lineup changes; "
        "latent dimensions are not identified subject traits. One optimization seed was used. "
        "Loss traces and variational marginal quantiles are saved per fit; probabilities use parameter medians, "
        "not posterior-predictive integration.", "",
    ]
    (output / "report.md").write_text("\n".join(text), encoding="utf-8")
    manifest = {"report_source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "input_sha256": {name: hashlib.sha256((output / name).read_bytes()).hexdigest()
                                 for name in ("metrics.csv", "metrics_by_question_type.csv", "excluded_games.csv")}}
    (output / "report_rendering.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Refresh the report from saved metric CSVs without scoring or fitting")
    parser.add_argument("--output-dir", required=True, type=Path)
    arguments = parser.parse_args()
    configuration = json.loads((arguments.output_dir / "configuration.json").read_text())
    write_report(arguments.output_dir, SimpleNamespace(**configuration))
