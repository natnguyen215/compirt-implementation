"""Infer the active team lineup for each game from buzz evidence.

The source quizbowl data records registered team *rosters* but not the players
who actually played a given game. CompIRT previously treated the whole roster as
active in every game, which inflates the tossup competing-risks population and
the bonus aggregation/synergy with players who may not have played. This module
reconstructs a plausible active lineup (usually four players) per team per game
from who actually buzzed, splitting a game into halves when a mid-game
substitution is evidenced.

The inferred lineups are the model's data-stage roster. The same lineup assigned
to a tossup is reused for the bonus in the same cycle (see ``roster_for``): a
bonus in cycle ``q`` uses the lineup of the tossup in cycle ``q`` by construction.

Resolution per ``(game_id, team_id)`` (``buzzers`` = distinct players who buzzed
that game for that team, partitioned into first half question_num <= 10 and
second half question_num >= 11):

1. ``roster_size <= 4``            -> whole roster (short-handed if < 4).
2. ``roster > 4`` & 4 buzzers      -> those four buzzers.
3. ``roster > 4`` & 1-3 buzzers    -> those buzzers only (short-handed, no fill).
4. ``roster > 4`` & 0 buzzers      -> whole roster (no evidence to infer from).
5. ``roster > 4`` & >= 5 buzzers   -> substitution: infer each half separately.
   A half short of four is filled from the *other* half's buzzers (the players
   known to have played that game), keeping cross-half players consistent. A
   half with more than four buzzers keeps them all. With >= 5 distinct game
   buzzers the two half-buzzer sets always union to >= 4, so no roster fill or
   removal is ever needed.

Random fills use ``random.Random`` seeded from a SHA-256 hash of
``(game_id, team_id, segment)`` so the same database always yields the same
lineups (Python's builtin ``hash`` is per-process salted and must not be used).

Lineups are cached to ``data/lineups/lineup_segments.csv`` and reused by every
training run; ``python lineup.py --rebuild`` regenerates the cache.
"""

from __future__ import annotations

import argparse
import hashlib
import random
from collections import defaultdict
from pathlib import Path

import pandas as pd

from compirt_data import DEFAULT_DATA_DIR, filter_tournament, load_hf_tables

ROOT = Path(__file__).parent
DEFAULT_CACHE = ROOT / "data" / "lineups" / "lineup_segments.csv"
FIRST_HALF_MAX = 10  # question numbers 1-10 are the first half, 11+ the second
LINEUP_TARGET = 4

SEGMENT_COLUMNS = [
    "game_id",
    "team_id",
    "segment",
    "start_question_number",
    "end_question_number",
    "roster_size",
    "distinct_game_buzzers",
    "lineup_size",
    "player_ids",
    "player_1_id",
    "player_2_id",
    "player_3_id",
    "player_4_id",
    "short_handed",
    "confidence",
    "resolution_rule",
    "random_seed",
    "notes",
]


def _segment_seed(game_id: str, team_id: str, segment: str) -> int:
    """Deterministic 64-bit seed for a game/team/segment random choice."""
    digest = hashlib.sha256(f"{game_id}|{team_id}|{segment}".encode()).digest()
    return int.from_bytes(digest[:8], "big")


def _segment_row(
    game_id,
    team_id,
    segment,
    players,
    roster_size,
    distinct_buzzers,
    resolution_rule,
    confidence,
    notes,
    seed=None,
):
    """Assemble one lineup_segments row from a resolved player list."""
    players = list(players)
    start, end = {
        "whole_game": (1, 99),
        "first_half": (1, FIRST_HALF_MAX),
        "second_half": (FIRST_HALF_MAX + 1, 99),
    }[segment]
    padded = players + [""] * (4 - len(players)) if len(players) < 4 else players
    return {
        "game_id": game_id,
        "team_id": team_id,
        "segment": segment,
        "start_question_number": start,
        "end_question_number": end,
        "roster_size": roster_size,
        "distinct_game_buzzers": distinct_buzzers,
        "lineup_size": len(players),
        "player_ids": "|".join(players),
        "player_1_id": padded[0] if len(padded) > 0 else "",
        "player_2_id": padded[1] if len(padded) > 1 else "",
        "player_3_id": padded[2] if len(padded) > 2 else "",
        "player_4_id": padded[3] if len(padded) > 3 else "",
        "short_handed": len(players) < LINEUP_TARGET,
        "confidence": confidence,
        "resolution_rule": resolution_rule,
        "random_seed": "" if seed is None else str(seed),
        "notes": notes,
    }


