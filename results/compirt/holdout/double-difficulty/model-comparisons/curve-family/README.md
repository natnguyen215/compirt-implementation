# DD linear spline vs. Bernstein 3/3/2

_The linear-spline family is archived under `archive/dd_linear_spline/`; this comparison is kept beside its runs._

This report compares two double-difficulty tossup models under the same
five-fold frozen matrix-infill holdout over `year_2024`:

- **DD linear spline:** a five-dimensional, clue-aligned unconstrained linear
  spline.
- **Bernstein 3/3/2:** a three-dimensional, degree-3 monotone Bernstein model
  with three curves/dimensions and drop concentration 2.0.

Player and question parameters were fitted on four training folds and replayed
on the held-out games without fitting any held-out outcomes. Both experiments
use game split seed 42, optimization seed 42, 3,000 training steps, no
correctness calibration, and no bouncebacks.

## Configuration

| Setting | DD linear spline | Bernstein 3/3/2 |
| --- | ---: | ---: |
| Difficulty family | Clue-aligned linear spline | Monotone Bernstein polynomial |
| Dimensions | 5 | 3 |
| Polynomial degree | N/A | 3 |
| Drop concentration | N/A | 2.0 |
| Learning rate | 0.01 | 0.005 |
| Effective parameter count | 114,520 | 43,620 |
| Median spline knots per tossup | 7 | N/A |
| Holdout protocol | Frozen matrix-infill | Frozen matrix-infill |

This is a comparison of the completed model configurations, not an isolated
curve-family ablation: dimensionality, learning rate, and parameter count also
differ.

## Five-fold aggregate results

Values are the unweighted mean and sample standard deviation across the five
matched folds. Arrows indicate the preferred direction.

| Metric | DD linear spline | Bernstein 3/3/2 | Better |
| --- | ---: | ---: | --- |
| Correctness AUC ↑ | **0.7228 ± 0.0024** | 0.7114 ± 0.0036 | Linear spline |
| Correctness log loss ↓ | 0.5651 ± 0.0074 | **0.5094 ± 0.0063** | Bernstein |
| ECE ↓ | 0.1185 ± 0.0040 | **0.0725 ± 0.0047** | Bernstein |
| Brier score ↓ | 0.1822 ± 0.0031 | **0.1661 ± 0.0024** | Bernstein |
| Accuracy ↑ | 73.45% ± 0.42% | **76.28% ± 0.54%** | Bernstein |
| All-correct accuracy ↑ | 76.70% ± 0.46% | 76.70% ± 0.46% | Same baseline |
| Lift over all-correct ↑ | -3.25 pp ± 0.35 pp | **-0.42 pp ± 0.38 pp** | Bernstein |
| Negative average precision ↑ | **0.4495 ± 0.0041** | 0.4460 ± 0.0073 | Linear spline |
| Joint tossup-event log loss ↓ | **6.4596 ± 0.0370** | 6.4959 ± 0.0226 | Linear spline |
| Integrated Brier score ↓ | **0.0928 ± 0.0011** | 0.0945 ± 0.0009 | Linear spline |
| First-buzzer top-1 accuracy ↑ | **39.74% ± 0.79%** | 38.08% ± 0.70% | Linear spline |
| First-buzzer MRR ↑ | **0.6019 ± 0.0059** | 0.5889 ± 0.0051 | Linear spline |
| First-buzzer log loss ↓ | **1.5915 ± 0.0176** | 1.6121 ± 0.0165 | Linear spline |
| No-buzz calibration error ↓ | **0.0337 ± 0.0018** | 0.0453 ± 0.0020 | Linear spline |
| Buzz-position MAE ↓ | **0.1359 ± 0.0010** | 0.1389 ± 0.0007 | Linear spline |
| Buzz-position bias | +0.0033 ± 0.0037 | **-0.0031 ± 0.0032** | Similar absolute bias |

Neither model exceeds the all-correct threshold-accuracy baseline. Bernstein
3/3/2 comes much closer, trailing it by 0.42 percentage points on average,
compared with 3.25 points for the linear spline.

## Fold-level core metrics

| Fold | Model | AUC | Correctness log loss | Accuracy | Integrated Brier | Joint event log loss |
| ---: | --- | ---: | ---: | ---: | ---: | ---: |
| 0 | Linear spline | 0.7246 | 0.5631 | 73.50% | 0.0930 | 6.4645 |
| 0 | Bernstein 3/3/2 | 0.7083 | **0.5132** | **75.50%** | 0.0948 | 6.4984 |
| 1 | Linear spline | 0.7193 | 0.5747 | 73.11% | 0.0924 | 6.4835 |
| 1 | Bernstein 3/3/2 | 0.7086 | **0.5176** | **76.15%** | 0.0940 | 6.5169 |
| 2 | Linear spline | 0.7213 | 0.5709 | 73.02% | 0.0938 | 6.4458 |
| 2 | Bernstein 3/3/2 | 0.7129 | **0.5094** | **76.15%** | 0.0957 | 6.4979 |
| 3 | Linear spline | 0.7249 | 0.5578 | 74.07% | 0.0911 | 6.4042 |
| 3 | Bernstein 3/3/2 | 0.7101 | **0.5055** | **76.80%** | 0.0934 | 6.4580 |
| 4 | Linear spline | 0.7241 | 0.5591 | 73.55% | 0.0935 | 6.4999 |
| 4 | Bernstein 3/3/2 | 0.7170 | **0.5015** | **76.81%** | 0.0945 | 6.5084 |

## Interpretation

Bernstein 3/3/2 is consistently better at assigning correctness probabilities:
it wins all five folds on correctness log loss, ECE, Brier score, and threshold
accuracy. Its accuracy remains just below the all-correct baseline, so this is
better probability estimation rather than a demonstrated threshold-accuracy
gain over that baseline.

The DD linear spline ranks correct versus incorrect buzzes better by AUC, but
its probabilities are less calibrated. It is consistently stronger on the
temporal task: it wins all five folds on integrated Brier score, joint-event
log loss, first-buzzer top-1 accuracy, first-buzzer MRR, first-buzzer log loss,
no-buzz calibration error, and buzz-position MAE.

The practical choice therefore depends on the target:

- Use **Bernstein 3/3/2** when correctness probability quality and threshold
  accuracy are primary.
- Use **DD linear spline** when buzz timing, first-buzzer identity, and no-buzz
  calibration are primary.

## Result locations

- DD linear spline:
  `results/compirt/holdout/double-difficulty/model-comparisons/curve-family/linear-spline/seed_42/`
- Bernstein 3/3/2:
  `results/compirt/holdout/double-difficulty/ablations/relevance-locations-terminal/dd-bernstein-332-unconstrained/`

Each fold's source metrics are stored under
`fold_*/evaluation/csvs/tossup_metrics.csv` (the linear-spline directory uses
`fold_0` through `fold_4`; the Bernstein directory follows the same naming).
