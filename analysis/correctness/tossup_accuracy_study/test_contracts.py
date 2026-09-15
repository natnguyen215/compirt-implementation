"""Small mathematical checks for the new likelihood and threshold policy."""
import unittest

import numpy as np
import torch

from analysis.correctness.tossup_accuracy_study.models import TimingModel
from analysis.correctness.tossup_accuracy_study.run import thresholds


class Contracts(unittest.TestCase):
    def test_race_matches_enumeration_and_normalizes(self):
        torch.manual_seed(14)
        model = TimingModel(2, 1).double()
        probabilities = []
        survival = 1.
        with torch.no_grad():
            base = torch.exp(model.theta @ model.relevance[0].softmax(-1)
                             + model.speed + model.start[0])
            for token in range(1, 5):
                rates = base*torch.exp(torch.nn.functional.softplus(model.slope[0])*token/4)
                duration = model.end.exp() if token == 4 else .25
                event = 1-torch.exp(-duration*rates.sum())
                for winner in range(2):
                    race = [torch.tensor([[0, 1]]), torch.ones((1, 2), dtype=torch.float64),
                            torch.tensor([0]), torch.tensor([float(token)], dtype=torch.float64),
                            torch.tensor([4.], dtype=torch.float64), torch.tensor([winner])]
                    probability = torch.exp(-model.event_loss(race)).item()
                    self.assertAlmostEqual(probability, float(survival*event*rates[winner]/rates.sum()), places=10)
                    probabilities.append(probability)
                survival *= float(1-event)
            race[-1] = torch.tensor([-1])
            dead = torch.exp(-model.event_loss(race)).item()
            self.assertAlmostEqual(dead, survival, places=10)
            self.assertAlmostEqual(sum(probabilities)+dead, 1., places=10)

    def test_infeasible_accuracy_policy_is_explicit(self):
        y = np.tile([0, 0, 0, 1], 100)
        selected = thresholds(y, np.full(len(y), .25))
        self.assertIsNone(selected['f1_accuracy80p6'])
        self.assertIsNone(selected['precision60'])

    def test_precision_policy_obeys_validation_constraint(self):
        y = np.r_[np.ones(100), np.zeros(300)]
        p = np.r_[np.linspace(.5, .9, 100), np.linspace(.05, .65, 300)]
        threshold = thresholds(y, p)['precision60']
        selected = p >= threshold
        self.assertGreaterEqual(selected.sum(), 50)
        self.assertGreaterEqual(y[selected].mean(), .6)


if __name__ == '__main__':
    unittest.main()
