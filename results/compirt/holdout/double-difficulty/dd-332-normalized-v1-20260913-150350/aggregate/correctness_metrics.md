# dd-332-normalized-v1-20260913-150350 correctness summary

These are pooled correctness metrics for rows with an observed buzz. In-sample rows come from each fold's training fit; the same underlying observation can therefore appear in multiple cross-validation fits.

| metric | in-sample | held-out | generalization gap |
| --- | ---: | ---: | ---: |
| accuracy | 0.797495 | 0.779346 | 0.018149 |
| auc | 0.813806 | 0.715367 | 0.098439 |
| log loss | 0.435329 | 0.487786 | 0.052457 |

For all three rows, a positive generalization gap means held-out performance is worse.

| sample | observed buzzes |
| --- | ---: |
| in-sample | 193575 |
| held-out | 45995 |

## Research Log main-table metrics

Both samples use unweighted means of their fold-level metrics, matching the convention used by the Research Log main table.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Accuracy | 0.797494 | 0.779339 |
| Neg F1 | 0.302785 | 0.231764 |
| Lift over all-correct | 0.030159 | 0.012348 |
| Joint event LL | 6.403326 | 6.602221 |
| Correctness LL | 0.435331 | 0.487816 |
| AUC | 0.813807 | 0.715403 |
| ECE | 0.054723 | 0.012243 |
| Position MAE | 0.148817 | 0.154426 |
| First-buzzer top-1 | 0.395646 | 0.353304 |
| No-buzz error | 0.016584 | 0.017371 |
| Predicted final-decile mass | 0.177586 | 0.175031 |

## Downstream tossup, game, and leaderboard metrics

All score-derived metrics use token-by-token tossup replay at 0.5 buzz and correctness thresholds, including opponent continuations and zero-point terminal misses. Targets use literal recorded tossup values.

| metric | in-sample fold mean | held-out fold mean |
| --- | ---: | ---: |
| Replayed first-player accuracy | 0.193541 | 0.176695 |
| Team-buzzed-first accuracy | 0.419343 | 0.410160 |
| Tossup scoring-player accuracy | 0.223360 | 0.206919 |
| Tossup scoring-team accuracy | 0.401273 | 0.390359 |
| Tossup-only game winner accuracy | 0.659481 | 0.655695 |
| Official game winner accuracy (tossup-only forecast) | 0.674655 | 0.669554 |
| Average tossup margin error | 47.049236 | 48.382699 |
| Zero-margin baseline MAE | 56.959684 | 57.163869 |
| Tournament PPG rank correlation | 0.795212 | 0.811712 |
| Average tournament PPG error | 8.216237 | 8.000703 |
| Tournament top-10 overlap | 0.735172 | 0.724138 |
| Random top-10 overlap | 0.221254 | 0.231105 |
| Chance-adjusted top-10 overlap | 0.664922 | 0.644271 |

Training folds included: 5. Held-out folds included: 5.
