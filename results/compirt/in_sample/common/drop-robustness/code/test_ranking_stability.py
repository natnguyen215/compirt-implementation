"""Tests for the ranking functionals shared by the drop-robustness runners."""

from __future__ import annotations

import math
import tempfile
import unittest
from pathlib import Path

import pandas as pd
import torch

from compirt_eval.common import player_scoring
from compirt_eval.common.ranking_metrics import compare_rankings, topk_jaccard


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
                "actual_player_tossup_points": [10, 0, -5, 0],
            }
        )
        ppg = player_scoring.actual_ppg(frame)
        # a: +10 (correct) - 5 (neg) over 2 games; b: no buzzes over 1 game.
        self.assertAlmostEqual(ppg["a"], (10.0 - 5.0) / 2)
        self.assertAlmostEqual(ppg["b"], 0.0)


class CompareRankingsTests(unittest.TestCase):
    def test_topk_selects_from_shared_players(self):
        ref = pd.Series({"only_ref": 100.0, "a": 3.0, "b": 2.0})
        alt = pd.Series({"only_alt": 100.0, "a": 3.0, "b": 2.0})
        self.assertEqual(topk_jaccard(ref, alt, 1), 1.0)
        self.assertEqual(topk_jaccard(-ref, -alt, 1, higher_is_better=False), 1.0)
        comparison = compare_rankings(ref, alt, topks=(1,))
        self.assertEqual(comparison["n_common"], 2)
        self.assertEqual(comparison["jaccard_top1"], 1.0)

    def test_disjoint_rankings_report_undefined_agreement(self):
        ref = pd.Series({"a": 3.0})
        alt = pd.Series({"b": 2.0})
        self.assertTrue(math.isnan(topk_jaccard(ref, alt, 5)))
        result = compare_rankings(ref, alt)
        self.assertEqual(result["n_common"], 0)
        for metric, value in result.items():
            if metric != "n_common":
                self.assertTrue(math.isnan(value), metric)

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
        """Hand-computed first threshold crossing and score."""
        for t in range(1, T + 1):
            if hazard_fn(t) >= 0.5:
                return 10.0 if correct_fn(t) >= 0.5 else (-5.0 if t < T else 0.0)
        return 0.0

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

    def test_replay_correctness_uses_saved_calibration(self):
        posterior = {
            "theta": torch.tensor([[-0.1]]), "c": torch.tensor([-1.0]),
            "r": torch.tensor([[1.0]]), "beta": torch.tensor([0.0]),
            "gamma": torch.tensor([1.0]), "mu": torch.tensor([0.5]),
        }
        data = single_event_data(2)
        self.assertEqual(float(player_scoring.predicted_player_points(data, posterior, "baseline")[0]), -5)
        posterior["correctness_bias"] = 1.0
        self.assertEqual(float(player_scoring.predicted_player_points(data, posterior, "baseline")[0]), 10)

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


if __name__ == "__main__":
    unittest.main()
