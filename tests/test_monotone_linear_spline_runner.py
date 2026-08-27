"""Contracts for the monotone linear-spline matrix-infill runner."""

import tempfile
import unittest

from run_scripts.linear_spline.run_monotone_holdout import (
    Configuration,
    experiment_commands,
)


class MonotoneLinearSplineRunnerTests(unittest.TestCase):
    def test_commands_train_and_frozen_replay_all_requested_settings(self):
        with tempfile.TemporaryDirectory() as tmp:
            config = Configuration(
                root=tmp,
                base_split="year_2024",
                folds=list(range(5)),
                split_seed=42,
                optimization_seed=7,
                dimensions=3,
                steps=10,
                lr=0.01,
                device="cpu",
                posterior_draws=0,
                data_dir=None,
                calibrate_correctness=False,
                include_bounceback=False,
            )
            _, stages = experiment_commands(config, 4)
        train = stages[0][2]
        frozen = stages[1][2]
        evaluate = stages[2][2]
        self.assertIn("dd_linear_spline.train_monotone_pyramidal", train)
        self.assertIn("game-holdout:year_2024:train:5:4:42", train)
        self.assertEqual(train[train.index("--dimensions") + 1], "3")
        self.assertIn("holdout.frozen_predict", frozen)
        self.assertIn("game-holdout:year_2024:test:5:4:42", frozen)
        self.assertIn("run_scripts.paper_model_selection.evaluate_fold", evaluate)


if __name__ == "__main__":
    unittest.main()
