# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation-rotcheck/dim_1/rot_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation-rotcheck/dim_1/rot_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| compositional | tournament | all tournaments |
| compositional | dimensions | 1 |
| compositional | steps | 2000 |
| compositional | final_loss | 90940.6 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.52107 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.890101 |
| log_loss | 0.418293 |
| ece | 0.0254858 |
| part_accuracy | 0.804805 |
| exact_acc | 0.503077 |
| per_bonus_points_mae | 5.94602 |
| ppb_mae | 3.38364 |
| accuracy | 0.804805 |

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
| bonus_part | beta | 4716 | 0.156053 | 1.61577 | -3.31383 | -2.38104 | -1.26105 | 0.290057 | 1.50021 | 2.54282 | 3.96102 |
| bonus_part | alpha_1 | 4716 | 0.425353 | 0.239273 | 0.0849892 | 0.146878 | 0.250478 | 0.36416 | 0.543599 | 0.890576 | 1.92943 |
| bonus_part | alpha_norm | 4716 | 0.425353 | 0.239273 | 0.0849892 | 0.146878 | 0.250478 | 0.36416 | 0.543599 | 0.890576 | 1.92943 |
