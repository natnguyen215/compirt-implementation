"""Lightweight tests for the isolated TF-IDF pyramidal variants."""

import math
import unittest

import pandas as pd
import torch

from tfidf.tfidf_features import build_tfidf_feature_matrices

try:
    from tfidf.pyramidal_tfidf_model import (
        CUMULATIVE_DIFFICULTY,
        HAZARD_SPIKE,
        REPLACE_POSITION,
        correctness_logit,
        hazard_logit,
    )
except ModuleNotFoundError as error:
    if error.name != "pyro":
        raise
    correctness_logit = hazard_logit = None
    CUMULATIVE_DIFFICULTY = HAZARD_SPIKE = REPLACE_POSITION = None


class TfidfFeatureTests(unittest.TestCase):
    def test_tfidf_prefix_and_token_matrices_align_and_normalize(self):
        tossups = pd.DataFrame(
            {
                "tossup_id": ["q1", "q2"],
                "tokens": [["rare", "common", "rare"], ["common", "term"]],
            }
        )
        prefix, token, summary = build_tfidf_feature_matrices(
            tossups, ["q2", "q1"], max_length=4
        )

        # idf(w) = log((1 + N) / (1 + df(w))); no +1 floor. "common" appears in
        # both docs (df == N), so its idf is log(1) == 0.
        rare_idf = math.log(3.0 / 2.0)
        common_idf = 0.0

        # token scores are (term_frequency / doc_length) * idf.
        self.assertEqual(tuple(prefix.shape), (2, 4))
        self.assertEqual(tuple(token.shape), (2, 4))
        self.assertAlmostEqual(float(token[0, 0]), (1.0 / 2.0) * common_idf)
        self.assertAlmostEqual(float(token[0, 1]), (1.0 / 2.0) * rare_idf)
        self.assertAlmostEqual(float(token[1, 0]), (2.0 / 3.0) * rare_idf)
        self.assertAlmostEqual(float(token[1, 1]), (1.0 / 3.0) * common_idf)
        self.assertAlmostEqual(float(token[1, 2]), (2.0 / 3.0) * rare_idf)
        self.assertAlmostEqual(float(token[1, 3]), 0.0)
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
        prefix, token, summary = build_tfidf_feature_matrices(
            tossups, ["q1", "q2"], max_length=4
        )

        rare_idf = math.log(3.0 / 2.0)

        # Ubiquitous "common" (df == n_documents) collapses to zero mass.
        self.assertAlmostEqual(float(token[0, 0]), (2.0 / 3.0) * rare_idf)
        self.assertAlmostEqual(float(token[0, 1]), 0.0)
        self.assertAlmostEqual(float(token[0, 2]), (2.0 / 3.0) * rare_idf)
        # The normalized reveal stays flat across the zero-mass common token.
        self.assertAlmostEqual(float(prefix[0, 0]), 0.5)
        self.assertAlmostEqual(float(prefix[0, 1]), 0.5)
        self.assertAlmostEqual(float(prefix[0, 2]), 1.0)
        self.assertEqual(summary["token_weighting"], "tf-idf")


class TfidfVariantTests(unittest.TestCase):
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

    def test_replace_position_uses_information_axis(self):
        low_info = correctness_logit(
            self.theta,
            self.alpha,
            self.beta,
            self.gamma,
            self.mu,
            self.t,
            self.T,
            torch.tensor([0.25]),
            tfidf_variant=REPLACE_POSITION,
        )
        high_info = correctness_logit(
            self.theta,
            self.alpha,
            self.beta,
            self.gamma,
            self.mu,
            self.t,
            self.T,
            torch.tensor([0.75]),
            tfidf_variant=REPLACE_POSITION,
        )

        self.assertLess(float(low_info), float(high_info))

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
            CUMULATIVE_DIFFICULTY,
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
            CUMULATIVE_DIFFICULTY,
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
            torch.tensor([0.0]),
            effect,
            CUMULATIVE_DIFFICULTY,
        )

        self.assertAlmostEqual(float(early), 0.5)
        self.assertAlmostEqual(float(late), 1.5)
        self.assertAlmostEqual(float(hazard), 1.25)

    def test_hazard_spike_changes_hazard_not_correctness(self):
        beta = torch.zeros(1)
        effect = torch.tensor(1.5)
        prefix = torch.tensor([0.5])

        correctness_without_token = correctness_logit(
            self.theta,
            self.alpha,
            beta,
            self.gamma,
            self.mu,
            self.t,
            self.T,
            prefix,
            effect,
            HAZARD_SPIKE,
        )
        correctness_with_token = correctness_logit(
            self.theta,
            self.alpha,
            beta,
            self.gamma,
            self.mu,
            self.t,
            self.T,
            prefix,
            effect,
            HAZARD_SPIKE,
        )
        hazard_without_token = hazard_logit(
            self.theta,
            self.alpha,
            beta,
            self.gamma,
            self.mu,
            torch.tensor([0.25]),
            self.t,
            self.T,
            prefix,
            torch.tensor([0.0]),
            effect,
            HAZARD_SPIKE,
        )
        hazard_with_token = hazard_logit(
            self.theta,
            self.alpha,
            beta,
            self.gamma,
            self.mu,
            torch.tensor([0.25]),
            self.t,
            self.T,
            prefix,
            torch.tensor([2.0]),
            effect,
            HAZARD_SPIKE,
        )

        self.assertAlmostEqual(float(correctness_without_token), 0.0)
        self.assertAlmostEqual(float(correctness_with_token), 0.0)
        self.assertAlmostEqual(float(hazard_without_token), -0.25)
        self.assertAlmostEqual(float(hazard_with_token), 2.75)


if __name__ == "__main__":
    unittest.main()
