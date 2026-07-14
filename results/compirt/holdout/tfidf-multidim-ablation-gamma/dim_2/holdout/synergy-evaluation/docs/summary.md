# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_2/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_2`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 466337 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 2 |
| synergy | steps | 2000 |
| synergy | final_loss | 81927.9 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.0246346 |
| mean_synergy_contribution | -0.282062 |
| median_synergy_contribution | -0.198287 |
| negative_synergy_fraction | 0.681179 |
| positive_synergy_fraction | 0.294439 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.921699 |
| log_loss | 0.362374 |
| ece | 0.0346045 |
| part_accuracy | 0.840694 |
| exact_acc | 0.580822 |
| per_bonus_points_mae | 4.9709 |
| ppb_mae | 1.72216 |
| accuracy | 0.840694 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.647541 |
| log_loss | 0.623918 |
| ece | 0.153126 |
| accuracy | 0.687417 |
| buzz_position_mae | 0.140238 |
| buzz_position_median_absolute_error | 0.118657 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.11829 | 0.979205 | 1.24519 | 3.14342 | 4.6799 | 5.24659 | 5.73164 | 6.48149 | 7.70591 |
| player | theta_1 | 1755 | 0.0337196 | 0.562081 | -1.98834 | -0.997943 | -0.255026 | 0.0681597 | 0.386473 | 0.878262 | 1.82836 |
| player | theta_2 | 1755 | 0.0552562 | 0.582477 | -1.92594 | -1.1125 | -0.224444 | 0.127332 | 0.453153 | 0.855335 | 1.53228 |
| player | theta_norm | 1755 | 0.681813 | 0.440765 | 0.010928 | 0.143176 | 0.368112 | 0.594398 | 0.892448 | 1.52023 | 2.59654 |
| tossup | beta_1 | 1350 | 1.07114 | 0.634981 | -1.2668 | 0.153851 | 0.51733 | 1.08755 | 1.53846 | 2.11856 | 3.13764 |
| tossup | beta_2 | 1350 | 1.16751 | 0.623637 | -1.1274 | 0.226788 | 0.691651 | 1.19557 | 1.62942 | 2.1578 | 3.28525 |
| tossup | gamma_1 | 1350 | 33.9893 | 141.168 | 0.306799 | 1.81393 | 3.7983 | 5.04317 | 8.97925 | 111.735 | 2200.95 |
| tossup | gamma_2 | 1350 | 35.215 | 149.145 | 0.325968 | 1.54471 | 3.855 | 5.30047 | 10.6231 | 126.278 | 2453.96 |
| tossup | mu_1 | 1350 | 0.558762 | 0.163627 | 0.0709464 | 0.329643 | 0.445787 | 0.530525 | 0.666313 | 0.857242 | 0.993952 |
| tossup | mu_2 | 1350 | 0.563177 | 0.160374 | 0.110617 | 0.320917 | 0.447194 | 0.549418 | 0.670934 | 0.851178 | 0.993169 |
| tossup | r_1 | 1350 | 1.91124 | 1.16016 | 0.0749031 | 0.296961 | 0.854746 | 1.8636 | 2.75013 | 3.8565 | 6.54444 |
| tossup | r_2 | 1350 | 2.08164 | 1.08741 | 0.109094 | 0.323392 | 1.2529 | 2.16009 | 2.87546 | 3.75265 | 5.59055 |
| tossup | r_norm | 1350 | 3.06395 | 1.06096 | 0.62795 | 1.59532 | 2.35447 | 2.97142 | 3.61581 | 4.98546 | 8.60721 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.286078 | 1.50815 | -3.33386 | -2.20251 | -1.02221 | 0.430055 | 1.5436 | 2.48327 | 3.7556 |
| bonus_part | alpha_1 | 4716 | 0.868468 | 0.461778 | 0.20227 | 0.378586 | 0.535651 | 0.763308 | 1.06631 | 1.72121 | 3.86266 |
| bonus_part | alpha_2 | 4716 | 0.831972 | 0.40568 | 0.163573 | 0.386858 | 0.526526 | 0.736786 | 1.03159 | 1.58642 | 3.37582 |
| bonus_part | alpha_norm | 4716 | 1.234 | 0.549052 | 0.4535 | 0.573222 | 0.815071 | 1.12698 | 1.54658 | 2.18389 | 4.50064 |
