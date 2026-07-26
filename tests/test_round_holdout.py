"""Tests for final-fraction-of-rounds linked-data holdouts."""

from __future__ import annotations

import os
import unittest
from unittest.mock import patch

import pandas as pd

from holdout.round_splits import (
    parse_round_holdout_split,
    round_holdout_game_mask,
    round_holdout_split_name,
    select_round_holdout_tables,
)
from run_scripts.common import run_compirt_round_holdout as runner


def linked_tables() -> dict[str, pd.DataFrame]:
    """Create two tournaments with enough linked rows to test filtering."""
    games = []
    buzzes = []
    responses = []
    for tournament_id, round_count in (("t1", 10), ("t2", 6)):
        for round_number in range(1, round_count + 1):
            # Two simultaneous games prove that round boundaries stay intact.
            for room in ("a", "b"):
                game_id = f"{tournament_id}-r{round_number}-{room}"
                games.append(
                    {
                        "game_id": game_id,
                        "tournament_id": tournament_id,
                        "round": f"round{round_number}",
                        "packet_id": round_number,
                        "team_ids": [f"{tournament_id}-{room}1", f"{tournament_id}-{room}2"],
                    }
                )
                buzzes.append({"buzz_id": f"z-{game_id}", "game_id": game_id})
                responses.append(
                    {"response_id": f"b-{game_id}", "game_id": game_id}
                )
    # An unnumbered game is test-only because its temporal position is unknown.
    games.append(
        {
            "game_id": "t2-unknown",
            "tournament_id": "t2",
            "round": "roundNone",
            "packet_id": 99,
            "team_ids": ["t2-a1", "t2-a2"],
        }
    )
    teams = sorted({team for game in games for team in game["team_ids"]})
    return {
        "tournaments": pd.DataFrame(
            [
                {"tournament_id": "t1", "question_set_event_id": "qse1"},
                {"tournament_id": "t2", "question_set_event_id": "qse2"},
            ]
        ),
        "teams": pd.DataFrame(
            [
                {
                    "team_id": team,
                    "tournament_id": team.split("-")[0],
                    "player_ids": [],
                }
                for team in teams
            ]
        ),
        "games": pd.DataFrame(games),
        "tossup_buzzes": pd.DataFrame(buzzes),
        "bonus_responses": pd.DataFrame(responses),
        "tossups": pd.DataFrame(
            [
                {"tossup_id": "q1", "question_set_event_id": "qse1"},
                {"tossup_id": "q2", "question_set_event_id": "qse2"},
            ]
        ),
        "bonuses": pd.DataFrame(
            [
                {"bonus_id": "p1", "question_set_event_id": "qse1"},
                {"bonus_id": "p2", "question_set_event_id": "qse2"},
            ]
        ),
    }


class RoundHoldoutTests(unittest.TestCase):
    def test_split_name_round_trip_and_validation(self):
        name = round_holdout_split_name("year_2024", "test", 0.2)
        self.assertEqual(name, "round-holdout:year_2024:test:0.2")
        spec = parse_round_holdout_split(name)
        self.assertEqual(spec.base_split, "year_2024")
        self.assertEqual(spec.part, "test")
        self.assertEqual(spec.fraction, 0.2)
        self.assertIsNone(parse_round_holdout_split("year_2024"))
        with self.assertRaisesRegex(ValueError, "strictly between"):
            round_holdout_split_name("all", "test", 1.0)

    def test_final_twenty_percent_uses_whole_rounds_and_ceiling(self):
        games = linked_tables()["games"]
        held_out = games[round_holdout_game_mask(games, 0.2)]

        t1_rounds = set(held_out.loc[held_out.tournament_id.eq("t1"), "round"])
        t2_rounds = set(held_out.loc[held_out.tournament_id.eq("t2"), "round"])
        self.assertEqual(t1_rounds, {"round9", "round10"})
        # ceil(6 * .2) = 2, plus the conservatively held-out unknown game.
        self.assertEqual(t2_rounds, {"round5", "round6", "roundNone"})
        self.assertEqual(
            held_out.groupby(["tournament_id", "round"]).size().loc[("t1", "round9")],
            2,
        )

    def test_train_and_test_are_disjoint_and_keep_linked_outcomes(self):
        tables = linked_tables()
        train = select_round_holdout_tables(tables, "train", 0.2)
        test = select_round_holdout_tables(tables, "test", 0.2)
        train_games = set(train["games"]["game_id"])
        test_games = set(test["games"]["game_id"])

        self.assertFalse(train_games & test_games)
        self.assertEqual(train_games | test_games, set(tables["games"]["game_id"]))
        for outcome_table in ("tossup_buzzes", "bonus_responses"):
            self.assertTrue(set(train[outcome_table]["game_id"]) <= train_games)
            self.assertTrue(set(test[outcome_table]["game_id"]) <= test_games)
        self.assertNotIn("t2-unknown", train_games)
        self.assertIn("t2-unknown", test_games)

    def test_wrapper_configures_existing_holdout_runner(self):
        with patch.dict(
            os.environ,
            {
                "BASE_SPLIT": "year_2024",
                "ROUND_HOLDOUT_FRACTION": "0.2",
                "MODEL": "multidim",
            },
            clear=True,
        ):
            train_split, test_split = runner.configure_round_holdout()
            self.assertEqual(
                train_split, "round-holdout:year_2024:train:0.2"
            )
            self.assertEqual(test_split, "round-holdout:year_2024:test:0.2")
            self.assertIn("final-round-fraction/multidim", os.environ["ROOT"])

    def test_wrapper_rejects_conflicting_explicit_splits(self):
        with patch.dict(os.environ, {"TRAIN_SPLIT": "year_2024"}, clear=True):
            with self.assertRaisesRegex(SystemExit, "derives TRAIN_SPLIT"):
                runner.configure_round_holdout()


if __name__ == "__main__":
    unittest.main()
