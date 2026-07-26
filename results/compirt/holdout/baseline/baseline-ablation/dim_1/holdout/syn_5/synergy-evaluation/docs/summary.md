# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_1/holdout/syn_5/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_1/holdout/syn_5`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 1 |
| synergy | steps | 2000 |
| synergy | final_loss | 86401.5 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 5 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.00834248 |
| mean_synergy_contribution | 0.0998 |
| median_synergy_contribution | 0.0230898 |
| negative_synergy_fraction | 0.437324 |
| positive_synergy_fraction | 0.538294 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.920913 |
| log_loss | 0.35895 |
| ece | 0.0231714 |
| part_accuracy | 0.839029 |
| part_accuracy_macro_team | 0.840278 |
| part_accuracy_macro_game | 0.839411 |
| part_accuracy_macro_bonus | 0.850887 |
| exact_acc | 0.577662 |
| ppb_mae | 0.512186 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.633004 |
| log_loss | 0.632639 |
| ece | 0.165846 |
| accuracy | 0.673428 |
| buzz_position_mae | 0.155906 |
| buzz_position_median_absolute_error | 0.135917 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.27013 | 0.9304 | 1.56789 | 3.35098 | 4.84343 | 5.39532 | 5.8516 | 6.52473 | 7.89358 |
| player | theta_1 | 1755 | 0.377838 | 1.00951 | -4.16731 | -1.63914 | 0.0368822 | 0.520743 | 0.963071 | 1.70476 | 2.89545 |
| player | theta_norm | 1755 | 0.842549 | 0.672063 | 3.49764e-05 | 0.0665987 | 0.355339 | 0.698574 | 1.14449 | 2.11422 | 4.16731 |
| tossup | beta | 1350 | 3.19965 | 0.883852 | -0.260797 | 1.72431 | 2.65742 | 3.23739 | 3.77603 | 4.56959 | 5.83159 |
| tossup | gamma | 1350 | 62.4725 | 183.226 | 3.49064 | 5.64867 | 8.77278 | 13.7967 | 29.9628 | 247.638 | 2311.77 |
| tossup | mu | 1350 | 0.590817 | 0.154717 | 0.069152 | 0.342139 | 0.488981 | 0.587218 | 0.696464 | 0.848644 | 0.989239 |
| tossup | alpha_1 | 1350 | 1.37178 | 0.727057 | -0.856994 | 0.313808 | 0.921303 | 1.31047 | 1.79205 | 2.55613 | 5.09451 |
| tossup | alpha_norm | 1350 | 1.3848 | 0.701932 | 0.00709622 | 0.356251 | 0.921303 | 1.31047 | 1.79205 | 2.55613 | 5.09451 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.269976 | 1.37752 | -2.91279 | -1.86555 | -0.851224 | 0.253508 | 1.39033 | 2.41489 | 3.84262 |
| bonus_part | alpha_1 | 4716 | 0.259468 | 0.800023 | -1.86334 | -0.895854 | -0.276548 | 0.0510635 | 0.810545 | 1.69882 | 2.44308 |
| bonus_part | alpha_norm | 4716 | 0.638164 | 0.547755 | 2.25871e-05 | 0.0338378 | 0.184779 | 0.463922 | 0.990838 | 1.70048 | 2.44308 |
