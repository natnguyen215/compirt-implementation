"""Drop-specific ranking metrics beyond generic rank agreement."""

from __future__ import annotations

import pandas as pd


def pair_gap(ppg: pd.Series, target: str, rival: str):
    """Return target-minus-rival gap and ranks, or Nones if either is absent."""
    if target not in ppg.index or rival not in ppg.index:
        return None, None, None
    ranks = ppg.rank(ascending=False, method="min")
    return (
        float(ppg[target] - ppg[rival]),
        int(ranks[target]),
        int(ranks[rival]),
    )
