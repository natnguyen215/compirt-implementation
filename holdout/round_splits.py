"""Build linked train/test tables from the final fraction of tournament rounds.

A derived split has the form::

    round-holdout:<base-split>:<train|test>:<fraction>

For example, ``round-holdout:year_2024:test:0.2`` selects every game in the
final 20 percent of each tournament's numbered rounds.  Selection is performed
at the round boundary, so simultaneous games are never divided across train and
test.  The number of held-out rounds is ``ceil(n_rounds * fraction)`` with a
minimum of one.  Games whose round cannot be parsed are conservatively assigned
to test so they cannot leak an unknown point in the schedule into training.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import pandas as pd


ROUND_HOLDOUT_PREFIX = "round-holdout"


@dataclass(frozen=True)
class RoundHoldoutSpec:
    """Parsed description of one side of a final-round-fraction split."""

    base_split: str
    part: str
    fraction: float


def round_holdout_split_name(base_split: str, part: str, fraction: float) -> str:
    """Return the canonical loader split name for a round holdout."""
    if not base_split or ":" in base_split:
        raise ValueError("base_split must be a non-empty dataset split name")
    if part not in {"train", "test"}:
        raise ValueError("round holdout part must be 'train' or 'test'")
    fraction = float(fraction)
    if not 0.0 < fraction < 1.0:
        raise ValueError("round holdout fraction must be strictly between 0 and 1")
    return f"{ROUND_HOLDOUT_PREFIX}:{base_split}:{part}:{fraction:g}"


def parse_round_holdout_split(split: str) -> RoundHoldoutSpec | None:
    """Parse a derived split name, returning ``None`` for ordinary splits."""
    if not split.startswith(f"{ROUND_HOLDOUT_PREFIX}:"):
        return None
    pieces = split.split(":")
    if len(pieces) != 4:
        raise ValueError(
            "round holdout splits must use "
            "'round-holdout:<base-split>:<train|test>:<fraction>'"
        )
    _, base_split, part, raw_fraction = pieces
    try:
        fraction = float(raw_fraction)
    except ValueError as error:
        raise ValueError(
            f"round holdout fraction must be numeric, got {raw_fraction!r}"
        ) from error
    # Reuse the public constructor's validation without depending on its text.
    round_holdout_split_name(base_split, part, fraction)
    return RoundHoldoutSpec(base_split, part, fraction)


def _round_numbers(games: pd.DataFrame) -> pd.Series:
    """Extract trailing numeric round labels such as ``round12``."""
    if "round" not in games:
        raise ValueError("games table has no 'round' column for round holdout")
    return pd.to_numeric(
        games["round"].astype("string").str.extract(r"(\d+)$", expand=False),
        errors="coerce",
    )


def round_holdout_game_mask(
    games: pd.DataFrame, fraction: float = 0.2
) -> pd.Series:
    """Return a boolean mask selecting each tournament's final round fraction.

    Distinct numeric rounds, rather than their labels' absolute values, define
    the denominator.  Thus a schedule with rounds ``1, 2, 4`` holds out one
    round at 20 percent, and a tiebreaker labeled ``round500`` sorts last.
    """
    fraction = float(fraction)
    if not 0.0 < fraction < 1.0:
        raise ValueError("round holdout fraction must be strictly between 0 and 1")
    if "tournament_id" not in games:
        raise ValueError("games table has no 'tournament_id' column")

    round_number = _round_numbers(games)
    held_out = round_number.isna()
    for _, indices in games.groupby("tournament_id", sort=False).groups.items():
        tournament_rounds = sorted(round_number.loc[indices].dropna().unique())
        if not tournament_rounds:
            # Every game in this tournament is already selected by the missing-
            # round rule above.
            continue
        count = max(1, math.ceil(len(tournament_rounds) * fraction))
        final_rounds = set(tournament_rounds[-count:])
        held_out.loc[indices] |= round_number.loc[indices].isin(final_rounds)
    return held_out.astype(bool)


def _tables_for_games(tables: dict[str, pd.DataFrame], games: pd.DataFrame):
    """Filter every outcome-linked table to ``games`` while preserving schema."""
    game_ids = set(games["game_id"])
    tournament_ids = set(games["tournament_id"])
    team_ids = {
        team_id
        for members in games["team_ids"]
        for team_id in members
    }

    tournaments = tables["tournaments"]
    selected_tournaments = tournaments[
        tournaments["tournament_id"].isin(tournament_ids)
    ].copy()
    question_set_event_ids = set(selected_tournaments["question_set_event_id"])

    return {
        "tournaments": selected_tournaments,
        "teams": tables["teams"][tables["teams"]["team_id"].isin(team_ids)].copy(),
        "games": games.copy(),
        "tossup_buzzes": tables["tossup_buzzes"][
            tables["tossup_buzzes"]["game_id"].isin(game_ids)
        ].copy(),
        "bonus_responses": tables["bonus_responses"][
            tables["bonus_responses"]["game_id"].isin(game_ids)
        ].copy(),
        # Question metadata is shared across mirrors of a question-set event.
        # Outcomes remain game-filtered above; retaining metadata lets the
        # observation builders resolve the selected games' packet contents.
        "tossups": tables["tossups"][
            tables["tossups"]["question_set_event_id"].isin(
                question_set_event_ids
            )
        ].copy(),
        "bonuses": tables["bonuses"][
            tables["bonuses"]["question_set_event_id"].isin(
                question_set_event_ids
            )
        ].copy(),
    }


def select_round_holdout_tables(
    tables: dict[str, pd.DataFrame], part: str, fraction: float = 0.2
) -> dict[str, pd.DataFrame]:
    """Return linked tables for the train or test side of a round holdout."""
    if part not in {"train", "test"}:
        raise ValueError("round holdout part must be 'train' or 'test'")
    held_out = round_holdout_game_mask(tables["games"], fraction)
    selected = held_out if part == "test" else ~held_out
    return _tables_for_games(tables, tables["games"].loc[selected])
