# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/model-comparisons/curve-family/sigmoid/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 296897 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.668366 |
| log_loss | 0.548896 |
| ece | 0.108668 |
| brier | 0.184208 |
| accuracy | 0.723507 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0417429 |
| probability_std | 0.180251 |
| probability_p10 | 0.410243 |
| probability_p50 | 0.673513 |
| probability_p90 | 0.892919 |
| mean_predictive_variance | 0.19152 |
| integrated_brier_score | 0.102975 |
| joint_tossup_event_log_loss | 6.686 |
| buzz_position_mae | 0.156231 |
| buzz_position_median_absolute_error | 0.139 |
| buzz_position_bias | -0.0589852 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.32383 |
| first_buzzer_mean_reciprocal_rank | 0.540651 |
| first_buzzer_log_loss | 1.72537 |
| first_buzzer_events | 9295 |
| neg_auroc | 0.668366 |
| neg_average_precision | 0.376638 |
| neg_precision | 0.396918 |
| neg_recall | 0.342346 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.156542 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00663169 |
| no_buzz_calibration_error | -0.00663795 |
| no_buzz_brier | 0.0124872 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.668366 | 0.548896 | 0.108668 | 0.184208 | 0.723507 | 0.76525 | -0.0417429 | 0.180251 | 0.410243 | 0.673513 | 0.892919 | 0.19152 |
| tossup_correctness | tier | fall | 2933 | 0.679583 | 0.516973 | 0.104961 | 0.17094 | 0.74838 | 0.791681 | -0.0433004 | 0.190535 | 0.416494 | 0.721406 | 0.915209 | 0.177583 |
| tossup_correctness | tier | nationals | 1584 | 0.647109 | 0.58028 | 0.088264 | 0.1971 | 0.714015 | 0.724747 | -0.0107323 | 0.143312 | 0.436618 | 0.651087 | 0.811581 | 0.210714 |
| tossup_correctness | tier | regionals | 1886 | 0.663987 | 0.578625 | 0.12826 | 0.19678 | 0.704136 | 0.746023 | -0.0418876 | 0.170753 | 0.388037 | 0.629548 | 0.846682 | 0.205909 |
| tossup_correctness | tier | winter | 2892 | 0.664675 | 0.544694 | 0.111047 | 0.182403 | 0.716113 | 0.773167 | -0.0570539 | 0.187337 | 0.40872 | 0.686613 | 0.907857 | 0.185758 |
| tossup_correctness | category | Current Events | 124 | 0.674991 | 0.57694 | 0.146507 | 0.200217 | 0.701613 | 0.75 | -0.0483871 | 0.203641 | 0.359483 | 0.623461 | 0.898575 | 0.191817 |
| tossup_correctness | category | Fine Arts | 1103 | 0.666506 | 0.552944 | 0.110462 | 0.183735 | 0.729828 | 0.759746 | -0.0299184 | 0.181621 | 0.406425 | 0.683141 | 0.894384 | 0.189573 |
| tossup_correctness | category | Geography | 197 | 0.677273 | 0.642152 | 0.139686 | 0.217636 | 0.664975 | 0.670051 | -0.00507614 | 0.224936 | 0.259181 | 0.59611 | 0.856533 | 0.193902 |
| tossup_correctness | category | History | 1491 | 0.691835 | 0.517992 | 0.113766 | 0.171779 | 0.751174 | 0.787391 | -0.0362173 | 0.178148 | 0.43493 | 0.680804 | 0.907335 | 0.188109 |
| tossup_correctness | category | Literature | 1472 | 0.688001 | 0.485612 | 0.0918972 | 0.158526 | 0.774457 | 0.804348 | -0.0298913 | 0.160481 | 0.487327 | 0.735709 | 0.908245 | 0.179111 |
| tossup_correctness | category | Mythology | 332 | 0.637336 | 0.516006 | 0.130244 | 0.168035 | 0.746988 | 0.813253 | -0.0662651 | 0.173869 | 0.447804 | 0.732651 | 0.914453 | 0.177885 |
| tossup_correctness | category | Other Academic | 69 | 0.581448 | 0.610659 | 0.167798 | 0.20923 | 0.724638 | 0.753623 | -0.0289855 | 0.155728 | 0.399141 | 0.655244 | 0.809272 | 0.209843 |
| tossup_correctness | category | Philosophy | 324 | 0.635343 | 0.54128 | 0.133634 | 0.182326 | 0.716049 | 0.799383 | -0.0833333 | 0.171968 | 0.436787 | 0.680066 | 0.89479 | 0.192731 |
| tossup_correctness | category | Popular Culture | 102 | 0.587543 | 0.479086 | 0.0880231 | 0.146984 | 0.803922 | 0.833333 | -0.0294118 | 0.150018 | 0.581491 | 0.843382 | 0.93876 | 0.142892 |
| tossup_correctness | category | Religion | 372 | 0.646359 | 0.600869 | 0.0967137 | 0.207842 | 0.680108 | 0.709677 | -0.0295699 | 0.168525 | 0.397604 | 0.627402 | 0.852632 | 0.207066 |
| tossup_correctness | category | Science | 1487 | 0.632025 | 0.578176 | 0.107731 | 0.197409 | 0.680565 | 0.752522 | -0.071957 | 0.188046 | 0.401342 | 0.669035 | 0.901387 | 0.190384 |
| tossup_correctness | category | Social Science | 336 | 0.690847 | 0.579317 | 0.0660438 | 0.196713 | 0.705357 | 0.702381 | 0.00297619 | 0.186351 | 0.37509 | 0.656764 | 0.877363 | 0.19626 |
| tossup_correctness | category | Unknown | 1886 | 0.663987 | 0.578625 | 0.12826 | 0.19678 | 0.704136 | 0.746023 | -0.0418876 | 0.170753 | 0.388037 | 0.629548 | 0.846682 | 0.205909 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.691379 | 0.53028 | 0.0608153 | 0.172734 | 0.77665 | 0.736041 | 0.0406091 | 0.162985 | 0.502433 | 0.793382 | 0.9163 | 0.164065 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.70895 | 0.525942 | 0.0313749 | 0.174444 | 0.740102 | 0.735025 | 0.00507614 | 0.175681 | 0.475334 | 0.777794 | 0.929797 | 0.162921 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.684026 | 0.518958 | 0.0665096 | 0.170536 | 0.753887 | 0.769436 | -0.0155486 | 0.178151 | 0.460261 | 0.74614 | 0.91651 | 0.173226 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.68615 | 0.528012 | 0.120971 | 0.175246 | 0.739707 | 0.78402 | -0.0443126 | 0.17742 | 0.414894 | 0.679366 | 0.889028 | 0.191214 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.646778 | 0.600137 | 0.16735 | 0.207017 | 0.676235 | 0.756008 | -0.079773 | 0.159292 | 0.370904 | 0.596384 | 0.797056 | 0.216766 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 4.02013 | 0.542305 | 2.17085 | 3.15507 | 3.62806 | 4.03646 | 4.39459 | 4.9 | 5.52081 |
| player | theta_1 | 1186 | -0.371726 | 1.04642 | -3.04608 | -1.91655 | -1.16186 | -0.484737 | 0.351039 | 1.56049 | 2.73723 |
| player | theta_2 | 1186 | -0.561048 | 0.726563 | -2.5911 | -1.64496 | -1.09211 | -0.611445 | -0.0670819 | 0.715896 | 1.60369 |
| player | theta_3 | 1186 | -0.381929 | 0.722758 | -2.67079 | -1.56459 | -0.882296 | -0.373695 | 0.090511 | 0.783553 | 1.77357 |
| player | theta_norm | 1186 | 1.52664 | 0.641862 | 0.171454 | 0.542707 | 1.05096 | 1.48236 | 1.9894 | 2.64765 | 3.66488 |
| tossup | beta_1 | 1240 | -0.595657 | 0.757554 | -3.64829 | -2.42995 | -0.748046 | -0.346525 | -0.139387 | 0.155463 | 0.725954 |
| tossup | beta_2 | 1240 | -0.416682 | 0.678369 | -3.70573 | -2.19579 | -0.400842 | -0.227282 | -0.127319 | 0.125031 | 1.83421 |
| tossup | beta_3 | 1240 | -0.467738 | 0.706641 | -3.24281 | -2.31562 | -0.45632 | -0.253604 | -0.134165 | 0.141986 | 2.58243 |
| tossup | gamma_1 | 1240 | 5.51604 | 3.69988 | 0.648442 | 2.89233 | 4.37797 | 4.81308 | 5.17577 | 12.4726 | 44.22 |
| tossup | gamma_2 | 1240 | 5.49632 | 3.45208 | 0.617388 | 3.99009 | 4.61398 | 4.88012 | 5.1689 | 9.06531 | 48.6185 |
| tossup | gamma_3 | 1240 | 5.49388 | 3.45833 | 0.764266 | 3.64589 | 4.6309 | 4.89093 | 5.17468 | 10.3335 | 60.3445 |
| tossup | mu_1 | 1240 | 0.560389 | 0.11801 | 0.438239 | 0.475029 | 0.495748 | 0.511825 | 0.554358 | 0.870699 | 0.954093 |
| tossup | mu_2 | 1240 | 0.538284 | 0.103729 | 0.428682 | 0.476855 | 0.494095 | 0.506058 | 0.520414 | 0.846809 | 0.965605 |
| tossup | mu_3 | 1240 | 0.546321 | 0.111306 | 0.454786 | 0.477257 | 0.493554 | 0.507657 | 0.524805 | 0.861701 | 0.954189 |
| tossup | r_1 | 1240 | 0.402627 | 0.242354 | 0.0380745 | 0.0703937 | 0.173544 | 0.379839 | 0.622421 | 0.795544 | 0.865722 |
| tossup | r_2 | 1240 | 0.278519 | 0.212614 | 0.0462834 | 0.0690436 | 0.119784 | 0.203849 | 0.371151 | 0.783722 | 0.899857 |
| tossup | r_3 | 1240 | 0.318854 | 0.217869 | 0.0555404 | 0.0842325 | 0.149408 | 0.256754 | 0.416285 | 0.821057 | 0.897785 |
| tossup | r_norm | 1240 | 0.696184 | 0.0892629 | 0.577382 | 0.585266 | 0.616944 | 0.675865 | 0.767833 | 0.855899 | 0.902686 |
| tossup_hazard | hazard_beta_1 | 1240 | 2.0575 | 1.51995 | -0.0586414 | 0.425346 | 0.679774 | 1.35055 | 3.64622 | 4.52795 | 5.29171 |
| tossup_hazard | hazard_beta_2 | 1240 | 1.96414 | 1.30535 | 0.118721 | 0.388442 | 0.732491 | 1.62507 | 3.28459 | 3.97338 | 4.8917 |
| tossup_hazard | hazard_beta_3 | 1240 | 1.70782 | 1.28762 | -0.107701 | 0.413936 | 0.666065 | 1.1333 | 2.75173 | 4.1268 | 4.91465 |
| tossup_hazard | hazard_gamma_1 | 1240 | 13.6233 | 31.5454 | 2.92498 | 5.50204 | 6.32643 | 7.38981 | 10.8113 | 41.8347 | 868.326 |
| tossup_hazard | hazard_gamma_2 | 1240 | 14.4252 | 23.7401 | 2.79595 | 5.48951 | 6.4235 | 8.07745 | 13.2496 | 39.2427 | 360.015 |
| tossup_hazard | hazard_gamma_3 | 1240 | 13.9062 | 34.3593 | 2.98005 | 5.51204 | 6.30423 | 7.36857 | 10.4531 | 32.9877 | 694.819 |
| tossup_hazard | hazard_mu_1 | 1240 | 0.604458 | 0.105527 | 0.292399 | 0.485183 | 0.5341 | 0.569835 | 0.662952 | 0.814209 | 0.956574 |
| tossup_hazard | hazard_mu_2 | 1240 | 0.598763 | 0.105979 | 0.213101 | 0.472663 | 0.526996 | 0.569684 | 0.66156 | 0.800664 | 0.975533 |
| tossup_hazard | hazard_mu_3 | 1240 | 0.59529 | 0.0982954 | 0.242101 | 0.49013 | 0.530525 | 0.56674 | 0.642884 | 0.803913 | 0.94331 |
| tossup_hazard | hazard_r_1 | 1240 | 0.357856 | 0.354581 | 0.0186011 | 0.0341161 | 0.0539611 | 0.129765 | 0.779876 | 0.916695 | 0.962773 |
| tossup_hazard | hazard_r_2 | 1240 | 0.369296 | 0.342012 | 0.00829871 | 0.0240825 | 0.0642741 | 0.175015 | 0.763321 | 0.901932 | 0.957601 |
| tossup_hazard | hazard_r_3 | 1240 | 0.272849 | 0.305115 | 0.0142712 | 0.0307359 | 0.0539011 | 0.107737 | 0.469459 | 0.878941 | 0.930675 |
