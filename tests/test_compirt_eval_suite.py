"""Focused tests for the end-to-end CompIRT evaluation additions."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from pyro.infer import Predictive

from compirt_eval.synergy_comparison import LOWER_IS_BETTER, NON_COMPARATIVE_METRICS
from compirt_eval.common.metrics import (
    binary_brier_score,
    classification_metrics,
    negative_class_metrics,
    ranked_probability_score,
    stratified_prediction_metrics,
)
from compirt_eval.diagnostics.match_simulation import _game_model, simulate_match_winners
from compirt_eval.parameter_recovery import generate_recovery_data
from compirt_eval.scenario_a_tossups.timing import (
    _full_pmf_score_row,
    buzz_density_fit_plot,
    evaluate_survival_and_first_buzzer,
    event_first_buzz_components,
)
from compirt_eval.scenario_a_tossups.metrics import tossup_joint_event_scores
from compirt_eval.scenario_b_bonuses.metrics import (
    bonus_ranked_probability_scores,
    bonus_score_distribution,
)


class ProperScoreTests(unittest.TestCase):
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

    def test_comparison_directions_handle_new_metrics(self):
        self.assertTrue(
            {
                "brier",
                "ranked_probability_score",
                "bonus_total_score_log_loss",
            }.issubset(LOWER_IS_BETTER)
        )
        self.assertIn("probability_std", NON_COMPARATIVE_METRICS)

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

        self.assertAlmostEqual(
            scores.loc["buzzed", "joint_event_probability"],
            0.8 * 0.9 * 0.25 * 0.7,
        )
        self.assertAlmostEqual(
            scores.loc["dead", "joint_event_probability"], 0.6 * 0.5
        )
        self.assertAlmostEqual(
            scores.loc["buzzed", "joint_event_log_loss"],
            -np.log(0.8 * 0.9 * 0.25 * 0.7),
        )
        self.assertEqual(scores.loc["dead", "observed_outcome"], "dead")

    def test_strata_include_aggregate_and_sharpness(self):
        frame = pd.DataFrame(
            {"y": [0, 1, 1, 0], "p": [0.1, 0.8, 0.7, 0.3], "tier": ["a", "a", "b", "b"]}
        )
        result = stratified_prediction_metrics(
            frame, "y", "p", "test", {"tier": "tier"}
        )
        self.assertEqual(set(result["stratum"]), {"aggregate", "tier"})
        self.assertIn("mean_predictive_variance", result)


class SeededGameSimulationTests(unittest.TestCase):
    def test_pyro_generative_process_scores_buzzes_bonuses_and_dead_tossups(self):
        def event(first_buzz, correct, team_slot, bonus):
            return {
                "first_buzz": torch.tensor(first_buzz, dtype=torch.float32),
                "correct": torch.tensor([correct], dtype=torch.float32),
                "team_slot": torch.tensor([team_slot]),
                "bonus": torch.tensor(bonus, dtype=torch.float32),
            }

        events = [
            event([1, 0], 1, 1, [[1, 0, 0, 0], [0, 0, 0, 1]]),
            event([1, 0], 0, 0, [[1, 0, 0, 0], [1, 0, 0, 0]]),
            event([0, 1], 1, 0, [[0, 1, 0, 0], [1, 0, 0, 0]]),
        ]

        scores = Predictive(
            _game_model,
            num_samples=1,
            return_sites=("_RETURN",),
            parallel=True,
        )(events)["_RETURN"]

        torch.testing.assert_close(scores, torch.tensor([[-5.0, 40.0]]))

    def test_complete_seeded_game_output_is_deterministic(self):
        players = pd.DataFrame(
            {
                "player_id": ["p1", "p2"],
                "c": [1.5, 1.8],
                "theta_1": [0.7, 0.3],
            }
        )
        tossups = pd.DataFrame(
            {
                "tossup_id": ["q1"],
                "alpha_1": [1.0],
                "beta": [0.8],
                "gamma": [7.0],
                "mu": [0.5],
            }
        )
        predictions = pd.DataFrame(
            {
                "event_id": ["e1", "e1"],
                "game_id": ["g1", "g1"],
                "team_id": ["a", "b"],
                "player_id": ["p1", "p2"],
                "tossup_id": ["q1", "q1"],
                "T_j": [20, 20],
                "tier": ["Open", "Open"],
                "z": ["BUZZ", "CENSORED"],
            }
        )
        bonus_parts = pd.DataFrame(
            {
                "response_id": ["r1"] * 3 + ["r2"] * 3,
                "team_id": ["a"] * 3 + ["b"] * 3,
                "tier": ["Open"] * 6,
                "part_index": [0, 1, 2, 0, 1, 2],
                "correct": [1, 1, 0, 1, 0, 0],
                "predicted_correct": [0.8, 0.7, 0.4, 0.6, 0.3, 0.2],
            }
        )
        games = pd.DataFrame(
            {
                "game_id": ["g1"],
                "team_ids": [["a", "b"]],
                "final_scores": [[200, 150]],
            }
        )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pyramidal = root / "pyramidal"
            compositional = root / "compositional"
            pyramidal.mkdir()
            compositional.mkdir()
            players.to_csv(pyramidal / "players.csv", index=False)
            tossups.to_csv(pyramidal / "tossups.csv", index=False)
            predictions.to_csv(pyramidal / "tossup_predictions.csv", index=False)
            bonus_parts.to_csv(
                compositional / "bonus_part_predictions.csv", index=False
            )

            first_metrics, first = simulate_match_winners(
                pyramidal, compositional, root / "first", games,
                simulations=64, seed=17,
            )
            second_metrics, second = simulate_match_winners(
                pyramidal, compositional, root / "second", games,
                simulations=64, seed=17,
            )

        pd.testing.assert_frame_equal(first, second)
        self.assertEqual(first_metrics, second_metrics)
        self.assertEqual(
            first.columns.tolist(),
            [
                "game_id", "team_1_id", "team_2_id",
                "actual_team_1_score", "actual_team_2_score",
                "predicted_team_1_score", "predicted_team_2_score",
                "team_1_win_probability", "actual_winner", "predicted_winner",
                "winner_correct", "usable_tossups", "simulations",
            ],
        )
        self.assertTrue(first["team_1_win_probability"].between(0, 1).all())
        self.assertEqual(first["simulations"].tolist(), [64])


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

    def test_recovery_generator_emits_model_rows(self):
        observations, truth = generate_recovery_data(
            players=6, tossups=4, events=6, seed=7
        )
        self.assertEqual(set(truth), {"theta", "c", "r", "beta", "gamma", "mu"})
        self.assertEqual(observations["event_id"].nunique(), 6)
        self.assertTrue(set(observations["z"]).issubset({"BUZZ", "CENSORED", "NO-BUZZ"}))


if __name__ == "__main__":
    unittest.main()
