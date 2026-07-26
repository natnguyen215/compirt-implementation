"""Pure seed-stability metrics for predicted-PPG rankings.

Aggregates the shared two-way primitives in
'compirt_eval.common.ranking_metrics' over every pair of same-data seed refits.
The per-seed inputs are rank positions (1 = best), so top-k selection asks for
the smallest ranks ('higher_is_better=False').
"""

from __future__ import annotations

import itertools

import numpy as np
import pandas as pd

from compirt_eval.common.ranking_metrics import (
    DEFAULT_TOPKS,
    rank_correlations,
    topk_jaccard,
)


def pairwise_agreement(rankings) -> pd.DataFrame:
    """Return rank correlations for every pair of available seeds."""
    seeds = sorted(rankings)
    rows = []
    for a, b in itertools.combinations(seeds, 2):
        n, kendall, spearman = rank_correlations(rankings[a], rankings[b])
        rows.append(
            {
                "seed_a": a,
                "seed_b": b,
                "n": n,
                "kendall_tau": kendall,
                "spearman": spearman,
            }
        )
    return pd.DataFrame(rows)


def topk_jaccards(rankings, topks=DEFAULT_TOPKS):
    """Return every pairwise top-k Jaccard value, keyed by k."""
    seeds = sorted(rankings)
    return {
        k: [
            topk_jaccard(rankings[a], rankings[b], k, higher_is_better=False)
            for a, b in itertools.combinations(seeds, 2)
        ]
        for k in topks
    }


def mean_topk_jaccards(rankings, topks=DEFAULT_TOPKS):
    """Return mean pairwise top-k Jaccard values."""
    return {
        k: float(np.mean(values))
        for k, values in topk_jaccards(rankings, topks).items()
    }
