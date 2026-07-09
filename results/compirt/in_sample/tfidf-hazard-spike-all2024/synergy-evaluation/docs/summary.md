# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/tfidf-hazard-spike-all2024/synergy-evaluation`
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
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 66721.7 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.492349 |
| mean_synergy_contribution | -1.0646 |
| median_synergy_contribution | -0.912005 |
| negative_synergy_fraction | 0.8197 |
| positive_synergy_fraction | 0.148897 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.930545 |
| log_loss | 0.343603 |
| ece | 0.0352786 |
| part_accuracy | 0.849087 |
| exact_score_accuracy | 0.604087 |
| rounded_score_accuracy | 0.602131 |
| per_bonus_points_mae | 4.75804 |
| ppb_mae | 1.80026 |
| accuracy | 0.849087 |

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
| bonus_part | beta | 3768 | 0.431235 | 1.51624 | -2.75396 | -2.10075 | -0.848553 | 0.610274 | 1.6828 | 2.67845 | 3.94834 |
| bonus_part | alpha_1 | 3768 | 0.813273 | 0.393608 | 0.183485 | 0.384961 | 0.51971 | 0.714778 | 1.01205 | 1.53416 | 3.77644 |
| bonus_part | alpha_2 | 3768 | 0.77561 | 0.274125 | 0.274546 | 0.441169 | 0.613458 | 0.730394 | 0.857162 | 1.29396 | 3.14125 |
| bonus_part | alpha_3 | 3768 | 0.761541 | 0.28389 | 0.205857 | 0.428613 | 0.568695 | 0.710848 | 0.882616 | 1.30286 | 2.7079 |
| bonus_part | alpha_4 | 3768 | 0.831173 | 0.440102 | 0.179746 | 0.36868 | 0.489684 | 0.726556 | 1.0321 | 1.76773 | 2.97107 |
| bonus_part | alpha_5 | 3768 | 0.778717 | 0.329913 | 0.241045 | 0.41211 | 0.532118 | 0.700328 | 0.958231 | 1.39381 | 2.81379 |
| bonus_part | alpha_norm | 3768 | 1.86886 | 0.510525 | 0.917322 | 1.18509 | 1.44103 | 1.81491 | 2.20762 | 2.79735 | 4.03773 |
| synergy_player | psi_1 | 1455 | -0.00321881 | 0.445078 | -1.82422 | -0.796127 | -0.0703872 | -0.00137179 | 0.0685703 | 0.789515 | 1.74908 |
| synergy_player | psi_2 | 1455 | 0.000374763 | 0.437284 | -1.63992 | -0.763358 | -0.0871466 | 0.00113209 | 0.0734569 | 0.862644 | 1.70486 |
| synergy_player | psi_3 | 1455 | 0.00114286 | 0.422196 | -2.13686 | -0.803394 | -0.0643993 | 0.00114688 | 0.067094 | 0.779611 | 1.95603 |
| synergy_player | psi_norm | 1455 | 0.601415 | 0.453458 | 0.00530823 | 0.0552698 | 0.205033 | 0.518045 | 0.914768 | 1.47191 | 2.26072 |
| synergy | synergy_score | 2521 | -0.164086 | 0.545201 | -3.01196 | -1.2033 | -0.372221 | -0.00133126 | 0.112657 | 0.462581 | 2.55941 |
| synergy | synergy_contribution | 44487 | -1.0646 | 1.08778 | -5.22665 | -3.02256 | -1.78655 | -0.912005 | -0.248306 | 0.531254 | 2.46199 |
