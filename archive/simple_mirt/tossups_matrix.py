"""Build a player-slug × tossup response matrix from a quiz-bowl SQLite database.

Matrix cell encoding:
    1   – player answered correctly (buzz value == 10)
    0   – player was in the game but did not convert
    NaN – player was not in any game where this tossup was read
"""

from __future__ import annotations

import sqlite3
from contextlib import contextmanager

import numpy as np
import pandas as pd


# Database connection

@contextmanager
def get_connection(db_path: str):
    """Open a SQLite connection and close it on exit."""
    conn = sqlite3.connect(db_path)
    try:
        yield conn
    finally:
        conn.close()


# Database loaders

def get_players(conn: sqlite3.Connection) -> pd.DataFrame:
    """All players joined with their team and tournament."""
    return pd.read_sql_query("""
        SELECT p.id   AS player_id,
               p.name AS player_name,
               p.slug AS player_slug,
               t.id   AS team_id,
               t.name AS team_name,
               t.tournament_id
        FROM player p
        JOIN team t ON t.id = p.team_id
        ORDER BY p.id
    """, conn)


def get_games(conn: sqlite3.Connection) -> pd.DataFrame:
    """All games with their two team slots, round, packet, and tournament."""
    return pd.read_sql_query("""
        SELECT g.id        AS game_id,
               g.round_id,
               r.number    AS round_number,
               g.tossups_read,
               g.team_one_id,
               g.team_two_id,
               r.tournament_id,
               tr.name     AS tournament_name,
               r.packet_id
        FROM game       g
        JOIN round      r  ON r.id  = g.round_id
        JOIN tournament tr ON tr.id = r.tournament_id
        ORDER BY g.id
    """, conn)


def get_buzzes(conn: sqlite3.Connection) -> pd.DataFrame:
    """All buzz records. value: 10 = correct, -5 = neg, 0 = dead buzz."""
    return pd.read_sql_query("""
        SELECT id AS buzz_id,
               player_id,
               game_id,
               tossup_id,
               buzz_position,
               value
        FROM buzz
        ORDER BY id
    """, conn)


def load_all_data(db_path: str) -> dict[str, pd.DataFrame]:
    """Open the DB once and return players, games, and buzzes as DataFrames."""
    with get_connection(db_path) as conn:
        return {
            "players": get_players(conn),
            "games":   get_games(conn),
            "buzzes":  get_buzzes(conn),
        }


# Game membership

def _player_game_membership(
    games_df: pd.DataFrame,
    players_df: pd.DataFrame,
) -> pd.DataFrame:
    """Long-form (player_id, player_slug, game_id) table derived from team rosters.

    Each game has two team slots. We normalise those into a single column,
    then join against players to expand each team into its individual members.
    """
    # Stack team_one and team_two into a single (game_id, team_id) column
    team_one = games_df[["game_id", "team_one_id"]].rename(columns={"team_one_id": "team_id"})
    team_two = games_df[["game_id", "team_two_id"]].rename(columns={"team_two_id": "team_id"})
    game_teams = pd.concat([team_one, team_two], ignore_index=True)

    # Expand team_id → individual players
    return (
        game_teams
        .merge(players_df[["player_id", "player_slug", "team_id"]], on="team_id")
        [["player_id", "player_slug", "game_id"]]
        .drop_duplicates()
    )


# Response matrix

def build_response_matrix(
    players_df: pd.DataFrame,
    buzzes_df: pd.DataFrame,
    games_df: pd.DataFrame,
    correct_value: int = 10,
) -> pd.DataFrame:
    """Build a player × tossup response matrix (index=player_slug, cols=tossup_id).

    A cell is eligible (0/1) when the player was on a roster for a game in which
    the tossup was read, and masked (NaN) otherwise.
    """
    # Long-form player ↔ game membership via team rosters
    player_game = _player_game_membership(games_df, players_df)

    # Which (game_id, tossup_id) pairs were actually read?
    # We derive this from buzz evidence rather than the packet schedule —
    # buzzes are the ground truth for what was actually played.
    tossup_games = buzzes_df[["game_id", "tossup_id"]].drop_duplicates()

    # Join player_game ↔ tossup_games on game_id to find every (player, tossup)
    # pair where the player was present. These get 0 by default; the same
    # tossup can appear in many games (shared packets), so deduplicate on
    # (player_slug, tossup_id) — we only care whether they were ever eligible.
    eligible = (
        player_game
        .merge(tossup_games, on="game_id")
        [["player_slug", "tossup_id"]]
        .drop_duplicates()
    )
    eligible["response"] = 0  # default: present but did not convert

    # Mark the eligible pairs where the player actually buzzed correctly
    correct = (
        buzzes_df
        .loc[buzzes_df["value"] == correct_value, ["player_id", "tossup_id"]]
        .merge(players_df[["player_id", "player_slug"]], on="player_id")
        [["player_slug", "tossup_id"]]
        .drop_duplicates()
        .assign(correct=1)
    )
    eligible = eligible.merge(correct, on=["player_slug", "tossup_id"], how="left")
    eligible["response"] = eligible["correct"].fillna(0).astype(int)

    # Pivot to wide format, then reindex so every player and tossup is present —
    # cells outside the eligible set become NaN (masked)
    matrix = eligible.pivot(index="player_slug", columns="tossup_id", values="response")
    matrix = matrix.reindex(
        index=players_df["player_slug"].sort_values().unique(),
        columns=buzzes_df["tossup_id"].sort_values().unique(),
    )
    matrix.index.name   = "player_slug"
    matrix.columns.name = "tossup_id"
    matrix = matrix.dropna(axis=1, how="all")
    return matrix


# Summary

def summarise_matrix(matrix: pd.DataFrame) -> pd.DataFrame:
    """Per-player stats: tossups_heard, correct, incorrect, conversion_rate."""
    tossups_heard = matrix.notna().sum(axis=1)
    correct       = (matrix == 1).sum(axis=1)
    return pd.DataFrame({
        "tossups_heard":   tossups_heard,
        "correct":         correct,
        "incorrect":       (matrix == 0).sum(axis=1),
        "conversion_rate": correct / tossups_heard.replace(0, np.nan),
    }, index=matrix.index)


# Script entry point

if __name__ == "__main__":
    import sys
    DB_PATH = sys.argv[1] if len(sys.argv) > 1 else "database.db"

    data       = load_all_data(DB_PATH)
    players_df = data["players"]
    games_df   = data["games"]
    buzzes_df  = data["buzzes"]

    print(f"{len(players_df)} players | {len(games_df)} games | {len(buzzes_df)} buzzes")

    matrix    = build_response_matrix(players_df, buzzes_df, games_df)
    eligible  = matrix.notna().sum().sum()
    correct   = (matrix == 1).sum().sum()
    matrix.to_csv("response_matrix.csv")
    print(f"\nMatrix : {matrix.shape[0]} × {matrix.shape[1]}")
    print(f"Eligible cells : {eligible:,}")
    print(f"Correct  (1)   : {correct:,}  ({100*correct/eligible:.1f}%)")
    print(f"Masked  (NaN)  : {matrix.isna().sum().sum():,}")

    summary = summarise_matrix(matrix)
    top = (
        summary[summary["tossups_heard"] >= 20]
        .sort_values("conversion_rate", ascending=False)
        .head(10)
        .merge(players_df[["player_slug", "player_name"]].drop_duplicates("player_slug"),
               left_index=True, right_on="player_slug")
        .set_index("player_slug")
    )
    print("\nTop 10 by conversion rate (min 20 tossups heard):")
    print(top[["player_name", "tossups_heard", "correct", "conversion_rate"]].to_string())
