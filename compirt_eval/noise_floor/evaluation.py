"""Analyze SVI seed jitter in the multidim-tanh player ranking.

Predicted PPG is a rotation-invariant expected-scoring quantity, so rankings
can be compared across independently initialized fits. This module reads saved
Stage-1 fits and never launches training.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from compirt_data import DEFAULT_DATA_DIR
from compirt_eval.common import player_scoring
from compirt_eval.noise_floor.metrics import (
    DEFAULT_TOPKS,
    mean_topk_jaccards,
    pairwise_agreement,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_ROOT = (
    REPO_ROOT
    / "results"
    / "compirt"
    / "in_sample"
    / "multidim"
    / "multidim-tanh-all2024-noisefloor"
)
DEFAULT_SPLIT = "year_2024"
DEFAULT_LINK = "tanh"


def discover_seed_dirs(root: Path) -> list[Path]:
    """Find completed seed directories in the historical lexical order."""
    return sorted(
        d for d in root.glob("seed_*") if (d / "pyramidal" / "players.csv").exists()
    )


def build_data(split=DEFAULT_SPLIT, data_dir=DEFAULT_DATA_DIR):
    observations = player_scoring.build_observations(split, None, data_dir)
    _, data, games = player_scoring.tensors_and_games(observations)
    return data, games


def predicted_ppg(seed_dir, data, games, link=DEFAULT_LINK):
    return player_scoring.predicted_ppg(
        Path(seed_dir) / "pyramidal", data, games, "multidim", link
    )


def predicted_ppg_table(seed_dirs, data, games, link=DEFAULT_LINK):
    """Build the historical per-seed table with identical column ordering."""
    ppgs = {
        d.name.replace("seed_", ""): predicted_ppg(d, data, games, link)
        for d in seed_dirs
    }
    out = pd.DataFrame(ppgs)
    out["mean_ppg"] = out.mean(axis=1)
    return out.sort_values("mean_ppg", ascending=False), ppgs


def print_report(ppgs) -> None:
    rankings = {s: v.rank(ascending=False, method="min") for s, v in ppgs.items()}
    seeds = sorted(rankings)
    print(
        f"{'=' * 72}\nNOISE FLOOR: predicted PPG ranking, seeds {', '.join(seeds)}"
        f"\n{'=' * 72}"
    )

    agree = pairwise_agreement(rankings)
    print("\nPairwise rank agreement:")
    print(agree.to_string(index=False))
    print(
        f"\n  mean Kendall tau = {agree['kendall_tau'].mean():.4f}"
        f"   mean Spearman = {agree['spearman'].mean():.4f}"
    )

    print("\nTop-k set stability (mean pairwise Jaccard):")
    for k, value in mean_topk_jaccards(rankings, DEFAULT_TOPKS).items():
        print(f"  top-{k:<3d}  Jaccard = {value:.4f}")
    ones = {r.idxmin() for r in rankings.values()}
    print(f"\n  distinct players ever ranked #1: {len(ones)}  {sorted(ones)}")

    ranks = pd.DataFrame(rankings).dropna()
    std = ranks.std(axis=1)
    print(
        f"\nPer-player rank std across seeds (n={len(std)} players in all seeds):"
        f"\n  median={std.median():.2f}  mean={std.mean():.2f}  "
        f"p90={std.quantile(0.9):.2f}  max={std.max():.2f}"
    )
    top_region = ranks[ranks.mean(axis=1) <= 50]
    swing = (top_region.max(axis=1) - top_region.min(axis=1)).sort_values(
        ascending=False
    )
    print("\nLargest rank swing among top-region players (mean rank <= 50):")
    for pid, sw in swing.head(10).items():
        row = ranks.loc[pid].astype(int).to_dict()
        print(f"  {pid:<28s} swing={int(sw):>3d}  ranks={row}")


def analyze(
    root=DEFAULT_ROOT,
    split=DEFAULT_SPLIT,
    data_dir=DEFAULT_DATA_DIR,
    link=DEFAULT_LINK,
    write=True,
):
    """Analyze completed seed runs and optionally write the canonical CSV."""
    root = Path(root)
    seed_dirs = discover_seed_dirs(root)
    if not seed_dirs:
        raise SystemExit(f"No completed seed runs under {root}")
    data, games = build_data(split, data_dir)
    out, ppgs = predicted_ppg_table(seed_dirs, data, games, link)
    print_report(ppgs)
    if write:
        output = root / "predicted_ppg_by_seed.csv"
        out.to_csv(output)
        print(f"\nWrote per-seed predicted PPG table -> {output}")
    return out

