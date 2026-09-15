"""Finite-outcome and gradient checks for the normalized first-buzz law."""

import importlib
import inspect
import json
import math

import numpy as np
import pandas as pd
import pyro
import pytest
import torch

from compirt_data import tossup_tensors
from compirt_race import first_buzz_distribution, winner_log_prob


def race_rows(winner=0, token=1, correct=1, players=2, total=3):
    return pd.DataFrame([
        dict(event_id="e", player_id=f"p{i}", tossup_id="q", t_star=token,
             T_j=total, y=correct if i == winner else np.nan,
             z="NO-BUZZ" if winner is None else "BUZZ" if i == winner else "CENSORED")
        for i in range(players)
    ])


def test_two_players_one_cell_is_categorical():
    mass, dead = first_buzz_distribution(np.zeros((2, 1)))
    np.testing.assert_allclose(mass[:, 0], [0.375, 0.375])
    assert dead == 0.25
    data = tossup_tensors(race_rows(total=1))
    assert winner_log_prob(data, torch.zeros(2)).exp().item() == pytest.approx(0.375)


@pytest.mark.parametrize("players,total", [(1, 1), (2, 3), (8, 7)])
def test_enumerated_training_law_equals_replay(players, total):
    rng = np.random.default_rng(42)
    logits = rng.normal(-2, 1, (players, total))
    logits[:, -1] += 4  # Distinct terminal exposure.
    mass, dead = first_buzz_distribution(logits)
    all_probabilities = [dead]
    for token in range(1, total + 1):
        survival = -np.logaddexp(0, logits[:, :token-1]).sum()
        for winner in range(players):
            data = tossup_tensors(race_rows(winner, token, players=players, total=total))
            current = torch.tensor(logits[:, token-1], dtype=torch.float64)
            probability = (survival + winner_log_prob(data, current)).exp().item()
            assert probability == pytest.approx(mass[winner, token-1], rel=1e-12)
            # Summing both Bernoulli correctness marks recovers event mass.
            all_probabilities.extend([probability * 0.3, probability * 0.7])
    assert sum(all_probabilities) == pytest.approx(1, abs=1e-12)


@pytest.mark.parametrize("values", [[-1000., -999.], [1000., 999.],
                                  [-40., -42.], [-2., 1.], [100., -100.]])
def test_extreme_logits_have_finite_values_and_gradients(values):
    data = tossup_tensors(race_rows())
    logits = torch.tensor(values, dtype=torch.float64, requires_grad=True)
    result = winner_log_prob(data, logits)
    result.sum().backward()
    assert torch.isfinite(result).all()
    assert torch.isfinite(logits.grad).all()
    assert torch.autograd.gradcheck(lambda x: winner_log_prob(data, x), (logits,))


def test_saturated_replay_preserves_odds_allocation():
    mass, dead = first_buzz_distribution(np.array([[1000.], [999.]]))
    assert dead == 0
    assert mass[0, 0] == pytest.approx(1 / (1 + math.exp(-1)))


def test_interleaved_rosters_and_bounceback_are_separate_races():
    first = race_rows(players=3).assign(phase=0)
    bounce = race_rows(players=2).assign(phase=1)
    other = race_rows(players=1).assign(event_id="other", phase=0)
    rows = pd.concat([first, bounce, other], ignore_index=True).iloc[[3, 0, 5, 1, 4, 2]]
    data = tossup_tensors(rows)
    probabilities = winner_log_prob(data, torch.zeros(len(rows))).exp()
    torch.testing.assert_close(probabilities, torch.tensor([0.375, 0.875 / 3, 0.5]))


def test_actual_bounceback_factor_is_product_of_separate_races():
    from pyramidal_model import competing_risks_model

    first = race_rows(winner=0, token=1, correct=0, players=3).assign(phase=0, t_start=1)
    bounce = race_rows(winner=1, token=3, players=2).assign(phase=1, t_start=2)
    bounce["player_id"] = ["p1", "p2"]
    bounce["z"] = "BOUNCE-" + bounce["z"]
    data = tossup_tensors(pd.concat([first, bounce], ignore_index=True))
    pyro.clear_param_store()
    pyro.set_rng_seed(42)
    trace = pyro.poutine.trace(competing_risks_model).get_trace(data)
    parameters = {name: trace.nodes[name]["value"] for name in ("theta", "c", "alpha", "beta", "gamma", "mu")}
    model = pyro.poutine.condition(competing_risks_model, data=parameters)

    def score(part):
        trace = pyro.poutine.trace(model).get_trace(part)
        trace.compute_log_prob()
        return trace.nodes["competing_risks_likelihood"]["log_prob"].sum()

    parts = []
    for phase0 in (True, False):
        mask = data["is_phase0"] == phase0
        parts.append({key: value[mask] if isinstance(value, torch.Tensor) else value
                      for key, value in data.items()})
    torch.testing.assert_close(score(data), score(parts[0]) + score(parts[1]))
    pyro.clear_param_store()


