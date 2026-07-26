# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/multidim-tanh-all2024-cal/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/multidim-tanh-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 343157 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 64476.7 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.347761 |
| mean_synergy_contribution | 0.506001 |
| median_synergy_contribution | 0.306758 |
| negative_synergy_fraction | 0.327534 |
| positive_synergy_fraction | 0.641064 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.930311 |
| log_loss | 0.34214 |
| ece | 0.0309183 |
| part_accuracy | 0.849709 |
| part_accuracy_macro_team | 0.851072 |
| part_accuracy_macro_game | 0.84989 |
| part_accuracy_macro_bonus | 0.851735 |
| exact_acc | 0.605368 |
| ppb_mae | 0.788364 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.659738 |
| log_loss | 0.514427 |
| ece | 0.0145269 |
| accuracy | 0.770526 |
| buzz_position_mae | 0.123381 |
| buzz_position_median_absolute_error | 0.10022 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.927551 | 0.930311 | 0.00276002 | synergy |
| log_loss | 0.349442 | 0.34214 | -0.00730175 | synergy |
| ece | 0.0352078 | 0.0309183 | -0.0042895 | synergy |
| part_accuracy | 0.844404 | 0.849709 | 0.00530492 | synergy |
| part_accuracy_macro_team | 0.845488 | 0.851072 | 0.0055843 | synergy |
| part_accuracy_macro_game | 0.844588 | 0.84989 | 0.00530237 | synergy |
| part_accuracy_macro_bonus | 0.850389 | 0.851735 | 0.0013461 | synergy |
| exact_acc | 0.592937 | 0.605368 | 0.0124306 | synergy |
| ppb_mae | 1.82848 | 0.788364 | -1.04011 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 1.38352 | 0.612092 | -1.02111 | 0.36005 | 1.02585 | 1.38642 | 1.761 | 2.32901 | 4.34025 |
| player | theta_1 | 1455 | -1.12521 | 0.730334 | -3.33825 | -2.28511 | -1.64811 | -1.12922 | -0.616304 | 0.10452 | 0.907898 |
| player | theta_2 | 1455 | -0.843057 | 0.679291 | -3.30288 | -1.94736 | -1.30634 | -0.840299 | -0.384247 | 0.294608 | 1.16841 |
| player | theta_3 | 1455 | -1.08523 | 0.712061 | -3.7797 | -2.27494 | -1.55224 | -1.077 | -0.636857 | 0.0973109 | 1.30644 |
| player | theta_4 | 1455 | -1.09164 | 0.68199 | -3.71689 | -2.16238 | -1.55626 | -1.12393 | -0.658965 | 0.0778421 | 1.02086 |
| player | theta_5 | 1455 | -1.03168 | 0.72378 | -4.40706 | -2.12483 | -1.53282 | -1.05977 | -0.542243 | 0.200759 | 1.24499 |
| player | theta_norm | 1455 | 2.7579 | 0.542128 | 1.02858 | 1.88973 | 2.3846 | 2.75713 | 3.1436 | 3.62857 | 4.55405 |
| tossup | beta_1 | 1260 | 0.499279 | 0.596363 | -0.22127 | -0.0427873 | 0.0818206 | 0.219766 | 0.890016 | 1.61857 | 4.31151 |
| tossup | beta_2 | 1260 | 0.361412 | 0.511958 | -0.269756 | -0.0307758 | 0.0660369 | 0.158429 | 0.350908 | 1.57144 | 2.63508 |
| tossup | beta_3 | 1260 | 0.373218 | 0.527759 | -0.26936 | -0.0349737 | 0.0703347 | 0.16284 | 0.372704 | 1.62496 | 3.13169 |
| tossup | beta_4 | 1260 | 0.500867 | 0.583881 | -0.13446 | -0.017876 | 0.0862708 | 0.211532 | 0.950231 | 1.67235 | 2.80886 |
| tossup | beta_5 | 1260 | 0.420714 | 0.537955 | -0.207989 | -0.0373782 | 0.0820578 | 0.185758 | 0.471537 | 1.60516 | 2.42888 |
| tossup | gamma_1 | 1260 | 5.64079 | 27.292 | 0.72439 | 1.50529 | 2.24287 | 2.87199 | 3.53828 | 8.52696 | 701.925 |
| tossup | gamma_2 | 1260 | 5.097 | 29.0235 | 0.525699 | 1.28633 | 1.96934 | 2.63703 | 3.30252 | 5.42752 | 741.284 |
| tossup | gamma_3 | 1260 | 6.03809 | 35.6361 | 0.947872 | 1.41861 | 2.06129 | 2.67719 | 3.47416 | 6.82039 | 792.833 |
| tossup | gamma_4 | 1260 | 5.02394 | 23.6688 | 0.702207 | 1.334 | 2.10476 | 2.66378 | 3.27596 | 6.23899 | 446.26 |
| tossup | gamma_5 | 1260 | 4.30211 | 14.2592 | 0.879418 | 1.5754 | 2.23814 | 2.75621 | 3.35809 | 6.91104 | 354.27 |
| tossup | mu_1 | 1260 | 0.573941 | 0.103852 | 0.214196 | 0.431564 | 0.515181 | 0.557658 | 0.615856 | 0.768093 | 0.99281 |
| tossup | mu_2 | 1260 | 0.578227 | 0.0950812 | 0.0868188 | 0.470338 | 0.526911 | 0.561866 | 0.609039 | 0.756074 | 0.992446 |
| tossup | mu_3 | 1260 | 0.580096 | 0.097791 | 0.207111 | 0.46747 | 0.521499 | 0.561882 | 0.6158 | 0.769167 | 0.992316 |
| tossup | mu_4 | 1260 | 0.583892 | 0.0992329 | 0.134403 | 0.459159 | 0.525779 | 0.566348 | 0.627946 | 0.763663 | 0.993764 |
| tossup | mu_5 | 1260 | 0.573493 | 0.095133 | 0.150938 | 0.461747 | 0.521596 | 0.55598 | 0.604586 | 0.756805 | 0.991151 |
| tossup | r_1 | 1260 | 1.13137 | 0.647575 | 0.080724 | 0.287824 | 0.634482 | 0.985349 | 1.51234 | 2.33856 | 3.46335 |
| tossup | r_2 | 1260 | 1.10939 | 0.677084 | 0.120813 | 0.282036 | 0.585112 | 0.97957 | 1.45304 | 2.48881 | 3.56011 |
| tossup | r_3 | 1260 | 0.996173 | 0.538068 | 0.0750428 | 0.223829 | 0.604468 | 0.936548 | 1.33156 | 2.00371 | 3.0914 |
| tossup | r_4 | 1260 | 1.24599 | 0.732248 | 0.140518 | 0.370513 | 0.689091 | 1.05815 | 1.69173 | 2.69989 | 3.95994 |
| tossup | r_5 | 1260 | 1.10529 | 0.767557 | 0.0938216 | 0.316655 | 0.59775 | 0.867329 | 1.34122 | 2.76132 | 4.15284 |
| tossup | r_norm | 1260 | 2.8711 | 0.570206 | 1.61356 | 2.04425 | 2.46557 | 2.81818 | 3.20292 | 3.88722 | 5.09038 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.000776488 | 0.744374 | -1.43256 | -1.04092 | -0.662748 | -0.0500363 | 0.632048 | 1.22317 | 1.98463 |
| bonus_part | alpha_1 | 3768 | 0.0149546 | 0.825119 | -2.13232 | -1.32323 | -0.692174 | 0.0925882 | 0.729041 | 1.15028 | 2.31224 |
| bonus_part | alpha_2 | 3768 | 0.0583542 | 0.632293 | -1.69353 | -1.02982 | -0.394908 | 0.115268 | 0.506315 | 1.02638 | 2.56335 |
| bonus_part | alpha_3 | 3768 | 0.0155307 | 0.820566 | -2.08729 | -1.30062 | -0.693833 | 0.073017 | 0.720888 | 1.178 | 2.09093 |
| bonus_part | alpha_4 | 3768 | 0.0825662 | 0.75118 | -2.02152 | -1.1628 | -0.549924 | 0.175769 | 0.687255 | 1.1766 | 2.43731 |
| bonus_part | alpha_5 | 3768 | 0.0444289 | 0.766776 | -2.15358 | -1.19444 | -0.584459 | 0.0993194 | 0.68021 | 1.14759 | 2.35445 |
| bonus_part | alpha_norm | 3768 | 1.61691 | 0.551114 | 0.128478 | 0.663623 | 1.23819 | 1.65136 | 2.00293 | 2.50445 | 2.97882 |
