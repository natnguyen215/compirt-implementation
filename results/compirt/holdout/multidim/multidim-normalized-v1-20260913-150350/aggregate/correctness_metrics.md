# multidim-normalized-v1-20260913-150350 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.707591 | 0.627894 | 0.079697 |
| auc | 0.705589 | 0.632324 | 0.073265 |
| log loss | 0.587079 | 0.808778 | 0.221698 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.707590 | 0.627938 |
| Neg F1 | 0.447868 | 0.400111 |
| Lift over all-correct | -0.059745 | -0.139052 |
| Joint event LL | 6.108323 | 6.794198 |
| Correctness LL | 0.587081 | 0.808652 |
| AUC | 0.705580 | 0.632324 |
| ECE | 0.144656 | 0.219480 |
| Position MAE | 0.134213 | 0.145472 |
| First-buzzer top-1 | 0.489502 | 0.396492 |
| No-buzz error | 0.047104 | 0.047814 |
| Predicted final-decile mass | 0.092718 | 0.091424 |

## Downstream tossup, game, and leaderboard metrics

All score-derived metrics use token-by-token tossup replay at 0.5 buzz and correctness thresholds, including opponent continuations and zero-point terminal misses. Targets use literal recorded tossup values.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Replayed first-player accuracy | 0.012569 | 0.010102 |
| Team-buzzed-first accuracy | 0.013685 | 0.012016 |
| Tossup scoring-player accuracy | 0.095566 | 0.092546 |
| Tossup scoring-team accuracy | 0.096569 | 0.094304 |
| Tossup-only game winner accuracy | 0.157333 | 0.159336 |
| Official game winner accuracy (tossup-only forecast) |  | 0.159865 |
| Average tossup margin error | 55.541796 | 55.824912 |
| Zero-margin baseline MAE | 56.942571 | 57.163869 |
| Tournament PPG rank correlation | 0.332237 | 0.362248 |
| Average tournament PPG error | 22.212685 | 22.194198 |
| Tournament top-10 overlap | 0.371724 | 0.417241 |
| Random top-10 overlap | 0.221254 | 0.231105 |
| Chance-adjusted top-10 overlap | 0.184261 | 0.240994 |

Training folds included: 5. Held-out folds included: 5.
