"""Tests for the data-dropping helpers and target selectors."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd

from run_scripts.common import run_targeted_drop as tier2
from compirt_eval.drop_robustness.perturbations import (
    drop_tossup_events,
    load_event_drop_list,
    random_drop_events,
    rank_events_for_target,
    write_drop_list,
)


def observation_frame() -> pd.DataFrame:
    """Three events: e1 has two rows, e2 one, e3 three (like BUZZ+CENSORED)."""
    return pd.DataFrame(
        {
            "event_id": ["e1", "e1", "e2", "e3", "e3", "e3"],
            "player_id": ["a", "b", "a", "a", "b", "c"],
            "z": ["BUZZ", "CENSORED", "BUZZ", "BUZZ", "CENSORED", "CENSORED"],
            "y": [1, 0, 0, 1, 0, 0],
            "relative_position": [0.5, 0.5, 0.1, 0.2, 0.2, 0.2],
        }
    )


class EventDropTests(unittest.TestCase):
    def test_drop_removes_every_row_of_the_listed_events(self):
        filtered, info = drop_tossup_events(observation_frame(), ["e1"])
        self.assertEqual(sorted(filtered["event_id"].unique()), ["e2", "e3"])
        self.assertEqual(info["dropped_events"], 1)
        self.assertEqual(info["dropped_rows"], 2)
        self.assertEqual(info["remaining_events"], 2)
        self.assertEqual(info["remaining_rows"], 4)
        self.assertEqual(list(filtered.index), list(range(4)))

    def test_unknown_event_id_raises(self):
        with self.assertRaises(ValueError):
            drop_tossup_events(observation_frame(), ["e1", "missing"])

    def test_dropping_everything_raises(self):
        with self.assertRaises(ValueError):
            drop_tossup_events(observation_frame(), ["e1", "e2", "e3"])

    def test_drop_list_file_roundtrip_skips_blanks_comments_duplicates(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "lists" / "drop.txt"
            write_drop_list(path, ["e2", "e1"])
            text = path.read_text() + "\n# comment\n\ne2\n"
            path.write_text(text)
            self.assertEqual(load_event_drop_list(path), ["e2", "e1"])


class DropSelectionTests(unittest.TestCase):
    def test_random_drop_is_deterministic_and_floor_sized(self):
        frame = pd.DataFrame({"event_id": [f"e{i}" for i in range(100)]})
        first = random_drop_events(frame, 0.05, np.random.default_rng(7))
        second = random_drop_events(frame, 0.05, np.random.default_rng(7))
        self.assertEqual(first, second)
        self.assertEqual(len(first), 5)
        self.assertTrue(set(first) <= set(frame["event_id"]))
        # Tiny fractions still drop at least one event.
        self.assertEqual(len(random_drop_events(frame, 0.001, np.random.default_rng(7))), 1)

    def test_demote_ranks_earliest_correct_buzzes_first(self):
        frame = pd.DataFrame(
            {
                "event_id": ["e1", "e2", "e3", "e4", "e5"],
                "player_id": ["a", "a", "a", "a", "b"],
                "z": ["BUZZ", "BUZZ", "BUZZ", "CENSORED", "BUZZ"],
                "y": [1, 0, 1, 1, 1],
                "relative_position": [0.6, 0.1, 0.2, 0.05, 0.01],
            }
        )
        ranked = rank_events_for_target(frame, "a", "demote")
        # Only a's correct BUZZ rows, earliest position first; e4 is censored
        # (not a's buzz) and e5 belongs to another player.
        self.assertEqual(ranked["event_id"].tolist(), ["e3", "e1"])
        promoted = rank_events_for_target(frame, "a", "promote")
        self.assertEqual(promoted["event_id"].tolist(), ["e2"])


class TargetedPairTests(unittest.TestCase):
    def test_default_pair_is_smallest_gap_in_top10(self):
        ppg = pd.Series(
            {f"p{i}": 100.0 - 10 * i for i in range(15)}
        )
        ppg["p3"] = ppg["p2"] - 0.1  # closest adjacent pair: p2 vs p3
        args = SimpleNamespace(target_player=None, target_rank=None, rival=None)
        target, rival = tier2.resolve_pair(args, ppg)
        self.assertEqual((target, rival), ("p2", "p3"))

    def test_explicit_rank_and_rival_defaults(self):
        ppg = pd.Series({"a": 3.0, "b": 2.0, "c": 1.0})
        args = SimpleNamespace(target_player=None, target_rank=2, rival=None)
        self.assertEqual(tier2.resolve_pair(args, ppg), ("b", "c"))
        args = SimpleNamespace(target_player="a", target_rank=None, rival="c")
        self.assertEqual(tier2.resolve_pair(args, ppg), ("a", "c"))

    def test_unknown_target_raises(self):
        ppg = pd.Series({"a": 3.0, "b": 2.0})
        args = SimpleNamespace(target_player="zz", target_rank=None, rival=None)
        with self.assertRaises(ValueError):
            tier2.resolve_pair(args, ppg)


if __name__ == "__main__":
    unittest.main()
