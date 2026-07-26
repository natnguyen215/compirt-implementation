# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/multidim-tanh-all2024/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/multidim-tanh-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 362001 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 64567.3 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.479063 |
| mean_synergy_contribution | -0.434193 |
| median_synergy_contribution | -0.288465 |
| negative_synergy_fraction | 0.663452 |
| positive_synergy_fraction | 0.305145 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.938159 |
| log_loss | 0.328526 |
| ece | 0.0410124 |
| part_accuracy | 0.858288 |
| part_accuracy_macro_team | 0.860849 |
| part_accuracy_macro_game | 0.858615 |
| part_accuracy_macro_bonus | 0.860805 |
| exact_acc | 0.625666 |
| ppb_mae | 0.783493 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.699043 |
| log_loss | 0.572278 |
| ece | 0.11993 |
| accuracy | 0.72123 |
| buzz_position_mae | 0.127577 |
| buzz_position_median_absolute_error | 0.106286 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.934747 | 0.938159 | 0.00341183 | synergy |
| log_loss | 0.341591 | 0.328526 | -0.0130653 | synergy |
| ece | 0.0490555 | 0.0410124 | -0.00804314 | synergy |
| part_accuracy | 0.853598 | 0.858288 | 0.00469051 | synergy |
| part_accuracy_macro_team | 0.855695 | 0.860849 | 0.00515433 | synergy |
| part_accuracy_macro_game | 0.853845 | 0.858615 | 0.00477065 | synergy |
| part_accuracy_macro_bonus | 0.860256 | 0.860805 | 0.000549673 | synergy |
| exact_acc | 0.614494 | 0.625666 | 0.0111718 | synergy |
| ppb_mae | 1.42893 | 0.783493 | -0.645434 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.67276 | 1.25699 | 1.21279 | 2.08823 | 4.05674 | 4.98359 | 5.55004 | 6.28559 | 7.20798 |
| player | theta_1 | 1455 | -0.540541 | 0.724196 | -3.11111 | -1.82467 | -1.01606 | -0.441561 | -0.0101158 | 0.49191 | 1.45236 |
| player | theta_2 | 1455 | -0.497747 | 0.706977 | -2.82118 | -1.68999 | -1.00889 | -0.395544 | 0.00967111 | 0.564349 | 1.57395 |
| player | theta_3 | 1455 | -0.539953 | 0.740563 | -3.1909 | -1.87166 | -1.01532 | -0.4218 | -0.0374277 | 0.567556 | 1.45783 |
| player | theta_4 | 1455 | -0.415678 | 0.76496 | -2.84352 | -1.84335 | -0.884396 | -0.297358 | 0.142033 | 0.64406 | 1.51882 |
| player | theta_5 | 1455 | -0.449403 | 0.703471 | -2.79126 | -1.68 | -0.919187 | -0.389197 | 0.0510936 | 0.600819 | 1.59723 |
| player | theta_norm | 1455 | 1.78135 | 0.827294 | 0.10966 | 0.666412 | 1.11195 | 1.63874 | 2.33978 | 3.27526 | 4.17472 |
| tossup | beta_1 | 1260 | 0.453699 | 0.60861 | -0.393721 | -0.0713201 | 0.0439759 | 0.141568 | 0.914981 | 1.6657 | 2.54297 |
| tossup | beta_2 | 1260 | 0.380517 | 0.571515 | -0.265089 | -0.0574233 | 0.0379817 | 0.113711 | 0.395649 | 1.62633 | 2.8379 |
| tossup | beta_3 | 1260 | 0.424918 | 0.588099 | -0.610124 | -0.0538984 | 0.0459776 | 0.137419 | 0.6876 | 1.66318 | 2.64017 |
| tossup | beta_4 | 1260 | 0.318596 | 0.527489 | -0.353837 | -0.0823687 | 0.0281835 | 0.102304 | 0.287028 | 1.61438 | 2.68784 |
| tossup | beta_5 | 1260 | 0.326592 | 0.534579 | -0.335569 | -0.0712326 | 0.0261105 | 0.104131 | 0.261935 | 1.58353 | 2.40079 |
| tossup | gamma_1 | 1260 | 5.38736 | 25.2729 | 0.865853 | 1.43661 | 2.25575 | 2.83068 | 3.38572 | 7.25076 | 559.546 |
| tossup | gamma_2 | 1260 | 6.19562 | 42.8811 | 0.724418 | 1.30745 | 2.15583 | 2.79325 | 3.47315 | 6.49817 | 979.586 |
| tossup | gamma_3 | 1260 | 5.86678 | 35.0458 | 0.600174 | 1.23682 | 2.05928 | 2.68167 | 3.35783 | 5.87968 | 903.334 |
| tossup | gamma_4 | 1260 | 4.26216 | 25.1607 | 0.534281 | 1.21702 | 2.12154 | 2.73683 | 3.3968 | 4.94628 | 848.556 |
| tossup | gamma_5 | 1260 | 4.85228 | 26.9243 | 0.711002 | 1.48799 | 2.24674 | 2.83369 | 3.42965 | 4.8003 | 781.151 |
| tossup | mu_1 | 1260 | 0.546859 | 0.105874 | 0.107961 | 0.358722 | 0.505999 | 0.541224 | 0.581183 | 0.73221 | 0.992901 |
| tossup | mu_2 | 1260 | 0.557089 | 0.108109 | 0.0705074 | 0.42469 | 0.510911 | 0.54362 | 0.587279 | 0.776836 | 0.992323 |
| tossup | mu_3 | 1260 | 0.556651 | 0.109456 | 0.10133 | 0.40367 | 0.507199 | 0.541462 | 0.592584 | 0.766232 | 0.977602 |
| tossup | mu_4 | 1260 | 0.549841 | 0.0963993 | 0.0605349 | 0.414818 | 0.509576 | 0.542336 | 0.580105 | 0.732298 | 0.984955 |
| tossup | mu_5 | 1260 | 0.554205 | 0.0973658 | 0.107851 | 0.449734 | 0.50865 | 0.537819 | 0.574201 | 0.76838 | 0.986315 |
| tossup | r_1 | 1260 | 1.12322 | 0.86673 | 0.0611027 | 0.202065 | 0.472003 | 0.844257 | 1.56597 | 2.92169 | 4.99665 |
| tossup | r_2 | 1260 | 1.036 | 0.788745 | 0.0406023 | 0.195351 | 0.442934 | 0.793349 | 1.41087 | 2.6361 | 4.73268 |
| tossup | r_3 | 1260 | 1.18033 | 0.897283 | 0.0796728 | 0.218696 | 0.488132 | 0.900846 | 1.61935 | 3.03161 | 4.76217 |
| tossup | r_4 | 1260 | 0.992589 | 0.711347 | 0.0882543 | 0.190244 | 0.432588 | 0.792089 | 1.40687 | 2.36617 | 4.03569 |
| tossup | r_5 | 1260 | 0.941575 | 0.819212 | 0.0930843 | 0.193098 | 0.381798 | 0.657291 | 1.18612 | 2.81153 | 4.6805 |
| tossup | r_norm | 1260 | 2.89792 | 0.745209 | 0.949499 | 1.78645 | 2.34954 | 2.86176 | 3.3726 | 4.17707 | 5.3531 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.247193 | 1.46669 | -2.62973 | -1.97449 | -1.10536 | 0.298776 | 1.51765 | 2.4227 | 3.64331 |
| bonus_part | alpha_1 | 3768 | 0.158881 | 0.585419 | -1.72888 | -0.881177 | -0.239703 | 0.253934 | 0.561863 | 0.995307 | 2.18199 |
| bonus_part | alpha_2 | 3768 | 0.185839 | 0.573385 | -1.65437 | -0.785532 | -0.163268 | 0.191738 | 0.554984 | 1.13714 | 2.43979 |
| bonus_part | alpha_3 | 3768 | 0.197418 | 0.619899 | -1.73635 | -0.826887 | -0.175166 | 0.19941 | 0.555733 | 1.2661 | 2.66549 |
| bonus_part | alpha_4 | 3768 | 0.179094 | 0.530219 | -1.88208 | -0.688079 | -0.13245 | 0.174921 | 0.499192 | 1.07281 | 2.74667 |
| bonus_part | alpha_5 | 3768 | 0.142923 | 0.557952 | -1.98776 | -0.803985 | -0.194039 | 0.172703 | 0.475824 | 1.04018 | 2.40544 |
| bonus_part | alpha_norm | 3768 | 1.23537 | 0.522458 | 0.0298827 | 0.470581 | 0.843422 | 1.20063 | 1.57271 | 2.16173 | 3.1466 |
