"""Load the local HuggingFace tables and build observation tensors.

Tossup pipeline:
    linked HuggingFace tables
        -> one row per player per game-tossup event
        -> integer-indexed, one-dimensional tensors

Bonus pipeline:
    linked HuggingFace tables
        -> one row per team bonus part
        -> padded roster matrices plus a padding mask
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
import torch
from datasets import load_from_disk


ROOT = Path(__file__).parent
DEFAULT_DATA_DIR = ROOT / "data" / "hf" / "quizbowl-irt"
TABLES = (
    "tournaments",
    "teams",
    "games",
    "tossups",
    "tossup_buzzes",
    "bonus_responses",
    "bonuses",
)


def load_hf_tables(data_dir: str | Path = DEFAULT_DATA_DIR, split: str = "all"):
    """Load every linked HuggingFace table as a pandas DataFrame.

    'split' is '"all"', a year split such as '"year_2024"', an academic-season
    split such as '"season_2024_25"', a derived final-round split such as
    '"round-holdout:year_2024:test:0.2"', or a derived stratified whole-game
    split such as '"game-holdout:year_2024:test:5:0:42"'. The returned dict is
    keyed by table name ('tables["games"]', etc.).
    """
    from holdout.round_splits import (
        parse_round_holdout_split,
        select_round_holdout_tables,
    )
    from holdout.game_splits import (
        parse_game_holdout_split,
        select_game_holdout_tables,
    )
    from holdout.season_splits import (
        SEASON_BASE_SPLIT,
        parse_season_split,
        select_season_tables,
    )

    data_dir = Path(data_dir)
    round_spec = parse_round_holdout_split(split)
    game_spec = parse_game_holdout_split(split)
    if round_spec is not None:
        disk_split = round_spec.base_split
    elif game_spec is not None:
        disk_split = game_spec.base_split
    else:
        disk_split = split
    # Seasons span calendar years, so they are carved out of "all" in memory
    # rather than read from a disk split of their own.
    season = parse_season_split(disk_split)
    if season is not None:
        disk_split = SEASON_BASE_SPLIT
    # Each table is its own DatasetDict directory; pandas is easier to join.
    tables = {
        name: load_from_disk(str(data_dir / name))[disk_split].to_pandas()
        for name in TABLES
    }
    if season is not None:
        # Applied before any derived selection so folds are drawn within the
        # season, not within the whole corpus.
        tables = select_season_tables(tables, season)
    if round_spec is not None:
        return select_round_holdout_tables(
            tables, round_spec.part, round_spec.fraction
        )
    if game_spec is not None:
        return select_game_holdout_tables(tables, game_spec)
    return tables


def filter_tournament(tables, tournament: str | None):
    """Return linked table copies restricted to a tournament selection.

    The value may be an exact ID or a prefix; e.g. '"2024-acf-regionals"'
    selects all 2024 Regionals mirror tournaments. Each table is filtered
    through its own foreign key so the result stays mutually consistent.
    """
    if not tournament:
        # Return independent tables to protect the originals from mutation.
        return {name: table.copy() for name, table in tables.items()}

    tournaments = tables["tournaments"]
    # Exact matches plus mirror sites sharing the requested prefix.
    selected = tournaments[
        (tournaments["tournament_id"] == tournament)
        | tournaments["tournament_id"].str.startswith(tournament)
    ]
    tournament_ids = set(selected["tournament_id"])
    # Tossups and bonuses belong to a shared question-set event, not a single
    # mirror tournament, so they are selected through this ID.
    question_set_event_ids = set(selected["question_set_event_id"])
    game_ids = set(
        tables["games"].loc[
            tables["games"]["tournament_id"].isin(tournament_ids), "game_id"
        ]
    )
    team_ids = set(
        tables["teams"].loc[
            tables["teams"]["tournament_id"].isin(tournament_ids), "team_id"
        ]
    )
    return {
        "tournaments": selected.copy(),
        "games": tables["games"][tables["games"]["game_id"].isin(game_ids)].copy(),
        "teams": tables["teams"][tables["teams"]["team_id"].isin(team_ids)].copy(),
        "tossup_buzzes": tables["tossup_buzzes"][
            tables["tossup_buzzes"]["game_id"].isin(game_ids)
        ].copy(),
        "bonus_responses": tables["bonus_responses"][
            tables["bonus_responses"]["game_id"].isin(game_ids)
        ].copy(),
        "tossups": tables["tossups"][
            tables["tossups"]["question_set_event_id"].isin(question_set_event_ids)
        ].copy(),
        "bonuses": tables["bonuses"][
            tables["bonuses"]["question_set_event_id"].isin(question_set_event_ids)
        ].copy(),
    }


def make_index(values):
    """Map readable string IDs to contiguous integer indices.

    Returns the sorted readable IDs and a mapping such as
    '{"andrew-heller": 0, ...}' for indexing parameter tensors.
    """
    ids = sorted({str(value) for value in values})
    return ids, {value: index for index, value in enumerate(ids)}


def _event_roster(game_id, game, lineups, question_number):
    """Return the inferred combined lineup for a game-tossup event.

    Both teams' inferred lineups (see 'lineup.py') for the segment containing
    'question_number' compete for the buzz. Returns the combined player list and
    a player-to-team lookup built from lineup membership.
    """
    player_team = {}
    for team_id in game["team_ids"]:
        for player_id in lineups.roster_for(game_id, team_id, question_number):
            player_team[player_id] = team_id
    return list(player_team), player_team


def _player_team(game, teams, player_id):
    """Return which of a game's teams a player is registered on, or None."""
    for team_id in game["team_ids"]:
        if player_id in teams[team_id]["player_ids"]:
            return team_id
    return None


