# Simplified frozen-skills matched holdouts

One monotone cubic Bernstein correctness model, fitted with Pyro SVI conditional on the original MAP timing traits.
The five original whole-game partitions and timing checkpoints are fixed. All 46,640 race events and 45,995 buzzes are scored.

| Model | Timing MAE | Correctness log loss | Correctness accuracy | Joint log loss |
| --- | ---: | ---: | ---: | ---: |
| frozen_skills | 0.14307 | 0.48117 | 78.76% | 6.37347 |
| pyro_frozen_skills | 0.14802 | 0.47612 | 78.86% | 6.42435 |
| saved_compirt | 0.15186 | 0.48777 | 77.95% | 6.61553 |
| simplified_frozen_skills | 0.14307 | 0.53296 | 76.76% | 6.42455 |

Lower losses are better. Accuracy uses a fixed 0.5 threshold.

Both the curve/priors and correctness fitting method differ from original frozen MAP; this does not isolate Bernstein versus spline alone.
One AutoNormal posterior is fitted for 3,000 steps at lr 0.005, seed 42 + fold. Prediction uses posterior medians, without quadrature or timing uncertainty propagation.
This is a fixed-budget development-fold comparison, not untouched-test evidence or a convergence claim. The saved DD fit predates the likelihood repair.
Timing columns are reused exactly from the validated original MAP replay; they are not evidence for a new Pyro timing fit.
Every held-out correctness prediction is reloaded and replayed on CPU with outcomes removed. Timing hashes and game-disjointness checks are saved per fold.
game_bootstrap.csv gives paired game-cluster 95% intervals for joint-loss differences, conditional on fitted parameters; it excludes refit uncertainty and cross-game question dependence.

Reproduce (code archived under `archive/frozen_skills/`): `PYTHONPATH=archive:. .venv/bin/python -m frozen_skills.simplified`.

## Training diagnostics

| Fold | Final-100-step ELBO-loss slope | Fit and replay seconds |
| --- | ---: | ---: |
| 0 | -0.5099 | 60.3 |
| 1 | -0.0677 | 55.9 |
| 2 | 0.0924 | 56.3 |
| 3 | -0.3798 | 56.8 |
| 4 | 0.3149 | 56.6 |

A negative slope means the estimated loss is still declining at the budget limit; it does not establish convergence.
