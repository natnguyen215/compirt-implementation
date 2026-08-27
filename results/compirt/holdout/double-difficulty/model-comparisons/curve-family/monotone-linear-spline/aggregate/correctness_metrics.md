# dd-monotone-linear-spline correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.687852 | 0.633938 | 0.053914 |
| auc | 0.746637 | 0.656880 | 0.089757 |
| log loss | 0.657945 | 0.836748 | 0.178803 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.687854 | 0.633953 |
| Neg F1 | 0.501362 | 0.430079 |
| Lift over all-correct | -0.079481 | -0.133037 |
| Joint event LL | 7.421016 | 8.144595 |
| Correctness LL | 0.657955 | 0.836675 |
| AUC | 0.746696 | 0.657073 |
| ECE | 0.189938 | 0.226474 |
| Position MAE | 0.141915 | 0.150999 |
| First-buzzer top-1 | 0.379718 | 0.324749 |
| No-buzz error | 0.187038 | 0.182172 |
| Predicted final-decile mass | 0.166575 | 0.163887 |

Training folds included: 5. Held-out folds included: 5.
