# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/all-2024/holdout/evaluation`
Result root: `results/compirt/holdout/all-2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 473270 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 84856.6 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.225944 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.933456 |
| log_loss | 0.337605 |
| ece | 0.0369495 |
| part_accuracy | 0.853382 |
| exact_score_accuracy | 0.612317 |
| rounded_score_accuracy | 0.606263 |
| per_bonus_points_mae | 4.82446 |
| ppb_mae | 2.07937 |
| accuracy | 0.853382 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.683961 |
| log_loss | 0.59377 |
| ece | 0.152617 |
| accuracy | 0.698538 |
| buzz_position_mae | 0.14333 |
| buzz_position_median_absolute_error | 0.123803 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.933456 | 0.938785 | 0.00532835 | synergy |
| log_loss | 0.337605 | 0.325077 | -0.0125288 | synergy |
| ece | 0.0369495 | 0.0365809 | -0.000368541 | synergy |
| accuracy | 0.853382 | 0.859629 | 0.00624717 | synergy |
| part_accuracy | 0.853382 | 0.859629 | 0.00624717 | synergy |
| exact_score_accuracy | 0.612317 | 0.627419 | 0.0151024 | synergy |
| rounded_score_accuracy | 0.606263 | 0.624955 | 0.0186919 | synergy |
| per_bonus_points_mae | 4.82446 | 4.55836 | -0.266103 | synergy |
| ppb_mae | 2.07937 | 1.68455 | -0.394816 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.02954 | 0.750281 | 1.91432 | 3.59511 | 4.63195 | 5.12291 | 5.52809 | 6.08598 | 6.78704 |
| player | theta_1 | 1755 | -0.00894615 | 0.617894 | -2.2186 | -1.02423 | -0.416152 | 0.00852735 | 0.403921 | 1.01181 | 1.7496 |
| player | theta_2 | 1755 | -0.189964 | 0.696674 | -2.37721 | -1.25526 | -0.644297 | -0.234433 | 0.216569 | 1.05206 | 2.15678 |
| player | theta_3 | 1755 | -0.190527 | 0.653369 | -2.29602 | -1.2363 | -0.626107 | -0.199578 | 0.237987 | 0.902123 | 1.90967 |
| player | theta_4 | 1755 | -0.12823 | 0.825649 | -2.19082 | -1.34017 | -0.726656 | -0.203975 | 0.421888 | 1.38621 | 2.41468 |
| player | theta_5 | 1755 | -0.0154778 | 0.723328 | -2.4256 | -1.26444 | -0.523017 | 0.00529294 | 0.494102 | 1.13366 | 2.17972 |
| player | theta_norm | 1755 | 1.53235 | 0.488573 | 0.186228 | 0.786685 | 1.17426 | 1.49904 | 1.84931 | 2.36708 | 3.14429 |
| tossup | beta | 1350 | 3.33792 | 0.787496 | 0.310577 | 1.94463 | 2.91837 | 3.40392 | 3.82902 | 4.5123 | 5.59115 |
| tossup | gamma | 1350 | 56.3927 | 180.88 | 2.86832 | 5.78514 | 8.96096 | 13.2564 | 26.8537 | 202.841 | 2368.22 |
| tossup | mu | 1350 | 0.588971 | 0.134003 | 0.110499 | 0.361333 | 0.504066 | 0.586532 | 0.675051 | 0.811607 | 0.985809 |
| tossup | alpha_1 | 1350 | -0.376807 | 0.669438 | -2.85083 | -1.67872 | -0.716892 | -0.281759 | 0.0762049 | 0.558784 | 1.27497 |
| tossup | alpha_2 | 1350 | -0.207234 | 0.818979 | -3.48664 | -1.69828 | -0.680498 | -0.0728997 | 0.373642 | 0.869582 | 1.61462 |
| tossup | alpha_3 | 1350 | 0.361942 | 0.843299 | -2.40239 | -1.0149 | -0.162853 | 0.369496 | 0.924689 | 1.77155 | 2.68608 |
| tossup | alpha_4 | 1350 | -0.620754 | 0.670948 | -2.48894 | -1.72991 | -1.08541 | -0.573236 | -0.160893 | 0.447398 | 1.35549 |
| tossup | alpha_5 | 1350 | 0.426415 | 0.607452 | -1.1855 | -0.539707 | 0.00343653 | 0.385906 | 0.840891 | 1.49974 | 2.65721 |
| tossup | alpha_norm | 1350 | 1.80681 | 0.515724 | 0.396905 | 1.01735 | 1.44661 | 1.78258 | 2.13384 | 2.65262 | 3.66209 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.690083 | 1.42894 | -2.61174 | -1.56559 | -0.550595 | 0.795069 | 1.90015 | 2.76719 | 3.98472 |
| bonus_part | alpha_1 | 4716 | -0.12353 | 0.471468 | -2.29023 | -0.945999 | -0.397991 | -0.0846151 | 0.169758 | 0.5827 | 1.95127 |
| bonus_part | alpha_2 | 4716 | 0.0229764 | 0.578709 | -3.01153 | -0.981612 | -0.265881 | 0.0503646 | 0.374357 | 0.916011 | 1.88475 |
| bonus_part | alpha_3 | 4716 | 0.194222 | 0.58855 | -2.18184 | -0.741992 | -0.174613 | 0.16892 | 0.547933 | 1.19959 | 2.63034 |
| bonus_part | alpha_4 | 4716 | -0.115727 | 0.58897 | -2.57713 | -1.12062 | -0.500498 | -0.0646743 | 0.292488 | 0.770805 | 1.92762 |
| bonus_part | alpha_5 | 4716 | 0.111392 | 0.570941 | -1.88103 | -0.788507 | -0.280346 | 0.110099 | 0.478088 | 1.0759 | 2.49905 |
| bonus_part | alpha_norm | 4716 | 1.16822 | 0.53921 | 0.0758809 | 0.371468 | 0.779548 | 1.13216 | 1.48735 | 2.14535 | 3.26725 |
