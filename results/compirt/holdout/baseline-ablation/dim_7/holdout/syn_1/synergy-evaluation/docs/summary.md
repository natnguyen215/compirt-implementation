# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation/dim_7/holdout/syn_1/synergy-evaluation`
Result root: `results/compirt/holdout/baseline-ablation/dim_7/holdout/syn_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 7 |
| synergy | steps | 2000 |
| synergy | final_loss | 83739 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.765611 |
| mean_synergy_contribution | -0.832627 |
| median_synergy_contribution | -0.802838 |
| negative_synergy_fraction | 0.868313 |
| positive_synergy_fraction | 0.107305 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.942626 |
| log_loss | 0.317774 |
| ece | 0.0411269 |
| part_accuracy | 0.8634 |
| exact_acc | 0.636352 |
| per_bonus_points_mae | 4.48115 |
| ppb_mae | 1.70479 |
| accuracy | 0.8634 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.698773 |
| log_loss | 0.579549 |
| ece | 0.148371 |
| accuracy | 0.70918 |
| buzz_position_mae | 0.139389 |
| buzz_position_median_absolute_error | 0.12024 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.97763 | 0.788943 | 1.41706 | 3.42919 | 4.59586 | 5.10415 | 5.50939 | 6.01006 | 6.84309 |
| player | theta_1 | 1755 | 0.129129 | 0.607466 | -2.02225 | -0.830599 | -0.302987 | 0.104717 | 0.54316 | 1.14284 | 2.05443 |
| player | theta_2 | 1755 | -0.0137497 | 0.669607 | -2.34223 | -1.17005 | -0.454241 | 0.0291656 | 0.467623 | 0.976233 | 2.37503 |
| player | theta_3 | 1755 | -0.129576 | 0.532882 | -1.8298 | -1.01849 | -0.483912 | -0.137088 | 0.184758 | 0.780748 | 1.77171 |
| player | theta_4 | 1755 | 0.020704 | 0.563131 | -2.05047 | -0.864429 | -0.361323 | 0.00152606 | 0.400704 | 0.970721 | 1.89817 |
| player | theta_5 | 1755 | -0.105566 | 0.797472 | -3.31846 | -1.4104 | -0.619027 | -0.0772511 | 0.44448 | 1.13877 | 1.90915 |
| player | theta_6 | 1755 | -0.10218 | 0.59059 | -2.45924 | -1.07707 | -0.479774 | -0.116375 | 0.285875 | 0.889562 | 1.9694 |
| player | theta_7 | 1755 | -0.248763 | 0.770819 | -1.88863 | -1.258 | -0.770316 | -0.359385 | 0.117705 | 1.19762 | 3.03528 |
| player | theta_norm | 1755 | 1.70311 | 0.461267 | 0.488363 | 1.00959 | 1.38621 | 1.67501 | 1.96959 | 2.48622 | 3.529 |
| tossup | beta | 1350 | 3.39963 | 0.770761 | 0.525 | 2.10196 | 3.00956 | 3.45698 | 3.90795 | 4.5233 | 5.3913 |
| tossup | gamma | 1350 | 54.562 | 173.157 | 2.76185 | 5.76981 | 9.0915 | 13.0837 | 26.0892 | 210.225 | 1986.05 |
| tossup | mu | 1350 | 0.592279 | 0.131817 | 0.111726 | 0.373684 | 0.508377 | 0.589419 | 0.67775 | 0.808419 | 0.985612 |
| tossup | alpha_1 | 1350 | 0.166195 | 0.622456 | -1.36267 | -0.761955 | -0.301742 | 0.102231 | 0.600452 | 1.23409 | 1.99416 |
| tossup | alpha_2 | 1350 | -0.257287 | 0.685831 | -2.51793 | -1.68729 | -0.53906 | -0.074998 | 0.206882 | 0.612185 | 1.26123 |
| tossup | alpha_3 | 1350 | 0.195438 | 0.63269 | -1.71461 | -0.736645 | -0.229016 | 0.145605 | 0.555217 | 1.40988 | 2.11886 |
| tossup | alpha_4 | 1350 | 0.0285311 | 0.672938 | -1.89068 | -1.02828 | -0.447795 | -0.00172256 | 0.522615 | 1.16308 | 1.99111 |
| tossup | alpha_5 | 1350 | 0.799991 | 0.678814 | -1.25262 | -0.266344 | 0.337664 | 0.78392 | 1.2662 | 1.92082 | 3.11506 |
| tossup | alpha_6 | 1350 | 0.337837 | 0.528001 | -1.46245 | -0.472316 | -0.0188781 | 0.30743 | 0.659711 | 1.24209 | 2.23091 |
| tossup | alpha_7 | 1350 | -0.244687 | 0.836173 | -3.61279 | -1.87318 | -0.679228 | -0.0789842 | 0.33047 | 0.862375 | 1.64521 |
| tossup | alpha_norm | 1350 | 1.96637 | 0.47723 | 0.587106 | 1.21862 | 1.6398 | 1.95573 | 2.27173 | 2.75822 | 3.84364 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.296483 | 1.4573 | -2.86755 | -2.03295 | -0.968294 | 0.381018 | 1.50035 | 2.54559 | 3.94897 |
| bonus_part | alpha_1 | 4716 | -0.0206467 | 0.479301 | -2.44662 | -0.810772 | -0.286701 | -0.022089 | 0.242886 | 0.758462 | 2.12476 |
| bonus_part | alpha_2 | 4716 | -0.0196601 | 0.52197 | -2.89888 | -0.919962 | -0.314869 | -0.00259044 | 0.328892 | 0.749386 | 2.04079 |
| bonus_part | alpha_3 | 4716 | 0.0536655 | 0.471453 | -1.67422 | -0.664866 | -0.236256 | 0.035071 | 0.325234 | 0.848913 | 2.17763 |
| bonus_part | alpha_4 | 4716 | -0.0118623 | 0.458606 | -2.43038 | -0.747833 | -0.268673 | -0.0101175 | 0.22443 | 0.735945 | 2.48979 |
| bonus_part | alpha_5 | 4716 | 0.118367 | 0.661052 | -1.88241 | -1.01055 | -0.365695 | 0.114252 | 0.576038 | 1.17768 | 2.12107 |
| bonus_part | alpha_6 | 4716 | 0.0410472 | 0.444801 | -1.72229 | -0.628349 | -0.254509 | 0.0225267 | 0.324127 | 0.769649 | 2.10294 |
| bonus_part | alpha_7 | 4716 | -0.01761 | 0.586654 | -2.30964 | -1.05105 | -0.384532 | 0.0195487 | 0.383712 | 0.888985 | 1.827 |
| bonus_part | alpha_norm | 4716 | 1.29685 | 0.501443 | 0.170898 | 0.54713 | 0.944245 | 1.26874 | 1.58326 | 2.21802 | 3.4357 |
