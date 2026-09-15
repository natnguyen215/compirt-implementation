"""Focused tests for the end-to-end CompIRT evaluation additions."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

from compirt_eval.common.metrics import (
    binary_brier_score,
    calibration_table,
    classification_metrics,
    expected_calibration_error,
    negative_class_metrics,
    ranked_probability_score,
)
from compirt_eval.scenario_a_tossups.survival import (
    _full_pmf_score_row,
    evaluate_survival_and_first_buzzer,
)
from compirt_eval.scenario_a_tossups.timing import buzz_density_fit_plot
from compirt_eval.scenario_a_tossups.reconstruction import event_first_buzz_components
from compirt_eval.scenario_a_tossups.metrics import tossup_joint_event_scores
from compirt_eval.scenario_b_bonuses.metrics import (
    bonus_ranked_probability_scores,
    bonus_score_distribution,
)
from compirt_eval.scenario_b_bonuses.distributions import bonus_parameter_distribution_plots


class FrozenBonusParameterPlotTests(unittest.TestCase):
    def test_frozen_replay_plots_training_parameters_and_synergy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            train = root / "train" / "synergy"
            holdout = root / "holdout" / "synergy"
            output = root / "synergy-evaluation"
            train.mkdir(parents=True)
            holdout.mkdir(parents=True)
            (holdout / "summary.json").write_text(json.dumps({"frozen_predict": True}))
            pd.DataFrame({"bonus_part_id": ["a", "b", "c"],
                          "beta": [-1., 0., 1.], "alpha_1": [0.5, 1., 1.5]}).to_csv(
                train / "bonus_parts.csv", index=False)
            pd.DataFrame({"player_id": ["p1", "p2", "p3"],
                          "psi_1": [-0.2, 0.1, 0.3]}).to_csv(
                train / "player_synergy_profiles.csv", index=False)
            bonus_parameter_distribution_plots(holdout, output)
            for name in ("bonus_part_parameter_distributions.png", "synergy_parameter_distributions.png"):
                self.assertTrue((output / "graphs" / "parameters" / name).is_file())
            summary = pd.read_csv(output / "csvs" / "bonus_parameter_distribution_summary.csv")
            self.assertEqual(set(summary.parameter_source), {str(train)})
            self.assertFalse((holdout / "bonus_parts.csv").exists())

    def test_nonfrozen_predictions_do_not_borrow_training_parameters(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            train = root / "train" / "compositional"
            holdout = root / "holdout" / "compositional"
            train.mkdir(parents=True)
            holdout.mkdir(parents=True)
            pd.DataFrame({"beta": [1.]}).to_csv(train / "bonus_parts.csv", index=False)
            (holdout / "summary.json").write_text(json.dumps({"frozen_predict": False}))
            bonus_parameter_distribution_plots(holdout, root / "evaluation")
            self.assertFalse((root / "evaluation").exists())


class ProperScoreTests(unittest.TestCase):
    def test_ece_matches_reliability_table_at_bin_boundaries(self):
        labels = [1, 0, 1, 0, 1]
        probabilities = [0.0, 0.1, 0.2, 0.9, 1.0]
        table = calibration_table(labels, probabilities)
        expected = (
            (table["observed"] - table["predicted"]).abs() * table["count"]
        ).sum() / len(labels)

        self.assertAlmostEqual(
            expected_calibration_error(labels, probabilities), expected
        )
        self.assertEqual(table["count"].sum(), len(labels))

    def test_auc_preserves_order_of_extreme_probabilities(self):
        for probabilities in ([1e-20, 2e-20], [1e-8, 2e-8], [1 - 2e-8, 1 - 1e-8]):
            with self.subTest(probabilities=probabilities):
                metrics = classification_metrics([0, 1], probabilities)
                self.assertEqual(metrics["auc"], 1.0)
                self.assertTrue(np.isfinite(metrics["log_loss"]))
                neg_metrics = negative_class_metrics([0, 1], probabilities)
                self.assertEqual(neg_metrics["neg_auroc"], 1.0)
                self.assertEqual(neg_metrics["neg_average_precision"], 1.0)

    def test_negative_prediction_complements_correctness_at_threshold(self):
        metrics = negative_class_metrics([0, 0, 0], [0.5, 0.4, np.nextafter(0.5, 0)])
        self.assertEqual(metrics["neg_recall"], 2 / 3)

    def test_full_pmf_uses_saved_calibrated_correctness(self):
        event = pd.DataFrame(
            {
                "player_id": ["p1"],
                "z": ["BUZZ"],
                "y": [1],
                "t_star": [1],
                "predicted_correct": [0.9],
            }
        )
        components = {
            "dead_mass": 0.8,
            "player_first_buzz_mass": np.asarray([[0.2]]),
            "first_buzz_mass": np.asarray([0.2]),
            "correctness_probability": np.asarray([[0.1]]),
            "player_ids": np.asarray(["p1"]),
            "relative_position": np.asarray([1.0]),
        }

        score = _full_pmf_score_row("e", event, components)

        self.assertAlmostEqual(score["observed_probability"], 0.18)

    def test_binary_brier_and_all_correct_baseline(self):
        self.assertAlmostEqual(binary_brier_score([0, 1], [0.2, 0.8]), 0.04)
        metrics = classification_metrics([1, 1, 0, 1], [0.9, 0.7, 0.4, 0.2])
        self.assertEqual(metrics["all_correct_accuracy"], 0.75)
        self.assertAlmostEqual(
            metrics["accuracy_lift_over_all_correct"],
            metrics["accuracy"] - 0.75,
        )
        self.assertIn("probability_std", metrics)

    def test_negative_class_metrics_reverse_labels_and_probabilities(self):
        metrics = negative_class_metrics([1, 0, 0], [0.8, 0.3, 0.6])

        self.assertAlmostEqual(metrics["neg_auroc"], 1.0)
        self.assertEqual(metrics["neg_precision"], 1.0)
        self.assertEqual(metrics["neg_recall"], 0.5)

    def test_bonus_distribution_and_rps_extremes(self):
        np.testing.assert_allclose(bonus_score_distribution([0, 0, 0]), [1, 0, 0, 0])
        np.testing.assert_allclose(bonus_score_distribution([1, 1, 1]), [0, 0, 0, 1])
        self.assertEqual(ranked_probability_score([0, 0, 1, 0], 2), 0.0)

    def test_bonus_rps_uses_complete_three_part_responses_only(self):
        parts = pd.DataFrame(
            {
                "response_id": ["complete"] * 3 + ["short"] * 2,
                "part_index": [0, 1, 2, 0, 1],
                "correct": [1, 0, 1, 1, 0],
                "predicted_correct": [0.8, 0.2, 0.7, 0.5, 0.5],
            }
        )
        scores = bonus_ranked_probability_scores(parts)
        self.assertEqual(scores["response_id"].tolist(), ["complete"])
        self.assertAlmostEqual(scores.filter(like="probability_").sum(axis=1).iloc[0], 1)
        self.assertAlmostEqual(
            scores["score_log_loss"].iloc[0],
            -np.log(scores["observed_score_probability"].iloc[0]),
        )

    def test_joint_tossup_event_score_combines_model_likelihood_terms(self):
        predictions = pd.DataFrame(
            {
                "event_id": ["buzzed", "buzzed", "dead", "dead"],
                "game_id": ["g1", "g1", "g2", "g2"],
                "tossup_id": ["q1", "q1", "q2", "q2"],
                "player_id": ["p1", "p2", "p1", "p2"],
                "z": ["BUZZ", "CENSORED", "NO-BUZZ", "NO-BUZZ"],
                "y": [1, np.nan, np.nan, np.nan],
                "t_star": [5, 5, 20, 20],
                "relative_position": [0.25, 0.25, 1.0, 1.0],
                "predicted_survival": [0.8, 0.9, 0.6, 0.5],
                "predicted_hazard": [0.25, 0.1, 0.05, 0.04],
                "predicted_correct": [0.7, 0.4, 0.3, 0.2],
            }
        )

        scores = tossup_joint_event_scores(predictions).set_index("event_id")

        winner_probability = (1 - 0.75 * 0.9) * (
            (0.25 / 0.75) / (0.25 / 0.75 + 0.1 / 0.9)
        )
        expected = 0.8 * 0.9 * winner_probability * 0.7
        self.assertAlmostEqual(
            scores.loc["buzzed", "joint_event_probability"],
            expected,
        )
        self.assertAlmostEqual(
            scores.loc["dead", "joint_event_probability"], 0.6 * 0.5
        )
        self.assertAlmostEqual(
            scores.loc["buzzed", "joint_event_log_loss"],
            -np.log(expected),
        )
        self.assertEqual(scores.loc["dead", "observed_outcome"], "dead")


class TimingAndRecoveryTests(unittest.TestCase):
    @staticmethod
    def _timing_parameters():
        players = pd.DataFrame(
            {
                "player_id": ["p1", "p2"],
                "c": [2.0, 2.2],
                "theta_1": [0.5, 0.2],
                "theta_2": [0.1, 0.4],
            }
        ).set_index("player_id")
        tossups = pd.DataFrame(
            {
                "tossup_id": ["q1"],
                "alpha_1": [1.0],
                "alpha_2": [0.8],
                "beta_1": [0.7],
                "beta_2": [0.6],
                "gamma_1": [8.0],
                "gamma_2": [7.0],
                "mu_1": [0.5],
                "mu_2": [0.6],
            }
        ).set_index("tossup_id")
        return players, tossups

    def test_first_buzz_player_mass_conserves_probability(self):
        players, tossups = self._timing_parameters()
        event = pd.DataFrame(
            {
                "event_id": ["e1", "e1"],
                "game_id": ["g1", "g1"],
                "team_id": ["a", "b"],
                "player_id": ["p1", "p2"],
                "tossup_id": ["q1", "q1"],
                "T_j": [20, 20],
            }
        )
        result = event_first_buzz_components(event, players, tossups)
        self.assertAlmostEqual(
            result["player_first_buzz_mass"].sum() + result["dead_mass"],
            1.0,
            places=6,
        )
        np.testing.assert_allclose(
            result["player_first_buzz_mass"].sum(axis=0),
            result["first_buzz_mass"],
        )

    def test_survival_metrics_use_supported_numpy_integration(self):
        players, tossups = self._timing_parameters()
        predictions = pd.DataFrame(
            {
                "event_id": ["buzzed", "buzzed", "dead", "dead"],
                "game_id": ["g1", "g1", "g2", "g2"],
                "team_id": ["a", "b", "a", "b"],
                "player_id": ["p1", "p2", "p1", "p2"],
                "tossup_id": ["q1", "q1", "q1", "q1"],
                "T_j": [20, 20, 20, 20],
                "relative_position": [0.25, 0.25, 1.0, 1.0],
                "z": ["BUZZ", "CENSORED", "CENSORED", "CENSORED"],
            }
        )
        with tempfile.TemporaryDirectory() as directory:
            results_dir = Path(directory) / "results"
            output_dir = Path(directory) / "evaluation"
            results_dir.mkdir()
            players.reset_index().to_csv(results_dir / "players.csv", index=False)
            tossups.reset_index().to_csv(results_dir / "tossups.csv", index=False)
            predictions.to_csv(results_dir / "tossup_predictions.csv", index=False)

            metrics = evaluate_survival_and_first_buzzer(results_dir, output_dir)

            self.assertTrue(np.isfinite(metrics["integrated_brier_score"]))
            self.assertEqual(
                set(metrics),
                {
                    "integrated_brier_score",
                    "survival_events",
                    "survival_events_skipped",
                    "first_buzzer_top1_accuracy",
                    "first_buzzer_mean_reciprocal_rank",
                    "first_buzzer_log_loss",
                    "first_buzzer_events",
                },
            )
            self.assertEqual(metrics["survival_events"], 2)
            time_metrics = pd.read_csv(
                output_dir / "csvs" / "tossup_time_metrics.csv"
            )
            self.assertEqual(
                list(time_metrics),
                [
                    "relative_position",
                    "events",
                    "observed_buzz_rate",
                    "predicted_buzz_rate",
                    "brier",
                ],
            )
            buzz_density_fit_plot(results_dir, output_dir)
            density_metrics = pd.read_csv(
                output_dir / "csvs" / "tossup_buzz_density_metrics.csv"
            )
            self.assertEqual(
                list(density_metrics),
                [
                    "tossup_id",
                    "events",
                    "observed_dead_rate",
                    "predicted_dead_rate",
                ],
            )


if __name__ == "__main__":
    unittest.main()
