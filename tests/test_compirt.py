"""Focused regression tests for the streamlined CompIRT pipeline."""

import math
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd
import pyro
import pyro.distributions as dist
import torch
import torch.nn.functional as F
from pyro.infer import SVI, Trace_ELBO
from pyro.infer.autoguide import AutoNormal
from pyro.optim import ClippedAdam

from compirt_eval.synergy_comparison import LOWER_IS_BETTER
from compirt_data import (
    bonus_tensors,
    build_bonus_part_observations,
    build_tossup_observations,
    tossup_tensors,
)
from compirt_race import winner_log_prob
from lineup import LineupIndex
from compirt_eval.scenario_b_bonuses.evaluation import evaluate_bonuses
from compirt_eval.scenario_b_bonuses.metrics import bonus_metrics
from compirt_eval.scenario_a_tossups.parameters import (
    _multidim_difficulty_components,
    _parameter_columns,
    load_difficulty_link,
    load_difficulty_scale,
)
from compirt_eval.scenario_a_tossups.reconstruction import event_first_buzz_components
from compirt_eval.scenario_a_tossups.metrics import tossup_joint_event_scores
from compositional_model import (
    compositional_model,
    lse_aggregation,
    posterior_predictions,
    synergy_contribution,
)
from compirt_eval.common.figures import density_estimate
from compirt_eval.scenario_a_tossups.reconstruction import first_buzz_distribution
from multidimensional.multidim_mirt.pyramidal_model import (
    competing_risks_model as multidim_competing_risks_model,
    correctness_logit as multidim_correctness_logit,
    difficulty_curve as multidim_difficulty_curve,
    posterior_row_predictions as multidim_posterior_row_predictions,
)
from pyramidal_model import (
    correctness_logit,
    expected_first_buzz_positions,
    hazard_logit,
    log_survival,
    posterior_row_predictions,
    row_parameters,
)
from train_compositional import load_player_skills
from utils.saving import save_synergy_outputs, save_tossup_predictions


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


def bounceback_tables():
    """A single tossup whose first buzz is a neg followed by a converted bounce.

    Team A = [p1, p2], Team B = [p3, p4]. p1 negs at token 2 (value -5); p3
    bounces back correctly at token 4 (value 10). The question has six tokens.
    """
    tables = synthetic_tables()
    tables["teams"] = pd.DataFrame(
        [
            {"team_id": "team-a", "tournament_id": "t1", "player_ids": ["p1", "p2"]},
            {"team_id": "team-b", "tournament_id": "t1", "player_ids": ["p3", "p4"]},
        ]
    )
    tables["games"] = pd.DataFrame(
        [
            {
                "game_id": "g1",
                "tournament_id": "t1",
                "packet_id": 10,
                "team_ids": ["team-a", "team-b"],
                "tossups_read": 1,
            }
        ]
    )
    tables["tossups"] = pd.DataFrame(
        [
            {
                "tossup_id": "q1",
                "question_set_event_id": "qs1",
                "packet": 10,
                "question_num": 1,
                "tokens": ["one", "two", "three", "four", "five", "six"],
            }
        ]
    )
    tables["tossup_buzzes"] = pd.DataFrame(
        [
            {
                "buzz_id": "g1::buzz-1",
                "game_id": "g1",
                "tossup_id": "q1",
                "player_id": "p1",
                "team_id": "team-a",
                "token_position": 2,
                "num_tokens_total": 6,
                "correct": False,
                "value": -5,
            },
            {
                "buzz_id": "g1::buzz-2",
                "game_id": "g1",
                "tossup_id": "q1",
                "player_id": "p3",
                "team_id": "team-b",
                "token_position": 4,
                "num_tokens_total": 6,
                "correct": True,
                "value": 10,
            },
        ]
    )
    return tables


def neg_event_tables(buzz_rows):
    """A single neg tossup with a caller-supplied buzz sequence.

    'buzz_rows' is a list of (player_id, team_id, token, correct, value) tuples
    in the order they occurred; buzz IDs are assigned so token/order sorting is
    stable. Team A = [p1, p2], Team B = [p3, p4], six tokens.
    """
    tables = bounceback_tables()
    tables["tossup_buzzes"] = pd.DataFrame(
        [
            {
                "buzz_id": f"g1::buzz-{index + 1}",
                "game_id": "g1",
                "tossup_id": "q1",
                "player_id": player_id,
                "team_id": team_id,
                "token_position": token,
                "num_tokens_total": 6,
                "correct": correct,
                "value": value,
            }
            for index, (player_id, team_id, token, correct, value) in enumerate(
                buzz_rows
            )
        ]
    )
    return tables


