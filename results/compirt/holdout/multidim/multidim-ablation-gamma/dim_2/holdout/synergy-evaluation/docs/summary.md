# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-ablation-gamma/dim_2/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-ablation-gamma/dim_2`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 467955 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 2 |
| synergy | steps | 2000 |
| synergy | final_loss | 82729.1 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.0120782 |
| mean_synergy_contribution | -0.511676 |
| median_synergy_contribution | -0.457585 |
| negative_synergy_fraction | 0.759172 |
| positive_synergy_fraction | 0.216446 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.920564 |
| log_loss | 0.361956 |
| ece | 0.0288073 |
| part_accuracy | 0.839288 |
| part_accuracy_macro_team | 0.840863 |
| part_accuracy_macro_game | 0.839712 |
| part_accuracy_macro_bonus | 0.847008 |
| exact_acc | 0.577795 |
| ppb_mae | 0.499297 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.649373 |
| log_loss | 0.621148 |
| ece | 0.151867 |
| accuracy | 0.687834 |
| buzz_position_mae | 0.140546 |
| buzz_position_median_absolute_error | 0.118666 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.11566 | 0.995216 | 1.20283 | 3.08752 | 4.67201 | 5.24724 | 5.73368 | 6.46821 | 7.69104 |
| player | theta_1 | 1755 | 0.278401 | 0.569413 | -1.83525 | -0.779925 | -0.0131024 | 0.324011 | 0.634575 | 1.12669 | 2.06924 |
| player | theta_2 | 1755 | 0.283325 | 0.590756 | -1.80179 | -0.879397 | 0.00328185 | 0.366238 | 0.685668 | 1.08148 | 1.71975 |
| player | theta_norm | 1755 | 0.815103 | 0.407827 | 0.0163291 | 0.249078 | 0.518863 | 0.762675 | 1.05964 | 1.56805 | 2.39211 |
| tossup | beta_1 | 1350 | 1.20002 | 0.660385 | -0.863023 | 0.210041 | 0.600176 | 1.23597 | 1.68106 | 2.27957 | 3.16045 |
| tossup | beta_2 | 1350 | 1.35266 | 0.650101 | -0.122346 | 0.266794 | 0.88537 | 1.39276 | 1.84324 | 2.34726 | 3.01342 |
| tossup | gamma_1 | 1350 | 26.7367 | 116.17 | 0.472612 | 2.31779 | 4.15216 | 5.267 | 8.73786 | 84.1599 | 1893.55 |
| tossup | gamma_2 | 1350 | 30.7551 | 127.965 | 0.477133 | 2.46245 | 4.27287 | 5.63283 | 10.4555 | 104.127 | 2299.97 |
| tossup | mu_1 | 1350 | 0.548897 | 0.15201 | 0.125416 | 0.322891 | 0.448911 | 0.520764 | 0.650132 | 0.81434 | 0.989758 |
| tossup | mu_2 | 1350 | 0.555974 | 0.15707 | 0.108152 | 0.310697 | 0.448323 | 0.542135 | 0.660558 | 0.828021 | 0.9939 |
| tossup | r_1 | 1350 | 1.86787 | 1.15447 | 0.072462 | 0.268261 | 0.834023 | 1.84015 | 2.70007 | 3.79414 | 6.64742 |
| tossup | r_2 | 1350 | 2.11846 | 1.10926 | 0.103791 | 0.312877 | 1.28198 | 2.22909 | 2.90724 | 3.81605 | 6.1459 |
| tossup | r_norm | 1350 | 3.06539 | 1.06882 | 0.608075 | 1.56656 | 2.34064 | 2.97652 | 3.64087 | 4.97243 | 9.05319 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.363106 | 1.37906 | -2.80927 | -1.82759 | -0.843341 | 0.45481 | 1.50404 | 2.40257 | 3.74793 |
| bonus_part | alpha_1 | 4716 | 0.859137 | 0.485169 | 0.179067 | 0.337655 | 0.478621 | 0.717477 | 1.13542 | 1.74498 | 4.08861 |
| bonus_part | alpha_2 | 4716 | 0.822173 | 0.444978 | 0.160888 | 0.343114 | 0.473039 | 0.6846 | 1.079 | 1.65553 | 3.72085 |
| bonus_part | alpha_norm | 4716 | 1.21967 | 0.599881 | 0.407553 | 0.506875 | 0.723241 | 1.07309 | 1.61985 | 2.29537 | 4.14827 |
