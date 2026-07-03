# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/baseline-all2024-cal/evaluation`
Result root: `results/compirt/in_sample/baseline-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 346864 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 63026.5 |
| compositional | calibrate_correctness | True |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.681262 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.929964 |
| log_loss | 0.342806 |
| ece | 0.0330169 |
| part_accuracy | 0.84624 |
| exact_score_accuracy | 0.597613 |
| rounded_score_accuracy | 0.597298 |
| per_bonus_points_mae | 4.89124 |
| ppb_mae | 2.29036 |
| accuracy | 0.84624 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.66977 |
| log_loss | 0.509218 |
| ece | 0.0101085 |
| accuracy | 0.771403 |
| buzz_position_mae | 0.133244 |
| buzz_position_median_absolute_error | 0.116404 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.929964 | 0.932743 | 0.00277858 | synergy |
| log_loss | 0.342806 | 0.338007 | -0.00479888 | synergy |
| ece | 0.0330169 | 0.0341318 | 0.00111496 | no-synergy |
| accuracy | 0.84624 | 0.851312 | 0.00507264 | synergy |
| part_accuracy | 0.84624 | 0.851312 | 0.00507264 | synergy |
| exact_score_accuracy | 0.597613 | 0.608875 | 0.0112617 | synergy |
| rounded_score_accuracy | 0.597298 | 0.61146 | 0.0141614 | synergy |
| per_bonus_points_mae | 4.89124 | 4.6849 | -0.206348 | synergy |
| ppb_mae | 2.29036 | 1.75832 | -0.532043 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 1.60879 | 0.596111 | -0.391714 | 0.649845 | 1.20395 | 1.609 | 1.99589 | 2.57987 | 3.81619 |
| player | theta_1 | 1455 | 0.604982 | 0.656343 | -1.44435 | -0.446744 | 0.165445 | 0.607679 | 1.06488 | 1.63855 | 2.84822 |
| player | theta_2 | 1455 | -0.425241 | 0.856557 | -2.67143 | -1.7953 | -1.08775 | -0.401059 | 0.221326 | 0.906277 | 2.07711 |
| player | theta_3 | 1455 | 0.45729 | 0.763405 | -2.09589 | -0.767627 | -0.0920463 | 0.464981 | 0.991111 | 1.71102 | 2.68981 |
| player | theta_4 | 1455 | 0.207569 | 0.711046 | -1.87423 | -0.922547 | -0.279996 | 0.184997 | 0.672946 | 1.38439 | 2.49554 |
| player | theta_5 | 1455 | 1.22275 | 0.565894 | -0.493397 | 0.334383 | 0.827708 | 1.20021 | 1.56425 | 2.21518 | 3.37986 |
| player | theta_norm | 1455 | 2.14225 | 0.525743 | 0.791608 | 1.29952 | 1.76403 | 2.13502 | 2.49677 | 3.04903 | 3.63338 |
| tossup | beta | 1260 | 3.7874 | 0.707123 | 0.898327 | 2.70097 | 3.4049 | 3.80865 | 4.19945 | 4.89598 | 5.95994 |
| tossup | gamma | 1260 | 41.7267 | 129.17 | 3.03802 | 5.94437 | 8.99519 | 12.5536 | 22.9688 | 135.107 | 1677.6 |
| tossup | mu | 1260 | 0.648127 | 0.138061 | 0.209926 | 0.422182 | 0.551218 | 0.655692 | 0.744534 | 0.870731 | 0.990467 |
| tossup | alpha_1 | 1260 | -0.653563 | 0.661461 | -2.92097 | -1.9179 | -1.00873 | -0.592427 | -0.206361 | 0.323839 | 0.846712 |
| tossup | alpha_2 | 1260 | 0.304085 | 0.98388 | -2.34984 | -1.30487 | -0.385297 | 0.225912 | 1.14147 | 1.83255 | 2.45642 |
| tossup | alpha_3 | 1260 | -0.558967 | 0.757229 | -3.04098 | -2.00932 | -1.02433 | -0.445834 | -0.0224442 | 0.517366 | 1.22124 |
| tossup | alpha_4 | 1260 | -0.0732343 | 0.755902 | -2.42679 | -1.48084 | -0.508085 | -0.0942141 | 0.405917 | 1.24764 | 1.91389 |
| tossup | alpha_5 | 1260 | -1.2795 | 0.613705 | -2.92922 | -2.25714 | -1.70787 | -1.29177 | -0.875311 | -0.215527 | 1.07547 |
| tossup | alpha_norm | 1260 | 2.27692 | 0.463675 | 0.810602 | 1.47511 | 1.97258 | 2.28944 | 2.59563 | 3.05082 | 3.59691 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.000911676 | 0.879596 | -1.90682 | -1.2817 | -0.763337 | -0.088663 | 0.709327 | 1.46485 | 2.2182 |
| bonus_part | alpha_1 | 3768 | -0.1813 | 0.675763 | -2.47429 | -1.19379 | -0.704065 | -0.18547 | 0.346149 | 0.878922 | 1.73877 |
| bonus_part | alpha_2 | 3768 | 0.0841611 | 0.654411 | -2.10793 | -0.839569 | -0.363107 | -0.00128856 | 0.463397 | 1.30616 | 2.61344 |
| bonus_part | alpha_3 | 3768 | -0.20105 | 0.655562 | -2.63406 | -1.24958 | -0.653943 | -0.218197 | 0.268641 | 0.829163 | 1.90065 |
| bonus_part | alpha_4 | 3768 | -0.0644909 | 0.550915 | -2.513 | -1.0306 | -0.381056 | -0.0140685 | 0.294054 | 0.759251 | 1.94067 |
| bonus_part | alpha_5 | 3768 | -0.197644 | 0.914312 | -2.14565 | -1.45817 | -0.972695 | -0.307937 | 0.514255 | 1.36264 | 1.97838 |
| bonus_part | alpha_norm | 3768 | 1.53127 | 0.482031 | 0.237284 | 0.673595 | 1.22284 | 1.55609 | 1.85796 | 2.2906 | 3.31359 |
