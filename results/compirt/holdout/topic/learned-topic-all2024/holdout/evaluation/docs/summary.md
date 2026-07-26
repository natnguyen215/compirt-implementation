# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/learned-topic-all2024/holdout/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/learned-topic-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

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
| part_accuracy_macro_team | 0.82751 |
| part_accuracy_macro_game | 0.825644 |
| part_accuracy_macro_bonus | 0.803847 |
| exact_acc | 0.546217 |
| ppb_mae | 1.78588 |

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

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.911356 | 0.91787 | 0.00651385 | synergy |
| log_loss | 0.391726 | 0.376906 | -0.0148195 | synergy |
| ece | 0.0588322 | 0.0526634 | -0.00616874 | synergy |
| part_accuracy | 0.825327 | 0.838494 | 0.013167 | synergy |
| part_accuracy_macro_team | 0.82751 | 0.840145 | 0.0126353 | synergy |
| part_accuracy_macro_game | 0.825644 | 0.838911 | 0.0132673 | synergy |
| part_accuracy_macro_bonus | 0.803847 | 0.830824 | 0.0269773 | synergy |
| exact_acc | 0.546217 | 0.576157 | 0.0299401 | synergy |
| ppb_mae | 1.78588 | 0.607208 | -1.17868 | synergy |

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

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 4716 | 0.280351 | 0.894439 | -3.11172 | -0.363949 | -0.0458302 | 0.0885206 | 0.245469 | 2.43078 | 4.87615 |
| bonus_part | beta_2 | 4716 | 0.367313 | 1.10822 | -2.98643 | -1.02532 | -0.0669855 | 0.112533 | 0.427255 | 3.08108 | 4.81007 |
| bonus_part | beta_3 | 4716 | 0.221531 | 0.757919 | -3.28063 | -0.375487 | -0.053795 | 0.0903514 | 0.250615 | 1.6938 | 4.72892 |
| bonus_part | beta_4 | 4716 | 0.441169 | 1.19224 | -3.16393 | -0.8807 | -0.0593822 | 0.109279 | 0.436093 | 3.42571 | 5.19399 |
| bonus_part | beta_5 | 4716 | 0.279916 | 0.938102 | -3.25386 | -0.700573 | -0.0568359 | 0.101168 | 0.296095 | 2.45547 | 4.69937 |
