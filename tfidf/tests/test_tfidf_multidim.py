"""Tests for the multidimensional cumulative TF-IDF pyramidal model."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import torch

try:
    import pyro
    from pyro.infer import SVI, Trace_ELBO
    from pyro.infer.autoguide import AutoNormal
    from pyro.optim import ClippedAdam

    from tfidf.multidim.pyramidal_model import (
        competing_risks_model,
        correctness_logit,
        hazard_logit,
    )
    from tfidf.multidim.train_pyramidal import save_tfidf_adjustment_curves
    from tfidf.plot_tfidf_difficulty_curves import curve_components
    from tfidf.pyramidal_tfidf_model import (
        CUMULATIVE_DIFFICULTY,
    )
except ModuleNotFoundError as error:
    if error.name != "pyro":
        raise
    pyro = None


@unittest.skipIf(pyro is None, "pyro is not installed in this environment")
class MultidimTfidfFormulaTests(unittest.TestCase):
    def setUp(self):
        self.theta = torch.zeros((1, 2))
        self.r = torch.tensor([[0.5, 1.5]])
        self.beta = torch.tensor([[2.0, 2.0]])
        self.gamma = torch.tensor([[10.0, 10.0]])
        self.mu = torch.tensor([[0.5, 0.5]])
        self.t = torch.tensor([1.0])
        self.T = torch.tensor([4.0])

    def test_cumulative_difficulty_applies_before_r_weighting(self):
        beta = torch.zeros((1, 2))
        effect = torch.tensor(2.0)

        early = correctness_logit(
            self.theta,
            self.r,
            beta,
            self.gamma,
            self.mu,
            self.t,
            self.T,
            torch.tensor([0.25]),
            effect,
            CUMULATIVE_DIFFICULTY,
        )
        late = correctness_logit(
            self.theta,
            self.r,
            beta,
            self.gamma,
            self.mu,
            self.t,
            self.T,
            torch.tensor([0.75]),
            effect,
            CUMULATIVE_DIFFICULTY,
        )
        hazard = hazard_logit(
            self.theta,
            self.r,
            beta,
            self.gamma,
            self.mu,
            torch.tensor([0.25]),
            self.t,
            self.T,
            torch.tensor([0.75]),
            effect,
            CUMULATIVE_DIFFICULTY,
        )

        self.assertAlmostEqual(float(early), 1.0)
        self.assertAlmostEqual(float(late), 3.0)
        self.assertAlmostEqual(float(hazard), 2.75)

    def test_svi_posterior_has_positive_r_and_vector_difficulty(self):
        data = {
            "player": torch.tensor([0]),
            "tossup": torch.tensor([0]),
            "event": torch.tensor([0]),
            "t_star": torch.tensor([1]),
            "T_j": torch.tensor([1]),
            "y": torch.tensor([1.0]),
            "is_buzz": torch.tensor([True]),
            "tfidf_prefix": torch.tensor([[1.0]]),
            "player_ids": ["p1"],
            "tossup_ids": ["q1"],
            "event_ids": ["e1"],
        }
        pyro.clear_param_store()
        guide = AutoNormal(competing_risks_model)
        svi = SVI(
            competing_risks_model,
            guide,
            ClippedAdam({"lr": 0.01}),
            loss=Trace_ELBO(),
        )

        svi.step(data, 2, False, 1.0, CUMULATIVE_DIFFICULTY)
        posterior = guide.median(data, 2, False, 1.0, CUMULATIVE_DIFFICULTY)

        self.assertEqual(tuple(posterior["r"].shape), (1, 2))
        self.assertTrue(torch.all(posterior["r"] > 0))
        self.assertEqual(tuple(posterior["beta"].shape), (1, 2))
        self.assertEqual(tuple(posterior["gamma"].shape), (1, 2))
        self.assertEqual(tuple(posterior["mu"].shape), (1, 2))


@unittest.skipIf(pyro is None, "pyro is not installed in this environment")
class MultidimTfidfOutputTests(unittest.TestCase):
    def test_adjustment_curves_save_r_weighted_aggregate_delta(self):
        data = {
            "tossup_ids": ["q1"],
            "tfidf_prefix": torch.tensor([[0.0, 0.5, 1.0]]),
        }
        observations = pd.DataFrame({"tossup_id": ["q1"], "T_j": [3]})
        posterior = {
            "r": torch.tensor([[0.5, 1.5]]),
            "tfidf_clue_effect": torch.tensor(2.0),
        }

        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            save_tfidf_adjustment_curves(
                output_dir,
                data,
                observations,
                posterior,
                CUMULATIVE_DIFFICULTY,
                n_points=3,
            )
            frame = pd.read_csv(output_dir / "tfidf_adjustment_curves.csv")

        values = frame.filter(like="adjustment_").iloc[0].to_numpy(dtype=float)
        self.assertTrue(np.allclose(values, np.array([0.0, -2.0, -4.0])))

    def test_plot_curve_components_accept_multidim_saved_parameters(self):
        row = pd.Series(
            {
                "r_1": 0.5,
                "r_2": 1.5,
                "beta_1": 0.0,
                "beta_2": 0.0,
                "gamma_1": 1.0,
                "gamma_2": 1.0,
                "mu_1": 0.5,
                "mu_2": 0.5,
            }
        )
        features = {
            "T": 3,
            "prefix": torch.tensor([0.0, 0.5, 1.0]),
        }
        summary = {
            "tfidf_variant": CUMULATIVE_DIFFICULTY,
            "tfidf_clue_effect": 1.0,
        }
        curves = curve_components(row, features, summary, np.array([0.0, 0.5, 1.0]))

        self.assertTrue(np.allclose(curves["base"], np.array([0.0, 0.0, 0.0])))
        self.assertTrue(
            np.allclose(curves["effective"], np.array([0.0, -1.0, -2.0]))
        )


if __name__ == "__main__":
    unittest.main()
