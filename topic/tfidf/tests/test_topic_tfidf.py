"""Focused checks for fixed and learned topic-specific TF-IDF likelihoods."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import pyro
import torch

from topic.fixed.topic_compirt.pyramidal import correctness_logit as baseline_logit
from topic.tfidf.evaluation import topic_first_buzz_distribution
from topic.tfidf.joint_pyramidal import joint_model
from topic.tfidf.outputs import lambda_mapping, save_adjustment_curves, save_lambdas
from topic.tfidf.pyramidal import (
    competing_risks_model,
    correctness_logit,
    effective_difficulty,
    hazard_logit,
)
from utils.training import fit_svi


class TopicTfidfMathTests(unittest.TestCase):
    def test_one_hot_topic_weight_selects_its_lambda(self):
        logit = correctness_logit(
            torch.zeros((1, 2)),
            torch.tensor([[0.0, 1.0]]),
            torch.zeros((1, 2)),
            torch.zeros((1, 2)),
            torch.full((1, 2), 0.5),
            torch.tensor([1]),
            torch.tensor([2]),
            torch.tensor([0.5]),
            torch.tensor([2.0, 4.0]),
        )
        self.assertTrue(torch.allclose(logit, torch.tensor([2.0])))

    def test_mixed_topic_weight_combines_lambdas(self):
        logit = correctness_logit(
            torch.zeros((1, 2)),
            torch.tensor([[0.25, 0.75]]),
            torch.zeros((1, 2)),
            torch.zeros((1, 2)),
            torch.full((1, 2), 0.5),
            torch.tensor([1]),
            torch.tensor([2]),
            torch.tensor([0.5]),
            torch.tensor([2.0, 4.0]),
        )
        self.assertTrue(torch.allclose(logit, torch.tensor([1.75])))

    def test_zero_prefix_preserves_the_baseline_topic_logit(self):
        arguments = (
            torch.tensor([[1.0, -1.0]]),
            torch.tensor([[0.25, 0.75]]),
            torch.tensor([[2.0, 4.0]]),
            torch.tensor([[1.0, 1.0]]),
            torch.tensor([[0.5, 0.5]]),
            torch.tensor([1]),
            torch.tensor([2]),
        )
        baseline = baseline_logit(*arguments)
        adjusted = correctness_logit(
            *arguments, torch.tensor([0.0]), torch.tensor([2.0, 4.0])
        )
        self.assertTrue(torch.allclose(adjusted, baseline))

    def test_positive_lambda_lowers_difficulty_and_raises_hazard(self):
        beta = torch.zeros((1, 1))
        gamma = torch.zeros((1, 1))
        mu = torch.full((1, 1), 0.5)
        base_difficulty = effective_difficulty(
            beta,
            gamma,
            mu,
            torch.tensor([1]),
            torch.tensor([2]),
            torch.tensor([0.0]),
            torch.tensor([2.0]),
        )
        adjusted_difficulty = effective_difficulty(
            beta,
            gamma,
            mu,
            torch.tensor([1]),
            torch.tensor([2]),
            torch.tensor([0.5]),
            torch.tensor([2.0]),
        )
        base_hazard = torch.sigmoid(
            hazard_logit(
                torch.zeros((1, 1)),
                torch.ones((1, 1)),
                beta,
                gamma,
                mu,
                torch.tensor([0.0]),
                torch.tensor([1]),
                torch.tensor([2]),
                torch.tensor([0.0]),
                torch.tensor([2.0]),
            )
        )
        adjusted_hazard = torch.sigmoid(
            hazard_logit(
                torch.zeros((1, 1)),
                torch.ones((1, 1)),
                beta,
                gamma,
                mu,
                torch.tensor([0.0]),
                torch.tensor([1]),
                torch.tensor([2]),
                torch.tensor([0.5]),
                torch.tensor([2.0]),
            )
        )
        self.assertLess(float(adjusted_difficulty[0, 0]), float(base_difficulty[0, 0]))
        self.assertGreater(float(adjusted_hazard[0]), float(base_hazard[0]))


class TopicTfidfSviTests(unittest.TestCase):
    def setUp(self):
        pyro.clear_param_store()

    @staticmethod
    def _fixed_data():
        return {
            "player": torch.tensor([0]),
            "tossup": torch.tensor([0]),
            "event": torch.tensor([0]),
            "t_star": torch.tensor([1]),
            "T_j": torch.tensor([2]),
            "y": torch.tensor([1.0]),
            "is_buzz": torch.tensor([True]),
            "topic_weight": torch.tensor([[0.25, 0.75]]),
            "tfidf_prefix": torch.tensor([[0.25, 1.0]]),
            "player_ids": ["p1"],
            "tossup_ids": ["q1"],
            "event_ids": ["e1"],
        }

    def test_fixed_topic_svi_learns_a_nonnegative_lambda_per_topic(self):
        posterior, _guide, _losses = fit_svi(
            competing_risks_model,
            model_kwargs={
                "data": self._fixed_data(),
                "calibrate_correctness": False,
                "prior_scale": 1.0,
            },
            n_steps=2,
            lr=0.01,
        )
        self.assertEqual(tuple(posterior["topic_tfidf_lambdas"].shape), (2,))
        self.assertTrue(torch.all(posterior["topic_tfidf_lambdas"] >= 0.0))

    def test_learned_topic_svi_learns_a_nonnegative_lambda_per_topic(self):
        data = self._fixed_data()
        data["bow"] = torch.tensor([[1.0, 1.0, 0.0]])
        posterior, _guide, losses = fit_svi(
            joint_model,
            model_kwargs={
                "data": data,
                "n_dimensions": 2,
                "bow_weight": 1.0,
                "topic_concentration": 1.0,
                "calibrate_correctness": False,
                "prior_scale": 1.0,
            },
            n_steps=2,
            lr=0.01,
        )
        self.assertEqual(len(losses), 2)
        self.assertEqual(tuple(posterior["topic_tfidf_lambdas"].shape), (2,))
        self.assertTrue(torch.all(posterior["topic_tfidf_lambdas"] >= 0.0))


class TopicTfidfOutputTests(unittest.TestCase):
    def test_outputs_record_lambdas_and_weighted_adjustments(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        output_dir = Path(directory.name)
        data = {
            "tossup_ids": ["q1"],
            "tfidf_prefix": torch.tensor([[0.25, 1.0]]),
        }
        observations = pd.DataFrame({"tossup_id": ["q1"], "T_j": [2]})
        weights = torch.tensor([[0.25, 0.75]])
        lambdas = torch.tensor([2.0, 4.0])

        save_lambdas(output_dir, ["topic_a", "topic_b"], lambdas)
        save_adjustment_curves(
            output_dir, data, observations, weights, lambdas, n_points=3
        )

        lambda_frame = pd.read_csv(output_dir / "topic_tfidf_lambdas.csv")
        self.assertEqual(lambda_frame["topic_label"].tolist(), ["topic_a", "topic_b"])
        np.testing.assert_allclose(lambda_frame["lambda_tfidf"], [2.0, 4.0])
        adjustment = pd.read_csv(output_dir / "tfidf_adjustment_curves.csv")
        np.testing.assert_allclose(
            adjustment.filter(like="adjustment_").iloc[0], [-0.875, -0.875, -3.5]
        )
        self.assertEqual(
            lambda_mapping(["topic_a", "topic_b"], lambdas),
            {"topic_a": 2.0, "topic_b": 4.0},
        )

    def test_timing_replay_changes_only_with_saved_adjustments(self):
        event = pd.DataFrame({"tossup_id": ["q1"], "player_id": ["p1"], "T_j": [1]})
        players = pd.DataFrame(
            {"player_id": ["p1"], "theta_1": [0.0], "c": [0.0]}
        ).set_index("player_id")
        tossups = pd.DataFrame(
            {
                "tossup_id": ["q1"],
                "topic_weight_1": [1.0],
                "beta_1": [0.0],
                "gamma_1": [1.0],
                "mu_1": [0.5],
            }
        ).set_index("tossup_id")
        no_adjustment = ({}, np.array([0.0, 1.0]))
        adjustment = ({"q1": np.array([-1.0, -1.0])}, np.array([0.0, 1.0]))
        base_mass, _ = topic_first_buzz_distribution(
            event, players, tossups, no_adjustment, n_bins=1
        )
        adjusted_mass, _ = topic_first_buzz_distribution(
            event, players, tossups, adjustment, n_bins=1
        )
        self.assertGreater(float(adjusted_mass[0]), float(base_mass[0]))


if __name__ == "__main__":
    unittest.main()