class DataTests(unittest.TestCase):
    def test_tossup_observations_expand_roster_and_recover_dead_tossup(self):
        tables = synthetic_tables()
        observations = build_tossup_observations(tables, LineupIndex.from_tables(tables))

        first_buzz = observations[observations["tossup_id"] == "q1"]
        dead = observations[observations["tossup_id"] == "q2"]

        self.assertEqual(first_buzz["z"].value_counts().to_dict(), {"CENSORED": 2, "BUZZ": 1})
        self.assertEqual(set(dead["z"]), {"NO-BUZZ"})
        self.assertEqual(len(dead), 3)

    def test_bounceback_off_by_default_leaves_first_buzz_rows_unchanged(self):
        tables = bounceback_tables()
        lineups = LineupIndex.from_tables(tables)
        default = build_tossup_observations(tables, lineups)

        self.assertEqual(set(default["t_start"]), {1})
        self.assertEqual(set(default["phase"]), {0})

    def test_bounceback_rows_add_opponent_phase1_risk_set(self):
        tables = bounceback_tables()
        lineups = LineupIndex.from_tables(tables)
        observations = build_tossup_observations(
            tables, lineups, include_bounceback=True
        )

        phase0 = observations[observations["phase"] == 0]
        phase1 = observations[observations["phase"] == 1]

        # Phase 0 is the ordinary full-field first buzz: the neg plus three
        # censored lineup members, all at risk from token 1.
        self.assertEqual(
            phase0["z"].value_counts().to_dict(), {"CENSORED": 3, "BUZZ": 1}
        )
        self.assertEqual(set(phase0["t_start"]), {1})

        # Phase 1 is opponent-only (team B), entering the risk set at t_neg + 1.
        self.assertEqual(set(phase1["player_id"]), {"p3", "p4"})
        self.assertEqual(set(phase1["t_start"]), {3})
        self.assertEqual(set(phase1["t_star"]), {4})

        bounce_buzz = phase1[phase1["z"] == "BOUNCE-BUZZ"]
        self.assertEqual(bounce_buzz["player_id"].tolist(), ["p3"])
        self.assertEqual(bounce_buzz["y"].tolist(), [1.0])
        self.assertEqual(
            phase1[phase1["z"] == "BOUNCE-CENSORED"]["player_id"].tolist(), ["p4"]
        )

        # The bounceback buzzer feeds hazard + correctness (is_buzz) but is kept
        # out of the phase-0 first-buzz timing set (is_phase0).
        data = tossup_tensors(observations)
        self.assertEqual(int(data["is_buzz"].sum()), 2)
        self.assertEqual(int(data["is_phase0"].sum()), len(phase0))

    def test_genuine_dead_bounceback_is_right_censored(self):
        # A neg with no later buzz at all is legitimate right-censoring: the
        # opponent heard the rest and never buzzed.
        tables = neg_event_tables([("p1", "team-a", 2, False, -5)])
        phase1 = build_tossup_observations(
            tables, LineupIndex.from_tables(tables), include_bounceback=True
        ).query("phase == 1")
        self.assertEqual(set(phase1["z"]), {"BOUNCE-NO-BUZZ"})
        self.assertEqual(set(phase1["player_id"]), {"p3", "p4"})
        self.assertEqual(set(phase1["t_star"]), {6})

    def test_same_team_continuation_skips_to_later_opponent_buzz(self):
        # p1 negs; a spurious same-team p2 record follows; then p3 (opponent)
        # actually converts. The bounceback must be attributed to p3, not the
        # impossible-under-lockout same-team record.
        tables = neg_event_tables(
            [
                ("p1", "team-a", 2, False, -5),
                ("p2", "team-a", 3, False, 0),  # same-team anomaly, skipped
                ("p3", "team-b", 4, True, 10),  # real opponent conversion
            ]
        )
        phase1 = build_tossup_observations(
            tables, LineupIndex.from_tables(tables), include_bounceback=True
        ).query("phase == 1")
        self.assertEqual(
            phase1[phase1["z"] == "BOUNCE-BUZZ"]["player_id"].tolist(), ["p3"]
        )
        self.assertEqual(set(phase1["player_id"]), {"p3", "p4"})

    def test_same_team_continuation_without_opponent_omits_phase1(self):
        # Only same-team continuations and no opponent buzz: phase 1 is omitted
        # rather than fabricated as a no-buzz (which would falsely assert the
        # opponent survived to the end).
        tables = neg_event_tables(
            [
                ("p1", "team-a", 2, False, -5),
                ("p2", "team-a", 3, False, 0),  # same-team anomaly, no opponent
            ]
        )
        observations = build_tossup_observations(
            tables, LineupIndex.from_tables(tables), include_bounceback=True
        )
        self.assertTrue((observations["phase"] == 0).all())

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

    def test_tossup_predictions_include_expected_buzz_timing(self):
        observations = pd.DataFrame(
            [
                {
                    "event_id": "event-1",
                    "player_id": "player-1",
                    "z": "BUZZ",
                    "y": 1.0,
                    "relative_position": 0.5,
                }
            ]
        )
        values = torch.tensor([0.75])
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            save_tossup_predictions(
                output_dir,
                observations,
                values,
                values,
                values,
                buzz_expected={"event-1": 0.625},
            )
            buzz_events = pd.read_csv(output_dir / "buzz_event_predictions.csv")

        self.assertEqual(buzz_events["event_id"].tolist(), ["event-1"])
        self.assertEqual(buzz_events["predicted_relative_position"].tolist(), [0.625])