def _observed_first_buzz_rows(
    first_buzzes,
    games,
    teams,
    tournaments,
    lineups,
    tossup_qnum,
    tossup_category,
):
    """Expand each first-buzz event into BUZZ and CENSORED roster rows.

    The observed buzzer carries correctness at the clamped buzz position; every
    other active player is censored at that same position.
    """
    rows = []
    for buzz in first_buzzes.itertuples(index=False):
        game = games[buzz.game_id]
        question_number = int(tossup_qnum.get(buzz.tossup_id, 1))
        roster, player_team = _event_roster(
            buzz.game_id, game, lineups, question_number
        )
        # The observed buzzer must remain in the risk set even if lineup
        # inference omitted an off-roster or otherwise anomalous player.
        if buzz.player_id not in player_team:
            team_of = _player_team(game, teams, buzz.player_id)
            if team_of is not None:
                player_team[buzz.player_id] = team_of
                roster.append(buzz.player_id)
        T_j = max(1, int(buzz.num_tokens_total))
        t_star = min(max(1, int(buzz.token_position)), T_j)
        tier = tournaments[game["tournament_id"]]["tier"]
        for player_id in roster:
            is_buzzer = player_id == buzz.player_id
            rows.append(
                {
                    "event_id": f"{buzz.game_id}::{buzz.tossup_id}",
                    "game_id": buzz.game_id,
                    "team_id": player_team[player_id],
                    "player_id": player_id,
                    "tossup_id": buzz.tossup_id,
                    # raw_t_star preserves source anomalies; the likelihood
                    # consumes the clamped position in [1, T_j].
                    "raw_t_star": int(buzz.token_position),
                    # First-buzz rows are phase 0: everyone is at risk from the
                    # first token, so survival runs over [t_start, t_star).
                    "t_start": 1,
                    "phase": 0,
                    "t_star": t_star,
                    "T_j": T_j,
                    "relative_position": t_star / T_j,
                    "y": float(bool(buzz.correct)) if is_buzzer else float("nan"),
                    "z": "BUZZ" if is_buzzer else "CENSORED",
                    "tournament_id": game["tournament_id"],
                    "tier": tier,
                    "category": tossup_category.get(buzz.tossup_id, "Unknown"),
                    "roster_size": len(roster),
                }
            )
    return rows


