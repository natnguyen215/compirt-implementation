"""Tests for per-game lineup inference (lineup.py)."""

import unittest

import pandas as pd

from compirt_data import build_bonus_part_observations, build_tossup_observations
from lineup import LineupIndex, build_lineup_segments


def make_tables(roster, buzzes, opponent=("opp1",), bonus_questions=()):
    """Build the smallest linked tables for one game of team 'A'.

    'roster' is team A's registered players; 'buzzes' is a list of
    '(player_id, question_num)' buzzes by team A; 'bonus_questions' adds a
    team-A bonus response at each listed question number.
    """
    question_nums = sorted({q for _, q in buzzes} | set(bonus_questions)) or [1]
    tossups = pd.DataFrame(
        [
            {"tossup_id": f"q{q}", "question_num": q, "packet": 1, "tokens": ["a", "b"]}
            for q in question_nums
        ]
    )
    buzz_rows = [
        {
            "buzz_id": f"g1::buzz-{i + 1}",
            "game_id": "g1",
            "tossup_id": f"q{q}",
            "player_id": p,
            "token_position": 1,
            "num_tokens_total": 2,
            "correct": True,
        }
        for i, (p, q) in enumerate(buzzes)
    ]
    tables = {
        "tournaments": pd.DataFrame(
            [{"tournament_id": "t1", "tier": "test"}]
        ),
        "teams": pd.DataFrame(
            [
                {"team_id": "A", "player_ids": list(roster)},
                {"team_id": "B", "player_ids": list(opponent)},
            ]
        ),
        "games": pd.DataFrame(
            [{"game_id": "g1", "tournament_id": "t1", "team_ids": ["A", "B"]}]
        ),
        "tossups": tossups,
        "tossup_buzzes": pd.DataFrame(
            buzz_rows,
            columns=[
                "buzz_id",
                "game_id",
                "tossup_id",
                "player_id",
                "token_position",
                "num_tokens_total",
                "correct",
            ],
        ),
        "bonuses": pd.DataFrame(
            [
                {"bonus_id": f"b{q}", "question_num": q, "category": "history"}
                for q in bonus_questions
            ],
            columns=["bonus_id", "question_num", "category"],
        ),
        "bonus_responses": pd.DataFrame(
            [
                {
                    "response_id": f"r{q}",
                    "game_id": "g1",
                    "team_id": "A",
                    "bonus_id": f"b{q}",
                    "parts_correct": [True, False, True],
                    "total_points": 20,
                }
                for q in bonus_questions
            ],
            columns=[
                "response_id",
                "game_id",
                "team_id",
                "bonus_id",
                "parts_correct",
                "total_points",
            ],
        ),
    }
    return tables


def team_a_segment(tables, segment="whole_game"):
    """Return the (players, row) for team A's given segment."""
    df = build_lineup_segments(tables)
    row = df[(df["team_id"] == "A") & (df["segment"] == segment)].iloc[0]
    players = row["player_ids"].split("|") if row["player_ids"] else []
    return players, row


class WholeGameRules(unittest.TestCase):
    def test_small_roster_uses_entire_roster(self):
        # roster <= 4 trusts the roster even when fewer players buzzed.
        tables = make_tables(["p1", "p2", "p3", "p4"], [("p1", 1), ("p2", 2)])
        players, row = team_a_segment(tables)
        self.assertEqual(set(players), {"p1", "p2", "p3", "p4"})
        self.assertEqual(row["resolution_rule"], "whole_game_small_roster")
        self.assertFalse(bool(row["short_handed"]))

    def test_small_roster_marks_short_handed(self):
        tables = make_tables(["p1", "p2", "p3"], [("p1", 1)])
        players, row = team_a_segment(tables)
        self.assertEqual(set(players), {"p1", "p2", "p3"})
        self.assertTrue(bool(row["short_handed"]))

    def test_exact_four_game_buzzers(self):
        tables = make_tables(
            ["p1", "p2", "p3", "p4", "p5", "p6"],
            [("p1", 1), ("p2", 2), ("p3", 3), ("p4", 4)],
        )
        players, row = team_a_segment(tables)
        self.assertEqual(set(players), {"p1", "p2", "p3", "p4"})
        self.assertEqual(row["resolution_rule"], "whole_game_exact_four_buzzers")

    def test_one_to_three_buzzers_no_fill(self):
        tables = make_tables(
            ["p1", "p2", "p3", "p4", "p5", "p6"], [("p1", 1), ("p2", 2)]
        )
        players, row = team_a_segment(tables)
        self.assertEqual(set(players), {"p1", "p2"})
        self.assertEqual(row["resolution_rule"], "whole_game_short_handed")
        self.assertTrue(bool(row["short_handed"]))

    def test_zero_buzzers_falls_back_to_full_roster(self):
        roster = ["p1", "p2", "p3", "p4", "p5", "p6"]
        tables = make_tables(roster, [], opponent=("opp1",))
        # Team A never buzzes; it is the opponent that is small. Give A no buzzes.
        players, row = team_a_segment(tables)
        self.assertEqual(set(players), set(roster))
        self.assertEqual(row["resolution_rule"], "whole_game_no_evidence")


