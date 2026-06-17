"""Focused regression tests for the streamlined CompIRT pipeline."""

import math
import tempfile
import unittest
from pathlib import Path

import pandas as pd
import torch

from compirt_data import (
    bonus_tensors,
    build_bonus_part_observations,
    build_tossup_observations,
    tossup_tensors,
)
from compositional_model import lse_aggregation, synergy_contribution
from evaluate_compirt import bonus_metrics, density_estimate, first_buzz_distribution
from pyramidal_model import log_survival
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
        observations = build_tossup_observations(synthetic_tables())

        first_buzz = observations[observations["tossup_id"] == "q1"]
        dead = observations[observations["tossup_id"] == "q2"]

        self.assertEqual(first_buzz["z"].value_counts().to_dict(), {"CENSORED": 2, "BUZZ": 1})
        self.assertEqual(set(dead["z"]), {"NO-BUZZ"})
        self.assertEqual(len(dead), 3)

    def test_tossup_tensors_preserve_dead_tossup_mask(self):
        data = tossup_tensors(build_tossup_observations(synthetic_tables()))

        self.assertEqual(tuple(data["player"].shape), (6,))
        self.assertEqual(int(data["is_buzz"].sum()), 1)
        self.assertEqual(int(data["is_no_buzz"].sum()), 3)

    def test_bonus_observations_and_padding(self):
        observations = build_bonus_part_observations(synthetic_tables())
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
