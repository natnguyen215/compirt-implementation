# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/topic-tfidf-ablation/dim_5/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/topic-tfidf-ablation/dim_5`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 508151 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 107863 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.544909 |
| mean_synergy_contribution | -0.0384516 |
| median_synergy_contribution | -0.00146427 |
| negative_synergy_fraction | 0.524696 |
| positive_synergy_fraction | 0.450921 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.921159 |
| log_loss | 0.371735 |
| ece | 0.0556054 |
| part_accuracy | 0.843142 |
| part_accuracy_macro_team | 0.844803 |
| part_accuracy_macro_game | 0.843606 |
| part_accuracy_macro_bonus | 0.839171 |
| exact_acc | 0.58552 |
| ppb_mae | 0.454272 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.649596 |
| log_loss | 0.57448 |
| ece | 0.117244 |
| accuracy | 0.714347 |
| buzz_position_mae | 0.144965 |
| buzz_position_median_absolute_error | 0.126168 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.60368 | 0.483516 | 3.45019 | 4.83725 | 5.28401 | 5.60622 | 5.91818 | 6.41705 | 7.31835 |
| player | theta_1 | 1755 | -0.537119 | 0.672382 | -3.85679 | -1.68032 | -0.855104 | -0.53079 | -0.206692 | 0.560874 | 3.02 |
| player | theta_2 | 1755 | -0.997174 | 1.21033 | -4.649 | -3.33126 | -1.77359 | -0.589675 | -0.385997 | 0.870376 | 3.16443 |
| player | theta_3 | 1755 | -0.987937 | 1.22529 | -3.29766 | -2.5166 | -1.96526 | -1.21346 | -0.282284 | 1.41804 | 3.52149 |
| player | theta_4 | 1755 | -0.888851 | 1.23578 | -3.76624 | -2.8624 | -1.79384 | -0.829993 | -0.187552 | 1.33407 | 3.41184 |
| player | theta_5 | 1755 | -0.835448 | 1.20235 | -4.10642 | -2.55262 | -1.77733 | -0.942006 | -0.0375104 | 1.33404 | 2.81701 |
| player | theta_norm | 1755 | 3.06119 | 0.874032 | 0.781363 | 1.63716 | 2.4109 | 3.0573 | 3.69739 | 4.4559 | 5.71612 |
| tossup | beta_1 | 1350 | 0.654618 | 0.961854 | -2.66708 | -0.049378 | 0.118133 | 0.251762 | 0.641018 | 2.88507 | 5.80338 |
| tossup | beta_2 | 1350 | 0.966869 | 1.21227 | -2.97509 | -0.0186019 | 0.164242 | 0.320425 | 1.71917 | 3.52365 | 4.43273 |
| tossup | beta_3 | 1350 | 0.768816 | 1.12887 | -2.81363 | -0.0342078 | 0.114943 | 0.235403 | 0.719395 | 3.28204 | 4.87306 |
| tossup | beta_4 | 1350 | 0.537487 | 0.920497 | -3.42612 | -0.024067 | 0.118502 | 0.223916 | 0.403531 | 2.91138 | 4.37337 |
| tossup | beta_5 | 1350 | 0.856461 | 1.16529 | -1.60582 | -0.0185544 | 0.120043 | 0.263826 | 1.07398 | 3.38239 | 4.33889 |
| tossup | gamma_1 | 1350 | 17.1605 | 77.8924 | 0.437553 | 4.38713 | 4.8008 | 5.09489 | 5.54496 | 47.9479 | 1542.1 |
| tossup | gamma_2 | 1350 | 26.5204 | 111.512 | 0.894547 | 4.41871 | 4.88861 | 5.20096 | 6.53939 | 117.901 | 1929.53 |
| tossup | gamma_3 | 1350 | 21.5354 | 102.379 | 0.63767 | 4.41105 | 4.82246 | 5.12299 | 5.60674 | 58.3022 | 1897.61 |
| tossup | gamma_4 | 1350 | 23.6504 | 109.433 | 0.897627 | 4.38602 | 4.81282 | 5.07663 | 5.43387 | 41.1807 | 1788.75 |
| tossup | gamma_5 | 1350 | 29.5639 | 130.05 | 0.245076 | 4.35612 | 4.85163 | 5.16234 | 5.90693 | 87.5204 | 1983.34 |
| tossup | mu_1 | 1350 | 0.536671 | 0.102056 | 0.136997 | 0.465803 | 0.488977 | 0.50217 | 0.523058 | 0.805702 | 0.98666 |
| tossup | mu_2 | 1350 | 0.568549 | 0.140538 | 0.192789 | 0.466575 | 0.488214 | 0.505993 | 0.566903 | 0.894306 | 0.990881 |
| tossup | mu_3 | 1350 | 0.543654 | 0.119181 | 0.138868 | 0.467101 | 0.48837 | 0.503118 | 0.524454 | 0.838045 | 0.990915 |
| tossup | mu_4 | 1350 | 0.529543 | 0.103105 | 0.253489 | 0.465316 | 0.48741 | 0.502319 | 0.517464 | 0.803181 | 0.994002 |
| tossup | mu_5 | 1350 | 0.542805 | 0.118498 | 0.158444 | 0.454187 | 0.487325 | 0.50363 | 0.527785 | 0.842112 | 0.991015 |
| tossup | topic_weight_1 | 1350 | 0.165667 | 0.227042 | 0.00606819 | 0.0122121 | 0.0245619 | 0.0529087 | 0.179833 | 0.701108 | 0.879444 |
| tossup | topic_weight_2 | 1350 | 0.245487 | 0.292624 | 0.00596548 | 0.0135669 | 0.0357057 | 0.0830351 | 0.44053 | 0.851918 | 0.935633 |
| tossup | topic_weight_3 | 1350 | 0.207025 | 0.286294 | 0.0056377 | 0.0158677 | 0.0313295 | 0.0612181 | 0.189257 | 0.852584 | 0.951844 |
| tossup | topic_weight_4 | 1350 | 0.149375 | 0.214399 | 0.00812827 | 0.019509 | 0.0339637 | 0.0556319 | 0.142049 | 0.715379 | 0.976542 |
| tossup | topic_weight_5 | 1350 | 0.232446 | 0.276872 | 0.00476933 | 0.0175889 | 0.0359647 | 0.085623 | 0.343218 | 0.818352 | 0.965417 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 4716 | 0.00105709 | 0.983034 | -3.86204 | -2.12374 | -0.252164 | 0.0203644 | 0.271754 | 1.99881 | 3.86122 |
| bonus_part | beta_2 | 4716 | 0.033442 | 0.910675 | -4.1358 | -1.52627 | -0.224602 | 0.011198 | 0.250818 | 1.76548 | 3.99798 |
| bonus_part | beta_3 | 4716 | 0.0577138 | 0.838423 | -4.01405 | -1.1407 | -0.214749 | 0.0170554 | 0.235058 | 1.61759 | 4.08214 |
| bonus_part | beta_4 | 4716 | 0.014187 | 0.682576 | -3.88448 | -0.639286 | -0.207122 | 0.0153455 | 0.226383 | 0.779753 | 4.13702 |
| bonus_part | beta_5 | 4716 | 0.00237076 | 0.821323 | -3.72243 | -1.49659 | -0.219736 | 0.0218662 | 0.234997 | 1.1855 | 4.11301 |
