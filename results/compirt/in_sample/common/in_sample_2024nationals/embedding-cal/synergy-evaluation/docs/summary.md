# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/embedding-cal/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/in_sample/in_sample_2024nationals/embedding-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | 2024-acf-nationals |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 60709.1 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | 2024-acf-nationals |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 10036.5 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.910802 |
| mean_synergy_contribution | 0.264154 |
| median_synergy_contribution | 0.319123 |
| negative_synergy_fraction | 0.0716831 |
| positive_synergy_fraction | 0.927462 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.925021 |
| log_loss | 0.345709 |
| ece | 0.0159843 |
| part_accuracy | 0.848178 |
| part_accuracy_macro_team | 0.849112 |
| part_accuracy_macro_game | 0.848666 |
| part_accuracy_macro_bonus | 0.850375 |
| exact_acc | 0.596979 |
| ppb_mae | 0.384742 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.600806 |
| log_loss | 0.573481 |
| ece | 0.0235287 |
| accuracy | 0.727834 |
| buzz_position_mae | 0.14368 |
| buzz_position_median_absolute_error | 0.134398 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 189 | 3.35639 | 0.56816 | 1.82253 | 2.52829 | 2.96948 | 3.35162 | 3.67228 | 4.27931 | 5.2867 |
| player | theta_1 | 189 | -1.20088 | 0.612603 | -2.61644 | -2.0949 | -1.63838 | -1.19308 | -0.912884 | -0.0550921 | 1.02893 |
| player | theta_2 | 189 | -0.00478165 | 0.0510886 | -0.12309 | -0.0925139 | -0.040352 | -0.00623001 | 0.0231151 | 0.0851259 | 0.116647 |
| player | theta_3 | 189 | -0.11124 | 0.494054 | -1.06248 | -0.691532 | -0.418272 | -0.238136 | 0.122084 | 0.764511 | 1.70737 |
| player | theta_4 | 189 | -1.10682 | 0.728711 | -2.56209 | -2.28434 | -1.62795 | -1.16335 | -0.597521 | 0.116387 | 0.946407 |
| player | theta_5 | 189 | -1.25919 | 0.601267 | -2.5915 | -2.27625 | -1.65137 | -1.22995 | -0.858344 | -0.32681 | 0.734455 |
| player | theta_norm | 189 | 2.33507 | 0.566362 | 0.715754 | 1.40301 | 1.92557 | 2.34737 | 2.75911 | 3.17541 | 3.69572 |
| tossup | beta_1 | 360 | 1.41031 | 1.75286 | -0.118551 | -0.0609348 | -0.0126209 | 0.0421386 | 3.48253 | 3.83373 | 4.44505 |
| tossup | beta_2 | 360 | 0.00208351 | 0.0482022 | -0.15868 | -0.0728459 | -0.030258 | 0.00298169 | 0.0322154 | 0.0835686 | 0.160628 |
| tossup | beta_3 | 360 | 0.0527991 | 0.494134 | -0.144986 | -0.0819524 | -0.0297531 | 0.0028063 | 0.031248 | 0.080579 | 4.97267 |
| tossup | beta_4 | 360 | 0.853295 | 1.58655 | -0.182184 | -0.0668045 | -0.0218604 | 0.0185979 | 0.127582 | 4.09773 | 4.48586 |
| tossup | beta_5 | 360 | 1.35088 | 1.74629 | -0.0884812 | -0.0631297 | 0.000428088 | 0.0611119 | 3.49731 | 3.94891 | 4.26614 |
| tossup | gamma_1 | 360 | 17.5157 | 49.2062 | 4.38136 | 4.62169 | 4.89914 | 5.27411 | 12.412 | 42.4892 | 470.254 |
| tossup | gamma_2 | 360 | 5.02808 | 0.28345 | 4.15257 | 4.55227 | 4.83817 | 5.00719 | 5.22239 | 5.52562 | 5.76468 |
| tossup | gamma_3 | 360 | 5.06692 | 0.586608 | 4.09389 | 4.57631 | 4.83105 | 5.0173 | 5.21221 | 5.52216 | 12.2568 |
| tossup | gamma_4 | 360 | 18.5032 | 106.08 | 4.3739 | 4.63649 | 4.92297 | 5.19522 | 5.54025 | 32.8403 | 1804.7 |
| tossup | gamma_5 | 360 | 15.2214 | 48.152 | 4.19516 | 4.57293 | 4.93064 | 5.22205 | 11.6297 | 47.2299 | 757.455 |
| tossup | mu_1 | 360 | 0.591007 | 0.12717 | 0.463843 | 0.482806 | 0.498884 | 0.513532 | 0.68767 | 0.842097 | 0.960545 |
| tossup | mu_2 | 360 | 0.499534 | 0.0121697 | 0.459949 | 0.479577 | 0.491484 | 0.499572 | 0.507589 | 0.519735 | 0.530803 |
| tossup | mu_3 | 360 | 0.502775 | 0.0321659 | 0.457252 | 0.479281 | 0.490562 | 0.49919 | 0.509436 | 0.521057 | 0.820256 |
| tossup | mu_4 | 360 | 0.558909 | 0.119377 | 0.457248 | 0.481695 | 0.493681 | 0.504426 | 0.521233 | 0.820308 | 0.957932 |
| tossup | mu_5 | 360 | 0.587729 | 0.128249 | 0.426041 | 0.48151 | 0.497604 | 0.51046 | 0.698493 | 0.843188 | 0.929924 |
| tossup | r_1 | 360 | 0.39125 | 0.48327 | 7.37658e-15 | 3.04453e-11 | 8.55293e-08 | 5.65946e-05 | 0.999687 | 1 | 1 |
| tossup | r_2 | 360 | 9.14078e-06 | 8.36817e-05 | 5.86141e-17 | 2.14541e-13 | 7.79305e-11 | 8.01482e-09 | 1.90702e-07 | 1.7972e-05 | 0.00150683 |
| tossup | r_3 | 360 | 0.0112101 | 0.104867 | 6.49491e-19 | 4.22522e-15 | 6.57652e-11 | 6.51138e-09 | 1.15164e-06 | 0.000113148 | 0.999568 |
| tossup | r_4 | 360 | 0.223823 | 0.413966 | 1.94533e-16 | 7.56531e-13 | 4.71898e-09 | 6.26825e-06 | 0.0217276 | 0.999998 | 1 |
| tossup | r_5 | 360 | 0.373707 | 0.478993 | 1.15026e-14 | 3.7239e-11 | 4.76527e-07 | 0.000363323 | 0.999807 | 1 | 1 |
| tossup | r_norm | 360 | 0.992807 | 0.0291175 | 0.742166 | 0.955637 | 0.999454 | 0.999977 | 1 | 1 | 1 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta_1 | 1071 | 0.00160244 | 0.680739 | -2.29935 | -1.40465 | -0.0492655 | 0.00226012 | 0.0646519 | 1.38167 | 1.94045 |
| bonus_part | beta_2 | 1071 | -0.00233557 | 0.0515731 | -0.17645 | -0.0889593 | -0.0370501 | -0.00294466 | 0.0326777 | 0.0839604 | 0.153904 |
| bonus_part | beta_3 | 1071 | -0.00105846 | 0.0502911 | -0.160667 | -0.0827365 | -0.0343976 | -0.00116606 | 0.0307797 | 0.0873716 | 0.154655 |
| bonus_part | beta_4 | 1071 | 0.0305465 | 0.565358 | -2.1931 | -0.883088 | -0.0451452 | 0.00162456 | 0.0585186 | 1.19998 | 2.00216 |
| bonus_part | beta_5 | 1071 | -0.00538009 | 0.840133 | -2.34788 | -1.76548 | -0.102918 | -0.00154577 | 0.150129 | 1.44719 | 1.86184 |
| bonus_part | r_1 | 1071 | 0.312945 | 0.445923 | 1.05845e-14 | 1.73197e-11 | 4.53257e-08 | 5.11283e-05 | 0.981291 | 1 | 1 |
| bonus_part | r_2 | 1071 | 7.35093e-06 | 3.37713e-05 | 1.22986e-15 | 6.83792e-13 | 2.1994e-10 | 2.09962e-08 | 5.8081e-07 | 2.65367e-05 | 0.000352199 |
| bonus_part | r_3 | 1071 | 0.00018948 | 0.00186244 | 2.21284e-19 | 1.6317e-14 | 1.59125e-10 | 4.20311e-08 | 2.75884e-06 | 0.000333047 | 0.0335057 |
| bonus_part | r_4 | 1071 | 0.226508 | 0.392724 | 4.56605e-16 | 7.90397e-12 | 4.20964e-08 | 5.49122e-05 | 0.210571 | 0.99999 | 1 |
| bonus_part | r_5 | 1071 | 0.460351 | 0.473442 | 3.99252e-12 | 1.15284e-09 | 1.27896e-05 | 0.139042 | 0.999893 | 1 | 1 |
| bonus_part | r_norm | 1071 | 0.965027 | 0.0811392 | 0.626495 | 0.738077 | 0.989721 | 0.99989 | 0.999999 | 1 | 1 |
| synergy_player | psi_1 | 189 | -0.051821 | 0.146669 | -0.428985 | -0.300695 | -0.0771807 | -0.018195 | 0.0180076 | 0.121215 | 0.703914 |
| synergy_player | psi_2 | 189 | -0.0109372 | 0.109864 | -0.302249 | -0.244003 | -0.0336506 | -0.00371246 | 0.0343873 | 0.173195 | 0.297182 |
| synergy_player | psi_3 | 189 | 0.00144489 | 0.126995 | -0.328016 | -0.232142 | -0.0415247 | -0.00421564 | 0.03386 | 0.279878 | 0.366071 |
| synergy_player | psi_norm | 189 | 0.204687 | 0.102039 | 0.0228232 | 0.0496903 | 0.108779 | 0.233444 | 0.275076 | 0.340757 | 0.705109 |
| synergy | synergy_score | 274 | 0.0437849 | 0.0432137 | -0.198909 | -0.00161056 | 0.0079403 | 0.0487845 | 0.0710377 | 0.106128 | 0.177317 |
| synergy | synergy_contribution | 7017 | 0.264154 | 0.201558 | -0.347333 | -0.00431084 | 0.052259 | 0.319123 | 0.422633 | 0.52415 | 0.637651 |
