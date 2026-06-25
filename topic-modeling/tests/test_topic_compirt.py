"""Tests for the isolated topic-weighted CompIRT implementation."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import torch

from topic_compirt.compositional import (
    compositional_model as topic_compositional_model,
    posterior_predictions as topic_posterior_predictions,
    topic_weighted_member_abilities,
    topic_weighted_part_difficulty,
)
from topic_compirt.common import fit_svi
from topic_compirt.evaluation import topic_first_buzz_distribution
from topic_compirt.pyramidal import (
    competing_risks_model,
    correctness_logit,
    topic_weighted_skill,
)
from topic_compirt.topics import (
    align_bonus_topic_weights,
    align_topic_vectors,
    align_tossup_topic_weights,
    bonus_id_from_part_id,
    load_topic_dataframe,
)
from topic_utils.categories import UNKNOWN, top_level_category
from topic_utils.corpus import clean_text, tokenize
from topic_utils.outputs import (
    DEFAULT_LDA_OUTPUT_DIR,
    DEFAULT_PLDA_OUTPUT_DIR,
    DEFAULT_TOPIC_VECTORS,
    load_dimension_labels,
)


class TopicVectorTests(unittest.TestCase):
    def write_topic_csv(self, rows) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "topics.csv"
        pd.DataFrame(rows).to_csv(path, index=False)
        return path

    def test_load_topic_dataframe_normalizes_and_sorts_columns(self):
        path = self.write_topic_csv(
            [
                {
                    "document_id": "tossup-a",
                    "question_type": "tossup",
                    "latent_topic_01": 2.0,
                    "latent_topic_00": 2.0,
                },
                {
                    "document_id": "bonus-a",
                    "question_type": "bonus",
                    "latent_topic_01": 3.0,
                    "latent_topic_00": 1.0,
                },
            ]
        )

        frame, columns = load_topic_dataframe(path, question_type="tossup")

        self.assertEqual(columns, ["latent_topic_00", "latent_topic_01"])
        np.testing.assert_allclose(
            frame.loc["tossup-a", columns].to_numpy(dtype=float), [0.5, 0.5]
        )

    def test_align_tossup_topic_weights_matches_data_order(self):
        path = self.write_topic_csv(
            [
                {
                    "document_id": "tossup-a",
                    "question_type": "tossup",
                    "latent_topic_00": 1.0,
                    "latent_topic_01": 0.0,
                },
                {
                    "document_id": "tossup-b",
                    "question_type": "tossup",
                    "latent_topic_00": 0.0,
                    "latent_topic_01": 2.0,
                },
            ]
        )
        data = {
            "tossup_ids": ["tossup-b", "tossup-a"],
            "y": torch.zeros(2),
        }

        weights, columns = align_tossup_topic_weights(data, path)

        self.assertEqual(columns, ["latent_topic_00", "latent_topic_01"])
        self.assertEqual(weights.tolist(), [[0.0, 1.0], [1.0, 0.0]])

    def test_bonus_part_ids_align_to_base_bonus_ids(self):
        path = self.write_topic_csv(
            [
                {
                    "document_id": "bonus-a",
                    "question_type": "bonus",
                    "latent_topic_00": 1.0,
                    "latent_topic_01": 0.0,
                },
                {
                    "document_id": "bonus-b",
                    "question_type": "bonus",
                    "latent_topic_00": 1.0,
                    "latent_topic_01": 3.0,
                },
            ]
        )
        data = {
            "part_ids": ["bonus-b::part-3", "bonus-a::part-1"],
            "y": torch.zeros(2),
        }

        weights, _ = align_bonus_topic_weights(data, path)

        self.assertEqual(bonus_id_from_part_id("bonus-b::part-3"), "bonus-b")
        self.assertEqual(weights.tolist(), [[0.25, 0.75], [1.0, 0.0]])

    def test_missing_ids_and_dimension_mismatch_are_errors(self):
        path = self.write_topic_csv(
            [
                {
                    "document_id": "tossup-a",
                    "question_type": "tossup",
                    "latent_topic_00": 1.0,
                    "latent_topic_01": 1.0,
                }
            ]
        )
        frame, columns = load_topic_dataframe(path, question_type="tossup")

        with self.assertRaisesRegex(ValueError, "Missing topic vectors"):
            align_topic_vectors(frame, columns, ["missing"], id_label="tossup_id")
        with self.assertRaisesRegex(ValueError, "Expected 3 topic dimensions"):
            load_topic_dataframe(path, question_type="tossup", expected_dimensions=3)

    def test_empty_question_type_filter_is_an_error(self):
        path = self.write_topic_csv(
            [
                {
                    "document_id": "bonus-a",
                    "question_type": "bonus",
                    "latent_topic_00": 1.0,
                    "latent_topic_01": 1.0,
                }
            ]
        )

        with self.assertRaisesRegex(ValueError, "question_type='tossup'"):
            load_topic_dataframe(path, question_type="tossup")

    def test_nan_and_zero_mass_rows_are_errors(self):
        nan_path = self.write_topic_csv(
            [
                {
                    "document_id": "tossup-a",
                    "question_type": "tossup",
                    "latent_topic_00": np.nan,
                    "latent_topic_01": 1.0,
                }
            ]
        )
        zero_path = self.write_topic_csv(
            [
                {
                    "document_id": "tossup-a",
                    "question_type": "tossup",
                    "latent_topic_00": 0.0,
                    "latent_topic_01": 0.0,
                }
            ]
        )

        with self.assertRaisesRegex(ValueError, "NaN or infinite"):
            load_topic_dataframe(nan_path, question_type="tossup")
        with self.assertRaisesRegex(ValueError, "zero total mass"):
            load_topic_dataframe(zero_path, question_type="tossup")


class TopicUtilityTests(unittest.TestCase):
    def test_topic_output_defaults_use_stable_directories(self):
        self.assertEqual(DEFAULT_PLDA_OUTPUT_DIR.name, "plda")
        self.assertEqual(DEFAULT_LDA_OUTPUT_DIR.name, "lda")
        self.assertEqual(
            DEFAULT_TOPIC_VECTORS,
            DEFAULT_PLDA_OUTPUT_DIR / "document_latent_vectors.csv",
        )

    def test_tokenizer_strips_html_and_boilerplate(self):
        text = "<p>Napoleon&nbsp;called this question.</p>"

        self.assertEqual(clean_text(text), "Napoleon called this question.")
        self.assertEqual(tokenize(text), ["napoleon"])

    def test_category_and_dimension_label_helpers(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "category_index.csv"
        pd.DataFrame(
            [
                {"dimension": 0, "column": "latent_topic_00", "category": "Science"},
                {"dimension": 1, "column": "latent_topic_01", "category": "History"},
            ]
        ).to_csv(path, index=False)

        self.assertEqual(
            top_level_category("category:Painting & Sculpture|subcategory:Painting"),
            "Fine Arts",
        )
        self.assertEqual(top_level_category(""), UNKNOWN)
        self.assertEqual(load_dimension_labels(path), {1: "Science", 2: "History"})


class TopicWeightedMathTests(unittest.TestCase):
    def test_one_hot_topic_weight_selects_one_dimension(self):
        theta = torch.tensor([[2.0, 3.0]])
        topic_weight = torch.tensor([[0.0, 1.0]])

        skill = topic_weighted_skill(theta, topic_weight)

        self.assertEqual(skill.tolist(), [3.0])

    def test_uniform_topic_weight_gates_all_dimensions(self):
        theta = torch.tensor([[2.0, 3.0]])
        topic_weight = torch.tensor([[0.5, 0.5]])

        skill = topic_weighted_skill(theta, topic_weight)

        self.assertEqual(skill.tolist(), [2.5])

    def test_correctness_logit_weights_per_topic_gap(self):
        theta = torch.tensor([[10.0, 0.0]])
        topic_weight = torch.tensor([[0.25, 0.75]])
        beta = torch.tensor([[4.0, 8.0]])
        gamma = torch.tensor([[0.0, 0.0]])
        mu = torch.tensor([[0.5, 0.5]])
        t = torch.tensor([1])
        T_j = torch.tensor([2])

        logit = correctness_logit(theta, topic_weight, beta, gamma, mu, t, T_j)

        # gamma=0 makes d_k(t)=0.5*beta_k, so this is
        # 0.25*(10-2) + 0.75*(0-4).
        self.assertTrue(torch.allclose(logit, torch.tensor([-1.0])))

    def test_bonus_member_abilities_use_part_topic_weights(self):
        member_theta = torch.tensor([[[2.0, 3.0], [4.0, 5.0]]])
        topic_weight = torch.tensor([[1.0, 0.0]])

        abilities = topic_weighted_member_abilities(member_theta, topic_weight)

        self.assertEqual(abilities.tolist(), [[2.0, 4.0]])

    def test_bonus_part_difficulty_uses_part_topic_weights(self):
        beta = torch.tensor([[2.0, 6.0]])
        topic_weight = torch.tensor([[0.25, 0.75]])

        difficulty = topic_weighted_part_difficulty(beta, topic_weight)

        self.assertEqual(difficulty.tolist(), [5.0])

    def test_topic_first_buzz_distribution_uses_topic_weights(self):
        event = pd.DataFrame(
            {
                "tossup_id": ["q1"],
                "player_id": ["p1"],
                "T_j": [1],
            }
        )
        players = pd.DataFrame(
            {
                "player_id": ["p1"],
                "theta_1": [2.0],
                "theta_2": [4.0],
                "c": [0.0],
            }
        ).set_index("player_id")
        tossups = pd.DataFrame(
            {
                "tossup_id": ["q1"],
                "topic_weight_1": [0.25],
                "topic_weight_2": [0.75],
                "beta_1": [0.0],
                "beta_2": [0.0],
                "gamma_1": [1.0],
                "gamma_2": [1.0],
                "mu_1": [0.5],
                "mu_2": [0.5],
            }
        ).set_index("tossup_id")

        mass, dead = topic_first_buzz_distribution(event, players, tossups, n_bins=1)

        expected_hazard = 1 / (1 + np.exp(-3.5))
        self.assertAlmostEqual(float(mass[0]), expected_hazard)
        self.assertAlmostEqual(dead, 1 - expected_hazard)

    def test_pyramidal_svi_posterior_uses_vector_difficulty_without_alpha(self):
        data = {
            "player": torch.tensor([0]),
            "tossup": torch.tensor([0]),
            "event": torch.tensor([0]),
            "t_star": torch.tensor([1]),
            "T_j": torch.tensor([1]),
            "y": torch.tensor([1.0]),
            "is_buzz": torch.tensor([True]),
            "topic_weight": torch.tensor([[0.25, 0.75]]),
            "player_ids": ["p1"],
            "tossup_ids": ["q1"],
            "event_ids": ["e1"],
        }

        posterior, _ = fit_svi(
            competing_risks_model, (data, 2, False), n_steps=1, lr=0.01
        )

        self.assertNotIn("alpha", posterior)
        self.assertEqual(tuple(posterior["beta"].shape), (1, 2))
        self.assertEqual(tuple(posterior["gamma"].shape), (1, 2))
        self.assertEqual(tuple(posterior["mu"].shape), (1, 2))

    def test_compositional_svi_posterior_uses_vector_difficulty_without_alpha(self):
        data = {
            "part": torch.tensor([0]),
            "roster": torch.tensor([[0, 1]]),
            "roster_mask": torch.tensor([[True, True]]),
            "y": torch.tensor([1.0]),
            "topic_weight": torch.tensor([[0.25, 0.75]]),
            "part_ids": ["b1::part-1"],
        }
        theta = torch.tensor([[2.0, 4.0], [0.0, 1.0]])

        posterior, _ = fit_svi(
            topic_compositional_model, (data, theta, True, 1, True), n_steps=1, lr=0.01
        )
        probabilities, aggregate, synergy = topic_posterior_predictions(
            data, theta, posterior, use_synergy=True, calibrate_correctness=True
        )

        self.assertNotIn("alpha", posterior)
        self.assertEqual(tuple(posterior["beta"].shape), (1, 2))
        self.assertIn("psi", posterior)
        self.assertIn("correctness_scale", posterior)
        self.assertEqual(tuple(probabilities.shape), (1,))
        self.assertEqual(tuple(aggregate.shape), (1,))
        self.assertEqual(tuple(synergy.shape), (1,))


if __name__ == "__main__":
    unittest.main()
