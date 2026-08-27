"""Focused tests for portable SVI quantile and joint-draw artifacts."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pyro
import pyro.distributions as dist
import torch

from utils.posterior import save_variational_posterior
from utils.saving import write_summary
from utils.training import fit_svi


class _FakeGuide:
    """Small guide-shaped object with deterministic quantiles and random draws."""

    def quantiles(self, probabilities, **_kwargs):
        probabilities = torch.tensor(probabilities, dtype=torch.float32)
        return {
            "theta": torch.stack([probabilities, probabilities + 1], dim=1),
            "tau": probabilities + 2,
        }

    def __call__(self, **_kwargs):
        shared = torch.rand(())
        return {
            "theta": torch.stack([shared, shared + 1]),
            "tau": shared + 2,
        }


class PosteriorArtifactTests(unittest.TestCase):
    def test_summary_keeps_bias_only_calibration(self):
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            write_summary(
                output_dir,
                {"model": "test"},
                {"correctness_bias": torch.tensor(0.75)},
            )

            summary = json.loads(
                (output_dir / "summary.json").read_text(encoding="utf-8")
            )
            self.assertEqual(summary["correctness_bias"], 0.75)
            self.assertNotIn("correctness_scale", summary)

    def test_saves_shape_preserving_quantiles_and_aligned_draws(self):
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            manifest = save_variational_posterior(
                output_dir,
                _FakeGuide(),
                {},
                draws=4,
                seed=17,
            )

            self.assertEqual(manifest["draws"], 4)
            self.assertEqual(manifest["sites"]["theta"]["shape"], [2])
            quantiles = np.load(output_dir / "posterior_quantiles.npz")
            np.testing.assert_allclose(quantiles["theta__p025"], [0.025, 1.025])
            np.testing.assert_allclose(quantiles["tau__p975"], 2.975)

            theta = np.load(output_dir / "posterior_draws" / "theta.npy")
            tau = np.load(output_dir / "posterior_draws" / "tau.npy")
            self.assertEqual(theta.shape, (4, 2))
            self.assertEqual(tau.shape, (4,))
            # The fake guide derives every site from one shared random value.
            np.testing.assert_allclose(theta[:, 0] + 2, tau)
            np.testing.assert_allclose(theta[:, 0] + 1, theta[:, 1])

            saved_manifest = json.loads(
                (output_dir / "posterior_manifest.json").read_text(encoding="utf-8")
            )
            self.assertEqual(saved_manifest["draw_seed"], 17)

    def test_zero_draws_still_saves_parameter_uncertainty(self):
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            save_variational_posterior(output_dir, _FakeGuide(), {}, draws=0)

            self.assertTrue((output_dir / "posterior_quantiles.csv").exists())
            self.assertTrue((output_dir / "posterior_quantiles.npz").exists())
            self.assertFalse((output_dir / "posterior_draws").exists())

    def test_rejects_negative_draw_count(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "non-negative"):
                save_variational_posterior(
                    directory, _FakeGuide(), {}, draws=-1
                )

    def test_fit_svi_can_persist_a_real_autonormal_guide(self):
        def model(data):
            location = pyro.sample("location", dist.Normal(0.0, 1.0))
            with pyro.plate("rows", len(data)):
                pyro.sample("observed", dist.Normal(location, 1.0), obs=data)

        with tempfile.TemporaryDirectory() as directory:
            posterior, _guide, losses = fit_svi(
                model,
                model_kwargs={"data": torch.tensor([0.8, 1.0, 1.2])},
                n_steps=20,
                lr=0.03,
                posterior_output_dir=directory,
                posterior_draws=3,
                posterior_seed=9,
            )

            self.assertIn("location", posterior)
            self.assertEqual(len(losses), 20)
            draws = np.load(Path(directory) / "posterior_draws" / "location.npy")
            self.assertEqual(draws.shape, (3,))
            manifest = json.loads(
                (Path(directory) / "posterior_manifest.json").read_text(
                    encoding="utf-8"
                )
            )
            self.assertIn("location", manifest["sites"])


if __name__ == "__main__":
    unittest.main()
