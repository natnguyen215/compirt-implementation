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

    'split' is '"all"' or a year split such as '"year_2024"'. The
    returned dict is keyed by table name ('tables["games"]', etc.).
    """
    data_dir = Path(data_dir)
    # Each table is its own DatasetDict directory; pandas is easier to join.
    return {
        name: load_from_disk(str(data_dir / name))[split].to_pandas()
        for name in TABLES
    }


def filter_tournament(tables, tournament: str | None):
    """Return linked table copies restricted to a tournament selection.

    The value may be an exact ID or a prefix; e.g. '"2024-acf-regionals"'
    selects all 2024 Regionals mirror tournaments. Each table is filtered
    through its own foreign key so the result stays mutually consistent.
    """
    if not tournament:
        # Copy so callers cannot mutate the originals.
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


def build_tossup_observations(tables, lineups=None):
    """Build one model row per rostered player per game-tossup event.

    For a tossup with a recorded first buzz, the function emits:

    * one 'BUZZ' row for the first buzzer; its 'y' is correctness;
    * one 'CENSORED' row for every other rostered player, meaning that player
      had not buzzed before the observed first-buzz position.

    For a recoverable dead tossup, it emits one 'NO-BUZZ' row per player.
    These rows let the competing-risks model learn from nobody buzzing.

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
    tossup_qnum = tables["tossups"].set_index("tossup_id")["question_num"].to_dict()
    buzzes = tables["tossup_buzzes"].copy()
    # Order by token position, breaking ties deterministically on the numeric
    # suffix of buzz_id, then keep only each event's first buzz. Later buzzes,
    # including post-neg bounce-backs, are intentionally not modeled.
    buzzes["_buzz_order"] = buzzes["buzz_id"].str.rsplit("-", n=1).str[-1].astype(int)
    buzzes = buzzes.sort_values(
        ["game_id", "tossup_id", "token_position", "_buzz_order"]
    )
    first_buzzes = buzzes.drop_duplicates(["game_id", "tossup_id"])
    rows = []

    for buzz in first_buzzes.itertuples(index=False):
        game = games[buzz.game_id]
        # Both teams' inferred lineups for this tossup's segment compete.
        question_number = int(tossup_qnum.get(buzz.tossup_id, 1))
        roster, player_team = _event_roster(
            buzz.game_id, game, lineups, question_number
        )
        # The observed buzzer must always yield a BUZZ row even if inference
        # somehow omitted them (e.g. a buzz by a player off the roster).
        if buzz.player_id not in player_team:
            team_of = _player_team(game, teams, buzz.player_id)
            if team_of is not None:
                player_team[buzz.player_id] = team_of
                roster.append(buzz.player_id)
        # Clamp into [1, T_j]; raw_t_star keeps any source-data anomaly visible.
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
                    "raw_t_star": int(buzz.token_position),
                    "t_star": t_star,
                    "T_j": T_j,
                    "relative_position": t_star / T_j,
                    # Correctness is observed only for the buzzer.
                    "y": float(bool(buzz.correct)) if is_buzzer else float("nan"),
                    "z": "BUZZ" if is_buzzer else "CENSORED",
                    "tournament_id": game["tournament_id"],
                    "tier": tier,
                    "roster_size": len(roster),
                }
            )

    if games and "packet_id" in tables["games"].columns:
        # Dead tossups have no buzz record; recover them from each game's packet.
        tossups_by_packet = {
            packet_id: group.sort_values("question_num")
            for packet_id, group in tables["tossups"].groupby("packet")
        }
        buzzed = set(zip(first_buzzes["game_id"], first_buzzes["tossup_id"]))
        for game_id, game in games.items():
            scheduled = tossups_by_packet.get(int(game["packet_id"]))
            if scheduled is None:
                # Skip unmatched packets rather than invent tossup identities.
                continue
            # A game may end before the packet is exhausted; only count reads.
            scheduled = scheduled.iloc[: int(game["tossups_read"])]
            tier = tournaments[game["tournament_id"]]["tier"]
            for tossup in scheduled.itertuples(index=False):
                if (game_id, tossup.tossup_id) in buzzed:
                    continue
                # The dead tossup's segment follows its packet question number.
                roster, player_team = _event_roster(
                    game_id, game, lineups, int(tossup.question_num)
                )
                # Every player is observed as not buzzing before the end.
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
                            "t_star": T_j,
                            "T_j": T_j,
                            "relative_position": 1.0,
                            "y": float("nan"),
                            "z": "NO-BUZZ",
                            "tournament_id": game["tournament_id"],
                            "tier": tier,
                            "roster_size": len(roster),
                        }
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
        "is_buzz": torch.tensor(
            (observations["z"] == "BUZZ").to_numpy(),
            dtype=torch.bool,
            device=device,
        ),
        "is_no_buzz": torch.tensor(
            (observations["z"] == "NO-BUZZ").to_numpy(),
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
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    tables = filter_tournament(load_hf_tables(args.data_dir, args.split), args.tournament)
    tossups = build_tossup_observations(tables)
    bonuses = build_bonus_part_observations(tables)
    print(f"Tossup rows: {len(tossups):,}  events: {tossups['event_id'].nunique():,}")
    print(tossups["z"].value_counts().to_string())
    print(f"Bonus part rows: {len(bonuses):,}")
