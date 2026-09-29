# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_3/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_3/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 316561 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.628927 |
| log_loss | 0.535009 |
| ece | 0.0375559 |
| brier | 0.17515 |
| accuracy | 0.761795 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.000329924 |
| probability_std | 0.130255 |
| probability_p10 | 0.577445 |
| probability_p50 | 0.786784 |
| probability_p90 | 0.908607 |
| mean_predictive_variance | 0.164723 |
| integrated_brier_score | 0.101552 |
| joint_tossup_event_log_loss | 6.91214 |
| buzz_position_mae | 0.161291 |
| buzz_position_median_absolute_error | 0.14676 |
| buzz_position_bias | -0.0702973 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.34675 |
| first_buzzer_mean_reciprocal_rank | 0.560433 |
| first_buzzer_log_loss | 1.68144 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.638403 |
| tossup_scorer_player_top1_accuracy | 0.314502 |
| tossup_scorer_team_top1_accuracy | 0.480736 |
| tossup_game_winner_accuracy | 0.765766 |
| tossup_game_margin_mae | 34.8841 |
| tournament_player_ppg_spearman | 0.680577 |
| tournament_player_ppg_mae | 8.85001 |
| tournament_player_ppg_top10_overlap | 0.662069 |
| neg_auroc | 0.628927 |
| neg_average_precision | 0.358577 |
| neg_precision | 0.496144 |
| neg_recall | 0.0892279 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0571086 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0935857 |
| no_buzz_calibration_error | 0.0776766 |
| no_buzz_brier | 0.027158 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.628927 | 0.535009 | 0.0375559 | 0.17515 | 0.761795 | 0.762125 | -0.000329924 | 0.130255 | 0.577445 | 0.786784 | 0.908607 | 0.164723 |
| tossup_correctness | tier | fall | 2842 | 0.615281 | 0.51274 | 0.0326472 | 0.165444 | 0.783251 | 0.785362 | -0.00211119 | 0.106575 | 0.655104 | 0.823166 | 0.919446 | 0.146843 |
| tossup_correctness | tier | nationals | 1564 | 0.652195 | 0.574015 | 0.0550385 | 0.193029 | 0.723785 | 0.718031 | 0.00575448 | 0.136195 | 0.491027 | 0.68542 | 0.83726 | 0.202171 |
| tossup_correctness | tier | regionals | 1937 | 0.616467 | 0.542323 | 0.0392192 | 0.17842 | 0.752194 | 0.758389 | -0.00619515 | 0.124593 | 0.587614 | 0.783467 | 0.897777 | 0.167233 |
| tossup_correctness | tier | winter | 2750 | 0.629688 | 0.530688 | 0.0364721 | 0.172711 | 0.768 | 0.765818 | 0.00218182 | 0.127898 | 0.584844 | 0.798237 | 0.912988 | 0.160136 |
| tossup_correctness | category | Current Events | 126 | 0.564522 | 0.550128 | 0.0633589 | 0.182917 | 0.761905 | 0.769841 | -0.00793651 | 0.0976843 | 0.561769 | 0.715655 | 0.832474 | 0.197823 |
| tossup_correctness | category | Fine Arts | 1071 | 0.629544 | 0.527445 | 0.0452657 | 0.172507 | 0.774977 | 0.766573 | 0.00840336 | 0.130773 | 0.577792 | 0.782623 | 0.908183 | 0.16471 |
| tossup_correctness | category | Geography | 185 | 0.683278 | 0.564679 | 0.052568 | 0.191875 | 0.713514 | 0.697297 | 0.0162162 | 0.15152 | 0.487782 | 0.728474 | 0.865285 | 0.189161 |
| tossup_correctness | category | History | 1440 | 0.656031 | 0.529443 | 0.0270466 | 0.17442 | 0.759722 | 0.754167 | 0.00555556 | 0.12384 | 0.54877 | 0.758576 | 0.877254 | 0.180153 |
| tossup_correctness | category | Literature | 1422 | 0.564054 | 0.498996 | 0.0654651 | 0.156197 | 0.808017 | 0.814346 | -0.00632911 | 0.11872 | 0.639749 | 0.830597 | 0.933414 | 0.142563 |
| tossup_correctness | category | Mythology | 318 | 0.669025 | 0.499054 | 0.0792059 | 0.160318 | 0.786164 | 0.789308 | -0.00314465 | 0.131587 | 0.541111 | 0.755238 | 0.880897 | 0.181138 |
| tossup_correctness | category | Other Academic | 66 | 0.678611 | 0.558408 | 0.101694 | 0.188074 | 0.681818 | 0.712121 | -0.030303 | 0.119612 | 0.534003 | 0.720271 | 0.845439 | 0.196133 |
| tossup_correctness | category | Philosophy | 311 | 0.64426 | 0.546324 | 0.0481809 | 0.181341 | 0.742765 | 0.745981 | -0.00321543 | 0.121079 | 0.61679 | 0.796436 | 0.912223 | 0.158576 |
| tossup_correctness | category | Popular Culture | 102 | 0.614815 | 0.46246 | 0.182944 | 0.146124 | 0.823529 | 0.882353 | -0.0588235 | 0.150022 | 0.488205 | 0.729025 | 0.868756 | 0.18773 |
| tossup_correctness | category | Religion | 358 | 0.65098 | 0.577552 | 0.0506627 | 0.195317 | 0.709497 | 0.712291 | -0.0027933 | 0.126664 | 0.568641 | 0.779303 | 0.895005 | 0.170793 |
| tossup_correctness | category | Science | 1433 | 0.645953 | 0.561633 | 0.0536367 | 0.185896 | 0.7418 | 0.738311 | 0.00348918 | 0.139592 | 0.571752 | 0.821137 | 0.920397 | 0.152117 |
| tossup_correctness | category | Social Science | 324 | 0.636549 | 0.553999 | 0.0829217 | 0.183515 | 0.746914 | 0.731481 | 0.0154321 | 0.117855 | 0.577217 | 0.76216 | 0.876202 | 0.176819 |
| tossup_correctness | category | Unknown | 1937 | 0.616467 | 0.542323 | 0.0392192 | 0.17842 | 0.752194 | 0.758389 | -0.00619515 | 0.124593 | 0.587614 | 0.783467 | 0.897777 | 0.167233 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.588761 | 0.602424 | 0.0482817 | 0.206027 | 0.676647 | 0.712575 | -0.0359281 | 0.130245 | 0.522594 | 0.704821 | 0.844808 | 0.196198 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.620566 | 0.573114 | 0.0461867 | 0.192245 | 0.723684 | 0.729167 | -0.00548246 | 0.127294 | 0.53785 | 0.724997 | 0.861281 | 0.190209 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.63146 | 0.537929 | 0.0298766 | 0.177354 | 0.758392 | 0.755083 | 0.00330969 | 0.125656 | 0.570303 | 0.76866 | 0.884387 | 0.17392 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.616659 | 0.517865 | 0.0440936 | 0.168007 | 0.778481 | 0.780942 | -0.00246132 | 0.12448 | 0.595155 | 0.799526 | 0.909468 | 0.160227 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.638453 | 0.533887 | 0.0377297 | 0.173483 | 0.764648 | 0.762029 | 0.00261866 | 0.132658 | 0.590683 | 0.810103 | 0.925811 | 0.153214 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | -2.18534 | 0.881916 | -4.80594 | -3.59484 | -2.79553 | -2.25134 | -1.54126 | -0.725232 | -0.167903 |
| player | theta_2 | 1167 | -1.09115 | 0.669492 | -3.57099 | -2.28157 | -1.58775 | -1.00348 | -0.593334 | -0.159833 | 0.488458 |
| player | theta_3 | 1167 | -1.65901 | 1.08179 | -4.47011 | -3.35858 | -2.49327 | -1.82654 | -0.518858 | -0.178751 | 0.17311 |
| player | theta_norm | 1167 | 3.24333 | 0.770812 | 1.45389 | 2.13983 | 2.62833 | 3.17859 | 3.77529 | 4.65015 | 5.66615 |
| tossup | start_difficulty_d1 | 1220 | -2.37097 | 1.16559 | -4.76267 | -3.90711 | -3.34233 | -2.6223 | -1.46575 | -0.321055 | 0.43495 |
| tossup | start_difficulty_d2 | 1220 | -0.916721 | 1.0871 | -4.69742 | -3.08942 | -1.44803 | -0.574768 | -0.123197 | 0.279783 | 1.26738 |
| tossup | start_difficulty_d3 | 1220 | -1.75395 | 1.3544 | -4.49115 | -3.70872 | -2.8797 | -2.09323 | -0.383336 | 0.187497 | 1.08585 |
| tossup | end_difficulty_d1 | 1220 | -3.48192 | 1.30492 | -9.20278 | -5.3015 | -4.46859 | -3.71469 | -2.4949 | -1.26968 | -0.412004 |
| tossup | end_difficulty_d2 | 1220 | -1.95032 | 1.18832 | -6.71291 | -4.36401 | -2.57151 | -1.61298 | -1.08722 | -0.627596 | 0.414796 |
| tossup | end_difficulty_d3 | 1220 | -2.80289 | 1.44727 | -7.03686 | -4.94519 | -3.9842 | -3.11416 | -1.3764 | -0.744516 | 0.2436 |
| tossup | total_drop_d1 | 1220 | 1.11095 | 0.438163 | 0.369767 | 0.69538 | 0.909442 | 1.0193 | 1.20175 | 1.74754 | 6.78367 |
| tossup | total_drop_d2 | 1220 | 1.0336 | 0.225054 | 0.65007 | 0.818398 | 0.930488 | 0.993541 | 1.0842 | 1.33151 | 3.868 |
| tossup | total_drop_d3 | 1220 | 1.04894 | 0.264029 | 0.544761 | 0.735178 | 0.917164 | 0.99461 | 1.10372 | 1.52926 | 3.23416 |
| tossup | drop_share_1_d1 | 1220 | 0.35493 | 0.0461755 | 0.215207 | 0.300073 | 0.322932 | 0.34454 | 0.377534 | 0.445157 | 0.635931 |
| tossup | drop_share_2_d1 | 1220 | 0.338071 | 0.0195851 | 0.230081 | 0.306139 | 0.326886 | 0.33917 | 0.34948 | 0.365573 | 0.519425 |
| tossup | drop_share_3_d1 | 1220 | 0.307 | 0.0417159 | 0.133988 | 0.230555 | 0.28375 | 0.314233 | 0.336533 | 0.360091 | 0.461553 |
| tossup | drop_share_1_d2 | 1220 | 0.320417 | 0.0241657 | 0.242895 | 0.292396 | 0.306488 | 0.315544 | 0.328268 | 0.372383 | 0.458349 |
| tossup | drop_share_2_d2 | 1220 | 0.344923 | 0.0116353 | 0.296716 | 0.323115 | 0.338128 | 0.34601 | 0.352581 | 0.362197 | 0.385008 |
| tossup | drop_share_3_d2 | 1220 | 0.33466 | 0.0231404 | 0.221531 | 0.287877 | 0.325091 | 0.338302 | 0.347925 | 0.365248 | 0.411489 |
| tossup | drop_share_1_d3 | 1220 | 0.341424 | 0.0413745 | 0.223818 | 0.294079 | 0.312084 | 0.330655 | 0.364448 | 0.416932 | 0.672718 |
| tossup | drop_share_2_d3 | 1220 | 0.340424 | 0.016154 | 0.224038 | 0.312685 | 0.331554 | 0.341903 | 0.3501 | 0.363325 | 0.427188 |
| tossup | drop_share_3_d3 | 1220 | 0.318151 | 0.0379691 | 0.103244 | 0.247447 | 0.296297 | 0.326901 | 0.34428 | 0.364991 | 0.463084 |
| tossup | r_1 | 1220 | 0.4954 | 0.32055 | 0.0353014 | 0.0605129 | 0.160827 | 0.559872 | 0.807195 | 0.896704 | 0.965553 |
| tossup | r_2 | 1220 | 0.140257 | 0.110118 | 0.0135479 | 0.0327303 | 0.0583818 | 0.105931 | 0.185369 | 0.379502 | 0.67561 |
| tossup | r_3 | 1220 | 0.364343 | 0.287309 | 0.015011 | 0.0378688 | 0.0775121 | 0.351857 | 0.638185 | 0.805136 | 0.924729 |
| tossup | r_norm | 1220 | 0.766865 | 0.0838144 | 0.586626 | 0.635533 | 0.696866 | 0.764412 | 0.835904 | 0.900457 | 0.965863 |
