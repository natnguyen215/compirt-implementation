# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/baseline-ablation-seedcheck/dim_7/seed_1/evaluation`
Result root: `results/compirt/holdout/baseline-ablation-seedcheck/dim_7/seed_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| compositional | tournament | all tournaments |
| compositional | dimensions | 7 |
| compositional | steps | 2000 |
| compositional | final_loss | 93265 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.351073 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.917351 |
| log_loss | 0.366421 |
| ece | 0.0219019 |
| part_accuracy | 0.834436 |
| exact_acc | 0.571062 |
| per_bonus_points_mae | 5.20801 |
| ppb_mae | 2.57948 |
| accuracy | 0.834436 |

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
| bonus_part | beta | 4716 | 0.910371 | 1.65717 | -3.18737 | -1.77478 | -0.449049 | 1.02212 | 2.2702 | 3.41537 | 4.22563 |
| bonus_part | alpha_1 | 4716 | 0.638414 | 0.276332 | 0.117982 | 0.302503 | 0.431227 | 0.572476 | 0.815225 | 1.11965 | 3.02266 |
| bonus_part | alpha_2 | 4716 | 0.643489 | 0.203685 | 0.140253 | 0.337693 | 0.504324 | 0.628701 | 0.764941 | 0.976321 | 2.12943 |
| bonus_part | alpha_3 | 4716 | 0.677502 | 0.24975 | 0.197349 | 0.370882 | 0.509391 | 0.656116 | 0.786718 | 1.08076 | 2.98327 |
| bonus_part | alpha_4 | 4716 | 0.635928 | 0.262064 | 0.161096 | 0.314083 | 0.432416 | 0.591478 | 0.806959 | 1.03539 | 2.98712 |
| bonus_part | alpha_5 | 4716 | 0.742411 | 0.379866 | 0.208888 | 0.28575 | 0.441319 | 0.700814 | 0.933382 | 1.40605 | 3.15289 |
| bonus_part | alpha_6 | 4716 | 0.669625 | 0.246646 | 0.182307 | 0.370823 | 0.481375 | 0.632385 | 0.812524 | 1.0779 | 2.38562 |
| bonus_part | alpha_7 | 4716 | 0.676806 | 0.258265 | 0.11413 | 0.300873 | 0.521555 | 0.645901 | 0.798858 | 1.12335 | 2.51822 |
| bonus_part | alpha_norm | 4716 | 1.86709 | 0.421113 | 0.833856 | 1.21156 | 1.5328 | 1.89059 | 2.16507 | 2.51768 | 3.84289 |
