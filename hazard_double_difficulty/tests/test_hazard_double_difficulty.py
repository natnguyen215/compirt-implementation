"""Synthetic regression tests for the double-difficulty CompIRT variants.

The load-bearing test in each class is the parent-equivalence one: setting the
correctness and hazard curves to the same values must reproduce the parent
family's logits and survival exactly. That is what makes "the same equation,
just learned twice" a checkable claim rather than a comment.
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pandas as pd
import pyro
import torch

from compirt_data import build_tossup_observations, tossup_tensors
from compirt_eval.scenario_a_tossups.difficulty import (
    difficulty_plot,
    multidim_difficulty_components_plot,
)
from compirt_eval.scenario_a_tossups.distributions import (
    pyramidal_parameter_distribution_plots,
)
from compirt_eval.scenario_a_tossups.parameters import (
    _buzz_parameter_prefix,
    _saved_difficulty_curve,
)
from compirt_eval.scenario_a_tossups.timing import event_first_buzz_components

from multidimensional.multidim_mirt import pyramidal_model as parent_multidim
from polynomial_compirt import pyramidal_model as parent_bernstein

from hazard_double_difficulty.multidim import pyramidal_model as double_multidim
from hazard_double_difficulty.bernstein import pyramidal_model as double_bernstein
from hazard_double_difficulty.multidim.train_pyramidal import (
    parse_args as parse_multidim_args,
    run_experiment as run_multidim_experiment,
)
from hazard_double_difficulty.bernstein.train_pyramidal import (
    parse_args as parse_bernstein_args,
    run_experiment as run_bernstein_experiment,
)
from holdout.frozen_predict import (
    frozen_predict_tossups,
    parse_args as parse_frozen_args,
)


DIMENSIONS = 3
DEGREE = 4
ROWS = 6


def synthetic_tables():
    """Return linked tables with one observed buzz and one dead tossup."""
    return {
        "tournaments": pd.DataFrame(
            [{"tournament_id": "t1", "question_set_event_id": "qs1", "tier": "test"}]
        ),
        "teams": pd.DataFrame(
            [
                {"team_id": "team-a", "tournament_id": "t1", "player_ids": ["p1", "p2"]},
                {"team_id": "team-b", "tournament_id": "t1", "player_ids": ["p3"]},
            ]
        ),
        "games": pd.DataFrame(
            [
                {
                    "game_id": "g1",
                    "tournament_id": "t1",
                    "packet_id": 10,
                    "team_ids": ["team-a", "team-b"],
                    "tossups_read": 2,
                }
            ]
        ),
        "tossups": pd.DataFrame(
            [
                {
                    "tossup_id": "q1",
                    "question_set_event_id": "qs1",
                    "packet": 10,
                    "question_num": 1,
                    "tokens": ["one", "two", "three", "four"],
                },
                {
                    "tossup_id": "q2",
                    "question_set_event_id": "qs1",
                    "packet": 10,
                    "question_num": 2,
                    "tokens": ["one", "two", "three"],
                },
            ]
        ),
        "tossup_buzzes": pd.DataFrame(
            [
                {
                    "buzz_id": "g1::buzz-1",
                    "game_id": "g1",
                    "tossup_id": "q1",
                    "player_id": "p1",
                    "token_position": 2,
                    "num_tokens_total": 4,
                    "correct": True,
                }
            ]
        ),
        "bonuses": pd.DataFrame(
            [
                {
                    "bonus_id": "b1",
                    "question_set_event_id": "qs1",
                    "question_num": 1,
                    "category": "history",
                }
            ]
        ),
        "bonus_responses": pd.DataFrame(
            [
                {
                    "response_id": "r1",
                    "game_id": "g1",
                    "team_id": "team-a",
                    "bonus_id": "b1",
                    "parts_correct": [True, False, True],
                    "total_points": 20,
                }
            ]
        ),
    }


def tiny_data():
    """Build tensors used by the direct model tests."""
    return tossup_tensors(build_tossup_observations(synthetic_tables()))


def shared_row_inputs():
    """Return the '(theta, r, c, t, T_j)' row inputs shared by both families."""
    torch.manual_seed(0)
    return (
        torch.randn(ROWS, DIMENSIONS, dtype=torch.float64),
        torch.rand(ROWS, DIMENSIONS, dtype=torch.float64) + 0.1,
        torch.randn(ROWS, dtype=torch.float64),
        torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=torch.float64),
        torch.full((ROWS,), 9.0, dtype=torch.float64),
    )


def multidim_curve(seed):
    """Return one '(beta, gamma, mu)' curve for the multidim family."""
    generator = torch.Generator().manual_seed(seed)
    return (
        torch.randn(ROWS, DIMENSIONS, generator=generator, dtype=torch.float64),
        torch.rand(ROWS, DIMENSIONS, generator=generator, dtype=torch.float64) + 0.5,
        torch.rand(ROWS, DIMENSIONS, generator=generator, dtype=torch.float64),
    )


def bernstein_curve(seed):
    """Return one '(start, total_drop, shares)' curve for the Bernstein family."""
    generator = torch.Generator().manual_seed(seed)
    shares = torch.rand(ROWS, DIMENSIONS, DEGREE, generator=generator, dtype=torch.float64)
    return (
        torch.randn(ROWS, DIMENSIONS, generator=generator, dtype=torch.float64),
        torch.rand(ROWS, DIMENSIONS, generator=generator, dtype=torch.float64) + 0.2,
        shares / shares.sum(-1, keepdim=True),
    )


class MultidimEquivalenceTests(unittest.TestCase):
    """The multidim variant must collapse onto its parent when curves coincide."""

    def test_matches_parent_when_both_curves_are_equal(self):
        theta, r, c, t, T = shared_row_inputs()
        curve = multidim_curve(1)
        t_star = torch.tensor([2, 3, 4, 5, 6, 7])
        for link in ("sigmoid", "tanh"):
            with self.subTest(link=link):
                torch.testing.assert_close(
                    double_multidim.correctness_logit(theta, r, *curve, t, T, link),
                    parent_multidim.correctness_logit(theta, r, *curve, t, T, link),
                )
                torch.testing.assert_close(
                    double_multidim.hazard_logit(theta, r, *curve, c, t, T, link),
                    parent_multidim.hazard_logit(theta, r, *curve, c, t, T, link),
                )
                torch.testing.assert_close(
                    double_multidim.log_survival(
                        theta, r, *curve, c, t_star, T, link
                    ),
                    parent_multidim.log_survival(
                        theta, r, *curve, c, t_star, T, link
                    ),
                )

    def test_curves_are_independent(self):
        theta, r, c, t, T = shared_row_inputs()
        correct, hazard = multidim_curve(1), multidim_curve(2)
        baseline_correctness = double_multidim.correctness_logit(
            theta, r, *correct, t, T
        )
        baseline_hazard = double_multidim.hazard_logit(theta, r, *hazard, c, t, T)
        # Perturbing one curve must leave the other branch bit-identical.
        moved_hazard = multidim_curve(3)
        torch.testing.assert_close(
            double_multidim.correctness_logit(theta, r, *correct, t, T),
            baseline_correctness,
            rtol=0,
            atol=0,
        )
        self.assertFalse(
            torch.allclose(
                double_multidim.hazard_logit(theta, r, *moved_hazard, c, t, T),
                baseline_hazard,
            )
        )

    def test_grid_shapes_collapse_the_dimension_axis(self):
        theta, r, c, t, T = shared_row_inputs()
        curve = multidim_curve(1)
        self.assertEqual(
            tuple(double_multidim.correctness_logit(theta, r, *curve, t, T).shape),
            (ROWS,),
        )
        # The (n_rows, 1, K) grid path used inside log_survival.
        positions = torch.arange(1, 8, dtype=torch.float64).unsqueeze(0)
        grid = double_multidim.hazard_logit(
            theta.unsqueeze(1),
            r.unsqueeze(1),
            *(parameter.unsqueeze(1) for parameter in curve),
            c.unsqueeze(1),
            positions,
            T.unsqueeze(1),
        )
        self.assertEqual(tuple(grid.shape), (ROWS, 7))

    def test_survival_ignores_an_all_ones_t_start(self):
        theta, r, c, _, T = shared_row_inputs()
        curve = multidim_curve(1)
        t_star = torch.tensor([2, 3, 4, 5, 6, 7])
        torch.testing.assert_close(
            double_multidim.log_survival(theta, r, *curve, c, t_star, T),
            double_multidim.log_survival(
                theta, r, *curve, c, t_star, T, t_start=torch.ones_like(t_star)
            ),
            rtol=0,
            atol=0,
        )

    def test_model_trace_carries_both_curve_families(self):
        data = tiny_data()
        pyro.clear_param_store()
        trace = pyro.poutine.trace(double_multidim.competing_risks_model).get_trace(
            data, DIMENSIONS
        )
        n_tossups = len(data["tossup_ids"])
        for name in ("beta", "gamma", "mu"):
            for suffix in ("correct", "hazard"):
                site = trace.nodes[f"{name}_{suffix}"]["value"]
                self.assertEqual(tuple(site.shape), (n_tossups, DIMENSIONS))
        for name in ("r_correct", "r_hazard"):
            self.assertEqual(
                tuple(trace.nodes[name]["value"].shape), (n_tossups, DIMENSIONS)
            )

    def test_simplex_terminal_sigmoid_trace_has_requested_sites(self):
        data = tiny_data()
        pyro.clear_param_store()
        trace = pyro.poutine.trace(double_multidim.competing_risks_model).get_trace(
            data,
            DIMENSIONS,
            link="sigmoid",
            relevance_prior="simplex",
            terminal_intercepts=True,
        )
        for name in ("r_correct", "r_hazard"):
            distribution = trace.nodes[name]["fn"]
            self.assertIsInstance(distribution, torch.distributions.Dirichlet)
            value = trace.nodes[name]["value"]
            torch.testing.assert_close(value.sum(-1), torch.ones_like(value.sum(-1)))
        for name in ("end_correct", "end_hazard"):
            self.assertIn(name, trace.nodes)
            self.assertEqual(tuple(trace.nodes[name]["value"].shape), ())

    def test_terminal_intercept_changes_only_final_cell(self):
        theta, r, c, _, T = shared_row_inputs()
        curve = multidim_curve(1)
        t = T.clone()
        effect = torch.tensor(1.75, dtype=torch.float64)
        base = double_multidim.hazard_logit(theta, r, *curve, c, t, T)
        changed = double_multidim.hazard_logit(
            theta, r, *curve, c, t, T, end=effect
        )
        torch.testing.assert_close(changed - base, effect.expand_as(base))
        before = double_multidim.hazard_logit(
            theta, r, *curve, c, t - 1, T, end=effect
        )
        before_base = double_multidim.hazard_logit(theta, r, *curve, c, t - 1, T)
        torch.testing.assert_close(before, before_base)


class BernsteinEquivalenceTests(unittest.TestCase):
    """The Bernstein variant must collapse onto its parent when curves coincide."""

    def test_incorrect_weight_only_scales_incorrect_correctness_terms(self):
        logits = torch.tensor([1.5, -0.75], dtype=torch.float64)
        targets = torch.tensor([1.0, 0.0], dtype=torch.float64)
        terms = torch.distributions.Bernoulli(logits=logits).log_prob(targets)
        actual = double_bernstein.correctness_log_likelihood(
            logits, targets, incorrect_weight=3.0
        )
        torch.testing.assert_close(actual, terms[0] + 3.0 * terms[1])

    def test_matches_parent_when_both_curves_are_equal(self):
        theta, r, c, t, T = shared_row_inputs()
        curve = bernstein_curve(1)
        t_star = torch.tensor([2, 3, 4, 5, 6, 7])
        torch.testing.assert_close(
            double_bernstein.correctness_logit(theta, r, *curve, t, T),
            parent_bernstein.correctness_logit(theta, r, *curve, t, T),
        )
        torch.testing.assert_close(
            double_bernstein.hazard_logit(theta, r, *curve, c, t, T),
            parent_bernstein.hazard_logit(theta, r, *curve, c, t, T),
        )
        torch.testing.assert_close(
            double_bernstein.log_survival(theta, r, *curve, c, t_star, T),
            parent_bernstein.log_survival(theta, r, *curve, c, t_star, T),
        )

    def test_curves_are_independent(self):
        theta, r, c, t, T = shared_row_inputs()
        correct, hazard = bernstein_curve(1), bernstein_curve(2)
        baseline_correctness = double_bernstein.correctness_logit(
            theta, r, *correct, t, T
        )
        baseline_hazard = double_bernstein.hazard_logit(theta, r, *hazard, c, t, T)
        moved_hazard = bernstein_curve(3)
        torch.testing.assert_close(
            double_bernstein.correctness_logit(theta, r, *correct, t, T),
            baseline_correctness,
            rtol=0,
            atol=0,
        )
        self.assertFalse(
            torch.allclose(
                double_bernstein.hazard_logit(theta, r, *moved_hazard, c, t, T),
                baseline_hazard,
            )
        )

    def test_both_curves_stay_strictly_decreasing(self):
        x = torch.linspace(0, 1, 201, dtype=torch.float64)
        ones = torch.ones_like(x)
        for seed in (1, 2):
            start, total, shares = bernstein_curve(seed)
            curve = double_bernstein.difficulty_curve(
                start[0].unsqueeze(0),
                total[0].unsqueeze(0),
                shares[0].unsqueeze(0),
                x.unsqueeze(1),
                ones.unsqueeze(1),
            )
            self.assertTrue((curve[1:] < curve[:-1]).all())

    def test_model_trace_carries_both_curve_families(self):
        data = tiny_data()
        pyro.clear_param_store()
        trace = pyro.poutine.trace(double_bernstein.competing_risks_model).get_trace(
            data, DIMENSIONS, DEGREE, 2.0
        )
        n_tossups = len(data["tossup_ids"])
        for suffix in ("correct", "hazard"):
            relevance_distribution = trace.nodes[f"r_{suffix}"]["fn"]
            self.assertIsInstance(
                relevance_distribution.base_dist, torch.distributions.Gamma
            )
            self.assertEqual(
                tuple(trace.nodes[f"r_{suffix}"]["value"].shape),
                (n_tossups, DIMENSIONS),
            )
            self.assertEqual(
                tuple(trace.nodes[f"start_difficulty_{suffix}"]["value"].shape),
                (n_tossups, DIMENSIONS),
            )
            total_drop = trace.nodes[f"total_drop_{suffix}"]["value"]
            self.assertEqual(tuple(total_drop.shape), (n_tossups, DIMENSIONS))
            self.assertTrue((total_drop > 0).all())
            self.assertEqual(
                tuple(trace.nodes[f"drop_proportions_{suffix}"]["value"].shape),
                (n_tossups, DIMENSIONS, DEGREE),
            )

    def test_simplex_prior_applies_independently_to_both_relevance_vectors(self):
        data = tiny_data()
        pyro.clear_param_store()
        trace = pyro.poutine.trace(double_bernstein.competing_risks_model).get_trace(
            data,
            DIMENSIONS,
            DEGREE,
            2.0,
            relevance_prior="simplex",
        )
        values = []
        for name in ("r_correct", "r_hazard"):
            distribution = trace.nodes[name]["fn"]
            self.assertIsInstance(distribution, torch.distributions.Dirichlet)
            torch.testing.assert_close(
                distribution.concentration,
                torch.ones_like(distribution.concentration),
            )
            value = trace.nodes[name]["value"]
            torch.testing.assert_close(value.sum(-1), torch.ones_like(value.sum(-1)))
            values.append(value)
        self.assertFalse(torch.equal(*values))

    def test_learned_locations_add_two_global_curve_start_mus(self):
        data = tiny_data()
        pyro.clear_param_store()
        base = pyro.poutine.trace(double_bernstein.competing_risks_model).get_trace(
            data,
            DIMENSIONS,
            DEGREE,
            2.0,
            relevance_prior="simplex",
            terminal_intercepts=True,
        )
        learned = pyro.poutine.trace(
            double_bernstein.competing_risks_model
        ).get_trace(
            data,
            DIMENSIONS,
            DEGREE,
            2.0,
            relevance_prior="simplex",
            terminal_intercepts=True,
            learned_curve_locations=True,
        )
        self.assertEqual(
            set(learned.nodes) - set(base.nodes),
            {"curve_location_correct", "curve_location_hazard"},
        )
        conditioned = pyro.poutine.condition(
            double_bernstein.competing_risks_model,
            data={
                "curve_location_correct": torch.tensor(1.25),
                "curve_location_hazard": torch.tensor(-0.75),
            },
        )
        centered = pyro.poutine.trace(conditioned).get_trace(
            data,
            DIMENSIONS,
            DEGREE,
            2.0,
            learned_curve_locations=True,
        )
        for suffix, expected in (("correct", 1.25), ("hazard", -0.75)):
            start_prior = centered.nodes[f"start_difficulty_{suffix}"]["fn"]
            torch.testing.assert_close(
                start_prior.base_dist.loc,
                torch.full_like(start_prior.base_dist.loc, expected),
            )

    def test_player_neg_propensity_adds_hierarchical_scale_and_player_effects(self):
        data = tiny_data()
        pyro.clear_param_store()
        base = pyro.poutine.trace(double_bernstein.competing_risks_model).get_trace(
            data, DIMENSIONS
        )
        hierarchical = pyro.poutine.trace(
            double_bernstein.competing_risks_model
        ).get_trace(data, DIMENSIONS, player_neg_propensity=True)
        self.assertEqual(set(hierarchical.nodes) - set(base.nodes), {"a", "a_scale"})
        self.assertEqual(
            tuple(hierarchical.nodes["a"]["value"].shape),
            (len(data["player_ids"]),),
        )
        self.assertGreater(float(hierarchical.nodes["a_scale"]["value"]), 0.0)


class TrainerSmokeTests(unittest.TestCase):
    """Each trainer runs end to end on synthetic tables and saves both curves."""

    def test_multidim_trainer_saves_both_curve_column_families(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "pyramidal"
            args = parse_multidim_args(
                [
                    "--dimensions", "2",
                    "--difficulty-link", "sigmoid",
                    "--relevance-prior", "simplex",
                    "--terminal-intercepts",
                    "--steps", "1",
                    "--posterior-draws", "0",
                    "--device", "cpu",
                    "--output-dir", str(output),
                ]
            )
            summary = run_multidim_experiment(args, tables=synthetic_tables())
            self.assertEqual(
                summary["difficulty_coupling"], "separate_correctness_hazard"
            )
            self.assertEqual(summary["difficulty_link"], "sigmoid")
            self.assertEqual(summary["relevance_prior_family"], "simplex")
            self.assertTrue(summary["terminal_intercepts"])
            self.assertEqual(summary["effective_item_parameters"], 14)
            self.assertEqual(summary["global_parameters"], 2)
            self.assertIn("end_correct", summary)
            self.assertIn("end_hazard", summary)
            tossups = pd.read_csv(output / "tossups.csv")
            self.assertIn("r_1", tossups)
            self.assertIn("hazard_r_1", tossups)
            for column in ("beta_1", "gamma_1", "mu_1"):
                self.assertIn(column, tossups)
                self.assertIn(f"hazard_{column}", tossups)
            for name in (
                "players.csv",
                "summary.json",
                "tossup_predictions.csv",
                "buzz_event_predictions.csv",
            ):
                self.assertTrue((output / name).exists(), name)

            # Frozen replay must recover the two global terminal effects from
            # summary.json in addition to the per-player/tossup CSV parameters.
            heldout = Path(directory) / "heldout"
            frozen_args = parse_frozen_args(
                [
                    "tossup",
                    "--split", "all",
                    "--train-pyramidal", str(output),
                    "--dimensions", "2",
                    "--difficulty-link", "sigmoid",
                    "--device", "cpu",
                    "--output-dir", str(heldout),
                ]
            )
            with patch(
                "holdout.frozen_predict.load_hf_tables",
                return_value=synthetic_tables(),
            ):
                frozen_predict_tossups(frozen_args)
            native = pd.read_csv(output / "tossup_predictions.csv")
            replay = pd.read_csv(heldout / "tossup_predictions.csv")
            for column in (
                "predicted_correct",
                "predicted_hazard",
                "predicted_survival",
            ):
                np.testing.assert_allclose(native[column], replay[column], rtol=1e-5)

            evaluation = Path(directory) / "evaluation"
            difficulty_plot(output, evaluation)
            multidim_difficulty_components_plot(output, evaluation)
            pyramidal_parameter_distribution_plots(output, evaluation)
            for relative_path in (
                "graphs/tossup/tossup_difficulty_curves.png",
                "graphs/tossup/tossup_hazard_difficulty_curves.png",
                "graphs/tossup/tossup_difficulty_curves_by_dimension.png",
                "graphs/tossup/tossup_hazard_difficulty_curves_by_dimension.png",
                "graphs/tossup/pyramidal_difficulty_curve_distribution.png",
                "graphs/tossup/pyramidal_hazard_difficulty_curve_distribution.png",
                "graphs/parameters/pyramidal_hazard_parameter_distributions.png",
                "csvs/pyramidal_difficulty_curve_distribution.csv",
                "csvs/pyramidal_hazard_difficulty_curve_distribution.csv",
                "csvs/pyramidal_parameter_distribution_summary.csv",
            ):
                artifact = evaluation / relative_path
                self.assertTrue(artifact.exists(), relative_path)
                self.assertGreater(artifact.stat().st_size, 0, relative_path)
            parameter_summary = pd.read_csv(
                evaluation
                / "csvs"
                / "pyramidal_parameter_distribution_summary.csv"
            )
            self.assertIn("tossup_hazard", set(parameter_summary["group"]))
            self.assertIn("hazard_r_1", set(parameter_summary["parameter"]))

    def test_bernstein_trainer_saves_both_curve_column_families(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "pyramidal"
            args = parse_bernstein_args(
                [
                    "--degree", "3",
                    "--dimensions", "2",
                    "--relevance-prior", "simplex",
                    "--learn-curve-locations",
                    "--player-neg-propensity",
                    "--incorrect-weight", "3",
                    "--steps", "1",
                    "--posterior-draws", "0",
                    "--device", "cpu",
                    "--output-dir", str(output),
                ]
            )
            summary = run_bernstein_experiment(args, tables=synthetic_tables())
            self.assertEqual(
                summary["difficulty_coupling"], "separate_correctness_hazard"
            )
            self.assertEqual(summary["relevance_prior_family"], "simplex")
            self.assertEqual(summary["relevance_prior"], "Dirichlet(ones(2))")
            self.assertTrue(summary["learned_curve_locations"])
            self.assertEqual(summary["incorrect_weight"], 3.0)
            self.assertTrue(summary["player_neg_propensity"])
            self.assertEqual(summary["global_parameters"], 5)
            self.assertIn("curve_location_correct", summary)
            self.assertIn("curve_location_hazard", summary)
            self.assertIn("a_scale", summary)
            self.assertEqual(summary["effective_item_parameters"], 18)
            players = pd.read_csv(output / "players.csv")
            self.assertIn("a", players)
            tossups = pd.read_csv(output / "tossups.csv")
            self.assertIn("r_1", tossups)
            self.assertIn("hazard_r_1", tossups)
            for column in (
                "start_difficulty_d1",
                "end_difficulty_d1",
                "total_drop_d1",
                "drop_share_1_d1",
            ):
                self.assertIn(column, tossups)
                self.assertIn(f"hazard_{column}", tossups)
            # end = start - total_drop must hold for both saved curves.
            for prefix in ("", "hazard_"):
                np.testing.assert_allclose(
                    tossups[f"{prefix}end_difficulty_d1"],
                    tossups[f"{prefix}start_difficulty_d1"]
                    - tossups[f"{prefix}total_drop_d1"],
                )
            for name in (
                "players.csv",
                "summary.json",
                "tossup_predictions.csv",
                "buzz_event_predictions.csv",
            ):
                self.assertTrue((output / name).exists(), name)

            # Frozen replay must carry the fitted player propensity alongside
            # theta/c; otherwise correctness predictions would silently differ.
            heldout = Path(directory) / "heldout"
            frozen_args = parse_frozen_args(
                [
                    "tossup",
                    "--split", "all",
                    "--train-pyramidal", str(output),
                    "--dimensions", "2",
                    "--device", "cpu",
                    "--output-dir", str(heldout),
                ]
            )
            with patch(
                "holdout.frozen_predict.load_hf_tables",
                return_value=synthetic_tables(),
            ):
                frozen_predict_tossups(frozen_args)
            native = pd.read_csv(output / "tossup_predictions.csv")
            replay = pd.read_csv(heldout / "tossup_predictions.csv")
            for column in (
                "predicted_correct",
                "predicted_hazard",
                "predicted_survival",
            ):
                np.testing.assert_allclose(native[column], replay[column], rtol=1e-5)


class EvaluatorRoutingTests(unittest.TestCase):
    """Saved DD curves must be replayed according to their modeled role."""

    def test_buzz_replay_uses_hazard_but_correctness_uses_canonical_curve(self):
        players = pd.DataFrame(
            {"theta_1": [0.0], "c": [0.0]},
            index=pd.Index(["p1"], name="player_id"),
        )
        tossups = pd.DataFrame(
            {
                "r_1": [1.0],
                "beta_1": [0.0],
                "gamma_1": [1.0],
                "mu_1": [0.5],
                "hazard_beta_1": [8.0],
                "hazard_gamma_1": [20.0],
                "hazard_mu_1": [0.75],
            },
            index=pd.Index(["q1"], name="tossup_id"),
        )
        event = pd.DataFrame(
            {
                "event_id": ["e1"],
                "tossup_id": ["q1"],
                "player_id": ["p1"],
                "team_id": ["a"],
                "T_j": [2],
                "z": ["DEAD"],
            }
        )

        self.assertEqual(_buzz_parameter_prefix(tossups), "hazard_")
        routed = event_first_buzz_components(event, players, tossups)
        canonical_timing = event_first_buzz_components(
            event,
            players,
            tossups,
            buzz_parameter_prefix="",
        )
        self.assertLess(
            routed["first_buzz_mass"][0],
            canonical_timing["first_buzz_mass"][0],
        )
        np.testing.assert_allclose(routed["correctness_probability"], 0.5)

    def test_curve_reader_selects_each_multidim_family_explicitly(self):
        tossup = pd.Series(
            {
                "r_1": 1.0,
                "beta_1": -3.0,
                "gamma_1": 5.0,
                "mu_1": 0.5,
                "hazard_beta_1": 4.0,
                "hazard_gamma_1": 5.0,
                "hazard_mu_1": 0.5,
            }
        )
        positions = np.asarray([0.0, 0.5, 1.0])
        correctness = _saved_difficulty_curve(tossup, positions)
        hazard = _saved_difficulty_curve(
            tossup,
            positions,
            parameter_prefix="hazard_",
        )
        self.assertTrue((correctness < 0).all())
        self.assertTrue((hazard > 0).all())
        self.assertFalse(np.allclose(correctness, hazard))


if __name__ == "__main__":
    unittest.main()
