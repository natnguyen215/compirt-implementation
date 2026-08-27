# perceived-logit-bernstein-332 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.767945 | 0.766496 | 0.001449 |
| auc | 0.622792 | 0.548630 | 0.074162 |
| log loss | 0.562988 | 0.608005 | 0.045018 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.767944 | 0.766490 |
| Neg F1 | 0.019759 | 0.016726 |
| Lift over all-correct | 0.000609 | -0.000501 |
| Joint event LL | 7.589886 | 7.777616 |
| Correctness LL | 0.562989 | 0.608011 |
| AUC | 0.622808 | 0.548631 |
| ECE | 0.089990 | 0.105813 |
| Position MAE | 0.340038 | 0.341802 |
| First-buzzer top-1 | 0.400857 | 0.351546 |
| No-buzz error | 0.222538 | 0.222829 |
| Predicted final-decile mass | 0.029189 | 0.028632 |

Training folds included: 5. Held-out folds included: 5.
