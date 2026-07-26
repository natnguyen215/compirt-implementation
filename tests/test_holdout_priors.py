"""Tests for the held-out (temporal) player-prior construction."""

import unittest

import pandas as pd
import torch

from holdout.player_priors import (
    build_prior_tensors,
    estimate_tier_priors,
    player_tier_map,
)


def train_posterior_frame():
    """A two-dimensional training posterior with a tier label per player."""
    return pd.DataFrame(
        {
            "theta_1_loc": [2.0, 2.2, -1.0, -1.2],
            "theta_2_loc": [0.5, 0.7, -0.5, -0.3],
            "theta_1_scale": [0.1, 0.1, 0.2, 0.2],
            "theta_2_scale": [0.1, 0.1, 0.2, 0.2],
            "c_loc": [0.3, 0.4, -0.1, -0.2],
            "c_scale": [0.5, 0.5, 0.5, 0.5],
            "tier": ["nationals", "nationals", "fall", "fall"],
        },
        index=pd.Index(["p_nat1", "p_nat2", "p_fall1", "p_fall2"], name="player_id"),
    )


class TestTierPriors(unittest.TestCase):
    def test_tier_means_separate_by_difficulty(self):
        priors = estimate_tier_priors(train_posterior_frame())
        # Nationals players carry higher theta than fall players.
        self.assertGreater(priors["nationals"][0][0], priors["fall"][0][0])
        # A global fallback is always present.
        self.assertIn("__global__", priors)

    def test_returning_player_uses_training_posterior(self):
        posterior = train_posterior_frame()
        priors = estimate_tier_priors(posterior)
        tensors, summary = build_prior_tensors(
            ["p_nat1", "newcomer"],
            posterior,
            priors,
            test_tier_map={"newcomer": "fall"},
            new_player_prior="tier",
        )
        # Returning player: prior loc/scale equal its saved training posterior.
        self.assertTrue(
            torch.allclose(tensors["theta_prior_loc"][0], torch.tensor([2.0, 0.5]))
        )
        self.assertTrue(
            torch.allclose(tensors["theta_prior_scale"][0], torch.tensor([0.1, 0.1]))
        )
        # New player: prior loc equals the fall tier mean.
        fall_mu = torch.tensor(priors["fall"][0], dtype=torch.float32)
        self.assertTrue(torch.allclose(tensors["theta_prior_loc"][1], fall_mu))
        self.assertEqual(summary, {
            "players": 2,
            "returning": 1,
            "new": 1,
            "new_player_prior": "tier",
        })

    def test_flat_new_player_prior_is_standard_normal(self):
        posterior = train_posterior_frame()
        priors = estimate_tier_priors(posterior)
        tensors, _ = build_prior_tensors(
            ["newcomer"],
            posterior,
            priors,
            test_tier_map={"newcomer": "nationals"},
            new_player_prior="flat",
        )
        # Ablation: new players fall back to N(0, I) regardless of tier.
        self.assertTrue(torch.allclose(tensors["theta_prior_loc"][0], torch.zeros(2)))
        self.assertTrue(torch.allclose(tensors["theta_prior_scale"][0], torch.ones(2)))


class TestPlayerTierMap(unittest.TestCase):
    def test_modal_tier_with_hard_tie_break(self):
        tables = {
            "tournaments": pd.DataFrame(
                {
                    "tournament_id": ["t_fall", "t_nats"],
                    "tier": ["fall", "nationals"],
                }
            ),
            "teams": pd.DataFrame(
                {
                    "tournament_id": ["t_fall", "t_nats"],
                    "player_ids": [["a", "b"], ["a"]],
                }
            ),
        }
        tier_map = player_tier_map(tables)
        # "a" appears once at each tier -> tie broken toward the harder tier.
        self.assertEqual(tier_map["a"], "nationals")
        # "b" appears only at fall.
        self.assertEqual(tier_map["b"], "fall")


class TestModelDefaultPriors(unittest.TestCase):
    def test_absent_prior_keys_keep_standard_normal(self):
        # Missing optional keys use the standard N(0, I)/N(0, 1) priors.
        import pyro
        from pyramidal_model import sample_parameters

        data = {"y": torch.zeros(1), "player_ids": ["a"], "tossup_ids": ["x"]}
        pyro.clear_param_store()
        trace = pyro.poutine.trace(sample_parameters).get_trace(data, 2)
        theta_dist = trace.nodes["theta"]["fn"].base_dist
        self.assertTrue(torch.allclose(theta_dist.loc, torch.zeros(1, 2)))
        self.assertTrue(torch.allclose(theta_dist.scale, torch.ones(1, 2)))


if __name__ == "__main__":
    unittest.main()
