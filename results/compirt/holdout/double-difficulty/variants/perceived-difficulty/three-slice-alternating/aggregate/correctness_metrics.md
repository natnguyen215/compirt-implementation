# perceived-difficulty-three-slice-alternating-positive-alpha-bernstein-332 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.600749 | 0.550408 | 0.050341 |
| auc | 0.636735 | 0.593891 | 0.042844 |
| log loss | 0.687222 | 0.733729 | 0.046507 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.600751 | 0.550420 |
| Neg F1 | 0.406063 | 0.381149 |
| Lift over all-correct | -0.166584 | -0.216570 |
| Joint event LL | 6.318673 | 6.862385 |
| Correctness LL | 0.687221 | 0.733708 |
| AUC | 0.636733 | 0.593885 |
| ECE | 0.262922 | 0.282242 |
| Position MAE | 0.129636 | 0.139181 |
| First-buzzer top-1 | 0.421477 | 0.360909 |
| No-buzz error | 0.035534 | 0.035288 |
| Predicted final-decile mass | 0.140865 | 0.138012 |

Training folds included: 5. Held-out folds included: 5.
