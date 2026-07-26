# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-all2024/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 467506 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 84723.4 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.397144 |
| mean_synergy_contribution | -0.220215 |
| median_synergy_contribution | -0.0807908 |
| negative_synergy_fraction | 0.600622 |
| positive_synergy_fraction | 0.374996 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.937103 |
| log_loss | 0.328551 |
| ece | 0.0350151 |
| part_accuracy | 0.858895 |
| part_accuracy_macro_team | 0.86042 |
| part_accuracy_macro_game | 0.859296 |
| part_accuracy_macro_bonus | 0.86947 |
| exact_acc | 0.625583 |
| ppb_mae | 0.690905 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.674274 |
| log_loss | 0.595258 |
| ece | 0.133279 |
| accuracy | 0.708795 |
| buzz_position_mae | 0.133093 |
| buzz_position_median_absolute_error | 0.11048 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.933325 | 0.937103 | 0.00377846 | synergy |
| log_loss | 0.341114 | 0.328551 | -0.0125634 | synergy |
| ece | 0.0429504 | 0.0350151 | -0.00793532 | synergy |
| part_accuracy | 0.852692 | 0.858895 | 0.00620306 | synergy |
| part_accuracy_macro_team | 0.854526 | 0.86042 | 0.00589472 | synergy |
| part_accuracy_macro_game | 0.853124 | 0.859296 | 0.00617183 | synergy |
| part_accuracy_macro_bonus | 0.863262 | 0.86947 | 0.006208 | synergy |
| exact_acc | 0.610381 | 0.625583 | 0.0152016 | synergy |
| ppb_mae | 1.33213 | 0.690905 | -0.641225 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.99078 | 0.91831 | 1.31485 | 3.15598 | 4.51414 | 5.13836 | 5.61875 | 6.22264 | 7.38598 |
| player | theta_1 | 1755 | -0.404101 | 0.578113 | -2.67891 | -1.43419 | -0.788509 | -0.356594 | -0.0198559 | 0.485428 | 1.32255 |
| player | theta_2 | 1755 | -0.462964 | 0.661619 | -2.57315 | -1.58411 | -0.918138 | -0.430054 | -0.0256281 | 0.585899 | 1.49011 |
| player | theta_3 | 1755 | -0.441924 | 0.642937 | -2.76609 | -1.60338 | -0.861248 | -0.402349 | 0.0111911 | 0.560026 | 1.39148 |
| player | theta_4 | 1755 | -0.664602 | 0.642075 | -2.62799 | -1.79099 | -1.08782 | -0.632494 | -0.214704 | 0.378241 | 1.1836 |
| player | theta_5 | 1755 | -0.496565 | 0.682499 | -2.73049 | -1.73322 | -0.948916 | -0.435519 | 0.00725609 | 0.530995 | 1.13937 |
| player | theta_norm | 1755 | 1.67525 | 0.719196 | 0.111419 | 0.71631 | 1.14211 | 1.55364 | 2.09571 | 3.09155 | 3.94227 |
| tossup | beta_1 | 1350 | 0.292013 | 0.530577 | -1.55496 | -0.106463 | 0.0204397 | 0.0946172 | 0.234633 | 1.57421 | 3.71123 |
| tossup | beta_2 | 1350 | 0.357197 | 0.568901 | -2.95208 | -0.0937694 | 0.0270459 | 0.109744 | 0.408266 | 1.54187 | 3.46556 |
| tossup | beta_3 | 1350 | 0.345099 | 0.554814 | -0.875829 | -0.0898983 | 0.0290074 | 0.111337 | 0.337074 | 1.59655 | 2.67118 |
| tossup | beta_4 | 1350 | 0.463859 | 0.618321 | -1.95983 | -0.073618 | 0.0493105 | 0.140563 | 0.970428 | 1.69322 | 2.72283 |
| tossup | beta_5 | 1350 | 0.478108 | 0.658003 | -3.01302 | -0.0973325 | 0.0360479 | 0.145818 | 1.05541 | 1.69715 | 2.81334 |
| tossup | gamma_1 | 1350 | 4.39809 | 15.4773 | 0.802113 | 1.38579 | 2.25865 | 2.82012 | 3.32532 | 6.51514 | 405.699 |
| tossup | gamma_2 | 1350 | 5.42044 | 25.8504 | 0.599705 | 1.44103 | 2.29033 | 2.83144 | 3.4408 | 6.73623 | 592.335 |
| tossup | gamma_3 | 1350 | 7.40267 | 44.8955 | 0.621309 | 1.13658 | 2.02932 | 2.65924 | 3.32319 | 9.05778 | 1037.72 |
| tossup | gamma_4 | 1350 | 8.95692 | 51.7904 | 0.714734 | 1.19624 | 2.05898 | 2.71214 | 3.41246 | 10.1209 | 841.375 |
| tossup | gamma_5 | 1350 | 5.19287 | 15.914 | 0.823874 | 1.43782 | 2.2374 | 2.8652 | 3.5735 | 12.1905 | 282.94 |
| tossup | mu_1 | 1350 | 0.541001 | 0.0997485 | 0.0655899 | 0.397953 | 0.50898 | 0.535973 | 0.569885 | 0.718317 | 0.989842 |
| tossup | mu_2 | 1350 | 0.544687 | 0.102435 | 0.0456977 | 0.383644 | 0.508995 | 0.538901 | 0.575935 | 0.718997 | 0.992617 |
| tossup | mu_3 | 1350 | 0.540496 | 0.113466 | 0.0620118 | 0.336593 | 0.508001 | 0.541781 | 0.577599 | 0.722741 | 0.994329 |
| tossup | mu_4 | 1350 | 0.545502 | 0.118334 | 0.064146 | 0.325414 | 0.503368 | 0.537703 | 0.585728 | 0.753324 | 0.992225 |
| tossup | mu_5 | 1350 | 0.538014 | 0.114461 | 0.0965302 | 0.321786 | 0.502441 | 0.537675 | 0.579908 | 0.732353 | 0.973557 |
| tossup | r_1 | 1350 | 0.840704 | 0.680743 | 0.0833526 | 0.227377 | 0.406904 | 0.634789 | 1.00362 | 2.43505 | 4.87197 |
| tossup | r_2 | 1350 | 0.99834 | 0.882343 | 0.0518164 | 0.204007 | 0.414256 | 0.669593 | 1.15707 | 3.06526 | 4.91988 |
| tossup | r_3 | 1350 | 0.974876 | 0.619366 | 0.0730006 | 0.244676 | 0.476716 | 0.810756 | 1.32908 | 2.20007 | 3.28611 |
| tossup | r_4 | 1350 | 1.14823 | 0.838264 | 0.0707515 | 0.216824 | 0.525125 | 0.926086 | 1.5477 | 2.87636 | 4.38532 |
| tossup | r_5 | 1350 | 1.12628 | 0.859132 | 0.04438 | 0.210459 | 0.480883 | 0.797932 | 1.63303 | 2.85767 | 4.56494 |
| tossup | r_norm | 1350 | 2.79036 | 0.720543 | 0.894222 | 1.67214 | 2.28837 | 2.76345 | 3.28352 | 4.00051 | 5.42647 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.218421 | 1.42414 | -2.65325 | -1.93721 | -0.957097 | 0.205805 | 1.36679 | 2.55401 | 3.39891 |
| bonus_part | alpha_1 | 4716 | 0.130076 | 0.483939 | -1.50042 | -0.61868 | -0.188667 | 0.135543 | 0.41669 | 0.935955 | 2.21448 |
| bonus_part | alpha_2 | 4716 | 0.147497 | 0.586166 | -1.98863 | -0.753392 | -0.230405 | 0.13207 | 0.478748 | 1.12168 | 3.34203 |
| bonus_part | alpha_3 | 4716 | 0.156556 | 0.529743 | -1.87961 | -0.638978 | -0.174512 | 0.10895 | 0.482244 | 1.10219 | 2.43333 |
| bonus_part | alpha_4 | 4716 | 0.196403 | 0.692435 | -1.83419 | -0.946268 | -0.265763 | 0.222587 | 0.632067 | 1.29788 | 3.1168 |
| bonus_part | alpha_5 | 4716 | 0.143968 | 0.591365 | -1.98399 | -0.789646 | -0.251275 | 0.166966 | 0.515973 | 1.05588 | 2.91056 |
| bonus_part | alpha_norm | 4716 | 1.21406 | 0.579519 | 0.0538845 | 0.372288 | 0.770606 | 1.178 | 1.58031 | 2.26572 | 3.44145 |
