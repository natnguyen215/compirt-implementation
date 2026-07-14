# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim-ablation/dim_4/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/multidim-ablation/dim_4`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 470105 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 4 |
| synergy | steps | 2000 |
| synergy | final_loss | 85361.8 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.270728 |
| mean_synergy_contribution | -0.269537 |
| median_synergy_contribution | -0.211709 |
| negative_synergy_fraction | 0.622043 |
| positive_synergy_fraction | 0.354981 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.932321 |
| log_loss | 0.340167 |
| ece | 0.036134 |
| part_accuracy | 0.85261 |
| exact_score_accuracy | 0.610481 |
| per_bonus_points_mae | 4.73004 |
| ppb_mae | 1.71995 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.670713 |
| log_loss | 0.606065 |
| ece | 0.141933 |
| accuracy | 0.699047 |
| buzz_position_mae | 0.136275 |
| buzz_position_median_absolute_error | 0.114674 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1791 | 4.92067 | 1.06954 | 1.48119 | 2.38008 | 4.50831 | 5.13712 | 5.63255 | 6.25649 | 7.16072 |
| player | theta_1 | 1791 | 0.0191406 | 0.659889 | -3.48607 | -1.18286 | -0.354311 | 0.115625 | 0.467892 | 0.954817 | 1.94501 |
| player | theta_2 | 1791 | 0.090006 | 0.600401 | -1.82244 | -1.1621 | -0.212524 | 0.159948 | 0.477874 | 0.999792 | 1.6528 |
| player | theta_3 | 1791 | 0.172803 | 0.612632 | -1.81506 | -1.07532 | -0.160139 | 0.253005 | 0.6059 | 1.03833 | 1.74922 |
| player | theta_4 | 1791 | 0.192653 | 0.609292 | -2.07615 | -1.01635 | -0.144714 | 0.242847 | 0.590971 | 1.13255 | 1.9561 |
| player | theta_norm | 1791 | 1.17991 | 0.474345 | 0.120309 | 0.5287 | 0.832117 | 1.11423 | 1.44624 | 2.14686 | 3.84944 |
| tossup | beta_1 | 1350 | 0.77586 | 0.53664 | -0.619066 | 0.134773 | 0.398886 | 0.625529 | 1.07424 | 1.88306 | 3.23427 |
| tossup | beta_2 | 1350 | 0.95268 | 0.629733 | -3.26812 | 0.167515 | 0.453893 | 0.812351 | 1.4306 | 2.09938 | 2.79261 |
| tossup | beta_3 | 1350 | 0.850671 | 0.573026 | -1.27784 | 0.187774 | 0.436246 | 0.654472 | 1.24566 | 1.95312 | 2.75074 |
| tossup | beta_4 | 1350 | 0.841357 | 0.596065 | -2.1622 | 0.174513 | 0.427877 | 0.64185 | 1.2332 | 2.02814 | 2.98742 |
| tossup | gamma_1 | 1350 | 22.1995 | 115.104 | 0.486796 | 2.37785 | 4.11064 | 4.94416 | 6.23679 | 50.468 | 2302.24 |
| tossup | gamma_2 | 1350 | 23.9212 | 115.779 | 0.0879938 | 2.85056 | 4.3003 | 5.10867 | 6.98071 | 50.147 | 2108.27 |
| tossup | gamma_3 | 1350 | 18.3334 | 89.6992 | 0.290423 | 2.7292 | 4.29563 | 5.00653 | 6.53462 | 39.3391 | 2080.55 |
| tossup | gamma_4 | 1350 | 15.6357 | 71.1762 | 0.146452 | 2.69445 | 4.22201 | 4.91308 | 6.11828 | 41.6148 | 1332.74 |
| tossup | mu_1 | 1350 | 0.492571 | 0.105827 | 0.0974163 | 0.353516 | 0.436254 | 0.473058 | 0.531884 | 0.697853 | 0.966007 |
| tossup | mu_2 | 1350 | 0.530153 | 0.143001 | 0.112835 | 0.349889 | 0.439623 | 0.486516 | 0.61253 | 0.814779 | 0.991263 |
| tossup | mu_3 | 1350 | 0.501919 | 0.116487 | 0.125434 | 0.345863 | 0.437754 | 0.477936 | 0.552455 | 0.727506 | 0.992263 |
| tossup | mu_4 | 1350 | 0.509778 | 0.124319 | 0.140489 | 0.348405 | 0.441339 | 0.481363 | 0.562332 | 0.774047 | 0.989204 |
| tossup | alpha_1 | 1350 | 1.02539 | 0.598084 | 0.0495709 | 0.231593 | 0.558896 | 0.926109 | 1.38264 | 2.16975 | 3.76845 |
| tossup | alpha_2 | 1350 | 1.57576 | 1.19697 | 0.0961687 | 0.281241 | 0.610147 | 1.22019 | 2.24879 | 3.95325 | 7.22346 |
| tossup | alpha_3 | 1350 | 1.28039 | 0.911358 | 0.120622 | 0.261216 | 0.526693 | 1.0125 | 1.9097 | 3.02456 | 5.33743 |
| tossup | alpha_4 | 1350 | 1.31666 | 1.05239 | 0.103901 | 0.256368 | 0.533293 | 0.959214 | 1.83551 | 3.53774 | 6.00602 |
| tossup | alpha_norm | 1350 | 3.13276 | 0.905331 | 1.09785 | 1.80017 | 2.52871 | 3.06591 | 3.66528 | 4.69199 | 8.60154 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.291225 | 1.48493 | -3.14446 | -2.13944 | -0.979865 | 0.409298 | 1.50395 | 2.5294 | 4.11456 |
| bonus_part | alpha_1 | 4716 | 0.0919816 | 0.464952 | -1.87251 | -0.657286 | -0.188254 | 0.0794159 | 0.357966 | 0.865168 | 2.26751 |
| bonus_part | alpha_2 | 4716 | 0.0921051 | 0.588735 | -2.11968 | -0.796116 | -0.26885 | 0.0560819 | 0.402602 | 1.02735 | 2.93418 |
| bonus_part | alpha_3 | 4716 | 0.0505878 | 0.552985 | -1.67996 | -0.794744 | -0.325251 | 0.0158576 | 0.395244 | 0.988023 | 2.15271 |
| bonus_part | alpha_4 | 4716 | 0.07684 | 0.606987 | -1.74069 | -0.874509 | -0.343076 | 0.0613577 | 0.488149 | 1.07387 | 2.89528 |
| bonus_part | alpha_norm | 4716 | 0.996621 | 0.518616 | 0.0369585 | 0.259839 | 0.582406 | 0.936212 | 1.35943 | 1.90759 | 3.15061 |
