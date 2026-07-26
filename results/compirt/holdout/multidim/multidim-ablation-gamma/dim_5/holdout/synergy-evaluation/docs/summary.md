# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-ablation-gamma/dim_5/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-ablation-gamma/dim_5`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 468406 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 85490.2 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.339765 |
| mean_synergy_contribution | -1.18438 |
| median_synergy_contribution | -1.22523 |
| negative_synergy_fraction | 0.930145 |
| positive_synergy_fraction | 0.0454726 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.925931 |
| log_loss | 0.353499 |
| ece | 0.0344169 |
| part_accuracy | 0.84521 |
| part_accuracy_macro_team | 0.847875 |
| part_accuracy_macro_game | 0.84572 |
| part_accuracy_macro_bonus | 0.852858 |
| exact_acc | 0.593278 |
| ppb_mae | 0.904324 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.677357 |
| log_loss | 0.595528 |
| ece | 0.137857 |
| accuracy | 0.706558 |
| buzz_position_mae | 0.135128 |
| buzz_position_median_absolute_error | 0.113222 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 4.90304 | 0.992943 | 1.11833 | 2.79346 | 4.4838 | 5.09401 | 5.58249 | 6.18008 | 7.19794 |
| player | theta_1 | 1755 | 0.174679 | 0.593192 | -2.41398 | -0.885893 | -0.18704 | 0.209181 | 0.557454 | 1.09814 | 1.85198 |
| player | theta_2 | 1755 | 0.13407 | 0.603954 | -1.99 | -1.00975 | -0.202835 | 0.198119 | 0.535307 | 1.00621 | 1.99021 |
| player | theta_3 | 1755 | 0.244691 | 0.57499 | -2.29816 | -0.855212 | -0.0842631 | 0.320527 | 0.663741 | 1.04696 | 1.7247 |
| player | theta_4 | 1755 | -0.105803 | 0.603961 | -2.48432 | -1.16565 | -0.500061 | -0.054524 | 0.313904 | 0.831861 | 1.4718 |
| player | theta_5 | 1755 | 0.0978509 | 0.615196 | -3.83472 | -1.00941 | -0.318089 | 0.176846 | 0.547371 | 1.00424 | 1.57184 |
| player | theta_norm | 1755 | 1.31687 | 0.429604 | 0.238724 | 0.682531 | 1.01274 | 1.27303 | 1.57724 | 2.12281 | 4.20896 |
| tossup | beta_1 | 1350 | 0.766103 | 0.557816 | -1.94205 | 0.144682 | 0.398338 | 0.576021 | 1.01334 | 1.93934 | 2.67587 |
| tossup | beta_2 | 1350 | 0.737527 | 0.473443 | -0.537321 | 0.18009 | 0.415556 | 0.609155 | 1.00102 | 1.69176 | 3.30894 |
| tossup | beta_3 | 1350 | 0.66156 | 0.45992 | -1.98691 | 0.169693 | 0.389114 | 0.545235 | 0.823385 | 1.61233 | 2.69362 |
| tossup | beta_4 | 1350 | 0.841534 | 0.582646 | -0.493063 | 0.121928 | 0.404849 | 0.658681 | 1.23872 | 1.93596 | 3.2172 |
| tossup | beta_5 | 1350 | 0.757107 | 0.54334 | -1.18569 | 0.174711 | 0.380105 | 0.560611 | 1.07606 | 1.89019 | 2.70643 |
| tossup | gamma_1 | 1350 | 12.4946 | 54.7776 | 0.443467 | 3.08219 | 4.27959 | 4.97949 | 6.02538 | 28.3328 | 1231.38 |
| tossup | gamma_2 | 1350 | 16.5686 | 92.5826 | 0.616188 | 2.81567 | 4.25717 | 4.9923 | 6.1531 | 34.5831 | 2103.65 |
| tossup | gamma_3 | 1350 | 13.5617 | 75.1083 | 0.0949182 | 2.92253 | 4.32875 | 4.94204 | 5.78187 | 22.5807 | 1905.87 |
| tossup | gamma_4 | 1350 | 17.2525 | 85.6952 | 1.27101 | 3.01666 | 4.4088 | 5.12274 | 6.83831 | 28.099 | 1812.88 |
| tossup | gamma_5 | 1350 | 20.2969 | 104.236 | 0.621648 | 3.19067 | 4.48723 | 5.12953 | 6.4825 | 47.3409 | 2177.14 |
| tossup | mu_1 | 1350 | 0.502737 | 0.114453 | 0.151971 | 0.368138 | 0.440194 | 0.4762 | 0.532976 | 0.743871 | 0.990529 |
| tossup | mu_2 | 1350 | 0.497316 | 0.108014 | 0.130488 | 0.360039 | 0.440644 | 0.476669 | 0.533732 | 0.712233 | 0.963414 |
| tossup | mu_3 | 1350 | 0.484945 | 0.0942217 | 0.160875 | 0.365771 | 0.442255 | 0.471 | 0.508884 | 0.660992 | 0.957911 |
| tossup | mu_4 | 1350 | 0.515755 | 0.13136 | 0.112079 | 0.36726 | 0.434445 | 0.476482 | 0.574564 | 0.783467 | 0.991784 |
| tossup | mu_5 | 1350 | 0.489784 | 0.105276 | 0.102744 | 0.356385 | 0.435957 | 0.469332 | 0.516563 | 0.699315 | 0.973193 |
| tossup | r_1 | 1350 | 1.18204 | 1.00697 | 0.0703761 | 0.242773 | 0.47423 | 0.804745 | 1.51815 | 3.55569 | 5.48539 |
| tossup | r_2 | 1350 | 1.05229 | 0.754957 | 0.0755473 | 0.250367 | 0.468948 | 0.819768 | 1.46869 | 2.54115 | 4.78564 |
| tossup | r_3 | 1350 | 0.952233 | 0.788021 | 0.0708036 | 0.203609 | 0.418141 | 0.70071 | 1.21976 | 2.61879 | 5.98038 |
| tossup | r_4 | 1350 | 1.39955 | 1.08163 | 0.0714869 | 0.260386 | 0.584466 | 1.02595 | 1.92062 | 3.76791 | 5.55296 |
| tossup | r_5 | 1350 | 1.05456 | 0.779719 | 0.0454112 | 0.208512 | 0.46063 | 0.79371 | 1.52824 | 2.63395 | 3.94359 |
| tossup | r_norm | 1350 | 3.12594 | 0.831246 | 1.05948 | 1.87431 | 2.5663 | 3.0595 | 3.60129 | 4.60334 | 7.44665 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.436973 | 1.43109 | -2.69893 | -1.81801 | -0.804231 | 0.543055 | 1.62081 | 2.55661 | 4.00168 |
| bonus_part | alpha_1 | 4716 | 0.817993 | 0.401161 | 0.240905 | 0.411381 | 0.534377 | 0.72961 | 0.992896 | 1.48694 | 4.10795 |
| bonus_part | alpha_2 | 4716 | 0.777688 | 0.336605 | 0.249949 | 0.410843 | 0.527204 | 0.69387 | 0.960135 | 1.36382 | 3.48623 |
| bonus_part | alpha_3 | 4716 | 0.795693 | 0.375994 | 0.204671 | 0.400261 | 0.520461 | 0.688304 | 1.00578 | 1.47392 | 3.83639 |
| bonus_part | alpha_4 | 4716 | 0.798398 | 0.371798 | 0.230781 | 0.425102 | 0.567286 | 0.739772 | 0.899836 | 1.39923 | 4.61734 |
| bonus_part | alpha_5 | 4716 | 0.781327 | 0.348096 | 0.22358 | 0.415665 | 0.531734 | 0.699679 | 0.953153 | 1.36811 | 4.64573 |
| bonus_part | alpha_norm | 4716 | 1.86224 | 0.601613 | 0.894601 | 1.05301 | 1.37605 | 1.79126 | 2.27696 | 2.93172 | 4.97538 |
