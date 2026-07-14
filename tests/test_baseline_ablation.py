"""Tests for the baseline skill-by-synergy grid ablation runner."""

from __future__ import annotations

import json
import os
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock

import pandas as pd

from run_scripts import run_baseline_ablation as ablation


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
        seed=42,
        device="cuda",
        new_player_prior="tier",
        calibrate_correctness=False,
        predict_buzz_positions=True,
        save_synergy_details=False,
    )


class CommandConstructionTests(unittest.TestCase):
    def test_pyramidal_stages_train_the_baseline_model(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "baseline-ablation"
            stages = ablation.pyramidal_stages(args_for(root), 5)

        self.assertEqual(
            [stage.name for stage in stages], ["train-pyramidal", "holdout-pyramidal"]
        )
        commands = [" ".join(stage.command) for stage in stages]
        for command in commands:
            self.assertIn("-m train_pyramidal", command)
            self.assertNotIn("multidimensional", command)
            self.assertIn("--dimensions 5", command)
            self.assertIn("--seed 42", command)
        self.assertIn("--split year_2024", commands[0])
        self.assertIn("--split year_2025", commands[1])
        self.assertIn("--train-posterior", commands[1])
        self.assertNotIn("--train-posterior", commands[0])

    def test_pyramidal_stages_do_not_depend_on_the_synergy_rank(self):
        """Stage 1 is shared down a dimension's synergy column, so its paths must be too."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "baseline-ablation"
            markers = [str(stage.marker) for stage in ablation.pyramidal_stages(args_for(root), 3)]

        for marker in markers:
            self.assertNotIn("syn_", marker)

    def test_bonus_stages_run_the_synergy_branch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "baseline-ablation"
            stages = ablation.bonus_stages(args_for(root), 5, 3)

        self.assertEqual([stage.name for stage in stages], ["synergy", "synergy-evaluation"])
        commands = [" ".join(stage.command) for stage in stages]
        self.assertIn("-m train_compositional", commands[0])
        self.assertIn("--use-synergy", commands[0])
        self.assertIn("--synergy-dimensions 3", commands[0])
        self.assertIn("--seed 42", commands[0])
        self.assertIn("holdout/syn_3/synergy", commands[0])
        self.assertIn("-m evaluate_compirt", commands[1])
        self.assertIn("holdout/syn_3/synergy-evaluation", commands[1])
        # Stage 2 reads the frozen skills from this dimension's shared Stage-1 run.
        self.assertIn("dim_5/holdout/pyramidal/players.csv", commands[0])

    def test_bonus_stages_at_rank_zero_run_the_no_synergy_branch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "baseline-ablation"
            stages = ablation.bonus_stages(args_for(root), 5, 0)

        self.assertEqual(
            [stage.name for stage in stages], ["compositional", "compositional-evaluation"]
        )
        commands = [" ".join(stage.command) for stage in stages]
        self.assertNotIn("--use-synergy", commands[0])
        self.assertNotIn("--synergy-dimensions", commands[0])
        self.assertIn("holdout/syn_0/compositional", commands[0])
        self.assertIn("holdout/syn_0/compositional-evaluation", commands[1])

    def test_bonus_stages_never_pass_dimensions_to_the_bonus_trainer(self):
        """train_compositional infers the skill width from players.csv."""
        with tempfile.TemporaryDirectory() as directory:
            stages = ablation.bonus_stages(args_for(Path(directory)), 4, 2)

        self.assertNotIn("--dimensions", " ".join(stages[0].command))

    def test_save_synergy_details_is_omitted_at_rank_zero(self):
        with tempfile.TemporaryDirectory() as directory:
            args = args_for(Path(directory))
            args.save_synergy_details = True
            zero = " ".join(ablation.bonus_stages(args, 2, 0)[0].command)
            three = " ".join(ablation.bonus_stages(args, 2, 3)[0].command)

        self.assertNotIn("--save-synergy-details", zero)
        self.assertIn("--save-synergy-details", three)


class GridSchedulingTests(unittest.TestCase):
    def _stage_names(self, root: Path, extra_argv: list[str]) -> list[str]:
        """Run main() with training stubbed out, returning the stages it scheduled."""
        scheduled: list[str] = []
        argv = ["run_baseline_ablation", "--root", str(root), *extra_argv]
        with (
            mock.patch.object(ablation.sys, "argv", argv),
            mock.patch.dict(os.environ, {"COMPIRT_LOG_ACTIVE": "1"}),
            mock.patch.object(ablation, "save_ablation_config"),
            mock.patch.object(
                ablation,
                "run_stage",
                side_effect=lambda stage, rerun: scheduled.append(stage.name),
            ),
            mock.patch.object(ablation, "collect_results", return_value=pd.DataFrame()),
            mock.patch.object(ablation, "save_aggregate_outputs", return_value=root / "x.csv"),
        ):
            ablation.main()
        return scheduled

    def test_stage_one_is_scheduled_once_per_dimension_not_once_per_cell(self):
        """--rerun must not refit theta under already-finished synergy points."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "ablation"
            scheduled = self._stage_names(
                root,
                ["--dimensions", "1", "2", "--synergy-dimensions", "0", "1", "3", "--rerun"],
            )

        self.assertEqual(scheduled.count("train-pyramidal"), 2)
        self.assertEqual(scheduled.count("holdout-pyramidal"), 2)
        # One bonus branch and one evaluation per grid cell.
        self.assertEqual(scheduled.count("compositional"), 2)
        self.assertEqual(scheduled.count("synergy"), 4)
        self.assertEqual(scheduled.count("synergy-evaluation"), 4)

    def test_each_dimension_fits_stage_one_before_any_of_its_bonus_points(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "ablation"
            scheduled = self._stage_names(
                root, ["--dimensions", "2", "--synergy-dimensions", "1", "2"]
            )

        self.assertEqual(
            scheduled,
            [
                "train-pyramidal",
                "holdout-pyramidal",
                "synergy",
                "synergy-evaluation",
                "synergy",
                "synergy-evaluation",
            ],
        )


class ConfigTests(unittest.TestCase):
    def test_save_ablation_config_writes_every_resolved_setting(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path = ablation.save_ablation_config(root, args_for(root))
            config = json.loads(config_path.read_text(encoding="utf-8"))

        self.assertEqual(config_path.name, "ablation_config.json")
        self.assertEqual(config["new_player_prior"], "tier")
        self.assertEqual(config["pyramidal_steps"], 3000)
        self.assertEqual(config["lr"], 0.01)
        self.assertEqual(config["seed"], 42)
        # Paths must survive the JSON round-trip as strings.
        self.assertEqual(config["python"], ".venv/bin/python")

    def _run_main(self, root: Path, extra_argv: list[str]) -> mock.Mock:
        """Run main() with training and aggregation stubbed out."""
        argv = ["run_baseline_ablation", "--root", str(root), *extra_argv]
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

    def test_plot_axes_default_to_the_swept_axes(self):
        argv = [
            "run_baseline_ablation",
            "--root",
            "custom/root",
            "--dimensions",
            "2",
            "4",
            "--synergy-dimensions",
            "0",
            "2",
        ]
        with mock.patch.object(ablation.sys, "argv", argv):
            args = ablation.parse_args()

        self.assertEqual(args.plot_dimensions, [2, 4])
        self.assertEqual(args.plot_synergy_dimensions, [0, 2])

    def test_negative_synergy_rank_is_rejected(self):
        argv = ["run_baseline_ablation", "--synergy-dimensions", "-1"]
        with mock.patch.object(ablation.sys, "argv", argv):
            with self.assertRaises(ValueError):
                ablation.parse_args()


class MetricCollectionTests(unittest.TestCase):
    def _write_point(self, root: Path, dimension: int, synergy: int, bonus_loss: float) -> None:
        """Write the saved artifacts one finished grid cell would leave behind."""
        run = ablation.run_dir(root, dimension)
        stage_name = ablation.bonus_stage_name(synergy)
        point = ablation.bonus_dir(root, dimension, synergy)
        evaluation = point / f"{stage_name}-evaluation"
        for path in (
            run / "train" / "pyramidal",
            run / "holdout" / "pyramidal",
            point / stage_name,
            evaluation / "csvs",
        ):
            path.mkdir(parents=True, exist_ok=True)
        (run / "train" / "pyramidal" / "summary.json").write_text(
            '{"final_loss": 101.5, "steps": 7}', encoding="utf-8"
        )
        (run / "holdout" / "pyramidal" / "summary.json").write_text(
            '{"final_loss": 202.5, "steps": 8}', encoding="utf-8"
        )
        (point / stage_name / "summary.json").write_text(
            json.dumps(
                {
                    "final_loss": 303.5,
                    "steps": 9,
                    "use_synergy": synergy > 0,
                    "synergy_dimensions": synergy,
                    "tau": 0.4,
                }
            ),
            encoding="utf-8",
        )
        pd.DataFrame(
            [{"log_loss": bonus_loss, "part_accuracy": 0.86, "exact_acc": 0.61}]
        ).to_csv(evaluation / "csvs" / "bonus_metrics.csv", index=False)
        pd.DataFrame([{"log_loss": 0.44, "auc": 0.91}]).to_csv(
            evaluation / "csvs" / "tossup_metrics.csv", index=False
        )
        pd.DataFrame(
            [
                {"z": "BUZZ", "y": 1, "predicted_correct": 0.8},
                {"z": "BUZZ", "y": 0, "predicted_correct": 0.6},
                {"z": "CENSORED", "y": None, "predicted_correct": 0.2},
            ]
        ).to_csv(run / "holdout" / "pyramidal" / "tossup_predictions.csv", index=False)

    def test_collect_run_reads_nested_metrics(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "baseline-ablation"
            self._write_point(root, 5, 3, bonus_loss=0.33)
            row = ablation.collect_run(root, 5, 3)

        self.assertEqual(row["dimension"], 5)
        self.assertEqual(row["synergy_dimensions"], 3)
        self.assertEqual(row["train_pyramidal_final_loss"], 101.5)
        self.assertEqual(row["holdout_pyramidal_final_loss"], 202.5)
        self.assertEqual(row["bonus_final_loss"], 303.5)
        self.assertTrue(row["bonus_use_synergy"])
        self.assertAlmostEqual(row["bonus_tau"], 0.4)
        self.assertAlmostEqual(row["bonus_log_loss"], 0.33)
        self.assertAlmostEqual(row["bonus_part_accuracy"], 0.86)
        self.assertAlmostEqual(row["bonus_exact_acc"], 0.61)
        self.assertAlmostEqual(row["tossup_log_loss"], 0.44)
        self.assertAlmostEqual(row["tossup_auc"], 0.91)
        self.assertAlmostEqual(row["tossup_accuracy"], 0.5)

    def test_collect_run_keeps_the_grid_coordinate_at_rank_zero(self):
        """The bonus summary reports 0 for no-synergy runs; the coordinate must survive."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "baseline-ablation"
            self._write_point(root, 2, 0, bonus_loss=0.5)
            row = ablation.collect_run(root, 2, 0)

        self.assertEqual(row["synergy_dimensions"], 0)
        self.assertFalse(row["bonus_use_synergy"])
        self.assertAlmostEqual(row["bonus_log_loss"], 0.5)

    def test_collect_results_yields_one_row_per_grid_cell(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "baseline-ablation"
            for dimension in (1, 2):
                for synergy in (0, 2):
                    self._write_point(root, dimension, synergy, bonus_loss=0.3)
            frame = ablation.collect_results(root, [1, 2], [0, 2])

        self.assertEqual(len(frame), 4)
        self.assertEqual(list(frame["dimension"]), [1, 1, 2, 2])
        self.assertEqual(list(frame["synergy_dimensions"]), [0, 2, 0, 2])


class ColorTests(unittest.TestCase):
    def test_synergy_shade_depends_on_the_rank_not_on_the_plotted_subset(self):
        self.assertEqual(ablation.synergy_color(3), ablation.synergy_color(3))
        self.assertNotEqual(ablation.synergy_color(1), ablation.synergy_color(2))

    def test_no_synergy_is_visually_set_apart_from_the_synergy_ramp(self):
        self.assertEqual(ablation.synergy_color(0), ablation.NO_SYNERGY_COLOR)
        self.assertEqual(ablation.synergy_label(0), "no synergy")
        self.assertEqual(ablation.synergy_label(2), "s = 2")

    def test_ranks_past_the_shade_cap_stay_on_the_ramp(self):
        self.assertEqual(
            ablation.synergy_color(ablation.SYNERGY_SHADE_CAP + 4),
            ablation.synergy_color(ablation.SYNERGY_SHADE_CAP),
        )


class PlottingTests(unittest.TestCase):
    @staticmethod
    def grid_frame() -> pd.DataFrame:
        return pd.DataFrame(
            {
                "dimension": [1, 1, 5, 5],
                "synergy_dimensions": [0, 3, 0, 3],
                "bonus_log_loss": [0.40, 0.38, 0.34, 0.30],
                "bonus_part_accuracy": [0.80, 0.82, 0.85, 0.86],
                # Stage 1 never sees the synergy rank, so these repeat down each column.
                "tossup_log_loss": [0.50, 0.50, 0.45, 0.45],
                "tossup_auc": [0.88, 0.88, 0.91, 0.91],
                "tossup_accuracy": [0.77, 0.77, 0.82, 0.82],
            }
        )

    def test_save_aggregate_outputs_writes_grid_and_tossup_graphs(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            csv_output = ablation.save_aggregate_outputs(root, self.grid_frame())
            graphs = root / "graphs"

            self.assertTrue(csv_output.exists())
            for name in (
                "bonus_log_loss_vs_dimensions.png",
                "bonus_log_loss_grid.png",
                "bonus_part_accuracy_vs_dimensions.png",
                "bonus_part_accuracy_grid.png",
                "tossup_log_loss_vs_dimensions.png",
                "tossup_auc_vs_dimensions.png",
                "tossup_accuracy_vs_dimensions.png",
            ):
                self.assertTrue((graphs / name).exists(), name)

    def test_tossup_metrics_are_not_plotted_as_a_grid(self):
        """A tossup heatmap would repeat every row, so no such graph is written."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            ablation.save_aggregate_outputs(root, self.grid_frame())
            names = {path.name for path in (root / "graphs").iterdir()}

        self.assertFalse({name for name in names if name.startswith("tossup") and "grid" in name})

    def test_numeric_grid_pivots_synergy_by_dimension(self):
        grid = ablation.numeric_grid(self.grid_frame(), "bonus_log_loss")

        self.assertEqual(list(grid.index), [0, 3])
        self.assertEqual(list(grid.columns), [1, 5])
        self.assertAlmostEqual(grid.loc[3, 5], 0.30)

    def test_grid_plots_tolerate_missing_cells(self):
        frame = self.grid_frame().drop(index=1).reset_index(drop=True)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            ablation.save_grid_heatmap(frame, root, "bonus_log_loss", "g.png", "loss", "t")
            ablation.save_grid_line_plot(frame, root, "bonus_log_loss", "l.png", "loss", "t")

            self.assertTrue((root / "graphs" / "g.png").exists())
            self.assertTrue((root / "graphs" / "l.png").exists())

    def test_missing_metric_column_is_skipped_without_raising(self):
        frame = pd.DataFrame({"dimension": [1], "synergy_dimensions": [0]})
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            ablation.save_grid_heatmap(frame, root, "bonus_log_loss", "g.png", "loss", "t")
            ablation.save_tossup_plot(frame, root, "tossup_auc", "t.png", "auc", "t")

            self.assertFalse((root / "graphs" / "g.png").exists())
            self.assertFalse((root / "graphs" / "t.png").exists())


if __name__ == "__main__":
    unittest.main()
