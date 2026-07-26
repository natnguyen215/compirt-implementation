# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_4/holdout/syn_5/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation/dim_4/holdout/syn_5`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 4 |
| synergy | steps | 2000 |
| synergy | final_loss | 87683.3 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 5 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.326386 |
| mean_synergy_contribution | -0.310974 |
| median_synergy_contribution | -0.238712 |
| negative_synergy_fraction | 0.66128 |
| positive_synergy_fraction | 0.314338 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.935906 |
| log_loss | 0.329228 |
| ece | 0.031005 |
| part_accuracy | 0.856359 |
| part_accuracy_macro_team | 0.857913 |
| part_accuracy_macro_game | 0.85676 |
| part_accuracy_macro_bonus | 0.865935 |
| exact_acc | 0.618751 |
| ppb_mae | 0.616164 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.675263 |
| log_loss | 0.598647 |
| ece | 0.151109 |
| accuracy | 0.696872 |
| buzz_position_mae | 0.145206 |
| buzz_position_median_absolute_error | 0.126221 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.04166 | 0.820328 | 1.57959 | 3.35859 | 4.64504 | 5.1694 | 5.60326 | 6.13275 | 6.92307 |
| player | theta_1 | 1755 | 0.245881 | 0.618972 | -1.65976 | -0.799675 | -0.148318 | 0.273862 | 0.644532 | 1.23594 | 2.80276 |
| player | theta_2 | 1755 | 0.29218 | 0.711648 | -2.31342 | -1.03116 | -0.079412 | 0.35028 | 0.744606 | 1.34316 | 3.41047 |
| player | theta_3 | 1755 | 0.0237141 | 0.904335 | -3.33637 | -1.71773 | -0.471462 | 0.147226 | 0.610191 | 1.3165 | 2.3242 |
| player | theta_4 | 1755 | 0.00344224 | 0.721661 | -2.32564 | -1.13265 | -0.498729 | 0.0132605 | 0.509278 | 1.18918 | 2.3372 |
| player | theta_norm | 1755 | 1.44355 | 0.538173 | 0.167389 | 0.667774 | 1.07167 | 1.39423 | 1.7521 | 2.34449 | 3.68573 |
| tossup | beta | 1350 | 3.31971 | 0.786944 | 0.216614 | 1.87139 | 2.88939 | 3.38498 | 3.82251 | 4.46125 | 5.45026 |
| tossup | gamma | 1350 | 55.4887 | 177.336 | 3.01183 | 5.73794 | 8.84678 | 13.4245 | 27.5125 | 197.253 | 2149.88 |
| tossup | mu | 1350 | 0.589508 | 0.136681 | 0.11219 | 0.361494 | 0.50161 | 0.586737 | 0.678035 | 0.817556 | 0.985512 |
| tossup | alpha_1 | 1350 | -0.130187 | 0.737664 | -2.15958 | -1.56392 | -0.54537 | -0.0532618 | 0.391482 | 0.912838 | 2.20721 |
| tossup | alpha_2 | 1350 | 0.207322 | 0.787195 | -1.55129 | -0.835696 | -0.323024 | 0.0504529 | 0.627672 | 1.72018 | 3.6974 |
| tossup | alpha_3 | 1350 | 1.00807 | 0.638875 | -1.29324 | -0.0947172 | 0.60146 | 1.06282 | 1.44506 | 1.96598 | 3.1617 |
| tossup | alpha_4 | 1350 | 0.468585 | 0.724659 | -1.20953 | -0.536758 | -0.0168978 | 0.326961 | 0.797457 | 1.94011 | 2.90375 |
| tossup | alpha_norm | 1350 | 1.76335 | 0.531095 | 0.281402 | 0.948945 | 1.39034 | 1.75167 | 2.09731 | 2.66036 | 3.81788 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.351367 | 1.42053 | -2.79205 | -1.90572 | -0.889371 | 0.428486 | 1.50314 | 2.53802 | 3.92302 |
| bonus_part | alpha_1 | 4716 | -0.0696473 | 0.577906 | -2.62567 | -1.06841 | -0.394492 | -0.0866498 | 0.26509 | 0.873976 | 2.36844 |
| bonus_part | alpha_2 | 4716 | -0.00707166 | 0.612116 | -2.00834 | -0.934712 | -0.426766 | -0.0729655 | 0.35352 | 1.10503 | 2.54825 |
| bonus_part | alpha_3 | 4716 | 0.152523 | 0.662048 | -1.97326 | -0.917654 | -0.279988 | 0.120566 | 0.561868 | 1.33013 | 2.59663 |
| bonus_part | alpha_4 | 4716 | 0.0659364 | 0.575521 | -1.73863 | -0.784661 | -0.308676 | 0.0370772 | 0.394065 | 1.10463 | 2.86921 |
| bonus_part | alpha_norm | 4716 | 1.12453 | 0.495867 | 0.0705244 | 0.385524 | 0.752096 | 1.07802 | 1.45111 | 2.03408 | 3.12018 |