def _resolve_half(game_id, team_id, segment, own_buzzers, other_buzzers,
                  roster_size, distinct_buzzers):
    """Resolve one half of a substitution game.

    Start from the players who buzzed in this half. If fewer than four, fill
    randomly from the other half's buzzers (consistent cross-half players);
    never remove a player who buzzed in this half, so a half with more than
    four buzzers keeps them all.
    """
    own = sorted(own_buzzers)
    if len(own) >= LINEUP_TARGET:
        return _segment_row(
            game_id, team_id, segment, own, roster_size, distinct_buzzers,
            "half_substitution", "inferred_half_lineup",
            notes=f"{segment}: {len(own)} half buzzers kept as-is",
        )
    pool = sorted(other_buzzers - own_buzzers)
    seed = _segment_seed(game_id, team_id, segment)
    need = min(LINEUP_TARGET - len(own), len(pool))
    fill = random.Random(seed).sample(pool, need)
    lineup = sorted(set(own) | set(fill))
    return _segment_row(
        game_id, team_id, segment, lineup, roster_size, distinct_buzzers,
        "half_substitution", "inferred_half_lineup_with_random_adjustment",
        notes=f"{segment}: {len(own)} half buzzers + {need} filled from other half",
        seed=seed,
    )


def _resolve_team_game(game_id, team_id, roster, first_buzzers, second_buzzers):
    """Return the lineup_segments rows for one team in one game."""
    roster = sorted(roster)
    roster_size = len(roster)
    all_buzzers = first_buzzers | second_buzzers
    n = len(all_buzzers)

    if roster_size <= LINEUP_TARGET:
        return [_segment_row(
            game_id, team_id, "whole_game", roster, roster_size, n,
            "whole_game_small_roster", "high_roster_size_leq_4",
            notes="roster <= 4: entire roster active",
        )]
    if n == LINEUP_TARGET:
        return [_segment_row(
            game_id, team_id, "whole_game", sorted(all_buzzers), roster_size, n,
            "whole_game_exact_four_buzzers", "high_exact_four_game_buzzers",
            notes="exactly four distinct game buzzers",
        )]
    if 1 <= n <= 3:
        return [_segment_row(
            game_id, team_id, "whole_game", sorted(all_buzzers), roster_size, n,
            "whole_game_short_handed", "inferred_whole_game_short_handed",
            notes="1-3 distinct game buzzers; treated as short-handed, no fill",
        )]
    if n == 0:
        return [_segment_row(
            game_id, team_id, "whole_game", roster, roster_size, n,
            "whole_game_no_evidence", "whole_game_no_evidence_full_roster",
            notes="no buzz evidence; falling back to full registered roster",
        )]
    # n >= 5: a substitution occurred; infer each half separately.
    return [
        _resolve_half(game_id, team_id, "first_half", first_buzzers,
                      second_buzzers, roster_size, n),
        _resolve_half(game_id, team_id, "second_half", second_buzzers,
                      first_buzzers, roster_size, n),
    ]


def _buzzers_by_game_team(tables):
    """Map ``(game_id, team_id)`` to (first-half, second-half) buzzer sets.

    Each buzz is attributed to a team by roster membership and to a half by the
    packet ``question_num`` of the tossup it landed on (<= 10 first, >= 11
    second). ``question_num`` equals ``question_number_in_game`` and is always
    present, so this does not depend on the buzz-level game-position column.
    """
    rosters = tables["teams"].set_index("team_id")["player_ids"].to_dict()
    tossup_qnum = tables["tossups"].set_index("tossup_id")["question_num"].to_dict()

    player_team_by_game = {}
    for game in tables["games"].to_dict("records"):
        lookup = {}
        for team_id in game["team_ids"]:
            for player_id in rosters.get(team_id, []):
                lookup[player_id] = team_id
        player_team_by_game[game["game_id"]] = lookup

    buzzers = defaultdict(lambda: (set(), set()))
    for buzz in tables["tossup_buzzes"].itertuples(index=False):
        lookup = player_team_by_game.get(buzz.game_id)
        if not lookup:
            continue
        team_id = lookup.get(buzz.player_id)
        qnum = tossup_qnum.get(buzz.tossup_id)
        if team_id is None or qnum is None:
            continue
        first, second = buzzers[(buzz.game_id, team_id)]
        (first if qnum <= FIRST_HALF_MAX else second).add(buzz.player_id)
    return buzzers


