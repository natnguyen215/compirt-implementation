# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/baseline-all2024-cal/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/baseline-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 347014 |
| pyramidal | calibrate_correctness | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 63322.7 |
| compositional | calibrate_correctness | True |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.658656 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.930449 |
| log_loss | 0.341971 |
| ece | 0.0328726 |
| part_accuracy | 0.847439 |
| part_accuracy_macro_team | 0.848741 |
| part_accuracy_macro_game | 0.847578 |
| part_accuracy_macro_bonus | 0.853553 |
| exact_acc | 0.60067 |
| ppb_mae | 1.66061 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.669921 |
| log_loss | 0.508854 |
| ece | 0.00660488 |
| accuracy | 0.772259 |
| buzz_position_mae | 0.132791 |
| buzz_position_median_absolute_error | 0.115895 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.930449 | 0.93325 | 0.00280107 | synergy |
| log_loss | 0.341971 | 0.337717 | -0.00425355 | synergy |
| ece | 0.0328726 | 0.0362837 | 0.00341105 | no-synergy |
| part_accuracy | 0.847439 | 0.851859 | 0.00442077 | synergy |
| part_accuracy_macro_team | 0.848741 | 0.853837 | 0.00509561 | synergy |
| part_accuracy_macro_game | 0.847578 | 0.852023 | 0.00444507 | synergy |
| part_accuracy_macro_bonus | 0.853553 | 0.853714 | 0.000160897 | synergy |
| exact_acc | 0.60067 | 0.610043 | 0.00937352 | synergy |
| ppb_mae | 1.66061 | 0.854383 | -0.80623 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 1.57738 | 0.599395 | -0.278617 | 0.589542 | 1.1943 | 1.57184 | 1.9647 | 2.57383 | 3.74996 |
| player | theta_1 | 1455 | 1.089 | 0.580559 | -0.794655 | 0.188721 | 0.688056 | 1.06122 | 1.48932 | 2.02577 | 3.06021 |
| player | theta_2 | 1455 | 0.300159 | 0.781441 | -1.97939 | -0.866688 | -0.227646 | 0.235378 | 0.770649 | 1.69582 | 2.98908 |
| player | theta_3 | 1455 | 0.918615 | 0.555322 | -0.86287 | 0.0225585 | 0.524683 | 0.911856 | 1.30011 | 1.8145 | 2.61268 |
| player | theta_4 | 1455 | 0.399525 | 0.710451 | -1.94213 | -0.806647 | -0.108798 | 0.462471 | 0.912557 | 1.47749 | 2.50414 |
| player | theta_5 | 1455 | 0.313222 | 0.847466 | -2.14711 | -1.09264 | -0.318385 | 0.305325 | 0.956928 | 1.63857 | 2.60296 |
| player | theta_norm | 1455 | 2.14009 | 0.524526 | 0.631199 | 1.30945 | 1.76795 | 2.1157 | 2.50568 | 3.03833 | 3.85282 |
| tossup | beta | 1260 | 3.79948 | 0.688712 | 0.962637 | 2.6977 | 3.40782 | 3.84304 | 4.22017 | 4.85367 | 6.03393 |
| tossup | gamma | 1260 | 41.0739 | 126.291 | 3.10731 | 5.97709 | 8.90061 | 12.4397 | 22.3732 | 129.421 | 1636.65 |
| tossup | mu | 1260 | 0.649152 | 0.135894 | 0.211756 | 0.421645 | 0.553733 | 0.656214 | 0.742297 | 0.870949 | 0.991253 |
| tossup | alpha_1 | 1260 | -1.2224 | 0.619667 | -2.89356 | -2.22299 | -1.64645 | -1.23566 | -0.809071 | -0.16915 | 1.10687 |
| tossup | alpha_2 | 1260 | -0.47286 | 0.792807 | -2.27932 | -1.81029 | -1.11429 | -0.389462 | 0.078973 | 0.761226 | 1.52823 |
| tossup | alpha_3 | 1260 | -0.973046 | 0.593506 | -2.90211 | -2.05799 | -1.35133 | -0.924787 | -0.558056 | -0.0952848 | 0.520645 |
| tossup | alpha_4 | 1260 | -0.290547 | 0.766838 | -2.29717 | -1.53874 | -0.852711 | -0.331661 | 0.304059 | 0.934264 | 1.76428 |
| tossup | alpha_5 | 1260 | -0.139913 | 0.931683 | -2.20646 | -1.62028 | -0.861667 | -0.0991073 | 0.453891 | 1.48115 | 3.03832 |
| tossup | alpha_norm | 1260 | 2.31715 | 0.467227 | 0.771214 | 1.53182 | 2.00327 | 2.33534 | 2.64146 | 3.05761 | 3.78048 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.000566633 | 0.895617 | -1.83057 | -1.29219 | -0.780723 | -0.0709869 | 0.737693 | 1.48919 | 2.16275 |
| bonus_part | alpha_1 | 3768 | -0.206333 | 0.815664 | -2.53596 | -1.38299 | -0.867094 | -0.322074 | 0.418388 | 1.2427 | 1.69654 |
| bonus_part | alpha_2 | 3768 | -0.0970441 | 0.656117 | -2.37846 | -1.07537 | -0.617254 | -0.115128 | 0.360488 | 0.987003 | 2.32558 |
| bonus_part | alpha_3 | 3768 | -0.204875 | 0.751937 | -2.33007 | -1.28326 | -0.83104 | -0.290734 | 0.411048 | 1.05414 | 1.73573 |
| bonus_part | alpha_4 | 3768 | -0.182943 | 0.618104 | -2.59191 | -1.34654 | -0.52104 | -0.119236 | 0.259556 | 0.679694 | 2.05698 |
| bonus_part | alpha_5 | 3768 | -0.102977 | 0.676602 | -2.5086 | -1.30942 | -0.544182 | -0.0722683 | 0.424391 | 0.870676 | 1.8911 |
| bonus_part | alpha_norm | 3768 | 1.55086 | 0.483023 | 0.142545 | 0.697139 | 1.23577 | 1.57904 | 1.88404 | 2.30484 | 3.1618 |
