"""Tests for the supervised-LDA correctness response aggregation."""

from __future__ import annotations

import unittest

import pandas as pd

from topic.learned.slda_responses import (
    bonus_responses,
    tossup_buzz_positions,
    tossup_responses,
)


def tossup_frame(rows) -> pd.DataFrame:
    return pd.DataFrame(
        rows, columns=["tossup_id", "event_id", "z", "y", "relative_position"]
    )


class TossupResponseTests(unittest.TestCase):
    def test_conversion_rate_counts_reads_not_buzzes(self):
        # T1: two reads, one correct buzz -> 0.5. T2: one dead read -> 0.0.
        # T3: one correct buzz -> 1.0. Censored rows must not change the count.
        frame = tossup_frame(
            [
                ("T1", "T1::g1", "BUZZ", 1.0, 0.4),
                ("T1", "T1::g1", "CENSORED", float("nan"), 0.4),
                ("T1", "T1::g2", "BUZZ", 0.0, 0.7),
                ("T2", "T2::g1", "NO-BUZZ", float("nan"), 1.0),
                ("T3", "T3::g1", "BUZZ", 1.0, 0.2),
            ]
        )
        self.assertEqual(
            tossup_responses(frame), {"T1": 0.5, "T2": 0.0, "T3": 1.0}
        )

    def test_keys_are_strings_and_values_in_unit_interval(self):
        frame = tossup_frame([("T1", "T1::g1", "BUZZ", 1.0, 0.3)])
        result = tossup_responses(frame)
        self.assertEqual(list(result), ["T1"])
        self.assertTrue(all(0.0 <= value <= 1.0 for value in result.values()))

    def test_empty_frame_returns_empty_map(self):
        self.assertEqual(tossup_responses(tossup_frame([])), {})

    def test_buzz_positions_average_only_buzz_rows(self):
        frame = tossup_frame(
            [
                ("T1", "T1::g1", "BUZZ", 1.0, 0.4),
                ("T1", "T1::g2", "BUZZ", 0.0, 0.6),
                ("T1", "T1::g1", "CENSORED", float("nan"), 0.4),
                ("T2", "T2::g1", "NO-BUZZ", float("nan"), 1.0),
            ]
        )
        positions = tossup_buzz_positions(frame)
        self.assertAlmostEqual(positions["T1"], 0.5)
        self.assertNotIn("T2", positions)  # no buzz rows -> no entry


class BonusResponseTests(unittest.TestCase):
    def test_part_correctness_rate_over_all_parts(self):
        # B1 across two responses: [1,0,1] and [1,1,0] -> 4/6.
        frame = pd.DataFrame(
            {
                "bonus_id": ["B1"] * 6 + ["B2"] * 3,
                "correct": [1.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            }
        )
        result = bonus_responses(frame)
        self.assertAlmostEqual(result["B1"], 4 / 6)
        self.assertEqual(result["B2"], 0.0)
        self.assertIsInstance(next(iter(result)), str)

    def test_empty_frame_returns_empty_map(self):
        self.assertEqual(bonus_responses(pd.DataFrame({"bonus_id": [], "correct": []})), {})


if __name__ == "__main__":
    unittest.main()
