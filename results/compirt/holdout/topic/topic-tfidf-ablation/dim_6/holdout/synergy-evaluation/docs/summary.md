# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/topic-tfidf-ablation/dim_6/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/topic-tfidf-ablation/dim_6`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 509468 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 6 |
| synergy | steps | 2000 |
| synergy | final_loss | 109436 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.509053 |
| mean_synergy_contribution | -0.0468788 |
| median_synergy_contribution | -0.00189258 |
| negative_synergy_fraction | 0.534109 |
| positive_synergy_fraction | 0.441509 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.920773 |
| log_loss | 0.374212 |
| ece | 0.0600861 |
| part_accuracy | 0.844245 |
| part_accuracy_macro_team | 0.845793 |
| part_accuracy_macro_game | 0.844685 |
| part_accuracy_macro_bonus | 0.835178 |
| exact_acc | 0.5881 |
| ppb_mae | 0.461421 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.651008 |
| log_loss | 0.568014 |
| ece | 0.109955 |
| accuracy | 0.718419 |
| buzz_position_mae | 0.145372 |
| buzz_position_median_absolute_error | 0.127095 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.68354 | 0.473728 | 3.69425 | 4.92462 | 5.36799 | 5.67963 | 6.00044 | 6.48849 | 7.23801 |
| player | theta_1 | 1755 | -1.04253 | 1.30697 | -3.92145 | -3.04577 | -1.94256 | -1.17123 | -0.27709 | 1.35667 | 3.51728 |
| player | theta_2 | 1755 | -1.00792 | 1.1782 | -4.21671 | -2.71744 | -1.9133 | -1.11755 | -0.210636 | 1.07616 | 2.48717 |
| player | theta_3 | 1755 | -0.613323 | 0.82027 | -3.16197 | -2.0648 | -1.15162 | -0.406744 | -0.292852 | 0.85425 | 3.22485 |
| player | theta_4 | 1755 | -0.614336 | 0.975091 | -3.53612 | -2.27965 | -1.25061 | -0.404226 | -0.192479 | 0.937223 | 3.74378 |
| player | theta_5 | 1755 | -0.453271 | 0.618365 | -3.66953 | -1.63479 | -0.617725 | -0.310235 | -0.188957 | 0.251607 | 2.51127 |
| player | theta_6 | 1755 | -0.933758 | 1.20982 | -3.30331 | -2.43189 | -1.87168 | -1.18467 | -0.231799 | 1.44725 | 3.75332 |
| player | theta_norm | 1755 | 3.12958 | 0.837918 | 0.866282 | 1.70997 | 2.52378 | 3.1439 | 3.7209 | 4.49306 | 6.17665 |
| tossup | beta_1 | 1350 | 0.712604 | 1.1187 | -3.29326 | -0.00399484 | 0.154499 | 0.260388 | 0.537689 | 3.56605 | 5.04528 |
| tossup | beta_2 | 1350 | 1.01765 | 1.24365 | -1.99265 | 0.00471174 | 0.145085 | 0.329975 | 2.03353 | 3.47325 | 4.60177 |
| tossup | beta_3 | 1350 | 0.483483 | 0.816018 | -2.81694 | -0.0247772 | 0.12041 | 0.228722 | 0.406586 | 2.59685 | 5.76732 |
| tossup | beta_4 | 1350 | 0.611871 | 1.00722 | -2.00734 | -0.0432096 | 0.129002 | 0.240978 | 0.478484 | 3.27017 | 4.57215 |
| tossup | beta_5 | 1350 | 0.494991 | 0.816565 | -0.78641 | -0.060386 | 0.0841097 | 0.195766 | 0.443115 | 2.67322 | 3.99148 |
| tossup | beta_6 | 1350 | 0.764321 | 1.1643 | -2.9927 | -0.0412097 | 0.122348 | 0.226233 | 0.630197 | 3.3876 | 5.47765 |
| tossup | gamma_1 | 1350 | 28.0157 | 122.31 | 0.369191 | 4.39435 | 4.82295 | 5.12594 | 5.55854 | 99.7355 | 1755.27 |
| tossup | gamma_2 | 1350 | 37.4443 | 148.351 | 0.40515 | 4.35498 | 4.87938 | 5.25053 | 7.49842 | 153.863 | 2184.79 |
| tossup | gamma_3 | 1350 | 10.7818 | 62.1152 | 2.81097 | 4.43156 | 4.8075 | 5.04646 | 5.37874 | 13.137 | 1830.58 |
| tossup | gamma_4 | 1350 | 14.5192 | 81.3136 | 1.29431 | 4.4183 | 4.85958 | 5.12197 | 5.49348 | 21.5641 | 1810.48 |
| tossup | gamma_5 | 1350 | 9.728 | 32.2937 | 1.84537 | 4.42278 | 4.80959 | 5.07788 | 5.4045 | 23.7603 | 856.122 |
| tossup | gamma_6 | 1350 | 19.8307 | 90.7087 | 1.12201 | 4.41437 | 4.83255 | 5.14517 | 5.61822 | 50.6798 | 1602.51 |
| tossup | mu_1 | 1350 | 0.543597 | 0.124978 | 0.262589 | 0.462307 | 0.488833 | 0.502707 | 0.521958 | 0.89628 | 0.994084 |
| tossup | mu_2 | 1350 | 0.555653 | 0.12774 | 0.141809 | 0.453856 | 0.488822 | 0.506583 | 0.555859 | 0.855941 | 0.988894 |
| tossup | mu_3 | 1350 | 0.51922 | 0.0753012 | 0.246567 | 0.470294 | 0.488754 | 0.501043 | 0.515256 | 0.684736 | 0.988799 |
| tossup | mu_4 | 1350 | 0.535213 | 0.103953 | 0.29197 | 0.47188 | 0.490402 | 0.502722 | 0.519011 | 0.82774 | 0.989114 |
| tossup | mu_5 | 1350 | 0.524374 | 0.0837403 | 0.299331 | 0.468047 | 0.488853 | 0.501456 | 0.518803 | 0.727011 | 0.968511 |
| tossup | mu_6 | 1350 | 0.544164 | 0.120535 | 0.137018 | 0.46724 | 0.48735 | 0.502296 | 0.523588 | 0.843757 | 0.991417 |
| tossup | topic_weight_1 | 1350 | 0.159171 | 0.239454 | 0.00572814 | 0.017354 | 0.0272405 | 0.0437241 | 0.132316 | 0.76842 | 0.952306 |
| tossup | topic_weight_2 | 1350 | 0.238714 | 0.27561 | 0.00629716 | 0.0137 | 0.0274474 | 0.0812129 | 0.502472 | 0.763489 | 0.939943 |
| tossup | topic_weight_3 | 1350 | 0.104526 | 0.156345 | 0.00632574 | 0.0148483 | 0.0285294 | 0.0446843 | 0.0881784 | 0.555052 | 0.809268 |
| tossup | topic_weight_4 | 1350 | 0.14936 | 0.230645 | 0.00641227 | 0.0151612 | 0.0314653 | 0.0544744 | 0.114528 | 0.777719 | 0.911077 |
| tossup | topic_weight_5 | 1350 | 0.142886 | 0.193865 | 0.00683643 | 0.0156509 | 0.0306099 | 0.0577556 | 0.142608 | 0.643079 | 0.829056 |
| tossup | topic_weight_6 | 1350 | 0.205343 | 0.283932 | 0.00938332 | 0.0198824 | 0.0344558 | 0.0602358 | 0.169005 | 0.842235 | 0.95351 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 4716 | 0.0237921 | 0.796625 | -4.11669 | -0.940137 | -0.209504 | 0.020074 | 0.238561 | 1.10478 | 4.13412 |
| bonus_part | beta_2 | 4716 | -0.00393671 | 1.00433 | -3.9554 | -2.06233 | -0.248464 | 0.0145099 | 0.257008 | 1.98475 | 4.01623 |
| bonus_part | beta_3 | 4716 | 0.0141892 | 0.587903 | -3.81756 | -0.488347 | -0.200576 | 0.022936 | 0.214212 | 0.52363 | 4.00733 |
| bonus_part | beta_4 | 4716 | 0.0179592 | 0.649789 | -3.6239 | -0.562327 | -0.203594 | 0.0197195 | 0.225189 | 0.665712 | 3.85305 |
| bonus_part | beta_5 | 4716 | 0.00335802 | 0.783748 | -3.8532 | -1.21136 | -0.210812 | 0.0123969 | 0.228088 | 1.23166 | 3.76079 |
| bonus_part | beta_6 | 4716 | 0.0580098 | 0.842036 | -3.93194 | -1.11001 | -0.205509 | 0.0178583 | 0.226469 | 1.61549 | 4.19556 |
