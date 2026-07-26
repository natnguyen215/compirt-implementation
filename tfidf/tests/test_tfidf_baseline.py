"""Lightweight tests for the cumulative TF-IDF pyramidal model."""

import unittest

import pandas as pd
import torch

from tfidf.tfidf_features import build_tfidf_feature_matrices

try:
    from tfidf.pyramidal_tfidf_model import (
        correctness_logit,
        hazard_logit,
    )
except ModuleNotFoundError as error:
    if error.name != "pyro":
        raise
    correctness_logit = hazard_logit = None


class TfidfFeatureTests(unittest.TestCase):
    def test_tfidf_prefix_matrix_aligns_and_normalizes(self):
        tossups = pd.DataFrame(
            {
                "tossup_id": ["q1", "q2"],
                "tokens": [["rare", "common", "rare"], ["common", "term"]],
            }
        )
        prefix, summary = build_tfidf_feature_matrices(
            tossups, ["q2", "q1"], max_length=4
        )

        # idf(w) = log((1 + N) / (1 + df(w))); no +1 floor. "common" appears in
        # both docs (df == N), so its idf is log(1) == 0.
        self.assertEqual(tuple(prefix.shape), (2, 4))
        self.assertAlmostEqual(float(prefix[0, 1]), 1.0)
        self.assertAlmostEqual(float(prefix[1, 2]), 1.0)
        self.assertTrue(torch.all(prefix[:, 1:] >= prefix[:, :-1]))
        self.assertEqual(summary["token_weighting"], "tf-idf")
        self.assertEqual(summary["tossups"], 2)

    def test_ubiquitous_words_zero_out_and_flatten_the_reveal(self):
        tossups = pd.DataFrame(
            {
                "tossup_id": ["q1", "q2"],
                "tokens": [["rare", "common", "rare"], ["common", "term"]],
            }
        )
        prefix, summary = build_tfidf_feature_matrices(
            tossups, ["q1", "q2"], max_length=4
        )

        # Ubiquitous "common" (df == n_documents) collapses to zero mass.
        # The normalized reveal stays flat across the zero-mass common token.
        self.assertAlmostEqual(float(prefix[0, 0]), 0.5)
        self.assertAlmostEqual(float(prefix[0, 1]), 0.5)
        self.assertAlmostEqual(float(prefix[0, 2]), 1.0)
        self.assertEqual(summary["token_weighting"], "tf-idf")


class TfidfFormulaTests(unittest.TestCase):
    def setUp(self):
        if correctness_logit is None:
            self.skipTest("pyro is not installed in this environment")
        self.theta = torch.zeros((1, 1))
        self.alpha = torch.zeros((1, 1))
        self.beta = torch.tensor([2.0])
        self.gamma = torch.tensor([10.0])
        self.mu = torch.tensor([0.5])
        self.t = torch.tensor([1.0])
        self.T = torch.tensor([4.0])

    def test_cumulative_difficulty_raises_correctness_and_hazard(self):
        beta = torch.zeros(1)
        effect = torch.tensor(2.0)

        early = correctness_logit(
            self.theta,
            self.alpha,
            beta,
            self.gamma,
            self.mu,
            self.t,
            self.T,
            torch.tensor([0.25]),
            effect,
        )
        late = correctness_logit(
            self.theta,
            self.alpha,
            beta,
            self.gamma,
            self.mu,
            self.t,
            self.T,
            torch.tensor([0.75]),
            effect,
        )
        hazard = hazard_logit(
            self.theta,
            self.alpha,
            beta,
            self.gamma,
            self.mu,
            torch.tensor([0.25]),
            self.t,
            self.T,
            torch.tensor([0.75]),
            effect,
        )

        self.assertAlmostEqual(float(early), 0.5)
        self.assertAlmostEqual(float(late), 1.5)
        self.assertAlmostEqual(float(hazard), 1.25)

if __name__ == "__main__":
    unittest.main()
