"""Contracts for shared-difficulty perceived Bernstein."""

from __future__ import annotations

import numpy as np
import pandas as pd
import pyro
import torch

from compirt_eval.scenario_a_tossups import evaluate_tossups
from compirt_eval.imaginary_tournament.evaluation import (
    simulate_imaginary_tournament,
)
from hazard_double_difficulty.perceived_difficulty_bernstein import (
    pyramidal_model as model,
)
from hazard_double_difficulty.perceived_difficulty_bernstein.train_pyramidal import (
    parse_args,
    run_experiment,
    save_perceived_parameters,
)
from hazard_double_difficulty.tests.test_hazard_double_difficulty import (
    synthetic_tables,
    tiny_data,
)
from hazard_double_difficulty.tests.perception_contracts import (
    assert_frozen_replay_matches,
    perception_tournament_inputs,
)
from holdout.frozen_predict import (
    PERCEIVED_DIFFICULTY_BERNSTEIN,
    PERCEIVED_DIFFICULTY_SLICED_BERNSTEIN,
)
from run_scripts.bernstein.run_perceived_difficulty_bernstein_332 import (
    Configuration,
    experiment_commands,
)
from run_scripts.bernstein.run_perceived_difficulty_sliced_bernstein_332 import (
    experiment_commands as sliced_experiment_commands,
)
from run_scripts.bernstein import (
    run_perceived_difficulty_sliced_alternating_bernstein_332 as alternating_runner,
)
from utils.training import fit_svi_alternating


def posterior(data, dimensions=3, degree=3):
    torch.manual_seed(4)
    players = len(data["player_ids"])
    tossups = len(data["tossup_ids"])
    shares = torch.rand(tossups, dimensions, degree)
    return {
        "theta": torch.randn(players, dimensions),
        "alpha": torch.exp(torch.randn(players, dimensions)),
        "beta": torch.randn(players, dimensions),
        "r": torch.softmax(torch.randn(tossups, dimensions), dim=-1),
        "start_difficulty": torch.randn(tossups, dimensions),
        "total_drop": torch.rand(tossups, dimensions) + 0.5,
        "drop_proportions": shares / shares.sum(-1, keepdim=True),
    }


def sliced_posterior(data, dimensions=3, degree=3):
    fit = posterior(data, dimensions, degree)
    players = len(data["player_ids"])
    fit["alpha"] = torch.exp(torch.randn(players, 3, dimensions))
    fit["beta"] = torch.randn(players, 3, dimensions)
    return fit


def runner_configuration(root):
    """Return the holdout-runner configuration the three 3-3-2 runners share."""
    return Configuration(
        root=root, base_split="year_2024", folds=list(range(5)), split_seed=42,
        optimization_seed=42, degree=3, dimensions=3,
        relevance_concentration=2.0, drop_concentration=2.0, steps=3000,
        lr=0.005, device="cuda", posterior_draws=0, data_dir=None,
    )


def alternating_test_fit(steps):
    pyro.set_rng_seed(33)
    posterior, _guide, _losses = fit_svi_alternating(
        model.competing_risks_model,
        model_kwargs={
            "data": tiny_data(),
            "n_dimensions": 3,
            "degree": 3,
            "perception_slices": 3,
        },
        n_steps=steps,
        lr=0.02,
        frozen_site_cycle=(("alpha", "beta"), ("theta",)),
    )
    return posterior


def test_alternating_svi_trains_every_item_site_on_both_step_types():
    initial = alternating_test_fit(0)
    after_theta_step = alternating_test_fit(1)
    after_perception_step = alternating_test_fit(2)

    assert not torch.equal(after_theta_step["theta"], initial["theta"])
    torch.testing.assert_close(after_theta_step["alpha"], initial["alpha"])
    torch.testing.assert_close(after_theta_step["beta"], initial["beta"])
    torch.testing.assert_close(
        after_perception_step["theta"], after_theta_step["theta"]
    )
    assert not torch.equal(
        after_perception_step["alpha"], after_theta_step["alpha"]
    )
    assert not torch.equal(
        after_perception_step["beta"], after_theta_step["beta"]
    )

    always_trainable = (
        "r",
        "start_difficulty",
        "total_drop",
        "drop_proportions",
    )
    for site in always_trainable:
        assert not torch.equal(after_theta_step[site], initial[site])
        assert not torch.equal(
            after_perception_step[site], after_theta_step[site]
        )


def test_relative_third_boundaries_include_exact_cutoffs_in_later_slice():
    positions = torch.tensor([0.9, 1.0, 1.1, 1.9, 2.0, 2.1])
    total = torch.full_like(positions, 3.0)
    assert model.perception_slice_index(positions, total).tolist() == [
        0, 1, 1, 1, 2, 2
    ]
    integer_positions = torch.arange(1, 11, dtype=torch.float32)
    integer_total = torch.full_like(integer_positions, 10.0)
    assert model.perception_slice_index(integer_positions, integer_total).tolist() == [
        0, 0, 0, 1, 1, 1, 2, 2, 2, 2
    ]


