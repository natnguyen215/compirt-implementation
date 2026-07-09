# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/tfidf-hazard-spike-all2024/evaluation`
Result root: `results/compirt/in_sample/tfidf-hazard-spike-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 363175 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 69160.7 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.140983 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.91835 |
| log_loss | 0.367102 |
| ece | 0.0282857 |
| part_accuracy | 0.835428 |
| exact_score_accuracy | 0.574055 |
| rounded_score_accuracy | 0.570009 |
| per_bonus_points_mae | 5.15446 |
| ppb_mae | 2.51519 |
| accuracy | 0.835428 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.705441 |
| log_loss | 0.576547 |
| ece | 0.148134 |
| accuracy | 0.709521 |
| buzz_position_mae | 0.138866 |
| buzz_position_median_absolute_error | 0.121146 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.91835 | 0.930545 | 0.0121952 | synergy |
| log_loss | 0.367102 | 0.343603 | -0.0234986 | synergy |
| ece | 0.0282857 | 0.0352786 | 0.00699293 | no-synergy |
| accuracy | 0.835428 | 0.849087 | 0.0136594 | synergy |
| part_accuracy | 0.835428 | 0.849087 | 0.0136594 | synergy |
| exact_score_accuracy | 0.574055 | 0.604087 | 0.0300312 | synergy |
| rounded_score_accuracy | 0.570009 | 0.602131 | 0.0321217 | synergy |
| per_bonus_points_mae | 5.15446 | 4.75804 | -0.396421 | synergy |
| ppb_mae | 2.51519 | 1.80026 | -0.714928 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.73411 | 1.03939 | 1.67938 | 2.5435 | 4.25181 | 4.98175 | 5.45931 | 6.05191 | 6.7498 |
| player | theta_1 | 1455 | 0.0549703 | 0.743254 | -2.26986 | -1.10558 | -0.487173 | 0.0312503 | 0.573725 | 1.32228 | 2.59459 |
| player | theta_2 | 1455 | -0.0262613 | 0.815349 | -1.99956 | -1.25437 | -0.570515 | -0.111808 | 0.452546 | 1.4233 | 2.79699 |
| player | theta_3 | 1455 | -0.161154 | 0.717801 | -2.17449 | -1.34808 | -0.661495 | -0.159343 | 0.328706 | 1.0388 | 2.30739 |
| player | theta_4 | 1455 | -0.0776858 | 0.978745 | -2.7664 | -1.89396 | -0.680498 | 0.067465 | 0.609451 | 1.37261 | 2.17908 |
| player | theta_5 | 1455 | -0.0441292 | 0.76142 | -2.26343 | -1.37547 | -0.566853 | 0.0102491 | 0.487981 | 1.13897 | 2.25152 |
| player | theta_norm | 1455 | 1.7207 | 0.58737 | 0.389586 | 0.849039 | 1.30803 | 1.6701 | 2.07262 | 2.81437 | 3.59573 |
| tossup | beta | 1260 | 3.37339 | 0.693225 | 0.445435 | 2.30154 | 3.01451 | 3.40436 | 3.7983 | 4.37095 | 5.84983 |
| tossup | gamma | 1260 | 49.1672 | 167.818 | 3.58762 | 5.78269 | 9.0401 | 12.9574 | 25.2583 | 177.69 | 2305.5 |
| tossup | mu | 1260 | 0.604685 | 0.132983 | 0.203905 | 0.382738 | 0.511759 | 0.609895 | 0.697791 | 0.820036 | 0.98423 |
| tossup | alpha_1 | 1260 | -0.00353127 | 0.72258 | -1.91135 | -1.11448 | -0.494081 | -0.0893882 | 0.470915 | 1.26607 | 2.18981 |
| tossup | alpha_2 | 1260 | -0.291426 | 0.760344 | -2.62239 | -1.6403 | -0.76921 | -0.23997 | 0.233844 | 0.843883 | 1.85958 |
| tossup | alpha_3 | 1260 | 0.264173 | 0.664947 | -2.21067 | -0.78617 | -0.178523 | 0.244898 | 0.730092 | 1.41256 | 2.06207 |
| tossup | alpha_4 | 1260 | 0.880049 | 0.599 | -0.798825 | -0.00562795 | 0.486169 | 0.844475 | 1.26129 | 1.96061 | 2.77234 |
| tossup | alpha_5 | 1260 | 0.333686 | 0.676822 | -1.5273 | -0.841664 | -0.158755 | 0.415911 | 0.846014 | 1.33385 | 2.18049 |
| tossup | alpha_norm | 1260 | 1.7868 | 0.453318 | 0.520204 | 1.05283 | 1.47512 | 1.77202 | 2.08118 | 2.54776 | 3.29087 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 1.02342 | 1.6007 | -2.53083 | -1.76544 | -0.25121 | 1.29273 | 2.3859 | 3.22336 | 3.98641 |
| bonus_part | alpha_1 | 3768 | 0.635994 | 0.32011 | 0.165051 | 0.299806 | 0.388468 | 0.550037 | 0.828829 | 1.20081 | 3.1715 |
| bonus_part | alpha_2 | 3768 | 0.633016 | 0.21991 | 0.16919 | 0.321037 | 0.493041 | 0.614017 | 0.738171 | 1.01796 | 2.61762 |
| bonus_part | alpha_3 | 3768 | 0.630142 | 0.233253 | 0.17367 | 0.350465 | 0.459115 | 0.583498 | 0.769346 | 1.02549 | 2.16337 |
| bonus_part | alpha_4 | 3768 | 0.694558 | 0.369454 | 0.16292 | 0.289782 | 0.395895 | 0.613727 | 0.901068 | 1.37125 | 3.23212 |
| bonus_part | alpha_5 | 3768 | 0.634187 | 0.270962 | 0.18474 | 0.332456 | 0.421901 | 0.557032 | 0.809274 | 1.11571 | 2.54992 |
| bonus_part | alpha_norm | 3768 | 1.51959 | 0.439122 | 0.702258 | 0.936471 | 1.13167 | 1.47198 | 1.87313 | 2.21452 | 3.51989 |
