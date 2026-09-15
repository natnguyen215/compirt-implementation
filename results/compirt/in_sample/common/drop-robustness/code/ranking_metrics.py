"""Generic metrics for comparing player-score rankings.

The 'drop_robustness' studies compare a full-data ranking against perturbed
refits and alternate-seed fits through 'compare_rankings'. Its shared
'rank_correlations' and 'topk_jaccard' primitives keep the
Kendall/Spearman/Jaccard definitions consistent across comparisons.
"""

from __future__ import annotations

from scipy.stats import kendalltau, spearmanr

DEFAULT_TOPKS = (5, 10, 25)


def rank_correlations(scores_a, scores_b):
    """Return (n_common, kendall_tau, spearman) on the two series' shared index.

    Both series must use the same orientation: higher is better (PPG) or lower
    is better (rank position). Reversing both orientations preserves the
    correlations. Fewer than two shared players gives undefined correlations.
    """
    common = scores_a.index.intersection(scores_b.index)
    if len(common) < 2:
        return len(common), float("nan"), float("nan")
    a = scores_a.loc[common]
    b = scores_b.loc[common]
    return len(common), kendalltau(a, b).statistic, spearmanr(a, b).statistic


def topk_jaccard(scores_a, scores_b, k, higher_is_better=True):
    """Jaccard overlap of the two top-k sets on a shared index.

    'higher_is_better' picks the best k by largest score (PPG) when True and by
    smallest score (rank position) when False. Selection is restricted to
    players present in both series; an empty selection returns NaN.
    """
    pick = (lambda s: s.nlargest(k)) if higher_is_better else (lambda s: s.nsmallest(k))
    common = scores_a.index.intersection(scores_b.index)
    top_a = set(pick(scores_a.loc[common]).index)
    top_b = set(pick(scores_b.loc[common]).index)
    union = top_a | top_b
    return len(top_a & top_b) / len(union) if union else float("nan")


def compare_rankings(ppg_ref, ppg_alt, topks=DEFAULT_TOPKS):
    """Agreement between a reference and an alternate PPG ranking.

    All statistics are computed on the players present in both series; a
    dropped-data refit can lose players whose only appearances were dropped.
    With no shared players, agreement statistics (including ``top1_changed``)
    are NaN and ``n_common`` is zero.
    """
    common = ppg_ref.index.intersection(ppg_alt.index)
    ref = ppg_ref.loc[common]
    alt = ppg_alt.loc[common]
    ref_rank = ref.rank(ascending=False, method="min")
    alt_rank = alt.rank(ascending=False, method="min")

    n_common, kendall, spearman = rank_correlations(ref, alt)
    result = {
        "n_common": n_common,
        "kendall_tau": kendall,
        "spearman": spearman,
        "top1_changed": bool(ref.idxmax() != alt.idxmax()) if len(common) else float("nan"),
        "mean_abs_ppg_change": float((ref - alt).abs().mean()),
    }
    for k in topks:
        result[f"jaccard_top{k}"] = topk_jaccard(ref, alt, k, higher_is_better=True)
    top25 = ref_rank[ref_rank <= 25].index
    result["max_displacement_top25"] = float(
        (ref_rank.loc[top25] - alt_rank.loc[top25]).abs().max()
    )
    return result
