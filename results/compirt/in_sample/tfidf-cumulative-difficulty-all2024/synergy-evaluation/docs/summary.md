# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/tfidf-cumulative-difficulty-all2024/synergy-evaluation`
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
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 64590.1 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.711671 |
| mean_synergy_contribution | -0.5144 |
| median_synergy_contribution | -0.25219 |
| negative_synergy_fraction | 0.647762 |
| positive_synergy_fraction | 0.320835 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.93257 |
| log_loss | 0.339477 |
| ece | 0.0355157 |
| part_accuracy | 0.852047 |
| exact_score_accuracy | 0.609459 |
| rounded_score_accuracy | 0.609189 |
| per_bonus_points_mae | 4.70285 |
| ppb_mae | 1.68894 |
| accuracy | 0.852047 |

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
| rounded_score_accuracy | 0.575921 | 0.609189 | 0.0332681 | synergy |
| per_bonus_points_mae | 5.07876 | 4.70285 | -0.375912 | synergy |
| ppb_mae | 2.43547 | 1.68894 | -0.746525 | synergy |

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
| bonus_part | beta | 3768 | 0.22355 | 1.53843 | -2.94317 | -2.23188 | -1.11837 | 0.344183 | 1.52203 | 2.52974 | 3.77793 |
| bonus_part | alpha_1 | 3768 | 0.846428 | 0.454131 | 0.186501 | 0.379561 | 0.507461 | 0.719893 | 1.06448 | 1.78165 | 3.09195 |
| bonus_part | alpha_2 | 3768 | 0.779601 | 0.304833 | 0.211211 | 0.390642 | 0.585058 | 0.735432 | 0.89486 | 1.40398 | 2.63851 |
| bonus_part | alpha_3 | 3768 | 0.806762 | 0.306547 | 0.239395 | 0.454454 | 0.6128 | 0.749355 | 0.912238 | 1.43085 | 3.08414 |
| bonus_part | alpha_4 | 3768 | 0.885342 | 0.433802 | 0.247018 | 0.440593 | 0.58096 | 0.766195 | 1.04664 | 1.76964 | 3.86265 |
| bonus_part | alpha_5 | 3768 | 0.807714 | 0.312931 | 0.197293 | 0.467978 | 0.597518 | 0.732736 | 0.937224 | 1.40045 | 3.18124 |
| bonus_part | alpha_norm | 3768 | 1.96951 | 0.459851 | 0.976147 | 1.39802 | 1.63084 | 1.87617 | 2.2061 | 2.87092 | 4.25472 |
| synergy_player | psi_1 | 1455 | 4.06735e-05 | 0.36933 | -1.73914 | -0.615235 | -0.0669843 | 0.00174924 | 0.0712339 | 0.551436 | 1.67512 |
| synergy_player | psi_2 | 1455 | 0.0029528 | 0.346425 | -1.54854 | -0.564676 | -0.0632575 | 0.000256897 | 0.0665194 | 0.611703 | 1.8982 |
| synergy_player | psi_3 | 1455 | -0.00545275 | 0.319366 | -1.90747 | -0.53795 | -0.0557915 | 0.000129738 | 0.0491737 | 0.49324 | 1.71025 |
| synergy_player | psi_norm | 1455 | 0.455419 | 0.388457 | 0.00602842 | 0.0474421 | 0.143064 | 0.354823 | 0.643781 | 1.27755 | 2.1584 |
| synergy | synergy_score | 2521 | -0.0651696 | 0.409481 | -3.02016 | -0.853429 | -0.121911 | 0.00234404 | 0.100198 | 0.426519 | 1.74703 |
| synergy | synergy_contribution | 44487 | -0.5144 | 1.08159 | -4.91353 | -2.69957 | -1.0853 | -0.25219 | 0.0331263 | 1.09813 | 3.17518 |
