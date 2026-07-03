# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/all2024-cal/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 452590 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 84489.6 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.282681 |
| mean_synergy_contribution | 0.406484 |
| median_synergy_contribution | 0.288789 |
| negative_synergy_fraction | 0.305555 |
| positive_synergy_fraction | 0.670063 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.933332 |
| log_loss | 0.333378 |
| ece | 0.0270304 |
| part_accuracy | 0.854396 |
| exact_score_accuracy | 0.614401 |
| rounded_score_accuracy | 0.614219 |
| per_bonus_points_mae | 4.66279 |
| ppb_mae | 1.67029 |
| accuracy | 0.854396 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.635142 |
| log_loss | 0.518723 |
| ece | 0.00994355 |
| accuracy | 0.771493 |
| buzz_position_mae | 0.136803 |
| buzz_position_median_absolute_error | 0.117623 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.930974 | 0.933332 | 0.00235761 | synergy |
| log_loss | 0.337875 | 0.333378 | -0.0044966 | synergy |
| ece | 0.0254287 | 0.0270304 | 0.00160163 | no-synergy |
| accuracy | 0.850018 | 0.854396 | 0.00437798 | synergy |
| part_accuracy | 0.850018 | 0.854396 | 0.00437798 | synergy |
| exact_score_accuracy | 0.604112 | 0.614401 | 0.0102888 | synergy |
| rounded_score_accuracy | 0.599729 | 0.614219 | 0.0144904 | synergy |
| per_bonus_points_mae | 4.87328 | 4.66279 | -0.210484 | synergy |
| ppb_mae | 2.17029 | 1.67029 | -0.499999 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 1.42025 | 0.576582 | -0.20016 | 0.480651 | 1.01535 | 1.40054 | 1.80957 | 2.41553 | 3.29526 |
| player | theta_1 | 1755 | 0.878495 | 0.603885 | -0.934424 | -0.0613751 | 0.478387 | 0.834358 | 1.28244 | 1.90818 | 3.0142 |
| player | theta_2 | 1755 | -1.01093 | 0.706289 | -2.96099 | -2.20681 | -1.51896 | -0.983505 | -0.505468 | 0.0989285 | 1.30184 |
| player | theta_3 | 1755 | -1.03156 | 0.647703 | -2.77619 | -2.08621 | -1.48352 | -1.07309 | -0.594749 | 0.109161 | 1.30308 |
| player | theta_4 | 1755 | 0.926747 | 0.510787 | -0.911532 | 0.0636299 | 0.603039 | 0.944554 | 1.248 | 1.74332 | 2.75814 |
| player | theta_5 | 1755 | -0.213801 | 0.503719 | -2.4654 | -1.05745 | -0.536663 | -0.207462 | 0.121429 | 0.622596 | 1.40644 |
| player | theta_norm | 1755 | 2.30608 | 0.491111 | 0.747312 | 1.46574 | 1.98077 | 2.33015 | 2.65913 | 3.0839 | 3.67328 |
| tossup | beta | 1350 | 3.77193 | 0.753546 | 0.683273 | 2.51878 | 3.37107 | 3.78024 | 4.22803 | 4.88825 | 7.14195 |
| tossup | gamma | 1350 | 57.6537 | 183.691 | 3.01236 | 6.1152 | 9.24084 | 12.9044 | 25.4617 | 215.352 | 1991.47 |
| tossup | mu | 1350 | 0.636207 | 0.13536 | 0.147297 | 0.415386 | 0.547032 | 0.639521 | 0.723235 | 0.859626 | 0.993534 |
| tossup | alpha_1 | 1350 | -0.822146 | 0.726464 | -2.71412 | -1.89456 | -1.35577 | -0.914887 | -0.329916 | 0.501389 | 1.56648 |
| tossup | alpha_2 | 1350 | 0.995443 | 0.603321 | -0.943596 | 0.0711631 | 0.584511 | 0.999787 | 1.36826 | 2.00769 | 3.1371 |
| tossup | alpha_3 | 1350 | 0.921228 | 0.7253 | -1.19172 | -0.268955 | 0.373472 | 0.959314 | 1.44626 | 2.09522 | 2.92709 |
| tossup | alpha_4 | 1350 | -0.922535 | 0.7273 | -3.02563 | -2.03806 | -1.45949 | -0.950414 | -0.439709 | 0.296907 | 1.90148 |
| tossup | alpha_5 | 1350 | 0.247339 | 0.601635 | -1.38797 | -0.698562 | -0.189196 | 0.215685 | 0.64426 | 1.29244 | 2.21979 |
| tossup | alpha_norm | 1350 | 2.33961 | 0.511063 | 0.754213 | 1.5245 | 1.98003 | 2.34446 | 2.69869 | 3.16002 | 3.89555 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.00112508 | 0.899498 | -1.89482 | -1.29857 | -0.745976 | -0.0561723 | 0.685289 | 1.54758 | 2.21423 |
| bonus_part | alpha_1 | 4716 | -0.0351771 | 0.777417 | -2.09218 | -1.11275 | -0.689227 | -0.150905 | 0.621701 | 1.23267 | 2.21594 |
| bonus_part | alpha_2 | 4716 | 0.0920156 | 0.63927 | -2.09927 | -1.00951 | -0.342515 | 0.13742 | 0.52625 | 1.07048 | 2.17828 |
| bonus_part | alpha_3 | 4716 | 0.105629 | 0.788709 | -2.53343 | -1.22894 | -0.523556 | 0.211296 | 0.722432 | 1.23454 | 2.79729 |
| bonus_part | alpha_4 | 4716 | 0.00636267 | 0.81091 | -2.07162 | -1.18531 | -0.666696 | -0.0441774 | 0.664637 | 1.2662 | 2.49611 |
| bonus_part | alpha_5 | 4716 | -0.000530369 | 0.534122 | -2.18563 | -0.840498 | -0.329212 | -0.033952 | 0.339874 | 0.910133 | 2.00045 |
| bonus_part | alpha_norm | 4716 | 1.51608 | 0.547624 | 0.142082 | 0.531664 | 1.145 | 1.5744 | 1.87837 | 2.37794 | 3.51665 |
| synergy_player | psi_1 | 1755 | -0.00977439 | 0.311553 | -1.71769 | -0.537559 | -0.0539175 | -0.00270004 | 0.0467486 | 0.480984 | 1.70787 |
| synergy_player | psi_2 | 1755 | 0.00142352 | 0.31832 | -1.61272 | -0.526968 | -0.0570412 | -0.000140589 | 0.0588961 | 0.522952 | 1.72479 |
| synergy_player | psi_3 | 1755 | 0.0202593 | 0.292797 | -1.89406 | -0.437156 | -0.0454153 | 0.00508358 | 0.0690286 | 0.522101 | 1.4861 |
| synergy_player | psi_norm | 1755 | 0.424645 | 0.322808 | 0.0134442 | 0.0545332 | 0.168024 | 0.381875 | 0.563519 | 1.09686 | 2.05175 |
| synergy | synergy_score | 3042 | 0.031207 | 0.322207 | -2.93694 | -0.455534 | -0.0162277 | 0.0337031 | 0.170884 | 0.411001 | 1.54585 |
| synergy | synergy_contribution | 60454 | 0.406484 | 0.917201 | -3.64743 | -1.14549 | -0.0773681 | 0.288789 | 1.06177 | 1.78893 | 4.20334 |
