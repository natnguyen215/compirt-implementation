"""Focused tests for Scenario C classification, fitting, and evaluation."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import pandas as pd
import pyro
import torch
from pyro import poutine
from pyro.infer.autoguide import AutoNormal

from compirt_eval.scenario_c import (
    build_training_context,
    canonical_roster,
    classify_observations,
    scenario_metrics,
    validate_historical_prediction_ids,
)
from scenario_c_model import frozen_global_item_model


def part_rows(response, game, team, roster, scenario=None, predicted=(0.8, 0.2, 0.8)):
    rows = []
    for index, (correct, probability) in enumerate(zip((1.0, 0.0, 1.0), predicted)):
        rows.append(
            {
                "observation_id": f"{response}::part-{index + 1}",
                "response_id": response,
                "game_id": game,
                "team_id": team,
                "tournament_id": "t1",
                "tier": "regionals",
                "player_ids": list(roster),
                "roster_key": "|".join(sorted(roster)),
                "roster_size": len(roster),
                "team_label_key": team.lower(),
                "lineup_segment": "whole_game",
                "lineup_has_game_buzz_evidence": True,
                "lineup_is_full_roster_fallback": False,
                "correct": correct,
                "predicted_correct": probability,
                "total_points": 20,
                "scenario": scenario,
            }
        )
    return rows


class ClassificationTests(unittest.TestCase):
    def test_canonical_roster_is_order_independent_and_arbitrary_size(self):
        self.assertEqual(canonical_roster(["c", "a", "b", "a", "e", "d"]), ("a", "b", "c", "d", "e"))
        with self.assertRaisesRegex(ValueError, "empty"):
            canonical_roster([])

    def test_precedence_and_theta_vs_psi_coverage(self):
        training = pd.DataFrame(
            part_rows("train", "g0", "School A", ["a", "b", "c", "d"])
        )
        context = build_training_context(training, {"a", "b", "c", "d", "e"})
        test = pd.DataFrame(
            part_rows("c1", "g1", "School A", ["d", "c", "b", "a"])
            + part_rows("c2", "g2", "Other", ["a", "b", "c", "e"])
            + part_rows("c3", "g3", "Other", ["a", "new"])
            + part_rows("c4", "g4", "Other", ["x", "y"])
        ).drop(columns=["scenario"])
        result = classify_observations(test, context).drop_duplicates("response_id").set_index("response_id")

        self.assertEqual(result.loc["c1", "scenario"], "C1")
        self.assertEqual(result.loc["c2", "scenario"], "C2")
        self.assertEqual(result.loc["c3", "scenario"], "C3")
        self.assertEqual(result.loc["c4", "scenario"], "C4")
        self.assertEqual(result.loc["c2", "theta_known_member_count"], 4)
        self.assertEqual(result.loc["c2", "psi_informed_member_count"], 3)

    def test_historical_branches_must_match(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pd.DataFrame({"observation_id": ["a"], "response_id": ["r"]}).to_csv(root / "a.csv", index=False)
            pd.DataFrame({"observation_id": ["b"], "response_id": ["r"]}).to_csv(root / "b.csv", index=False)
            with self.assertRaisesRegex(ValueError, "different observation/response"):
                validate_historical_prediction_ids(root / "a.csv", root / "b.csv")

    def test_historical_branches_must_match_response_mapping(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            pd.DataFrame(
                {"observation_id": ["a"], "response_id": ["response-left"]}
            ).to_csv(root / "a.csv", index=False)
            pd.DataFrame(
                {"observation_id": ["a"], "response_id": ["response-right"]}
            ).to_csv(root / "b.csv", index=False)
            with self.assertRaisesRegex(ValueError, "different observation/response"):
                validate_historical_prediction_ids(root / "a.csv", root / "b.csv")


class MetricTests(unittest.TestCase):
    def test_mixed_scenario_game_team_is_excluded_from_scenario_ppb_only(self):
        parts = pd.DataFrame(
            part_rows("r1", "g1", "A", ["a"], "C1")
            + part_rows("r2", "g1", "A", ["b"], "C2")
            + part_rows("r3", "g2", "B", ["a"], "C1")
        )
        c1 = scenario_metrics(parts, "C1")
        overall = scenario_metrics(parts, "ALL")

        self.assertEqual(c1["responses"], 2)
        self.assertEqual(c1["ppb_excluded_mixed_game_teams"], 1)
        self.assertEqual(overall["ppb_excluded_mixed_game_teams"], 0)


class FrozenModelTests(unittest.TestCase):
    def _inputs(self):
        data = {
            "part_ids": ["part-1"],
            "part": torch.tensor([0]),
            "roster": torch.tensor([[0, 1]]),
            "roster_mask": torch.tensor([[True, True]]),
            "y": torch.tensor([1.0]),
        }
        theta = torch.tensor([[1.0, 0.0], [0.0, 1.0]])
        tau = torch.tensor(1.0)
        psi = torch.tensor([[0.2], [0.1]])
        return data, theta, tau, psi

    def test_only_item_parameters_are_latent(self):
        data, theta, tau, psi = self._inputs()
        trace = poutine.trace(frozen_global_item_model).get_trace(data, theta, tau, psi)
        self.assertIsInstance(
            trace.nodes["alpha"]["fn"].base_dist, torch.distributions.Normal
        )
        sample_sites = {
            name for name, node in trace.nodes.items()
            if node.get("type") == "sample" and not node.get("is_observed")
            and name not in {"bonus_parts", "bonus_observations"}
        }
        self.assertEqual(sample_sites, {"alpha", "beta"})

        pyro.clear_param_store()
        guide = AutoNormal(frozen_global_item_model)
        guide(data, theta, tau, psi)
        self.assertEqual(set(guide.prototype_trace.nodes) & {"psi", "tau", "theta"}, set())


if __name__ == "__main__":
    unittest.main()
