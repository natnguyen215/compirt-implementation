# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/tfidf-multidim-cumulative-difficulty-all2024/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/tfidf-multidim-cumulative-difficulty-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 358742 |
| pyramidal | calibrate_correctness | False |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 66812.8 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.0179513 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.920612 |
| log_loss | 0.367469 |
| ece | 0.039716 |
| part_accuracy | 0.839137 |
| part_accuracy_macro_team | 0.841863 |
| part_accuracy_macro_game | 0.839304 |
| part_accuracy_macro_bonus | 0.837622 |
| exact_acc | 0.579945 |
| ppb_mae | 1.58176 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.700574 |
| log_loss | 0.574214 |
| ece | 0.12801 |
| accuracy | 0.716889 |
| buzz_position_mae | 0.128959 |
| buzz_position_median_absolute_error | 0.108413 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.920612 | 0.925131 | 0.00451986 | synergy |
| log_loss | 0.367469 | 0.357551 | -0.00991714 | synergy |
| ece | 0.039716 | 0.0386346 | -0.00108141 | synergy |
| part_accuracy | 0.839137 | 0.84331 | 0.0041735 | synergy |
| part_accuracy_macro_team | 0.841863 | 0.846946 | 0.0050832 | synergy |
| part_accuracy_macro_game | 0.839304 | 0.843593 | 0.00428934 | synergy |
| part_accuracy_macro_bonus | 0.837622 | 0.84297 | 0.00534779 | synergy |
| exact_acc | 0.579945 | 0.591229 | 0.0112842 | synergy |
| ppb_mae | 1.58176 | 1.01464 | -0.567125 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.51545 | 1.34868 | 0.675408 | 1.62193 | 3.90179 | 4.86275 | 5.46194 | 6.16661 | 7.19792 |
| player | theta_1 | 1455 | -0.0360388 | 0.690565 | -2.34203 | -1.35493 | -0.44658 | 0.0987609 | 0.44396 | 0.918728 | 1.786 |
| player | theta_2 | 1455 | -0.0638962 | 0.699806 | -2.56766 | -1.34739 | -0.490403 | 0.0694276 | 0.42712 | 0.912724 | 1.70503 |
| player | theta_3 | 1455 | -0.0352001 | 0.705628 | -2.71444 | -1.33233 | -0.463515 | 0.0689169 | 0.476763 | 0.963323 | 1.76588 |
| player | theta_4 | 1455 | -0.116469 | 0.700249 | -2.5811 | -1.50361 | -0.501579 | 0.000366095 | 0.360461 | 0.885434 | 1.59526 |
| player | theta_5 | 1455 | -0.0383729 | 0.728238 | -2.48887 | -1.46854 | -0.456457 | 0.0894974 | 0.475362 | 0.962213 | 1.36836 |
| player | theta_norm | 1455 | 1.4555 | 0.622039 | 0.253964 | 0.618174 | 0.98964 | 1.34045 | 1.82704 | 2.64754 | 3.73722 |
| tossup | beta_1 | 1260 | 0.654074 | 0.440221 | -1.23571 | 0.202854 | 0.387148 | 0.527926 | 0.790919 | 1.63495 | 2.60045 |
| tossup | beta_2 | 1260 | 0.638211 | 0.425808 | -2.12928 | 0.198526 | 0.39431 | 0.537887 | 0.745887 | 1.55101 | 3.11713 |
| tossup | beta_3 | 1260 | 0.714169 | 0.49659 | -1.4185 | 0.220029 | 0.400365 | 0.55408 | 0.866841 | 1.81272 | 2.97633 |
| tossup | beta_4 | 1260 | 0.779324 | 0.516062 | -1.03974 | 0.200156 | 0.405997 | 0.614079 | 1.09715 | 1.77215 | 2.8198 |
| tossup | beta_5 | 1260 | 0.774753 | 0.529811 | -1.55459 | 0.207415 | 0.409013 | 0.586993 | 1.08246 | 1.83067 | 2.79247 |
| tossup | gamma_1 | 1260 | 11.0905 | 57.4982 | 0.527099 | 2.95098 | 4.3764 | 4.99774 | 5.68649 | 18.001 | 1112.66 |
| tossup | gamma_2 | 1260 | 15.5848 | 115.303 | 0.398468 | 3.06714 | 4.46437 | 5.00073 | 5.75795 | 14.6832 | 2048.1 |
| tossup | gamma_3 | 1260 | 12.5263 | 59.4365 | 0.667511 | 3.11977 | 4.41931 | 5.06749 | 6.06798 | 26.8104 | 1580.03 |
| tossup | gamma_4 | 1260 | 12.407 | 67.9432 | 0.51738 | 3.003 | 4.46145 | 5.08695 | 6.22503 | 23.2931 | 1517.85 |
| tossup | gamma_5 | 1260 | 14.4251 | 70.052 | 0.510504 | 3.32108 | 4.58754 | 5.19247 | 6.7486 | 29.055 | 1392.8 |
| tossup | mu_1 | 1260 | 0.499895 | 0.100082 | 0.169505 | 0.387388 | 0.446171 | 0.475211 | 0.524069 | 0.706981 | 0.981093 |
| tossup | mu_2 | 1260 | 0.489487 | 0.0909184 | 0.184846 | 0.389133 | 0.444636 | 0.471585 | 0.505944 | 0.677917 | 0.940551 |
| tossup | mu_3 | 1260 | 0.505437 | 0.118971 | 0.162897 | 0.375298 | 0.44002 | 0.474073 | 0.527441 | 0.777244 | 0.987235 |
| tossup | mu_4 | 1260 | 0.520068 | 0.128851 | 0.154518 | 0.374195 | 0.441336 | 0.480495 | 0.575129 | 0.800026 | 0.970953 |
| tossup | mu_5 | 1260 | 0.511732 | 0.117929 | 0.204826 | 0.379423 | 0.444453 | 0.476951 | 0.547157 | 0.770743 | 0.971617 |
| tossup | alpha_1 | 1260 | 1.00632 | 0.835178 | 0.0907184 | 0.23215 | 0.446497 | 0.722365 | 1.32641 | 2.66504 | 6.32599 |
| tossup | alpha_2 | 1260 | 0.946944 | 0.765439 | 0.0826538 | 0.219053 | 0.44658 | 0.719136 | 1.16784 | 2.55466 | 5.35013 |
| tossup | alpha_3 | 1260 | 1.1343 | 0.980165 | 0.093849 | 0.230428 | 0.451771 | 0.774889 | 1.49589 | 3.24667 | 6.15817 |
| tossup | alpha_4 | 1260 | 1.43314 | 1.16458 | 0.105808 | 0.255991 | 0.568277 | 1.02296 | 1.93417 | 4.01682 | 5.96985 |
| tossup | alpha_5 | 1260 | 1.27971 | 0.997355 | 0.078018 | 0.247551 | 0.507749 | 0.923992 | 1.8749 | 3.27654 | 5.45532 |
| tossup | alpha_norm | 1260 | 3.26493 | 0.905484 | 1.07251 | 1.97339 | 2.60079 | 3.14947 | 3.83507 | 4.93375 | 6.84994 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 1.14403 | 1.55086 | -2.34948 | -1.57786 | -0.149725 | 1.44008 | 2.46583 | 3.25691 | 3.98785 |
| bonus_part | alpha_1 | 3768 | 0.66284 | 0.244118 | 0.273289 | 0.399478 | 0.473552 | 0.598409 | 0.81516 | 1.07961 | 2.72171 |
| bonus_part | alpha_2 | 3768 | 0.661701 | 0.254381 | 0.23003 | 0.391399 | 0.481287 | 0.599839 | 0.802 | 1.077 | 3.52666 |
| bonus_part | alpha_3 | 3768 | 0.689393 | 0.277866 | 0.248942 | 0.390146 | 0.478909 | 0.628967 | 0.843987 | 1.12009 | 2.81837 |
| bonus_part | alpha_4 | 3768 | 0.728077 | 0.360614 | 0.254738 | 0.381264 | 0.487734 | 0.654678 | 0.851309 | 1.33324 | 3.60019 |
| bonus_part | alpha_5 | 3768 | 0.704513 | 0.309465 | 0.255603 | 0.402955 | 0.485966 | 0.626912 | 0.845704 | 1.19488 | 3.56442 |
| bonus_part | alpha_norm | 3768 | 1.60271 | 0.487341 | 0.852737 | 0.964965 | 1.18054 | 1.5534 | 1.97016 | 2.41077 | 3.93898 |
