# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation-rotcheck/dim_7/rot_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/baseline-ablation-rotcheck/dim_7/rot_2`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| compositional | tournament | all tournaments |
| compositional | dimensions | 7 |
| compositional | steps | 2000 |
| compositional | final_loss | 97982.4 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.18444 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.907651 |
| log_loss | 0.38363 |
| ece | 0.0145036 |
| part_accuracy | 0.824644 |
| exact_acc | 0.549459 |
| per_bonus_points_mae | 5.49525 |
| ppb_mae | 3.00965 |
| accuracy | 0.824644 |

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
| bonus_part | beta | 4716 | 1.04108 | 1.55112 | -2.26091 | -1.3648 | -0.360455 | 1.16505 | 2.37727 | 3.30122 | 4.50929 |
| bonus_part | alpha_1 | 4716 | 0.680844 | 0.275057 | 0.152064 | 0.354559 | 0.497877 | 0.646121 | 0.803596 | 1.10831 | 4.04863 |
| bonus_part | alpha_2 | 4716 | 0.630429 | 0.199146 | 0.152735 | 0.332171 | 0.489596 | 0.618092 | 0.758812 | 0.938179 | 2.04138 |
| bonus_part | alpha_3 | 4716 | 0.664027 | 0.337584 | 0.150626 | 0.286597 | 0.421198 | 0.579036 | 0.846927 | 1.25222 | 3.20052 |
| bonus_part | alpha_4 | 4716 | 0.559416 | 0.242467 | 0.123897 | 0.229685 | 0.377631 | 0.533385 | 0.704504 | 0.974907 | 2.15551 |
| bonus_part | alpha_5 | 4716 | 0.687078 | 0.257935 | 0.103471 | 0.343564 | 0.507592 | 0.650156 | 0.825392 | 1.14027 | 2.56588 |
| bonus_part | alpha_6 | 4716 | 0.56457 | 0.234764 | 0.121057 | 0.241952 | 0.386854 | 0.537385 | 0.71114 | 0.960005 | 2.47866 |
| bonus_part | alpha_7 | 4716 | 0.710139 | 0.358175 | 0.155834 | 0.291238 | 0.428965 | 0.631272 | 0.906991 | 1.36977 | 2.76368 |
| bonus_part | alpha_norm | 4716 | 1.80109 | 0.451657 | 0.856097 | 1.15017 | 1.42419 | 1.75691 | 2.17336 | 2.51155 | 4.47735 |
