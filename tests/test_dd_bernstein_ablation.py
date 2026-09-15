"""Contracts for the full double-Bernstein matrix-infill grid runner."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from run_scripts.double_difficulty.run_dd_bernstein_ablation import (
    Configuration,
    concentration_label,
    experiment_commands,
    point_dir,
)


def _config(root: Path) -> Configuration:
    return Configuration(
        root=str(root),
        base_split="year_2024",
        folds=[0, 1, 2, 3, 4],
        split_seed=42,
        optimization_seed=42,
        degrees=[3, 4, 5, 6],
        dimensions=[1, 2, 3, 4, 5],
        drop_concentrations=[0.67, 1.0, 1.33, 1.66, 2.0],
        relevance_prior="gamma",
        learned_curve_locations=False,
        terminal_intercepts=True,
        steps=3000,
        lr=0.005,
        device="cuda",
        posterior_draws=0,
        data_dir=None,
    )


class DoubleBernsteinAblationTests(unittest.TestCase):
    def test_paths_distinguish_dirichlet_values(self):
        root = Path("/tmp/results")
        paths = {point_dir(root, 3, 1, value) for value in (0.67, 1.0, 1.33, 1.66, 2.0)}
        self.assertEqual(len(paths), 5)
        self.assertEqual(concentration_label(0.67), "0p67")

    def test_commands_match_frozen_tossup_matrix_infill_protocol(self):
        with tempfile.TemporaryDirectory() as tmp:
            config = _config(Path(tmp))
            _, stages = experiment_commands(config, 6, 4, 1.33, 2)
        train = stages[0][2]
        frozen = stages[1][2]
        evaluate = stages[2][2]
        self.assertIn("hazard_double_difficulty.bernstein.train_pyramidal", train)
        self.assertEqual(train[train.index("--degree") + 1], "6")
        self.assertEqual(train[train.index("--dimensions") + 1], "4")
        self.assertEqual(train[train.index("--drop-concentration") + 1], "1.33")
        self.assertEqual(train[train.index("--relevance-prior") + 1], "gamma")
        self.assertEqual(train[train.index("--posterior-draws") + 1], "0")
        self.assertIn("game-holdout:year_2024:train:5:2:42", train)
        self.assertIn("holdout.frozen_predict", frozen)
        self.assertIn("game-holdout:year_2024:test:5:2:42", frozen)
        self.assertIn("run_scripts.double_difficulty.evaluate_fold", evaluate)


if __name__ == "__main__":
    unittest.main()
