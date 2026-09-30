# perceived-logit-positive-alpha-bernstein-332 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.396745 | 0.375823 | 0.020922 |
| auc | 0.628405 | 0.606415 | 0.021989 |
| log loss | 0.764627 | 0.787559 | 0.022931 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.396744 | 0.375861 |
| Neg F1 | 0.399181 | 0.392111 |
| Lift over all-correct | -0.370592 | -0.391130 |
| Joint event LL | 6.437382 | 6.758884 |
| Correctness LL | 0.764628 | 0.787527 |
| AUC | 0.628399 | 0.606510 |
| ECE | 0.334871 | 0.345781 |
| Position MAE | 0.129701 | 0.137620 |
| First-buzzer top-1 | 0.437494 | 0.391814 |
| No-buzz error | 0.036821 | 0.036482 |
| Predicted final-decile mass | 0.129145 | 0.127520 |

Training folds included: 5. Held-out folds included: 5.
