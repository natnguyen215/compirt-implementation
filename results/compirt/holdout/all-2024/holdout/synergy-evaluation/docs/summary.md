# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/all-2024/holdout/synergy-evaluation`
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
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 85125.8 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.462536 |
| mean_synergy_contribution | -0.521407 |
| median_synergy_contribution | -0.470707 |
| negative_synergy_fraction | 0.754954 |
| positive_synergy_fraction | 0.220664 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.938785 |
| log_loss | 0.325077 |
| ece | 0.0365809 |
| part_accuracy | 0.859629 |
| exact_score_accuracy | 0.627419 |
| rounded_score_accuracy | 0.624955 |
| per_bonus_points_mae | 4.55836 |
| ppb_mae | 1.68455 |
| accuracy | 0.859629 |

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
| bonus_part | beta | 4716 | 0.317671 | 1.44902 | -2.93208 | -1.97693 | -0.939472 | 0.41066 | 1.49811 | 2.52229 | 4.01956 |
| bonus_part | alpha_1 | 4716 | -0.0343641 | 0.49544 | -2.22782 | -0.845384 | -0.319653 | -0.0225099 | 0.272517 | 0.730474 | 2.2014 |
| bonus_part | alpha_2 | 4716 | -0.014975 | 0.55998 | -2.95838 | -0.976943 | -0.302449 | 0.0151734 | 0.327261 | 0.845816 | 2.02291 |
| bonus_part | alpha_3 | 4716 | 0.0827406 | 0.570854 | -2.21484 | -0.836789 | -0.274938 | 0.0899172 | 0.440846 | 1.00704 | 2.42555 |
| bonus_part | alpha_4 | 4716 | -0.0713561 | 0.62721 | -2.48626 | -1.20502 | -0.450002 | -0.0211572 | 0.369714 | 0.856555 | 2.18399 |
| bonus_part | alpha_5 | 4716 | 0.0662449 | 0.570907 | -1.9134 | -0.79298 | -0.334243 | 0.0445043 | 0.426762 | 1.03803 | 2.36332 |
| bonus_part | alpha_norm | 4716 | 1.16537 | 0.513409 | 0.0611312 | 0.388026 | 0.785218 | 1.13647 | 1.49834 | 2.06658 | 3.19526 |
| synergy_player | psi_1 | 1755 | 0.00342931 | 0.350683 | -1.86224 | -0.596026 | -0.046991 | 0.000735611 | 0.0507704 | 0.622828 | 1.6962 |
| synergy_player | psi_2 | 1755 | 0.000306205 | 0.411405 | -1.65356 | -0.723635 | -0.0691618 | -0.00407511 | 0.0666304 | 0.730415 | 1.73404 |
| synergy_player | psi_3 | 1755 | -0.00187911 | 0.36064 | -1.74089 | -0.662442 | -0.0548522 | 0.00320199 | 0.0611994 | 0.565995 | 1.58005 |
| synergy_player | psi_norm | 1755 | 0.515731 | 0.395195 | 0.0073251 | 0.0559387 | 0.184366 | 0.41605 | 0.757499 | 1.30899 | 1.86897 |
| synergy | synergy_score | 3042 | -0.121849 | 0.395534 | -2.76351 | -0.899569 | -0.27683 | -0.00121248 | 0.0837956 | 0.347811 | 1.32295 |
| synergy | synergy_contribution | 60454 | -0.521407 | 0.685133 | -2.76351 | -1.65288 | -1.02214 | -0.470707 | -0.000213304 | 0.515512 | 1.88386 |
