"""Evaluate completed Tier-2 targeted-drop fits without launching training."""

from __future__ import annotations

import numpy as np
import pandas as pd

from compirt_eval.common import player_scoring
from compirt_eval.common.ranking_metrics import compare_rankings
from compirt_eval.drop_robustness.layout import full_dir, targeted_cell_dir
from compirt_eval.drop_robustness.metrics import pair_gap
from compirt_eval.drop_robustness.perturbations import drop_tossup_events
from compirt_eval.drop_robustness.tier1 import ranking_for


def reference_dirs(args, model: str):
    """Return one full fit and all noise fits, optionally from the Tier-1 root."""
    base = args.reuse_full if args.reuse_full is not None else args.root
    noise_runs = sorted((base / model / "noisefloor").glob("seed_*/pyramidal"))
    return full_dir(base, model), noise_runs


def resolve_pair(args, reference_ppg: pd.Series):
    """Resolve the explicit pair or closest adjacent top-10 pair."""
    ordered = reference_ppg.sort_values(ascending=False)
    if args.target_player:
        target = args.target_player
        if target not in ordered.index:
            raise ValueError(f"--target-player {target} not in the reference ranking")
    elif args.target_rank:
        target = ordered.index[args.target_rank - 1]
    else:
        top = ordered.head(10)
        gaps = top.values[:-1] - top.values[1:]
        target = top.index[int(np.argmin(gaps))]
    if args.rival:
        rival = args.rival
        if rival not in ordered.index:
            raise ValueError(f"--rival {rival} not in the reference ranking")
    else:
        position = ordered.index.get_loc(target)
        if position + 1 >= len(ordered):
            raise ValueError(f"{target} is ranked last; pass --rival explicitly")
        rival = ordered.index[position + 1]
    return target, rival


def collect_results(args, observations, target, rival, ranked, counts):
    """Score pair gaps for every completed refit and the exact raw prefix curve."""
    _, full_data, full_games = player_scoring.tensors_and_games(observations)

    dropped_by_count = {}
    for count in counts:
        dropped_obs, _ = drop_tossup_events(
            observations, ranked["event_id"].head(count).tolist()
        )
        dropped_by_count[count] = player_scoring.tensors_and_games(dropped_obs)

    rows = []
    full_gaps = {}
    noise_stds = {}
    for model in args.models:
        full, noise_runs = reference_dirs(args, model)
        if not (full / "summary.json").exists():
            print(f"skip collect for {model}: no full fit", flush=True)
            continue
        full_ppg = ranking_for(args, model, full, observations, full_data, full_games)
        gap, target_rank, rival_rank = pair_gap(full_ppg, target, rival)
        full_gaps[model] = gap
        noise_gaps = []
        for run_dir in noise_runs:
            if not (run_dir / "summary.json").exists():
                continue
            noise_ppg = ranking_for(
                args, model, run_dir, observations, full_data, full_games
            )
            noise_gap, _, _ = pair_gap(noise_ppg, target, rival)
            if noise_gap is not None:
                noise_gaps.append(noise_gap)
        noise_stds[model] = float(np.std([gap] + noise_gaps)) if noise_gaps else None
        rows.append(
            {
                "model": model,
                "n_dropped": 0,
                "gap": gap,
                "target_rank": target_rank,
                "rival_rank": rival_rank,
                "flipped": False,
                "noise_gap_std": noise_stds[model],
            }
        )
        for count in counts:
            cell = targeted_cell_dir(args.root, model, args.direction, target, count)
            if not (cell / "summary.json").exists():
                continue
            dropped_obs, dropped_data, dropped_games = dropped_by_count[count]
            ppg = ranking_for(args, model, cell, dropped_obs, dropped_data, dropped_games)
            gap, target_rank, rival_rank = pair_gap(ppg, target, rival)
            rows.append(
                {
                    "model": model,
                    "n_dropped": count,
                    "gap": gap,
                    "target_rank": target_rank,
                    "rival_rank": rival_rank,
                    "flipped": gap is not None
                    and full_gaps[model] is not None
                    and (gap < 0) != (full_gaps[model] < 0),
                    "noise_gap_std": noise_stds[model],
                    **compare_rankings(full_ppg, ppg),
                }
            )

    actual_rows = []
    full_actual_gap, _, _ = pair_gap(
        player_scoring.actual_ppg(observations), target, rival
    )
    for n in range(0, len(ranked) + 1):
        if n == 0:
            frame = observations
        else:
            prefix = set(ranked["event_id"].head(n))
            frame = observations[~observations["event_id"].isin(prefix)]
        gap, target_rank, rival_rank = pair_gap(
            player_scoring.actual_ppg(frame), target, rival
        )
        actual_rows.append(
            {
                "n_dropped": n,
                "gap": gap,
                "target_rank": target_rank,
                "rival_rank": rival_rank,
                "flipped": gap is not None
                and full_actual_gap is not None
                and (gap < 0) != (full_actual_gap < 0),
            }
        )
    return pd.DataFrame(rows), pd.DataFrame(actual_rows)


def report_flip_brackets(frame: pd.DataFrame, actual: pd.DataFrame) -> None:
    """Print each method's largest non-flipping and smallest flipping counts."""
    print("\nFlip brackets (dropped-event counts):")
    flips = actual[actual["flipped"]]
    if flips.empty:
        print(f"  actual    no flip within {int(actual['n_dropped'].max())} drops")
    else:
        n = int(flips["n_dropped"].min())
        print(f"  actual    exact minimal flip count = {n}")
    for model, group in frame[frame["n_dropped"] > 0].groupby("model"):
        flipped = group[group["flipped"]]
        held = group[~group["flipped"]]
        largest_held = int(held["n_dropped"].max()) if not held.empty else 0
        if flipped.empty:
            print(f"  {model:<9s} no flip within {int(group['n_dropped'].max())} drops")
        else:
            smallest_flip = int(flipped["n_dropped"].min())
            print(f"  {model:<9s} flip bracket = ({largest_held}, {smallest_flip}]")
