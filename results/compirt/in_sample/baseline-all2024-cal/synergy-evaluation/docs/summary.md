# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/baseline-all2024-cal/synergy-evaluation`
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
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 63653.1 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.634799 |
| mean_synergy_contribution | 0.219967 |
| median_synergy_contribution | 0.0838857 |
| negative_synergy_fraction | 0.38155 |
| positive_synergy_fraction | 0.587048 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.932743 |
| log_loss | 0.338007 |
| ece | 0.0341318 |
| part_accuracy | 0.851312 |
| exact_score_accuracy | 0.608875 |
| rounded_score_accuracy | 0.61146 |
| per_bonus_points_mae | 4.6849 |
| ppb_mae | 1.75832 |
| accuracy | 0.851312 |

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
| bonus_part | beta | 3768 | -0.00323239 | 0.953364 | -1.83277 | -1.39296 | -0.859021 | -0.0612753 | 0.784013 | 1.51334 | 2.49802 |
| bonus_part | alpha_1 | 3768 | -0.0458557 | 0.683675 | -2.16928 | -1.03655 | -0.608489 | -0.0620129 | 0.490143 | 1.07904 | 1.77641 |
| bonus_part | alpha_2 | 3768 | 0.0290897 | 0.579774 | -1.72074 | -0.904198 | -0.338082 | -0.018654 | 0.379209 | 1.0622 | 2.28109 |
| bonus_part | alpha_3 | 3768 | -0.0963823 | 0.624703 | -2.56081 | -1.05902 | -0.543858 | -0.140111 | 0.346081 | 0.923258 | 1.88607 |
| bonus_part | alpha_4 | 3768 | -0.0378504 | 0.504396 | -2.42602 | -0.892031 | -0.342556 | 0.00316788 | 0.268086 | 0.745302 | 2.02025 |
| bonus_part | alpha_5 | 3768 | -0.0183324 | 1.01127 | -2.15315 | -1.42538 | -0.890951 | -0.135601 | 0.815295 | 1.6552 | 2.17515 |
| bonus_part | alpha_norm | 3768 | 1.49357 | 0.503535 | 0.10045 | 0.619293 | 1.15361 | 1.52452 | 1.82968 | 2.29828 | 3.17756 |
| synergy_player | psi_1 | 1455 | 0.000722949 | 0.328985 | -1.49307 | -0.559106 | -0.0542784 | 0.000515957 | 0.0549436 | 0.519967 | 2.13942 |
| synergy_player | psi_2 | 1455 | -0.00359513 | 0.308186 | -1.90411 | -0.488786 | -0.060386 | -0.00247032 | 0.0524522 | 0.500279 | 1.64654 |
| synergy_player | psi_3 | 1455 | 0.00746313 | 0.305823 | -1.42114 | -0.496564 | -0.0611891 | 0.00323265 | 0.0633479 | 0.549057 | 1.63924 |
| synergy_player | psi_norm | 1455 | 0.424041 | 0.341867 | 0.00822514 | 0.0451279 | 0.155597 | 0.355533 | 0.581623 | 1.12272 | 2.2158 |
| synergy | synergy_score | 2521 | 0.00316987 | 0.338457 | -2.8739 | -0.546591 | -0.0325563 | 0.0230424 | 0.140067 | 0.393829 | 1.74017 |
| synergy | synergy_contribution | 44487 | 0.219967 | 0.906652 | -4.39305 | -1.25696 | -0.281853 | 0.0838857 | 0.824002 | 1.72305 | 2.61044 |
