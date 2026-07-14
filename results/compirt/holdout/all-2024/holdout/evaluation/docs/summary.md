# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/all-2024/holdout/evaluation`
Result root: `results/compirt/holdout/all-2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 473105 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 84928.7 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.239034 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.932352 |
| log_loss | 0.340014 |
| ece | 0.0370095 |
| part_accuracy | 0.852323 |
| exact_acc | 0.609306 |
| per_bonus_points_mae | 4.86941 |
| ppb_mae | 2.12287 |
| accuracy | 0.852323 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.683797 |
| log_loss | 0.591326 |
| ece | 0.149341 |
| accuracy | 0.701114 |
| buzz_position_mae | 0.143238 |
| buzz_position_median_absolute_error | 0.123594 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.932352 | 0.938384 | 0.00603197 | synergy |
| log_loss | 0.340014 | 0.325596 | -0.0144186 | synergy |
| ece | 0.0370095 | 0.0358433 | -0.00116626 | synergy |
| accuracy | 0.852323 | 0.858691 | 0.00636848 | synergy |
| part_accuracy | 0.852323 | 0.858691 | 0.00636848 | synergy |
| exact_acc | 0.609306 | 0.624094 | 0.0147881 | synergy |
| per_bonus_points_mae | 4.86941 | 4.57135 | -0.298059 | synergy |
| ppb_mae | 2.12287 | 1.65731 | -0.465569 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.01869 | 0.831158 | 1.36038 | 3.34654 | 4.6331 | 5.15451 | 5.57089 | 6.08943 | 6.94181 |
| player | theta_1 | 1755 | 0.0498846 | 0.642754 | -2.21465 | -1.00366 | -0.363987 | 0.0566982 | 0.477198 | 1.05138 | 2.46832 |
| player | theta_2 | 1755 | -0.117049 | 0.515023 | -1.7986 | -0.994588 | -0.447951 | -0.114996 | 0.216666 | 0.718264 | 1.51172 |
| player | theta_3 | 1755 | 0.237633 | 0.860999 | -3.21343 | -1.45963 | -0.157172 | 0.353737 | 0.797216 | 1.3879 | 2.36524 |
| player | theta_4 | 1755 | -0.00580181 | 0.789764 | -2.90299 | -1.36121 | -0.494897 | 0.0293537 | 0.547801 | 1.23741 | 2.28912 |
| player | theta_5 | 1755 | -0.221676 | 0.588029 | -2.30223 | -1.14614 | -0.593759 | -0.228314 | 0.146585 | 0.778904 | 1.7529 |
| player | theta_norm | 1755 | 1.49896 | 0.512791 | 0.254983 | 0.760754 | 1.14203 | 1.45114 | 1.7878 | 2.40506 | 3.38837 |
| tossup | beta | 1350 | 3.34126 | 0.781601 | 0.20615 | 1.90161 | 2.93196 | 3.39615 | 3.85566 | 4.46343 | 5.30968 |
| tossup | gamma | 1350 | 55.4915 | 177.974 | 2.82206 | 5.71873 | 8.8938 | 12.9586 | 27.2244 | 215.027 | 2252.87 |
| tossup | mu | 1350 | 0.590618 | 0.1341 | 0.110025 | 0.364744 | 0.503968 | 0.589382 | 0.677585 | 0.814072 | 0.98542 |
| tossup | alpha_1 | 1350 | -0.16624 | 0.686364 | -2.09508 | -1.45021 | -0.596665 | -0.104122 | 0.330519 | 0.8124 | 1.74489 |
| tossup | alpha_2 | 1350 | 0.331821 | 0.636115 | -1.88323 | -0.707599 | -0.0897906 | 0.333016 | 0.737126 | 1.35233 | 2.39322 |
| tossup | alpha_3 | 1350 | 0.744132 | 0.811585 | -1.19468 | -0.465911 | 0.150661 | 0.693255 | 1.25311 | 2.22238 | 3.63644 |
| tossup | alpha_4 | 1350 | 0.696167 | 0.703454 | -1.19415 | -0.452473 | 0.196402 | 0.696466 | 1.14867 | 1.88991 | 2.84085 |
| tossup | alpha_5 | 1350 | 0.307224 | 0.661824 | -2.0286 | -0.731586 | -0.146067 | 0.245376 | 0.762245 | 1.43225 | 2.2873 |
| tossup | alpha_norm | 1350 | 1.85875 | 0.530296 | 0.334511 | 1.07468 | 1.4868 | 1.83123 | 2.19306 | 2.7689 | 3.99255 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.678555 | 1.40926 | -2.54497 | -1.53581 | -0.52567 | 0.780365 | 1.88136 | 2.74679 | 3.87118 |
| bonus_part | alpha_1 | 4716 | -0.0990685 | 0.481136 | -2.48644 | -0.958388 | -0.335678 | -0.0680904 | 0.177234 | 0.637474 | 1.83122 |
| bonus_part | alpha_2 | 4716 | 0.166616 | 0.438679 | -1.90119 | -0.507243 | -0.0994459 | 0.137469 | 0.401227 | 0.949818 | 2.30352 |
| bonus_part | alpha_3 | 4716 | 0.130813 | 0.705807 | -1.98973 | -0.942549 | -0.392347 | 0.118196 | 0.639169 | 1.29827 | 2.54418 |
| bonus_part | alpha_4 | 4716 | 0.190578 | 0.561463 | -1.86609 | -0.707997 | -0.171818 | 0.174546 | 0.534413 | 1.12103 | 2.79904 |
| bonus_part | alpha_5 | 4716 | 0.212502 | 0.538442 | -1.71476 | -0.5987 | -0.141077 | 0.196354 | 0.51743 | 1.1589 | 2.46742 |
| bonus_part | alpha_norm | 4716 | 1.18017 | 0.519951 | 0.0804981 | 0.44728 | 0.794155 | 1.13933 | 1.46848 | 2.14956 | 3.30225 |