def _terminal_no_buzz_rows(
    tables,
    games,
    tournaments,
    lineups,
    first_buzzes,
):
    """Recover played tossups without a buzz and emit one NO-BUZZ row per player.

    Packet position supplies tossup identity, while each game's 'tossups_read'
    limit prevents unread packet questions from becoming dead-tossup events.
    """
    if not games or "packet_id" not in tables["games"].columns:
        return []
    tossups_by_packet = {
        packet_id: group.sort_values("question_num")
        for packet_id, group in tables["tossups"].groupby("packet")
    }
    buzzed = set(zip(first_buzzes["game_id"], first_buzzes["tossup_id"]))
    rows = []
    for game_id, game in games.items():
        scheduled = tossups_by_packet.get(int(game["packet_id"]))
        if scheduled is None:
            # Without a packet match, no tossup identity can be recovered safely.
            continue
        scheduled = scheduled.iloc[: int(game["tossups_read"])]
        tier = tournaments[game["tournament_id"]]["tier"]
        for tossup in scheduled.itertuples(index=False):
            if (game_id, tossup.tossup_id) in buzzed:
                continue
            roster, player_team = _event_roster(
                game_id, game, lineups, int(tossup.question_num)
            )
            T_j = max(1, len(tossup.tokens))
            for player_id in roster:
                rows.append(
                    {
                        "event_id": f"{game_id}::{tossup.tossup_id}",
                        "game_id": game_id,
                        "team_id": player_team[player_id],
                        "player_id": player_id,
                        "tossup_id": tossup.tossup_id,
                        "raw_t_star": T_j,
                        "t_start": 1,
                        "phase": 0,
                        "t_star": T_j,
                        "T_j": T_j,
                        "relative_position": 1.0,
                        "y": float("nan"),
                        "z": "NO-BUZZ",
                        "tournament_id": game["tournament_id"],
                        "tier": tier,
                        "category": getattr(tossup, "category", "Unknown"),
                        "roster_size": len(roster),
                    }
                )
    return rows


