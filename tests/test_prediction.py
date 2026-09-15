"""Check event grouping against analytically known first-buzz distributions."""

import importlib

import pytest
import torch

from utils.prediction import event_rosters


MODEL_MODULES = [
    "pyramidal_model",
    "multidimensional.multidim_mirt.pyramidal_model",
    *[
        f"hazard_double_difficulty.{family}.pyramidal_model"
        for family in (
            "bernstein", "multidim",
            "perceived_difficulty_bernstein", "perceived_logit_bernstein",
        )
    ],
]


def prediction_data():
    # Interleaved events have unequal rosters and question lengths. The final
    # row repeats a player for a bounceback and must not enter the first race.
    return {
        "event_ids": ["short", "long"],
        "event": torch.tensor([1, 0, 1, 1]),
        "player": torch.tensor([2, 0, 1, 2]),
        "tossup": torch.tensor([1, 0, 1, 1]),
        "T_j": torch.tensor([3, 2, 3, 3]),
        "is_phase0": torch.tensor([True, True, True, False]),
        "y": torch.zeros(4),
    }


@pytest.mark.parametrize("module_name", MODEL_MODULES)
def test_first_buzz_expectation_respects_rosters_and_question_lengths(module_name):
    model = importlib.import_module(module_name)
    scalar = module_name == "pyramidal_model"
    posterior = {
        "theta": torch.zeros(3, 2), "c": torch.zeros(3),
        "alpha": torch.ones(2, 2), "r": torch.full((2, 2), 0.5),
        "beta": torch.zeros(2) if scalar else torch.zeros(2, 2),
        "gamma": torch.ones(2) if scalar else torch.ones(2, 2),
        "mu": torch.full((2,), 0.5) if scalar else torch.full((2, 2), 0.5),
    }
    # Zero difficulty and skill give each player hazard 1/2 at every token.
    posterior["gamma"] = torch.zeros_like(posterior["gamma"])
    for suffix in ("", "_correct", "_hazard"):
        posterior[f"r{suffix}"] = torch.full((2, 2), 0.5)
        posterior[f"start_difficulty{suffix}"] = torch.zeros(2, 2)
        posterior[f"total_drop{suffix}"] = torch.zeros(2, 2)
        posterior[f"drop_proportions{suffix}"] = torch.full((2, 2, 3), 1 / 3)
        posterior[f"beta{suffix}"] = posterior["beta"].clone()
        posterior[f"gamma{suffix}"] = posterior["gamma"].clone()
        posterior[f"mu{suffix}"] = posterior["mu"].clone()
    if "perceived_" in module_name:
        shape = (3,) if "perceived_logit" in module_name else (3, 2)
        posterior["alpha"] = torch.ones(shape)
        posterior["beta"] = torch.zeros(shape)

    result = model.expected_first_buzz_positions(prediction_data(), posterior)
    # One player over two tokens: masses (1/2, 1/4); two players over three
    # tokens: masses (3/4, 3/16, 3/64). Normalize each mean by buzz mass and T.
    assert result == pytest.approx({"short": 2 / 3, "long": 3 / 7})


def test_legacy_observations_keep_player_order_without_phase_flags():
    data = prediction_data()
    for name in ("event", "player", "tossup", "T_j"):
        data[name] = data[name][:3]
    del data["is_phase0"]
    roster, mask, tossups, tokens = event_rosters(data)
    assert roster.tolist() == [[0, 0], [2, 1]]
    assert mask.tolist() == [[True, False], [True, True]]
    assert tossups.tolist() == [0, 1]
    assert tokens.tolist() == [2, 3]
