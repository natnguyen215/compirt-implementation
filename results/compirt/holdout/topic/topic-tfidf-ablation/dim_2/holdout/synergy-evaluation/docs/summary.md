# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/topic-tfidf-ablation/dim_2/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/topic-tfidf-ablation/dim_2`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 509084 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 2 |
| synergy | steps | 2000 |
| synergy | final_loss | 103533 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.630675 |
| mean_synergy_contribution | -0.104933 |
| median_synergy_contribution | -0.00643228 |
| negative_synergy_fraction | 0.543951 |
| positive_synergy_fraction | 0.431667 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.918694 |
| log_loss | 0.370889 |
| ece | 0.0420527 |
| part_accuracy | 0.839663 |
| part_accuracy_macro_team | 0.840808 |
| part_accuracy_macro_game | 0.840047 |
| part_accuracy_macro_bonus | 0.840064 |
| exact_acc | 0.579002 |
| ppb_mae | 0.479954 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.631078 |
| log_loss | 0.607946 |
| ece | 0.147195 |
| accuracy | 0.692476 |
| buzz_position_mae | 0.148617 |
| buzz_position_median_absolute_error | 0.130701 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.46092 | 0.597036 | 2.55228 | 4.51454 | 5.08762 | 5.46297 | 5.86815 | 6.40375 | 7.43014 |
| player | theta_1 | 1755 | -1.13029 | 1.14524 | -4.02668 | -2.79962 | -2.01148 | -1.25388 | -0.372782 | 0.943169 | 2.61723 |
| player | theta_2 | 1755 | -1.40695 | 1.41014 | -5.18073 | -3.91147 | -2.34361 | -1.32167 | -0.378628 | 0.810768 | 2.16059 |
| player | theta_norm | 1755 | 2.27039 | 1.18381 | 0.0534289 | 0.556865 | 1.4067 | 2.14206 | 2.97954 | 4.46249 | 5.85197 |
| tossup | beta_1 | 1350 | 0.998526 | 1.26804 | -4.53248 | -0.155994 | 0.201284 | 0.511607 | 2.05225 | 3.29232 | 4.30301 |
| tossup | beta_2 | 1350 | 1.93486 | 1.25726 | -2.17731 | 0.042461 | 0.810243 | 2.21577 | 2.94879 | 3.66798 | 4.62797 |
| tossup | gamma_1 | 1350 | 30.4262 | 120.985 | 0.324006 | 3.94256 | 4.78765 | 5.20513 | 7.61848 | 107.974 | 1698.94 |
| tossup | gamma_2 | 1350 | 69.111 | 194.042 | 0.476945 | 3.51405 | 5.04725 | 8.20473 | 30.1203 | 381.799 | 1933.31 |
| tossup | mu_1 | 1350 | 0.5741 | 0.151173 | 0.141993 | 0.443179 | 0.486246 | 0.507034 | 0.632584 | 0.913318 | 0.990301 |
| tossup | mu_2 | 1350 | 0.671132 | 0.189662 | 0.133884 | 0.407869 | 0.502044 | 0.669492 | 0.840842 | 0.957007 | 0.993778 |
| tossup | topic_weight_1 | 1350 | 0.339422 | 0.335754 | 0.00799154 | 0.0238163 | 0.0712603 | 0.185158 | 0.613397 | 0.971108 | 0.991688 |
| tossup | topic_weight_2 | 1350 | 0.660578 | 0.335754 | 0.00831229 | 0.0288924 | 0.386603 | 0.814842 | 0.92874 | 0.976184 | 0.992008 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 4716 | 0.0603755 | 1.07081 | -3.88222 | -1.90259 | -0.284357 | 0.0253826 | 0.338314 | 2.27633 | 3.90667 |
| bonus_part | beta_2 | 4716 | 0.0286289 | 1.43554 | -3.95825 | -2.60797 | -0.582191 | 0.0401085 | 0.816066 | 2.5343 | 3.58619 |
