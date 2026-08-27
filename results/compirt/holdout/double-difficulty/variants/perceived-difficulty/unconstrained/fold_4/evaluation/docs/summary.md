# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/unconstrained/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perceived-difficulty/unconstrained/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 338629 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.660885 |
| log_loss | 0.510529 |
| ece | 0.0385675 |
| brier | 0.166691 |
| accuracy | 0.772276 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00107875 |
| probability_std | 0.136941 |
| probability_p10 | 0.53792 |
| probability_p50 | 0.763656 |
| probability_p90 | 0.886832 |
| mean_predictive_variance | 0.175654 |
| integrated_brier_score | 0.16738 |
| joint_tossup_event_log_loss | 7.6197 |
| buzz_position_mae | 0.327091 |
| buzz_position_median_absolute_error | 0.329784 |
| buzz_position_bias | -0.31327 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.353506 |
| first_buzzer_mean_reciprocal_rank | 0.563337 |
| first_buzzer_log_loss | 1.68939 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.660885 |
| neg_average_precision | 0.372663 |
| neg_precision | 0.492212 |
| neg_recall | 0.150405 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0317596 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.223143 |
| no_buzz_calibration_error | 0.211416 |
| no_buzz_brier | 0.0671504 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.660885 | 0.510529 | 0.0385675 | 0.166691 | 0.772276 | 0.773355 | -0.00107875 | 0.136941 | 0.53792 | 0.763656 | 0.886832 | 0.175654 |
| tossup_correctness | tier | fall | 2876 | 0.640759 | 0.487585 | 0.0222995 | 0.156362 | 0.795202 | 0.793115 | 0.00208623 | 0.101414 | 0.645598 | 0.805074 | 0.896511 | 0.157707 |
| tossup_correctness | tier | nationals | 1579 | 0.677653 | 0.576809 | 0.119496 | 0.196227 | 0.704877 | 0.729576 | -0.0246992 | 0.152588 | 0.403338 | 0.619136 | 0.809427 | 0.214395 |
| tossup_correctness | tier | regionals | 1990 | 0.662404 | 0.520696 | 0.0471083 | 0.170862 | 0.762312 | 0.765829 | -0.00351759 | 0.131917 | 0.54037 | 0.742729 | 0.872418 | 0.183775 |
| tossup_correctness | tier | winter | 2825 | 0.67491 | 0.48968 | 0.0290563 | 0.157759 | 0.793628 | 0.783009 | 0.0106195 | 0.116222 | 0.610122 | 0.781556 | 0.895558 | 0.16655 |
| tossup_correctness | category | Current Events | 123 | 0.669846 | 0.552547 | 0.13827 | 0.185411 | 0.699187 | 0.764228 | -0.0650407 | 0.151666 | 0.400078 | 0.66024 | 0.819748 | 0.206579 |
| tossup_correctness | category | Fine Arts | 1093 | 0.661613 | 0.508928 | 0.033823 | 0.166122 | 0.777676 | 0.769442 | 0.00823422 | 0.118586 | 0.58755 | 0.765854 | 0.871293 | 0.178603 |
| tossup_correctness | category | Geography | 191 | 0.748716 | 0.536645 | 0.0462824 | 0.179568 | 0.732984 | 0.691099 | 0.0418848 | 0.157656 | 0.466829 | 0.721094 | 0.856946 | 0.192219 |
| tossup_correctness | category | History | 1469 | 0.684987 | 0.517916 | 0.0332657 | 0.170796 | 0.757658 | 0.758339 | -0.000680735 | 0.146898 | 0.509865 | 0.759925 | 0.898888 | 0.175189 |
| tossup_correctness | category | Literature | 1436 | 0.619016 | 0.474537 | 0.0410547 | 0.15084 | 0.80571 | 0.81546 | -0.0097493 | 0.117691 | 0.615666 | 0.80386 | 0.896997 | 0.159746 |
| tossup_correctness | category | Mythology | 325 | 0.60176 | 0.468405 | 0.107575 | 0.147902 | 0.821538 | 0.843077 | -0.0215385 | 0.129533 | 0.55119 | 0.758444 | 0.881544 | 0.176219 |
| tossup_correctness | category | Other Academic | 67 | 0.6469 | 0.574878 | 0.18329 | 0.194714 | 0.701493 | 0.791045 | -0.0895522 | 0.1403 | 0.412658 | 0.622106 | 0.798526 | 0.218705 |
| tossup_correctness | category | Philosophy | 322 | 0.606118 | 0.51341 | 0.0713868 | 0.166218 | 0.785714 | 0.785714 | 0 | 0.120422 | 0.603797 | 0.770285 | 0.890449 | 0.171618 |
| tossup_correctness | category | Popular Culture | 100 | 0.463739 | 0.445432 | 0.154808 | 0.136068 | 0.85 | 0.89 | -0.04 | 0.101571 | 0.593666 | 0.752481 | 0.848332 | 0.184368 |
| tossup_correctness | category | Religion | 365 | 0.662729 | 0.560569 | 0.0342108 | 0.189308 | 0.717808 | 0.723288 | -0.00547945 | 0.1374 | 0.513469 | 0.736686 | 0.869031 | 0.187323 |
| tossup_correctness | category | Science | 1456 | 0.660709 | 0.51039 | 0.0445933 | 0.166103 | 0.778846 | 0.76717 | 0.0116758 | 0.147509 | 0.529024 | 0.792233 | 0.903267 | 0.165097 |
| tossup_correctness | category | Social Science | 333 | 0.696159 | 0.537848 | 0.0566273 | 0.179708 | 0.744745 | 0.72973 | 0.015015 | 0.142137 | 0.517453 | 0.70715 | 0.866766 | 0.192612 |
| tossup_correctness | category | Unknown | 1990 | 0.662404 | 0.520696 | 0.0471083 | 0.170862 | 0.762312 | 0.765829 | -0.00351759 | 0.131917 | 0.54037 | 0.742729 | 0.872418 | 0.183775 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.638474 | 0.540397 | 0.0662598 | 0.178467 | 0.77095 | 0.748603 | 0.0223464 | 0.131666 | 0.507842 | 0.736802 | 0.834497 | 0.190789 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.624589 | 0.545077 | 0.0486223 | 0.181388 | 0.751306 | 0.754441 | -0.0031348 | 0.134737 | 0.528557 | 0.745699 | 0.866923 | 0.184155 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.656388 | 0.520058 | 0.0344387 | 0.170775 | 0.76532 | 0.766682 | -0.00136178 | 0.133288 | 0.544219 | 0.759671 | 0.880504 | 0.178223 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.676662 | 0.487801 | 0.0444808 | 0.157758 | 0.785426 | 0.787441 | -0.00201478 | 0.133039 | 0.551809 | 0.770282 | 0.889521 | 0.172954 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.659551 | 0.513335 | 0.0442456 | 0.167176 | 0.77108 | 0.771758 | -0.000677277 | 0.143525 | 0.527218 | 0.768738 | 0.894877 | 0.172788 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | -2.06023 | 0.617179 | -4.04993 | -3.07344 | -2.49782 | -2.03089 | -1.58513 | -1.11292 | -0.812976 |
| player | theta_2 | 1196 | -1.41428 | 0.69491 | -4.25668 | -2.62355 | -1.86787 | -1.37473 | -0.856675 | -0.366321 | 0.0199884 |
| player | theta_3 | 1196 | -0.957642 | 0.827857 | -3.81325 | -2.76763 | -1.28213 | -0.646046 | -0.374008 | -0.151786 | 0.191129 |
| player | alpha_1 | 1196 | -0.981921 | 0.694243 | -3.21974 | -2.21492 | -1.3909 | -0.950279 | -0.506563 | 0.136583 | 0.810564 |
| player | alpha_2 | 1196 | -0.371912 | 0.885939 | -2.62243 | -1.74998 | -0.915087 | -0.452872 | 0.0676001 | 1.2965 | 2.75073 |
| player | alpha_3 | 1196 | 0.414735 | 0.876169 | -3.32933 | -1.07258 | -0.119738 | 0.47706 | 0.938036 | 1.84739 | 3.0019 |
| player | beta_1 | 1196 | -2.30027 | 0.903779 | -5.79243 | -4.14422 | -2.79218 | -2.09933 | -1.63859 | -1.18542 | -0.794405 |
| player | beta_2 | 1196 | -1.56623 | 0.812203 | -4.18924 | -3.01409 | -2.13062 | -1.54166 | -0.900333 | -0.353771 | -0.0995717 |
| player | beta_3 | 1196 | -1.20744 | 1.2518 | -5.50983 | -4.17323 | -1.47661 | -0.669914 | -0.381682 | -0.154151 | 0.045157 |
| player | theta_norm | 1196 | 2.83634 | 0.815723 | 0.925642 | 1.56645 | 2.21452 | 2.80389 | 3.38412 | 4.23725 | 5.24766 |
| tossup | start_difficulty_d1 | 1240 | -2.5152 | 1.00251 | -4.84499 | -3.90944 | -3.25502 | -2.65967 | -1.90135 | -0.594348 | 0.150896 |
| tossup | start_difficulty_d2 | 1240 | -1.02736 | 1.24804 | -4.45027 | -3.56069 | -1.83062 | -0.499153 | -0.088885 | 0.25193 | 0.782232 |
| tossup | start_difficulty_d3 | 1240 | -0.71821 | 1.00537 | -3.05098 | -2.5102 | -1.57448 | -0.560697 | 0.150136 | 0.620339 | 1.31585 |
| tossup | end_difficulty_d1 | 1240 | -3.37515 | 1.06332 | -11.0486 | -4.94947 | -4.0135 | -3.44388 | -2.75894 | -1.49733 | -0.645385 |
| tossup | end_difficulty_d2 | 1240 | -2.09368 | 1.35968 | -10.0611 | -4.39115 | -3.25592 | -1.53034 | -1.03993 | -0.639006 | 0.0263899 |
| tossup | end_difficulty_d3 | 1240 | -1.92184 | 1.22794 | -11.655 | -3.98317 | -2.66854 | -1.75968 | -0.949776 | -0.364998 | 0.450057 |
| tossup | total_drop_d1 | 1240 | 0.85995 | 0.562415 | 0.289464 | 0.423916 | 0.568348 | 0.7342 | 0.972071 | 1.59006 | 8.97059 |
| tossup | total_drop_d2 | 1240 | 1.06632 | 0.705283 | 0.411388 | 0.535664 | 0.866099 | 0.948576 | 1.06023 | 1.87389 | 9.92896 |
| tossup | total_drop_d3 | 1240 | 1.20363 | 0.739714 | 0.57629 | 0.793079 | 0.948234 | 1.03117 | 1.19129 | 1.95937 | 11.3019 |
| tossup | drop_share_1_d1 | 1240 | 0.344497 | 0.032752 | 0.253221 | 0.299061 | 0.322154 | 0.33956 | 0.365402 | 0.403651 | 0.464555 |
| tossup | drop_share_2_d1 | 1240 | 0.323965 | 0.0199375 | 0.264696 | 0.293053 | 0.309983 | 0.32384 | 0.337795 | 0.354024 | 0.453968 |
| tossup | drop_share_3_d1 | 1240 | 0.331539 | 0.0328941 | 0.224591 | 0.275272 | 0.310588 | 0.331674 | 0.351432 | 0.38626 | 0.46016 |
| tossup | drop_share_1_d2 | 1240 | 0.314803 | 0.0286695 | 0.0935052 | 0.285598 | 0.302852 | 0.312242 | 0.32358 | 0.367527 | 0.441413 |
| tossup | drop_share_2_d2 | 1240 | 0.339686 | 0.0207859 | 0.179678 | 0.301797 | 0.33198 | 0.342769 | 0.351666 | 0.366081 | 0.431347 |
| tossup | drop_share_3_d2 | 1240 | 0.345511 | 0.0310429 | 0.245793 | 0.305265 | 0.33231 | 0.344666 | 0.355126 | 0.384767 | 0.726817 |
| tossup | drop_share_1_d3 | 1240 | 0.314354 | 0.0299349 | 0.113479 | 0.277817 | 0.299308 | 0.313842 | 0.331991 | 0.357906 | 0.440851 |
| tossup | drop_share_2_d3 | 1240 | 0.34787 | 0.0180648 | 0.27751 | 0.325442 | 0.337889 | 0.345953 | 0.354844 | 0.375087 | 0.505584 |
| tossup | drop_share_3_d3 | 1240 | 0.337777 | 0.0245632 | 0.240801 | 0.299121 | 0.324026 | 0.338897 | 0.351635 | 0.365985 | 0.604023 |
| tossup | r_1 | 1240 | 0.57159 | 0.248111 | 0.0487643 | 0.118618 | 0.369833 | 0.666561 | 0.79053 | 0.868543 | 0.949819 |
| tossup | r_2 | 1240 | 0.211561 | 0.210076 | 0.0276081 | 0.0488525 | 0.0722636 | 0.115038 | 0.240099 | 0.661582 | 0.907886 |
| tossup | r_3 | 1240 | 0.216849 | 0.211202 | 0.0187658 | 0.035776 | 0.0686767 | 0.111438 | 0.36325 | 0.673348 | 0.792807 |
| tossup | r_norm | 1240 | 0.75009 | 0.077733 | 0.581312 | 0.636291 | 0.681599 | 0.747769 | 0.813606 | 0.877656 | 0.950498 |
