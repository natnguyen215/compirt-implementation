"""Equation, nesting, saving, and replay contracts for compact Bernstein."""

from __future__ import annotations

import pandas as pd
import pyro
import torch

from hazard_double_difficulty.compact_bernstein import pyramidal_model as compact
from hazard_double_difficulty.compact_bernstein.train_pyramidal import (
    save_compact_parameters,
)
from hazard_double_difficulty.tests.test_hazard_double_difficulty import tiny_data
from holdout.frozen_predict import (
    COMPACT_BERNSTEIN,
    _load_tossup_posterior,
    detect_tossup_parameter_schema,
)


def _posterior(data, degree=3):
    torch.manual_seed(7)
    players = len(data["player_ids"])
    tossups = len(data["tossup_ids"])
    dimensions = 2
    weights = torch.softmax(torch.randn(tossups, dimensions), dim=-1)
    posterior = {
        "theta": torch.randn(players, dimensions),
        "c": torch.randn(players),
        "skill_weights": weights,
        "discrimination": torch.rand(tossups) + 0.5,
    }
    for suffix, offset in (("correct", 0.0), ("hazard", 0.2)):
        posterior[f"start_difficulty_{suffix}"] = torch.randn(tossups) + offset
        posterior[f"total_drop_{suffix}"] = torch.rand(tossups) + 0.5
        posterior[f"drop_proportions_{suffix}"] = torch.softmax(
            torch.randn(tossups, degree), dim=-1
        )
    return posterior


def test_compact_equation_uses_scalar_curve_outside_skill_projection():
    theta = torch.tensor([[1.0, -0.5]])
    weights = torch.tensor([[0.25, 0.75]])
    discrimination = torch.tensor([2.0])
    start = torch.tensor([1.2])
    total = torch.tensor([0.6])
    shares = torch.tensor([[0.2, 0.3, 0.5]])
    t, T = torch.tensor([4.0]), torch.tensor([10.0])
    expected = (
        discrimination * (weights * theta).sum(-1)
        - compact.difficulty_curve(start, total, shares, t, T)
    )
    actual = compact.correctness_logit(
        theta, weights, discrimination, start, total, shares, t, T
    )
    torch.testing.assert_close(actual, expected)


def test_compact_curve_is_monotone_and_weight_decomposition_is_unique():
    positions = torch.linspace(0, 10, 101)
    curve = compact.difficulty_curve(
        torch.tensor(1.0),
        torch.tensor(2.0),
        torch.tensor([0.2, 0.3, 0.5]),
        positions,
        torch.tensor(10.0),
    )
    assert torch.all(torch.diff(curve) <= 1e-7)
    alpha = torch.tensor([[6.0, 3.0, 1.0]])
    discrimination = alpha.sum(-1)
    weights = alpha / discrimination.unsqueeze(-1)
    torch.testing.assert_close(discrimination, torch.tensor([10.0]))
    torch.testing.assert_close(weights, torch.tensor([[0.6, 0.3, 0.1]]))
    torch.testing.assert_close(discrimination.unsqueeze(-1) * weights, alpha)


def test_selected_model_adds_exactly_four_global_sites():
    data = tiny_data()
    base = pyro.poutine.trace(compact.competing_risks_model).get_trace(
        data, n_dimensions=2, degree=3
    )
    selected = pyro.poutine.trace(compact.competing_risks_model).get_trace(
        data,
        n_dimensions=2,
        degree=3,
        learned_curve_locations=True,
        terminal_intercepts=True,
    )
    additions = set(selected.nodes) - set(base.nodes)
    assert additions == {
        "curve_location_correct",
        "curve_location_hazard",
        "end_correct",
        "end_hazard",
    }


def test_terminal_intercept_changes_only_final_cell():
    common = (
        torch.tensor([[0.2, -0.1], [0.2, -0.1]]),
        torch.tensor([[0.4, 0.6], [0.4, 0.6]]),
        torch.ones(2),
        torch.ones(2),
        torch.ones(2),
        torch.tensor([[0.2, 0.3, 0.5], [0.2, 0.3, 0.5]]),
        torch.zeros(2),
        torch.tensor([9.0, 10.0]),
        torch.tensor([10.0, 10.0]),
    )
    base = compact.hazard_logit(*common)
    changed = compact.hazard_logit(*common, torch.tensor(1.5))
    torch.testing.assert_close(changed[0], base[0])
    torch.testing.assert_close(changed[1], base[1] + 1.5)


def test_saved_compact_schema_reconstructs_native_predictions(tmp_path):
    data = tiny_data()
    posterior = _posterior(data)
    save_compact_parameters(tmp_path, data, posterior)
    players = pd.read_csv(tmp_path / "players.csv")
    tossups = pd.read_csv(tmp_path / "tossups.csv")
    assert detect_tossup_parameter_schema(tossups) == COMPACT_BERNSTEIN
    rebuilt = _load_tossup_posterior(
        players, tossups, data, dimensions=2, device="cpu", schema=COMPACT_BERNSTEIN
    )
    native = compact.posterior_row_predictions(data, posterior)
    replay = compact.posterior_row_predictions(data, rebuilt)
    for expected, actual in zip(native, replay):
        torch.testing.assert_close(actual, expected, rtol=1e-6, atol=1e-6)

