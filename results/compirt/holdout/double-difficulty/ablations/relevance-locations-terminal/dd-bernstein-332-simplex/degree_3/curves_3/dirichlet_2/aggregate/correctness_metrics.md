# dirichlet_2 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.809893 | 0.771606 | 0.038287 |
| auc | 0.810275 | 0.711491 | 0.098784 |
| log loss | 0.444922 | 0.502545 | 0.057623 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.809894 | 0.771619 |
| Neg F1 | 0.468513 | 0.368444 |
| Lift over all-correct | 0.042558 | 0.004629 |
| Joint event LL | 6.548653 | 6.744418 |
| Correctness LL | 0.444923 | 0.502547 |
| AUC | 0.810267 | 0.711492 |
| ECE | 0.074991 | 0.067294 |
| Position MAE | 0.172284 | 0.178267 |
| First-buzzer top-1 | 0.384083 | 0.340354 |
| No-buzz error | 0.064993 | 0.064398 |
| Predicted final-decile mass | 0.096939 | 0.094827 |

Training folds included: 5. Held-out folds included: 5.
