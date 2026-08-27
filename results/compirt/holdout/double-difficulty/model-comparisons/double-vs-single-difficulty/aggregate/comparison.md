# Frozen matrix-infill double-difficulty results

Current as of 2026-07-29. This report evaluates held-out games by replaying
player and tossup parameters fit on the other four folds. No held-out outcomes
are used to refit either players or questions. All models use five dimensions,
five whole-game folds, split seed 42, and optimization seed 42.

## Decision summary

The frozen results favor **double Bernstein overall**, but they also expose a
shared incidence-calibration problem that prevents a clean paper claim.

- **Double Bernstein is the best correctness and neg model.** It has pooled
  correctness/neg AUROC 0.709, neg average precision 0.442, correctness log
  loss 0.528, and full marked-PMF log loss 6.514. It improves all four measures
  over the corresponding single-curve Bernstein baseline in every fold.
- **Double sigmoid is the best survival-calibration model.** It has the lowest
  integrated Brier score (0.0938), the lowest no-buzz Brier score (0.0222)
  among the double models, and less late timing bias than double Bernstein.
- **Bernstein is necessary for the late buzz tail.** Conditional final-decile
  mass rises from 9.71% for the sigmoid baseline to 11.36% for double sigmoid,
  from 14.83% for the Bernstein baseline to 16.57% for double Bernstein, and is
  17.80% in the data.
- **All four models overpredict no buzz and fail the always-correct accuracy
  baseline.** The observed no-buzz rate is 1.38%, while predictions range from
  5.87% to 6.88%. The observed correct-buzz rate is 76.70%; model accuracy
  ranges from 62.75% to 74.66%.

The strongest current choice is therefore double Bernstein if the priority is
neg discrimination and realistic late buzzes. Double sigmoid remains the
important parsimonious calibration baseline. Before a final model-selection
claim, the no-buzz level needs calibration and the comparison needs more than
one optimizer seed.

## Evaluation population and reference baselines

The five held-out folds contain 46,640 player-question events. There are 45,995
observed buzzes and 645 no-buzz events.

| Empirical reference | Value |
| --- | ---: |
| Observed any-buzz rate | 98.62% |
| Observed no-buzz rate | 1.38% |
| Observed correct-buzz rate / always-correct accuracy | 76.70% |
| Observed neg rate among buzzes | 23.30% |
| Observed final-decile mass, all events | 17.56% |
| Observed final-decile mass, conditional on a buzz | 17.80% |

The two single-curve arms are the corresponding saved training-fold baselines:
single-curve multidimensional sigmoid and single-curve degree-5 Bernstein.
They were replayed through the same current frozen scorer and evaluator as the
double models.

This makes the **test protocol and metric definitions common**, but the
baseline comparison is descriptive rather than a controlled estimate of
decoupling alone:

- the saved baselines were originally fit under the older terminal no-buzz
  convention, while the double fits include survival through the final token;
- the saved sigmoid baseline used the older unconstrained amplitude
  parameterization (254 of 31,500 saved beta values are negative), whereas the
  double sigmoid fit uses positive Gamma amplitudes; and
- the saved Bernstein baseline used learning rate 0.01, while double Bernstein
  used 0.005.

## Model complexity

| Model | Curve structure | Effective item parameters |
| --- | --- | ---: |
| Single-curve sigmoid baseline | One relevance vector and one sigmoid curve per dimension | **20** |
| Double sigmoid | Separate correctness and hazard relevance/curves | 40 |
| Single-curve Bernstein baseline | One relevance vector and one degree-5 monotone Bernstein curve | **35** |
| Double Bernstein | Separate correctness and hazard relevance/curves | 70 |

The parameter counts are per item. Double difficulty exactly doubles each
parent's item-specific relevance and curve parameters while retaining shared
player skill and confidence.

## Correctness and neg prediction

The table reports pooled predictions over all five folds. Higher is better for
AUROC, neg average precision, accuracy, and lift; lower is better for log loss,
ECE, and Brier.

| Metric | Sigmoid baseline | Double sigmoid | Bernstein baseline | Double Bernstein |
| --- | ---: | ---: | ---: | ---: |
| Correctness / neg AUROC | 0.632 | 0.675 | 0.631 | **0.709** |
| Neg average precision | 0.327 | 0.368 | 0.338 | **0.442** |
| Correctness log loss | 0.811 | 0.546 | 0.729 | **0.528** |
| ECE | 0.219 | **0.075** | 0.192 | 0.092 |
| Brier | 0.258 | 0.180 | 0.238 | **0.173** |
| Accuracy | 0.628 | 0.741 | 0.657 | **0.747** |
| Always-correct accuracy | 0.767 | 0.767 | 0.767 | 0.767 |
| Accuracy lift over always-correct | -0.139 | -0.026 | -0.110 | **-0.020** |
| Neg precision at 0.5 | 0.320 | 0.418 | 0.333 | **0.451** |
| Neg recall at 0.5 | **0.533** | 0.282 | 0.469 | 0.405 |
| Observed neg rate | 23.30% | 23.30% | 23.30% | 23.30% |
| Mean predicted neg rate | 43.69% | **29.74%** | 38.19% | 30.92% |
| Predicted minus observed neg rate | +20.39 pp | **+6.44 pp** | +14.89 pp | +7.62 pp |