def _bounceback_rows(
    neg_first_buzzes,
    continuation_buzzes,
    games,
    teams,
    tournaments,
    lineups,
    tossup_qnum,
    tossup_category,
):
    """Emit the opponent-only phase-1 risk set after a first-buzz neg.

    Paper Section 3.1 ("Neg handling") and Appendix A: once a player negs at
    't_neg', that player's team is locked out and only the opposing team stays
    at risk over the remaining tokens '[t_neg + 1, T_j]'. Phase 0 has already
    censored every player at 't_neg' (the neg is a BUZZ row, everyone else a
    CENSORED row at that token), so this second phase adds *only* the opponent's
    continuation. Combined, an opponent's survival is the product of its phase-0
    term over '[1, t_neg)' and its phase-1 term over '[t_neg + 1, ...)'; the neg
    token itself contributes no factor for the opponent, matching the
    competing-risks convention that losers are censored just before the winner's
    event (Eq. 6 uses a strict '< t' product).

    Row types mirror phase 0 but carry a 'BOUNCE-' prefix so every existing
    'z == "BUZZ"' first-buzz diagnostic transparently ignores them:

    * 'BOUNCE-BUZZ'     the opponent who converts (or misses) the bounceback;
                        contributes hazard and correctness at the bounce token.
    * 'BOUNCE-CENSORED' the opponent's other players, censored at the bounce
                        token.
    * 'BOUNCE-NO-BUZZ'  every opponent when the question ran out with *no*
                        recorded continuation at all; right-censored to 'T_j'
                        (genuine post-neg survival evidence).

    The bounceback is the *earliest post-neg record belonging to the opposing
    team*. Records attributed to the locked-out negging team are impossible
    under lockout, so they are skipped over rather than trusted. Three outcomes:

    * an opposing-team continuation exists -> BOUNCE-BUZZ / BOUNCE-CENSORED;
    * no continuation record at all -> BOUNCE-NO-BUZZ (real right-censoring);
    * continuation records exist but none resolves to the opposing team (e.g.
      only same-team anomalies) -> phase 1 is *omitted* for that event. Emitting
      a no-buzz there would falsely assert the opponent survived to the end.

    A continuation recorded at or before the neg token is pushed to 't_neg + 1'
    so the phase-1 interval stays ordered.
    """
    continuations_by_event = {}
    for row in continuation_buzzes.itertuples(index=False):
        # continuation_buzzes is already token-then-buzz-id ordered, so each
        # list stays in ascending token order.
        continuations_by_event.setdefault(
            (row.game_id, row.tossup_id), []
        ).append(row)

    rows = []
    for neg in neg_first_buzzes.itertuples(index=False):
        game = games[neg.game_id]
        question_number = int(tossup_qnum.get(neg.tossup_id, 1))
        roster, player_team = _event_roster(
            neg.game_id, game, lineups, question_number
        )
        neg_team = player_team.get(neg.player_id) or _player_team(
            game, teams, neg.player_id
        )
        if neg_team is None:
            # Without the locked-out team we cannot define the opponent risk set.
            continue
        opponent = [
            player_id for player_id in roster if player_team[player_id] != neg_team
        ]
        T_j = max(1, int(neg.num_tokens_total))
        t_neg = min(max(1, int(neg.token_position)), T_j)
        # First token at which the opponent alone is at risk.
        t_start = min(t_neg + 1, T_j)
        tier = tournaments[game["tournament_id"]]["tier"]
        tossup_cat = tossup_category.get(neg.tossup_id, "Unknown")

        # Earliest post-neg record that resolves to the opposing team.
        continuations = continuations_by_event.get(
            (neg.game_id, neg.tossup_id), []
        )
        bounce = None
        bounce_team = None
        for candidate in continuations:
            candidate_team = player_team.get(candidate.player_id) or _player_team(
                game, teams, candidate.player_id
            )
            if candidate_team is not None and candidate_team != neg_team:
                bounce = candidate
                bounce_team = candidate_team
                break

        if bounce is None and continuations:
            # Only same-team / unresolvable continuations: omit phase 1 rather
            # than fabricate false no-buzz survival evidence for the opponent.
            continue

        def base_row(player_id, t_star, z, y, raw_t_star):
            return {
                "event_id": f"{neg.game_id}::{neg.tossup_id}",
                "game_id": neg.game_id,
                "team_id": player_team[player_id],
                "player_id": player_id,
                "tossup_id": neg.tossup_id,
                "raw_t_star": raw_t_star,
                "t_start": t_start,
                "phase": 1,
                "t_star": t_star,
                "T_j": T_j,
                "relative_position": t_star / T_j,
                "y": y,
                "z": z,
                "tournament_id": game["tournament_id"],
                "tier": tier,
                "category": tossup_cat,
                "roster_size": len(opponent),
            }

        if bounce is not None:
            # Keep the observed converter in the risk set even if lineup
            # inference dropped them, mirroring the phase-0 fallback.
            if bounce.player_id not in player_team:
                player_team[bounce.player_id] = bounce_team
                opponent.append(bounce.player_id)
            raw_bounce = min(max(1, int(bounce.token_position)), T_j)
            bounce_pos = min(max(t_start, raw_bounce), T_j)
            for player_id in opponent:
                is_buzzer = player_id == bounce.player_id
                rows.append(
                    base_row(
                        player_id,
                        bounce_pos,
                        "BOUNCE-BUZZ" if is_buzzer else "BOUNCE-CENSORED",
                        float(bool(bounce.correct)) if is_buzzer else float("nan"),
                        int(bounce.token_position),
                    )
                )
        else:
            # No continuation at all: the opponent heard the rest of the
            # question and never buzzed, a right-censored survival to T_j.
            for player_id in opponent:
                rows.append(
                    base_row(player_id, T_j, "BOUNCE-NO-BUZZ", float("nan"), T_j)
                )
    return rows


