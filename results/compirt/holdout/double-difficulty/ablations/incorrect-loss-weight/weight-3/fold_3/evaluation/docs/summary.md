# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-3/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/incorrect-loss-weight/weight-3/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 299165 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.705391 |
| log_loss | 0.587886 |
| ece | 0.187252 |
| brier | 0.201189 |
| accuracy | 0.688546 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0814978 |
| probability_std | 0.215229 |
| probability_p10 | 0.276253 |
| probability_p50 | 0.605816 |
| probability_p90 | 0.851748 |
| mean_predictive_variance | 0.196822 |
| integrated_brier_score | 0.101221 |
| joint_tossup_event_log_loss | 6.68204 |
| buzz_position_mae | 0.151899 |
| buzz_position_median_absolute_error | 0.135361 |
| buzz_position_bias | -0.0490756 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.348678 |
| first_buzzer_mean_reciprocal_rank | 0.566351 |
| first_buzzer_log_loss | 1.67099 |
| first_buzzer_events | 9080 |
| neg_auroc | 0.705391 |
| neg_average_precision | 0.444574 |
| neg_precision | 0.38254 |
| neg_recall | 0.577107 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.183477 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0152012 |
| no_buzz_calibration_error | 1.68492e-05 |
| no_buzz_brier | 0.0136857 |
| full_pmf_max_mass_error | 1.33227e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.705391 | 0.587886 | 0.187252 | 0.201189 | 0.688546 | 0.770044 | -0.0814978 | 0.215229 | 0.276253 | 0.605816 | 0.851748 | 0.196822 |
| tossup_correctness | tier | fall | 2817 | 0.698596 | 0.575936 | 0.179398 | 0.195608 | 0.70394 | 0.781683 | -0.0777423 | 0.216933 | 0.282567 | 0.634869 | 0.864092 | 0.192301 |
| tossup_correctness | tier | nationals | 1542 | 0.722327 | 0.60849 | 0.190383 | 0.21035 | 0.666018 | 0.73476 | -0.0687419 | 0.218213 | 0.231688 | 0.560953 | 0.829172 | 0.200188 |
| tossup_correctness | tier | regionals | 1934 | 0.707143 | 0.591154 | 0.181333 | 0.202855 | 0.682523 | 0.75698 | -0.0744571 | 0.210685 | 0.280351 | 0.596084 | 0.841943 | 0.199889 |
| tossup_correctness | tier | winter | 2787 | 0.695505 | 0.586296 | 0.199806 | 0.200605 | 0.68963 | 0.786868 | -0.0972372 | 0.212177 | 0.290297 | 0.609986 | 0.851865 | 0.197401 |
| tossup_correctness | category | Current Events | 125 | 0.734951 | 0.598016 | 0.166055 | 0.208487 | 0.656 | 0.704 | -0.048 | 0.224958 | 0.232134 | 0.541076 | 0.853895 | 0.197954 |
| tossup_correctness | category | Fine Arts | 1072 | 0.719192 | 0.579028 | 0.18857 | 0.197846 | 0.692164 | 0.770522 | -0.0783582 | 0.218277 | 0.271997 | 0.603235 | 0.852083 | 0.195634 |
| tossup_correctness | category | Geography | 185 | 0.764196 | 0.62664 | 0.21329 | 0.217327 | 0.686486 | 0.702703 | -0.0162162 | 0.238167 | 0.155599 | 0.515563 | 0.786184 | 0.193164 |
| tossup_correctness | category | History | 1443 | 0.732392 | 0.591032 | 0.197041 | 0.202433 | 0.688843 | 0.765073 | -0.0762301 | 0.221339 | 0.247968 | 0.589793 | 0.847326 | 0.19638 |
| tossup_correctness | category | Literature | 1411 | 0.656084 | 0.553746 | 0.174549 | 0.18562 | 0.722183 | 0.81219 | -0.0900071 | 0.196608 | 0.343758 | 0.670586 | 0.871517 | 0.191822 |
| tossup_correctness | category | Mythology | 320 | 0.661775 | 0.572856 | 0.183985 | 0.192521 | 0.709375 | 0.79375 | -0.084375 | 0.19723 | 0.331523 | 0.64697 | 0.859956 | 0.196366 |
| tossup_correctness | category | Other Academic | 64 | 0.636719 | 0.639543 | 0.202636 | 0.220351 | 0.65625 | 0.75 | -0.09375 | 0.186793 | 0.344978 | 0.58913 | 0.819112 | 0.2069 |
| tossup_correctness | category | Philosophy | 312 | 0.668903 | 0.567997 | 0.199172 | 0.194941 | 0.698718 | 0.801282 | -0.102564 | 0.190542 | 0.355327 | 0.606082 | 0.85259 | 0.202977 |
| tossup_correctness | category | Popular Culture | 104 | 0.59517 | 0.51843 | 0.198534 | 0.166774 | 0.807692 | 0.846154 | -0.0384615 | 0.151083 | 0.480569 | 0.705415 | 0.857312 | 0.194582 |
| tossup_correctness | category | Religion | 358 | 0.712912 | 0.630284 | 0.194497 | 0.218969 | 0.645251 | 0.726257 | -0.0810056 | 0.206678 | 0.253604 | 0.533248 | 0.812117 | 0.206276 |
| tossup_correctness | category | Science | 1431 | 0.691471 | 0.608689 | 0.199105 | 0.210969 | 0.663173 | 0.765199 | -0.102027 | 0.220708 | 0.253689 | 0.584912 | 0.842483 | 0.196683 |
| tossup_correctness | category | Social Science | 321 | 0.721808 | 0.613915 | 0.19829 | 0.211636 | 0.676012 | 0.744548 | -0.0685358 | 0.237777 | 0.215272 | 0.571241 | 0.848202 | 0.1912 |
| tossup_correctness | category | Unknown | 1934 | 0.707143 | 0.591154 | 0.181333 | 0.202855 | 0.682523 | 0.75698 | -0.0744571 | 0.210685 | 0.280351 | 0.596084 | 0.841943 | 0.199889 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.739321 | 0.628411 | 0.184266 | 0.215952 | 0.671875 | 0.697917 | -0.0260417 | 0.204987 | 0.23415 | 0.526616 | 0.77606 | 0.207794 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.737329 | 0.585346 | 0.175166 | 0.200685 | 0.692913 | 0.733408 | -0.0404949 | 0.218985 | 0.243591 | 0.576267 | 0.835311 | 0.198653 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.683259 | 0.596377 | 0.165622 | 0.203815 | 0.686425 | 0.759276 | -0.0728507 | 0.214642 | 0.283834 | 0.617268 | 0.862406 | 0.195158 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.68812 | 0.572077 | 0.183474 | 0.194999 | 0.698501 | 0.789125 | -0.0906239 | 0.204662 | 0.311983 | 0.634804 | 0.855993 | 0.196951 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.725001 | 0.595101 | 0.21121 | 0.204467 | 0.680137 | 0.775342 | -0.0952055 | 0.221837 | 0.248969 | 0.584816 | 0.842867 | 0.196675 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 2.66043 | 0.796376 | 0.487071 | 1.39289 | 2.089 | 2.65837 | 3.20538 | 4.02682 | 4.67075 |
| player | theta_1 | 1133 | -1.26876 | 0.990077 | -4.5472 | -2.80069 | -1.89846 | -1.34126 | -0.710831 | 0.447012 | 2.64402 |
| player | theta_2 | 1133 | -1.02086 | 0.764598 | -3.62579 | -2.27608 | -1.49977 | -1.0216 | -0.535729 | 0.249244 | 1.23881 |
| player | theta_3 | 1133 | -1.11834 | 0.860028 | -3.55533 | -2.49602 | -1.69859 | -1.16687 | -0.586976 | 0.404627 | 1.8067 |
| player | theta_norm | 1133 | 2.36727 | 0.775647 | 0.242715 | 1.15498 | 1.81574 | 2.34985 | 2.88561 | 3.68357 | 4.77052 |
| tossup | start_difficulty_d1 | 1240 | -0.745009 | 0.675703 | -3.29025 | -1.78196 | -1.12057 | -0.789202 | -0.381827 | 0.392775 | 2.46167 |
| tossup | start_difficulty_d2 | 1240 | -0.725007 | 0.615243 | -3.57532 | -1.67133 | -1.09623 | -0.7348 | -0.373296 | 0.322785 | 1.65897 |
| tossup | start_difficulty_d3 | 1240 | -0.720539 | 0.614853 | -3.3177 | -1.7622 | -1.09507 | -0.746981 | -0.355598 | 0.343346 | 1.77646 |
| tossup | end_difficulty_d1 | 1240 | -1.74944 | 0.803889 | -5.62932 | -2.99678 | -2.21038 | -1.79169 | -1.29172 | -0.402322 | 1.87278 |
| tossup | end_difficulty_d2 | 1240 | -1.71938 | 0.729427 | -5.27139 | -2.89142 | -2.14732 | -1.72901 | -1.31251 | -0.499715 | 1.05106 |
| tossup | end_difficulty_d3 | 1240 | -1.71106 | 0.720664 | -4.95764 | -2.92526 | -2.13423 | -1.7144 | -1.27748 | -0.526004 | 1.07243 |
| tossup | total_drop_d1 | 1240 | 1.00443 | 0.204806 | 0.576986 | 0.740196 | 0.895889 | 0.988844 | 1.08003 | 1.29088 | 3.47492 |
| tossup | total_drop_d2 | 1240 | 0.994375 | 0.173908 | 0.607904 | 0.775072 | 0.902505 | 0.982222 | 1.05908 | 1.23214 | 3.63902 |
| tossup | total_drop_d3 | 1240 | 0.990517 | 0.158543 | 0.576447 | 0.784106 | 0.894425 | 0.980306 | 1.05757 | 1.24045 | 2.49003 |
| tossup | drop_share_1_d1 | 1240 | 0.301395 | 0.0230357 | 0.124085 | 0.265774 | 0.290089 | 0.302653 | 0.314774 | 0.332748 | 0.418511 |
| tossup | drop_share_2_d1 | 1240 | 0.347438 | 0.0138634 | 0.283432 | 0.326106 | 0.338687 | 0.347337 | 0.355781 | 0.368799 | 0.440668 |
| tossup | drop_share_3_d1 | 1240 | 0.351167 | 0.0243199 | 0.234919 | 0.316564 | 0.336397 | 0.350019 | 0.363099 | 0.390338 | 0.536575 |
| tossup | drop_share_1_d2 | 1240 | 0.301461 | 0.0194755 | 0.154426 | 0.271257 | 0.291333 | 0.302462 | 0.312883 | 0.32971 | 0.399163 |
| tossup | drop_share_2_d2 | 1240 | 0.346951 | 0.0135363 | 0.298161 | 0.326348 | 0.338434 | 0.34691 | 0.354839 | 0.36806 | 0.44294 |
| tossup | drop_share_3_d2 | 1240 | 0.351587 | 0.0207799 | 0.253736 | 0.320553 | 0.338675 | 0.351439 | 0.362365 | 0.385354 | 0.471156 |
| tossup | drop_share_1_d3 | 1240 | 0.301261 | 0.0210688 | 0.1374 | 0.267564 | 0.291484 | 0.302165 | 0.313321 | 0.330918 | 0.388784 |
| tossup | drop_share_2_d3 | 1240 | 0.347101 | 0.0131196 | 0.22638 | 0.327042 | 0.339037 | 0.346972 | 0.354863 | 0.367155 | 0.425518 |
| tossup | drop_share_3_d3 | 1240 | 0.351638 | 0.0230794 | 0.284573 | 0.319483 | 0.338494 | 0.350476 | 0.362102 | 0.38716 | 0.63622 |
| tossup | r_1 | 1240 | 0.350522 | 0.227032 | 0.0384158 | 0.0731396 | 0.154946 | 0.30083 | 0.535697 | 0.762215 | 0.895427 |
| tossup | r_2 | 1240 | 0.324087 | 0.2014 | 0.0420793 | 0.0855241 | 0.160519 | 0.269362 | 0.45667 | 0.728698 | 0.915755 |
| tossup | r_3 | 1240 | 0.325391 | 0.203306 | 0.0458289 | 0.0867775 | 0.157743 | 0.274885 | 0.459112 | 0.735199 | 0.894194 |
| tossup | r_norm | 1240 | 0.679296 | 0.0752988 | 0.577392 | 0.584729 | 0.618063 | 0.662242 | 0.729395 | 0.825702 | 0.917706 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.4779 | 0.507037 | 1.99292 | 3.74243 | 4.17724 | 4.4276 | 4.73617 | 5.40381 | 6.3664 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.43916 | 0.417745 | 2.14187 | 3.81906 | 4.21294 | 4.41431 | 4.64054 | 5.15373 | 6.59545 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.44984 | 0.434398 | 2.4033 | 3.74029 | 4.20855 | 4.43177 | 4.68473 | 5.17587 | 6.03649 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.65184 | 2.35864 | -12.0702 | -3.10008 | 0.49314 | 2.77259 | 3.26972 | 3.62258 | 4.51135 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.31551 | 2.00289 | -8.53368 | -2.32071 | 2.47551 | 3.10821 | 3.38005 | 3.7006 | 4.07523 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.21678 | 2.05243 | -9.30733 | -2.4339 | 2.17745 | 3.08015 | 3.3731 | 3.73964 | 4.22492 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.82606 | 2.5242 | 0.856225 | 0.98503 | 1.06729 | 1.3691 | 4.3082 | 7.98303 | 16.6977 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.12365 | 2.16354 | 0.89484 | 0.960005 | 1.01916 | 1.15605 | 1.8079 | 7.31093 | 13.9226 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.23306 | 2.17928 | 0.874409 | 0.966447 | 1.02813 | 1.19975 | 2.09452 | 7.42503 | 13.8566 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.233839 | 0.0817308 | 0.0322742 | 0.080215 | 0.173919 | 0.26775 | 0.293869 | 0.317021 | 0.51521 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.341 | 0.0765709 | 0.0604652 | 0.177816 | 0.333836 | 0.351112 | 0.365207 | 0.445392 | 0.715276 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.425161 | 0.133286 | 0.107712 | 0.304212 | 0.347533 | 0.370472 | 0.459501 | 0.731366 | 0.895786 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.253984 | 0.0685309 | 0.0385099 | 0.0912982 | 0.235215 | 0.280497 | 0.296732 | 0.314582 | 0.611778 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.348698 | 0.0593232 | 0.0530975 | 0.245597 | 0.340545 | 0.351265 | 0.36276 | 0.409907 | 0.692287 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.397318 | 0.102071 | 0.171747 | 0.320603 | 0.348871 | 0.36414 | 0.39646 | 0.646574 | 0.908393 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.250677 | 0.0692773 | 0.040731 | 0.0949061 | 0.229712 | 0.275763 | 0.296508 | 0.315248 | 0.538492 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.350048 | 0.0591688 | 0.0842434 | 0.241901 | 0.3396 | 0.351093 | 0.364531 | 0.42394 | 0.707665 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.399275 | 0.102221 | 0.0703285 | 0.319782 | 0.349474 | 0.366595 | 0.405635 | 0.64483 | 0.864527 |
| tossup_hazard | hazard_r_1 | 1240 | 0.393087 | 0.277281 | 0.0256093 | 0.0576598 | 0.145893 | 0.326033 | 0.619226 | 0.884949 | 0.951429 |
| tossup_hazard | hazard_r_2 | 1240 | 0.286502 | 0.205577 | 0.0295769 | 0.0534473 | 0.114515 | 0.227266 | 0.430584 | 0.694534 | 0.866291 |
| tossup_hazard | hazard_r_3 | 1240 | 0.320411 | 0.227223 | 0.0178487 | 0.047437 | 0.132936 | 0.257057 | 0.479651 | 0.752247 | 0.927983 |
