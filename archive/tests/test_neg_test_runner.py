"""Check that neg-test evaluation uses the held-out fit and its output directory."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from neg_test.run_neg_test import evaluate_stage


class NegTestRunnerTests(unittest.TestCase):
    def test_evaluator_is_routed_beside_the_heldout_fit(self):
        with tempfile.TemporaryDirectory() as tmp:
            holdout = Path(tmp) / "fold0" / "holdout" / "pyramidal"

            with patch("neg_test.run_neg_test.run_logged") as run_logged:
                evaluate_stage(holdout)

            command = run_logged.call_args.args[0]
            self.assertEqual(
                command[1:3], ["-m", "run_scripts.paper_model_selection.evaluate_fold"]
            )
            self.assertEqual(
                command[-4:],
                [
                    "--pyramidal-results",
                    str(holdout),
                    "--output-dir",
                    str(holdout.parent / "evaluation"),
                ],
            )


if __name__ == "__main__":
    unittest.main()
