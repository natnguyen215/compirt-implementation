"""Tests for the ranking functionals shared by the drop-robustness runners."""

from __future__ import annotations

import math
import tempfile
import unittest
from pathlib import Path

import pandas as pd
import torch

from compirt_eval.common import player_scoring
from compirt_eval.common.ranking_metrics import compare_rankings
from simple_mirt.train_plain_irt import response_matrix_from_observations


def sigmoid(x: float) -> float:
    return 1.0 / (1.0 + math.exp(-x))


class ActualPpgTests(unittest.TestCase):
    def test_hand_computed_points_and_games(self):
        frame = pd.DataFrame(
            {
                "event_id": ["e1", "e1", "e2", "e3"],
                "game_id": ["g1", "g1", "g2", "g1"],
                "player_id": ["a", "b", "a", "b"],
                "z": ["BUZZ", "CENSORED", "BUZZ", "NO-BUZZ"],
                "y": [1, 0, 0, 0],
            }
        )
        ppg = player_scoring.actual_ppg(frame)
        # a: +10 (correct) - 5 (neg) over 2 games; b: no buzzes over 1 game.
        self.assertAlmostEqual(ppg["a"], (10.0 - 5.0) / 2)
        self.assertAlmostEqual(ppg["b"], 0.0)


class CompareRankingsTests(unittest.TestCase):
    def test_identical_rankings_agree_perfectly(self):
        ppg = pd.Series({f"p{i}": float(30 - i) for i in range(30)})
        result = compare_rankings(ppg, ppg.copy())
        self.assertEqual(result["n_common"], 30)
        self.assertAlmostEqual(result["kendall_tau"], 1.0)
        self.assertAlmostEqual(result["spearman"], 1.0)
        self.assertFalse(result["top1_changed"])
        self.assertAlmostEqual(result["jaccard_top5"], 1.0)
        self.assertAlmostEqual(result["max_displacement_top25"], 0.0)
        self.assertAlmostEqual(result["mean_abs_ppg_change"], 0.0)

    def test_swapped_top_pair_flips_top1_only(self):
        ref = pd.Series({f"p{i}": float(30 - i) for i in range(30)})
        alt = ref.copy()
        alt["p0"], alt["p1"] = ref["p1"], ref["p0"]
        result = compare_rankings(ref, alt)
        self.assertTrue(result["top1_changed"])
        # The top-5 *set* is unchanged even though its order flipped.
        self.assertAlmostEqual(result["jaccard_top5"], 1.0)
        self.assertAlmostEqual(result["max_displacement_top25"], 1.0)

    def test_only_common_players_are_scored(self):
        ref = pd.Series({"a": 3.0, "b": 2.0, "c": 1.0})
        alt = pd.Series({"a": 3.0, "b": 2.0})
        result = compare_rankings(ref, alt, topks=(2,))
        self.assertEqual(result["n_common"], 2)


class LoadPosteriorTests(unittest.TestCase):
    def test_baseline_reads_scalar_difficulty_and_alpha_weight(self):
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            pd.DataFrame(
                {
                    "player_id": ["p1", "p2"],
                    "c": [0.3, 0.1],
                    "theta_1": [0.8, -0.1],
                    "theta_2": [-0.2, 0.4],
                }
            ).to_csv(run_dir / "players.csv", index=False)
            pd.DataFrame(
                {
                    "tossup_id": ["q1"],
                    "beta": [1.2],
                    "gamma": [2.0],
                    "mu": [0.6],
                    "alpha_1": [1.0],
                    "alpha_2": [0.5],
                }
            ).to_csv(run_dir / "tossups.csv", index=False)
            data = {"player_ids": ["p2", "p1"], "tossup_ids": ["q1"]}
            posterior = player_scoring.load_posterior(run_dir, data, "baseline")

        # Rows align to the tensor order (p2 first) and alpha becomes "r".
        self.assertEqual(posterior["theta"].shape, (2, 2))
        self.assertAlmostEqual(float(posterior["theta"][0, 0]), -0.1)
        self.assertEqual(posterior["r"].shape, (1, 2))
        self.assertEqual(posterior["beta"].shape, (1,))
        self.assertAlmostEqual(float(posterior["beta"][0]), 1.2)


def single_event_data(T: float) -> dict:
    """One BUZZ row: one player, one tossup, one event."""
    return {
        "event": torch.tensor([0]),
        "player": torch.tensor([0]),
        "tossup": torch.tensor([0]),
        "T_j": torch.tensor([T]),
        "event_ids": ["g::q"],
        "player_ids": ["p1"],
        "tossup_ids": ["q1"],
    }


