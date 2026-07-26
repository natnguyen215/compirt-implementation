# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_2/holdout/syn_2/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_2/holdout/syn_2`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 2 |
| synergy | steps | 2000 |
| synergy | final_loss | 82712 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 2 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.19433 |
| mean_synergy_contribution | -0.20963 |
| median_synergy_contribution | -0.108074 |
| negative_synergy_fraction | 0.593575 |
| positive_synergy_fraction | 0.382043 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.926543 |
| log_loss | 0.349404 |
| ece | 0.0296392 |
| part_accuracy | 0.845028 |
| part_accuracy_macro_team | 0.846627 |
| part_accuracy_macro_game | 0.845483 |
| part_accuracy_macro_bonus | 0.856144 |
| exact_acc | 0.591293 |
| ppb_mae | 0.53624 |

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
| bonus_part | beta | 4716 | 0.257712 | 1.39287 | -3.14854 | -2.03328 | -0.888681 | 0.324895 | 1.40417 | 2.39676 | 3.77164 |
| bonus_part | alpha_1 | 4716 | -0.0122782 | 0.512937 | -2.51181 | -0.969581 | -0.211241 | 0.00822783 | 0.255541 | 0.750612 | 1.97928 |
| bonus_part | alpha_2 | 4716 | 0.226522 | 0.780323 | -1.96675 | -1.01464 | -0.288247 | 0.0978601 | 0.745965 | 1.63351 | 2.59352 |
| bonus_part | alpha_norm | 4716 | 0.801079 | 0.530677 | 0.00797411 | 0.137359 | 0.344188 | 0.690397 | 1.19786 | 1.75663 | 2.64496 |
