"""Unit tests for public-standings ranking metrics."""

from __future__ import annotations

import sqlite3
import tempfile
import unittest
from pathlib import Path

from compare_player_rankings import actual_tournament_stats, tournament_overlap_summary


class ActualTournamentStatsTests(unittest.TestCase):
    def make_database(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        directory = tempfile.TemporaryDirectory()
        database = Path(directory.name) / "stats.db"
        connection = sqlite3.connect(database)
        try:
            connection.executescript(
                """
                create table tournament (id integer primary key, slug text);
                create table round (
                    id integer primary key, tournament_id integer,
                    exclude_from_individual integer default 0
                );
                create table team (id integer primary key, name text);
                create table game (
                    id integer primary key, round_id integer, tossups_read integer,
                    team_one_id integer, team_two_id integer
                );
                create table player (
                    id integer primary key, team_id integer, name text, slug text
                );
                create table buzz (
                    id integer primary key, player_id integer, game_id integer,
                    value integer
                );
                insert into tournament values (1, 'sample');
                insert into round values (1, 1, 0);
                insert into team values (1, 'Alpha'), (2, 'Beta'), (3, 'Gamma');
                insert into game values
                    (1, 1, 10, 1, 2), (2, 1, 20, 1, 3), (3, 1, 20, 1, 3);
                insert into player values
                    (1, 1, 'High PPG', 'high-ppg'),
                    (2, 2, 'High PP20', 'high-pp20');
                insert into buzz values
                    (1, 1, 1, 70), (2, 1, 2, 70), (3, 1, 3, 70),
                    (4, 2, 1, 45);
                """
            )
            connection.commit()
        finally:
            connection.close()
        return directory, database

    def test_default_ppg_ranking_matches_public_standings_convention(self):
        temporary, database = self.make_database()
        with temporary:
            rows = actual_tournament_stats(database, "sample", min_games=1, min_tuh=1)

        self.assertEqual([row["player_id"] for row in rows], ["high-ppg", "high-pp20"])
        self.assertEqual([row["actual_ppg"] for row in rows], [70.0, 45.0])
        self.assertEqual([row["actual_pp20"] for row in rows], [84.0, 90.0])

    def test_pp20_mode_remains_available(self):
        temporary, database = self.make_database()
        with temporary:
            rows = actual_tournament_stats(
                database, "sample", min_games=1, min_tuh=1, rank_mode="pp20"
            )

        self.assertEqual([row["player_id"] for row in rows], ["high-pp20", "high-ppg"])

    def test_minimum_game_tossups_excludes_incomplete_games_separately(self):
        temporary, database = self.make_database()
        with temporary:
            rows = actual_tournament_stats(
                database,
                "sample",
                min_games=1,
                min_tuh=1,
                min_game_tossups=20,
            )

        self.assertEqual([row["player_id"] for row in rows], ["high-ppg"])

    def test_overlap_summary_keeps_only_like_for_like_tournament_metrics(self):
        metrics = tournament_overlap_summary(
            [
                {
                    "player_id": "a",
                    "actual_rank": 1,
                    "global_model_rank": 200,
                    "tournament_model_rank": 1,
                },
                {
                    "player_id": "b",
                    "actual_rank": 21,
                    "global_model_rank": 1,
                    "tournament_model_rank": 50,
                },
            ]
        )

        self.assertEqual(
            metrics,
            {
                "actual_top_20_in_tournament_model_rank_top_20": "1/20",
                "actual_top_50_in_tournament_model_rank_top_50": "2/50",
            },
        )