def test_sliced_hazard_selects_alpha_and_beta_without_changing_correctness():
    theta = torch.tensor([[0.4]])
    relevance = torch.ones(1, 1)
    start = torch.tensor([[0.9]])
    total_drop = torch.tensor([[0.6]])
    shares = torch.full((1, 1, 3), 1 / 3)
    positions = torch.tensor([2.0, 4.0, 8.0])
    total_tokens = torch.full_like(positions, 9.0)
    alpha = torch.tensor([[[0.5], [1.0], [2.0]]])
    beta = torch.tensor([[[0.1], [0.2], [0.3]]])
    difficulty = model.difficulty_curve(
        start, total_drop, shares, positions, total_tokens
    )
    expected = theta - alpha[0, :, :] * difficulty + beta[0, :, :]
    torch.testing.assert_close(
        model.hazard_logit(
            theta,
            relevance,
            start,
            total_drop,
            shares,
            alpha,
            beta,
            positions,
            total_tokens,
        ),
        expected.squeeze(-1),
    )
    torch.testing.assert_close(
        model.correctness_logit(
            theta,
            relevance,
            start,
            total_drop,
            shares,
            positions,
            total_tokens,
        ),
        (theta - difficulty).squeeze(-1),
    )


def test_logits_match_literal_equations():
    theta = torch.tensor([[0.4, -0.2, 0.8]], dtype=torch.float64)
    r = torch.tensor([[0.2, 0.3, 0.5]], dtype=torch.float64)
    start = torch.tensor([[1.0, 0.2, -0.4]], dtype=torch.float64)
    total = torch.tensor([[0.7, 0.6, 0.5]], dtype=torch.float64)
    shares = torch.tensor(
        [[[0.2, 0.3, 0.5], [0.4, 0.2, 0.4], [0.1, 0.6, 0.3]]],
        dtype=torch.float64,
    )
    alpha = torch.tensor([[1.2, 0.5, 0.7]], dtype=torch.float64)
    beta = torch.tensor([[0.1, -0.3, 0.2]], dtype=torch.float64)
    t, T = torch.tensor([4.0]), torch.tensor([10.0])
    difficulty = model.difficulty_curve(start, total, shares, t, T)
    torch.testing.assert_close(
        model.correctness_logit(theta, r, start, total, shares, t, T),
        (r * (theta - difficulty)).sum(-1),
    )
    torch.testing.assert_close(
        model.hazard_logit(theta, r, start, total, shares, alpha, beta, t, T),
        (r * (theta - alpha * difficulty + beta)).sum(-1),
    )


def test_identity_perception_recovers_correctness_and_positive_alpha_preserves_slope():
    theta = torch.zeros(1, 2)
    r = torch.tensor([[0.4, 0.6]])
    start = torch.ones(1, 2)
    total = torch.ones(1, 2)
    shares = torch.full((1, 2, 3), 1 / 3)
    T = torch.tensor([10.0])
    early, late = torch.tensor([1.0]), torch.tensor([9.0])
    for t in (early, late):
        torch.testing.assert_close(
            model.hazard_logit(
                theta, r, start, total, shares, torch.ones_like(theta),
                torch.zeros_like(theta), t, T
            ),
            model.correctness_logit(theta, r, start, total, shares, t, T),
        )
    positive = torch.full_like(theta, 0.5)
    early_hazard = model.hazard_logit(
        theta, r, start, total, shares, positive, torch.zeros_like(theta), early, T
    )
    late_hazard = model.hazard_logit(
        theta, r, start, total, shares, positive, torch.zeros_like(theta), late, T
    )
    assert late_hazard > early_hazard


def test_trace_uses_one_simplex_relevance_and_one_curve():
    pyro.clear_param_store()
    trace = pyro.poutine.trace(model.competing_risks_model).get_trace(
        tiny_data(), n_dimensions=3, degree=3, relevance_concentration=2.0
    )
    r = trace.nodes["r"]["value"]
    assert isinstance(trace.nodes["r"]["fn"], torch.distributions.Dirichlet)
    torch.testing.assert_close(r.sum(-1), torch.ones(r.shape[0]))
    assert "c" not in trace.nodes
    assert "end_correct" not in trace.nodes
    assert "end_hazard" not in trace.nodes
    assert tuple(trace.nodes["alpha"]["value"].shape) == (3, 3)
    assert tuple(trace.nodes["beta"]["value"].shape) == (3, 3)
    alpha_prior = trace.nodes["alpha"]["fn"]
    assert isinstance(alpha_prior, torch.distributions.Independent)
    assert isinstance(alpha_prior.base_dist, torch.distributions.LogNormal)
    beta_prior = trace.nodes["beta"]["fn"]
    assert isinstance(beta_prior, torch.distributions.Independent)
    assert isinstance(beta_prior.base_dist, torch.distributions.Normal)
    assert torch.all(trace.nodes["alpha"]["value"] > 0)


