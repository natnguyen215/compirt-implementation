# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-all2024-cal/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim-tanh-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 447692 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 85529.5 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.176463 |
| mean_synergy_contribution | 0.63232 |
| median_synergy_contribution | 0.452693 |
| negative_synergy_fraction | 0.288881 |
| positive_synergy_fraction | 0.686737 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.930128 |
| log_loss | 0.340836 |
| ece | 0.0273278 |
| part_accuracy | 0.850939 |
| part_accuracy_macro_team | 0.852141 |
| part_accuracy_macro_game | 0.851306 |
| part_accuracy_macro_bonus | 0.860163 |
| exact_acc | 0.606494 |
| ppb_mae | 0.649599 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.621269 |
| log_loss | 0.523727 |
| ece | 0.0131262 |
| accuracy | 0.770768 |
| buzz_position_mae | 0.129624 |
| buzz_position_median_absolute_error | 0.105364 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.925767 | 0.930128 | 0.00436118 | synergy |
| log_loss | 0.35033 | 0.340836 | -0.00949429 | synergy |
| ece | 0.0281366 | 0.0273278 | -0.000808869 | synergy |
| part_accuracy | 0.843666 | 0.850939 | 0.00727275 | synergy |
| part_accuracy_macro_team | 0.844557 | 0.852141 | 0.00758453 | synergy |
| part_accuracy_macro_game | 0.843953 | 0.851306 | 0.00735301 | synergy |
| part_accuracy_macro_bonus | 0.854361 | 0.860163 | 0.00580198 | synergy |
| exact_acc | 0.588447 | 0.606494 | 0.0180468 | synergy |
| ppb_mae | 1.75481 | 0.649599 | -1.10521 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 1.1003 | 0.655811 | -0.805008 | 0.0273806 | 0.672098 | 1.07169 | 1.53035 | 2.17357 | 4.17067 |
| player | theta_1 | 1755 | -1.34314 | 0.696767 | -3.61237 | -2.46471 | -1.81654 | -1.3581 | -0.888146 | -0.171955 | 0.953041 |
| player | theta_2 | 1755 | -1.21659 | 0.60279 | -3.0433 | -2.17802 | -1.61494 | -1.23151 | -0.816395 | -0.225485 | 1.02209 |
| player | theta_3 | 1755 | -1.21993 | 0.732699 | -3.47302 | -2.37539 | -1.77508 | -1.25887 | -0.695577 | 0.00557117 | 0.936622 |
| player | theta_4 | 1755 | -1.06818 | 0.655014 | -3.4307 | -2.01972 | -1.53347 | -1.12842 | -0.654552 | 0.128112 | 1.23055 |
| player | theta_5 | 1755 | -1.04625 | 0.659326 | -3.39762 | -2.00756 | -1.53622 | -1.09078 | -0.605124 | 0.119897 | 1.0456 |
| player | theta_norm | 1755 | 2.99169 | 0.553315 | 1.06473 | 2.03937 | 2.60425 | 3.02389 | 3.40092 | 3.87077 | 4.54093 |
| tossup | beta_1 | 1350 | 0.574592 | 0.631032 | -0.265487 | -0.0291733 | 0.0935403 | 0.243461 | 1.12989 | 1.72276 | 3.77273 |
| tossup | beta_2 | 1350 | 0.278585 | 0.417093 | -0.343149 | -0.0437443 | 0.0587577 | 0.142744 | 0.277687 | 1.33646 | 2.54587 |
| tossup | beta_3 | 1350 | 0.499842 | 0.622443 | -3.38785 | -0.0607553 | 0.0749232 | 0.20399 | 0.959118 | 1.64829 | 3.8723 |
| tossup | beta_4 | 1350 | 0.394083 | 0.538534 | -0.286465 | -0.042856 | 0.0735524 | 0.1698 | 0.414115 | 1.65602 | 2.99023 |
| tossup | beta_5 | 1350 | 0.418509 | 0.531974 | -1.36713 | -0.0281489 | 0.0844023 | 0.183044 | 0.533181 | 1.57576 | 3.26634 |
| tossup | gamma_1 | 1350 | 8.89305 | 57.2037 | 0.741828 | 1.25281 | 2.00943 | 2.76161 | 3.61222 | 12.233 | 1031.75 |
| tossup | gamma_2 | 1350 | 4.80221 | 21.378 | 0.808379 | 1.4308 | 2.23591 | 2.79256 | 3.39349 | 5.03963 | 448.696 |
| tossup | gamma_3 | 1350 | 9.0236 | 49.6261 | 0.83073 | 1.48569 | 2.30776 | 2.91192 | 3.72481 | 13.0142 | 945.143 |
| tossup | gamma_4 | 1350 | 6.89626 | 42.7181 | 0.688653 | 1.3658 | 2.06971 | 2.66042 | 3.34704 | 5.9781 | 1001.03 |
| tossup | gamma_5 | 1350 | 6.29512 | 39.7567 | 0.609711 | 1.36431 | 2.04993 | 2.61114 | 3.24545 | 6.60319 | 935.051 |
| tossup | mu_1 | 1350 | 0.580854 | 0.113524 | 0.107159 | 0.442753 | 0.516167 | 0.561535 | 0.63 | 0.790928 | 0.994382 |
| tossup | mu_2 | 1350 | 0.559103 | 0.0776352 | 0.19537 | 0.463422 | 0.515926 | 0.553168 | 0.588012 | 0.693563 | 0.993838 |
| tossup | mu_3 | 1350 | 0.560263 | 0.101765 | 0.0932655 | 0.408164 | 0.514783 | 0.550081 | 0.599782 | 0.735725 | 0.994665 |
| tossup | mu_4 | 1350 | 0.567164 | 0.0883448 | 0.142527 | 0.465417 | 0.518503 | 0.554486 | 0.602516 | 0.726206 | 0.992154 |
| tossup | mu_5 | 1350 | 0.573745 | 0.0997019 | 0.207979 | 0.446948 | 0.524092 | 0.559491 | 0.610414 | 0.763512 | 0.994496 |
| tossup | r_1 | 1350 | 1.26977 | 0.648402 | 0.071054 | 0.312589 | 0.754474 | 1.23008 | 1.71021 | 2.42403 | 3.53078 |
| tossup | r_2 | 1350 | 0.878042 | 0.447862 | 0.0786697 | 0.21757 | 0.559148 | 0.812955 | 1.1622 | 1.69798 | 2.67818 |
| tossup | r_3 | 1350 | 1.09655 | 0.634581 | 0.0533735 | 0.256681 | 0.60982 | 0.99145 | 1.47677 | 2.32771 | 3.46821 |
| tossup | r_4 | 1350 | 1.05435 | 0.599554 | 0.0817127 | 0.312812 | 0.618869 | 0.938465 | 1.35105 | 2.21893 | 3.58614 |
| tossup | r_5 | 1350 | 1.12036 | 0.619863 | 0.085603 | 0.347256 | 0.668104 | 0.985451 | 1.42216 | 2.39294 | 3.90143 |
| tossup | r_norm | 1350 | 2.7291 | 0.520427 | 1.36518 | 1.93282 | 2.37488 | 2.70078 | 3.02066 | 3.65988 | 4.58084 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | -0.000103146 | 0.719133 | -1.41857 | -1.02619 | -0.611885 | -0.0550225 | 0.552843 | 1.25482 | 1.79615 |
| bonus_part | alpha_1 | 4716 | 0.0549979 | 0.791789 | -2.09897 | -1.25161 | -0.614481 | 0.125938 | 0.715949 | 1.19798 | 2.42979 |
| bonus_part | alpha_2 | 4716 | 0.0236803 | 0.788797 | -1.78965 | -1.22708 | -0.642918 | 0.0532002 | 0.681413 | 1.20447 | 2.27367 |
| bonus_part | alpha_3 | 4716 | -0.0140329 | 0.832198 | -2.28879 | -1.31887 | -0.717131 | 0.0302368 | 0.670522 | 1.20061 | 2.79538 |
| bonus_part | alpha_4 | 4716 | 0.11091 | 0.668129 | -1.59626 | -0.945748 | -0.443888 | 0.152522 | 0.636732 | 1.06135 | 2.89006 |
| bonus_part | alpha_5 | 4716 | 0.0646993 | 0.680647 | -1.96938 | -1.00954 | -0.484092 | 0.0969282 | 0.592577 | 1.06115 | 2.6005 |
| bonus_part | alpha_norm | 4716 | 1.58535 | 0.598148 | 0.169015 | 0.522508 | 1.1623 | 1.63952 | 2.01283 | 2.51978 | 3.42538 |
