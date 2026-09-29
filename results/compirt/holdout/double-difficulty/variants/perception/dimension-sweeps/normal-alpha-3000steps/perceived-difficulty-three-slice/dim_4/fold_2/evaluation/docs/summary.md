# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_4/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_4/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 320575 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.648628 |
| log_loss | 0.522535 |
| ece | 0.0228948 |
| brier | 0.171373 |
| accuracy | 0.764395 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.000216053 |
| probability_std | 0.122716 |
| probability_p10 | 0.587448 |
| probability_p50 | 0.780694 |
| probability_p90 | 0.899213 |
| mean_predictive_variance | 0.16764 |
| integrated_brier_score | 0.10427 |
| joint_tossup_event_log_loss | 6.93702 |
| buzz_position_mae | 0.163462 |
| buzz_position_median_absolute_error | 0.146862 |
| buzz_position_bias | -0.0689742 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.349897 |
| first_buzzer_mean_reciprocal_rank | 0.563893 |
| first_buzzer_log_loss | 1.67662 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.652479 |
| tossup_scorer_player_top1_accuracy | 0.319296 |
| tossup_scorer_team_top1_accuracy | 0.488273 |
| tossup_game_winner_accuracy | 0.773913 |
| tossup_game_margin_mae | 36.8467 |
| tournament_player_ppg_spearman | 0.699103 |
| tournament_player_ppg_mae | 8.77498 |
| tournament_player_ppg_top10_overlap | 0.641379 |
| neg_auroc | 0.648628 |
| neg_average_precision | 0.363004 |
| neg_precision | 0.503106 |
| neg_recall | 0.0742098 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0562417 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0911262 |
| no_buzz_calibration_error | 0.0780132 |
| no_buzz_brier | 0.0246182 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9257 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 460 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.648628 | 0.522535 | 0.0228948 | 0.171373 | 0.764395 | 0.764178 | 0.000216053 | 0.122716 | 0.587448 | 0.780694 | 0.899213 | 0.16764 |
| tossup_correctness | tier | fall | 2798 | 0.655103 | 0.494613 | 0.0234163 | 0.159339 | 0.789135 | 0.785204 | 0.00393138 | 0.119818 | 0.606847 | 0.800621 | 0.908978 | 0.158993 |
| tossup_correctness | tier | nationals | 1545 | 0.64599 | 0.566423 | 0.0314355 | 0.19178 | 0.715858 | 0.721036 | -0.00517799 | 0.115346 | 0.539577 | 0.69661 | 0.834382 | 0.200647 |
| tossup_correctness | tier | regionals | 2039 | 0.617268 | 0.535315 | 0.0304439 | 0.176656 | 0.762138 | 0.762138 | 0 | 0.115629 | 0.594689 | 0.776233 | 0.885825 | 0.171479 |
| tossup_correctness | tier | winter | 2875 | 0.651608 | 0.517062 | 0.0251901 | 0.16837 | 0.768 | 0.768348 | -0.000347826 | 0.120122 | 0.616199 | 0.80685 | 0.912659 | 0.155594 |
| tossup_correctness | category | Current Events | 129 | 0.626825 | 0.620781 | 0.0622376 | 0.215434 | 0.666667 | 0.666667 | 0 | 0.109833 | 0.574529 | 0.74537 | 0.85631 | 0.188117 |
| tossup_correctness | category | Fine Arts | 1074 | 0.639164 | 0.512069 | 0.0291093 | 0.166587 | 0.77095 | 0.776536 | -0.00558659 | 0.120277 | 0.598017 | 0.79798 | 0.9095 | 0.160568 |
| tossup_correctness | category | Geography | 180 | 0.706489 | 0.624587 | 0.100902 | 0.214916 | 0.677778 | 0.616667 | 0.0611111 | 0.163118 | 0.458447 | 0.741565 | 0.89561 | 0.179775 |
| tossup_correctness | category | History | 1454 | 0.655353 | 0.52628 | 0.0307457 | 0.173818 | 0.755158 | 0.757909 | -0.00275103 | 0.122035 | 0.58607 | 0.785833 | 0.901772 | 0.165053 |
| tossup_correctness | category | Literature | 1435 | 0.642143 | 0.46852 | 0.0251687 | 0.146707 | 0.810453 | 0.810453 | 0 | 0.102408 | 0.670603 | 0.834652 | 0.930821 | 0.140553 |
| tossup_correctness | category | Mythology | 324 | 0.638132 | 0.499866 | 0.0583919 | 0.16186 | 0.790123 | 0.79321 | -0.00308642 | 0.129158 | 0.561212 | 0.759094 | 0.882804 | 0.176511 |
| tossup_correctness | category | Other Academic | 71 | 0.368192 | 0.612282 | 0.167247 | 0.208837 | 0.732394 | 0.760563 | -0.028169 | 0.0962546 | 0.575257 | 0.720856 | 0.837657 | 0.196219 |
| tossup_correctness | category | Philosophy | 310 | 0.647962 | 0.527357 | 0.0454271 | 0.174045 | 0.770968 | 0.76129 | 0.00967742 | 0.114976 | 0.612334 | 0.788783 | 0.918498 | 0.158688 |
| tossup_correctness | category | Popular Culture | 108 | 0.601562 | 0.405212 | 0.127673 | 0.121072 | 0.861111 | 0.888889 | -0.0277778 | 0.103008 | 0.629004 | 0.77992 | 0.872967 | 0.171156 |
| tossup_correctness | category | Religion | 361 | 0.62819 | 0.558314 | 0.060282 | 0.1865 | 0.720222 | 0.742382 | -0.0221607 | 0.132754 | 0.554136 | 0.771463 | 0.891121 | 0.171701 |
| tossup_correctness | category | Science | 1445 | 0.664661 | 0.535819 | 0.0338912 | 0.17768 | 0.750173 | 0.746021 | 0.00415225 | 0.124354 | 0.542316 | 0.736599 | 0.864324 | 0.187496 |
| tossup_correctness | category | Social Science | 327 | 0.705134 | 0.541638 | 0.0384431 | 0.180958 | 0.737003 | 0.718654 | 0.0183486 | 0.121659 | 0.556531 | 0.746617 | 0.874582 | 0.18264 |
| tossup_correctness | category | Unknown | 2039 | 0.617268 | 0.535315 | 0.0304439 | 0.176656 | 0.762138 | 0.762138 | 0 | 0.115629 | 0.594689 | 0.776233 | 0.885825 | 0.171479 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.591364 | 0.592417 | 0.0904518 | 0.20078 | 0.710383 | 0.743169 | -0.0327869 | 0.138906 | 0.480571 | 0.687526 | 0.819422 | 0.202529 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.634042 | 0.563794 | 0.0357252 | 0.188697 | 0.740314 | 0.728796 | 0.0115183 | 0.125812 | 0.526813 | 0.727858 | 0.859392 | 0.191005 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.655341 | 0.530837 | 0.0248386 | 0.175534 | 0.754355 | 0.752568 | 0.00178651 | 0.124912 | 0.564239 | 0.766619 | 0.886159 | 0.175516 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.658391 | 0.491958 | 0.0232256 | 0.158944 | 0.785391 | 0.786087 | -0.000695652 | 0.117625 | 0.606567 | 0.793355 | 0.904395 | 0.162212 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.641804 | 0.528237 | 0.0284561 | 0.172867 | 0.762729 | 0.764393 | -0.00166389 | 0.114442 | 0.619624 | 0.799924 | 0.915838 | 0.157413 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | -1.97537 | 1.1232 | -4.65636 | -3.48481 | -2.78974 | -2.26716 | -0.796935 | -0.113188 | 0.763206 |
| player | theta_2 | 1197 | -0.807901 | 0.668215 | -3.91369 | -2.30128 | -0.989981 | -0.604394 | -0.383831 | -0.0772924 | 0.432577 |
| player | theta_3 | 1197 | -0.979781 | 0.820674 | -4.08634 | -2.71859 | -1.29714 | -0.764816 | -0.407321 | 0.019696 | 0.815135 |
| player | theta_4 | 1197 | -1.79857 | 1.11373 | -5.15758 | -3.45065 | -2.65599 | -2.03378 | -0.664358 | -0.124212 | 0.711073 |
| player | theta_norm | 1197 | 3.39052 | 0.934719 | 1.33565 | 2.04262 | 2.67755 | 3.29858 | 4.072 | 5.12846 | 6.15827 |
| tossup | start_difficulty_d1 | 1240 | -2.29965 | 1.28359 | -4.8667 | -3.92241 | -3.15098 | -2.73306 | -1.57612 | 0.00318102 | 0.578739 |
| tossup | start_difficulty_d2 | 1240 | -0.785217 | 0.840825 | -3.8699 | -2.60474 | -1.18026 | -0.546217 | -0.165451 | 0.1636 | 0.603527 |
| tossup | start_difficulty_d3 | 1240 | -0.943531 | 0.891864 | -3.56928 | -2.69444 | -1.54097 | -0.824491 | -0.236862 | 0.281765 | 1.02733 |
| tossup | start_difficulty_d4 | 1240 | -1.73134 | 1.52499 | -4.80787 | -4.06284 | -3.25115 | -1.2345 | -0.292015 | 0.0776297 | 0.602923 |
| tossup | end_difficulty_d1 | 1240 | -3.39081 | 1.3888 | -8.03857 | -5.26734 | -4.33993 | -3.74551 | -2.57234 | -0.9488 | -0.365554 |
| tossup | end_difficulty_d2 | 1240 | -1.82841 | 0.974366 | -6.1715 | -3.8719 | -2.25996 | -1.54447 | -1.12649 | -0.759181 | -0.27885 |
| tossup | end_difficulty_d3 | 1240 | -1.98166 | 0.99588 | -5.50271 | -3.86475 | -2.63085 | -1.84302 | -1.2098 | -0.643778 | 0.191316 |
| tossup | end_difficulty_d4 | 1240 | -2.81894 | 1.66792 | -9.80273 | -5.45486 | -4.31489 | -2.30727 | -1.29283 | -0.861698 | -0.312526 |
| tossup | total_drop_d1 | 1240 | 1.09117 | 0.342289 | 0.494381 | 0.703568 | 0.927575 | 1.02178 | 1.18645 | 1.65207 | 4.4727 |
| tossup | total_drop_d2 | 1240 | 1.0432 | 0.166993 | 0.817 | 0.898013 | 0.956825 | 1.00212 | 1.07205 | 1.31937 | 2.64796 |
| tossup | total_drop_d3 | 1240 | 1.03813 | 0.138739 | 0.781102 | 0.884977 | 0.95585 | 1.01215 | 1.08427 | 1.26571 | 2.21115 |
| tossup | total_drop_d4 | 1240 | 1.0876 | 0.406077 | 0.395748 | 0.742188 | 0.948436 | 1.00915 | 1.10688 | 1.56545 | 6.72475 |
| tossup | drop_share_1_d1 | 1240 | 0.350516 | 0.0423953 | 0.203626 | 0.295571 | 0.317033 | 0.348895 | 0.375707 | 0.422072 | 0.557429 |
| tossup | drop_share_2_d1 | 1240 | 0.337995 | 0.0185726 | 0.277605 | 0.308351 | 0.328181 | 0.338707 | 0.347658 | 0.363211 | 0.478551 |
| tossup | drop_share_3_d1 | 1240 | 0.311489 | 0.0407295 | 0.142365 | 0.239345 | 0.28571 | 0.315663 | 0.34032 | 0.365147 | 0.478259 |
| tossup | drop_share_1_d2 | 1240 | 0.322015 | 0.0225517 | 0.275904 | 0.29648 | 0.307426 | 0.317165 | 0.329786 | 0.366991 | 0.440075 |
| tossup | drop_share_2_d2 | 1240 | 0.345814 | 0.00958143 | 0.312686 | 0.330291 | 0.339207 | 0.345603 | 0.352323 | 0.361783 | 0.375114 |
| tossup | drop_share_3_d2 | 1240 | 0.33217 | 0.0222069 | 0.216493 | 0.288559 | 0.322445 | 0.336894 | 0.347142 | 0.35979 | 0.380759 |
| tossup | drop_share_1_d3 | 1240 | 0.324792 | 0.0224789 | 0.273623 | 0.295314 | 0.309552 | 0.320811 | 0.334732 | 0.369458 | 0.419509 |
| tossup | drop_share_2_d3 | 1240 | 0.345718 | 0.00960484 | 0.31219 | 0.330393 | 0.339032 | 0.345892 | 0.352235 | 0.361097 | 0.379765 |
| tossup | drop_share_3_d3 | 1240 | 0.32949 | 0.0219205 | 0.241352 | 0.287965 | 0.318203 | 0.332983 | 0.344626 | 0.359328 | 0.381348 |
| tossup | drop_share_1_d4 | 1240 | 0.342678 | 0.048145 | 0.214099 | 0.296667 | 0.309552 | 0.32386 | 0.367061 | 0.441497 | 0.606279 |
| tossup | drop_share_2_d4 | 1240 | 0.339718 | 0.017684 | 0.243494 | 0.308252 | 0.330479 | 0.342528 | 0.3501 | 0.361736 | 0.462623 |
| tossup | drop_share_3_d4 | 1240 | 0.317605 | 0.0408372 | 0.150228 | 0.233273 | 0.297197 | 0.332184 | 0.34414 | 0.360264 | 0.447834 |
| tossup | r_1 | 1240 | 0.439395 | 0.266448 | 0.0178942 | 0.0320379 | 0.199166 | 0.472488 | 0.652472 | 0.835294 | 0.938713 |
| tossup | r_2 | 1240 | 0.102096 | 0.0896074 | 0.0160441 | 0.0269642 | 0.0435342 | 0.0682797 | 0.119955 | 0.314198 | 0.531514 |
| tossup | r_3 | 1240 | 0.129358 | 0.113892 | 0.0157304 | 0.0291041 | 0.0497988 | 0.0898329 | 0.170241 | 0.378594 | 0.672909 |
| tossup | r_4 | 1240 | 0.329151 | 0.303922 | 0.023154 | 0.0369176 | 0.0610051 | 0.184904 | 0.60481 | 0.844648 | 0.935247 |
| tossup | r_norm | 1240 | 0.709375 | 0.0978514 | 0.517204 | 0.575491 | 0.62627 | 0.690636 | 0.794121 | 0.87255 | 0.93939 |
