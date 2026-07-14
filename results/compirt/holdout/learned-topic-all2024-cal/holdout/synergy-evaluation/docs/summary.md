# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/learned-topic-all2024-cal/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/learned-topic-all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 845200 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 279666 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.587299 |
| mean_synergy_contribution | 0.13939 |
| median_synergy_contribution | 0.119154 |
| negative_synergy_fraction | 0.321865 |
| positive_synergy_fraction | 0.653753 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.924418 |
| log_loss | 0.349253 |
| ece | 0.0133964 |
| part_accuracy | 0.844659 |
| exact_score_accuracy | 0.589225 |
| per_bonus_points_mae | 4.76637 |
| ppb_mae | 1.6658 |
| accuracy | 0.844659 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.597349 |
| log_loss | 0.527683 |
| ece | 0.00240029 |
| accuracy | 0.770367 |
| buzz_position_mae | 0.146981 |
| buzz_position_median_absolute_error | 0.129307 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 3.31567 | 0.64203 | 1.25425 | 2.23888 | 2.89016 | 3.31835 | 3.7134 | 4.45235 | 5.1819 |
| player | theta_1 | 1755 | -1.26185 | 0.862863 | -4.08488 | -2.48304 | -1.83779 | -1.40246 | -0.709999 | 0.350124 | 1.37165 |
| player | theta_2 | 1755 | -0.857675 | 0.619656 | -2.74484 | -1.71598 | -1.23063 | -0.958831 | -0.584612 | 0.331929 | 1.95528 |
| player | theta_3 | 1755 | -0.660881 | 0.461042 | -2.22988 | -1.40804 | -0.893069 | -0.649871 | -0.490245 | 0.136374 | 1.51673 |
| player | theta_4 | 1755 | -1.11769 | 0.899256 | -3.5036 | -2.34288 | -1.73946 | -1.27606 | -0.582249 | 0.60297 | 2.55289 |
| player | theta_5 | 1755 | -1.26815 | 0.802506 | -3.22804 | -2.23774 | -1.79183 | -1.46521 | -0.908352 | 0.387166 | 2.32758 |
| player | theta_norm | 1755 | 2.85616 | 0.50665 | 0.654365 | 1.96808 | 2.62742 | 2.86486 | 3.11248 | 3.70636 | 5.1181 |
| tossup | beta_1 | 1350 | 1.40389 | 1.78868 | -0.225689 | 0.0446831 | 0.144658 | 0.304778 | 3.17545 | 4.77197 | 6.05756 |
| tossup | beta_2 | 1350 | 0.8739 | 1.56384 | -0.419164 | 0.0496422 | 0.124464 | 0.201784 | 0.375017 | 4.78555 | 5.85298 |
| tossup | beta_3 | 1350 | 0.788928 | 1.41533 | -2.77015 | 0.0455606 | 0.130014 | 0.221252 | 0.457606 | 4.71088 | 5.88671 |
| tossup | beta_4 | 1350 | 1.05858 | 1.65871 | -0.333255 | 0.0334855 | 0.119126 | 0.202804 | 0.631128 | 4.60226 | 5.5583 |
| tossup | beta_5 | 1350 | 1.38897 | 1.8391 | -0.417641 | 0.0463285 | 0.147443 | 0.296159 | 3.14783 | 5.00244 | 5.69283 |
| tossup | gamma_1 | 1350 | 21.8276 | 99.5361 | 3.7448 | 4.65322 | 4.97766 | 5.27585 | 8.23441 | 57.5551 | 1968.95 |
| tossup | gamma_2 | 1350 | 18.6802 | 107.71 | 3.7938 | 4.5939 | 4.87088 | 5.09459 | 5.44332 | 23.5691 | 1961 |
| tossup | gamma_3 | 1350 | 13.6331 | 80.7066 | 4.11394 | 4.6501 | 4.92429 | 5.15308 | 5.46826 | 21.1799 | 1879.2 |
| tossup | gamma_4 | 1350 | 12.75 | 56.9796 | 4.12868 | 4.65765 | 4.92875 | 5.16843 | 5.68709 | 20.8378 | 1119.44 |
| tossup | gamma_5 | 1350 | 20.6679 | 86.6019 | 4.10309 | 4.64954 | 4.96784 | 5.28178 | 7.53188 | 48.6653 | 1511.61 |
| tossup | mu_1 | 1350 | 0.540818 | 0.0996992 | 0.139699 | 0.470873 | 0.492014 | 0.50526 | 0.536279 | 0.764579 | 0.972575 |
| tossup | mu_2 | 1350 | 0.536532 | 0.0980598 | 0.288109 | 0.477922 | 0.493255 | 0.503133 | 0.516549 | 0.79559 | 0.993296 |
| tossup | mu_3 | 1350 | 0.527722 | 0.0831428 | 0.258347 | 0.478286 | 0.492635 | 0.503247 | 0.515916 | 0.72577 | 0.987664 |
| tossup | mu_4 | 1350 | 0.5342 | 0.0907249 | 0.233853 | 0.477271 | 0.493178 | 0.504105 | 0.519184 | 0.761184 | 0.985946 |
| tossup | mu_5 | 1350 | 0.55306 | 0.112454 | 0.233023 | 0.476119 | 0.493654 | 0.506249 | 0.544523 | 0.802622 | 0.987622 |
| tossup | topic_weight_1 | 1350 | 0.250644 | 0.33622 | 0.00563546 | 0.00964834 | 0.017025 | 0.041835 | 0.617758 | 0.876215 | 0.952602 |
| tossup | topic_weight_2 | 1350 | 0.145353 | 0.272936 | 0.00641883 | 0.0106332 | 0.0155331 | 0.0245925 | 0.0562276 | 0.853664 | 0.960042 |
| tossup | topic_weight_3 | 1350 | 0.130662 | 0.239107 | 0.00697456 | 0.0112979 | 0.0178047 | 0.0310025 | 0.0800606 | 0.803083 | 0.942097 |
| tossup | topic_weight_4 | 1350 | 0.214113 | 0.343293 | 0.0064166 | 0.0113074 | 0.0181405 | 0.0329747 | 0.12605 | 0.940458 | 0.969052 |
| tossup | topic_weight_5 | 1350 | 0.259228 | 0.34263 | 0.00604138 | 0.0123256 | 0.025038 | 0.0600392 | 0.481717 | 0.913564 | 0.969744 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| synergy_player | psi_1 | 1755 | -0.00409332 | 0.199737 | -0.961586 | -0.355071 | -0.0430299 | -0.00149376 | 0.0407647 | 0.302772 | 1.03206 |
| synergy_player | psi_2 | 1755 | -0.000782383 | 0.17469 | -1.01429 | -0.291808 | -0.0370586 | -0.00208631 | 0.0353916 | 0.274701 | 0.865788 |
| synergy_player | psi_3 | 1755 | -0.00511338 | 0.197714 | -0.944538 | -0.33145 | -0.0466278 | -0.00307231 | 0.0377521 | 0.3549 | 0.981928 |
| synergy_player | psi_norm | 1755 | 0.267514 | 0.194786 | 0.0117009 | 0.0441758 | 0.111923 | 0.227565 | 0.363582 | 0.648764 | 1.10116 |
| synergy | synergy_score | 3042 | 0.0170859 | 0.118614 | -0.963132 | -0.172679 | -0.00636962 | 0.0140094 | 0.0630162 | 0.175537 | 0.830285 |
| synergy | synergy_contribution | 60454 | 0.13939 | 0.310377 | -0.981656 | -0.384708 | -0.038697 | 0.119154 | 0.333754 | 0.664282 | 1.57425 |
