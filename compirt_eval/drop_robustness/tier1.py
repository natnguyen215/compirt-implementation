"""Evaluate completed Tier-1 random-drop fits without launching training."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from compirt_data import DEFAULT_DATA_DIR
from compirt_eval.common import player_scoring
from compirt_eval.common.ranking_metrics import compare_rankings
from compirt_eval.drop_robustness.layout import (
    cell_dir,
    droplist_path,
    full_dir,
    noise_dir,
)
from compirt_eval.drop_robustness.perturbations import (
    drop_tossup_events,
    load_event_drop_list,
)


def ranking_for(
    args,
    model: str,
    run_dir: Path,
    observations: pd.DataFrame,
    data: dict,
    games: pd.Series,
) -> pd.Series:
    """One family's predicted-PPG ranking from a saved fit."""
    if model == "plain":
        return player_scoring.plain_irt_expected_ppg(run_dir, observations, games)
    link = args.difficulty_link if model == "multidim" else "sigmoid"
    return player_scoring.predicted_ppg(run_dir, data, games, model, link)


def _training_summary(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    summary = json.loads(path.read_text(encoding="utf-8"))
    return {
        "train_final_loss": summary.get("final_loss"),
        "train_steps": summary.get("steps"),
    }


def collect_results(args) -> pd.DataFrame:
    """Score every completed fit against its own full-data ranking."""
    observations = player_scoring.build_observations(
        args.split, args.tournament, args.data_dir or DEFAULT_DATA_DIR
    )
    _, full_data, full_games = player_scoring.tensors_and_games(observations)
    full_actual = player_scoring.actual_ppg(observations)

    full_rankings = {}
    for model in args.models:
        summary = full_dir(args.root, model) / "summary.json"
        if not summary.exists():
            print(f"skip collect for {model}: no full fit yet", flush=True)
            continue
        full_rankings[model] = ranking_for(
            args, model, full_dir(args.root, model), observations, full_data, full_games
        )

    rows = []
    for model, full_ppg in full_rankings.items():
        for seed in args.noise_seeds:
            run_dir = noise_dir(args.root, model, seed)
            if not (run_dir / "summary.json").exists():
                continue
            ppg = ranking_for(args, model, run_dir, observations, full_data, full_games)
            rows.append(
                {
                    "model": model,
                    "fraction": 0.0,
                    "rep": f"seed_{seed}",
                    "n_events_dropped": 0,
                    **compare_rankings(full_ppg, ppg),
                    **_training_summary(run_dir / "summary.json"),
                }
            )

    for fraction in args.fractions:
        for replicate in range(1, args.replicates + 1):
            list_path = droplist_path(args.root, fraction, replicate)
            if not list_path.exists():
                continue
            drop_ids = load_event_drop_list(list_path)
            dropped_obs, _ = drop_tossup_events(observations, drop_ids)
            _, dropped_data, dropped_games = player_scoring.tensors_and_games(dropped_obs)
            rows.append(
                {
                    "model": "actual",
                    "fraction": fraction,
                    "rep": str(replicate),
                    "n_events_dropped": len(drop_ids),
                    **compare_rankings(
                        full_actual, player_scoring.actual_ppg(dropped_obs)
                    ),
                }
            )
            for model, full_ppg in full_rankings.items():
                run_dir = cell_dir(args.root, model, fraction, replicate)
                if not (run_dir / "summary.json").exists():
                    continue
                ppg = ranking_for(
                    args, model, run_dir, dropped_obs, dropped_data, dropped_games
                )
                rows.append(
                    {
                        "model": model,
                        "fraction": fraction,
                        "rep": str(replicate),
                        "n_events_dropped": len(drop_ids),
                        **compare_rankings(full_ppg, ppg),
                        **_training_summary(run_dir / "summary.json"),
                    }
                )
    return pd.DataFrame(rows)
