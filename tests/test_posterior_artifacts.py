"""Focused tests for portable SVI quantile and joint-draw artifacts."""

from __future__ import annotations

import json
import numpy as np
import pyro
import pyro.distributions as dist
import pytest
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


@pytest.mark.parametrize("options, message", [
    ({"probabilities": (0.025, 0.025)}, "distinct.*labels"),
    ({"probabilities": (0.0251, 0.0252)}, "distinct.*labels"),
    ({"draws": -1}, "non-negative"),
])
def test_invalid_posterior_artifact_settings(tmp_path, options, message):
    with pytest.raises(ValueError, match=message):
        save_variational_posterior(tmp_path, _FakeGuide(), {}, **options)


def test_summary_keeps_bias_calibration(tmp_path):
    write_summary(tmp_path, {"model": "test"}, {"correctness_bias": torch.tensor(0.75)})
    assert json.loads((tmp_path / "summary.json").read_text())["correctness_bias"] == 0.75


@pytest.mark.parametrize("draws", [0, 4])
def test_saves_shape_preserving_quantiles_and_aligned_draws(tmp_path, draws):
    manifest = save_variational_posterior(tmp_path, _FakeGuide(), {}, draws=draws, seed=17)
    assert manifest["draws"] == draws
    assert manifest["sites"]["theta"]["shape"] == [2]
    quantiles = np.load(tmp_path / "posterior_quantiles.npz")
    np.testing.assert_allclose(quantiles["theta__p025"], [0.025, 1.025])
    np.testing.assert_allclose(quantiles["tau__p975"], 2.975)
    if draws:
        theta = np.load(tmp_path / "posterior_draws/theta.npy")
        tau = np.load(tmp_path / "posterior_draws/tau.npy")
        assert theta.shape == (draws, 2)
        assert tau.shape == (draws,)
        # Each site uses the same random draw, preserving joint uncertainty.
        np.testing.assert_allclose(theta[:, 0] + 2, tau)
        np.testing.assert_allclose(theta[:, 0] + 1, theta[:, 1])
    saved = json.loads((tmp_path / "posterior_manifest.json").read_text())
    assert saved["draw_seed"] == 17


def test_fit_svi_persists_an_autonormal_guide(tmp_path):
    def model(data):
        location = pyro.sample("location", dist.Normal(0.0, 1.0))
        with pyro.plate("rows", len(data)):
            pyro.sample("observed", dist.Normal(location, 1.0), obs=data)

    posterior, _, losses = fit_svi(
        model, model_kwargs={"data": torch.tensor([0.8, 1.0, 1.2])},
        n_steps=20, lr=0.03, posterior_output_dir=tmp_path,
        posterior_draws=3, posterior_seed=9,
    )
    assert "location" in posterior
    assert len(losses) == 20
    assert np.load(tmp_path / "posterior_draws/location.npy").shape == (3,)
    manifest = json.loads((tmp_path / "posterior_manifest.json").read_text())
    assert "location" in manifest["sites"]
