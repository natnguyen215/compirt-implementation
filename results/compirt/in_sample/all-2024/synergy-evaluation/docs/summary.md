# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/all-2024/synergy-evaluation`
Result root: `results/compirt/in_sample/all-2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 363404 |
| pyramidal | calibrate_correctness | False |
| pyramidal | predicted_buzz_positions | True |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 65458.2 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.546143 |
| mean_synergy_contribution | -0.758513 |
| median_synergy_contribution | -0.746789 |
| negative_synergy_fraction | 0.835413 |
| positive_synergy_fraction | 0.133185 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.939144 |
| log_loss | 0.328479 |
| ece | 0.0447856 |
| part_accuracy | 0.858693 |
| exact_score_accuracy | 0.626453 |
| rounded_score_accuracy | 0.623823 |
| per_bonus_points_mae | 4.5566 |
| ppb_mae | 1.76204 |
| accuracy | 0.858693 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.70368 |
| log_loss | 0.580392 |
| ece | 0.151482 |
| accuracy | 0.705931 |
| buzz_position_mae | 0.138836 |
| buzz_position_median_absolute_error | 0.121284 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.93318 | 0.939144 | 0.0059641 | synergy |
| log_loss | 0.341453 | 0.328479 | -0.0129744 | synergy |
| ece | 0.0415155 | 0.0447856 | 0.0032701 | no-synergy |
| accuracy | 0.852301 | 0.858693 | 0.00639138 | synergy |
| part_accuracy | 0.852301 | 0.858693 | 0.00639138 | synergy |
| exact_score_accuracy | 0.611662 | 0.626453 | 0.0147908 | synergy |
| rounded_score_accuracy | 0.60548 | 0.623823 | 0.0183424 | synergy |
| per_bonus_points_mae | 4.82035 | 4.5566 | -0.263754 | synergy |
| ppb_mae | 2.17874 | 1.76204 | -0.416696 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.72992 | 1.02899 | 1.57541 | 2.57268 | 4.23106 | 4.97025 | 5.44094 | 6.04183 | 7.15025 |
| player | theta_1 | 1455 | -0.0545043 | 0.719242 | -2.32128 | -1.26173 | -0.529482 | -0.0718292 | 0.405541 | 1.21023 | 1.98207 |
| player | theta_2 | 1455 | 0.0795811 | 0.803382 | -1.95569 | -1.20738 | -0.489937 | 0.0684209 | 0.678854 | 1.40364 | 2.32643 |
| player | theta_3 | 1455 | 0.148088 | 0.926453 | -2.43299 | -1.21126 | -0.509572 | 0.0306273 | 0.722188 | 1.85252 | 2.89459 |
| player | theta_4 | 1455 | -0.196893 | 0.79028 | -2.54469 | -1.50322 | -0.750458 | -0.216674 | 0.325337 | 1.18168 | 2.56392 |
| player | theta_5 | 1455 | -0.0406318 | 0.771597 | -2.42499 | -1.41855 | -0.558134 | 0.0273555 | 0.523706 | 1.10243 | 2.1991 |
| player | theta_norm | 1455 | 1.72393 | 0.581953 | 0.236211 | 0.85335 | 1.31673 | 1.68364 | 2.0749 | 2.7955 | 3.54924 |
| tossup | beta | 1260 | 3.36433 | 0.690971 | 0.359666 | 2.28217 | 3.01439 | 3.41161 | 3.81599 | 4.3591 | 5.6672 |
| tossup | gamma | 1260 | 51.7059 | 178.778 | 3.69829 | 5.78002 | 8.89318 | 12.7736 | 25.0612 | 184.919 | 2051.49 |
| tossup | mu | 1260 | 0.603548 | 0.13268 | 0.202009 | 0.380392 | 0.511996 | 0.606552 | 0.692687 | 0.822221 | 0.98497 |
| tossup | alpha_1 | 1260 | -0.0556313 | 0.681278 | -2.46043 | -1.25244 | -0.476471 | -0.0360728 | 0.413679 | 1.00069 | 1.84852 |
| tossup | alpha_2 | 1260 | 0.354686 | 0.694435 | -1.28203 | -0.654819 | -0.203213 | 0.312714 | 0.876656 | 1.55915 | 2.77204 |
| tossup | alpha_3 | 1260 | -0.718115 | 0.65347 | -2.92486 | -1.85909 | -1.12998 | -0.680847 | -0.263262 | 0.28993 | 1.00924 |
| tossup | alpha_4 | 1260 | 0.232635 | 0.820231 | -2.31936 | -1.13423 | -0.33354 | 0.281823 | 0.82049 | 1.50093 | 2.39967 |
| tossup | alpha_5 | 1260 | 0.532974 | 0.590031 | -1.12965 | -0.315651 | 0.102646 | 0.489631 | 0.911367 | 1.54232 | 2.71118 |
| tossup | alpha_norm | 1260 | 1.7793 | 0.457662 | 0.398203 | 1.05313 | 1.45173 | 1.77902 | 2.07571 | 2.59161 | 3.26752 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.334681 | 1.53096 | -2.90626 | -2.19008 | -0.976661 | 0.532597 | 1.60018 | 2.5985 | 3.84151 |
| bonus_part | alpha_1 | 3768 | 0.00627284 | 0.479676 | -2.10152 | -0.783796 | -0.249052 | 0.00790436 | 0.269948 | 0.785093 | 2.43558 |
| bonus_part | alpha_2 | 3768 | 0.0461937 | 0.533135 | -2.061 | -0.73636 | -0.294696 | -0.0310189 | 0.367796 | 1.01269 | 2.20883 |
| bonus_part | alpha_3 | 3768 | -0.141222 | 0.579291 | -2.17363 | -1.11953 | -0.515469 | -0.116563 | 0.256391 | 0.759196 | 1.79945 |
| bonus_part | alpha_4 | 3768 | 0.0610092 | 0.540398 | -1.90971 | -0.831844 | -0.254006 | 0.0549358 | 0.380238 | 0.975122 | 2.51186 |
| bonus_part | alpha_5 | 3768 | 0.0624691 | 0.502909 | -2.00527 | -0.73717 | -0.285706 | 0.0487011 | 0.39543 | 0.902906 | 1.92794 |
| bonus_part | alpha_norm | 3768 | 1.09297 | 0.479258 | 0.0781065 | 0.410565 | 0.732031 | 1.04143 | 1.40546 | 1.96789 | 2.88297 |
| synergy_player | psi_1 | 1455 | -0.0078123 | 0.393595 | -1.87631 | -0.688422 | -0.0678935 | -0.000246679 | 0.0582037 | 0.67788 | 1.66583 |
| synergy_player | psi_2 | 1455 | 0.00207894 | 0.386437 | -1.78306 | -0.614205 | -0.053856 | 0.00184147 | 0.0561384 | 0.695475 | 1.73226 |
| synergy_player | psi_3 | 1455 | -0.00403457 | 0.428852 | -1.77491 | -0.724788 | -0.0793539 | -0.00356808 | 0.0728011 | 0.781318 | 1.61762 |
| synergy_player | psi_norm | 1455 | 0.554098 | 0.425453 | 0.0073093 | 0.0547284 | 0.192045 | 0.459348 | 0.837485 | 1.37134 | 1.87798 |
| synergy | synergy_score | 2521 | -0.14589 | 0.455026 | -2.53631 | -1.06636 | -0.328532 | -0.00421529 | 0.0910578 | 0.378292 | 1.48818 |
| synergy | synergy_contribution | 44487 | -0.758513 | 0.748084 | -2.82631 | -2.04539 | -1.25083 | -0.746789 | -0.118074 | 0.346958 | 1.43277 |
