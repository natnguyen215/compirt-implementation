#!/usr/bin/env python3
"""Reevaluate a Research Log model manifest with the shared tossup replay.

Write per-fold audit CSVs, fold-mean scoring metrics, pooled tournament PPG,
and pooled round summaries. Uses saved fits without training or selection.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ProcessPoolExecutor, as_completed
import hashlib
import json
from pathlib import Path
import re
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pandas as pd

from compirt_eval.scenario_a_tossups.outcomes import (
    OUTCOME_SCHEMA_VERSION, REPLAY_SEED, evaluate_tossup_outcomes,
    player_leaderboards, round_metrics,
)


def slug(label):
    return re.sub(r"[^a-z0-9]+", "-", label.lower()).strip("-")


def source_signature(results):
    paths = [results / name for name in ("players.csv", "tossups.csv", "tossup_predictions.csv", "summary.json")]
    code = [ROOT / "compirt_eval/scenario_a_tossups" / name
            for name in ("outcomes.py", "reconstruction.py", "parameters.py")]
    return {
        "inputs": {str(p): [p.stat().st_size, p.stat().st_mtime_ns] for p in paths},
        "code": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in code},
        "schema": OUTCOME_SCHEMA_VERSION, "seed": REPLAY_SEED,
    }


def evaluate_fold(task):
    model, fold, source, destination = task
    source, destination = Path(source), Path(destination)
    signature = source_signature(source)
    stamp = destination / "complete.json"
    if stamp.exists() and json.loads(stamp.read_text()).get("signature") == signature:
        summary = pd.read_csv(destination / "csvs/tossup_outcome_metrics.csv").iloc[0].to_dict()
        return {"model": model, "fold": fold, **summary}
    started = time.monotonic()
    summary, events, _players, games, _leaderboard = evaluate_tossup_outcomes(source, destination)
    if not summary or events.empty or games.empty:
        raise ValueError(f"No complete replayed games for {model}, fold {fold}: {summary}")
    stamp.write_text(json.dumps({"signature": signature, "elapsed_seconds": time.monotonic() - started}, indent=2) + "\n")
    return {"model": model, "fold": fold, **summary}


def write_replay_diagnostics(output_dir, models):
    """Explain threshold replay behavior and summarize rounds from game rows."""
    rows = []
    for model in models:
        directory = output_dir / slug(model["model"])
        events = pd.concat([
            pd.read_csv(directory / f"fold_{fold}/csvs/tossup_outcome_predictions.csv")
            for fold in range(5)
        ], ignore_index=True)
        games = pd.read_csv(directory / "pooled_game_predictions.csv")
        rounds = pd.read_csv(directory / "pooled_round_metrics.csv")
        ranks = pd.read_csv(directory / "pooled_player_ranking_metrics.csv")
        teams = pd.concat([
            pd.DataFrame({
                "tournament_id": games.tournament_id, "round": games["round"],
                "actual": games[f"actual_team_{side}_tossup_points"],
                "predicted": games[f"predicted_team_{side}_tossup_points"],
            })
            for side in (1, 2)
        ], ignore_index=True)
        teams["error"] = (teams.predicted - teams.actual).abs()
        rows.append({
            "model": model["model"],
            "replay_no_buzz_rate": events.predicted_no_buzz.mean(),
            "actual_no_buzz_rate": events.actual_first_player_id.eq("no_buzz").mean(),
            "replay_no_score_rate": events.predicted_no_score.mean(),
            "replay_tied_game_rate": games.predicted_tossup_winner.eq("tie").mean(),
            "replay_zero_zero_game_rate": (
                games.predicted_team_1_tossup_points.eq(0)
                & games.predicted_team_2_tossup_points.eq(0)
            ).mean(),
            "team_points_mae": teams.error.mean(),
            "round_macro_team_points_mae": teams.groupby(["tournament_id", "round"]).error.mean().mean(),
            "mean_replayed_team_points": teams.predicted.mean(),
            "mean_recorded_team_points": teams.actual.mean(),
            "zero_team_points_mae": teams.actual.abs().mean(),
            "round_macro_winner_accuracy": rounds.tossup_game_winner_accuracy.mean(),
            "round_macro_margin_mae": rounds.tossup_game_margin_mae.mean(),
            "rounds": len(rounds),
            "ppg_spearman_tournaments": ranks.ppg_spearman.notna().sum(),
            "rounds_with_decisive_games": rounds.tossup_game_winner_accuracy.notna().sum(),
        })
    pd.DataFrame(rows).to_csv(output_dir / "replay_diagnostics.csv", index=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=5)
    args = parser.parse_args()
    models = json.loads(args.manifest.read_text())
    tasks = []
    for model in models:
        sources = sorted((ROOT / model["results_dir"]).glob("**/fold_*/holdout/pyramidal/tossup_predictions.csv"))
        if len(sources) != 5:
            raise ValueError(f"Expected five folds for {model['model']}: {len(sources)}")
        for source in sources:
            fold = int(source.parents[2].name.removeprefix("fold_"))
            destination = args.output_dir / slug(model["model"]) / f"fold_{fold}"
            tasks.append((model["model"], fold, str(source.parent), str(destination)))
    rows = []
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(evaluate_fold, task): task for task in tasks}
        for future in as_completed(futures):
            row = future.result()
            rows.append(row)
            print(f"{len(rows)}/{len(tasks)} {row['model']} fold {row['fold']}: "
                  f"{int(row['tossup_outcome_events'])} events, "
                  f"{int(row['tossup_replay_incomplete_games'])} incomplete games", flush=True)
    folds = pd.DataFrame(rows).sort_values(["model", "fold"])
    folds.to_csv(args.output_dir / "fold_metrics.csv", index=False)
    summaries, coverage = [], []
    for model in models:
        label = model["model"]
        directory = args.output_dir / slug(label)
        player_frames, game_frames = [], []
        for fold in range(5):
            csvs = directory / f"fold_{fold}/csvs"
            player_frames.append(pd.read_csv(csvs / "tossup_player_predictions.csv", dtype={"player_id": str, "team_id": str, "game_id": str, "tournament_id": str}))
            game_frames.append(pd.read_csv(csvs / "tossup_game_predictions.csv", dtype={"game_id": str, "tournament_id": str, "round": str}))
        players, games = pd.concat(player_frames, ignore_index=True), pd.concat(game_frames, ignore_index=True)
        if games.duplicated(["tournament_id", "game_id"]).any():
            raise ValueError(f"Overlapping held-out games: {label}")
        leaderboard, ranks = player_leaderboards(players)
        leaderboard.to_csv(directory / "pooled_player_ppg_leaderboard.csv", index=False)
        ranks.to_csv(directory / "pooled_player_ranking_metrics.csv", index=False)
        rounds = round_metrics(games)
        rounds.to_csv(directory / "pooled_round_metrics.csv", index=False)
        games.to_csv(directory / "pooled_game_predictions.csv", index=False)
        subset = folds[folds.model == label].drop(columns=["model", "fold"])
        summary = {"model": label, **subset.mean(numeric_only=True).to_dict()}
        for metric, column in (
            ("spearman", "ppg_spearman"), ("mae", "ppg_mae"),
            ("top10_overlap", "top10_overlap_rate"),
            ("top10_random_overlap", "top10_random_overlap_rate"),
            ("top10_adjusted_overlap", "top10_adjusted_overlap_rate"),
        ):
            summary[f"tournament_player_ppg_{metric}"] = ranks[column].mean()
        summary.update(events=int(subset.tossup_outcome_events.sum()), games=len(games),
                       tournaments=len(ranks), tournament_players=len(leaderboard),
                       incomplete_games=int(subset.tossup_replay_incomplete_games.sum()),
                       rounds=len(rounds))
        summaries.append(summary)
        coverage.extend({"model": label, "tournament_id": row.tournament_id, "game_id": row.game_id}
                        for row in games.itertuples(index=False))
    pd.DataFrame(summaries).to_csv(args.output_dir / "model_metrics.csv", index=False)
    pd.DataFrame(coverage).to_csv(args.output_dir / "game_coverage.csv", index=False)
    write_replay_diagnostics(args.output_dir, models)
    print(f"Wrote {args.output_dir / 'model_metrics.csv'}", flush=True)


if __name__ == "__main__":
    main()
