"""Tests for the 2024 ACF Nationals in-sample ranking batch runner."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from run_scripts import run_2024_nationals_in_sample_ranking_comparison as runner


def args_for(*extra: str):
    """Return parsed args with temporary result roots and optional overrides."""
    directory = tempfile.TemporaryDirectory()
    root = Path(directory.name)
    args = runner.parse_args(
        [
            "--model-root",
            str(root / "results" / "compirt" / "in_sample" / "in_sample_2024nationals"),
            "--ranking-root",
            str(root / "results" / "ranking_comparison" / "in_sample_2024nationals"),
            "--skip-validation",
            *extra,
        ]
    )
    return directory, args


def command_text(stages: list[runner.Stage]) -> str:
    return "\n".join(" ".join(stage.command) for stage in stages)


class CommandMatrixTests(unittest.TestCase):
    def test_default_matrix_includes_cal_and_no_cal_versions(self):
        temporary, args = args_for("--models", "baseline")
        with temporary:
            runs = runner.build_model_runs(args)

        self.assertEqual([run.run_name for run in runs], ["baseline", "baseline-cal"])
        no_cal_text = command_text(list(runs[0].stages))
        cal_text = command_text(list(runs[1].stages))
        self.assertNotIn("--calibrate-correctness", no_cal_text)
        self.assertIn("--calibrate-correctness", cal_text)

    def test_commands_include_nationals_tournament_and_2024_split(self):
        temporary, args = args_for("--models", "baseline", "--calibration", "no-cal")
        with temporary:
            runs = runner.build_model_runs(args)

        text = command_text(list(runs[0].stages))
        self.assertIn("2024-acf-nationals", text)
        self.assertIn("year_2024", text)

    def test_every_bonus_command_uses_synergy(self):
        temporary, args = args_for(
            "--models",
            "baseline",
            "plda",
            "learned-topic",
            "multidim",
            "embedding",
            "tfidf-cumulative-difficulty",
            "tfidf-multidim-cumulative-difficulty",
            "--calibration",
            "no-cal",
        )
        with temporary:
            stages = [stage for run in runner.build_model_runs(args) for stage in run.stages]

        bonus_stages = [stage for stage in stages if stage.kind == "bonus"]
        self.assertEqual(len(bonus_stages), 7)
        for stage in bonus_stages:
            text = " ".join(stage.command)
            self.assertIn("--use-synergy", text)
            self.assertIn("--synergy-dimensions 3", text)
            self.assertNotIn("/compositional", text)

    def test_no_commands_target_no_synergy_outputs_or_compare_compirt(self):
        temporary, args = args_for("--models", "baseline", "plda", "--calibration", "both")
        with temporary:
            stages = [stage for run in runner.build_model_runs(args) for stage in run.stages]

        text = command_text(stages)
        marker_text = "\n".join(
            str(marker) for stage in stages for marker in stage.markers
        )
        self.assertNotIn("/compositional", text)
        self.assertNotIn("/evaluation", text)
        self.assertNotIn("compare_compirt", text)
        self.assertNotIn("/compositional", marker_text)
        self.assertNotIn("/evaluation", marker_text)

    def test_ranking_commands_target_requested_ranking_root(self):
        temporary, args = args_for("--models", "baseline", "--calibration", "no-cal")
        with temporary:
            stages = [stage for run in runner.build_model_runs(args) for stage in run.stages]

        ranking = [stage for stage in stages if stage.kind == "ranking"]
        self.assertEqual(len(ranking), 1)
        text = " ".join(ranking[0].command)
        self.assertIn("results/ranking_comparison/in_sample_2024nationals", text)
        self.assertIn("compare_player_rankings.py", text)
        self.assertIn("--actual-rank-mode ppg", text)
        self.assertIn("--min-game-tossups 20", text)

    def test_category_uses_13_dimensions_and_other_models_use_shared_5d(self):
        temporary, args = args_for(
            "--models",
            "baseline",
            "plda",
            "category",
            "learned-topic",
            "multidim",
            "tfidf-cumulative-difficulty",
            "--calibration",
            "no-cal",
        )
        with temporary:
            runs = runner.build_model_runs(args)

        pyramidal_by_run = {
            run.run_name: next(stage for stage in run.stages if stage.name == "pyramidal")
            for run in runs
        }
        self.assertIn("--dimensions 13", " ".join(pyramidal_by_run["category"].command))
        for name in (
            "baseline",
            "plda",
            "learned-topic",
            "multidim",
            "tfidf-cumulative-difficulty",
        ):
            self.assertIn("--dimensions 5", " ".join(pyramidal_by_run[name].command))


class AggregateOutputTests(unittest.TestCase):
    def test_aggregate_markdown_omits_duplicate_global_rank_and_explains_top_overlap(self):
        temporary, args = args_for("--models", "baseline", "--calibration", "no-cal")
        with temporary:
            run = runner.build_model_runs(args)[0]
            summary_dir = run.ranking_root / args.tournament
            summary_dir.mkdir(parents=True)
            (summary_dir / "summary.json").write_text(
                json.dumps(
                    {
                        "tournament": args.tournament,
                        "actual_players_after_floor": 2,
                        "actual_rank_mode": "ppg",
                        "actual_rank_metric": "actual_ppg",
                        "min_games": 1,
                        "min_tuh": 1,
                        "min_game_tossups": 20,
                        "global_model_matches": 2,
                        "tournament_model_matches": 2,
                        "global_rank_correlation": 0.5,
                        "tournament_rank_correlation": 0.5,
                        "actual_top_20_in_global_model_rank_top_20": "1/20",
                        "actual_top_20_in_tournament_model_rank_top_20": "1/20",
                        "actual_top_20_in_tournament_model_rank_top_50": "2/20",
                    }
                ),
                encoding="utf-8",
            )
            (summary_dir / "player_ranking_comparison.csv").write_text(
                "\n".join(
                    [
                        "actual_rank,player_id,tournament_model_rank",
                        "1,a,1",
                        "2,b,49",
                        "30,c,3",
                        "55,d,4",
                    ]
                )
                + "\n",
                encoding="utf-8",
            )

            output = runner.write_aggregate_outputs(args, [run])

            self.assertIsNotNone(output)
            csv_path, md_path, json_path = output
            csv_text = csv_path.read_text(encoding="utf-8")
            md_text = md_path.read_text(encoding="utf-8")
            json_text = json_path.read_text(encoding="utf-8")

        self.assertNotIn("global_rank_correlation", csv_text)
        self.assertNotIn("global_rank_correlation", md_text)
        self.assertNotIn("global_rank_correlation", json_text)
        self.assertNotIn("actual_top_20_in_tournament_model_rank_top_50", csv_text)
        self.assertNotIn("actual_top_20_in_tournament_model_rank_top_50", json_text)
        self.assertIn("actual_top_20_in_tournament_model_rank_top_20", md_text)
        self.assertIn("actual_top_50_in_tournament_model_rank_top_50", md_text)
        self.assertIn("1/20", md_text)
        self.assertIn("3/50", md_text)
        self.assertIn("Top-N Overlap Columns", md_text)
        self.assertIn("public [2024 ACF Nationals player standings]", md_text)


if __name__ == "__main__":
    unittest.main()
