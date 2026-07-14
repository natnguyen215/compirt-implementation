# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/baseline-all2024-cal/synergy-evaluation`
Result root: `results/compirt/in_sample/baseline-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 347014 |
| pyramidal | calibrate_correctness | True |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 64005.7 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.590842 |
| mean_synergy_contribution | 0.213586 |
| median_synergy_contribution | 0.0794557 |
| negative_synergy_fraction | 0.366736 |
| positive_synergy_fraction | 0.601861 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.93325 |
| log_loss | 0.337717 |
| ece | 0.0362837 |
| part_accuracy | 0.851859 |
| exact_acc | 0.610043 |
| per_bonus_points_mae | 4.67697 |
| ppb_mae | 1.76554 |
| accuracy | 0.851859 |

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
| accuracy | 0.847439 | 0.851859 | 0.00442077 | synergy |
| part_accuracy | 0.847439 | 0.851859 | 0.00442077 | synergy |
| exact_acc | 0.60067 | 0.610043 | 0.00937352 | synergy |
| per_bonus_points_mae | 4.87996 | 4.67697 | -0.202989 | synergy |
| ppb_mae | 2.27113 | 1.76554 | -0.505585 | synergy |

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
| bonus_part | beta | 3768 | 0.000985469 | 0.96811 | -1.89028 | -1.39673 | -0.873087 | -0.0478619 | 0.813354 | 1.52834 | 2.50294 |
| bonus_part | alpha_1 | 3768 | -0.0395354 | 0.884215 | -2.37468 | -1.3005 | -0.772128 | -0.160647 | 0.657203 | 1.51967 | 1.94634 |
| bonus_part | alpha_2 | 3768 | -0.0449152 | 0.628866 | -2.25466 | -0.925979 | -0.525249 | -0.0967766 | 0.373313 | 1.06999 | 2.0902 |
| bonus_part | alpha_3 | 3768 | -0.0460212 | 0.808611 | -2.13642 | -1.18647 | -0.736977 | -0.12668 | 0.638065 | 1.28522 | 2.06548 |
| bonus_part | alpha_4 | 3768 | -0.0833623 | 0.569951 | -2.49509 | -1.13761 | -0.38954 | -0.0386608 | 0.289775 | 0.743388 | 2.22597 |
| bonus_part | alpha_5 | 3768 | -0.0398683 | 0.612533 | -2.1961 | -1.08813 | -0.466777 | -0.0228788 | 0.447113 | 0.861926 | 1.87756 |
| bonus_part | alpha_norm | 3768 | 1.51258 | 0.506898 | 0.107356 | 0.633466 | 1.17168 | 1.54796 | 1.86374 | 2.32883 | 2.9874 |
| synergy_player | psi_1 | 1455 | 0.0037599 | 0.296572 | -2.19828 | -0.467511 | -0.049417 | 0.000711942 | 0.0545821 | 0.435413 | 1.8178 |
| synergy_player | psi_2 | 1455 | 0.00649771 | 0.291958 | -1.56502 | -0.460268 | -0.0452688 | 0.00185031 | 0.0486294 | 0.51562 | 1.33661 |
| synergy_player | psi_3 | 1455 | -0.00600401 | 0.349807 | -1.89628 | -0.601687 | -0.0654522 | -0.000538473 | 0.056967 | 0.57609 | 1.81123 |
| synergy_player | psi_norm | 1455 | 0.420568 | 0.34446 | 0.0118664 | 0.0503055 | 0.141842 | 0.352822 | 0.56371 | 1.1176 | 2.21471 |
| synergy | synergy_score | 2521 | 0.00252712 | 0.33938 | -4.17165 | -0.546469 | -0.0296493 | 0.0184198 | 0.139231 | 0.387949 | 2.00662 |
| synergy | synergy_contribution | 44487 | 0.213586 | 0.914768 | -4.56551 | -1.28759 | -0.262033 | 0.0794557 | 0.786396 | 1.72244 | 2.58305 |
