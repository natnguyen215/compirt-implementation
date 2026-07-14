"""Tests for the learned-topic synergy-only topic-count ablation runner."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

import pandas as pd

from run_scripts import run_learned_topic_ablation as ablation


def args_for(root: Path) -> SimpleNamespace:
    """Return a minimal argparse-like object for command construction tests."""
    return SimpleNamespace(
        root=root,
        python=Path(".venv/bin/python"),
        data_dir=None,
        database=None,
        tournament=None,
        train_split="year_2024",
        test_split="year_2025",
        bow_weight=1.0,
        topic_concentration=1.0,
        vocab_size=2000,
        min_df=2,
        rm_top=20,
        seed=42,
        pyramidal_steps=3000,
        bonus_steps=2000,
        lr=0.01,
        device="cuda",
        new_player_prior="tier",
        synergy_dimensions=3,
        pyramidal_module="learned",
        calibrate_correctness=False,
        predict_buzz_positions=True,
        save_synergy_details=False,
    )


class CommandConstructionTests(unittest.TestCase):
    def test_build_stages_runs_synergy_only_holdout_pipeline(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "learned-topic-ablation"
            stages = ablation.build_stages(args_for(root), 5)

        self.assertEqual(
            [stage.name for stage in stages],
            ["train-pyramidal", "holdout-pyramidal", "synergy", "synergy-evaluation"],
        )
        commands = [" ".join(stage.command) for stage in stages]
        self.assertEqual(commands[0].count("topic.learned.train_joint_pyramidal"), 1)
        self.assertEqual(commands[1].count("topic.learned.train_joint_pyramidal"), 1)
        self.assertIn("topic.learned.train_joint_compositional", commands[2])
        self.assertIn("--use-synergy", commands[2])
        self.assertIn("--synergy-dimensions 3", commands[2])
        self.assertIn("holdout/synergy", commands[2])
        self.assertIn("holdout/synergy-evaluation", commands[3])

    def test_stage_one_receives_topic_count_and_vocabulary_knobs(self):
        with tempfile.TemporaryDirectory() as directory:
            stages = ablation.build_stages(args_for(Path(directory)), 7)

        train = " ".join(stages[0].command)
        self.assertIn("--dimensions 7", train)
        self.assertIn("--vocab-size 2000", train)
        self.assertIn("--min-df 2", train)
        self.assertIn("--rm-top 20", train)
        self.assertIn("--bow-weight 1.0", train)
        self.assertIn("--topic-concentration 1.0", train)
        self.assertIn("--seed 42", train)
        self.assertIn("--predict-buzz-positions", train)
        self.assertNotIn("--no-predict-buzz-positions", train)

    def test_holdout_pyramidal_freezes_the_trained_topic_model(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            stages = ablation.build_stages(args_for(root), 5)

        holdout = " ".join(stages[1].command)
        # --train-posterior is rejected by the trainer unless --train-topic-model
        # is supplied alongside it.
        self.assertIn("--train-posterior", holdout)
        self.assertIn("--train-topic-model", holdout)
        self.assertIn("--new-player-prior tier", holdout)
        self.assertIn("--split year_2025", holdout)

    def test_synergy_stage_omits_dimensions_and_freezes_training_topics(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            stages = ablation.build_stages(args_for(root), 5)

        synergy = " ".join(stages[2].command)
        # Stage 2 infers the topic count from the saved player skills and
        # validates it against the frozen topic-word matrix.
        self.assertNotIn("--dimensions", synergy)
        # Frozen topics come from the training run, never the held-out one.
        self.assertIn(f"--topic-model-dir {root / 'dim_5' / 'train' / 'pyramidal'}", synergy)
        self.assertNotIn("--topic-model-dir " + str(root / "dim_5" / "holdout"), synergy)
        self.assertIn(
            f"--player-skills {root / 'dim_5' / 'holdout' / 'pyramidal' / 'players.csv'}",
            synergy,
        )

    def test_evaluation_uses_the_topic_weighted_evaluator(self):
        with tempfile.TemporaryDirectory() as directory:
            stages = ablation.build_stages(args_for(Path(directory)), 5)

        evaluation = " ".join(stages[3].command)
        # The root evaluate_compirt silently skips difficulty/timing figures for
        # this family: learned tossups.csv names its weights topic_weight_*, not
        # alpha_* or r_*.
        self.assertIn("topic.fixed.evaluate_topic_compirt", evaluation)
        self.assertNotIn("-m evaluate_compirt", evaluation)

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
    def test_collect_run_reads_nested_metrics(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "learned-topic-ablation"
            run = root / "dim_5"
            for path in (
                run / "train" / "pyramidal",
                run / "holdout" / "pyramidal",
                run / "holdout" / "synergy",
                run / "holdout" / "synergy-evaluation" / "csvs",
            ):
                path.mkdir(parents=True)
            (run / "train" / "pyramidal" / "summary.json").write_text(
                json.dumps(
                    {
                        "final_loss": 101.5,
                        "steps": 7,
                        "bow_weight": 0.25,
                        "topic_concentration": 0.5,
                        "vocab_size": 1873,
                        "vocab_size_limit": 2000,
                        "min_df": 2,
                        "rm_top": 20,
                        "seed": 42,
                    }
                ),
                encoding="utf-8",
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
                        "exact_acc": 0.61,
                    }
                ]
            ).to_csv(
                run / "holdout" / "synergy-evaluation" / "csvs" / "bonus_metrics.csv",
                index=False,
            )
            pd.DataFrame([{"log_loss": 0.44, "auc": 0.91}]).to_csv(
                run / "holdout" / "synergy-evaluation" / "csvs" / "tossup_metrics.csv",
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
        self.assertAlmostEqual(row["bonus_exact_acc"], 0.61)
        self.assertAlmostEqual(row["tossup_log_loss"], 0.44)
        self.assertAlmostEqual(row["tossup_auc"], 0.91)
        self.assertAlmostEqual(row["tossup_accuracy"], 0.5)

    def test_collect_run_records_topic_hyperparameters(self):
        """Every row pins the settings needed to reproduce that ablation point."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "learned-topic-ablation"
            train = root / "dim_5" / "train" / "pyramidal"
            train.mkdir(parents=True)
            (train / "summary.json").write_text(
                json.dumps(
                    {
                        "final_loss": 1.0,
                        "steps": 3000,
                        "bow_weight": 0.25,
                        "topic_concentration": 0.5,
                        "vocab_size": 1873,
                        "vocab_size_limit": 2000,
                        "min_df": 2,
                        "rm_top": 20,
                        "seed": 7,
                    }
                ),
                encoding="utf-8",
            )

            row = ablation.collect_run(root, 5)

        self.assertAlmostEqual(row["bow_weight"], 0.25)
        self.assertAlmostEqual(row["topic_concentration"], 0.5)
        self.assertEqual(row["vocab_size"], 1873)
        self.assertEqual(row["vocab_size_limit"], 2000)
        self.assertEqual(row["min_df"], 2)
        self.assertEqual(row["rm_top"], 20)
        self.assertEqual(row["seed"], 7)