def test_three_slice_trace_has_independent_positive_player_vectors():
    pyro.clear_param_store()
    trace = pyro.poutine.trace(model.competing_risks_model).get_trace(
        tiny_data(), n_dimensions=3, degree=3, perception_slices=3
    )
    assert tuple(trace.nodes["alpha"]["value"].shape) == (3, 3, 3)
    assert tuple(trace.nodes["beta"]["value"].shape) == (3, 3, 3)
    alpha_prior = trace.nodes["alpha"]["fn"]
    beta_prior = trace.nodes["beta"]["fn"]
    assert isinstance(alpha_prior, torch.distributions.Independent)
    assert isinstance(alpha_prior.base_dist, torch.distributions.LogNormal)
    assert alpha_prior.reinterpreted_batch_ndims == 2
    assert isinstance(beta_prior, torch.distributions.Independent)
    assert isinstance(beta_prior.base_dist, torch.distributions.Normal)
    assert beta_prior.reinterpreted_batch_ndims == 2
    assert torch.all(trace.nodes["alpha"]["value"] > 0)


def test_no_buzz_survival_includes_final_token():
    data = tiny_data()
    fit = posterior(data)
    _correct, _hazard, survival = model.posterior_row_predictions(data, fit)
    row = int(torch.nonzero(data["is_no_buzz"], as_tuple=False)[0])
    theta, alpha, beta, r, start, total, shares = model.row_parameters(
        data, fit["theta"], fit["alpha"], fit["beta"], fit["r"],
        fit["start_difficulty"], fit["total_drop"], fit["drop_proportions"]
    )
    expected = torch.exp(
        model.log_survival(
            theta[row : row + 1], r[row : row + 1], start[row : row + 1],
            total[row : row + 1], shares[row : row + 1], alpha[row : row + 1],
            beta[row : row + 1], data["t_star"][row : row + 1] + 1,
            data["T_j"][row : row + 1]
        )
    )
    torch.testing.assert_close(survival[row : row + 1], expected)


def test_saved_schema_frozen_replay_and_numpy_evaluator_match(tmp_path):
    data = tiny_data()
    assert_frozen_replay_matches(
        tmp_path,
        data,
        posterior(data),
        model=model,
        save_parameters=save_perceived_parameters,
        schema=PERCEIVED_DIFFICULTY_BERNSTEIN,
    )


def test_sliced_schema_frozen_replay_and_numpy_evaluator_match(tmp_path):
    data = tiny_data()
    fit = sliced_posterior(data)
    players, _tossups, rebuilt = assert_frozen_replay_matches(
        tmp_path,
        data,
        fit,
        model=model,
        save_parameters=save_perceived_parameters,
        schema=PERCEIVED_DIFFICULTY_SLICED_BERNSTEIN,
    )
    expected_columns = {
        f"{parameter}_{slice_name}_{dimension}"
        for parameter in ("alpha", "beta")
        for slice_name in model.PERCEPTION_SLICE_NAMES
        for dimension in range(1, 4)
    }
    assert expected_columns.issubset(players.columns)
    assert not {"alpha_1", "beta_1"}.intersection(players.columns)
    torch.testing.assert_close(rebuilt["alpha"], fit["alpha"], rtol=1e-5, atol=1e-6)
    torch.testing.assert_close(rebuilt["beta"], fit["beta"], rtol=1e-5, atol=1e-6)


def test_trainer_smoke_and_runner_contract(tmp_path):
    output = tmp_path / "pyramidal"
    args = parse_args(
        [
            "--dimensions", "3", "--degree", "3", "--steps", "1",
            "--posterior-draws", "0", "--device", "cpu",
            "--output-dir", str(output),
        ]
    )
    summary = run_experiment(args, tables=synthetic_tables())
    assert summary["parameter_schema"] == PERCEIVED_DIFFICULTY_BERNSTEIN
    assert summary["alpha_prior"] == "LogNormal(0, 1.0)"
    assert summary["alpha_constraint"] == "positive"
    assert summary["beta_prior"] == "Normal(0, 1)"
    players = pd.read_csv(output / "players.csv")
    assert {"theta_3", "alpha_3", "beta_3"}.issubset(players.columns)
    assert (players[["alpha_1", "alpha_2", "alpha_3"]] > 0).all().all()
    tossups = pd.read_csv(output / "tossups.csv")
    np.testing.assert_allclose(tossups[["r_1", "r_2", "r_3"]].sum(axis=1), 1)
    metrics = evaluate_tossups(output, tmp_path / "evaluation")
    assert metrics["first_buzzer_events"] == 1
    assert metrics["full_pmf_max_mass_error"] < 1e-6

    config = runner_configuration("/tmp/perceived-332")
    _run_dir, stages = experiment_commands(config, 2)
    train, frozen, evaluate = (stage[2] for stage in stages)
    assert (
        "hazard_double_difficulty.perceived_difficulty_bernstein.train_pyramidal"
        in train
    )
    assert train[train.index("--relevance-concentration") + 1] == "2.0"
    assert "game-holdout:year_2024:train:5:2:42" in train
    assert "holdout.frozen_predict" in frozen
    assert "game-holdout:year_2024:test:5:2:42" in frozen
    assert "run_scripts.paper_model_selection.evaluate_fold" in evaluate