def build_tossup_observations(tables, lineups=None, include_bounceback=False):
    """Build one model row per rostered player per game-tossup event.

    For a tossup with a recorded first buzz, the function emits:

    * one 'BUZZ' row for the first buzzer; its 'y' is correctness;
    * one 'CENSORED' row for every other rostered player, meaning that player
      had not buzzed before the observed first-buzz position.

    For a recoverable dead tossup, it emits one 'NO-BUZZ' row per player.
    These rows let the competing-risks model learn from nobody buzzing.

    With 'include_bounceback=True', tossups whose first buzz was a neg
    (raw value '-5') additionally get an opposing-team phase-1 risk set
    ('BOUNCE-*' rows) covering the tokens after the neg, completing the paper's
    unfinished neg-then-bounceback derivation (Section 3.1 / Appendix A). See
    '_bounceback_rows'. The default is off: no 'BOUNCE-*' rows are produced and
    every phase-0 value is unchanged, so every other model family and the
    held-out/ablation runners fit numerically identical models to before.

    Every row carries a phase-1 survival interval '[t_start, t_star)': phase-0
    rows use 't_start = 1' (identical to the historical '[1, t_star)') and
    phase-1 bounceback rows use 't_start = t_neg + 1'. The 't_start' and 'phase'
    columns are present regardless (phase-0 rows are '1' and '0'), a small
    additive schema change from pre-bounceback runs.

    The active players are the per-game lineups inferred in 'lineup.py' (cached
    under 'data/lineups/') rather than the full registered roster, so the
    competing-risks population reflects who plausibly played each game. A
    tossup's segment is chosen from its packet 'question_num' (<= 10 first half,
    >= 11 second half).
    """
    from lineup import LineupIndex

    games = tables["games"].set_index("game_id").to_dict("index")
    teams = tables["teams"].set_index("team_id").to_dict("index")
    tournaments = tables["tournaments"].set_index("tournament_id").to_dict("index")
    if lineups is None:
        lineups = LineupIndex.load_or_build(tables)
    tossup_metadata = tables["tossups"].set_index("tossup_id")
    tossup_qnum = tossup_metadata["question_num"].to_dict()
    tossup_category = (
        tossup_metadata["category"].to_dict()
        if "category" in tossup_metadata
        else {}
    )
    buzzes = tables["tossup_buzzes"].copy()
    # Order by token position with deterministic buzz_id tie-breaking, then rank
    # buzzes within each event so the first buzz (and, for bouncebacks, the
    # second) can be selected by rank.
    buzzes["_buzz_order"] = buzzes["buzz_id"].str.rsplit("-", n=1).str[-1].astype(int)
    buzzes = buzzes.sort_values(
        ["game_id", "tossup_id", "token_position", "_buzz_order"]
    )
    buzzes["_event_rank"] = buzzes.groupby(["game_id", "tossup_id"]).cumcount()
    first_buzzes = buzzes[buzzes["_event_rank"] == 0]
    rows = _observed_first_buzz_rows(
        first_buzzes,
        games,
        teams,
        tournaments,
        lineups,
        tossup_qnum,
        tossup_category,
    )
    rows.extend(
        _terminal_no_buzz_rows(
            tables, games, tournaments, lineups, first_buzzes
        )
    )
    if include_bounceback:
        # A neg is the first recorded buzz with raw value -5; its bounceback is
        # the earliest later record from the opposing team, so pass every
        # post-first record (rank >= 1) and let _bounceback_rows pick it. Phase-1
        # rows are appended after phase-0 rows so any drop_duplicates('event_id')
        # downstream keeps the phase-0 representative.
        neg_first_buzzes = first_buzzes[first_buzzes["value"] == -5]
        continuation_buzzes = buzzes[buzzes["_event_rank"] >= 1]
        rows.extend(
            _bounceback_rows(
                neg_first_buzzes,
                continuation_buzzes,
                games,
                teams,
                tournaments,
                lineups,
                tossup_qnum,
                tossup_category,
            )
        )
    return pd.DataFrame(rows)