class ModelTests(unittest.TestCase):
    def test_bonus_alpha_uses_paper_normal_prior(self):
        data = {
            "part_ids": ["part-1"],
            "part": torch.tensor([0]),
            "roster": torch.tensor([[0]]),
            "roster_mask": torch.tensor([[True]]),
            "y": torch.tensor([1.0]),
        }
        trace = pyro.poutine.trace(compositional_model).get_trace(
            data, torch.zeros((1, 2))
        )

        self.assertIsInstance(
            trace.nodes["alpha"]["fn"].base_dist, torch.distributions.Normal
        )

    def test_dead_tossup_survival_matches_equations_6_and_13(self):
        zero_vector = torch.zeros((1, 1))
        zero = torch.zeros(1)
        t_star = torch.tensor([3])
        T_j = torch.tensor([3])

        survival = log_survival(
            zero_vector, zero_vector, zero, zero, zero, zero, t_star, T_j
        )
        self.assertAlmostEqual(float(survival), 2 * math.log(0.5), places=6)

    def test_interval_survival_masks_tokens_before_t_start(self):
        # A phase-1 bounceback row survives only over [t_start, t_star); tokens
        # before t_start belong to phase 0 and must not be recounted here.
        theta = torch.tensor([[0.6]])
        alpha = torch.tensor([[1.3]])
        beta = torch.tensor([0.7])
        gamma = torch.tensor([2.0])
        mu = torch.tensor([0.4])
        c = torch.tensor([0.2])
        t_star = torch.tensor([6])
        t_start = torch.tensor([3])
        T_j = torch.tensor([8])

        interval = log_survival(theta, alpha, beta, gamma, mu, c, t_star, T_j, t_start)

        # Independent reference: explicit product of (1 - hazard(s)) over the
        # interval tokens s in {3, 4, 5}.
        reference = 0.0
        for s in range(int(t_start), int(t_star)):
            logit = hazard_logit(
                theta, alpha, beta, gamma, mu, c, torch.tensor([float(s)]), T_j
            )
            reference += float(F.logsigmoid(-logit))
        self.assertAlmostEqual(float(interval), reference, places=5)

        # Passing t_start = 1 reproduces the historical [1, t_star) survival.
        full = log_survival(theta, alpha, beta, gamma, mu, c, t_star, T_j)
        full_with_start = log_survival(
            theta, alpha, beta, gamma, mu, c, t_star, T_j, torch.tensor([1])
        )
        self.assertAlmostEqual(float(full), float(full_with_start), places=6)

    def test_bounceback_likelihood_matches_hand_summed_competing_risks(self):
        # End-to-end: the log-likelihood the model assembles from phase-aware
        # rows must equal the neg-then-bounceback competing-risks likelihood
        # written out by hand (paper Section 3.1 / Appendix A).
        tables = bounceback_tables()
        lineups = LineupIndex.from_tables(tables)
        observations = build_tossup_observations(
            tables, lineups, include_bounceback=True
        )
        data = tossup_tensors(observations)
        # Fix this scenario's roster so the hand reference below is unambiguous.
        self.assertEqual(set(data["player_ids"]), {"p1", "p2", "p3", "p4"})

        pidx = {pid: i for i, pid in enumerate(data["player_ids"])}
        theta = torch.tensor([[0.5], [-0.3], [0.8], [0.1]])
        c = torch.tensor([0.2, 0.0, -0.1, 0.3])
        alpha = torch.tensor([[1.2]])
        beta = torch.tensor([0.7])
        gamma = torch.tensor([2.0])
        mu = torch.tensor([0.4])

        # Roster survival plus an exclusive-winner term for each phase.
        row_theta, row_c, row_alpha, row_beta, row_gamma, row_mu = row_parameters(
            data, theta, c, alpha, beta, gamma, mu
        )
        survival = log_survival(
            row_theta, row_alpha, row_beta, row_gamma, row_mu, row_c,
            data["t_star"], data["T_j"], data["t_start"],
        ).sum()
        buzz = data["is_buzz"]
        buzz_logits = hazard_logit(
            row_theta, row_alpha, row_beta, row_gamma,
            row_mu, row_c, data["t_star"], data["T_j"],
        )
        correctness = correctness_logit(
            row_theta[buzz], row_alpha[buzz], row_beta[buzz], row_gamma[buzz],
            row_mu[buzz], data["t_star"][buzz], data["T_j"][buzz],
        )
        assembled = float(
            survival
            + winner_log_prob(data, buzz_logits).sum()
            + dist.Bernoulli(logits=correctness).log_prob(data["y"][buzz]).sum()
        )

        # Hand reference for T_j = 6, neg by p1 at token 2, bounce by p3 at 4.
        T_j = torch.tensor([6])

        def hazard(pid, token):
            return hazard_logit(
                theta[pidx[pid]], alpha[0], beta, gamma, mu, c[pidx[pid]],
                torch.tensor([float(token)]), T_j,
            )

        def correct_logit(pid, token):
            return correctness_logit(
                theta[pidx[pid]], alpha[0], beta, gamma, mu,
                torch.tensor([float(token)]), T_j,
            )

        reference = 0.0
        # Phase 0: all four players survive [1, 2); p1 buzzes (neg) at token 2.
        for pid in ("p1", "p2", "p3", "p4"):
            for s in range(1, 2):
                reference += float(F.logsigmoid(-hazard(pid, s)))
        hazards = [float(torch.sigmoid(hazard(pid, 2))) for pid in ("p1", "p2", "p3", "p4")]
        odds = [h / (1 - h) for h in hazards]
        reference += math.log((1 - math.prod(1 - h for h in hazards)) * odds[0] / sum(odds))
        reference += float(F.logsigmoid(-correct_logit("p1", 2)))  # neg: y = 0
        # Phase 1: opponent (p3, p4) survives [3, 4); p3 converts at token 4.
        for pid in ("p3", "p4"):
            for s in range(3, 4):
                reference += float(F.logsigmoid(-hazard(pid, s)))
        hazards = [float(torch.sigmoid(hazard(pid, 4))) for pid in ("p3", "p4")]
        odds = [h / (1 - h) for h in hazards]
        reference += math.log((1 - math.prod(1 - h for h in hazards)) * odds[0] / sum(odds))
        reference += float(F.logsigmoid(correct_logit("p3", 4)))   # bounce: y = 1

        self.assertAlmostEqual(assembled, reference, places=5)

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

    def test_multidim_difficulty_curve_and_r_weighted_formula(self):
        theta = torch.tensor([[10.0, 0.0]])
        r = torch.tensor([[0.25, 0.75]])
        beta = torch.tensor([[4.0, 8.0]])
        gamma = torch.tensor([[0.0, 0.0]])
        mu = torch.tensor([[0.5, 0.5]])
        t = torch.tensor([1])
        T_j = torch.tensor([2])

        difficulty = multidim_difficulty_curve(beta, gamma, mu, t, T_j)
        logit = multidim_correctness_logit(theta, r, beta, gamma, mu, t, T_j)

        self.assertEqual(tuple(difficulty.shape), (1, 2))
        self.assertTrue(torch.allclose(difficulty, torch.tensor([[2.0, 4.0]])))
        # 0.25 * (10 - 2) + 0.75 * (0 - 4)
        self.assertTrue(torch.allclose(logit, torch.tensor([-1.0])))

    def test_multidim_svi_posterior_uses_vector_difficulty_with_r(self):
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

        self.assertEqual(tuple(posterior["r"].shape), (1, 2))
        self.assertTrue(torch.all(posterior["r"] > 0))
        self.assertEqual(tuple(posterior["beta"].shape), (1, 2))
        self.assertEqual(tuple(posterior["gamma"].shape), (1, 2))
        self.assertEqual(tuple(posterior["mu"].shape), (1, 2))

    def test_calibration_replays_only_correctness(self):
        """`correctness_scale`/`bias` must rescale correctness and nothing else.

        Both families share the contract: replaying with calibration on leaves
        the buzz hazard and survival untouched, because the calibration is a
        read-out transform, not part of the fitted timing model.
        """
        data = {
            "player": torch.tensor([0]),
            "tossup": torch.tensor([0]),
            "t_star": torch.tensor([1]),
            "T_j": torch.tensor([2]),
        }
        calibration = {
            "correctness_scale": torch.tensor(2.0),
            "correctness_bias": torch.tensor(1.0),
        }
        families = {
            "multidim": (
                multidim_posterior_row_predictions,
                {
                    "theta": torch.tensor([[0.0, 0.0]]),
                    "c": torch.tensor([0.0]),
                    "r": torch.tensor([[1.0, 1.0]]),
                    "beta": torch.tensor([[0.0, 0.0]]),
                    "gamma": torch.tensor([[1.0, 1.0]]),
                    "mu": torch.tensor([[0.5, 0.5]]),
                },
            ),
            "pyramidal": (
                posterior_row_predictions,
                {
                    "theta": torch.tensor([[0.0]]),
                    "c": torch.tensor([0.0]),
                    "alpha": torch.tensor([[0.0]]),
                    "beta": torch.tensor([0.0]),
                    "gamma": torch.tensor([1.0]),
                    "mu": torch.tensor([0.5]),
                },
            ),
        }

        for family, (predict, parameters) in families.items():
            with self.subTest(family=family):
                posterior = {**parameters, **calibration}
                raw = predict(data, posterior)
                calibrated = predict(data, posterior, calibrate_correctness=True)

                self.assertAlmostEqual(float(raw[0]), 0.5)
                self.assertAlmostEqual(
                    float(calibrated[0]), float(torch.sigmoid(torch.tensor(1.0)))
                )
                self.assertTrue(torch.allclose(raw[1], calibrated[1]))
                self.assertTrue(torch.allclose(raw[2], calibrated[2]))

    def test_expected_buzz_position_conditions_on_a_buzz(self):
        data = {
            "player": torch.tensor([0]),
            "tossup": torch.tensor([0]),
            "event": torch.tensor([0]),
            "T_j": torch.tensor([2]),
            "y": torch.tensor([1.0]),
            "event_ids": ["e1"],
        }
        posterior = {
            "theta": torch.tensor([[0.0]]),
            "c": torch.tensor([0.0]),
            "alpha": torch.tensor([[0.0]]),
            "beta": torch.tensor([0.0]),
            "gamma": torch.tensor([1.0]),
            "mu": torch.tensor([0.5]),
        }

        expected = expected_first_buzz_positions(data, posterior)

        # Hazards are 0.5 at both tokens, so conditional first-buzz masses are
        # 2/3 at token 1 and 1/3 at token 2. The expected relative position is
        # therefore (1 * 2/3 + 2 * 1/3) / 2 = 2/3.
        self.assertAlmostEqual(expected["e1"], 2 / 3)

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

    def test_bonus_metrics_calculate_team_level_ppb(self):
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

        self.assertAlmostEqual(metrics["ppb_mae"], 0.0)

    def test_ppb_mae_pools_all_response_rows_by_team(self):
        parts = pd.DataFrame(
            {
                "response_id": ["r1", "r1", "r1"],
                "correct": [1, 0, 0],
                "predicted_correct": [0.8, 0.1, 0.1],
            }
        )
        teams = pd.DataFrame(
            {
                "team_id": ["a", "a"],
                "total_points": [0, 30],
                "predicted_points": [10, 20],
            }
        )

        metrics = bonus_metrics(parts, teams)

        self.assertAlmostEqual(metrics["ppb_mae"], 0.0)
        self.assertIn("ppb_mae", LOWER_IS_BETTER)

    def test_bonus_metrics_report_team_and_bonus_macro_accuracy(self):
        parts = pd.DataFrame(
            {
                "response_id": [f"r{index}" for index in range(6)],
                "team_id": ["a", "a", "a", "a", "b", "b"],
                "game_id": ["g1", "g1", "g1", "g1", "g1", "g2"],
                "bonus_id": ["q1", "q1", "q2", "q2", "q2", "q2"],
                "correct": [1, 1, 1, 1, 1, 1],
                "predicted_correct": [0.9, 0.8, 0.7, 0.4, 0.3, 0.2],
            }
        )
        teams = pd.DataFrame(
            {
                "team_id": ["a", "b"],
                "total_points": [20, 0],
                "predicted_points": [20, 0],
            }
        )

        metrics = bonus_metrics(parts, teams)

        self.assertAlmostEqual(metrics["part_accuracy"], 0.5)
        self.assertAlmostEqual(metrics["part_all_correct_accuracy"], 1.0)
        self.assertAlmostEqual(metrics["accuracy_lift_over_all_correct"], -0.5)
        self.assertAlmostEqual(metrics["part_accuracy_macro_team"], 0.375)
        self.assertAlmostEqual(metrics["part_accuracy_macro_bonus"], 0.625)

    def test_bonus_metrics_report_strict_exact_part_recovery(self):
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
                "r_1": [0.25],
                "r_2": [0.75],
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

    def test_biased_tanh_difficulty_uses_saved_bias_and_scale(self):
        with tempfile.TemporaryDirectory() as directory:
            results_dir = Path(directory) / "pyramidal"
            results_dir.mkdir()
            (results_dir / "summary.json").write_text(
                '{"model": "multidim-tanhbias-competing-risks", '
                '"difficulty_scale": 3.0}',
                encoding="utf-8",
            )
            row = pd.Series(
                {
                    "r_1": 0.25,
                    "r_2": 0.75,
                    "bias_1": 0.0,
                    "bias_2": 0.5,
                    "gamma_1": 2.0,
                    "gamma_2": 4.0,
                    "mu_1": 0.5,
                    "mu_2": 0.25,
                }
            )

            link = load_difficulty_link(results_dir)
            scale = load_difficulty_scale(results_dir)

        positions = np.array([0.25, 0.5])
        per_dimension, aggregate = _multidim_difficulty_components(
            row, _parameter_columns(row), positions, link, scale
        )
        expected = 3.0 * np.tanh(
            np.array([[2.0], [4.0]]) * (np.array([[0.5], [0.25]]) - positions)
            + np.array([[0.0], [0.5]])
        )

        np.testing.assert_allclose(per_dimension, expected)
        np.testing.assert_allclose(aggregate, np.array([0.25, 0.75]) @ expected)

        players = pd.DataFrame(
            {"theta_1": [0.0], "theta_2": [0.0], "c": [0.0]},
            index=pd.Index(["p1"], name="player_id"),
        )
        tossups = pd.DataFrame(
            [row], index=pd.Index(["q1"], name="tossup_id")
        )
        event = pd.DataFrame(
            {"player_id": ["p1"], "tossup_id": ["q1"], "T_j": [2]}
        )
        scaled = event_first_buzz_components(
            event, players, tossups, link=link, difficulty_scale=scale
        )
        unscaled = event_first_buzz_components(
            event, players, tossups, link=link
        )
        self.assertFalse(
            np.allclose(scaled["first_buzz_mass"], unscaled["first_buzz_mass"])
        )

    def test_bonus_score_probability_ledger_and_log_loss(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            results_dir = root / "compositional"
            output_dir = root / "evaluation"
            results_dir.mkdir()
            pd.DataFrame(
                {
                    "response_id": ["r1"] * 3 + ["r2"] * 3,
                    "team_id": ["team-a"] * 6,
                    "bonus_id": ["b1"] * 3 + ["b2"] * 3,
                    "correct": [0, 0, 0, 1, 1, 1],
                    "predicted_correct": [0.1, 0.2, 0.3, 0.7, 0.8, 0.9],
                }
            ).to_csv(results_dir / "bonus_part_predictions.csv", index=False)
            pd.DataFrame(
                {
                    "game_id": ["g1", "g1"],
                    "team_id": ["team-a", "team-a"],
                    "total_points": [0, 30],
                    "predicted_points": [6, 24],
                }
            ).to_csv(results_dir / "team_predictions.csv", index=False)

            metrics = evaluate_bonuses(results_dir, output_dir)

            ledger = pd.read_csv(
                output_dir / "csvs" / "bonus_score_probability_predictions.csv"
            )
            self.assertIn("score_log_loss", ledger)
            self.assertIn("observed_score_probability", ledger)
            self.assertTrue(np.isfinite(metrics["bonus_total_score_log_loss"]))

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


class BouncebackEvaluationTests(unittest.TestCase):
    """The saved-CSV evaluation must stay phase-0 when bounceback rows exist."""

    @staticmethod
    def _flat_hazard_prediction_rows():
        """Four phase-0 + two phase-1 rows, every hazard/survival factor 0.5."""
        return pd.DataFrame(
            [
                # phase 0: full field
                {"event_id": "g1::q1", "tossup_id": "q1", "player_id": "p1",
                 "team_id": "team-a", "T_j": 3, "z": "BUZZ", "y": 1.0,
                 "predicted_survival": 0.5, "predicted_hazard": 0.5,
                 "predicted_correct": 0.5},
                {"event_id": "g1::q1", "tossup_id": "q1", "player_id": "p2",
                 "team_id": "team-a", "T_j": 3, "z": "CENSORED", "y": 0.0,
                 "predicted_survival": 0.5, "predicted_hazard": 0.5,
                 "predicted_correct": 0.5},
                {"event_id": "g1::q1", "tossup_id": "q1", "player_id": "p3",
                 "team_id": "team-b", "T_j": 3, "z": "CENSORED", "y": 0.0,
                 "predicted_survival": 0.5, "predicted_hazard": 0.5,
                 "predicted_correct": 0.5},
                {"event_id": "g1::q1", "tossup_id": "q1", "player_id": "p4",
                 "team_id": "team-b", "T_j": 3, "z": "CENSORED", "y": 0.0,
                 "predicted_survival": 0.5, "predicted_hazard": 0.5,
                 "predicted_correct": 0.5},
                # phase 1: opponent-only continuation (must be ignored)
                {"event_id": "g1::q1", "tossup_id": "q1", "player_id": "p3",
                 "team_id": "team-b", "T_j": 3, "z": "BOUNCE-BUZZ", "y": 1.0,
                 "predicted_survival": 0.5, "predicted_hazard": 0.5,
                 "predicted_correct": 0.5},
                {"event_id": "g1::q1", "tossup_id": "q1", "player_id": "p4",
                 "team_id": "team-b", "T_j": 3, "z": "BOUNCE-CENSORED", "y": 0.0,
                 "predicted_survival": 0.5, "predicted_hazard": 0.5,
                 "predicted_correct": 0.5},
            ]
        )

    def test_first_buzz_reconstruction_ignores_bounceback_rows(self):
        # theta/beta/c all zero -> hazard 0.5 for every player at every token.
        players = pd.DataFrame(
            {"player_id": ["p1", "p2", "p3", "p4"], "theta_1": 0.0, "c": 0.0}
        ).set_index("player_id")
        tossups = pd.DataFrame(
            {"tossup_id": ["q1"], "beta": [0.0], "gamma": [1.0], "mu": [0.5],
             "alpha_1": [1.0]}
        ).set_index("tossup_id")
        event = self._flat_hazard_prediction_rows()

        components = event_first_buzz_components(event, players, tossups)

        # Four players at hazard 0.5: P(first buzz at token 1) = 1 - 0.5^4.
        # Double-counting p3/p4 (six players) would give 1 - 0.5^6 = 0.984375.
        self.assertAlmostEqual(
            float(components["first_buzz_mass"][0]), 0.9375, places=6
        )
        self.assertEqual(len(components["player_ids"]), 4)

    def test_joint_event_score_is_phase0_only(self):
        scores = tossup_joint_event_scores(self._flat_hazard_prediction_rows())
        row = scores.iloc[0]
        # Phase-0 survival only: 0.5^4 = 0.0625 (not 0.5^6 from the six rows).
        self.assertAlmostEqual(float(row["survival_probability"]), 0.0625, places=9)
        # Full phase-0 score: survival * P(any buzz) / four players * correctness.
        self.assertAlmostEqual(
            float(row["joint_event_probability"]), 0.0625 * 0.9375 / 4 * 0.5, places=9
        )


if __name__ == "__main__":
    unittest.main()
