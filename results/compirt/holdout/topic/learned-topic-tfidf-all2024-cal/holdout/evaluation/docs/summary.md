# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/learned-topic-tfidf-all2024-cal/holdout/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/learned-topic-tfidf-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 844398 |
| pyramidal | calibrate_correctness | True |
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 277424 |
| compositional | calibrate_correctness | True |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.607825 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.91558 |
| log_loss | 0.367053 |
| ece | 0.00921776 |
| part_accuracy | 0.833184 |
| part_accuracy_macro_team | 0.83408 |
| part_accuracy_macro_game | 0.833439 |
| part_accuracy_macro_bonus | 0.842891 |
| exact_acc | 0.563767 |
| ppb_mae | 1.69835 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.583266 |
| log_loss | 0.530726 |
| ece | 0.0102945 |
| accuracy | 0.770352 |
| buzz_position_mae | 0.146027 |
| buzz_position_median_absolute_error | 0.128165 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.91558 | 0.924547 | 0.0089666 | synergy |
| log_loss | 0.367053 | 0.349022 | -0.0180312 | synergy |
| ece | 0.00921776 | 0.0138288 | 0.00461103 | no-synergy |
| part_accuracy | 0.833184 | 0.844003 | 0.0108181 | synergy |
| part_accuracy_macro_team | 0.83408 | 0.84533 | 0.0112493 | synergy |
| part_accuracy_macro_game | 0.833439 | 0.844463 | 0.0110248 | synergy |
| part_accuracy_macro_bonus | 0.842891 | 0.847898 | 0.00500649 | synergy |
| exact_acc | 0.563767 | 0.588084 | 0.024316 | synergy |
| ppb_mae | 1.69835 | 0.445241 | -1.25311 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 3.6758 | 0.643643 | 1.60049 | 2.60353 | 3.24464 | 3.66142 | 4.07062 | 4.78432 | 5.52216 |
| player | theta_1 | 1755 | -1.73696 | 0.878826 | -3.92301 | -2.86522 | -2.31342 | -1.95019 | -1.30947 | 0.0216359 | 2.20433 |
| player | theta_2 | 1755 | -0.901802 | 0.51411 | -3.70166 | -1.6831 | -1.15097 | -0.921137 | -0.652951 | -0.0220287 | 1.16638 |
| player | theta_3 | 1755 | -1.29616 | 0.907753 | -4.12562 | -2.50982 | -1.9382 | -1.45756 | -0.776344 | 0.425754 | 2.44209 |
| player | theta_4 | 1755 | -1.0085 | 0.780487 | -3.61522 | -2.12228 | -1.53374 | -1.13981 | -0.540008 | 0.468862 | 2.03631 |
| player | theta_5 | 1755 | -0.708114 | 0.578875 | -2.79696 | -1.49372 | -1.00486 | -0.780902 | -0.51622 | 0.383765 | 2.79359 |
| player | theta_norm | 1755 | 3.09052 | 0.530054 | 0.72634 | 2.16856 | 2.83807 | 3.11406 | 3.38109 | 3.92722 | 5.62613 |
| tossup | beta_1 | 1350 | 1.82297 | 1.93539 | -0.872754 | 0.0679195 | 0.18942 | 0.556759 | 3.91484 | 5.06517 | 5.68866 |
| tossup | beta_2 | 1350 | 0.907857 | 1.40985 | -0.173978 | 0.0417156 | 0.130115 | 0.24533 | 0.673914 | 4.36723 | 5.44804 |
| tossup | beta_3 | 1350 | 1.10892 | 1.61273 | -0.42256 | 0.0364916 | 0.118926 | 0.222339 | 1.16033 | 4.39622 | 5.59604 |
| tossup | beta_4 | 1350 | 1.01227 | 1.53408 | -0.595056 | 0.0385325 | 0.12473 | 0.225615 | 0.882611 | 4.49688 | 5.48369 |
| tossup | beta_5 | 1350 | 0.578597 | 1.197 | -1.34106 | 0.0384164 | 0.116589 | 0.170631 | 0.296203 | 4.26331 | 5.54842 |
| tossup | gamma_1 | 1350 | 43.8672 | 170.379 | 3.10333 | 4.66773 | 5.0128 | 5.40461 | 10.7245 | 155.377 | 1947.18 |
| tossup | gamma_2 | 1350 | 16.7759 | 81.844 | 3.24385 | 4.59404 | 4.91713 | 5.15375 | 5.62462 | 35.9758 | 1550.7 |
| tossup | gamma_3 | 1350 | 16.6209 | 74.3956 | 3.41419 | 4.61657 | 4.90644 | 5.16364 | 5.88313 | 31.288 | 1162 |
| tossup | gamma_4 | 1350 | 18.5988 | 95.39 | 2.65663 | 4.60541 | 4.9317 | 5.18777 | 5.68762 | 32.957 | 1766.22 |
| tossup | gamma_5 | 1350 | 13.2605 | 75.9201 | 2.86049 | 4.58959 | 4.86133 | 5.07746 | 5.32059 | 11.9556 | 1553.22 |
| tossup | mu_1 | 1350 | 0.616311 | 0.168261 | 0.255063 | 0.477328 | 0.497133 | 0.516058 | 0.772239 | 0.940725 | 0.99438 |
| tossup | mu_2 | 1350 | 0.535543 | 0.0929851 | 0.221122 | 0.476615 | 0.493528 | 0.504682 | 0.52049 | 0.767415 | 0.968247 |
| tossup | mu_3 | 1350 | 0.550627 | 0.111954 | 0.236292 | 0.477034 | 0.494632 | 0.505622 | 0.527995 | 0.820594 | 0.989503 |
| tossup | mu_4 | 1350 | 0.536713 | 0.0983551 | 0.148569 | 0.474395 | 0.492706 | 0.504016 | 0.520675 | 0.782966 | 0.981279 |
| tossup | mu_5 | 1350 | 0.528444 | 0.0930649 | 0.40582 | 0.479699 | 0.493138 | 0.502031 | 0.512826 | 0.812966 | 0.989375 |
| tossup | topic_weight_1 | 1350 | 0.323187 | 0.3532 | 0.00658792 | 0.0124119 | 0.0245599 | 0.0924938 | 0.720232 | 0.901053 | 0.961616 |
| tossup | topic_weight_2 | 1350 | 0.148579 | 0.237523 | 0.00488731 | 0.0100974 | 0.0179893 | 0.0350997 | 0.120353 | 0.753391 | 0.922554 |
| tossup | topic_weight_3 | 1350 | 0.226919 | 0.344195 | 0.00641696 | 0.0104898 | 0.0177957 | 0.0356848 | 0.200506 | 0.935162 | 0.965502 |
| tossup | topic_weight_4 | 1350 | 0.195911 | 0.296337 | 0.00520239 | 0.0118473 | 0.0221702 | 0.0428036 | 0.164413 | 0.872426 | 0.967524 |
| tossup | topic_weight_5 | 1350 | 0.105405 | 0.220789 | 0.0069937 | 0.0118763 | 0.0188924 | 0.0278067 | 0.0529407 | 0.809484 | 0.963849 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 4716 | -0.055241 | 0.82963 | -3.37526 | -1.6872 | -0.2831 | -0.027323 | 0.239646 | 1.32775 | 2.9352 |
| bonus_part | beta_2 | 4716 | -0.00840336 | 0.640309 | -2.75767 | -1.226 | -0.201012 | 0.0091691 | 0.19669 | 1.08145 | 2.71173 |
| bonus_part | beta_3 | 4716 | 0.0291372 | 0.70843 | -2.96797 | -1.23144 | -0.16217 | -0.00456521 | 0.158491 | 1.41336 | 2.99089 |
| bonus_part | beta_4 | 4716 | -0.0070015 | 0.614508 | -2.81821 | -1.16594 | -0.179633 | 0.000799762 | 0.176869 | 0.972134 | 2.70969 |
| bonus_part | beta_5 | 4716 | 0.0389469 | 0.489783 | -2.63076 | -0.563519 | -0.130289 | 0.022721 | 0.16242 | 0.777671 | 2.86681 |
