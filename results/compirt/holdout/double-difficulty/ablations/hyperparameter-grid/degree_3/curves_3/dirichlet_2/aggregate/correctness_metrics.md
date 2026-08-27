# dirichlet_2 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.806297 | 0.762779 | 0.043519 |
| auc | 0.812360 | 0.711337 | 0.101023 |
| log loss | 0.430862 | 0.509428 | 0.078566 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.806299 | 0.762799 |
| Neg F1 | 0.498207 | 0.400738 |
| Lift over all-correct | 0.038964 | -0.004192 |
| Joint event LL | 6.148097 | 6.495917 |
| Correctness LL | 0.430863 | 0.509441 |
| AUC | 0.812355 | 0.711382 |
| ECE | 0.057210 | 0.072503 |
| Position MAE | 0.130552 | 0.138891 |
| First-buzzer top-1 | 0.433970 | 0.380824 |
| No-buzz error | 0.045654 | 0.045312 |
| Predicted final-decile mass | 0.130964 | 0.129172 |

Training folds included: 5. Held-out folds included: 5.
