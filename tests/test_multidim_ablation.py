"""Tests for the multidim synergy-only dimension ablation runner."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

import pandas as pd

from run_scripts import run_multidim_ablation as ablation


def args_for(root: Path) -> SimpleNamespace:
    """Return a minimal argparse-like object for command construction tests."""
    return SimpleNamespace(
        root=root,
        python=Path(".venv/bin/python"),
        data_dir=None,
        tournament=None,
        train_split="year_2024",
        test_split="year_2025",
        pyramidal_steps=3000,
        bonus_steps=2000,
        lr=0.01,
        device="cuda",
        new_player_prior="tier",
        synergy_dimensions=3,
        calibrate_correctness=False,
        predict_buzz_positions=True,
        save_synergy_details=False,
    )


class CommandConstructionTests(unittest.TestCase):
    def test_build_stages_runs_synergy_only_holdout_pipeline(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "multidim-ablation"
            stages = ablation.build_stages(args_for(root), 5)

        self.assertEqual(
            [stage.name for stage in stages],
            ["train-pyramidal", "holdout-pyramidal", "synergy", "synergy-evaluation"],
        )
        commands = [" ".join(stage.command) for stage in stages]
        self.assertEqual(commands[0].count("multidimensional.multidim_mirt.train_pyramidal"), 1)
        self.assertEqual(commands[1].count("multidimensional.multidim_mirt.train_pyramidal"), 1)
        self.assertIn("train_compositional", commands[2])
        self.assertIn("--use-synergy", commands[2])
        self.assertIn("--synergy-dimensions 3", commands[2])
        self.assertIn("evaluate_compirt", commands[3])
        self.assertIn("holdout/synergy", commands[2])
        self.assertIn("holdout/synergy-evaluation", commands[3])

    def test_build_stages_never_targets_no_synergy_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            stages = ablation.build_stages(args_for(Path(directory)), 2)

        all_command_text = "\n".join(" ".join(stage.command) for stage in stages)
        all_marker_text = "\n".join(str(stage.marker) for stage in stages)
        self.assertNotIn("holdout/compositional", all_command_text)
        self.assertNotIn("holdout/evaluation", all_command_text)
        self.assertNotIn("compare_compirt", all_command_text)
        self.assertNotIn("holdout/compositional", all_marker_text)
        self.assertNotIn("holdout/evaluation", all_marker_text)


class MetricCollectionTests(unittest.TestCase):
    def test_collect_run_reads_nested_metrics_and_normalizes_legacy_names(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "multidim-ablation"
            run = root / "dim_5"
            for path in (
                run / "train" / "pyramidal",
                run / "holdout" / "pyramidal",
                run / "holdout" / "synergy",
                run / "holdout" / "synergy-evaluation" / "csvs",
            ):
                path.mkdir(parents=True)
            (run / "train" / "pyramidal" / "summary.json").write_text(
                '{"final_loss": 101.5, "steps": 7}', encoding="utf-8"
            )
            (run / "holdout" / "pyramidal" / "summary.json").write_text(
                '{"final_loss": 202.5, "steps": 8}', encoding="utf-8"
            )
            (run / "holdout" / "synergy" / "summary.json").write_text(
                '{"final_loss": 303.5, "steps": 9, "synergy_dimensions": 3, "tau": 0.4}',
                encoding="utf-8",
            )
            pd.DataFrame(
                [
                    {
                        "log_loss": 0.33,
                        "part_accuracy": 0.86,
                        "exact_score_accuracy": 0.61,
                    }
                ]
            ).to_csv(
                run
                / "holdout"
                / "synergy-evaluation"
                / "csvs"
                / "bonus_metrics.csv",
                index=False,
            )
            pd.DataFrame([{"log_loss": 0.44, "auc": 0.91}]).to_csv(
                run
                / "holdout"
                / "synergy-evaluation"
                / "csvs"
                / "tossup_metrics.csv",
                index=False,
            )
            pd.DataFrame(
                [
                    {"z": "BUZZ", "y": 1, "predicted_correct": 0.8},
                    {"z": "BUZZ", "y": 0, "predicted_correct": 0.6},
                    {"z": "CENSORED", "y": None, "predicted_correct": 0.2},
                ]
            ).to_csv(
                run / "holdout" / "pyramidal" / "tossup_predictions.csv",
                index=False,
            )

            row = ablation.collect_run(root, 5)

        self.assertEqual(row["dimension"], 5)
        self.assertEqual(row["train_pyramidal_final_loss"], 101.5)
        self.assertEqual(row["holdout_pyramidal_final_loss"], 202.5)
        self.assertEqual(row["synergy_final_loss"], 303.5)
        self.assertEqual(row["synergy_dimensions"], 3)
        self.assertAlmostEqual(row["bonus_log_loss"], 0.33)
        self.assertAlmostEqual(row["bonus_part_accuracy"], 0.86)
        self.assertAlmostEqual(row["bonus_rounded_score_accuracy"], 0.61)
        self.assertAlmostEqual(row["tossup_log_loss"], 0.44)
        self.assertAlmostEqual(row["tossup_auc"], 0.91)
        self.assertAlmostEqual(row["tossup_accuracy"], 0.5)


class PlottingTests(unittest.TestCase):
    def test_save_aggregate_outputs_writes_expected_pngs(self):
        frame = pd.DataFrame(
            {
                "dimension": [1, 5],
                "bonus_log_loss": [0.4, 0.3],
                "bonus_part_accuracy": [0.8, 0.86],
                "tossup_log_loss": [0.5, 0.45],
                "tossup_auc": [0.88, 0.91],
                "tossup_accuracy": [0.77, 0.82],
            }
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            csv_output = ablation.save_aggregate_outputs(root, frame)

            self.assertTrue(csv_output.exists())
            self.assertTrue(
                (root / "graphs" / "bonus_validation_loss_vs_dimensions.png").exists()
            )
            self.assertTrue(
                (
                    root
                    / "graphs"
                    / "bonus_validation_accuracy_vs_dimensions.png"
                ).exists()
            )
            self.assertTrue(
                (root / "graphs" / "tossup_validation_loss_vs_dimensions.png").exists()
            )
            self.assertTrue(
                (root / "graphs" / "tossup_validation_auc_vs_dimensions.png").exists()
            )
            self.assertTrue(
                (
                    root
                    / "graphs"
                    / "tossup_validation_accuracy_vs_dimensions.png"
                ).exists()
            )


if __name__ == "__main__":
    unittest.main()
