"""Training-validation log-score mixture of Bayesian and prefix predictions.

This is a single-holdout analogue of predictive stacking, not full Bayesian
model averaging or leave-one-out stacking. No model is refitted here.
"""
import json
import numpy as np
import pandas as pd
from scipy.optimize import minimize_scalar
from sklearn.metrics import average_precision_score, log_loss
from analysis.correctness.bayesian_mark_study.run import OUTPUT
from analysis.correctness.tossup_accuracy_study.run import thresholds


def main():
    for fold in range(5):
        root = OUTPUT/f'fold_{fold}'
        a = pd.read_csv(root/'vb_base_validation.csv')
        b = pd.read_csv(root/'whole_prefix_validation.csv')
        assert np.array_equal(a.event_id, b.event_id)
        assert np.array_equal(a.neg, b.neg)
        loss = lambda weight: log_loss(a.neg, weight*a.probability+(1-weight)*b.probability)
        optimum = minimize_scalar(loss, bounds=(0, 1), method='bounded')
        weight = min([0., float(optimum.x), 1.], key=loss)
        val_p = weight*a.probability+(1-weight)*b.probability
        policies = thresholds(a.neg.to_numpy(), val_p.to_numpy())
        x = pd.read_csv(root/'vb_base.csv')
        z = pd.read_csv(root/'whole_prefix.csv')
        assert np.array_equal(x.event_id, z.event_id)
        p = weight*x.probability+(1-weight)*z.probability
        old_policies = ['default', 'accuracy', 'precision60', 'f1_accuracy77', 'f1_accuracy78', 'f1_accuracy80p6']
        x = x.drop(columns=[c for c in old_policies+['plugin_probability'] if c in x])
        x['probability'] = p
        for policy, cut in policies.items():
            if cut is not None:
                x[policy] = p >= cut
        x.to_csv(root/'predictive_mixture.csv', index=False)
        a['probability'] = val_p
        a.to_csv(root/'predictive_mixture_validation.csv', index=False)
        config = {'members': ['vb_base', 'whole_prefix'], 'vb_weight': weight,
                  'selection': 'minimum inner-validation binary log loss'}
        result = {'family': 'predictive_mixture', 'config': config, 'thresholds': policies,
                  'candidates': [{'config': config, 'validation_ap': average_precision_score(a.neg, val_p),
                                  'validation_log_loss': loss(weight)}]}
        (root/'predictive_mixture.json').write_text(json.dumps(result, indent=2)+'\n')
        print(fold, config, flush=True)


if __name__ == '__main__':
    main()