def build_bonus_part_observations(tables, lineups=None):
    """Expand each observed team bonus into binary part-level observations.

    A standard bonus has three parts worth ten points each. One response such
    as 'parts_correct=[True, False, True]' becomes three rows with targets
    '1, 0, 1'. Every row carries the answering team's inferred lineup (see
    'lineup.py'); a bonus reuses the lineup of the tossup in the same cycle
    because both resolve through the same (game, team, question -> segment)
    mapping, so the compositional aggregation and synergy run over the players
    who plausibly played that game rather than the full registered roster.
    """
    from lineup import LineupIndex

    games = tables["games"].set_index("game_id").to_dict("index")
    tournaments = tables["tournaments"].set_index("tournament_id").to_dict("index")
    bonuses = tables["bonuses"].set_index("bonus_id").to_dict("index")
    if lineups is None:
        lineups = LineupIndex.load_or_build(tables)
    rows = []
    for response in tables["bonus_responses"].itertuples(index=False):
        game = games[response.game_id]
        bonus = bonuses[response.bonus_id]
        # Reuse the tossup lineup for this cycle via the shared question number.
        roster = lineups.roster_for(
            response.game_id, response.team_id, int(bonus["question_num"])
        )
        # part_index is zero-based; IDs use one-based part numbers.
        for part_index, correct in enumerate(response.parts_correct):
            rows.append(
                {
                    "observation_id": f"{response.response_id}::part-{part_index + 1}",
                    "response_id": response.response_id,
                    "game_id": response.game_id,
                    "team_id": response.team_id,
                    "player_ids": roster,
                    "bonus_id": response.bonus_id,
                    "part_index": part_index,
                    "bonus_part_id": f"{response.bonus_id}::part-{part_index + 1}",
                    "correct": float(bool(correct)),
                    "total_points": int(response.total_points),
                    "tournament_id": game["tournament_id"],
                    "tier": tournaments[game["tournament_id"]]["tier"],
                    "category": bonus["category"],
                }
            )
    return pd.DataFrame(rows)


def tossup_tensors(observations, device="cpu"):
    """Convert readable tossup rows into tensors used by the Pyro models.

    Every tensor below has shape '(n_rows,)'; a row is one player in one
    game-tossup event. Each entity type gets its own contiguous index space.
    """
    player_ids, player_index = make_index(observations["player_id"])
    tossup_ids, tossup_index = make_index(observations["tossup_id"])
    event_ids, event_index = make_index(observations["event_id"])
    return {
        "player": torch.tensor(
            [player_index[str(value)] for value in observations["player_id"]],
            dtype=torch.long,
            device=device,
        ),
        "tossup": torch.tensor(
            [tossup_index[str(value)] for value in observations["tossup_id"]],
            dtype=torch.long,
            device=device,
        ),
        "event": torch.tensor(
            [event_index[str(value)] for value in observations["event_id"]],
            dtype=torch.long,
            device=device,
        ),
        # Survival for each row runs over the interval [t_start, t_star). Rows
        # built before the bounceback change have no t_start column, so default
        # to 1 (the historical [1, t_star) behavior).
        "t_start": torch.tensor(
            (
                observations["t_start"]
                if "t_start" in observations
                else pd.Series(1, index=observations.index)
            ).to_numpy(),
            dtype=torch.long,
            device=device,
        ),
        "t_star": torch.tensor(
            observations["t_star"].to_numpy(), dtype=torch.long, device=device
        ),
        "T_j": torch.tensor(
            observations["T_j"].to_numpy(), dtype=torch.long, device=device
        ),
        # Non-buzz rows have no label; zero-fill is safe since the model reads y
        # only where is_buzz is true.
        "y": torch.tensor(
            observations["y"].fillna(0).to_numpy(),
            dtype=torch.float32,
            device=device,
        ),
        # A "buzz" contributes hazard + correctness: the phase-0 first buzzer and
        # the phase-1 bounceback buzzer both qualify.
        "is_buzz": torch.tensor(
            observations["z"].isin(["BUZZ", "BOUNCE-BUZZ"]).to_numpy(),
            dtype=torch.bool,
            device=device,
        ),
        "is_no_buzz": torch.tensor(
            observations["z"].isin(["NO-BUZZ", "BOUNCE-NO-BUZZ"]).to_numpy(),
            dtype=torch.bool,
            device=device,
        ),
        # Phase-0 rows are the genuine full-field first-buzz risk set; first-buzz
        # timing reconstruction and PPC replay restrict to them. Absent 'phase'
        # column (pre-bounceback frames) means every row is phase 0.
        "is_phase0": torch.tensor(
            (
                observations["phase"] == 0
                if "phase" in observations
                else pd.Series(True, index=observations.index)
            ).to_numpy(),
            dtype=torch.bool,
            device=device,
        ),
        "player_ids": player_ids,
        "tossup_ids": tossup_ids,
        "event_ids": event_ids,
    }


