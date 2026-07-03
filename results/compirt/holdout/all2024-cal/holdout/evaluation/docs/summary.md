# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/all2024-cal/holdout/evaluation`
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
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 83810.6 |
| compositional | calibrate_correctness | True |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.426245 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.930974 |
| log_loss | 0.337875 |
| ece | 0.0254287 |
| part_accuracy | 0.850018 |
| exact_score_accuracy | 0.604112 |
| rounded_score_accuracy | 0.599729 |
| per_bonus_points_mae | 4.87328 |
| ppb_mae | 2.17029 |
| accuracy | 0.850018 |

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
| bonus_part | beta | 4716 | 0.00224543 | 0.829194 | -2.05955 | -1.17047 | -0.687958 | -0.0636266 | 0.618383 | 1.4732 | 2.18226 |
| bonus_part | alpha_1 | 4716 | -0.124266 | 0.736716 | -2.15387 | -1.20152 | -0.738293 | -0.207128 | 0.51921 | 1.02027 | 1.89056 |
| bonus_part | alpha_2 | 4716 | 0.324131 | 0.662954 | -1.51996 | -0.774309 | -0.138503 | 0.327247 | 0.773893 | 1.42429 | 2.77785 |
| bonus_part | alpha_3 | 4716 | 0.251321 | 0.74717 | -1.94942 | -0.963748 | -0.365681 | 0.341173 | 0.811075 | 1.39887 | 2.76678 |
| bonus_part | alpha_4 | 4716 | -0.0914874 | 0.760656 | -2.30796 | -1.22931 | -0.705268 | -0.120374 | 0.546559 | 1.0588 | 2.22782 |
| bonus_part | alpha_5 | 4716 | -0.0693225 | 0.556407 | -2.23435 | -0.979379 | -0.427585 | -0.0841717 | 0.286902 | 0.871113 | 1.83421 |
| bonus_part | alpha_norm | 4716 | 1.53297 | 0.524498 | 0.13462 | 0.633671 | 1.20038 | 1.52358 | 1.88394 | 2.40977 | 3.52984 |
