# Frozen skills: research log extract

Archived from [`RESEARCH_LOG.md`](../../RESEARCH_LOG.md) on 2026-09-14, together
with the [`frozen_skills/`](../frozen_skills/README.md) package and its
[model guide](frozen-skills.md). Saved results remain under
[`results/compirt/holdout/frozen-skills/`](../../results/compirt/holdout/frozen-skills/).

**The original frozen-skills model improves both timing and correctness over the
saved simplex DD-Bernstein reference.** Different models lead different tasks;
frozen-skills full-game superiority has not been established.

## Evaluation conventions

The common `year_2024` population, fold protocol and metric definitions are in
the research log's [evaluation section](../../RESEARCH_LOG.md#evaluation-and-comparability).
Frozen-skills evidence adds:

| Evidence | Fitting and evaluation | Aggregation |
| --- | --- | --- |
| Frozen-skills correctness component | Candidates and thresholds selected on inner training-game validation, then refit on outer training games | Pooled held-out buzzes |
| Frozen timing comparison | Existing outer timing checkpoints and saved DD-Bernstein parameters replayed on identical held-out rosters; no retraining or selection | Pooled race events; position/identity metrics use buzzes only |

Frozen timing has its own normalized rate likelihood. Its DD comparison uses
full-grid normalized replay. The resulting saved-DD joint loss is **6.61553**,
whereas earlier research-log tables record about **6.6123–6.6124** under their
historical evaluation conventions. Keep those records separate; replay does not
constitute a repaired refit.

## Frozen skills: model and measured results

The Bayesian frozen-skills model answers the same two questions as CompIRT:
**who buzzes and when, and whether that answer is correct**. The difference is
how the two parts learn. Timing first estimates a distribution over player
skills and question parameters. Correctness then uses those estimates without
being allowed to change the timing fit.

“Frozen” therefore means **no correctness feedback into the timing posterior**.
It does not mean ignoring uncertainty or copying parameters from DD-Bernstein.
The implemented Pyro model carries timing uncertainty into correctness through
saved posterior draws.

### Tested simplification: one frozen fit and one correctness model

The essential idea is timing-first learning with no correctness feedback.
The sixteen conditional correctness posteriors are optional uncertainty
machinery. A simpler version keeps the exponential timing model,
freezes one fitted timing parameter vector, and fits one IRT-style correctness branch:

$$
P(Y_{ij}=1\mid x,\hat\phi)
=\sigma\!\left(u_i+w_j^\top\hat s_i-d_j(x)
+e_C\mathbf 1[x=1]\right),\qquad
\hat s_i=(\hat\theta_i,\hat v_i).
$$

Here d_j is one monotone cubic Bernstein difficulty curve. This replaces the
global/item spline expansion and per-item terminal effects; one shared terminal
effect remains. The matched test reuses the original MAP timing checkpoints
and fits one correctness posterior using Pyro SVI, with posterior medians for
default replay. Correctness uncertainty is conditional on the frozen timing
estimate, so this version gives up propagation of timing uncertainty. A fresh
two-stage Pyro fit remains a separate, untested extension.

**The completed five-fold test loses correctness performance.** It has about
22,400 model parameters, versus about 27,400 for original frozen. On the same
46,640 race events (45,995 buzzes), with 3,000 correctness SVI steps per fold,
learning rate 0.005 and seed 42 + fold:

| Model | Timing MAE ↓ | Correctness log loss ↓ | Correctness accuracy ↑ | Joint event log loss ↓ |
| --- | ---: | ---: | ---: | ---: |
| Saved DD-Bernstein | 0.15186 | 0.48777 | 77.95% | 6.61553 |
| Original frozen MAP | 0.14307 | 0.48117 | 78.76% | 6.37347 |
| Simplified Bernstein, fixed MAP timing | 0.14307 | 0.53296 | 76.76% | 6.42455 |

Timing predictions are identical by construction. Correctness loss is worse
than original frozen in all five folds. The joint-loss increase versus original
frozen is 0.05107, with paired game-bootstrap 95% interval [0.04659, 0.05532].
Joint loss still improves on saved DD by 0.19098.

