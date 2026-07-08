"""Tests for the embedding-relevance CompIRT variant.

These use tiny synthetic embedding tensors throughout -- Qwen3-Embedding-8B is
never loaded or called in tests, only 'project_relevance' and the Pyro models
that consume its output.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import numpy as np
import pyro
import torch
from pyro.infer import SVI, Trace_ELBO
from pyro.infer.autoguide import AutoNormal
from pyro.optim import ClippedAdam

import multidimensional.multidim_mirt.pyramidal_model as multidim_pyramidal_model
from multidimensional.embedding_mirt.compositional_model import (
    compositional_model,
    embedding_weighted_member_abilities,
    embedding_weighted_part_difficulty,
    posterior_predictions,
)
from multidimensional.embedding_mirt.embeddings import (
    align_bonus_embeddings,
    align_tossup_embeddings,
    center_embeddings,
    check_projection_shapes,
    load_embedding_cache,
    load_projection,
    load_projection_state,
    save_projection,
)
from multidimensional.embedding_mirt.pyramidal_model import (
    competing_risks_model,
    correctness_logit,
    hazard_logit,
    project_relevance,
)


def _fit(model, args, n_steps=1, lr=0.01):
    """Run a couple of SVI steps and return the posterior medians."""
    pyro.clear_param_store()
    guide = AutoNormal(model)
    svi = SVI(model, guide, ClippedAdam({"lr": lr}), loss=Trace_ELBO())
    for _ in range(n_steps):
        svi.step(*args)
    return guide.median(*args)


class ProjectRelevanceTests(unittest.TestCase):
    def test_output_is_a_relevance_distribution(self):
        embedding = torch.randn(4, 8)
        weight = torch.randn(8, 5)
        bias = torch.randn(5)

        r = project_relevance(embedding, weight, bias)

        self.assertEqual(tuple(r.shape), (4, 5))
        self.assertTrue(torch.allclose(r.sum(-1), torch.ones(4), atol=1e-5))
        self.assertTrue((r >= 0).all())

    def test_ffn_projection_output_is_a_relevance_distribution(self):
        embedding = torch.randn(4, 8)
        projection = {
            "kind": "ffn",
            "input_weight": torch.randn(8, 3),
            "hidden_bias": torch.randn(3),
            "output_weight": torch.randn(3, 5),
            "output_bias": torch.randn(5),
        }

        r = project_relevance(embedding, projection)

        self.assertEqual(tuple(r.shape), (4, 5))
        self.assertTrue(torch.allclose(r.sum(-1), torch.ones(4), atol=1e-5))
        self.assertTrue((r >= 0).all())

    def test_shares_math_with_multidim_mirt(self):
        # The whole point of this variant is reusing multidim_mirt's competing-
        # risks math unchanged -- guard that the imports really are the same
        # functions, not accidental reimplementations that could drift apart.
        self.assertIs(correctness_logit, multidim_pyramidal_model.correctness_logit)
        self.assertIs(hazard_logit, multidim_pyramidal_model.hazard_logit)


class EmbeddingCacheTests(unittest.TestCase):
    def write_cache(self, ids, embeddings) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "embeddings.npz"
        np.savez(path, ids=np.array(ids, dtype=object), embeddings=embeddings)
        return path

    def test_align_tossup_embeddings_matches_data_order(self):
        path = self.write_cache(
            ["q2", "q1"], np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
        )
        data = {"y": torch.tensor([0.0]), "tossup_ids": ["q1", "q2"]}

        embedding = align_tossup_embeddings(data, path)

        self.assertTrue(torch.allclose(embedding, torch.tensor([[3.0, 4.0], [1.0, 2.0]])))

    def test_align_bonus_embeddings_shares_one_vector_across_parts(self):
        path = self.write_cache(["b1"], np.array([[5.0, 6.0]], dtype=np.float32))
        data = {
            "y": torch.tensor([0.0]),
            "part_ids": ["b1::part-1", "b1::part-2", "b1::part-3"],
        }

        embedding = align_bonus_embeddings(data, path)

        self.assertEqual(tuple(embedding.shape), (3, 2))
        self.assertTrue(torch.allclose(embedding[0], embedding[1]))
        self.assertTrue(torch.allclose(embedding[1], embedding[2]))

    def test_missing_id_is_an_error(self):
        path = self.write_cache(["q1"], np.array([[1.0, 2.0]], dtype=np.float32))
        data = {"y": torch.tensor([0.0]), "tossup_ids": ["q1", "q2"]}

        with self.assertRaises(ValueError):
            align_tossup_embeddings(data, path)

    def test_duplicate_id_is_an_error(self):
        path = self.write_cache(
            ["q1", "q1"], np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)
        )

        with self.assertRaises(ValueError):
            load_embedding_cache(path)

    def test_non_finite_embedding_is_an_error(self):
        path = self.write_cache(["q1"], np.array([[1.0, float("nan")]], dtype=np.float32))

        with self.assertRaises(ValueError):
            load_embedding_cache(path)

    def test_save_and_load_projection_round_trips(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "r_projection.npz"
        weight = torch.randn(8, 5)
        bias = torch.randn(5)

        save_projection(path, weight, bias)
        loaded_weight, loaded_bias = load_projection(path)

        self.assertTrue(torch.allclose(loaded_weight, weight))
        self.assertTrue(torch.allclose(loaded_bias, bias))

    def test_save_and_load_ffn_projection_state_round_trips(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "r_projection.npz"
        projection = {
            "kind": "ffn",
            "input_weight": torch.randn(8, 3),
            "hidden_bias": torch.randn(3),
            "output_weight": torch.randn(3, 5),
            "output_bias": torch.randn(5),
        }
        embedding_mean = torch.randn(8)

        save_projection(path, projection, embedding_mean=embedding_mean)
        loaded_projection, loaded_mean = load_projection_state(path)

        self.assertEqual(loaded_projection["kind"], "ffn")
        self.assertTrue(torch.allclose(loaded_projection["input_weight"], projection["input_weight"]))
        self.assertTrue(torch.allclose(loaded_projection["hidden_bias"], projection["hidden_bias"]))
        self.assertTrue(torch.allclose(loaded_projection["output_weight"], projection["output_weight"]))
        self.assertTrue(torch.allclose(loaded_projection["output_bias"], projection["output_bias"]))
        self.assertTrue(torch.allclose(loaded_mean, embedding_mean))

    def test_center_embeddings_subtracts_saved_mean(self):
        embedding = torch.tensor([[3.0, 5.0], [7.0, 11.0]])
        embedding_mean = torch.tensor([1.0, 2.0])

        centered = center_embeddings(embedding, embedding_mean)

        self.assertTrue(torch.allclose(centered, torch.tensor([[2.0, 3.0], [6.0, 9.0]])))


class CheckProjectionShapesTests(unittest.TestCase):
    def test_matching_shapes_pass(self):
        weight = torch.randn(8, 5)
        embedding = torch.randn(3, 8)
        theta = torch.randn(4, 5)

        check_projection_shapes(
            weight,
            embedding,
            theta,
            projection_path="r_projection.npz",
            embeddings_path="bonus_embeddings.npz",
            player_skills_path="players.csv",
        )

    def test_matching_ffn_shapes_pass(self):
        projection = {
            "kind": "ffn",
            "input_weight": torch.randn(8, 3),
            "hidden_bias": torch.randn(3),
            "output_weight": torch.randn(3, 5),
            "output_bias": torch.randn(5),
        }
        embedding = torch.randn(3, 8)
        theta = torch.randn(4, 5)

        check_projection_shapes(
            projection,
            embedding,
            theta,
            projection_path="r_projection.npz",
            embeddings_path="bonus_embeddings.npz",
            player_skills_path="players.csv",
            embedding_mean=torch.randn(8),
        )

    def test_embed_dim_mismatch_is_an_error(self):
        weight = torch.randn(8, 5)
        embedding = torch.randn(3, 16)
        theta = torch.randn(4, 5)

        with self.assertRaises(ValueError):
            check_projection_shapes(
                weight,
                embedding,
                theta,
                projection_path="r_projection.npz",
                embeddings_path="bonus_embeddings.npz",
                player_skills_path="players.csv",
            )

    def test_relevance_dimension_mismatch_is_an_error(self):
        weight = torch.randn(8, 5)
        embedding = torch.randn(3, 8)
        theta = torch.randn(4, 1)

        with self.assertRaises(ValueError):
            check_projection_shapes(
                weight,
                embedding,
                theta,
                projection_path="r_projection.npz",
                embeddings_path="bonus_embeddings.npz",
                player_skills_path="players.csv",
            )


class PyramidalSviTests(unittest.TestCase):
    def test_svi_posterior_has_no_alpha_and_fits_a_projection(self):
        data = {
            "player": torch.tensor([0]),
            "tossup": torch.tensor([0]),
            "event": torch.tensor([0]),
            "t_star": torch.tensor([1]),
            "T_j": torch.tensor([1]),
            "y": torch.tensor([1.0]),
            "is_buzz": torch.tensor([True]),
            "embedding": torch.randn(1, 8),
            "projection_hidden_dim": 3,
            "player_ids": ["p1"],
            "tossup_ids": ["q1"],
            "event_ids": ["e1"],
        }

        posterior = _fit(competing_risks_model, (data, 2, False))

        self.assertNotIn("alpha", posterior)
        self.assertNotIn("r", posterior)
        self.assertEqual(tuple(posterior["beta"].shape), (1, 2))
        self.assertEqual(tuple(pyro.param("r_projection_input_weight").shape), (8, 3))
        self.assertEqual(tuple(pyro.param("r_projection_hidden_bias").shape), (3,))
        self.assertEqual(tuple(pyro.param("r_projection_output_weight").shape), (3, 2))
        self.assertEqual(tuple(pyro.param("r_projection_output_bias").shape), (2,))


class CompositionalTests(unittest.TestCase):
    def test_member_abilities_and_difficulty_use_bonus_relevance(self):
        member_theta = torch.tensor([[[2.0, 3.0], [4.0, 5.0]]])
        r = torch.tensor([[1.0, 0.0]])

        abilities = embedding_weighted_member_abilities(member_theta, r)
        self.assertTrue(torch.allclose(abilities, torch.tensor([[2.0, 4.0]])))

        beta = torch.tensor([[2.0, 6.0]])
        difficulty = embedding_weighted_part_difficulty(beta, r)
        self.assertTrue(torch.allclose(difficulty, torch.tensor([2.0])))

    def test_svi_posterior_uses_frozen_relevance(self):
        data = {
            "part": torch.tensor([0]),
            "roster": torch.tensor([[0, 1]]),
            "roster_mask": torch.tensor([[True, True]]),
            "y": torch.tensor([1.0]),
            "part_ids": ["b1::part-1"],
        }
        theta = torch.tensor([[2.0, 4.0], [0.0, 1.0]])
        r = torch.tensor([[0.25, 0.75]])

        posterior = _fit(compositional_model, (data, theta, r, True, 1, True))
        probabilities, aggregate, synergy = posterior_predictions(
            data, theta, r, posterior, use_synergy=True, calibrate_correctness=True
        )

        self.assertEqual(tuple(probabilities.shape), (1,))
        self.assertTrue(bool(torch.isfinite(probabilities).all()))
        self.assertTrue(bool(torch.isfinite(aggregate).all()))
        self.assertTrue(bool(torch.isfinite(synergy).all()))


if __name__ == "__main__":
    unittest.main()
