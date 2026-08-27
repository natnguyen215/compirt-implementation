# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/optimization-steps/steps-20000/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/optimization-steps/steps-20000/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 20000 |
| pyramidal | final_loss | 277376 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.711538 |
| log_loss | 0.485456 |
| ece | 0.0105123 |
| brier | 0.15696 |
| accuracy | 0.785683 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0156388 |
| probability_std | 0.147952 |
| probability_p10 | 0.567305 |
| probability_p50 | 0.808361 |
| probability_p90 | 0.919445 |
| mean_predictive_variance | 0.154412 |
| integrated_brier_score | 0.0940272 |
| joint_tossup_event_log_loss | 6.42511 |
| buzz_position_mae | 0.138579 |
| buzz_position_median_absolute_error | 0.116518 |
| buzz_position_bias | -0.00852571 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.360793 |
| first_buzzer_mean_reciprocal_rank | 0.575579 |
| first_buzzer_log_loss | 1.63938 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.711538 |
| neg_average_precision | 0.448262 |
| neg_precision | 0.629562 |
| neg_recall | 0.16523 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.176998 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0108346 |
| no_buzz_calibration_error | -0.00434977 |
| no_buzz_brier | 0.0138674 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.711538 | 0.485456 | 0.0105123 | 0.15696 | 0.785683 | 0.770044 | 0.0156388 | 0.147952 | 0.567305 | 0.808361 | 0.919445 | 0.154412 |
| tossup_correctness | tier | fall | 2817 | 0.703872 | 0.477309 | 0.013158 | 0.153143 | 0.793042 | 0.781683 | 0.0113596 | 0.14167 | 0.57051 | 0.816579 | 0.919967 | 0.15278 |
| tossup_correctness | tier | nationals | 1542 | 0.727782 | 0.512471 | 0.0284923 | 0.169362 | 0.759403 | 0.73476 | 0.0246433 | 0.156737 | 0.529578 | 0.792772 | 0.91527 | 0.15964 |
| tossup_correctness | tier | regionals | 1934 | 0.715745 | 0.497565 | 0.0156405 | 0.162159 | 0.770424 | 0.75698 | 0.0134436 | 0.147597 | 0.563931 | 0.804931 | 0.91797 | 0.155343 |
| tossup_correctness | tier | winter | 2787 | 0.702478 | 0.47034 | 0.0284693 | 0.150348 | 0.803373 | 0.786868 | 0.0165052 | 0.148816 | 0.579868 | 0.810659 | 0.922126 | 0.152522 |
| tossup_correctness | category | Current Events | 125 | 0.765663 | 0.519994 | 0.0664972 | 0.175636 | 0.72 | 0.704 | 0.016 | 0.146051 | 0.524479 | 0.766984 | 0.905384 | 0.170857 |
| tossup_correctness | category | Fine Arts | 1072 | 0.729724 | 0.473498 | 0.0208971 | 0.152276 | 0.794776 | 0.770522 | 0.0242537 | 0.151718 | 0.564864 | 0.815448 | 0.919646 | 0.154176 |
| tossup_correctness | category | Geography | 185 | 0.783636 | 0.486493 | 0.05214 | 0.158893 | 0.767568 | 0.702703 | 0.0648649 | 0.212769 | 0.390347 | 0.758807 | 0.904204 | 0.168091 |
| tossup_correctness | category | History | 1443 | 0.724747 | 0.48769 | 0.0342637 | 0.159891 | 0.777547 | 0.765073 | 0.012474 | 0.152675 | 0.536787 | 0.796973 | 0.913681 | 0.159382 |
| tossup_correctness | category | Literature | 1411 | 0.664316 | 0.458578 | 0.0260067 | 0.144467 | 0.810064 | 0.81219 | -0.00212615 | 0.121934 | 0.655073 | 0.839976 | 0.92843 | 0.139051 |
| tossup_correctness | category | Mythology | 320 | 0.661895 | 0.482047 | 0.0360522 | 0.151625 | 0.80625 | 0.79375 | 0.0125 | 0.119196 | 0.627349 | 0.827918 | 0.927589 | 0.146666 |
| tossup_correctness | category | Other Academic | 64 | 0.66276 | 0.547835 | 0.130062 | 0.183751 | 0.71875 | 0.75 | -0.03125 | 0.109616 | 0.627426 | 0.802396 | 0.905111 | 0.15323 |
| tossup_correctness | category | Philosophy | 312 | 0.660194 | 0.466742 | 0.0395023 | 0.148165 | 0.814103 | 0.801282 | 0.0128205 | 0.115743 | 0.635207 | 0.810491 | 0.913241 | 0.154034 |
| tossup_correctness | category | Popular Culture | 104 | 0.639205 | 0.413877 | 0.0567299 | 0.123959 | 0.846154 | 0.846154 | 0 | 0.0717886 | 0.734329 | 0.852334 | 0.916957 | 0.131075 |
| tossup_correctness | category | Religion | 358 | 0.707221 | 0.537891 | 0.0404961 | 0.179685 | 0.743017 | 0.726257 | 0.0167598 | 0.147798 | 0.550156 | 0.765248 | 0.896949 | 0.171175 |
| tossup_correctness | category | Science | 1431 | 0.70402 | 0.489529 | 0.024228 | 0.158297 | 0.793152 | 0.765199 | 0.0279525 | 0.150144 | 0.551407 | 0.796555 | 0.917026 | 0.158379 |
| tossup_correctness | category | Social Science | 321 | 0.723798 | 0.502194 | 0.0346313 | 0.162533 | 0.772586 | 0.744548 | 0.0280374 | 0.184314 | 0.478236 | 0.785335 | 0.922284 | 0.159983 |
| tossup_correctness | category | Unknown | 1934 | 0.715745 | 0.497565 | 0.0156405 | 0.162159 | 0.770424 | 0.75698 | 0.0134436 | 0.147597 | 0.563931 | 0.804931 | 0.91797 | 0.155343 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.741379 | 0.542835 | 0.0695305 | 0.184109 | 0.713542 | 0.697917 | 0.015625 | 0.165809 | 0.465802 | 0.744538 | 0.87793 | 0.179438 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.748783 | 0.498655 | 0.0210719 | 0.163749 | 0.768279 | 0.733408 | 0.0348706 | 0.152272 | 0.537065 | 0.787479 | 0.910386 | 0.162977 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.685851 | 0.515145 | 0.0270515 | 0.16801 | 0.768326 | 0.759276 | 0.00904977 | 0.14634 | 0.569151 | 0.810042 | 0.920659 | 0.153145 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.699939 | 0.468256 | 0.01918 | 0.149822 | 0.803764 | 0.789125 | 0.0146392 | 0.132386 | 0.608011 | 0.822428 | 0.922995 | 0.148318 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.725792 | 0.472094 | 0.0154338 | 0.151757 | 0.791096 | 0.775342 | 0.0157534 | 0.157899 | 0.540061 | 0.801963 | 0.919075 | 0.157106 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 0.793123 | 0.848362 | -1.43571 | -0.585275 | 0.20774 | 0.790137 | 1.3421 | 2.28975 | 3.07779 |
| player | theta_1 | 1133 | -0.378043 | 0.950186 | -2.97759 | -1.71161 | -1.01576 | -0.484989 | 0.117295 | 1.49347 | 4.36971 |
| player | theta_2 | 1133 | -0.380372 | 0.801538 | -2.86892 | -1.6762 | -0.866368 | -0.444265 | 0.108739 | 1.02031 | 2.67092 |
| player | theta_3 | 1133 | -0.424166 | 0.879198 | -2.74234 | -1.73145 | -1.03261 | -0.527929 | 0.105632 | 1.21895 | 2.94679 |
| player | theta_norm | 1133 | 1.53316 | 0.65846 | 0.185579 | 0.589282 | 1.07137 | 1.45794 | 1.93689 | 2.74182 | 4.83282 |
| tossup | start_difficulty_d1 | 1240 | -0.959869 | 0.542045 | -2.97844 | -1.70318 | -1.29506 | -1.01116 | -0.675186 | -0.0157596 | 2.17493 |
| tossup | start_difficulty_d2 | 1240 | -0.970984 | 0.493242 | -2.57307 | -1.72018 | -1.28803 | -1.00587 | -0.685313 | -0.168168 | 1.55557 |
| tossup | start_difficulty_d3 | 1240 | -0.968908 | 0.496185 | -2.77918 | -1.72814 | -1.28941 | -0.991757 | -0.646792 | -0.159742 | 0.886638 |
| tossup | end_difficulty_d1 | 1240 | -1.95701 | 0.635561 | -4.39343 | -2.8478 | -2.34953 | -2.01575 | -1.59832 | -0.883667 | 1.49976 |
| tossup | end_difficulty_d2 | 1240 | -1.96853 | 0.581964 | -3.82459 | -2.83255 | -2.34564 | -1.99952 | -1.62056 | -0.984974 | 0.928373 |
| tossup | end_difficulty_d3 | 1240 | -1.9667 | 0.582429 | -4.06414 | -2.86828 | -2.35109 | -1.98241 | -1.58768 | -1.0503 | 0.192588 |
| tossup | total_drop_d1 | 1240 | 0.997137 | 0.113526 | 0.628723 | 0.811447 | 0.923251 | 0.997552 | 1.06704 | 1.17829 | 1.55069 |
| tossup | total_drop_d2 | 1240 | 0.997543 | 0.106705 | 0.627193 | 0.821051 | 0.93207 | 0.998291 | 1.06587 | 1.16822 | 1.44403 |
| tossup | total_drop_d3 | 1240 | 0.997792 | 0.108817 | 0.633678 | 0.827214 | 0.926954 | 0.993449 | 1.06428 | 1.1704 | 1.6664 |
| tossup | drop_share_1_d1 | 1240 | 0.304557 | 0.0153999 | 0.237313 | 0.279804 | 0.295207 | 0.305308 | 0.314515 | 0.327201 | 0.370367 |
| tossup | drop_share_2_d1 | 1240 | 0.346677 | 0.0113721 | 0.304711 | 0.328275 | 0.339024 | 0.346322 | 0.354442 | 0.365962 | 0.388115 |
| tossup | drop_share_3_d1 | 1240 | 0.348765 | 0.0163274 | 0.28752 | 0.323818 | 0.337723 | 0.348507 | 0.358475 | 0.376781 | 0.436189 |
| tossup | drop_share_1_d2 | 1240 | 0.304396 | 0.0142487 | 0.250407 | 0.280827 | 0.295816 | 0.304559 | 0.312817 | 0.32871 | 0.357974 |
| tossup | drop_share_2_d2 | 1240 | 0.347347 | 0.0109549 | 0.311693 | 0.329101 | 0.339686 | 0.347277 | 0.354444 | 0.365726 | 0.382823 |
| tossup | drop_share_3_d2 | 1240 | 0.348258 | 0.0154619 | 0.305628 | 0.323093 | 0.338512 | 0.347806 | 0.3574 | 0.374594 | 0.418577 |
| tossup | drop_share_1_d3 | 1240 | 0.305023 | 0.0149914 | 0.219599 | 0.280292 | 0.296113 | 0.304885 | 0.315284 | 0.328835 | 0.360654 |
| tossup | drop_share_2_d3 | 1240 | 0.346965 | 0.0113788 | 0.309374 | 0.328764 | 0.339363 | 0.34671 | 0.354446 | 0.365488 | 0.418097 |
| tossup | drop_share_3_d3 | 1240 | 0.348011 | 0.0154776 | 0.29758 | 0.323809 | 0.337656 | 0.34721 | 0.357682 | 0.3742 | 0.429687 |
| tossup | r_1 | 1240 | 0.319168 | 0.161354 | 0.040984 | 0.114127 | 0.190875 | 0.284807 | 0.422548 | 0.627135 | 0.865555 |
| tossup | r_2 | 1240 | 0.339468 | 0.157693 | 0.0629334 | 0.127868 | 0.223577 | 0.309907 | 0.437587 | 0.644526 | 0.857396 |
| tossup | r_3 | 1240 | 0.341364 | 0.160143 | 0.0561178 | 0.12837 | 0.221152 | 0.309085 | 0.436943 | 0.659092 | 0.82728 |
| tossup | r_norm | 1240 | 0.637894 | 0.0567074 | 0.577423 | 0.581033 | 0.594911 | 0.618979 | 0.662033 | 0.761141 | 0.870902 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 8.60483 | 0.518006 | 5.29529 | 7.61064 | 8.45739 | 8.6301 | 8.83206 | 9.40619 | 10.2841 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 8.68813 | 0.475535 | 5.49212 | 7.9927 | 8.54117 | 8.66298 | 8.84874 | 9.41222 | 11.1402 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 8.64475 | 0.513642 | 5.38408 | 7.74491 | 8.51325 | 8.65853 | 8.85851 | 9.44796 | 10.7215 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 4.87055 | 3.87625 | -10.7517 | -2.79205 | 2.068 | 7.43265 | 7.6499 | 7.95891 | 8.50524 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 5.71198 | 3.70479 | -14.7633 | -2.55561 | 5.00267 | 7.56683 | 7.73924 | 8.07159 | 8.89516 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 5.27694 | 3.66849 | -8.89559 | -2.25646 | 2.41715 | 7.53501 | 7.71158 | 8.05353 | 8.9054 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.73428 | 3.90473 | 0.825144 | 0.947269 | 0.997962 | 1.05693 | 6.5356 | 11.6798 | 19.6102 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.97615 | 3.77495 | 0.877918 | 0.931675 | 0.978149 | 1.02072 | 3.45245 | 11.4973 | 23.6262 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 3.36781 | 3.67586 | 0.811994 | 0.935265 | 0.985082 | 1.03546 | 6.08831 | 10.8453 | 18.2552 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.280916 | 0.0989338 | 0.0495681 | 0.10496 | 0.259984 | 0.297634 | 0.309575 | 0.439292 | 0.748886 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.323608 | 0.0817207 | 0.0671858 | 0.152052 | 0.320058 | 0.343222 | 0.355328 | 0.421884 | 0.716087 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.395477 | 0.13095 | 0.0731737 | 0.229454 | 0.341461 | 0.355113 | 0.390525 | 0.70485 | 0.880759 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.281222 | 0.0801526 | 0.0381939 | 0.111708 | 0.280493 | 0.298319 | 0.310025 | 0.338374 | 0.774461 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.331194 | 0.069428 | 0.0575205 | 0.168474 | 0.33272 | 0.344194 | 0.353667 | 0.394114 | 0.692762 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.387584 | 0.116091 | 0.129777 | 0.273625 | 0.342901 | 0.354132 | 0.371993 | 0.674659 | 0.904285 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.283499 | 0.0887742 | 0.0369329 | 0.10708 | 0.278438 | 0.298695 | 0.309922 | 0.403893 | 0.73549 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.328331 | 0.0738675 | 0.0681666 | 0.170439 | 0.326225 | 0.343684 | 0.354449 | 0.420584 | 0.666879 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.38817 | 0.120817 | 0.0587334 | 0.244176 | 0.341634 | 0.354756 | 0.377984 | 0.689486 | 0.8949 |
| tossup_hazard | hazard_r_1 | 1240 | 0.365148 | 0.303921 | 0.0169675 | 0.0403759 | 0.100933 | 0.223444 | 0.630311 | 0.907049 | 0.958536 |
| tossup_hazard | hazard_r_2 | 1240 | 0.293822 | 0.262855 | 0.0183451 | 0.0351989 | 0.077439 | 0.177326 | 0.476568 | 0.836 | 0.953989 |
| tossup_hazard | hazard_r_3 | 1240 | 0.34103 | 0.295354 | 0.0179944 | 0.0381271 | 0.0812224 | 0.20896 | 0.618899 | 0.871609 | 0.964154 |
