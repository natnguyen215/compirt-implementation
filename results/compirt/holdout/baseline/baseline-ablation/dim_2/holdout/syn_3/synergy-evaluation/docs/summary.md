# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_2/holdout/syn_3/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_2/holdout/syn_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 2 |
| synergy | steps | 2000 |
| synergy | final_loss | 83915.9 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.172658 |
| mean_synergy_contribution | -0.160915 |
| median_synergy_contribution | -0.0652479 |
| negative_synergy_fraction | 0.566447 |
| positive_synergy_fraction | 0.409171 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.926419 |
| log_loss | 0.349293 |
| ece | 0.0287269 |
| part_accuracy | 0.844813 |
| part_accuracy_macro_team | 0.846498 |
| part_accuracy_macro_game | 0.845287 |
| part_accuracy_macro_bonus | 0.856101 |
| exact_acc | 0.590978 |
| ppb_mae | 0.542678 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.646583 |
| log_loss | 0.6231 |
| ece | 0.159369 |
| accuracy | 0.677947 |
| buzz_position_mae | 0.152097 |
| buzz_position_median_absolute_error | 0.133087 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.19161 | 0.902728 | 1.60359 | 3.31873 | 4.76706 | 5.31464 | 5.76192 | 6.43912 | 7.75525 |
| player | theta_1 | 1755 | -0.0220725 | 0.627349 | -2.33078 | -1.07694 | -0.397794 | -0.00945902 | 0.371319 | 1.01589 | 2.02438 |
| player | theta_2 | 1755 | 0.302642 | 1.01076 | -4.06236 | -1.68617 | -0.0941787 | 0.451406 | 0.923831 | 1.64746 | 2.76475 |
| player | theta_norm | 1755 | 1.05569 | 0.626274 | 0.0161641 | 0.270883 | 0.616267 | 0.9434 | 1.36832 | 2.16747 | 4.09201 |
| tossup | beta | 1350 | 3.22932 | 0.810488 | -0.180627 | 1.78408 | 2.78803 | 3.28561 | 3.75554 | 4.42239 | 5.58873 |
| tossup | gamma | 1350 | 62.353 | 187.398 | 3.53177 | 5.79222 | 8.74982 | 13.3814 | 29.5267 | 280.174 | 2170.95 |
| tossup | mu | 1350 | 0.59123 | 0.146716 | 0.0692394 | 0.34643 | 0.495513 | 0.590603 | 0.687654 | 0.837275 | 0.988427 |
| tossup | alpha_1 | 1350 | -0.05952 | 0.738911 | -2.55373 | -1.46926 | -0.474516 | 0.00757134 | 0.453044 | 1.03443 | 1.78442 |
| tossup | alpha_2 | 1350 | 1.2908 | 0.709052 | -1.02507 | 0.236286 | 0.854295 | 1.22103 | 1.67787 | 2.46248 | 4.34146 |
| tossup | alpha_norm | 1350 | 1.52436 | 0.627934 | 0.0804245 | 0.640398 | 1.08583 | 1.45005 | 1.90733 | 2.61956 | 4.42768 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.276071 | 1.39881 | -3.14125 | -2.02177 | -0.877586 | 0.342002 | 1.42638 | 2.42583 | 3.80836 |
| bonus_part | alpha_1 | 4716 | -0.0124073 | 0.512553 | -2.5053 | -0.964815 | -0.21118 | 0.00660915 | 0.25561 | 0.751312 | 1.99054 |
| bonus_part | alpha_2 | 4716 | 0.224391 | 0.780162 | -1.98823 | -1.01418 | -0.289167 | 0.0948365 | 0.743729 | 1.62996 | 2.58663 |
| bonus_part | alpha_norm | 4716 | 0.79951 | 0.531533 | 0.00431882 | 0.135792 | 0.341425 | 0.68631 | 1.19509 | 1.75137 | 2.63796 |
