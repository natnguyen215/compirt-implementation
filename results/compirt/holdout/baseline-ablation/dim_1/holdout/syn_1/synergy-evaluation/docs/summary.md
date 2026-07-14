# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_1/holdout/syn_1/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_1/holdout/syn_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 1 |
| synergy | steps | 2000 |
| synergy | final_loss | 81208.2 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.0146435 |
| mean_synergy_contribution | -0.0362061 |
| median_synergy_contribution | -0.000552292 |
| negative_synergy_fraction | 0.516178 |
| positive_synergy_fraction | 0.45944 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.921156 |
| log_loss | 0.359378 |
| ece | 0.025846 |
| part_accuracy | 0.838946 |
| exact_acc | 0.576852 |
| per_bonus_points_mae | 4.99146 |
| ppb_mae | 1.68895 |
| accuracy | 0.838946 |

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
| bonus_part | beta | 4716 | 0.19863 | 1.34009 | -2.97238 | -1.88746 | -0.878949 | 0.175082 | 1.29019 | 2.27549 | 3.61637 |
| bonus_part | alpha_1 | 4716 | 0.273429 | 0.805951 | -1.84403 | -0.890707 | -0.274638 | 0.0558964 | 0.840004 | 1.71434 | 2.46706 |
| bonus_part | alpha_norm | 4716 | 0.646889 | 0.552976 | 0.000527226 | 0.0333961 | 0.190264 | 0.473976 | 0.996988 | 1.71596 | 2.46706 |
