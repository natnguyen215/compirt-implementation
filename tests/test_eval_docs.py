"""Tests for CompIRT eval docs helpers."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import pandas as pd

from compirt_eval.eval_docs import (
    result_root_for_evaluation,
    write_eval_docs_summary,
)


class EvalDocsTests(unittest.TestCase):
    def test_write_eval_docs_summary_combines_metrics_parameters_and_deltas(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "results" / "compirt" / "in_sample" / "all2024"
            evaluation = root / "synergy-evaluation"
            csvs = evaluation / "csvs"
            csvs.mkdir(parents=True)
            (root / "pyramidal").mkdir()
            (root / "synergy").mkdir()
            (root / "comparison").mkdir()

            (root / "pyramidal" / "summary.json").write_text(
                '{"model": "multidim", "formula": "unused", "dimensions": 2, '
                '"topic_dimensions": 2, "steps": 7, "calibrate_correctness": false}',
                encoding="utf-8",
            )
            (root / "synergy" / "summary.json").write_text(
                '{"use_synergy": true, "saved_synergy_details": true, '
                '"skill_dimensions": 2, "synergy_dimensions": 3, "tau": 0.4, '
                '"mean_synergy_contribution": -0.1}',
                encoding="utf-8",
            )
            pd.DataFrame(
                [
                    {
                        "auc": 0.91,
                        "log_loss": 0.33,
                        "ece": 0.02,
                        "part_accuracy": 0.86,
                        "exact_acc": 0.61,
                        "ppb_mae": 1.7,
                    }
                ]
            ).to_csv(csvs / "bonus_metrics.csv", index=False)
            pd.DataFrame(
                [
                    {
                        "auc": 0.72,
                        "log_loss": 0.55,
                        "ece": 0.04,
                        "buzz_position_mae": 0.12,
                    }
                ]
            ).to_csv(csvs / "tossup_metrics.csv", index=False)
            pd.DataFrame(
                [
                    {"group": "player", "parameter": "c", "observations": 2, "mean": 1.0},
                    {
                        "group": "tossup",
                        "parameter": "beta_2",
                        "observations": 2,
                        "mean": -0.2,
                    },
                ]
            ).to_csv(
                csvs / "pyramidal_parameter_distribution_summary.csv", index=False
            )
            pd.DataFrame(
                [
                    {
                        "group": "bonus_part",
                        "parameter": "alpha_2",
                        "observations": 3,
                        "mean": 0.7,
                    },
                    {
                        "group": "synergy_player",
                        "parameter": "psi_1",
                        "observations": 3,
                        "mean": -0.3,
                    },
                ]
            ).to_csv(csvs / "bonus_parameter_distribution_summary.csv", index=False)
            pd.DataFrame(
                [
                    {
                        "metric": "log_loss",
                        "no_synergy": 0.4,
                        "synergy": 0.33,
                        "synergy_minus_no_synergy": -0.07,
                        "better_in_sample": "synergy",
                    }
                ]
            ).to_csv(root / "comparison" / "bonus_model_comparison.csv", index=False)

            output = write_eval_docs_summary(evaluation)

            text = output.read_text(encoding="utf-8")

        self.assertIn("Stage 2 Bonus Metrics", text)
        self.assertIn("all 2024", text)
        self.assertIn("Bonus Stage Scalars", text)
        self.assertIn("exact_acc", text)
        self.assertIn("Stage 1 Tossup Metrics", text)
        self.assertIn("buzz_position_mae", text)
        self.assertIn("No-Synergy Versus Synergy Deltas", text)
        self.assertIn("beta_2", text)
        self.assertIn("alpha_2", text)
        self.assertIn("psi_1", text)
        self.assertIn("tau", text)
        self.assertNotIn("formula", text)
        self.assertNotIn("model |", text)
        self.assertNotIn("use_synergy", text)
        self.assertNotIn("saved_synergy_details", text)
        self.assertNotIn("topic_dimensions", text)
        self.assertNotIn("skill_dimensions", text)


class ResultRootDetectionTests(unittest.TestCase):
    def test_result_root_for_evaluation_covers_known_layouts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "results" / "compirt"
            in_sample = root / "in_sample" / "model-a" / "evaluation"
            holdout = root / "holdout" / "model-b" / "holdout" / "synergy-evaluation"
            ablation = (
                root
                / "holdout"
                / "multidim-ablation"
                / "dim_5"
                / "holdout"
                / "synergy-evaluation"
            )

            roots = {
                result_root_for_evaluation(in_sample).relative_to(root),
                result_root_for_evaluation(holdout).relative_to(root),
                result_root_for_evaluation(ablation).relative_to(root),
            }

        self.assertEqual(
            roots,
            {
                Path("in_sample/model-a"),
                Path("holdout/model-b"),
                Path("holdout/multidim-ablation/dim_5"),
            },
        )


if __name__ == "__main__":
    unittest.main()
