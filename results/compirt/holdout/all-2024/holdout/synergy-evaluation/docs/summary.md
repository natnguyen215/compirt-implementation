# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/all-2024/holdout/synergy-evaluation`
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
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 85263.7 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.47934 |
| mean_synergy_contribution | -0.504677 |
| median_synergy_contribution | -0.468732 |
| negative_synergy_fraction | 0.746915 |
| positive_synergy_fraction | 0.228703 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.938384 |
| log_loss | 0.325596 |
| ece | 0.0358433 |
| part_accuracy | 0.858691 |
| exact_acc | 0.624094 |
| per_bonus_points_mae | 4.57135 |
| ppb_mae | 1.65731 |
| accuracy | 0.858691 |

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
| bonus_part | beta | 4716 | 0.317477 | 1.42942 | -2.90683 | -1.98196 | -0.910705 | 0.40664 | 1.4965 | 2.50722 | 3.96705 |
| bonus_part | alpha_1 | 4716 | -0.0397857 | 0.49995 | -2.51501 | -0.906415 | -0.299012 | -0.0216596 | 0.257178 | 0.74253 | 1.90116 |
| bonus_part | alpha_2 | 4716 | 0.0691129 | 0.447448 | -2.06611 | -0.642171 | -0.196613 | 0.0615004 | 0.31531 | 0.834649 | 2.15151 |
| bonus_part | alpha_3 | 4716 | 0.0901802 | 0.711804 | -1.95561 | -0.957812 | -0.454596 | 0.058575 | 0.602198 | 1.29087 | 2.41163 |
| bonus_part | alpha_4 | 4716 | 0.0867495 | 0.58339 | -2.16443 | -0.836967 | -0.300452 | 0.0661519 | 0.433168 | 1.06951 | 2.62909 |
| bonus_part | alpha_5 | 4716 | 0.0771211 | 0.547039 | -2.22905 | -0.791128 | -0.286017 | 0.0719141 | 0.425074 | 1.00766 | 2.29136 |
| bonus_part | alpha_norm | 4716 | 1.17302 | 0.498124 | 0.117856 | 0.44297 | 0.792624 | 1.14418 | 1.48875 | 2.05838 | 3.2898 |
| synergy_player | psi_1 | 1755 | -0.00208345 | 0.373161 | -1.79116 | -0.642285 | -0.0586993 | -0.00100475 | 0.0558795 | 0.639669 | 1.76685 |
| synergy_player | psi_2 | 1755 | -0.000917383 | 0.375561 | -1.82796 | -0.617203 | -0.0543294 | -0.00496252 | 0.0576482 | 0.685462 | 1.6487 |
| synergy_player | psi_3 | 1755 | 0.00207396 | 0.374198 | -1.76037 | -0.683615 | -0.0585152 | 0.000686215 | 0.0616423 | 0.602656 | 1.7747 |
| synergy_player | psi_norm | 1755 | 0.513764 | 0.395254 | 0.00992599 | 0.0565197 | 0.198043 | 0.41103 | 0.763061 | 1.31505 | 1.83067 |
| synergy | synergy_score | 3042 | -0.121077 | 0.399785 | -2.61117 | -0.914133 | -0.259597 | -0.000662534 | 0.0803795 | 0.337596 | 1.34384 |
| synergy | synergy_contribution | 60454 | -0.504677 | 0.697213 | -2.61782 | -1.64751 | -0.996538 | -0.468732 | 0 | 0.586454 | 2.25112 |
