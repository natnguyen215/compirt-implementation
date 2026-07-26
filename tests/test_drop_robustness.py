"""Tests for the data-dropping helpers, selectors, and robustness runners."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import pandas as pd

from run_scripts.common import run_drop_robustness as tier1
from run_scripts.common import run_targeted_drop as tier2
from compirt_eval.drop_robustness.perturbations import (
    drop_tossup_events,
    load_event_drop_list,
    random_drop_events,
    rank_events_for_target,
    select_drop_events,
    write_drop_list,
)
from compirt_eval.drop_robustness.figures import (
    save_targeted_outputs,
    save_tier1_outputs,
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
        # Prefix lists are nested by construction.
        self.assertEqual(select_drop_events(frame, "a", "demote", 1), ["e3"])
        self.assertEqual(select_drop_events(frame, "a", "demote", 2), ["e3", "e1"])
        with self.assertRaises(ValueError):
            select_drop_events(frame, "a", "demote", 3)


def tier1_args(root: Path) -> SimpleNamespace:
    return SimpleNamespace(
        root=root,
        python=Path(".venv/bin/python"),
        data_dir=None,
        tournament=None,
        split="year_2024",
        models=["plain", "baseline", "multidim"],
        fractions=[0.01],
        replicates=2,
        noise_seeds=[7],
        seed=42,
        drop_seed=2025,
        difficulty_link="sigmoid",
        dimensions=None,
        steps=None,
        lr=None,
        device="cuda",
    )


class Tier1CommandTests(unittest.TestCase):
    def test_full_fit_has_no_drop_flag_and_cells_do(self):
        with tempfile.TemporaryDirectory() as directory:
            args = tier1_args(Path(directory))
            stages = tier1.build_stages(args)

        by_name = {stage.name: " ".join(stage.command) for stage in stages}
        self.assertNotIn("--drop-events", by_name["multidim-full"])
        cell = by_name["multidim-frac0.01-rep1"]
        self.assertIn("--drop-events", cell)
        self.assertIn("droplists/frac_0.01/rep_1.txt", cell)
        self.assertIn("--seed 42", cell)
        # The noise fit uses the alternate seed on full data.
        noise = by_name["multidim-noise-seed7"]
        self.assertIn("--seed 7", noise)
        self.assertNotIn("--drop-events", noise)

    def test_family_invocation_forms_and_defaults(self):
        with tempfile.TemporaryDirectory() as directory:
            stages = tier1.build_stages(tier1_args(Path(directory)))

        by_name = {stage.name: " ".join(stage.command) for stage in stages}
        baseline = by_name["baseline-full"]
        self.assertIn("train_pyramidal.py", baseline.split()[1])
        self.assertNotIn("-m", baseline.split())
        self.assertIn("--steps 5000", baseline)
        self.assertIn("--lr 0.005", baseline)
        multidim = by_name["multidim-full"]
        self.assertIn("-m multidimensional.multidim_mirt.train_pyramidal", multidim)
        self.assertIn("--difficulty-link sigmoid", multidim)
        self.assertIn("--steps 3000", multidim)
        plain = by_name["plain-full"]
        self.assertIn("-m simple_mirt.train_plain_irt", plain)
        self.assertIn("--dimensions 1", plain)

    def test_global_overrides_apply_to_every_family(self):
        with tempfile.TemporaryDirectory() as directory:
            args = tier1_args(Path(directory))
            args.steps = 30
            stages = tier1.build_stages(args)

        for stage in stages:
            self.assertIn("--steps 30", " ".join(stage.command))

    def test_stage_count_matches_the_grid(self):
        with tempfile.TemporaryDirectory() as directory:
            stages = tier1.build_stages(tier1_args(Path(directory)))
        # Per family: 1 full + 1 noise seed + 1 fraction x 2 replicates.
        self.assertEqual(len(stages), 3 * (1 + 1 + 2))


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


class DropArtifactTests(unittest.TestCase):
    def test_tier1_keeps_canonical_csv_and_graph_names(self):
        frame = pd.DataFrame(
            [
                {"model": "baseline", "fraction": 0.0, "kendall_tau": 0.9, "jaccard_top10": 0.8},
                {"model": "baseline", "fraction": 0.01, "kendall_tau": 0.8, "jaccard_top10": 0.7},
                {"model": "actual", "fraction": 0.01, "kendall_tau": 0.95, "jaccard_top10": 0.9},
            ]
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output = save_tier1_outputs(root, frame)
            self.assertEqual(output, root / "csvs" / "drop_robustness_metrics.csv")
            self.assertTrue((root / "graphs" / "kendall_tau_vs_fraction.png").exists())
            self.assertTrue((root / "graphs" / "topk_jaccard_vs_fraction.png").exists())

    def test_targeted_keeps_canonical_csv_and_graph_names(self):
        frame = pd.DataFrame(
            [
                {"model": "baseline", "n_dropped": 0, "gap": 1.0, "noise_gap_std": 0.1},
                {"model": "baseline", "n_dropped": 5, "gap": -0.2, "noise_gap_std": 0.1},
            ]
        )
        actual = pd.DataFrame(
            [{"n_dropped": 0, "gap": 1.0}, {"n_dropped": 1, "gap": 0.5}]
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            save_targeted_outputs(root, frame, actual)
            self.assertTrue((root / "csvs" / "targeted_flip_metrics.csv").exists())
            self.assertTrue((root / "csvs" / "actual_flip_curve.csv").exists())
            self.assertTrue((root / "graphs" / "gap_vs_dropped.png").exists())


if __name__ == "__main__":
    unittest.main()
