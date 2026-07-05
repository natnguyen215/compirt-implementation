"""Lightweight tests for the isolated TF-IDF baseline experiment."""

import unittest

import pandas as pd
import torch

from tfidf.tfidf_features import build_tfidf_prefix_matrix

try:
    from tfidf.pyramidal_tfidf_model import correctness_logit, hazard_logit
except ModuleNotFoundError as error:
    if error.name != "pyro":
        raise
    correctness_logit = hazard_logit = None


class TfidfFeatureTests(unittest.TestCase):
    def test_prefix_matrix_aligns_and_normalizes(self):
        tossups = pd.DataFrame(
            {
                "tossup_id": ["q1", "q2"],
                "tokens": [["rare", "common", "rare"], ["common", "term"]],
            }
        )
        prefix, summary = build_tfidf_prefix_matrix(
            tossups, ["q2", "q1"], max_length=4
        )

        self.assertEqual(tuple(prefix.shape), (2, 4))
        self.assertAlmostEqual(float(prefix[0, 1]), 1.0)
        self.assertAlmostEqual(float(prefix[1, 2]), 1.0)
        self.assertTrue(torch.all(prefix[:, 1:] >= prefix[:, :-1]))
        self.assertEqual(summary["tossups"], 2)

    def test_tfidf_adjustment_lowers_difficulty_and_raises_logit(self):
        if correctness_logit is None:
            self.skipTest("pyro is not installed in this environment")

        theta = torch.zeros((1, 1))
        alpha = torch.zeros((1, 1))
        beta = torch.zeros(1)
        gamma = torch.ones(1)
        mu = torch.tensor([0.5])
        t = torch.tensor([1])
        T = torch.tensor([2])
        tfidf_prefix = torch.tensor([0.5])
        tfidf_clue_effect = torch.tensor(1.0)

        logit = correctness_logit(
            theta,
            alpha,
            beta,
            gamma,
            mu,
            t,
            T,
            tfidf_prefix,
            tfidf_clue_effect,
        )
        hazard = hazard_logit(
            theta,
            alpha,
            beta,
            gamma,
            mu,
            torch.tensor([0.25]),
            t,
            T,
            tfidf_prefix,
            tfidf_clue_effect,
        )

        self.assertAlmostEqual(float(logit), 0.5)
        self.assertAlmostEqual(float(hazard), 0.25)


if __name__ == "__main__":
    unittest.main()
