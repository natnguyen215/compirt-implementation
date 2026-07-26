# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-all2024/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 467806 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 85717.4 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.371755 |
| mean_synergy_contribution | -0.391459 |
| median_synergy_contribution | -0.300501 |
| negative_synergy_fraction | 0.674232 |
| positive_synergy_fraction | 0.301386 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.935844 |
| log_loss | 0.333794 |
| ece | 0.040041 |
| part_accuracy | 0.856072 |
| part_accuracy_macro_team | 0.858234 |
| part_accuracy_macro_game | 0.856581 |
| part_accuracy_macro_bonus | 0.864618 |
| exact_acc | 0.617792 |
| ppb_mae | 0.779055 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.674184 |
| log_loss | 0.598882 |
| ece | 0.140053 |
| accuracy | 0.703705 |
| buzz_position_mae | 0.134469 |
| buzz_position_median_absolute_error | 0.112065 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.926833 | 0.935844 | 0.00901157 | synergy |
| log_loss | 0.35305 | 0.333794 | -0.0192555 | synergy |
| ece | 0.0384582 | 0.040041 | 0.00158276 | no-synergy |
| part_accuracy | 0.847123 | 0.856072 | 0.00894895 | synergy |
| part_accuracy_macro_team | 0.849199 | 0.858234 | 0.00903482 | synergy |
| part_accuracy_macro_game | 0.847631 | 0.856581 | 0.00894993 | synergy |
| part_accuracy_macro_bonus | 0.85991 | 0.864618 | 0.00470782 | synergy |
| exact_acc | 0.595941 | 0.617792 | 0.0218513 | synergy |
| ppb_mae | 1.7272 | 0.779055 | -0.948146 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.89181 | 1.00301 | 1.19529 | 2.75454 | 4.45306 | 5.06375 | 5.57369 | 6.16994 | 7.17542 |
| player | theta_1 | 1755 | 0.0919638 | 0.577129 | -2.18046 | -1.03076 | -0.238222 | 0.141945 | 0.45323 | 0.986065 | 1.71512 |
| player | theta_2 | 1755 | 0.178787 | 0.560188 | -1.88174 | -0.905858 | -0.168052 | 0.251265 | 0.553056 | 1.02431 | 1.97316 |
| player | theta_3 | 1755 | 0.14651 | 0.593374 | -2.02385 | -0.933869 | -0.223347 | 0.199201 | 0.548766 | 1.06442 | 1.97164 |
| player | theta_4 | 1755 | 0.0979658 | 0.58161 | -2.35032 | -0.94539 | -0.279473 | 0.170844 | 0.51942 | 0.910635 | 1.85282 |
| player | theta_5 | 1755 | 0.0809445 | 0.632372 | -2.17203 | -1.10625 | -0.288958 | 0.149506 | 0.523408 | 0.994659 | 1.67955 |
| player | theta_norm | 1755 | 1.27226 | 0.442331 | 0.270879 | 0.645478 | 0.943674 | 1.22887 | 1.54625 | 2.07901 | 3.07614 |
| tossup | beta_1 | 1350 | 0.890864 | 0.606405 | -2.17108 | 0.166471 | 0.433449 | 0.716769 | 1.3118 | 2.03649 | 3.19657 |
| tossup | beta_2 | 1350 | 0.69354 | 0.463739 | -3.27737 | 0.175995 | 0.431946 | 0.608201 | 0.867321 | 1.60206 | 2.56476 |
| tossup | beta_3 | 1350 | 0.765074 | 0.562824 | -1.01255 | 0.157427 | 0.384811 | 0.577976 | 0.998894 | 1.94374 | 2.65539 |
| tossup | beta_4 | 1350 | 0.697957 | 0.510716 | -1.41866 | 0.152686 | 0.382807 | 0.548157 | 0.895183 | 1.8017 | 3.02251 |
| tossup | beta_5 | 1350 | 0.779716 | 0.559751 | -2.221 | 0.156598 | 0.387715 | 0.632145 | 1.09666 | 1.90373 | 2.68326 |
| tossup | gamma_1 | 1350 | 20.4822 | 98.1996 | 0.116841 | 3.07665 | 4.31349 | 5.14308 | 6.95402 | 40.3618 | 1864.61 |
| tossup | gamma_2 | 1350 | 12.6793 | 65.6127 | 0.097106 | 2.54007 | 3.97834 | 4.80235 | 5.71954 | 24.9189 | 1580.47 |
| tossup | gamma_3 | 1350 | 12.034 | 42.9498 | 0.368694 | 2.98512 | 4.35916 | 5.01447 | 6.05142 | 28.1818 | 718.254 |
| tossup | gamma_4 | 1350 | 15.8868 | 85.3252 | 0.663816 | 2.92744 | 4.31292 | 4.93927 | 5.91037 | 28.5627 | 1884.26 |
| tossup | gamma_5 | 1350 | 22.399 | 116.609 | 0.162751 | 2.96353 | 4.3938 | 5.07148 | 6.34936 | 42.3151 | 2128.99 |
| tossup | mu_1 | 1350 | 0.521512 | 0.139078 | 0.112462 | 0.348316 | 0.438254 | 0.481554 | 0.582784 | 0.810428 | 0.992937 |
| tossup | mu_2 | 1350 | 0.499079 | 0.108082 | 0.132323 | 0.364996 | 0.44296 | 0.482181 | 0.528627 | 0.716222 | 0.975038 |
| tossup | mu_3 | 1350 | 0.499388 | 0.112331 | 0.145048 | 0.362225 | 0.439786 | 0.475076 | 0.527441 | 0.740667 | 0.989573 |
| tossup | mu_4 | 1350 | 0.488733 | 0.0961457 | 0.154248 | 0.370527 | 0.439032 | 0.47286 | 0.516734 | 0.677374 | 0.982051 |
| tossup | mu_5 | 1350 | 0.493045 | 0.10429 | 0.131555 | 0.364357 | 0.438875 | 0.473694 | 0.527756 | 0.696784 | 0.962736 |
| tossup | alpha_1 | 1350 | 1.4303 | 1.08898 | 0.0683255 | 0.254025 | 0.571663 | 1.08185 | 2.03608 | 3.6512 | 6.27357 |
| tossup | alpha_2 | 1350 | 1.06059 | 0.822799 | 0.0690995 | 0.2659 | 0.510901 | 0.822002 | 1.32038 | 2.88197 | 5.89719 |
| tossup | alpha_3 | 1350 | 1.15923 | 1.00123 | 0.0828932 | 0.211272 | 0.4608 | 0.815822 | 1.4445 | 3.40663 | 5.56147 |
| tossup | alpha_4 | 1350 | 0.913998 | 0.637484 | 0.0476436 | 0.220816 | 0.432307 | 0.722821 | 1.24302 | 2.17293 | 4.31607 |
| tossup | alpha_5 | 1350 | 1.06243 | 0.761102 | 0.0787188 | 0.220257 | 0.466521 | 0.803933 | 1.54492 | 2.59794 | 3.70848 |
| tossup | alpha_norm | 1350 | 3.09752 | 0.855912 | 1.00633 | 1.81718 | 2.50313 | 3.02205 | 3.62952 | 4.57913 | 7.92549 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.296982 | 1.49929 | -3.18032 | -2.15509 | -0.996785 | 0.418233 | 1.52162 | 2.54876 | 4.02794 |
| bonus_part | alpha_1 | 4716 | 0.0783721 | 0.569785 | -2.22239 | -0.78933 | -0.273849 | 0.0489192 | 0.4 | 1.00054 | 2.91857 |
| bonus_part | alpha_2 | 4716 | 0.0383152 | 0.56268 | -1.83124 | -0.845849 | -0.355868 | 0.0304573 | 0.425859 | 0.933156 | 2.31772 |
| bonus_part | alpha_3 | 4716 | 0.0605775 | 0.560757 | -1.9426 | -0.790259 | -0.323923 | 0.0370066 | 0.41873 | 1.01799 | 2.82364 |
| bonus_part | alpha_4 | 4716 | 0.0442175 | 0.471715 | -1.88394 | -0.695221 | -0.258422 | 0.0501115 | 0.323847 | 0.819449 | 2.1686 |
| bonus_part | alpha_5 | 4716 | 0.0501694 | 0.491097 | -2.2351 | -0.674547 | -0.268843 | 0.03286 | 0.344681 | 0.830904 | 2.61582 |
| bonus_part | alpha_norm | 4716 | 1.07935 | 0.519539 | 0.0698037 | 0.34075 | 0.672885 | 1.05068 | 1.41191 | 1.99871 | 3.33579 |
| synergy_player | psi_1 | 1755 | -0.00336138 | 0.369018 | -1.61423 | -0.629472 | -0.0735846 | -0.00205332 | 0.0618535 | 0.628754 | 1.82957 |
| synergy_player | psi_2 | 1755 | 0.00152041 | 0.359045 | -1.74331 | -0.590425 | -0.0660573 | -0.00307156 | 0.0646839 | 0.649271 | 1.59936 |
| synergy_player | psi_3 | 1755 | -0.00823482 | 0.392099 | -1.72707 | -0.621779 | -0.0899526 | -0.00442857 | 0.0662185 | 0.704401 | 1.79519 |
| synergy_player | psi_norm | 1755 | 0.517253 | 0.388854 | 0.0176979 | 0.0758672 | 0.210019 | 0.417985 | 0.742741 | 1.32381 | 1.83772 |
| synergy | synergy_score | 3042 | -0.110237 | 0.409737 | -2.62988 | -0.954926 | -0.250054 | 0.00115084 | 0.102898 | 0.371345 | 2.14452 |
| synergy | synergy_contribution | 60454 | -0.391459 | 0.760737 | -2.78552 | -1.65309 | -0.932436 | -0.300501 | 0.0258676 | 0.844283 | 2.2437 |
