"""Ensure learned-topic initialization follows the observation precision."""

import unittest

import pyro
import torch

from topic.learned.joint_pyramidal import joint_model
from topic.tfidf.joint_pyramidal import joint_model as tfidf_joint_model


class TopicPrecisionTests(unittest.TestCase):
    def test_double_precision_word_likelihood_and_gradients(self):
        data = {
            "bow": torch.tensor([[2.0, 1.0]], dtype=torch.float64),
            "y": torch.tensor([1.0], dtype=torch.float64),
            "player_ids": ["p"], "tossup_ids": ["q"],
            "player": torch.tensor([0]), "tossup": torch.tensor([0]),
            "event": torch.tensor([0]), "event_ids": ["e"],
            "t_star": torch.tensor([1]), "T_j": torch.tensor([2]),
            "is_buzz": torch.tensor([True]),
            "tfidf_prefix": torch.tensor([[0.5, 1.0]], dtype=torch.float64),
        }
        for model in (joint_model, tfidf_joint_model):
            with self.subTest(model=model.__module__):
                pyro.clear_param_store()
                self.addCleanup(pyro.clear_param_store)
                trace = pyro.poutine.trace(model).get_trace(
                    data, n_dimensions=2, bow_weight=1.0
                )
                loss = -trace.log_prob_sum()
                loss.backward()
                weights = pyro.param("topic_word_logits")
                self.assertEqual(weights.dtype, torch.float64)
                self.assertTrue(torch.isfinite(loss))
                self.assertTrue(torch.isfinite(weights.grad).all())
