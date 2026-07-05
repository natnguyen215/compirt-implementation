"""Focused regression tests for the streamlined CompIRT pipeline."""

import math
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import pyro
import torch
from pyro.infer import SVI, Trace_ELBO
from pyro.infer.autoguide import AutoNormal
from pyro.optim import ClippedAdam

from compirt_data import (
    bonus_tensors,
    build_bonus_part_observations,
    build_tossup_observations,
    tossup_tensors,
)
from lineup import LineupIndex
from compirt_eval.tossups import multidim_difficulty_components_plot
from compositional_model import lse_aggregation, posterior_predictions, synergy_contribution
from evaluate_compirt import bonus_metrics, density_estimate, first_buzz_distribution
from multidimensional.multidim_mirt.pyramidal_model import (
    competing_risks_model as multidim_competing_risks_model,
    correctness_logit as multidim_correctness_logit,
    difficulty_curve as multidim_difficulty_curve,
    posterior_row_predictions as multidim_posterior_row_predictions,
)
from pyramidal_model import log_survival, posterior_row_predictions
from train_compositional import load_player_skills
from utils.saving import save_synergy_outputs


def synthetic_tables():
    """Return the smallest linked dataset containing a buzz and a dead tossup."""
    return {
        "tournaments": pd.DataFrame(
            [
                {
                    "tournament_id": "t1",
                    "question_set_event_id": "qs1",
                    "tier": "test",
                }
            ]
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
                    "tokens": ["one", "two", "three"],
                },
                {
                    "tossup_id": "q2",
                    "question_set_event_id": "qs1",
                    "packet": 10,
                    "question_num": 2,
                    "tokens": ["one", "two"],
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
                    "num_tokens_total": 3,
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


class DataTests(unittest.TestCase):
    def test_tossup_observations_expand_roster_and_recover_dead_tossup(self):
        tables = synthetic_tables()
        observations = build_tossup_observations(tables, LineupIndex.from_tables(tables))

        first_buzz = observations[observations["tossup_id"] == "q1"]
        dead = observations[observations["tossup_id"] == "q2"]

        self.assertEqual(first_buzz["z"].value_counts().to_dict(), {"CENSORED": 2, "BUZZ": 1})
        self.assertEqual(set(dead["z"]), {"NO-BUZZ"})
        self.assertEqual(len(dead), 3)

    def test_tossup_tensors_preserve_dead_tossup_mask(self):
        tables = synthetic_tables()
        data = tossup_tensors(
            build_tossup_observations(tables, LineupIndex.from_tables(tables))
        )

        self.assertEqual(tuple(data["player"].shape), (6,))
        self.assertEqual(int(data["is_buzz"].sum()), 1)
        self.assertEqual(int(data["is_no_buzz"].sum()), 3)

    def test_bonus_observations_and_padding(self):
        tables = synthetic_tables()
        observations = build_bonus_part_observations(
            tables, LineupIndex.from_tables(tables)
        )
        data = bonus_tensors(observations, ["p1", "p2", "p3"])

        self.assertEqual(observations["correct"].tolist(), [1.0, 0.0, 1.0])
        self.assertEqual(tuple(data["roster"].shape), (3, 2))
        self.assertTrue(data["roster_mask"].all())


class ModelTests(unittest.TestCase):
    def test_dead_tossup_survival_matches_equations_6_and_13(self):
        zero_vector = torch.zeros((1, 1))
        zero = torch.zeros(1)
        t_star = torch.tensor([3])
        T_j = torch.tensor([3])

        survival = log_survival(
            zero_vector, zero_vector, zero, zero, zero, zero, t_star, T_j
        )
        self.assertAlmostEqual(float(survival), 2 * math.log(0.5), places=6)

    def test_bonus_aggregation_and_synergy_ignore_padding(self):
        scores = torch.tensor([[1.0, 2.0, 100.0]])
        mask = torch.tensor([[True, True, False]])
        aggregate = lse_aggregation(scores, mask, torch.tensor(1.0))
        expected = torch.logsumexp(torch.tensor([1.0, 2.0]), dim=0)
        self.assertTrue(torch.allclose(aggregate, expected.unsqueeze(0)))

        psi = torch.tensor([[1.0, 0.0], [2.0, 0.0], [100.0, 100.0]])
        roster = torch.tensor([[0, 1, 2]])
        synergy = synergy_contribution(psi, roster, mask)
        self.assertEqual(float(synergy), 2.0)

    def test_multidim_difficulty_curve_and_alpha_weighted_formula(self):
        theta = torch.tensor([[10.0, 0.0]])
        alpha = torch.tensor([[0.25, 0.75]])
        beta = torch.tensor([[4.0, 8.0]])
        gamma = torch.tensor([[0.0, 0.0]])
        mu = torch.tensor([[0.5, 0.5]])
        t = torch.tensor([1])
        T_j = torch.tensor([2])

        difficulty = multidim_difficulty_curve(beta, gamma, mu, t, T_j)
        logit = multidim_correctness_logit(theta, alpha, beta, gamma, mu, t, T_j)

        self.assertEqual(tuple(difficulty.shape), (1, 2))
        self.assertTrue(torch.allclose(difficulty, torch.tensor([[2.0, 4.0]])))
        # 0.25 * (10 - 2) + 0.75 * (0 - 4)
        self.assertTrue(torch.allclose(logit, torch.tensor([-1.0])))

    def test_multidim_svi_posterior_uses_vector_difficulty_with_alpha(self):
        data = {
            "player": torch.tensor([0]),
            "tossup": torch.tensor([0]),
            "event": torch.tensor([0]),
            "t_star": torch.tensor([1]),
            "T_j": torch.tensor([1]),
            "y": torch.tensor([1.0]),
            "is_buzz": torch.tensor([True]),
            "player_ids": ["p1"],
            "tossup_ids": ["q1"],
            "event_ids": ["e1"],
        }
        pyro.clear_param_store()
        guide = AutoNormal(multidim_competing_risks_model)
        svi = SVI(
            multidim_competing_risks_model,
            guide,
            ClippedAdam({"lr": 0.01}),
            loss=Trace_ELBO(),
        )

        svi.step(data, 2, False)
        posterior = guide.median(data, 2, False)

        self.assertEqual(tuple(posterior["alpha"].shape), (1, 2))
        self.assertTrue(torch.all(posterior["alpha"] > 0))
        self.assertEqual(tuple(posterior["beta"].shape), (1, 2))
        self.assertEqual(tuple(posterior["gamma"].shape), (1, 2))
        self.assertEqual(tuple(posterior["mu"].shape), (1, 2))

    def test_multidim_calibration_replays_only_correctness(self):
        data = {
            "player": torch.tensor([0]),
            "tossup": torch.tensor([0]),
            "t_star": torch.tensor([1]),
            "T_j": torch.tensor([2]),
        }
        posterior = {
            "theta": torch.tensor([[0.0, 0.0]]),
            "c": torch.tensor([0.0]),
            "alpha": torch.tensor([[1.0, 1.0]]),
            "beta": torch.tensor([[0.0, 0.0]]),
            "gamma": torch.tensor([[1.0, 1.0]]),
            "mu": torch.tensor([[0.5, 0.5]]),
            "correctness_scale": torch.tensor(2.0),
            "correctness_bias": torch.tensor(1.0),
        }

        raw_correctness, raw_hazard, raw_survival = multidim_posterior_row_predictions(
            data, posterior
        )
        cal_correctness, cal_hazard, cal_survival = multidim_posterior_row_predictions(
            data, posterior, calibrate_correctness=True
        )

        self.assertAlmostEqual(float(raw_correctness), 0.5)
        self.assertAlmostEqual(
            float(cal_correctness), float(torch.sigmoid(torch.tensor(1.0)))
        )
        self.assertTrue(torch.allclose(raw_hazard, cal_hazard))
        self.assertTrue(torch.allclose(raw_survival, cal_survival))

    def test_pyramidal_calibration_replays_only_correctness(self):
        data = {
            "player": torch.tensor([0]),
            "tossup": torch.tensor([0]),
            "t_star": torch.tensor([1]),
            "T_j": torch.tensor([2]),
        }
        posterior = {
            "theta": torch.tensor([[0.0]]),
            "c": torch.tensor([0.0]),
            "alpha": torch.tensor([[0.0]]),
            "beta": torch.tensor([0.0]),
            "gamma": torch.tensor([1.0]),
            "mu": torch.tensor([0.5]),
            "correctness_scale": torch.tensor(2.0),
            "correctness_bias": torch.tensor(1.0),
        }

        raw_correctness, raw_hazard, raw_survival = posterior_row_predictions(
            data, posterior
        )
        cal_correctness, cal_hazard, cal_survival = posterior_row_predictions(
            data, posterior, calibrate_correctness=True
        )

        self.assertAlmostEqual(float(raw_correctness), 0.5)
        self.assertAlmostEqual(
            float(cal_correctness), float(torch.sigmoid(torch.tensor(1.0)))
        )
        self.assertTrue(torch.allclose(raw_hazard, cal_hazard))
        self.assertTrue(torch.allclose(raw_survival, cal_survival))

    def test_bonus_calibration_replays_part_correctness_logits(self):
        data = {
            "roster": torch.tensor([[0]]),
            "roster_mask": torch.tensor([[True]]),
            "part": torch.tensor([0]),
        }
        theta = torch.tensor([[0.0]])
        posterior = {
            "alpha": torch.tensor([[0.0]]),
            "beta": torch.tensor([0.0]),
            "tau": torch.tensor(1.0),
            "correctness_scale": torch.tensor(2.0),
            "correctness_bias": torch.tensor(1.0),
        }

        raw_correctness, raw_aggregate, raw_synergy = posterior_predictions(
            data, theta, posterior
        )
        cal_correctness, cal_aggregate, cal_synergy = posterior_predictions(
            data, theta, posterior, calibrate_correctness=True
        )

        self.assertAlmostEqual(float(raw_correctness), 0.5)
        self.assertAlmostEqual(
            float(cal_correctness), float(torch.sigmoid(torch.tensor(1.0)))
        )
        self.assertTrue(torch.allclose(raw_aggregate, cal_aggregate))
        self.assertTrue(torch.allclose(raw_synergy, cal_synergy))

    def test_player_skill_dimensions_use_numeric_order(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "players.csv"
            pd.DataFrame(
                {
                    "player_id": ["p1"],
                    "theta_1": [1.0],
                    "theta_10": [10.0],
                    "theta_2": [2.0],
                    "theta_9": [9.0],
                    "theta_3": [3.0],
                    "theta_8": [8.0],
                    "theta_4": [4.0],
                    "theta_7": [7.0],
                    "theta_5": [5.0],
                    "theta_6": [6.0],
                    "theta_norm": [10.25],
                }
            ).to_csv(path, index=False)

            player_ids, theta = load_player_skills(path, "cpu")

        self.assertEqual(player_ids, ["p1"])
        self.assertEqual(theta.tolist(), [[float(value) for value in range(1, 11)]])

    def test_bonus_metrics_calculate_ppb_at_game_team_level(self):
        parts = pd.DataFrame(
            {
                "response_id": ["r1", "r1", "r2", "r2"],
                "correct": [1, 0, 1, 0],
                "predicted_correct": [0.9, 0.1, 0.8, 0.2],
            }
        )
        teams = pd.DataFrame(
            {
                "game_id": ["g1", "g1", "g2"],
                "team_id": ["a", "a", "b"],
                "total_points": [0, 30, 20],
                "predicted_points": [10, 20, 20],
            }
        )

        metrics = bonus_metrics(parts, teams)

        self.assertAlmostEqual(metrics["per_bonus_points_mae"], 20 / 3)
        self.assertAlmostEqual(metrics["ppb_mae"], 0.0)

    def test_bonus_metrics_distinguish_exact_parts_from_rounded_score(self):
        parts = pd.DataFrame(
            {
                "response_id": ["r1", "r1", "r1", "r2", "r2", "r2"],
                "correct": [1, 0, 0, 0, 1, 1],
                "predicted_correct": [0.49, 0.49, 0.02, 0.1, 0.8, 0.7],
            }
        )
        teams = pd.DataFrame(
            {
                "game_id": ["g1", "g1"],
                "team_id": ["a", "a"],
                "total_points": [10, 20],
                "predicted_points": [10, 16],
            }
        )

        metrics = bonus_metrics(parts, teams)

        self.assertAlmostEqual(metrics["exact_acc"], 0.5)
        self.assertAlmostEqual(metrics["rounded_score_accuracy"], 1.0)

    def test_saved_parameters_reconstruct_first_buzz_distribution(self):
        players = pd.DataFrame(
            {
                "player_id": ["p1", "p2"],
                "c": [0.0, 0.0],
                "theta_1": [0.0, 0.0],
            }
        ).set_index("player_id")
        tossups = pd.DataFrame(
            {
                "tossup_id": ["q1"],
                "beta": [0.0],
                "gamma": [1.0],
                "mu": [0.5],
                "alpha_1": [0.0],
            }
        ).set_index("tossup_id")
        event = pd.DataFrame(
            {
                "player_id": ["p1", "p2"],
                "tossup_id": ["q1", "q1"],
                "T_j": [2, 2],
            }
        )

        mass, dead = first_buzz_distribution(event, players, tossups, n_bins=2)

        self.assertAlmostEqual(float(mass.sum()), 0.9375)
        self.assertAlmostEqual(dead, 0.0625)
        self.assertAlmostEqual(float(mass.sum()) + dead, 1.0)

    def test_saved_multidim_parameters_reconstruct_first_buzz_distribution(self):
        players = pd.DataFrame(
            {
                "player_id": ["p1"],
                "c": [0.0],
                "theta_1": [2.0],
                "theta_2": [4.0],
            }
        ).set_index("player_id")
        tossups = pd.DataFrame(
            {
                "tossup_id": ["q1"],
                "alpha_1": [0.25],
                "alpha_2": [0.75],
                "beta_1": [0.0],
                "beta_2": [0.0],
                "gamma_1": [1.0],
                "gamma_2": [1.0],
                "mu_1": [0.5],
                "mu_2": [0.5],
            }
        ).set_index("tossup_id")
        event = pd.DataFrame(
            {
                "player_id": ["p1"],
                "tossup_id": ["q1"],
                "T_j": [1],
            }
        )

        mass, dead = first_buzz_distribution(event, players, tossups, n_bins=1)

        expected_hazard = 1 / (1 + np.exp(-3.5))
        self.assertAlmostEqual(float(mass[0]), expected_hazard)
        self.assertAlmostEqual(dead, 1 - expected_hazard)

    def test_multidim_difficulty_components_plot_writes_graph(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            results_dir = root / "pyramidal"
            output_dir = root / "evaluation"
            results_dir.mkdir()
            pd.DataFrame(
                {
                    "tossup_id": ["q1"],
                    "alpha_1": [0.25],
                    "alpha_2": [0.75],
                    "beta_1": [2.0],
                    "beta_2": [4.0],
                    "gamma_1": [3.0],
                    "gamma_2": [5.0],
                    "mu_1": [0.35],
                    "mu_2": [0.7],
                }
            ).to_csv(results_dir / "tossups.csv", index=False)
            pd.DataFrame(
                [
                    {
                        "event_id": "e1",
                        "tossup_id": "q1",
                        "z": "BUZZ",
                        "relative_position": 0.25,
                    },
                    {
                        "event_id": "e2",
                        "tossup_id": "q1",
                        "z": "BUZZ",
                        "relative_position": 0.75,
                    },
                ]
            ).to_csv(results_dir / "tossup_predictions.csv", index=False)

            multidim_difficulty_components_plot(results_dir, output_dir)

            graph = output_dir / "graphs" / "tossup_difficulty_curves_by_dimension.png"
            self.assertTrue(graph.exists())
            self.assertGreater(graph.stat().st_size, 0)

    def test_density_estimate_respects_parameter_bounds(self):
        grid, density = density_estimate([0.1, 0.2, 0.3], bounds=(0, 1))

        self.assertGreaterEqual(float(grid.min()), 0.0)
        self.assertLessEqual(float(grid.max()), 1.0)
        self.assertTrue((density >= 0).all())

    def test_saved_team_synergy_includes_pair_normalization_diagnostics(self):
        observations = pd.DataFrame(
            {
                "response_id": ["r1", "r1", "r1"],
                "team_id": ["team-a", "team-a", "team-a"],
                "player_ids": [["p1", "p2", "p3"]] * 3,
            }
        )
        posterior = {"psi": torch.tensor([[1.0], [2.0], [3.0]])}

        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            save_synergy_outputs(
                output_dir,
                ["p1", "p2", "p3"],
                observations,
                posterior,
                [11.0, 11.0, 11.0],
            )
            team = pd.read_csv(output_dir / "team_synergy_contributions.csv").iloc[0]

        self.assertEqual(team["roster_size"], 3)
        self.assertEqual(team["pair_count"], 3)
        self.assertAlmostEqual(team["synergy_per_pair"], 11 / 3)


if __name__ == "__main__":
    unittest.main()
