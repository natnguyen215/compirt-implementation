# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/learned-topic-all2024/holdout/evaluation`
Result root: `results/compirt/holdout/learned-topic-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 864247 |
| pyramidal | calibrate_correctness | False |
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 287285 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.0196528 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.911356 |
| log_loss | 0.391726 |
| ece | 0.0588322 |
| part_accuracy | 0.825327 |
| exact_score_accuracy | 0.546217 |
| rounded_score_accuracy | 0.549409 |
| per_bonus_points_mae | 5.25443 |
| ppb_mae | 2.49759 |
| accuracy | 0.825327 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.655846 |
| log_loss | 0.621151 |
| ece | 0.182357 |
| accuracy | 0.673242 |
| buzz_position_mae | 0.153987 |
| buzz_position_median_absolute_error | 0.13584 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.23629 | 0.440824 | 2.93195 | 4.51507 | 4.94068 | 5.24377 | 5.51624 | 5.954 | 6.82571 |
| player | theta_1 | 1755 | 0.146489 | 1.07934 | -2.02056 | -1.21458 | -0.72095 | -0.0532127 | 0.841088 | 2.16917 | 4.16464 |
| player | theta_2 | 1755 | 0.265984 | 1.2592 | -2.63194 | -1.66325 | -0.726491 | 0.228992 | 1.2243 | 2.41667 | 3.75525 |
| player | theta_3 | 1755 | 0.192914 | 0.946263 | -1.77523 | -0.943373 | -0.5328 | -0.00154773 | 0.715071 | 2.12728 | 3.68538 |
| player | theta_4 | 1755 | 0.127773 | 1.29608 | -2.62839 | -1.76812 | -0.892154 | 0.0272263 | 1.01565 | 2.48524 | 4.23494 |
| player | theta_5 | 1755 | 0.231689 | 0.981995 | -2.32973 | -1.2001 | -0.520601 | 0.13961 | 0.951298 | 1.93224 | 3.29833 |
| player | theta_norm | 1755 | 2.3793 | 0.908501 | 0.485058 | 1.1396 | 1.73043 | 2.27073 | 2.86096 | 4.0833 | 6.22037 |
| tossup | beta_1 | 1350 | 0.780095 | 1.35128 | -1.71724 | -0.0641732 | 0.0815123 | 0.179945 | 0.459661 | 4.08221 | 5.33804 |
| tossup | beta_2 | 1350 | 1.26394 | 1.62111 | -3.49582 | -0.0261304 | 0.119439 | 0.298964 | 2.85383 | 4.27264 | 5.43419 |
| tossup | beta_3 | 1350 | 0.530242 | 1.03302 | -3.31052 | -0.0736897 | 0.082952 | 0.167219 | 0.358958 | 3.43165 | 4.84807 |
| tossup | beta_4 | 1350 | 1.34357 | 1.694 | -4.53087 | -0.0561688 | 0.112573 | 0.305737 | 3.13872 | 4.40572 | 5.01199 |
| tossup | beta_5 | 1350 | 0.844467 | 1.33517 | -1.09677 | -0.0347476 | 0.107408 | 0.228499 | 0.634619 | 3.96617 | 5.98727 |
| tossup | gamma_1 | 1350 | 18.6005 | 94.4668 | 3.46855 | 4.60213 | 4.91419 | 5.16777 | 5.57539 | 36.4093 | 1913.28 |
| tossup | gamma_2 | 1350 | 29.0062 | 124.433 | 2.15949 | 4.65835 | 4.98478 | 5.35668 | 9.85381 | 83.137 | 2142.71 |
| tossup | gamma_3 | 1350 | 10.7164 | 39.2901 | 2.2292 | 4.57939 | 4.88402 | 5.12706 | 5.45703 | 20.8629 | 942.148 |
| tossup | gamma_4 | 1350 | 29.5332 | 134.458 | 3.23095 | 4.60823 | 4.97549 | 5.34999 | 9.63264 | 71.8472 | 1835.78 |
| tossup | gamma_5 | 1350 | 21.7017 | 108.858 | 2.75012 | 4.58528 | 4.91892 | 5.21312 | 5.96014 | 49.8456 | 1884.65 |
| tossup | mu_1 | 1350 | 0.516398 | 0.0776779 | 0.17636 | 0.467394 | 0.49054 | 0.501528 | 0.514544 | 0.679179 | 0.9791 |
| tossup | mu_2 | 1350 | 0.525054 | 0.0969192 | 0.126638 | 0.417523 | 0.488726 | 0.50269 | 0.528221 | 0.727937 | 0.968932 |
| tossup | mu_3 | 1350 | 0.509355 | 0.0555292 | 0.264148 | 0.470845 | 0.489899 | 0.499528 | 0.51016 | 0.616471 | 0.876592 |
| tossup | mu_4 | 1350 | 0.549014 | 0.109826 | 0.109662 | 0.463961 | 0.491575 | 0.505369 | 0.573357 | 0.785911 | 0.973232 |
| tossup | mu_5 | 1350 | 0.515072 | 0.0743564 | 0.244853 | 0.451901 | 0.489526 | 0.501141 | 0.514357 | 0.670853 | 0.93184 |
| tossup | topic_weight_1 | 1350 | 0.15643 | 0.268797 | 0.00526258 | 0.0101976 | 0.0167626 | 0.0306401 | 0.0927785 | 0.855054 | 0.95747 |
| tossup | topic_weight_2 | 1350 | 0.26322 | 0.327079 | 0.00392843 | 0.0102042 | 0.0218128 | 0.0648818 | 0.592288 | 0.877438 | 0.965184 |
| tossup | topic_weight_3 | 1350 | 0.116174 | 0.217961 | 0.00601154 | 0.0108751 | 0.0179313 | 0.0305135 | 0.0778281 | 0.765218 | 0.945919 |
| tossup | topic_weight_4 | 1350 | 0.291988 | 0.349923 | 0.00650292 | 0.0144305 | 0.0278399 | 0.0716507 | 0.698184 | 0.906013 | 0.969107 |
| tossup | topic_weight_5 | 1350 | 0.172189 | 0.255816 | 0.00866726 | 0.0142904 | 0.0258256 | 0.0485603 | 0.147294 | 0.799802 | 0.950229 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
