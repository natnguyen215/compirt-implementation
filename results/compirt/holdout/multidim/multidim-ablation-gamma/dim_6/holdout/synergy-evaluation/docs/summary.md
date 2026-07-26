# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-ablation-gamma/dim_6/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-ablation-gamma/dim_6`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 472185 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 6 |
| synergy | steps | 2000 |
| synergy | final_loss | 86783.1 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.466495 |
| mean_synergy_contribution | -1.40491 |
| median_synergy_contribution | -1.41239 |
| negative_synergy_fraction | 0.9559 |
| positive_synergy_fraction | 0.0197175 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.926771 |
| log_loss | 0.352683 |
| ece | 0.0372763 |
| part_accuracy | 0.845844 |
| part_accuracy_macro_team | 0.848987 |
| part_accuracy_macro_game | 0.846394 |
| part_accuracy_macro_bonus | 0.852224 |
| exact_acc | 0.595676 |
| ppb_mae | 1.04156 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.681767 |
| log_loss | 0.591869 |
| ece | 0.136516 |
| accuracy | 0.707684 |
| buzz_position_mae | 0.133949 |
| buzz_position_median_absolute_error | 0.111917 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.85996 | 1.02196 | 1.1422 | 2.66531 | 4.39244 | 5.05804 | 5.54621 | 6.14203 | 7.23544 |
| player | theta_1 | 1755 | 0.193978 | 0.604098 | -2.19245 | -0.952267 | -0.165159 | 0.276848 | 0.615443 | 1.05496 | 1.8918 |
| player | theta_2 | 1755 | 0.0920028 | 0.571746 | -1.88431 | -0.971308 | -0.265515 | 0.129949 | 0.494567 | 0.964248 | 1.61259 |
| player | theta_3 | 1755 | 0.209564 | 0.562588 | -1.81132 | -0.814972 | -0.118142 | 0.251297 | 0.577561 | 1.0715 | 2.12982 |
| player | theta_4 | 1755 | 0.0926363 | 0.630303 | -2.31813 | -1.07827 | -0.309512 | 0.137325 | 0.569742 | 1.02044 | 1.52065 |
| player | theta_5 | 1755 | 0.0700181 | 0.584951 | -1.74313 | -0.918876 | -0.325326 | 0.120509 | 0.479581 | 0.996908 | 2.16747 |
| player | theta_6 | 1755 | -0.0849257 | 0.601601 | -2.77068 | -1.12444 | -0.459051 | -0.0420452 | 0.333598 | 0.824611 | 1.64724 |
| player | theta_norm | 1755 | 1.42468 | 0.435422 | 0.323082 | 0.781402 | 1.11101 | 1.38085 | 1.67927 | 2.23222 | 3.37553 |
| tossup | beta_1 | 1350 | 0.691821 | 0.451472 | -1.11543 | 0.187967 | 0.401463 | 0.576121 | 0.860057 | 1.63286 | 3.21904 |
| tossup | beta_2 | 1350 | 0.763758 | 0.495187 | -2.99938 | 0.143019 | 0.44914 | 0.662452 | 1.05008 | 1.66957 | 3.06617 |
| tossup | beta_3 | 1350 | 0.708198 | 0.491732 | -1.23598 | 0.168552 | 0.412702 | 0.559709 | 0.853623 | 1.75977 | 2.56966 |
| tossup | beta_4 | 1350 | 0.770569 | 0.543021 | -3.4254 | 0.170234 | 0.417509 | 0.607936 | 1.07972 | 1.82569 | 2.88457 |
| tossup | beta_5 | 1350 | 0.624931 | 0.426531 | -0.223618 | 0.140834 | 0.361545 | 0.512279 | 0.749923 | 1.52371 | 2.98056 |
| tossup | beta_6 | 1350 | 0.707989 | 0.498472 | -1.14071 | 0.12734 | 0.375539 | 0.577805 | 0.9314 | 1.70854 | 2.87426 |
| tossup | gamma_1 | 1350 | 17.4075 | 90.5338 | 0.237243 | 2.82268 | 4.28705 | 4.95408 | 5.82279 | 29.3303 | 1967.33 |
| tossup | gamma_2 | 1350 | 15.0085 | 81.4907 | 0.323837 | 2.70658 | 4.09515 | 4.83937 | 6.01163 | 20.8038 | 1717.19 |
| tossup | gamma_3 | 1350 | 10.9085 | 53.5681 | 0.398236 | 3.14746 | 4.34019 | 4.94566 | 5.9058 | 17.6486 | 1318.81 |
| tossup | gamma_4 | 1350 | 20.1534 | 123.077 | 0.0913269 | 3.34287 | 4.45508 | 5.06686 | 6.42826 | 41.3085 | 2558.78 |
| tossup | gamma_5 | 1350 | 12.2188 | 55.4056 | 1.20018 | 3.26173 | 4.36945 | 4.95749 | 5.67803 | 23.6835 | 1347.46 |
| tossup | gamma_6 | 1350 | 18.0588 | 97.2012 | 0.241976 | 2.97169 | 4.22227 | 4.96519 | 6.13007 | 28.0675 | 1725.44 |
| tossup | mu_1 | 1350 | 0.499607 | 0.102401 | 0.111586 | 0.377321 | 0.447902 | 0.480037 | 0.529388 | 0.693405 | 0.986909 |
| tossup | mu_2 | 1350 | 0.518883 | 0.120485 | 0.148101 | 0.370645 | 0.447625 | 0.491619 | 0.567571 | 0.761606 | 0.993928 |
| tossup | mu_3 | 1350 | 0.497969 | 0.101695 | 0.183975 | 0.374788 | 0.445913 | 0.477923 | 0.518912 | 0.71192 | 0.989262 |
| tossup | mu_4 | 1350 | 0.496388 | 0.104729 | 0.127346 | 0.35988 | 0.442301 | 0.477975 | 0.532044 | 0.698116 | 0.975307 |
| tossup | mu_5 | 1350 | 0.489351 | 0.0989415 | 0.18334 | 0.377755 | 0.441255 | 0.470337 | 0.507195 | 0.683399 | 0.977359 |
| tossup | mu_6 | 1350 | 0.496323 | 0.108126 | 0.175695 | 0.373706 | 0.437716 | 0.472539 | 0.528006 | 0.719415 | 0.992092 |
| tossup | r_1 | 1350 | 0.956286 | 0.65307 | 0.0527054 | 0.190366 | 0.480703 | 0.810705 | 1.263 | 2.24572 | 4.34846 |
| tossup | r_2 | 1350 | 1.26052 | 0.962149 | 0.0621418 | 0.277822 | 0.539475 | 0.922595 | 1.723 | 3.26648 | 4.96228 |
| tossup | r_3 | 1350 | 1.03767 | 0.85447 | 0.076454 | 0.22802 | 0.424403 | 0.718891 | 1.40455 | 2.91972 | 5.10453 |
| tossup | r_4 | 1350 | 1.11537 | 0.852453 | 0.0827821 | 0.244137 | 0.465247 | 0.799771 | 1.55139 | 2.9009 | 4.28194 |
| tossup | r_5 | 1350 | 0.830335 | 0.668523 | 0.0576837 | 0.20103 | 0.386641 | 0.626272 | 1.02143 | 2.30269 | 4.81157 |
| tossup | r_6 | 1350 | 1.02167 | 0.704441 | 0.0527722 | 0.211232 | 0.484701 | 0.831293 | 1.40405 | 2.43298 | 3.65821 |
| tossup | r_norm | 1350 | 3.11548 | 0.775308 | 1.26139 | 1.94368 | 2.60593 | 3.07478 | 3.54947 | 4.49166 | 7.28757 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.453251 | 1.45211 | -2.74361 | -1.84244 | -0.808807 | 0.565867 | 1.65708 | 2.60634 | 4.06412 |
| bonus_part | alpha_1 | 4716 | 0.775757 | 0.326273 | 0.187114 | 0.403543 | 0.533575 | 0.69506 | 0.972742 | 1.35468 | 3.60042 |
| bonus_part | alpha_2 | 4716 | 0.817585 | 0.408196 | 0.248256 | 0.406354 | 0.54523 | 0.737303 | 0.944242 | 1.4925 | 4.1931 |
| bonus_part | alpha_3 | 4716 | 0.795836 | 0.344805 | 0.257859 | 0.431164 | 0.535888 | 0.70963 | 0.993805 | 1.37067 | 3.47972 |
| bonus_part | alpha_4 | 4716 | 0.79083 | 0.375815 | 0.224348 | 0.424005 | 0.542474 | 0.712441 | 0.93512 | 1.36369 | 3.80518 |
| bonus_part | alpha_5 | 4716 | 0.78331 | 0.330566 | 0.22752 | 0.436336 | 0.567917 | 0.728322 | 0.912946 | 1.29377 | 4.40924 |
| bonus_part | alpha_6 | 4716 | 0.759816 | 0.26258 | 0.239562 | 0.434159 | 0.579838 | 0.727286 | 0.881006 | 1.19885 | 2.93316 |
| bonus_part | alpha_norm | 4716 | 2.02036 | 0.591092 | 1.03659 | 1.20079 | 1.54436 | 1.97323 | 2.43468 | 3.04552 | 4.71238 |