This does not isolate Bernstein versus spline: curve constraints, features,
priors and correctness fitting all change. Final-100-step ELBO-loss slopes
range from −0.510 to +0.315; the fixed budget does not establish convergence.
The exact simplification is therefore not supported as a performance-preserving
replacement at this budget.

See the [model and run instructions](frozen-skills.md#simplified-correctness-branch),
[completed report](../../results/compirt/holdout/frozen-skills/simplified-bernstein-map-timing/REPORT.md)
and [pooled scores](../../results/compirt/holdout/frozen-skills/simplified-bernstein-map-timing/comparison.csv).
The Pyro comparisons below describe the mixture model, not this branch.

### Joint training of the original spline model

The completed matched five-fold experiment keeps the original exponential race,
spline correctness equation, feature scales and penalties. Both arms start from
the saved original fit and receive 1,000 additional full-batch Adam steps at
learning rate 0.005. The joint arm allows correctness gradients into theta and
speed. The control detaches those traits from correctness while continuing to
fit timing from timing observations. Correctness follows the moving detached
traits, so the control is not a permanently frozen timing checkpoint.

| Model | Timing MAE ↓ | Correctness log loss ↓ | Correctness accuracy ↑ | Joint event log loss ↓ |
| --- | ---: | ---: | ---: | ---: |
| Saved DD-Bernstein | 0.15186 | 0.48777 | 77.95% | 6.61553 |
| Original frozen MAP | 0.14307 | 0.48117 | 78.76% | 6.37347 |
| Matched no-feedback control | 0.14298 | 0.48117 | 78.76% | 6.37299 |
| Joint MAP fine-tuning | 0.14301 | 0.48176 | 78.66% | 6.37390 |

**Joint fine-tuning gives no performance benefit in this comparison.** Its
joint loss exceeds the matched control by 0.000913, with paired game-bootstrap
95% interval [0.000524, 0.001314]. Timing MAE increases by 0.0000314, interval
[0.0000120, 0.0000510]. These differences are small: joint training retains
almost all of the original model's measured performance, unlike the simplified
Bernstein replacement. Versus the original saved model, the joint-loss change
is +0.000430, interval [−0.0000150, 0.000889].

This is a warm-started MAP experiment, not Pyro VI or a comparison from scratch.
Both likelihoods enter with coefficient one and retain the original penalties;
the global correctness intercept remains unpenalized. Training-only feature
means and standard deviations are recomputed as traits change, with gradients
through them only in the joint arm.

See the [training equations and reproduction guide](frozen-skills.md#joint-map-fine-tuning),
[completed report](../../results/compirt/holdout/frozen-skills/joint-map-spline/REPORT.md),
[pooled scores](../../results/compirt/holdout/frozen-skills/joint-map-spline/comparison.csv)
and [paired intervals](../../results/compirt/holdout/frozen-skills/joint-map-spline/game_bootstrap.csv).

### Pyro model

The Pyro model fits a timing posterior, then one correctness posterior per
detached timing draw, and predicts by averaging paired probabilities over
draws. Its equations and priors are in the
[package README](../frozen_skills/README.md); the timing and correctness
equations it inherits are in the [model guide](frozen-skills.md). The saved
unweighted `mark_only_neg` predictor scores pooled log loss 0.47611, accuracy
78.84% and incorrect-buzz AP 50.35%.

### Pyro model: five-fold results

Both models are evaluated on **46,640 held-out race events**, including
**45,995 first buzzes**. The saved reference is DD-Bernstein **3/3/2 with simplex
relevance, learned locations and terminal intercepts**, without player
propensity—not the Gamma-relevance terminal model. Results are pooled across
folds; correctness is conditional on the observed buzzer and position.

| Timing / event metric | Saved DD-Bernstein | Frozen skills |
| --- | ---: | ---: |
| Position MAE ↓ | 0.15186 | 0.14802 |
| Position RMSE ↓ | 0.18577 | 0.18070 |
| Mean signed position error | -0.04530 | -0.04461 |
| Integrated timing Brier ↓ | 0.10170 | 0.09727 |
| Timing log loss, including no-buzz ↓ | 4.48193 | 4.38409 |
| First-buzzer accuracy ↑ | 35.16% | 39.20% |
| First-buzzer log loss ↓ | 1.67575 | 1.59332 |
| Timing + identity log loss ↓ | 6.13450 | 5.95481 |
| Joint event log loss ↓ | 6.61553 | 6.42435 |
| No-buzz Brier ↓ | 0.01323 | 0.01312 |
| Predicted no-buzz rate (1.38% observed) | 1.48% | 2.29% |

| Correctness at threshold 0.5 | Saved DD-Bernstein | Frozen skills |
| --- | ---: | ---: |
| Accuracy ↑ | 77.95% | 78.86% |
| Incorrect-buzz precision ↑ | 61.55% | 58.93% |
| Incorrect-buzz recall ↑ | 14.30% | 30.59% |
| Incorrect-buzz F1 ↑ | 23.20% | 40.27% |
| Incorrect-buzz AP ↑ | 44.93% | 50.35% |
| ROC AUC ↑ | 0.71544 | 0.74270 |
| Correctness log loss ↓ | 0.48777 | 0.47612 |

**Frozen skills improves both timing and correctness over saved DD-Bernstein.**
It reduces timing MAE by 2.53% and improves first-buzzer accuracy by 4.04
percentage points. Every metric in both tables improves in all five folds
individually, not only pooled. At a retrospective precision-60 operating point
it reaches 29.22% recall, against 15.81% for DD.

Its one clear regression is no-buzz calibration: it predicts 2.29% no-buzz
events versus 1.38% observed, a larger over-prediction than DD's 1.48%.

### Pyro model: uncertainty and interpretation

Paired game-cluster bootstrap 95% intervals (fitted predictions held fixed;
negative favors frozen skills):

| Difference | Position MAE | Integrated timing Brier | Joint event log loss |
| --- | --- | --- | --- |
| Frozen skills − saved DD | [−0.00430, −0.00339] | [−0.00472, −0.00415] | [−0.20008, −0.18272] |

The Bayesian computation is not yet a convergence result:

- **Optimization:** final-100-step timing ELBO slopes are −0.932 to −0.666;
  timing is still improving at 3,000 steps.
- **Timing draws:** eight versus sixteen draws changes expected position by
  mean absolute 0.0072–0.0090 across folds. More draws are needed to establish
  Monte Carlo precision.

These comparisons concern complete model setups. They do not isolate
exponential versus Bernstein curves, or attribute correctness gains to timing
skills alone: the correctness specification and fitting also change. An
exponential link can itself contain a Bernstein curve. The frozen model also
does not beat every historical timing result—the unconstrained DD
spline recorded 0.1359 position MAE and 0.0928 integrated Brier under its own
configuration and evaluation.

Evidence: [model and run instructions](../frozen_skills/README.md),
[comparison report](../../results/compirt/holdout/frozen-skills/pyro-cut-vi/REPORT.md),
[pooled scores](../../results/compirt/holdout/frozen-skills/pyro-cut-vi/comparison.csv),
[fold scores](../../results/compirt/holdout/frozen-skills/pyro-cut-vi/fold_metrics.csv)
and [bootstrap](../../results/compirt/holdout/frozen-skills/pyro-cut-vi/game_bootstrap.csv).

## Open follow-ups

1. Extend frozen timing optimization and increase timing posterior draws to
   assess convergence before interpreting small timing differences.
   Compare a normalized-likelihood DD refit with frozen timing on the same
   folds, multiple seeds and explicit optimization budgets. Separate curve
   shape, normalized exposure, and frozen/shared skill coupling in matched arms
   before attributing gains to exponential rates.
2. Validate frozen skills on an independent season or nested outer test,
   measuring timing, identity, correctness and joint event scores.
3. Evaluate frozen skills on scorer, game and leaderboard targets using the same
   token-threshold policy and complete-game coverage as the historical fits
   before making downstream claims.