def bonus_tensors(observations, player_ids, device="cpu"):
    """Convert bonus-part observations into indexed, padded roster tensors.

    'roster' has shape '(n_observations, max_roster_size)'; shorter rosters
    are padded with player index zero and 'roster_mask' marks the real
    entries. 'player_ids' must use the same order as the fitted tossup
    'theta' matrix; that shared indexing connects the two model stages.
    """
    if observations.empty:
        raise ValueError("Cannot build bonus tensors from an empty observation table")

    player_index = {str(value): index for index, value in enumerate(player_ids)}
    unknown_players = sorted(
        {
            str(player_id)
            for roster in observations["player_ids"]
            for player_id in roster
            if str(player_id) not in player_index
        }
    )
    if unknown_players:
        preview = ", ".join(unknown_players[:5])
        if len(unknown_players) > 5:
            preview += ", ..."
        raise ValueError(f"Bonus observations contain unknown players: {preview}")

    part_ids, part_index = make_index(observations["bonus_part_id"])
    max_roster = max(len(roster) for roster in observations["player_ids"])
    rosters = []
    roster_mask = []
    for roster in observations["player_ids"]:
        indexed_roster = [player_index[str(player_id)] for player_id in roster]
        rosters.append(indexed_roster + [0] * (max_roster - len(indexed_roster)))
        roster_mask.append(
            [True] * len(indexed_roster) + [False] * (max_roster - len(indexed_roster))
        )
    return {
        "roster": torch.tensor(rosters, dtype=torch.long, device=device),
        "roster_mask": torch.tensor(roster_mask, dtype=torch.bool, device=device),
        "part": torch.tensor(
            [part_index[str(value)] for value in observations["bonus_part_id"]],
            dtype=torch.long,
            device=device,
        ),
        "y": torch.tensor(
            observations["correct"].to_numpy(), dtype=torch.float32, device=device
        ),
        "part_ids": part_ids,
    }


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--split", default="all")
    parser.add_argument("--tournament")
    parser.add_argument(
        "--include-bounceback",
        action="store_true",
        help="add opponent-only phase-1 rows after first-buzz negs "
        "(paper Section 3.1 / Appendix A)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    tossups = build_tossup_observations(tables, include_bounceback=args.include_bounceback)
    bonuses = build_bonus_part_observations(tables)
    print(f"Tossup rows: {len(tossups):,}  events: {tossups['event_id'].nunique():,}")
    print(tossups["z"].value_counts().to_string())
    print(f"Bonus part rows: {len(bonuses):,}")
