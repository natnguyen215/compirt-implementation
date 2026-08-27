"""Tests for the stratified whole-game k-fold matrix-infill holdout."""

from __future__ import annotations

import unittest

import pandas as pd

from holdout.game_splits import (
    GameHoldoutSpec,
    game_holdout_fold_assignment,
    game_holdout_masks,
    game_holdout_split_name,
    parse_game_holdout_split,
    select_game_holdout_tables,
)


def linked_tables() -> dict[str, pd.DataFrame]:
    """Two tournaments, several rounds, two rooms per round, shared packets.

    Every player buzzes in every game and every game reuses the same tossup and
    bonus per room, so coverage is easy to satisfy: this lets the fold and
    stratification tests run without the coverage pass pulling everything back
    into train.
    """
    games, buzzes, responses = [], [], []
    for tournament_id, round_count in (("t1", 10), ("t2", 6)):
        for round_number in range(1, round_count + 1):
            for room in ("a", "b"):
                game_id = f"{tournament_id}-r{round_number}-{room}"
                players = [f"{tournament_id}-{room}-p1", f"{tournament_id}-{room}-p2"]
                games.append(
                    {
                        "game_id": game_id,
                        "tournament_id": tournament_id,
                        "round": f"round{round_number}",
                        "packet_id": round_number,
                        "team_ids": [f"{tournament_id}-{room}1", f"{tournament_id}-{room}2"],
                    }
                )
                # Every player buzzes the shared per-room tossup.
                for player in players:
                    buzzes.append(
                        {
                            "buzz_id": f"z-{game_id}-{player}",
                            "game_id": game_id,
                            "tossup_id": f"q-{tournament_id}-{room}",
                            "player_id": player,
                        }
                    )
                responses.append(
                    {
                        "response_id": f"b-{game_id}",
                        "game_id": game_id,
                        "bonus_id": f"p-{tournament_id}-{room}",
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
                {"team_id": team, "tournament_id": team.split("-")[0], "player_ids": []}
                for team in teams
            ]
        ),
        "games": pd.DataFrame(games),
        "tossup_buzzes": pd.DataFrame(buzzes),
        "bonus_responses": pd.DataFrame(responses),
        "tossups": pd.DataFrame(
            [
                {"tossup_id": "q-t1-a", "question_set_event_id": "qse1"},
                {"tossup_id": "q-t1-b", "question_set_event_id": "qse1"},
                {"tossup_id": "q-t2-a", "question_set_event_id": "qse2"},
                {"tossup_id": "q-t2-b", "question_set_event_id": "qse2"},
            ]
        ),
        "bonuses": pd.DataFrame(
            [
                {"bonus_id": "p-t1-a", "question_set_event_id": "qse1"},
                {"bonus_id": "p-t1-b", "question_set_event_id": "qse1"},
                {"bonus_id": "p-t2-a", "question_set_event_id": "qse2"},
                {"bonus_id": "p-t2-b", "question_set_event_id": "qse2"},
            ]
        ),
    }


class GameHoldoutSplitTests(unittest.TestCase):
    def test_split_name_round_trip_and_validation(self):
        name = game_holdout_split_name("year_2024", "test", 5, 0, 42)
        self.assertEqual(name, "game-holdout:year_2024:test:5:0:42")
        spec = parse_game_holdout_split(name)
        self.assertEqual(spec, GameHoldoutSpec("year_2024", "test", 5, 0, 42))
        self.assertIsNone(parse_game_holdout_split("year_2024"))
        with self.assertRaisesRegex(ValueError, "fold_index"):
            game_holdout_split_name("all", "test", 5, 5, 42)
        with self.assertRaisesRegex(ValueError, "at least 2"):
            game_holdout_split_name("all", "test", 1, 0, 42)

    def test_fold_assignment_tiles_games_and_is_deterministic(self):
        games = linked_tables()["games"]
        first = game_holdout_fold_assignment(games, 5, 42)
        second = game_holdout_fold_assignment(games, 5, 42)
        self.assertTrue(first.equals(second))
        self.assertEqual(set(first.unique()) <= set(range(5)), True)
        # Every game lands in exactly one fold, so the five test masks tile all games.
        union = set()
        for fold in range(5):
            union |= set(games.loc[first == fold, "game_id"])
        self.assertEqual(union, set(games["game_id"]))
        # The continuous deal balances fold sizes to within one game, so no fold
        # is starved (the bug where small groups piled onto fold 0).
        sizes = first.value_counts()
        self.assertLessEqual(int(sizes.max() - sizes.min()), 1)

    def test_fold_assignment_spreads_each_round_group_across_folds(self):
        games = linked_tables()["games"]
        assignment = game_holdout_fold_assignment(games, 5, 42)
        # Within one (tournament, round) group there are only two games, so no
        # fold can hold both; the deal is round-robin, hence distinct folds.
        grouped = games.assign(fold=assignment.to_numpy()).groupby(
            ["tournament_id", "round"]
        )["fold"]
        for _, folds in grouped:
            self.assertEqual(len(set(folds)), len(folds))

    def test_masks_are_whole_game_and_coverage_guaranteed(self):
        tables = linked_tables()
        spec = parse_game_holdout_split("game-holdout:all:test:5:0:42")
        held_out = game_holdout_masks(tables, spec)
        test_games = set(tables["games"].loc[held_out, "game_id"])
        train_games = set(tables["games"].loc[~held_out, "game_id"])

        self.assertFalse(test_games & train_games)
        self.assertTrue(test_games)  # coverage did not empty the fold
        # Every test game's players/tossups/bonuses also appear in training.
        train_players = set(
            tables["tossup_buzzes"][
                tables["tossup_buzzes"]["game_id"].isin(train_games)
            ]["player_id"]
        )
        train_tossups = set(
            tables["tossup_buzzes"][
                tables["tossup_buzzes"]["game_id"].isin(train_games)
            ]["tossup_id"]
        )
        train_bonuses = set(
            tables["bonus_responses"][
                tables["bonus_responses"]["game_id"].isin(train_games)
            ]["bonus_id"]
        )
        test_buzzes = tables["tossup_buzzes"][
            tables["tossup_buzzes"]["game_id"].isin(test_games)
        ]
        self.assertTrue(set(test_buzzes["player_id"]) <= train_players)
        self.assertTrue(set(test_buzzes["tossup_id"]) <= train_tossups)
        test_responses = tables["bonus_responses"][
            tables["bonus_responses"]["game_id"].isin(test_games)
        ]
        self.assertTrue(set(test_responses["bonus_id"]) <= train_bonuses)

    def test_select_tables_are_disjoint_and_keep_linked_outcomes(self):
        tables = linked_tables()
        train = select_game_holdout_tables(
            tables, parse_game_holdout_split("game-holdout:all:train:5:0:42")
        )
        test = select_game_holdout_tables(
            tables, parse_game_holdout_split("game-holdout:all:test:5:0:42")
        )
        train_games = set(train["games"]["game_id"])
        test_games = set(test["games"]["game_id"])
        self.assertFalse(train_games & test_games)
        self.assertEqual(train_games | test_games, set(tables["games"]["game_id"]))
        for outcome_table in ("tossup_buzzes", "bonus_responses"):
            self.assertTrue(set(test[outcome_table]["game_id"]) <= test_games)


if __name__ == "__main__":
    unittest.main()
