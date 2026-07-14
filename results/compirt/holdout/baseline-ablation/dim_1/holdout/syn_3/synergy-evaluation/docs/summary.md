# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_1/holdout/syn_3/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_1/holdout/syn_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 1 |
| synergy | steps | 2000 |
| synergy | final_loss | 83565.7 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.010081 |
| mean_synergy_contribution | 0.0386379 |
| median_synergy_contribution | 0.00268324 |
| negative_synergy_fraction | 0.46781 |
| positive_synergy_fraction | 0.507808 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.921033 |
| log_loss | 0.359157 |
| ece | 0.0245942 |
| part_accuracy | 0.839189 |
| exact_acc | 0.577712 |
| per_bonus_points_mae | 4.99356 |
| ppb_mae | 1.69073 |
| accuracy | 0.839189 |

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
| bonus_part | beta | 4716 | 0.23543 | 1.35887 | -2.92611 | -1.87594 | -0.864371 | 0.213945 | 1.34178 | 2.34825 | 3.74562 |
| bonus_part | alpha_1 | 4716 | 0.264995 | 0.802839 | -1.86455 | -0.896957 | -0.274103 | 0.0533721 | 0.824897 | 1.70587 | 2.45036 |
| bonus_part | alpha_norm | 4716 | 0.642027 | 0.550001 | 1.44368e-06 | 0.032631 | 0.187924 | 0.4683 | 0.993331 | 1.7083 | 2.45036 |