def build_lineup_segments(tables) -> pd.DataFrame:
    """Infer lineup segments for every team in every game.

    Returns one row per ``(game_id, team_id, segment)``; ``segment`` is
    ``whole_game`` or the pair ``first_half``/``second_half`` when a
    substitution is detected.
    """
    rosters = tables["teams"].set_index("team_id")["player_ids"].to_dict()
    buzzers = _buzzers_by_game_team(tables)
    rows = []
    for game in tables["games"].to_dict("records"):
        game_id = game["game_id"]
        for team_id in game["team_ids"]:
            first, second = buzzers.get((game_id, team_id), (set(), set()))
            rows.extend(_resolve_team_game(
                game_id, team_id, rosters.get(team_id, []), first, second
            ))
    return pd.DataFrame(rows, columns=SEGMENT_COLUMNS)


class LineupIndex:
    """Look up inferred lineups by game, team, and question number."""

    def __init__(self, segments: pd.DataFrame):
        self._by_key: dict[tuple[str, str], dict[str, list[str]]] = {}
        for row in segments.itertuples(index=False):
            raw = row.player_ids
            players = raw.split("|") if isinstance(raw, str) and raw else []
            self._by_key.setdefault((row.game_id, row.team_id), {})[row.segment] = players

    def roster_for(self, game_id, team_id, question_number) -> list[str]:
        """Return the active lineup for a team at a given question number.

        The bonus in a cycle reuses its tossup's lineup because both resolve
        through the same ``(game, team, question -> segment)`` mapping.
        """
        segments = self._by_key.get((game_id, team_id))
        if not segments:
            return []
        if "whole_game" in segments:
            return list(segments["whole_game"])
        half = "first_half" if question_number <= FIRST_HALF_MAX else "second_half"
        return list(segments.get(half, []))

    def _missing_game_teams(self, tables) -> bool:
        for game in tables["games"].to_dict("records"):
            for team_id in game["team_ids"]:
                if (game["game_id"], team_id) not in self._by_key:
                    return True
        return False

    def _merge(self, segments: pd.DataFrame) -> None:
        for row in segments.itertuples(index=False):
            key = (row.game_id, row.team_id)
            if key in self._by_key and row.segment in self._by_key[key]:
                continue
            raw = row.player_ids
            players = raw.split("|") if isinstance(raw, str) and raw else []
            self._by_key.setdefault(key, {})[row.segment] = players

    @classmethod
    def from_tables(cls, tables):
        """Build an in-memory index without touching the on-disk cache."""
        return cls(build_lineup_segments(tables))

    @classmethod
    def load_or_build(cls, tables, cache_path=DEFAULT_CACHE, rebuild=False):
        """Load the persisted lineup cache, building and writing it if absent.

        On a cache hit that is missing some games in ``tables`` (e.g. a stale or
        partial cache), the missing games are inferred on the fly without
        rewriting the cache.
        """
        cache_path = Path(cache_path)
        if not rebuild and cache_path.exists():
            cached = pd.read_csv(cache_path, dtype=str, keep_default_na=False)
            index = cls(cached)
            if index._missing_game_teams(tables):
                index._merge(build_lineup_segments(tables))
            return index
        segments = build_lineup_segments(tables)
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        segments.to_csv(cache_path, index=False)
        return cls(segments)


def _bonus_lineup_frame(tables, index: LineupIndex) -> pd.DataFrame:
    """Debug table: the reused lineup for every observed bonus response."""
    bonus_qnum = tables["bonuses"].set_index("bonus_id")["question_num"].to_dict()
    rows = []
    for response in tables["bonus_responses"].itertuples(index=False):
        qnum = bonus_qnum.get(response.bonus_id)
        lineup = index.roster_for(response.game_id, response.team_id, qnum or 1)
        rows.append({
            "game_id": response.game_id,
            "team_id": response.team_id,
            "bonus_id": response.bonus_id,
            "question_number": qnum,
            "segment": "first_half" if (qnum or 1) <= FIRST_HALF_MAX else "second_half",
            "player_ids": "|".join(lineup),
        })
    return pd.DataFrame(rows)


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--rebuild", action="store_true",
                        help="Recompute and overwrite the lineup cache.")
    parser.add_argument("--dump-debug", action="store_true",
                        help="Also write bonus_team_lineup.csv next to the cache.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    index = LineupIndex.load_or_build(tables, args.cache, rebuild=args.rebuild)
    segments = pd.read_csv(args.cache, dtype=str, keep_default_na=False)
    print(f"Lineup segments: {len(segments):,}")
    print(segments["resolution_rule"].value_counts().to_string())
    if args.dump_debug:
        debug_path = Path(args.cache).parent / "bonus_team_lineup.csv"
        _bonus_lineup_frame(tables, index).to_csv(debug_path, index=False)
        print(f"Wrote {debug_path}")
