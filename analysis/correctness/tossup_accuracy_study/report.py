"""One compact comparison of retained correctness benchmarks from saved scores."""
from pathlib import Path

import pandas as pd

from analysis.correctness.tossup_accuracy_study.run import OUTPUT
from analysis.correctness.bayesian_mark_study.run import OUTPUT as BAYES_OUTPUT


def main():
    tree = pd.read_csv(OUTPUT/'summary.csv')
    bayes = pd.read_csv(BAYES_OUTPUT/'metrics.csv')
    retained = [
        (tree, 'saved_compirt', 'DD-Bernstein reference'),
        (tree, 'regularized', 'Regularized question spline'),
        (tree, 'frozen_skills', 'Spline + frozen timing skills'),
        (tree, 'boosting', 'Boosted trees'),
        (tree, 'boosting_ensemble', 'Tree/spline ensemble'),
        (bayes, 'vb_base', 'Variational Bayes'),
        (bayes, 'predictive_mixture', 'Bayesian/prefix mixture'),
    ]
    lines = ['| Model | Log loss ↓ | Incorrect-buzz AP ↑ | Accuracy at 0.5 |',
             '| --- | ---: | ---: | ---: |']
    for frame, family, label in retained:
        row, = frame[frame.family.eq(family) & frame.policy.eq('default')].to_dict('records')
        lines.append(f"| {label} | {row['log_loss']:.5f} | {row['neg_ap']:.5f} | {row['accuracy']:.2%} |")
    report = '''# Correctness benchmarks: diminishing returns with the current inputs

Tree and Bayesian alternatives improve conditional first-buzz correctness
prediction, but the tested methods deliver modest accuracy gains and have not
reached the target of 60% incorrect-buzz precision at 50% recall. This is an empirical
performance frontier for the tested models and features, **not a demonstrated
upper bound on achievable accuracy**. A true optimum could still be higher.

All comparisons use the same 45,995 scored first buzzes in five whole-game folds.
The incorrect class includes zero-point incorrect attempts; majority-class
accuracy is 76.70%. Predictions condition on the observed buzzer and position.

'''+ '\n'.join(lines)+'''

The tree/spline ensemble is the strongest tested predictor by log loss and
incorrect-buzz average precision (AP). Bayesian fitting adds useful probability
prediction evidence: the Bayesian/prefix mixture improves log loss over frozen
skills by 0.01197, but its AP gain of 0.00139 has a paired game-bootstrap 95%
interval spanning zero (−0.00130 to +0.00398). Posterior averaging alone accounts
for only about 0.00064 of log-loss improvement in the base variational fit;
fitting and pooling also change. This is approximate empirical Bayes with a
diagonal variational coefficient posterior, not full Bayesian inference.

Accuracy depends on the decision policy. With thresholds chosen inside training
validation to target at least 60% incorrect-buzz precision, the tree ensemble
achieves 79.20% outer accuracy, 61.60% precision, and 28.53% recall. With validation
F1 maximized subject to at least 77% validation accuracy, it achieves 77.75%
outer accuracy and 48.13% F1. These are different operating points. The desired
60% precision/50% recall combination (about 80.6% accuracy and 54.5% F1 at this
prevalence) remains unmet; 79.2% is not an estimated maximum possible accuracy.

The retained experiment sequence is:

1. Regularized question splines and frozen timing skills: a compact comparator
   and the check of whether timing-derived skill adds correctness information.
2. Boosted trees and their fixed 50:50 spline ensemble: the flexible predictive
   benchmark and its component check.
3. Base variational Bayes and the Bayesian/prefix mixture: probabilistic fitting
   and complementary lexical information. Whole-prefix fitting remains only
   because the mixture needs it.

Other candidates tried during development (additive/context sweeps, neural
heads and interactions, extra player position effects, subcategory pooling,
recent-prefix variants, three-outcome fitting, Bayesian player slopes, and
player–prefix expertise) are not reported; their fit records remain under the
same result directories. The retained models still select from their original
inner candidate grids, so their settings are tuned, not prespecified.

These repeatedly used development folds cannot establish a population ceiling
or an untouched test result. These correctness scores alone do not establish
timing, full-game, unseen-question, or future-season performance. The archived
[frozen-skills timing evaluation](../archive/docs/frozen-skills.md#evaluation-and-results)
compares the saved timing checkpoints with DD-Bernstein on the same rosters;
it improves position MAE and first-buzzer accuracy in all five folds. The
[model guide](../archive/docs/frozen-skills.md) documents its likelihood, training and artifacts.
The defensible correctness takeaway is
**diminishing returns among the tested predictors with the recorded inputs**.

Run order and commands are in
[`analysis/correctness/README.md`](../analysis/correctness/README.md#running-them);
`tossup_accuracy_study.run` requires CUDA and `boosting` requires CatBoost.
Runners resume completed fold artifacts, and
`analysis.correctness.tossup_accuracy_study.report` regenerates this page from
the saved summaries.

Evidence: [tree metrics](../results/compirt/holdout/common/tossup-accuracy-study/summary.csv),
[Bayesian metrics](../results/compirt/holdout/common/bayesian-mark-study/metrics.csv),
[paired game bootstrap](../results/compirt/holdout/common/bayesian-mark-study/paired_game_bootstrap.csv),
[posterior averaging](../results/compirt/holdout/common/bayesian-mark-study/posterior_averaging.csv).
'''
    Path('docs/correctness-benchmarks.md').write_text(report)
    (OUTPUT/'REPORT.md').write_text(
        '# Correctness benchmarks\n\nSee the [consolidated comparison](../../../../../docs/correctness-benchmarks.md).\n')


if __name__ == '__main__':
    main()
