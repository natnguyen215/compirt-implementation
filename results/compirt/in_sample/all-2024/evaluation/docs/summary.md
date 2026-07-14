# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/all-2024/evaluation`
Result root: `results/compirt/in_sample/all-2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 363263 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 3000 |
| compositional | final_loss | 65784.5 |
| compositional | calibrate_correctness | False |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.175618 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.932678 |
| log_loss | 0.342423 |
| ece | 0.0411874 |
| part_accuracy | 0.852594 |
| exact_acc | 0.612404 |
| per_bonus_points_mae | 4.83864 |
| ppb_mae | 2.19379 |
| accuracy | 0.852594 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.701385 |
| log_loss | 0.579618 |
| ece | 0.149084 |
| accuracy | 0.705952 |
| buzz_position_mae | 0.139008 |
| buzz_position_median_absolute_error | 0.121411 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.932678 | 0.939241 | 0.00656315 | synergy |
| log_loss | 0.342423 | 0.327827 | -0.0145957 | synergy |
| ece | 0.0411874 | 0.0435584 | 0.00237102 | no-synergy |
| accuracy | 0.852594 | 0.859008 | 0.00641386 | synergy |
| part_accuracy | 0.852594 | 0.859008 | 0.00641386 | synergy |
| exact_acc | 0.612404 | 0.627015 | 0.014611 | synergy |
| per_bonus_points_mae | 4.83864 | 4.54743 | -0.291203 | synergy |
| ppb_mae | 2.19379 | 1.74084 | -0.452956 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.74177 | 1.02554 | 1.6814 | 2.6041 | 4.23823 | 4.99168 | 5.45991 | 6.00722 | 6.96045 |
| player | theta_1 | 1455 | 0.0514871 | 0.732826 | -2.27826 | -1.20026 | -0.480844 | 0.0727262 | 0.583654 | 1.1966 | 2.14132 |
| player | theta_2 | 1455 | -0.0977626 | 0.674036 | -2.34346 | -1.32009 | -0.515005 | -0.0656795 | 0.329034 | 1.00376 | 2.29596 |
| player | theta_3 | 1455 | 0.0781982 | 0.921686 | -3.25895 | -1.59361 | -0.487319 | 0.176611 | 0.747129 | 1.41908 | 2.3877 |
| player | theta_4 | 1455 | -0.113105 | 0.920372 | -2.63299 | -1.74513 | -0.743532 | -0.0316682 | 0.548065 | 1.28839 | 2.25273 |
| player | theta_5 | 1455 | -0.225188 | 0.709774 | -2.48771 | -1.4306 | -0.703884 | -0.194578 | 0.251767 | 0.940342 | 1.94621 |
| player | theta_norm | 1455 | 1.7133 | 0.579807 | 0.287633 | 0.872913 | 1.29688 | 1.66393 | 2.06672 | 2.76944 | 3.59256 |
| tossup | beta | 1260 | 3.36358 | 0.696832 | 0.365368 | 2.31451 | 3.00604 | 3.40145 | 3.80782 | 4.39127 | 5.74874 |
| tossup | gamma | 1260 | 51.3308 | 175.047 | 3.69545 | 5.63439 | 9.04839 | 12.8435 | 24.4688 | 180.907 | 2177.92 |
| tossup | mu | 1260 | 0.603627 | 0.133326 | 0.190116 | 0.379104 | 0.509968 | 0.609975 | 0.695831 | 0.818911 | 0.982927 |
| tossup | alpha_1 | 1260 | -0.177434 | 0.691993 | -2.50756 | -1.45001 | -0.622188 | -0.129886 | 0.274663 | 0.91949 | 2.02987 |
| tossup | alpha_2 | 1260 | 0.373332 | 0.643072 | -1.26797 | -0.575345 | -0.0671871 | 0.296642 | 0.75889 | 1.54912 | 3.35572 |
| tossup | alpha_3 | 1260 | 0.536921 | 0.782184 | -1.47804 | -0.610107 | -0.023626 | 0.424004 | 1.09822 | 1.94488 | 2.89414 |
| tossup | alpha_4 | 1260 | 0.721764 | 0.66541 | -1.08011 | -0.358458 | 0.263954 | 0.727278 | 1.18771 | 1.83134 | 2.82093 |
| tossup | alpha_5 | 1260 | 0.333625 | 0.657951 | -1.84656 | -0.685983 | -0.121316 | 0.277397 | 0.793698 | 1.42981 | 2.35236 |
| tossup | alpha_norm | 1260 | 1.80439 | 0.462311 | 0.478711 | 1.04603 | 1.49431 | 1.78086 | 2.11531 | 2.60161 | 3.43933 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.848126 | 1.48751 | -2.26654 | -1.70636 | -0.400696 | 1.11769 | 2.10623 | 2.88737 | 3.76609 |
| bonus_part | alpha_1 | 3768 | -0.0594851 | 0.466306 | -2.30198 | -0.917601 | -0.305228 | -0.0253722 | 0.214588 | 0.650402 | 1.68749 |
| bonus_part | alpha_2 | 3768 | 0.154711 | 0.44882 | -1.50673 | -0.535773 | -0.0907983 | 0.109237 | 0.38802 | 0.926476 | 2.04415 |
| bonus_part | alpha_3 | 3768 | 0.128435 | 0.608996 | -1.68423 | -0.749586 | -0.342946 | 0.0572045 | 0.579638 | 1.15678 | 2.04234 |
| bonus_part | alpha_4 | 3768 | 0.195255 | 0.511859 | -1.70358 | -0.526773 | -0.158699 | 0.128697 | 0.526065 | 1.10995 | 2.22779 |
| bonus_part | alpha_5 | 3768 | 0.130029 | 0.492172 | -1.90903 | -0.618094 | -0.195115 | 0.105318 | 0.40134 | 1.0123 | 2.02069 |
| bonus_part | alpha_norm | 3768 | 1.07102 | 0.495613 | 0.123008 | 0.37017 | 0.692978 | 1.0144 | 1.37367 | 1.99027 | 2.83699 |