def test_summary_versions_new_fits_without_relabeling_legacy_replay(tmp_path):
    from utils.saving import write_summary
    from compirt_race import FIRST_BUZZ_LIKELIHOOD

    write_summary(tmp_path, {"events": 1, "tossups": 1}, {})
    saved = json.loads((tmp_path / "summary.json").read_text())
    assert saved["first_buzz_likelihood"] == FIRST_BUZZ_LIKELIHOOD
    assert saved["terminal_no_buzz_survival"] == "tokens_1_through_T"
    legacy = {"events": 1, "tossups": 1, "frozen_predict": True, "first_buzz_likelihood": "legacy"}
    write_summary(tmp_path, legacy, {})
    assert json.loads((tmp_path / "summary.json").read_text())["first_buzz_likelihood"] == "legacy"


MODEL_MODULES = [
    "pyramidal_model",
    "multidimensional.multidim_mirt.pyramidal_model",
    *[f"hazard_double_difficulty.{family}.pyramidal_model" for family in
      ("bernstein", "multidim",
       "perceived_difficulty_bernstein", "perceived_logit_bernstein")],
]


@pytest.mark.parametrize("module_name", MODEL_MODULES)
def test_actual_model_factor_normalizes_over_all_outcomes(module_name, tmp_path):
    """Enumerate actual Pyro factors with fixed parameters, including no buzz.

    This catches incorrect training wiring and terminal survival without
    mocking the hazard, correctness, survival, or winner functions.
    """
    module = importlib.import_module(module_name)
    model = module.competing_risks_model
    kwargs = {"n_dimensions": 2} if "n_dimensions" in inspect.signature(model).parameters else {}
    pyro.clear_param_store()
    pyro.set_rng_seed(19)

    def data_for(winner, token, correct):
        data = tossup_tensors(race_rows(winner, token, correct, total=2))
        data["y"] = data["y"].double()
        return data

    try:
        initial = pyro.poutine.trace(model).get_trace(data_for(0, 1, 1), **kwargs)
        parameters = {name: node["value"] for name, node in initial.nodes.items()
                      if node["type"] == "sample" and not node.get("is_observed")
                      and not isinstance(node["fn"], pyro.poutine.subsample_messenger._Subsample)}
        fixed_model = pyro.poutine.condition(model, data=parameters)
        if module_name == "hazard_double_difficulty.bernstein.pyramidal_model":
            from hazard_double_difficulty.bernstein.train_pyramidal import save_double_difficulty_parameters
            from compirt_eval.scenario_a_tossups.reconstruction import event_first_buzz_components

            save_double_difficulty_parameters(tmp_path, data_for(0, 1, 1), parameters)
            players = pd.read_csv(tmp_path / "players.csv").set_index("player_id")
            tossups = pd.read_csv(tmp_path / "tossups.csv").set_index("tossup_id")
            replay = event_first_buzz_components(
                race_rows(total=2), players, tossups,
                terminal_intercepts=(float(parameters["end_correct"]), float(parameters["end_hazard"])))
        probabilities = []
        for winner, token, correct in [(None, 2, 0)] + [
            (p, t, y) for p in range(2) for t in (1, 2) for y in (0, 1)
        ]:
            trace = pyro.poutine.trace(fixed_model).get_trace(
                data_for(winner, token, correct), **kwargs)
            trace.compute_log_prob()
            factors = [node["log_prob"].sum() for node in trace.nodes.values()
                       if node["type"] == "sample" and isinstance(node["fn"], pyro.distributions.Unit)]
            assert len(factors) == 1
            probabilities.append(factors[0].exp().item())
            if module_name == "hazard_double_difficulty.bernstein.pyramidal_model":
                expected = replay["dead_mass"]
                if winner is not None:
                    p = replay["correctness_probability"][winner, token-1]
                    expected = replay["player_first_buzz_mass"][winner, token-1] * (p if correct else 1-p)
                assert probabilities[-1] == pytest.approx(expected, abs=1e-12)
        assert sum(probabilities) == pytest.approx(1, abs=2e-10)
    finally:
        pyro.clear_param_store()
