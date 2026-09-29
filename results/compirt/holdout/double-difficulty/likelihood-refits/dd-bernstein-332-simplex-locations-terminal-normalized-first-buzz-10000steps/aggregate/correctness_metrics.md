# likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-10000steps correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.802474 | 0.778432 | 0.024042 |
| auc | 0.823850 | 0.713085 | 0.110765 |
| log loss | 0.426950 | 0.488914 | 0.061964 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.802475 | 0.778426 |
| Neg F1 | 0.341414 | 0.254399 |
| Lift over all-correct | 0.035139 | 0.011436 |
| Joint event LL | 6.212128 | 6.449967 |
| Correctness LL | 0.426951 | 0.488939 |
| AUC | 0.823852 | 0.713174 |
| ECE | 0.054595 | 0.011738 |
| Position MAE | 0.135585 | 0.141821 |
| First-buzzer top-1 | 0.409486 | 0.367977 |
| No-buzz error | 0.007714 | 0.008163 |
| Predicted final-decile mass | 0.175246 | 0.173581 |

## Downstream tossup, game, and leaderboard metrics

All score-derived metrics use token-by-token tossup replay at 0.5 buzz and correctness thresholds, including opponent continuations and zero-point terminal misses. Targets use literal recorded tossup values.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Replayed first-player accuracy | 0.238198 | 0.219334 |
| Team-buzzed-first accuracy | 0.488837 | 0.479326 |
| Tossup scoring-player accuracy | 0.257999 | 0.238175 |
| Tossup scoring-team accuracy | 0.458220 | 0.445159 |
| Tossup-only game winner accuracy | 0.701887 | 0.685679 |
| Official game winner accuracy (tossup-only forecast) | 0.723975 | 0.705504 |
| Average tossup margin error | 46.369681 | 48.515677 |
| Zero-margin baseline MAE | 56.959684 | 57.163869 |
| Tournament PPG rank correlation | 0.825202 | 0.840728 |
| Average tournament PPG error | 7.141178 | 6.791909 |
| Tournament top-10 overlap | 0.755862 | 0.772414 |
| Random top-10 overlap | 0.221254 | 0.231105 |
| Chance-adjusted top-10 overlap | 0.692973 | 0.712764 |

Training folds included: 5. Held-out folds included: 5.
