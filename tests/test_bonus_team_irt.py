"""Contracts for direct team IRT and matched whole-game bonus evaluation."""

import numpy as np
import pandas as pd
import pyro
import pytest
import torch

from analysis.bonus_team_irt.model import (
    matched_games, observations, predict, team_irt, training_tensors,
)
from analysis.bonus_team_irt.report import score
from utils.training import fit_svi


def fixture():
    tables = {
        "games": pd.DataFrame([{"game_id": game, "tournament_id": "t", "team_ids": ["a", "b"]}
                               for game in ("g1", "g2")]),
        "tournaments": pd.DataFrame([{"tournament_id": "t", "tier": "open"}]),
        "bonuses": pd.DataFrame([{"bonus_id": "q", "category": "Science", "subcategory": "Physics"}]),
        "bonus_responses": pd.DataFrame([
            {"response_id": "r1", "game_id": "g1", "team_id": "a", "bonus_id": "q", "parts_correct": [1, 1, 1], "total_points": 30},
            {"response_id": "r2", "game_id": "g1", "team_id": "b", "bonus_id": "q", "parts_correct": [1, 0, 0], "total_points": 10},
            {"response_id": "r3", "game_id": "g2", "team_id": "a", "bonus_id": "q", "parts_correct": [0, 0, 0], "total_points": 0},
        ]),
    }
    parts = observations(tables)
    parts["predicted_correct"] = parts.response_id.map({"r1": 0.8, "r2": 0.2, "r3": 0.4})
    return tables, parts


@pytest.mark.parametrize("dimensions, parameters", [
    (1, {"theta": torch.tensor([[0.3], [0.7]]),
         "alpha": torch.tensor([[1.0], [0.2], [0.8]]),
         "beta": torch.tensor([-1.0, 0.0, 1.0])}),
    (2, {"theta": torch.tensor([[0.3, -0.2], [0.7, 0.1]]),
         "r": torch.tensor([[0.6, 0.4], [0.1, 0.9], [0.5, 0.5]]),
         "beta": torch.tensor([[-1.0, 0.5], [0.0, 0.3], [1.0, -0.4]])}),
])
def test_likelihood_matches_frozen_replay_and_labels_do_not_change_predictions(dimensions, parameters):
    _, parts = fixture()
    data = training_tensors(parts, "cpu")
    trace = pyro.poutine.trace(pyro.poutine.condition(team_irt, data=parameters)).get_trace(data, dimensions)
    values = {key: value.numpy().copy() for key, value in parameters.items()}
    expected = predict(parts, values, data["team_ids"], data["part_ids"])
    np.testing.assert_allclose(expected, trace.nodes["correct"]["fn"].probs.numpy(), rtol=1e-6)
    changed = parts.assign(correct=1 - parts.correct)
    np.testing.assert_array_equal(expected, predict(changed, values, data["team_ids"], data["part_ids"]))
    with pytest.raises(ValueError, match="coverage"):
        predict(parts.assign(team_id="unseen"), values, data["team_ids"], data["part_ids"])


def test_relevance_logit_uses_only_r_weighted_difficulty():
    _, parts = fixture()
    data = training_tensors(parts, "cpu")
    theta = np.array([[0.3, -0.2], [0.7, 0.1]])
    r = np.array([[0.6, 0.4], [0.1, 0.9], [0.5, 0.5]])
    beta = np.array([[-1.0, 0.5], [0.0, 0.3], [1.0, -0.4]])
    expected = 1 / (1 + np.exp(-(r[data["part"].numpy()] * (theta[data["team"].numpy()] - beta[data["part"].numpy()])).sum(-1)))
    null = np.stack([r[:, 1], -r[:, 0]], axis=1) * 5.0  # r_b dot null_b = 0
    for shifted in (beta, beta + null):
        np.testing.assert_allclose(
            predict(parts, {"theta": theta, "r": r, "beta": shifted}, data["team_ids"], data["part_ids"]),
            expected, rtol=1e-12)


@pytest.mark.parametrize("dimensions", [1, 3])
def test_small_svi_fit_is_finite(dimensions):
    _, parts = fixture()
    pyro.set_rng_seed(42)
    data = training_tensors(parts, "cpu")
    medians, _, losses = fit_svi(team_irt, model_kwargs={"data": data, "dimensions": dimensions}, n_steps=3, lr=0.01)
    assert np.isfinite(losses).all()
    assert medians["theta"].shape == (2, dimensions)
    if dimensions == 1:
        assert torch.all(medians["alpha"] > 0)
    else:
        assert medians["beta"].shape == (3, dimensions)
        assert torch.all(medians["r"] > 0)
        torch.testing.assert_close(medians["r"].sum(-1), torch.ones(3))


def test_matching_drops_entire_game_and_rejects_label_mismatch():
    _, parts = fixture()
    train = parts[parts.team_id == "a"]
    excluded = matched_games(train, parts, {"reference": parts})
    assert excluded.game_id.tolist() == ["g1"]
    missing = matched_games(parts, parts, {"reference": parts.iloc[:-1]})
    assert missing.game_id.tolist() == ["g2"]
    wrong = parts.copy()
    wrong.loc[0, "correct"] = 0
    with pytest.raises(ValueError, match="disagree"):
        matched_games(parts, parts, {"reference": wrong})


def test_pooled_metrics_include_zero_bonus_team():
    tables, parts = fixture()
    metrics, artifacts = score(parts, tables, tables["games"])
    assert metrics["bonus_game_margin_mae"] == pytest.approx(7.0)
    assert metrics["ppb_mae"] == pytest.approx(3.5)
    team_games = artifacts[0]
    assert len(team_games) == 4
    assert team_games[(team_games.game_id == "g2") & (team_games.team_id == "b")].predicted_bonus_points.item() == 0
