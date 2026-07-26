# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_2/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-ablation-gamma/dim_2`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 465984 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 2 |
| synergy | steps | 2000 |
| synergy | final_loss | 80910.7 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.504893 |
| mean_synergy_contribution | 0.0692146 |
| median_synergy_contribution | 0.00111249 |
| negative_synergy_fraction | 0.4582 |
| positive_synergy_fraction | 0.517418 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.924106 |
| log_loss | 0.359224 |
| ece | 0.0377852 |
| part_accuracy | 0.843269 |
| part_accuracy_macro_team | 0.844522 |
| part_accuracy_macro_game | 0.84363 |
| part_accuracy_macro_bonus | 0.849265 |
| exact_acc | 0.587091 |
| ppb_mae | 0.487036 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.650791 |
| log_loss | 0.619011 |
| ece | 0.146647 |
| accuracy | 0.691828 |
| buzz_position_mae | 0.139839 |
| buzz_position_median_absolute_error | 0.117737 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.18325 | 0.916809 | 1.34427 | 3.28517 | 4.71674 | 5.27811 | 5.7695 | 6.52994 | 7.8107 |
| player | theta_1 | 1755 | -0.645366 | 0.752887 | -3.12703 | -2.1904 | -1.04262 | -0.538438 | -0.108064 | 0.378459 | 1.05704 |
| player | theta_2 | 1755 | -0.630107 | 0.674842 | -2.86277 | -1.86384 | -1.0097 | -0.572225 | -0.189301 | 0.432032 | 1.49252 |
| player | theta_norm | 1755 | 1.14235 | 0.728377 | 0.0111596 | 0.247957 | 0.628053 | 0.992343 | 1.48583 | 2.63019 | 3.7328 |
| tossup | beta_1 | 1350 | 0.899372 | 0.677676 | -1.12149 | 0.0131773 | 0.167525 | 0.990874 | 1.4296 | 1.91071 | 3.69158 |
| tossup | beta_2 | 1350 | 0.839638 | 0.679261 | -1.93837 | 0.0105146 | 0.160934 | 0.885369 | 1.37107 | 1.85585 | 3.15027 |
| tossup | gamma_1 | 1350 | 13.5699 | 63.748 | 0.427476 | 1.03738 | 1.87926 | 2.80658 | 4.15561 | 32.6619 | 1009.99 |
| tossup | gamma_2 | 1350 | 11.4766 | 50.411 | 0.567346 | 1.09 | 1.91158 | 2.79441 | 4.05257 | 31.0424 | 780.936 |
| tossup | mu_1 | 1350 | 0.545418 | 0.168333 | 0.0408241 | 0.220885 | 0.474415 | 0.545932 | 0.653169 | 0.819771 | 0.994059 |
| tossup | mu_2 | 1350 | 0.544938 | 0.169876 | 0.0317124 | 0.225458 | 0.473114 | 0.542037 | 0.644127 | 0.828378 | 0.993242 |
| tossup | r_1 | 1350 | 1.6542 | 0.863782 | 0.0536129 | 0.234663 | 0.985281 | 1.73838 | 2.27185 | 3.05037 | 4.08391 |
| tossup | r_2 | 1350 | 1.60162 | 0.962358 | 0.0373285 | 0.234881 | 0.732443 | 1.54278 | 2.33878 | 3.258 | 4.36998 |
| tossup | r_norm | 1350 | 2.50491 | 0.835791 | 0.40469 | 1.31213 | 1.93339 | 2.39263 | 2.93134 | 4.12309 | 5.59988 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.0563626 | 1.64117 | -3.52413 | -2.58546 | -1.37777 | 0.156102 | 1.40526 | 2.59005 | 3.56389 |
| bonus_part | alpha_1 | 4716 | 0.839351 | 0.383662 | 0.176577 | 0.437281 | 0.606145 | 0.754785 | 0.948322 | 1.61429 | 3.58594 |
| bonus_part | alpha_2 | 4716 | 0.860827 | 0.437564 | 0.206456 | 0.425589 | 0.588404 | 0.750445 | 0.98503 | 1.74434 | 4.1331 |
| bonus_part | alpha_norm | 4716 | 1.23387 | 0.5116 | 0.45962 | 0.685289 | 0.903856 | 1.12227 | 1.39146 | 2.22721 | 4.93055 |