Double difficulty produces large and consistent improvements over both saved
parents:

- Double sigmoid improves AUROC by 0.043, neg average precision by 0.040,
  correctness log loss by 0.264, ECE by 0.143, and accuracy by 0.114. Each
  improvement occurs in all five folds.
- Double Bernstein improves AUROC by 0.078, neg average precision by 0.104,
  correctness log loss by 0.201, ECE by 0.099, and accuracy by 0.090. Each
  improvement also occurs in all five folds.

The mean predicted neg rate is the average model probability
\(1-P(\mathrm{correct})\) over observed buzzes; it is not the fraction classified
as a neg at the 0.5 threshold. All four models overpredict neg incidence.
Double sigmoid is closest to the observed 23.30% rate, overpredicting by 6.44
percentage points, while double Bernstein overpredicts by 7.62 points.

Double Bernstein ranks negs best, while double sigmoid has the best probability
level. Nevertheless, neither double model beats the 76.70% always-correct
threshold rule. The useful result is improved probability scoring and ranking,
not a claim of superior 0.5-threshold classification.

## Full marked PMF, timing, and no buzz

The full marked PMF scores the observed combination of no buzz, or first
player, token, and correctness mark. Expected-position errors condition on a
buzz; no-buzz metrics assess event incidence separately.

| Metric | Sigmoid baseline | Double sigmoid | Bernstein baseline | Double Bernstein |
| --- | ---: | ---: | ---: | ---: |
| Full marked-PMF log loss | 6.801 | 6.528 | 6.729 | **6.514** |
| Integrated Brier score over buzz CDF | 0.0951 | **0.0938** | 0.0955 | 0.0965 |
| Expected-position MAE | 0.1454 | 0.1397 | **0.1375** | 0.1376 |
| Median absolute position error | 0.1255 | 0.1191 | **0.1126** | 0.1130 |
| Expected-position signed bias | -0.0421 | -0.0155 | +0.0084 | +0.0200 |
| Conditional buzz-decile mass MAE | 1.71 pp | 1.97 pp | **1.42 pp** | 1.89 pp |
| Observed no-buzz rate | 1.38% | 1.38% | 1.38% | 1.38% |
| Predicted no-buzz rate | **5.87%** | 5.99% | 6.17% | 6.88% |
| No-buzz calibration error | **+4.49 pp** | +4.61 pp | +4.79 pp | +5.50 pp |
| No-buzz Brier | **0.0212** | 0.0222 | 0.0247 | 0.0251 |
| Final-decile mass, all events | 9.14% | 10.68% | 13.92% | **15.43%** |
| Final-decile mass, conditional on buzz | 9.71% | 11.36% | 14.83% | **16.57%** |
| Observed conditional final-decile mass | 17.80% | 17.80% | 17.80% | 17.80% |

Buzz-decile mass MAE is the mean absolute difference between predicted and
observed conditional buzz mass across the ten question deciles. It measures
the fit of the entire timing distribution, in percentage points per decile;
it is different from expected-position MAE, which compares one conditional
expected position with the observed position for each buzzed event.

Relative to its parent, double sigmoid improves full-PMF log loss by 0.273,
integrated Brier by 0.0013, and position MAE by 0.0057 in all five folds. It
moves signed timing bias 2.66 percentage points toward zero. Its no-buzz rate,
however, is 0.12 percentage points worse.

Double Bernstein improves full-PMF log loss by 0.215 in all five folds and adds
1.51 percentage points of unconditional final-decile mass. Its integrated
Brier score worsens by 0.0010 in all five folds, its expected-position MAE is
effectively unchanged, and its predicted no-buzz rate worsens by 0.71
percentage points.

Thus double Bernstein's full-PMF win comes from substantially better
correctness/neg scoring and later conditional timing, not from better buzz
incidence. The model assigns the most probability to the late tail, but also
the most probability to no buzz. Its exact final-decile mass is closest to the
data, but the single-curve Bernstein baseline has the lowest whole-distribution
buzz-decile MAE. Double Bernstein's extra mass in decile 9 and deficits in the
middle deciles outweigh its improvement in decile 10 under that metric.

## Buzz mass by question decile

The next table differences the pooled buzz CDF on the evaluator's 10% grid and
normalizes by predicted any-buzz mass. It is a grid approximation; the exact
evaluator final-decile numbers are in the preceding table.

| Question decile | Observed | Sigmoid baseline | Double sigmoid | Bernstein baseline | Double Bernstein |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 0.22% | 2.52% | 1.94% | 1.03% | 1.42% |
| 2 | 1.78% | 2.99% | 2.68% | 1.93% | 2.19% |
| 3 | 3.62% | 4.16% | 3.73% | 3.36% | 3.26% |
| 4 | 6.59% | 6.57% | 5.62% | 5.70% | 4.99% |
| 5 | 10.70% | 10.50% | 8.79% | 8.89% | 7.58% |
| 6 | 13.26% | 14.32% | 12.74% | 12.17% | 10.75% |
| 7 | 15.40% | 17.17% | 16.90% | 15.55% | 14.83% |
| 8 | 15.98% | 17.66% | **19.24%** | 18.23% | 18.69% |
| 9 | 14.75% | 14.51% | 17.13% | **18.47%** | **19.88%** |
| 10 | **17.71%** | 9.61% | 11.24% | 14.68% | 16.41% |

