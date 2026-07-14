# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/tfidf-cumulative-difficulty-all2024/evaluation`
Result root: `results/compirt/in_sample/tfidf-cumulative-difficulty-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 355570 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 66435.4 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.398007 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.919946 |
| log_loss | 0.364257 |
| ece | 0.0284211 |
| part_accuracy | 0.837466 |
| exact_score_accuracy | 0.578821 |
| per_bonus_points_mae | 5.07876 |
| ppb_mae | 2.43547 |
| accuracy | 0.837466 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.697245 |
| log_loss | 0.556327 |
| ece | 0.11076 |
| accuracy | 0.7258 |
| buzz_position_mae | 0.131824 |
| buzz_position_median_absolute_error | 0.114071 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.919946 | 0.93257 | 0.0126244 | synergy |
| log_loss | 0.364257 | 0.339477 | -0.0247804 | synergy |
| ece | 0.0284211 | 0.0355157 | 0.00709462 | no-synergy |
| accuracy | 0.837466 | 0.852047 | 0.014581 | synergy |
| part_accuracy | 0.837466 | 0.852047 | 0.014581 | synergy |
| exact_score_accuracy | 0.578821 | 0.609459 | 0.0306382 | synergy |
| 0.575921 | 0.609189 | 0.0332681 | synergy |
| 5.07876 | 4.70285 | -0.375912 | synergy |
| 2.43547 | 1.68894 | -0.746525 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.90407 | 1.05058 | 1.61619 | 2.75478 | 4.42162 | 5.11142 | 5.61322 | 6.32025 | 7.5698 |
| player | theta_1 | 1455 | 0.0841536 | 0.751135 | -2.07349 | -1.0432 | -0.439118 | 0.0287983 | 0.564598 | 1.3806 | 2.9225 |
| player | theta_2 | 1455 | 0.186445 | 0.811395 | -2.29778 | -1.04133 | -0.350212 | 0.135852 | 0.677447 | 1.64542 | 2.81196 |
| player | theta_3 | 1455 | -0.420727 | 0.76339 | -2.66993 | -1.70937 | -0.94453 | -0.389679 | 0.105386 | 0.784087 | 2.43318 |
| player | theta_4 | 1455 | -0.64613 | 0.902417 | -3.27979 | -2.28307 | -1.25425 | -0.533977 | 0.0336356 | 0.672492 | 1.51622 |
| player | theta_5 | 1455 | -0.432997 | 0.801244 | -2.98507 | -1.87893 | -0.947547 | -0.364853 | 0.0979709 | 0.7865 | 1.71014 |
| player | theta_norm | 1455 | 1.87189 | 0.761367 | 0.378818 | 0.881761 | 1.29319 | 1.73739 | 2.33061 | 3.32547 | 4.21129 |
| tossup | beta | 1260 | 2.53082 | 0.565263 | 0.407286 | 1.61886 | 2.18456 | 2.56353 | 2.89766 | 3.3606 | 4.62115 |
| tossup | gamma | 1260 | 59.334 | 165.319 | 0.546842 | 3.85047 | 7.1265 | 12.1421 | 33.8779 | 261.984 | 2057.43 |
| tossup | mu | 1260 | 0.705289 | 0.158909 | 0.199601 | 0.420405 | 0.605285 | 0.721517 | 0.824235 | 0.939872 | 0.991024 |
| tossup | alpha_1 | 1260 | -0.196315 | 0.748382 | -2.38864 | -1.40332 | -0.707419 | -0.222386 | 0.295458 | 1.08379 | 1.91506 |
| tossup | alpha_2 | 1260 | -0.0645804 | 0.84127 | -2.45226 | -1.58985 | -0.594921 | -0.028233 | 0.516714 | 1.20744 | 2.93755 |
| tossup | alpha_3 | 1260 | 0.485566 | 0.763988 | -1.69108 | -0.722029 | -0.0647877 | 0.448933 | 1.04278 | 1.83119 | 2.46416 |
| tossup | alpha_4 | 1260 | 0.661965 | 0.964054 | -1.95176 | -1.02402 | -0.0240346 | 0.761849 | 1.43833 | 2.02954 | 3.16069 |
| tossup | alpha_5 | 1260 | 0.370026 | 0.869702 | -2.41458 | -1.09005 | -0.217114 | 0.370621 | 0.994549 | 1.75579 | 2.67455 |
| tossup | alpha_norm | 1260 | 2.03562 | 0.494492 | 0.389794 | 1.22012 | 1.69804 | 2.04361 | 2.38136 | 2.81883 | 3.88754 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.480034 | 1.67528 | -2.9836 | -2.33948 | -0.858004 | 0.588272 | 1.92417 | 2.9386 | 3.60408 |
| bonus_part | alpha_1 | 3768 | 0.653952 | 0.364113 | 0.167395 | 0.273684 | 0.375568 | 0.542312 | 0.850339 | 1.36058 | 2.72029 |
| bonus_part | alpha_2 | 3768 | 0.702002 | 0.288493 | 0.144274 | 0.289541 | 0.516381 | 0.678573 | 0.829558 | 1.2492 | 2.43528 |
| bonus_part | alpha_3 | 3768 | 0.711889 | 0.271127 | 0.16067 | 0.358166 | 0.543877 | 0.679315 | 0.816295 | 1.1994 | 2.70588 |
| bonus_part | alpha_4 | 3768 | 0.786066 | 0.419042 | 0.205284 | 0.379764 | 0.501635 | 0.673669 | 0.910607 | 1.67672 | 3.98262 |
| bonus_part | alpha_5 | 3768 | 0.659966 | 0.253048 | 0.148123 | 0.359745 | 0.486404 | 0.614665 | 0.774905 | 1.10027 | 2.59102 |
| bonus_part | alpha_norm | 3768 | 1.68896 | 0.396166 | 0.755802 | 1.17089 | 1.40705 | 1.64063 | 1.89274 | 2.40995 | 4.19176 |
