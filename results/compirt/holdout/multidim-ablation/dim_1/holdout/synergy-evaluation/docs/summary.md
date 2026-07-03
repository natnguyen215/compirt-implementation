# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim-ablation/dim_1/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/multidim-ablation/dim_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 477137 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 1 |
| synergy | steps | 2000 |
| synergy | final_loss | 84184.3 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.00674849 |
| mean_synergy_contribution | 0.192247 |
| median_synergy_contribution | 0.0460635 |
| negative_synergy_fraction | 0.398832 |
| positive_synergy_fraction | 0.578192 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.919709 |
| log_loss | 0.36315 |
| ece | 0.0270955 |
| part_accuracy | 0.837833 |
| exact_score_accuracy | 0.574685 |
| rounded_score_accuracy | 0.580342 |
| per_bonus_points_mae | 5.01929 |
| ppb_mae | 1.71389 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.633531 |
| log_loss | 0.634516 |
| ece | 0.158579 |
| buzz_position_mae | 0.146475 |
| buzz_position_median_absolute_error | 0.123962 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1791 | 5.23765 | 1.1618 | 1.32453 | 2.38529 | 4.85744 | 5.42734 | 5.91911 | 6.69923 | 8.01645 |
| player | theta_1 | 1791 | 0.309658 | 0.761101 | -3.04979 | -1.3466 | 0.165209 | 0.458217 | 0.725402 | 1.14049 | 1.73361 |
| player | theta_norm | 1791 | 0.650861 | 0.501357 | 0.0025315 | 0.0835067 | 0.324105 | 0.552538 | 0.834211 | 1.56322 | 3.04979 |
| tossup | beta_1 | 1350 | 1.79297 | 0.488623 | 0.0893143 | 0.968135 | 1.43255 | 1.80578 | 2.15522 | 2.54619 | 3.20308 |
| tossup | gamma_1 | 1350 | 26.2687 | 123.438 | 1.5658 | 2.99987 | 4.75357 | 6.71534 | 10.9743 | 62.8726 | 2066.87 |
| tossup | mu_1 | 1350 | 0.579116 | 0.166539 | 0.101 | 0.29762 | 0.472899 | 0.579266 | 0.694931 | 0.857893 | 0.986125 |
| tossup | alpha_1 | 1350 | 3.13492 | 1.35986 | 0.392457 | 1.47127 | 2.1892 | 2.88629 | 3.81345 | 5.84525 | 9.03193 |
| tossup | alpha_norm | 1350 | 3.13492 | 1.35986 | 0.392457 | 1.47127 | 2.1892 | 2.88629 | 3.81345 | 5.84525 | 9.03193 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.202286 | 1.44025 | -3.12454 | -2.10002 | -1.00526 | 0.247831 | 1.3867 | 2.42718 | 3.925 |
| bonus_part | alpha_1 | 4716 | 0.186379 | 0.782792 | -2.10862 | -1.04932 | -0.309709 | 0.0683469 | 0.678098 | 1.58181 | 2.50188 |
| bonus_part | alpha_norm | 4716 | 0.615358 | 0.518423 | 0.000166855 | 0.0367728 | 0.180525 | 0.44618 | 0.999527 | 1.58375 | 2.50188 |
