# Pyro frozen-skills holdout comparison

Five saved whole-game folds; 46,640 race events, including 45,995 first buzzes.
The original MAP model and saved DD-Bernstein reference are unchanged.

| Metric | Saved DD-Bernstein | Original frozen MAP | Pyro frozen VI |
| --- | ---: | ---: | ---: |
| Position MAE ↓ | 0.15186 | 0.14307 | 0.14802 |
| Position RMSE ↓ | 0.18577 | 0.17670 | 0.18070 |
| Integrated timing Brier ↓ | 0.10170 | 0.09477 | 0.09727 |
| Timing log loss ↓ | 4.48193 | 4.34565 | 4.38409 |
| First-buzzer accuracy ↑ | 35.16% | 39.67% | 39.20% |
| Joint event log loss ↓ | 6.61553 | 6.37347 | 6.42435 |
| Correctness accuracy at 0.5 ↑ | 77.95% | 78.76% | 78.86% |
| Incorrect-buzz precision ↑ | 61.55% | 57.95% | 58.93% |
| Incorrect-buzz recall ↑ | 14.30% | 32.17% | 30.59% |
| Incorrect-buzz F1 ↑ | 23.20% | 41.38% | 40.27% |
| Incorrect-buzz AP ↑ | 44.93% | 50.20% | 50.35% |
| Correctness log loss ↓ | 0.48777 | 0.48117 | 0.47612 |

## Inference and comparability

Timing and correctness each use 3,000 and 3,000 full-batch SVI steps, respectively, with AutoNormal and clipped Adam (lr 0.005).
The cut-posterior approximation uses 16 fixed timing-posterior draws, each paired with its own independent conditional coefficient posterior.
Correctness never changes the timing draws. Coefficient uncertainty is integrated by 48-point Gauss-Hermite quadrature; mixture probabilities are averaged before scoring.
Conditional correctness in the main table is the joint incorrect-event mass divided by the timing/identity event mass. This weights the paired posterior components by the observed winner/time, without using the held-out correctness label.
Averaging the correctness heads without this timing conditioning gives log loss 0.47611, accuracy 78.84%, and incorrect AP 0.50352; see mark_only_correctness.json.
The timing equations, Gaussian priors and selected correctness feature scales match the original model. A proper N(0,10²) correctness-intercept prior replaces its unpenalized intercept.
The feature settings were selected by the original inner training-game validation; this run reuses them rather than conducting a new search. Only the fixed 0.5 threshold is reported. No held-out outcomes enter fitting or stopping.
This is approximate modular Bayesian inference, not a single jointly updated posterior. Finite timing draws and mean-field guides limit posterior accuracy. Its training budget and inference differ from the earlier MAP fit; this is not an isolated uncertainty-averaging ablation.
The DD reference is a saved historical fit scored through normalized full-grid replay, not a newly retrained likelihood-repair baseline.
The final-100-step timing ELBO slopes range from -0.932 to -0.666; timing is still improving at the fixed 3,000-step budget. These are budgeted fits, not a convergence or optimality claim.

## Artifacts and reproduction

comparison.csv and fold_metrics.csv hold pooled and per-fold scores. game_bootstrap.csv gives paired game-cluster 95% intervals (2,000 resamples), conditional on fixed fitted predictions and excluding cross-game question dependence.
Each fold contains split manifests, feature settings, complete timing posterior draws/quantiles, conditional correctness guide means/scales, training losses, prediction rows, and freeze/normalization checks.

The code is archived under `archive/frozen_skills/`; put `archive/` on the path:

```bash
PYTHONPATH=archive:. .venv/bin/python -m frozen_skills.train_holdout
PYTHONPATH=archive:. .venv/bin/python -m frozen_skills.report
PYTHONPATH=archive:. .venv/bin/python -m frozen_skills.verify
```

## Numerical checks

Saved-artifact replay checks 1,374 ordinary/terminal/dead examples on CPU, with correctness labels erased. All match original predictions within tolerance; see replay_checks.json.
On that verification subset, changing from eight to sixteen timing draws changes expected position by a mean absolute 0.0072–0.0090 across folds. Monte Carlo convergence is not established, and the bootstrap intervals do not include this variation.
The largest conditional-probability difference between 48- and 96-node coefficient quadrature is 9.6e-06.