class ConfigTests(unittest.TestCase):
    def test_save_ablation_config_writes_every_resolved_setting(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path = ablation.save_ablation_config(root, args_for(root))
            config = json.loads(config_path.read_text(encoding="utf-8"))

        self.assertEqual(config_path.name, "ablation_config.json")
        self.assertEqual(config["bow_weight"], 1.0)
        self.assertEqual(config["topic_concentration"], 1.0)
        self.assertEqual(config["seed"], 42)
        self.assertEqual(config["synergy_dimensions"], 3)
        self.assertEqual(config["new_player_prior"], "tier")
        self.assertEqual(config["train_split"], "year_2024")
        self.assertEqual(config["test_split"], "year_2025")
        # Paths must survive the JSON round-trip as strings.
        self.assertEqual(config["python"], ".venv/bin/python")

    def _run_main(self, root: Path, extra_argv: list[str]) -> mock.Mock:
        """Run main() with training and aggregation stubbed out."""
        argv = ["run_learned_topic_ablation", "--root", str(root), *extra_argv]
        with (
            mock.patch.object(ablation.sys, "argv", argv),
            mock.patch.dict(os.environ, {"COMPIRT_LOG_ACTIVE": "1"}),
            mock.patch.object(ablation, "save_ablation_config") as save_config,
            mock.patch.object(ablation, "run_stage"),
            mock.patch.object(ablation, "collect_results", return_value=pd.DataFrame()),
            mock.patch.object(ablation, "save_aggregate_outputs", return_value=root / "x.csv"),
        ):
            ablation.main()
        return save_config

    def test_collect_only_does_not_overwrite_the_sweep_configuration(self):
        """A re-aggregation pass must not clobber the real sweep's settings."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "ablation"
            save_config = self._run_main(root, ["--collect-only"])

        save_config.assert_not_called()

    def test_training_run_records_configuration_before_stages(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "ablation"
            save_config = self._run_main(root, ["--dimensions", "3"])

        save_config.assert_called_once()


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

            self.assertEqual(csv_output.name, "learned_topic_ablation_metrics.csv")
            self.assertTrue(csv_output.exists())
            for filename in (
                "bonus_validation_loss_vs_topics.png",
                "bonus_validation_accuracy_vs_topics.png",
                "tossup_validation_loss_vs_topics.png",
                "tossup_validation_auc_vs_topics.png",
                "tossup_validation_accuracy_vs_topics.png",
            ):
                self.assertTrue((root / "graphs" / filename).exists(), filename)


if __name__ == "__main__":
    unittest.main()