class PredictedPointsTests(unittest.TestCase):
    def expected_single_player_points(self, hazard_fn, correct_fn, T: int) -> float:
        """The competing-risks walk collapses to a plain survival sum for a
        roster of one: sum_t S(t-1) * h(t) * (10 p(t) - 5 (1 - p(t)))."""
        survival, points = 1.0, 0.0
        for t in range(1, T + 1):
            h = hazard_fn(t)
            p = correct_fn(t)
            points += survival * h * (10.0 * p - 5.0 * (1.0 - p))
            survival *= 1.0 - h
        return points

    def test_baseline_family_matches_hand_computation(self):
        theta, alpha = [0.8, -0.2], [1.0, 0.5]
        beta, gamma, mu, c, T = 1.2, 2.0, 0.6, 0.3, 2
        posterior = {
            "theta": torch.tensor([theta]),
            "c": torch.tensor([c]),
            "r": torch.tensor([alpha]),
            "beta": torch.tensor([beta]),
            "gamma": torch.tensor([gamma]),
            "mu": torch.tensor([mu]),
        }

        def logit(t):
            skill = sum(a * b for a, b in zip(theta, alpha))
            return skill - beta * sigmoid(gamma * (mu - t / T))

        expected = self.expected_single_player_points(
            lambda t: sigmoid(logit(t) - c), lambda t: sigmoid(logit(t)), T
        )
        points = player_scoring.predicted_player_points(
            single_event_data(float(T)), posterior, "baseline"
        )
        self.assertAlmostEqual(float(points[0]), expected, places=5)

    def test_multidim_family_matches_hand_computation(self):
        theta, r = [0.5, 1.0], [0.7, 0.3]
        beta, gamma, mu = [1.0, 0.4], [2.0, 1.0], [0.5, 0.3]
        c, T = 0.2, 3
        posterior = {
            "theta": torch.tensor([theta]),
            "c": torch.tensor([c]),
            "r": torch.tensor([r]),
            "beta": torch.tensor([beta]),
            "gamma": torch.tensor([gamma]),
            "mu": torch.tensor([mu]),
        }

        def logit(t):
            return sum(
                r[k] * (theta[k] - beta[k] * sigmoid(gamma[k] * (mu[k] - t / T)))
                for k in range(2)
            )

        expected = self.expected_single_player_points(
            lambda t: sigmoid(logit(t) - c), lambda t: sigmoid(logit(t)), T
        )
        points = player_scoring.predicted_player_points(
            single_event_data(float(T)), posterior, "multidim", link="sigmoid"
        )
        self.assertAlmostEqual(float(points[0]), expected, places=5)


class PlainIrtTests(unittest.TestCase):
    def observation_frame(self) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "event_id": ["e1", "e1", "e2"],
                "game_id": ["g1", "g1", "g2"],
                "player_id": ["a", "b", "a"],
                "tossup_id": ["q1", "q1", "q2"],
                "z": ["BUZZ", "CENSORED", "BUZZ"],
                "y": [1, 0, 0],
            }
        )

    def test_response_matrix_construction(self):
        responses, mask, player_ids, tossup_ids = response_matrix_from_observations(
            self.observation_frame()
        )
        self.assertEqual(player_ids, ["a", "b"])
        self.assertEqual(tossup_ids, ["q1", "q2"])
        # a converted q1, heard q2 without converting; b heard only q1.
        self.assertEqual(responses[0].tolist(), [1.0, 0.0])
        self.assertEqual(mask[0].tolist(), [True, True])
        self.assertEqual(responses[1].tolist(), [0.0, 0.0])
        self.assertEqual(mask[1].tolist(), [True, False])

    def test_expected_ppg_matches_hand_computation(self):
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory)
            pd.DataFrame(
                {"player_id": ["a", "b"], "theta_1": [1.0, -0.5]}
            ).to_csv(run_dir / "players.csv", index=False)
            pd.DataFrame(
                {"tossup_id": ["q1", "q2"], "d": [0.2, 0.8], "alpha_1": [0.9, 1.1]}
            ).to_csv(run_dir / "questions.csv", index=False)
            observations = self.observation_frame()
            games = observations.groupby("player_id")["game_id"].nunique()
            ppg = player_scoring.plain_irt_expected_ppg(
                run_dir, observations, games
            )

        # a: cells (q1, q2) over 2 games; b: cell (q1,) over 1 game.
        expected_a = 10.0 * (
            sigmoid(1.0 * 0.9 - 0.2) + sigmoid(1.0 * 1.1 - 0.8)
        ) / 2
        expected_b = 10.0 * sigmoid(-0.5 * 0.9 - 0.2)
        self.assertAlmostEqual(ppg["a"], expected_a, places=5)
        self.assertAlmostEqual(ppg["b"], expected_b, places=5)


if __name__ == "__main__":
    unittest.main()
