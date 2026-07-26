"""Tests for the packaged seed-noise-floor evaluator."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from compirt_eval.noise_floor import evaluation
from compirt_eval.noise_floor.metrics import (
    mean_topk_jaccards,
    pairwise_agreement,
    topk_jaccards,
)
from run_scripts.multidimensional.multidim import run_multidim_noise_floor as runner


class NoiseFloorMetricTests(unittest.TestCase):
    def test_pairwise_agreement_uses_sorted_seed_pairs(self):
        rankings = {
            "7": pd.Series({"a": 1.0, "b": 2.0, "c": 3.0}),
            "123": pd.Series({"a": 1.0, "b": 3.0, "c": 2.0}),
            "42": pd.Series({"a": 1.0, "b": 2.0, "c": 3.0}),
        }
        frame = pairwise_agreement(rankings)
        self.assertEqual(
            frame[["seed_a", "seed_b"]].values.tolist(),
            [["123", "42"], ["123", "7"], ["42", "7"]],
        )
        self.assertEqual(frame["n"].tolist(), [3, 3, 3])

    def test_topk_jaccard_preserves_set_semantics(self):
        rankings = {
            "a": pd.Series({"p1": 1.0, "p2": 2.0, "p3": 3.0}),
            "b": pd.Series({"p1": 2.0, "p2": 1.0, "p3": 3.0}),
        }
        self.assertEqual(topk_jaccards(rankings, (1,))[1], [0.0])
        self.assertEqual(mean_topk_jaccards(rankings, (2,))[2], 1.0)


class NoiseFloorArtifactTests(unittest.TestCase):
    def test_seed_discovery_matches_historical_lexical_order(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for seed in (7, 123, 42):
                stage = root / f"seed_{seed}" / "pyramidal"
                stage.mkdir(parents=True)
                (stage / "players.csv").write_text("player_id\np\n")
            incomplete = root / "seed_2024" / "pyramidal"
            incomplete.mkdir(parents=True)
            found = evaluation.discover_seed_dirs(root)
        self.assertEqual([path.name for path in found], ["seed_123", "seed_42", "seed_7"])

    def test_output_table_keeps_seed_columns_then_mean_and_sorts_descending(self):
        seed_dirs = [Path("seed_123"), Path("seed_42"), Path("seed_7")]
        values = [
            pd.Series({"p1": 1.0, "p2": 5.0}),
            pd.Series({"p1": 3.0, "p2": 4.0}),
            pd.Series({"p1": 2.0, "p2": 6.0}),
        ]
        with patch.object(evaluation, "predicted_ppg", side_effect=values):
            table, ppgs = evaluation.predicted_ppg_table(seed_dirs, {}, pd.Series())
        self.assertEqual(table.columns.tolist(), ["123", "42", "7", "mean_ppg"])
        self.assertEqual(table.index.tolist(), ["p2", "p1"])
        self.assertEqual(list(ppgs), ["123", "42", "7"])


class NoiseFloorRunnerTests(unittest.TestCase):
    def test_default_runner_preserves_historical_fit_grid(self):
        args = runner.parse_args([])
        self.assertEqual(args.seeds, [42, 7, 123, 2024, 31337])
        self.assertEqual(args.gpus, ["0", "1"])
        command = runner.train_command(
            args, 42, args.root / "seed_42" / "pyramidal"
        )
        text = " ".join(command)
        self.assertIn("--split year_2024", text)
        self.assertIn("--dimensions 5", text)
        self.assertIn("--difficulty-link tanh", text)
        self.assertIn("--steps 3000", text)
        self.assertIn("--lr 0.01", text)
        self.assertIn("--device cuda", text)
        self.assertIn("--seed 42", text)

    def test_collect_only_is_an_explicit_runner_mode(self):
        args = runner.parse_args(["--collect-only"])
        self.assertTrue(args.collect_only)


if __name__ == "__main__":
    unittest.main()
