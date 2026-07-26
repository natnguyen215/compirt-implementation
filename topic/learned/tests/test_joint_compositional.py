"""Tests for the joint supervised-LDA + compositional bonus model."""

from __future__ import annotations

import unittest

import torch
import torch.nn.functional as F

from topic.learned.joint_compositional import (
    joint_compositional_model,
    joint_posterior_predictions,
)
from topic.learned.train_joint_compositional import build_part_doc_index
from utils.training import fit_svi


class PartDocIndexTests(unittest.TestCase):
    def test_parts_of_a_bonus_share_one_document_row(self):
        # Parts arrive interleaved; each distinct bonus gets one document row in
        # first-appearance order, and every part maps back to its bonus's row.
        part_ids = [
            "b0::part-1", "b0::part-2", "b1::part-1", "b0::part-3", "b1::part-2",
        ]
        ordered, part_doc_index = build_part_doc_index(part_ids)
        self.assertEqual(ordered, ["b0", "b1"])
        self.assertEqual(part_doc_index, [0, 0, 1, 0, 1])

    def test_bonus_id_with_separator_in_name_is_preserved(self):
        # bonus_id_from_part_id strips only the trailing ::part-N suffix.
        ordered, part_doc_index = build_part_doc_index(["set::edition::b3::part-2"])
        self.assertEqual(ordered, ["set::edition::b3"])
        self.assertEqual(part_doc_index, [0])


def tiny_problem(seed=0):
    """Build a minimal data/theta/topic_word problem for smoke tests."""
    torch.manual_seed(seed)
    n_players, dim, vocab = 4, 2, 5
    part_ids = [
        "b0::part-1", "b0::part-2", "b0::part-3",
        "b1::part-1", "b1::part-2", "b1::part-3",
    ]
    ordered, part_doc_index = build_part_doc_index(part_ids)
    n_bonuses = len(ordered)

    theta = torch.randn(n_players, dim)
    topic_word = F.softmax(torch.randn(dim, vocab), dim=-1)
    bonus_bow = torch.randint(0, 4, (n_bonuses, vocab)).float()

    # One observation per part, each with a two-player roster.
    part = torch.arange(len(part_ids), dtype=torch.long)
    roster = torch.tensor([[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [0, 3]])
    roster_mask = torch.ones_like(roster, dtype=torch.bool)
    y = torch.tensor([1.0, 0.0, 1.0, 0.0, 1.0, 0.0])

    data = {
        "part_ids": part_ids,
        "part": part,
        "part_doc_index": torch.tensor(part_doc_index, dtype=torch.long),
        "bonus_bow": bonus_bow,
        "roster": roster,
        "roster_mask": roster_mask,
        "y": y,
    }
    return data, theta, topic_word


class ModelSmokeTests(unittest.TestCase):
    def _fit(self, use_synergy):
        data, theta, topic_word = tiny_problem()
        posterior, _guide, losses = fit_svi(
            joint_compositional_model,
            model_kwargs={
                "data": data,
                "theta": theta,
                "topic_word": topic_word,
                "bow_weight": 1.0,
                "topic_concentration": 1.0,
                "use_synergy": use_synergy,
                "synergy_dimensions": 2,
                "calibrate_correctness": False,
            },
            n_steps=5,
            lr=0.05,
        )
        return data, theta, posterior, losses

    def test_trains_without_synergy(self):
        data, theta, posterior, losses = self._fit(use_synergy=False)
        self.assertEqual(len(losses), 5)
        self.assertTrue(all(loss == loss for loss in losses))  # no NaNs
        self.assertEqual(tuple(posterior["theta_doc"].shape), (2, 2))
        probs, aggregate, synergy = joint_posterior_predictions(
            data, theta, posterior, use_synergy=False
        )
        self.assertEqual(tuple(probs.shape), (len(data["y"]),))
        self.assertTrue(((probs >= 0) & (probs <= 1)).all())

    def test_trains_with_synergy(self):
        data, theta, posterior, losses = self._fit(use_synergy=True)
        self.assertEqual(len(losses), 5)
        self.assertIn("psi", posterior)
        probs, aggregate, synergy = joint_posterior_predictions(
            data, theta, posterior, use_synergy=True
        )
        self.assertEqual(tuple(synergy.shape), (len(data["y"]),))


if __name__ == "__main__":
    unittest.main()