| Conditional buzz-time region | Observed | Sigmoid baseline | Double sigmoid | Bernstein baseline | Double Bernstein |
| --- | ---: | ---: | ---: | ---: | ---: |
| Early, deciles 1–4 | 12.21% | 16.24% | 13.97% | 12.02% | **11.85%** |
| Middle, deciles 5–8 | 55.33% | 59.65% | 57.66% | **54.83%** | 51.86% |
| Final fifth, deciles 9–10 | 32.46% | 24.12% | 28.36% | 33.15% | 36.29% |
| Modal decile | 10 | 8 | 8 | 9 | 9 |

The sigmoid family retains a pronounced middle bias: even after decoupling,
the modal buzz is in decile 8 and final-decile mass remains short by about 6.6
percentage points. The Bernstein family shifts the mode to decile 9. Double
Bernstein is closest in the final decile, missing the grid estimate by only 1.3
points, but overshoots the whole final fifth because too much mass remains in
decile 9.

## First-buzzer identity

| Metric | Sigmoid baseline | Double sigmoid | Bernstein baseline | Double Bernstein |
| --- | ---: | ---: | ---: | ---: |
| Top-1 accuracy | 0.396 | 0.393 | **0.401** | 0.395 |
| Mean reciprocal rank | 0.602 | 0.599 | **0.604** | 0.600 |
| Conditional identity log loss | 1.611 | 1.597 | 1.594 | **1.593** |

Separating the curves does not improve first-buzzer identity. Both double
models lose roughly 0.2–0.6 percentage points of top-1 accuracy relative to
their parent. These differences are small compared with the correctness and
timing changes, but they show that the full-PMF gains do not come from better
player ordering.

## Fold stability

The key five-fold means and sample standard deviations are:

| Metric | Sigmoid baseline | Double sigmoid | Bernstein baseline | Double Bernstein |
| --- | ---: | ---: | ---: | ---: |
| AUROC | 0.632 ± 0.006 | 0.675 ± 0.005 | 0.631 ± 0.007 | **0.709 ± 0.005** |
| Correctness log loss | 0.811 ± 0.026 | 0.546 ± 0.009 | 0.729 ± 0.018 | **0.528 ± 0.007** |
| Neg average precision | 0.328 ± 0.007 | 0.369 ± 0.005 | 0.339 ± 0.006 | **0.443 ± 0.009** |
| Full-PMF log loss | 6.801 ± 0.048 | 6.528 ± 0.030 | 6.729 ± 0.040 | **6.514 ± 0.024** |
| Position MAE | 0.1454 ± 0.0004 | 0.1397 ± 0.0006 | **0.1375 ± 0.0010** | 0.1376 ± 0.0011 |
| Pooled buzz-decile mass MAE | 1.71 pp | 1.97 pp | **1.42 pp** | 1.89 pp |
| Predicted no-buzz rate | 5.87% ± 0.18 | 5.99% ± 0.22 | 6.17% ± 0.16 | 6.88% ± 0.16 |

The main parent-to-double correctness and full-PMF improvements occur in all
five folds. The folds are not independent optimization replications: every arm
still uses only seed 42.

## Recommendation

1. Retain **double Bernstein** as the primary shape/ranking candidate and
   **double sigmoid** as the parsimonious calibration comparison.
2. Fit a training-only global hazard/no-buzz intercept. All models miss the
   observed 1.38% no-buzz rate by at least 4.49 percentage points, so incidence
   calibration is the clearest shared defect.
3. Test a bias-only correctness calibration, especially for double Bernstein.
   Its AUROC and neg average precision are strongest, while ECE remains worse
   than double sigmoid.
4. Repeat the frozen five-fold study over multiple optimization seeds and
   aggregate by complete CV repetition. One seed cannot separate structural
   differences from SVI initialization noise.
5. Retrain the single-curve baselines under the same terminal-token convention,
   positive amplitude prior, learning rate, and checkpoint policy before
   attributing the parent-to-double deltas solely to curve decoupling.

## Source artifacts

- [`matrix_infill_all_models_pooled.csv`](matrix_infill_all_models_pooled.csv)
  contains pooled metrics for all four models.
- [`matrix_infill_all_models_per_fold.csv`](matrix_infill_all_models_per_fold.csv)
  contains the five fold rows for each model.
- [`matrix_infill_decile_buzz_mass.csv`](matrix_infill_decile_buzz_mass.csv)
  contains the pooled conditional decile distributions.
- Each model's `seed_42/fold_k/evaluation/csvs/` directory contains the event
  PMF, buzz CDF, correctness, timing, and identity source rows.