class SubstitutionSplit(unittest.TestCase):
    def _split_tables(self):
        # 5 distinct buzzers across the game -> substitution detected.
        return make_tables(
            ["p1", "p2", "p3", "p4", "p5", "p6"],
            [("p1", 1), ("p2", 2), ("p3", 11), ("p4", 12), ("p5", 13)],
        )

    def test_first_half_fills_from_second_half_buzzers(self):
        tables = self._split_tables()
        players, row = team_a_segment(tables, "first_half")
        self.assertEqual(len(players), 4)
        # First-half buzzers are always kept.
        self.assertLessEqual({"p1", "p2"}, set(players))
        # Fill comes only from second-half buzzers, never the bench (p6).
        self.assertTrue(set(players) - {"p1", "p2"} <= {"p3", "p4", "p5"})
        self.assertNotIn("p6", players)
        self.assertEqual(row["resolution_rule"], "half_substitution")

    def test_second_half_fills_from_first_half_buzzers(self):
        tables = self._split_tables()
        players, row = team_a_segment(tables, "second_half")
        self.assertEqual(len(players), 4)
        self.assertLessEqual({"p3", "p4", "p5"}, set(players))
        self.assertTrue(set(players) - {"p3", "p4", "p5"} <= {"p1", "p2"})
        self.assertNotIn("p6", players)

    def test_half_overflow_keeps_all_buzzers(self):
        # Five buzzers in the first half; one in the second.
        tables = make_tables(
            ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"],
            [
                ("p1", 1), ("p2", 2), ("p3", 3), ("p4", 4), ("p5", 5),
                ("p6", 11),
            ],
        )
        first, first_row = team_a_segment(tables, "first_half")
        self.assertEqual(set(first), {"p1", "p2", "p3", "p4", "p5"})
        self.assertEqual(int(first_row["lineup_size"]), 5)
        second, _ = team_a_segment(tables, "second_half")
        self.assertEqual(len(second), 4)
        self.assertIn("p6", second)


class Determinism(unittest.TestCase):
    def test_repeated_builds_match(self):
        tables = make_tables(
            ["p1", "p2", "p3", "p4", "p5", "p6"],
            [("p1", 1), ("p2", 2), ("p3", 11), ("p4", 12), ("p5", 13)],
        )
        first = build_lineup_segments(tables)
        second = build_lineup_segments(tables)
        pd.testing.assert_frame_equal(first, second)

    def test_seed_differs_by_segment(self):
        tables = make_tables(
            ["p1", "p2", "p3", "p4", "p5", "p6"],
            [("p1", 1), ("p2", 2), ("p3", 11), ("p4", 12), ("p5", 13)],
        )
        df = build_lineup_segments(tables)
        a = df[df["team_id"] == "A"]
        seeds = a.set_index("segment")["random_seed"].to_dict()
        self.assertNotEqual(seeds["first_half"], seeds["second_half"])


class ReuseAndInvariants(unittest.TestCase):
    def test_metadata_lookup_uses_same_segment_as_roster_lookup(self):
        tables = make_tables(
            ["p1", "p2", "p3", "p4", "p5", "p6"],
            [("p1", 1), ("p2", 2), ("p3", 11), ("p4", 12), ("p5", 13)],
        )
        index = LineupIndex.from_tables(tables)
        record = index.record_for("g1", "A", 13)

        self.assertIsNotNone(record)
        self.assertEqual(record.segment, "second_half")
        self.assertEqual(list(record.player_ids), index.roster_for("g1", "A", 13))
        self.assertEqual(record.resolution_rule, "half_substitution")
        self.assertEqual(record.distinct_game_buzzers, 5)

    def test_bonus_reuses_tossup_lineup(self):
        # Second-half bonus (q15) must match team A's second-half tossup lineup.
        tables = make_tables(
            ["p1", "p2", "p3", "p4", "p5", "p6"],
            [("p1", 1), ("p2", 2), ("p3", 11), ("p4", 12), ("p5", 15)],
            bonus_questions=[15],
        )
        lineups = LineupIndex.from_tables(tables)
        tossups = build_tossup_observations(tables, lineups)
        bonuses = build_bonus_part_observations(tables, lineups)

        tossup_lineup = set(
            tossups[(tossups["tossup_id"] == "q15") & (tossups["team_id"] == "A")][
                "player_id"
            ]
        )
        bonus_lineup = set(bonuses.iloc[0]["player_ids"])
        self.assertEqual(bonus_lineup, tossup_lineup)

    def test_every_buzzer_is_in_its_segment_and_roster(self):
        roster = ["p1", "p2", "p3", "p4", "p5", "p6"]
        tables = make_tables(
            roster,
            [("p1", 1), ("p2", 2), ("p3", 11), ("p4", 12), ("p5", 13)],
        )
        index = LineupIndex.from_tables(tables)
        first = index.roster_for("g1", "A", 3)
        second = index.roster_for("g1", "A", 13)
        self.assertLessEqual({"p1", "p2"}, set(first))
        self.assertLessEqual({"p3", "p4", "p5"}, set(second))
        self.assertLessEqual(set(first) | set(second), set(roster))


if __name__ == "__main__":
    unittest.main()
