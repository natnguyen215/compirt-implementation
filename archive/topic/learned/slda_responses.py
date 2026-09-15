"""Per-question outcome aggregates for the topic diagnostics.

These pure helpers turn the observation DataFrames built by 'compirt_data' into
'{question_id: value}' maps -- correctness rate and mean buzz position per
question. They are used by 'topic_response_profiles' to profile what each learned
topic captures. The joint model itself is supervised by the IRT likelihood, not
by these aggregates.

The question_id key is the shared composite ID ('tossup_id' / 'bonus_id'), which
equals the topic-corpus 'document_id' (e.g. '2024-acf-regionals::01272024::p1::q1').
"""

from __future__ import annotations

import pandas as pd


def tossup_responses(tossup_obs: pd.DataFrame) -> dict[str, float]:
    """Return each tossup's conversion rate keyed by 'tossup_id'.

    Conversion rate = (correct first buzzes) / (times the tossup was read). A
    tossup read five times and answered correctly three times scores 0.6; negged
    and dead reads count against it, so harder tossups score lower.
    """
    if tossup_obs.empty:
        return {}
    # One BUZZ row per buzzed event; dead events contribute only NO-BUZZ rows.
    is_correct_buzz = (tossup_obs["z"] == "BUZZ") & (tossup_obs["y"] == 1.0)
    reads = tossup_obs.groupby("tossup_id")["event_id"].nunique()
    # Grouping over the same frame gives both series the same tossup_id index.
    correct = is_correct_buzz.groupby(tossup_obs["tossup_id"]).sum()
    rate = correct / reads
    return {str(tossup_id): float(value) for tossup_id, value in rate.items()}


def bonus_responses(bonus_obs: pd.DataFrame) -> dict[str, float]:
    """Return each bonus's part-correctness rate keyed by 'bonus_id'.

    Averaged over every observed part (all teams, all games). The bonus topic
    vector is shared by all three parts, so the response is per bonus, matching
    the per-bonus alignment in the downstream topic-CompIRT pipeline.
    """
    if bonus_obs.empty:
        return {}
    rate = bonus_obs.groupby("bonus_id")["correct"].mean()
    return {str(bonus_id): float(value) for bonus_id, value in rate.items()}


def tossup_buzz_positions(tossup_obs: pd.DataFrame) -> dict[str, float]:
    """Return each tossup's mean relative first-buzz position keyed by 'tossup_id'.

    Used by the diagnostic profiler, not by training. Lower means the tossup is
    answered earlier (easier to recognize).
    """
    if tossup_obs.empty:
        return {}
    buzzes = tossup_obs[tossup_obs["z"] == "BUZZ"]
    if buzzes.empty:
        return {}
    position = buzzes.groupby("tossup_id")["relative_position"].mean()
    return {str(tossup_id): float(value) for tossup_id, value in position.items()}
