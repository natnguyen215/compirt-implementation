# Frozen skills versus saved DD-Bernstein: timing and correctness

Frozen timing changes relative-position MAE from
0.15186 to
0.14307 (5.79% reduction).
Its correctness accuracy is 78.76%
versus 77.95% for saved DD-Bernstein.

Replayed all five saved outer timing checkpoints, without fitting or selection,
against the saved DD-Bernstein reference on identical held-out event rosters.
There are 46,640 events, including
45,995 observed first buzzes.

## Timing and first-buzzer results

| Metric | Saved DD-Bernstein | Frozen skills |
|---|---:|---:|
| Relative-position MAE ↓ | 0.15186 | 0.14307 |
| Relative-position RMSE ↓ | 0.18577 | 0.17670 |
| Mean signed position error (prediction − observation) | -0.04530 | -0.03306 |
| Integrated timing Brier score ↓ | 0.10170 | 0.09477 |
| Timing log loss, including no-buzz ↓ | 4.48193 | 4.34565 |
| First-buzzer accuracy ↑ | 35.16% | 39.67% |
| First-buzzer log loss ↓ | 1.67575 | 1.57509 |
| Timing + identity log loss ↓ | 6.13450 | 5.89895 |
| Timing + identity + correctness log loss ↓ | 6.61553 | 6.37347 |
| No-buzz Brier score ↓ | 0.01323 | 0.01279 |
| Predicted no-buzz rate | 1.48% | 1.63% |
| Observed no-buzz rate | 1.38% | 1.38% |

Position MAE/RMSE use E[relative position | a buzz occurs] on observed-buzz
events. A relative-position error of 0.01 is 1% of question length. First-buzzer
metrics also condition on a buzz occurring and integrate over its possible time.
The integrated Brier score uses a 21-point grid from 0 to 1, including dead
events. Timing log loss scores the exact observed token or no-buzz outcome;
race log loss additionally scores buzzer identity. The joint score additionally
uses each model's saved correctness probability at the observed player/token.
All log losses use natural logarithms; smaller is better.

## Correctness at threshold 0.5

| Metric | Saved DD-Bernstein | Frozen skills |
|---|---:|---:|
| Accuracy ↑ | 77.95% | 78.76% |
| Incorrect-buzz precision ↑ | 61.55% | 57.95% |
| Incorrect-buzz recall ↑ | 14.30% | 32.17% |
| Incorrect-buzz F1 ↑ | 23.20% | 41.38% |
| Incorrect-buzz average precision ↑ | 44.93% | 50.20% |
| ROC AUC ↑ | 0.71544 | 0.74088 |
| Correctness log loss ↓ | 0.48777 | 0.48117 |

Correctness metrics reuse the original study's saved probabilities and are
conditional on the observed buzzer and position. Their event IDs and outcomes
were checked against the timing evaluation. This is not full-game simulation.

## Verification and interpretation

- Every replayed event PMF sums to one, including no-buzz mass.
- Frozen replay likelihoods were checked independently against TimingModel.event_loss
  on initial examples and all terminal/no-buzz events (see checks.json).
- Reconstructed DD-Bernstein expected positions match its saved predictions to
  within 1e-4 (see saved_prediction_checks.json).
- The DD-Bernstein distribution uses the repository's normalized categorical
  first-buzz replay law. These scores evaluate the saved model's predictive
  distribution; they are not a claim about its historical training objective.
- Frozen-skills here means its separately fitted timing-only model paired with
  its frozen-skill correctness predictor. It does not reuse DD-Bernstein timing.
- Differences cannot isolate exponential versus Bernstein curves: fitting,
  regularization, timing/correctness coupling, and rate parameterization also differ.
- game_bootstrap.csv gives 95% paired game-cluster bootstrap intervals for
  frozen minus saved (2,000 resamples, fixed fitted models). These omit refitting,
  model-search uncertainty, and dependence across games sharing questions.

## Reproduce

```sh
.venv/bin/python -m analysis.correctness.tossup_accuracy_study.evaluate_timing
.venv/bin/python -m analysis.correctness.tossup_accuracy_study.report_timing
```

Pooled timing: summary.csv. Per-fold timing: fold_metrics.csv. Per-event scores:
fold_0_events.csv through fold_4_events.csv. Original correctness: ../summary.csv.