def test_sliced_trainer_smoke_evaluator_and_runner_contract(tmp_path):
    output = tmp_path / "pyramidal"
    args = parse_args(
        [
            "--dimensions", "3", "--degree", "3",
            "--perception-slices", "3", "--steps", "1",
            "--posterior-draws", "0", "--device", "cpu",
            "--output-dir", str(output),
        ]
    )
    summary = run_experiment(args, tables=synthetic_tables())
    assert (
        summary["parameter_schema"]
        == PERCEIVED_DIFFICULTY_SLICED_BERNSTEIN
    )
    assert summary["perception_slices"] == 3
    assert summary["perception_slice_names"] == ["first", "middle", "last"]
    assert summary["perception_slice_boundaries"] == [1 / 3, 2 / 3]
    item_parameters = 3 * 3 + 2 * 3 - 1
    assert summary["effective_parameter_count"] == (
        summary["players"] * 7 * 3
        + summary["tossups"] * item_parameters
    )
    players = pd.read_csv(output / "players.csv")
    alpha_columns = [
        f"alpha_{slice_name}_{dimension}"
        for slice_name in model.PERCEPTION_SLICE_NAMES
        for dimension in range(1, 4)
    ]
    assert set(alpha_columns).issubset(players.columns)
    assert (players[alpha_columns] > 0).all().all()
    metrics = evaluate_tossups(output, tmp_path / "evaluation")
    assert metrics["first_buzzer_events"] == 1
    assert metrics["full_pmf_max_mass_error"] < 1e-6

    config = runner_configuration("/tmp/perceived-sliced-332")
    _run_dir, stages = sliced_experiment_commands(config, 2)
    train, frozen, evaluate = (stage[2] for stage in stages)
    assert train[train.index("--perception-slices") + 1] == "3"
    assert "game-holdout:year_2024:train:5:2:42" in train
    assert "holdout.frozen_predict" in frozen
    assert "run_scripts.paper_model_selection.evaluate_fold" in evaluate


def test_sliced_alternating_trainer_and_runner_contract(tmp_path):
    output = tmp_path / "pyramidal"
    args = parse_args(
        [
            "--dimensions", "3", "--degree", "3",
            "--perception-slices", "3", "--steps", "2",
            "--alternate-player-steps", "--posterior-draws", "0",
            "--device", "cpu", "--output-dir", str(output),
        ]
    )
    summary = run_experiment(args, tables=synthetic_tables())
    assert summary["optimization_schedule"] == (
        "alternating-theta-perception"
    )
    assert summary["other_parameter_schedule"] == "trainable_every_step"
    assert summary["always_trainable_sites"] == [
        "r",
        "start_difficulty",
        "total_drop",
        "drop_proportions",
    ]
    assert summary["alternating_step_cycle"][0]["train_player_sites"] == [
        "theta"
    ]
    assert summary["alternating_step_cycle"][1]["train_player_sites"] == [
        "alpha", "beta"
    ]

    config = runner_configuration("/tmp/perceived-sliced-alternating-332")
    _run_dir, stages = alternating_runner.experiment_commands(config, 2)
    train = stages[0][2]
    assert train[train.index("--perception-slices") + 1] == "3"
    assert "--alternate-player-steps" in train


def test_sliced_perception_runs_in_imaginary_tournament():
    inputs = perception_tournament_inputs(
        question_lengths=6,
        perception_alpha=np.stack(
            [np.full((8, 1), 0.5), np.full((8, 1), 1.0), np.full((8, 1), 2.0)],
            axis=1,
        ),
        perception_beta=np.zeros((8, 3, 1)),
    )
    players, games, summary = simulate_imaginary_tournament(
        inputs, games=2, players_per_team=2, tossups_per_game=2, seed=9
    )
    assert not players.empty
    assert len(games) == 2
    assert summary["games"] == 2
