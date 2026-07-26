# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/topic-tfidf-ablation/dim_4/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/topic-tfidf-ablation/dim_4`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 507058 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 4 |
| synergy | steps | 2000 |
| synergy | final_loss | 106383 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.538146 |
| mean_synergy_contribution | -0.0581138 |
| median_synergy_contribution | -0.00272905 |
| negative_synergy_fraction | 0.546978 |
| positive_synergy_fraction | 0.42864 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.92175 |
| log_loss | 0.368761 |
| ece | 0.0517893 |
| part_accuracy | 0.84322 |
| part_accuracy_macro_team | 0.844807 |
| part_accuracy_macro_game | 0.843683 |
| part_accuracy_macro_bonus | 0.839212 |
| exact_acc | 0.586347 |
| ppb_mae | 0.44948 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.648954 |
| log_loss | 0.576641 |
| ece | 0.120258 |
| accuracy | 0.714239 |
| buzz_position_mae | 0.145999 |
| buzz_position_median_absolute_error | 0.127428 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.6086 | 0.472622 | 3.41795 | 4.8219 | 5.30913 | 5.61503 | 5.93043 | 6.36848 | 7.28895 |
| player | theta_1 | 1755 | -0.969073 | 1.07299 | -3.78627 | -2.47528 | -1.79356 | -1.14219 | -0.239749 | 0.981752 | 2.57634 |
| player | theta_2 | 1755 | -0.814402 | 0.848204 | -3.80114 | -2.12931 | -1.37601 | -0.835762 | -0.264245 | 0.632338 | 2.04895 |
| player | theta_3 | 1755 | -0.986416 | 1.16663 | -3.34249 | -2.50957 | -1.91398 | -1.21083 | -0.301035 | 1.22833 | 3.28563 |
| player | theta_4 | 1755 | -1.20539 | 1.39572 | -4.10983 | -3.01894 | -2.25143 | -1.43513 | -0.362626 | 1.41746 | 3.83617 |
| player | theta_norm | 1755 | 2.89993 | 0.892224 | 0.325178 | 1.38239 | 2.24642 | 2.92378 | 3.55563 | 4.28535 | 5.56584 |
| tossup | beta_1 | 1350 | 1.02946 | 1.24575 | -0.925971 | -0.025042 | 0.164295 | 0.359302 | 2.02318 | 3.53584 | 5.00197 |
| tossup | beta_2 | 1350 | 0.72657 | 1.0521 | -3.20085 | -0.0243649 | 0.145349 | 0.287382 | 0.771251 | 3.08157 | 4.58553 |
| tossup | beta_3 | 1350 | 0.801336 | 1.13451 | -3.3743 | -0.0478236 | 0.135551 | 0.267783 | 0.833682 | 3.28268 | 4.74372 |
| tossup | beta_4 | 1350 | 1.15323 | 1.42146 | -3.53743 | -0.0617297 | 0.168001 | 0.382945 | 2.16132 | 4.05772 | 5.18579 |
| tossup | gamma_1 | 1350 | 28.438 | 112.972 | 1.59847 | 4.21982 | 4.84873 | 5.18353 | 7.03709 | 93.0083 | 1594.09 |
| tossup | gamma_2 | 1350 | 26.8659 | 120.417 | 0.238475 | 4.3685 | 4.82885 | 5.12843 | 5.63419 | 85.7882 | 1855.34 |
| tossup | gamma_3 | 1350 | 20.3171 | 94.6446 | 0.80151 | 4.40909 | 4.81067 | 5.10503 | 5.65025 | 50.1085 | 1719.7 |
| tossup | gamma_4 | 1350 | 38.6458 | 151.058 | 0.863638 | 4.34276 | 4.85163 | 5.23141 | 8.79876 | 157.894 | 1918.35 |
| tossup | mu_1 | 1350 | 0.557616 | 0.128252 | 0.177597 | 0.453371 | 0.488574 | 0.506312 | 0.562691 | 0.848017 | 0.990916 |
| tossup | mu_2 | 1350 | 0.543749 | 0.119745 | 0.1349 | 0.460938 | 0.48748 | 0.504372 | 0.526132 | 0.856269 | 0.993323 |
| tossup | mu_3 | 1350 | 0.546057 | 0.121883 | 0.144457 | 0.464717 | 0.489302 | 0.504283 | 0.526383 | 0.851826 | 0.990861 |
| tossup | mu_4 | 1350 | 0.58559 | 0.161022 | 0.220099 | 0.45427 | 0.489327 | 0.508104 | 0.648113 | 0.934585 | 0.994206 |
| tossup | topic_weight_1 | 1350 | 0.270287 | 0.311247 | 0.00607094 | 0.0163298 | 0.0340537 | 0.0865538 | 0.562495 | 0.856212 | 0.964148 |
| tossup | topic_weight_2 | 1350 | 0.191512 | 0.243434 | 0.00520952 | 0.0151807 | 0.0328916 | 0.0674792 | 0.220309 | 0.751021 | 0.938564 |
| tossup | topic_weight_3 | 1350 | 0.231661 | 0.304829 | 0.00638256 | 0.0174383 | 0.0369177 | 0.0747482 | 0.233218 | 0.89986 | 0.970955 |
| tossup | topic_weight_4 | 1350 | 0.306541 | 0.326444 | 0.00768315 | 0.0218656 | 0.0487608 | 0.124601 | 0.614935 | 0.917875 | 0.981697 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 4716 | 0.00571894 | 1.00716 | -3.93724 | -1.94264 | -0.252577 | 0.0296654 | 0.270815 | 1.95196 | 3.8462 |
| bonus_part | beta_2 | 4716 | -0.0020431 | 0.997687 | -3.86479 | -2.16179 | -0.248356 | 0.0230167 | 0.271827 | 1.93966 | 3.86397 |
| bonus_part | beta_3 | 4716 | 0.0665548 | 0.872008 | -3.78807 | -1.27541 | -0.223467 | 0.0188494 | 0.244214 | 1.81157 | 4.10474 |
| bonus_part | beta_4 | 4716 | 0.0467736 | 0.873079 | -4.16941 | -1.22155 | -0.212004 | 0.0267287 | 0.250494 | 1.65567 | 4.29051 |
