"""Contracts for scalar perceived-logit Bernstein 332."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pyro
import torch

from compirt_eval.scenario_a_tossups import evaluate_tossups
from hazard_double_difficulty.perceived_logit_bernstein import (
    pyramidal_model as model,
)
from hazard_double_difficulty.perceived_logit_bernstein.train_pyramidal import (
    parse_args,
    run_experiment,
    save_perceived_logit_parameters,
)
from hazard_double_difficulty.tests.test_hazard_double_difficulty import (
    synthetic_tables,
    tiny_data,
)
from hazard_double_difficulty.tests.perception_contracts import (
    assert_frozen_replay_matches,
)
from holdout.frozen_predict import (
    PERCEIVED_DIFFICULTY_BERNSTEIN,
    PERCEIVED_LOGIT_BERNSTEIN,
    detect_tossup_parameter_schema,
)
from run_scripts.double_difficulty.run_perceived_logit_bernstein_332 import (
    Configuration,
    experiment_commands,
    parse_args as parse_runner_args,
)


def posterior(data, dimensions=3, degree=3):
    torch.manual_seed(14)
    players = len(data["player_ids"])
    tossups = len(data["tossup_ids"])
    shares = torch.rand(tossups, dimensions, degree)
    return {
        "theta": torch.randn(players, dimensions),
        "alpha": torch.exp(torch.randn(players)),
        "beta": torch.randn(players),
        "r": torch.softmax(torch.randn(tossups, dimensions), dim=-1),
        "start_difficulty": torch.randn(tossups, dimensions),
        "total_drop": torch.rand(tossups, dimensions) + 0.5,
        "drop_proportions": shares / shares.sum(-1, keepdim=True),
    }


def test_logits_match_literal_scalar_affine_equation():
    theta = torch.tensor([[0.4, -0.2, 0.8]], dtype=torch.float64)
    relevance = torch.tensor([[0.2, 0.3, 0.5]], dtype=torch.float64)
    start = torch.tensor([[1.0, 0.2, -0.4]], dtype=torch.float64)
    total = torch.tensor([[0.7, 0.6, 0.5]], dtype=torch.float64)
    shares = torch.tensor(
        [[[0.2, 0.3, 0.5], [0.4, 0.2, 0.4], [0.1, 0.6, 0.3]]],
        dtype=torch.float64,
    )
    alpha = torch.tensor([1.2], dtype=torch.float64)
    beta = torch.tensor([0.35], dtype=torch.float64)
    t, total_tokens = torch.tensor([4.0]), torch.tensor([10.0])
    difficulty = model.difficulty_curve(start, total, shares, t, total_tokens)
    expected_correctness = (relevance * (theta - difficulty)).sum(-1)

    torch.testing.assert_close(
        model.correctness_logit(
            theta, relevance, start, total, shares, t, total_tokens
        ),
        expected_correctness,
    )
    torch.testing.assert_close(
        model.hazard_logit(
            theta,
            relevance,
            start,
            total,
            shares,
            alpha,
            beta,
            t,
            total_tokens,
        ),
        alpha * expected_correctness + beta,
    )


def test_identity_transform_makes_hazard_equal_correctness():
    data = tiny_data()
    fit = posterior(data)
    fit["alpha"] = torch.ones_like(fit["alpha"])
    fit["beta"] = torch.zeros_like(fit["beta"])
    correct, hazard, _survival = model.posterior_row_predictions(data, fit)
    torch.testing.assert_close(correct, hazard)


def test_trace_has_scalar_player_parameters_simplex_and_monotone_curve():
    pyro.clear_param_store()
    trace = pyro.poutine.trace(model.competing_risks_model).get_trace(
        tiny_data(),
        n_dimensions=3,
        degree=3,
        relevance_concentration=2.0,
        drop_concentration=2.0,
    )
    relevance = trace.nodes["r"]["value"]
    assert isinstance(trace.nodes["r"]["fn"], torch.distributions.Dirichlet)
    torch.testing.assert_close(relevance.sum(-1), torch.ones(relevance.shape[0]))
    assert torch.all(relevance > 0)
    assert tuple(trace.nodes["alpha"]["value"].shape) == (3,)
    assert tuple(trace.nodes["beta"]["value"].shape) == (3,)
    assert isinstance(trace.nodes["alpha"]["fn"], torch.distributions.LogNormal)
    assert isinstance(trace.nodes["beta"]["fn"], torch.distributions.Normal)
    assert torch.all(trace.nodes["alpha"]["value"] > 0)

    controls = model.control_values(
        trace.nodes["start_difficulty"]["value"],
        trace.nodes["total_drop"]["value"],
        trace.nodes["drop_proportions"]["value"],
    )
    assert torch.all(controls[..., 1:] < controls[..., :-1])


def test_unconstrained_scalar_alpha_prior_reproduces_historical_center():
    pyro.clear_param_store()
    trace = pyro.poutine.trace(model.competing_risks_model).get_trace(
        tiny_data(),
        n_dimensions=3,
        degree=3,
        alpha_prior="normal-one",
    )
    alpha_prior = trace.nodes["alpha"]["fn"]
    assert isinstance(alpha_prior, torch.distributions.Normal)
    torch.testing.assert_close(alpha_prior.loc, torch.ones_like(alpha_prior.loc))
    torch.testing.assert_close(alpha_prior.scale, torch.ones_like(alpha_prior.scale))


def test_survival_includes_terminal_no_buzz_and_respects_bounceback_start():
    data = tiny_data()
    fit = posterior(data)
    theta, alpha, beta, relevance, start, total, shares = model.row_parameters(
        data,
        fit["theta"],
        fit["alpha"],
        fit["beta"],
        fit["r"],
        fit["start_difficulty"],
        fit["total_drop"],
        fit["drop_proportions"],
    )
    no_buzz_row = int(torch.nonzero(data["is_no_buzz"], as_tuple=False)[0])
    predicted = model.posterior_row_predictions(data, fit)[2]
    explicit = torch.exp(
        model.log_survival(
            theta[no_buzz_row : no_buzz_row + 1],
            relevance[no_buzz_row : no_buzz_row + 1],
            start[no_buzz_row : no_buzz_row + 1],
            total[no_buzz_row : no_buzz_row + 1],
            shares[no_buzz_row : no_buzz_row + 1],
            alpha[no_buzz_row : no_buzz_row + 1],
            beta[no_buzz_row : no_buzz_row + 1],
            data["t_star"][no_buzz_row : no_buzz_row + 1] + 1,
            data["T_j"][no_buzz_row : no_buzz_row + 1],
        )
    )
    torch.testing.assert_close(predicted[no_buzz_row : no_buzz_row + 1], explicit)

    row = slice(0, 1)
    stop = torch.tensor([5])
    full = model.log_survival(
        theta[row], relevance[row], start[row], total[row], shares[row],
        alpha[row], beta[row], stop, data["T_j"][row]
    )
    prefix = model.log_survival(
        theta[row], relevance[row], start[row], total[row], shares[row],
        alpha[row], beta[row], torch.tensor([3]), data["T_j"][row]
    )
    bounceback = model.log_survival(
        theta[row], relevance[row], start[row], total[row], shares[row],
        alpha[row], beta[row], stop, data["T_j"][row], t_start=torch.tensor([3])
    )
    torch.testing.assert_close(full, prefix + bounceback)


def test_saved_schema_frozen_replay_and_numpy_evaluator_match(tmp_path):
    data = tiny_data()
    players, _tossups, _rebuilt = assert_frozen_replay_matches(
        tmp_path,
        data,
        posterior(data),
        model=model,
        save_parameters=save_perceived_logit_parameters,
        schema=PERCEIVED_LOGIT_BERNSTEIN,
    )
    assert {"alpha", "beta", "theta_3", "theta_norm"}.issubset(players.columns)


def test_schema_detection_distinguishes_both_perception_models():
    tossups = pd.DataFrame({"start_difficulty_d1": [0.0]})
    scalar = pd.DataFrame({"theta_1": [0.0], "alpha": [1.0], "beta": [0.0]})
    vector = pd.DataFrame(
        {"theta_1": [0.0], "alpha_1": [1.0], "beta_1": [0.0]}
    )
    assert (
        detect_tossup_parameter_schema(tossups, scalar)
        == PERCEIVED_LOGIT_BERNSTEIN
    )
    assert (
        detect_tossup_parameter_schema(tossups, vector)
        == PERCEIVED_DIFFICULTY_BERNSTEIN
    )


def test_trainer_smoke_evaluator_and_runner_contract(tmp_path):
    output = tmp_path / "pyramidal"
    args = parse_args(
        [
            "--dimensions", "3", "--degree", "3", "--steps", "1",
            "--posterior-draws", "0", "--device", "cpu",
            "--output-dir", str(output),
        ]
    )
    summary = run_experiment(args, tables=synthetic_tables())
    assert summary["parameter_schema"] == PERCEIVED_LOGIT_BERNSTEIN
    assert summary["effective_item_parameters"] == 14
    assert summary["terminal_intercepts"] is False
    assert summary["alpha_prior"] == "LogNormal(0, 1.0)"
    assert summary["alpha_constraint"] == "positive"
    assert summary["beta_prior"] == "Normal(0, 1)"
    players = pd.read_csv(output / "players.csv")
    assert {"theta_3", "alpha", "beta"}.issubset(players.columns)
    assert (players["alpha"] > 0).all()
    tossups = pd.read_csv(output / "tossups.csv")
    np.testing.assert_allclose(tossups[["r_1", "r_2", "r_3"]].sum(axis=1), 1)
    metrics = evaluate_tossups(output, tmp_path / "evaluation")
    assert metrics["first_buzzer_events"] == 1
    assert metrics["full_pmf_max_mass_error"] < 1e-6

    defaults = parse_runner_args([])
    assert defaults.base_split == "year_2024"
    assert defaults.folds == list(range(5))
    assert defaults.steps == 3000
    assert defaults.lr == 0.005
    assert defaults.device == "cuda"
    assert "variants/perceived-logit/positive-alpha" in str(defaults.root)

    config = Configuration(
        root="/tmp/perceived-logit-332",
        base_split="year_2024",
        folds=list(range(5)),
        split_seed=42,
        optimization_seed=42,
        degree=3,
        dimensions=3,
        relevance_concentration=2.0,
        drop_concentration=2.0,
        steps=3000,
        lr=0.005,
        device="cuda",
        posterior_draws=0,
        data_dir=None,
    )
    _run_dir, stages = experiment_commands(config, 2)
    train, frozen, evaluate = (stage[2] for stage in stages)
    assert "hazard_double_difficulty.perceived_logit_bernstein.train_pyramidal" in train
    assert "game-holdout:year_2024:train:5:2:42" in train
    assert "holdout.frozen_predict" in frozen
    assert "game-holdout:year_2024:test:5:2:42" in frozen
    assert "run_scripts.double_difficulty.evaluate_fold" in evaluate


def test_unconstrained_scalar_trainer_records_prior(tmp_path):
    output = tmp_path / "pyramidal"
    args = parse_args(
        [
            "--dimensions", "2", "--degree", "3", "--steps", "1",
            "--alpha-prior", "normal-one", "--posterior-draws", "0",
            "--device", "cpu", "--output-dir", str(output),
        ]
    )
    summary = run_experiment(args, tables=synthetic_tables())
    assert summary["alpha_prior"] == "Normal(1, 1)"
    assert summary["alpha_constraint"] == "unconstrained"
