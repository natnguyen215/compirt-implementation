# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_2/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_2/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 311202 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.608725 |
| log_loss | 0.54884 |
| ece | 0.0519156 |
| brier | 0.180061 |
| accuracy | 0.751787 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0103376 |
| probability_std | 0.137813 |
| probability_p10 | 0.559141 |
| probability_p50 | 0.78682 |
| probability_p90 | 0.914707 |
| mean_predictive_variance | 0.16338 |
| integrated_brier_score | 0.103317 |
| joint_tossup_event_log_loss | 6.95064 |
| buzz_position_mae | 0.163117 |
| buzz_position_median_absolute_error | 0.148617 |
| buzz_position_bias | -0.0709025 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.335093 |
| first_buzzer_mean_reciprocal_rank | 0.55022 |
| first_buzzer_log_loss | 1.70376 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.634554 |
| tossup_scorer_player_top1_accuracy | 0.305952 |
| tossup_scorer_team_top1_accuracy | 0.47132 |
| tossup_game_winner_accuracy | 0.761261 |
| tossup_game_margin_mae | 34.9249 |
| tournament_player_ppg_spearman | 0.668431 |
| tournament_player_ppg_mae | 8.99447 |
| tournament_player_ppg_top10_overlap | 0.648276 |
| neg_auroc | 0.608725 |
| neg_average_precision | 0.330472 |
| neg_precision | 0.406 |
| neg_recall | 0.0938511 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0574049 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0915454 |
| no_buzz_calibration_error | 0.0756363 |
| no_buzz_brier | 0.026647 |
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
| tossup_correctness | aggregate | all | 9093 | 0.608725 | 0.54884 | 0.0519156 | 0.180061 | 0.751787 | 0.762125 | -0.0103376 | 0.137813 | 0.559141 | 0.78682 | 0.914707 | 0.16338 |
| tossup_correctness | tier | fall | 2842 | 0.598274 | 0.524263 | 0.0471414 | 0.168933 | 0.776918 | 0.785362 | -0.00844476 | 0.122766 | 0.622425 | 0.813063 | 0.929256 | 0.150518 |
| tossup_correctness | tier | nationals | 1564 | 0.624283 | 0.589343 | 0.0630428 | 0.199866 | 0.701407 | 0.718031 | -0.016624 | 0.146697 | 0.47178 | 0.683906 | 0.855218 | 0.199366 |
| tossup_correctness | tier | regionals | 1937 | 0.598406 | 0.558297 | 0.0577988 | 0.18368 | 0.745999 | 0.758389 | -0.0123903 | 0.133492 | 0.58905 | 0.802605 | 0.917826 | 0.156426 |
| tossup_correctness | tier | winter | 2750 | 0.605138 | 0.544544 | 0.0471688 | 0.177749 | 0.758545 | 0.765818 | -0.00727273 | 0.129179 | 0.58373 | 0.792623 | 0.912736 | 0.161103 |
| tossup_correctness | category | Current Events | 126 | 0.538571 | 0.577313 | 0.115387 | 0.195536 | 0.722222 | 0.769841 | -0.047619 | 0.118187 | 0.516384 | 0.661206 | 0.818049 | 0.209506 |
| tossup_correctness | category | Fine Arts | 1071 | 0.601525 | 0.543474 | 0.0561411 | 0.177719 | 0.764706 | 0.766573 | -0.00186741 | 0.128666 | 0.611869 | 0.808775 | 0.925708 | 0.154497 |
| tossup_correctness | category | Geography | 185 | 0.661822 | 0.586561 | 0.086866 | 0.202053 | 0.681081 | 0.697297 | -0.0162162 | 0.152064 | 0.450899 | 0.708375 | 0.854138 | 0.194845 |
| tossup_correctness | category | History | 1440 | 0.635827 | 0.54405 | 0.0447786 | 0.181137 | 0.739583 | 0.754167 | -0.0145833 | 0.136112 | 0.535591 | 0.745743 | 0.883475 | 0.182145 |
| tossup_correctness | category | Literature | 1422 | 0.544712 | 0.513133 | 0.0696873 | 0.158479 | 0.805907 | 0.814346 | -0.00843882 | 0.11581 | 0.660709 | 0.859277 | 0.951984 | 0.127377 |
| tossup_correctness | category | Mythology | 318 | 0.655587 | 0.508493 | 0.0792337 | 0.164963 | 0.77673 | 0.789308 | -0.0125786 | 0.128786 | 0.541606 | 0.737132 | 0.882401 | 0.184271 |
| tossup_correctness | category | Other Academic | 66 | 0.655095 | 0.574846 | 0.06126 | 0.19423 | 0.681818 | 0.712121 | -0.030303 | 0.123939 | 0.527602 | 0.687475 | 0.85532 | 0.203927 |
| tossup_correctness | category | Philosophy | 311 | 0.632202 | 0.556034 | 0.067997 | 0.183559 | 0.745981 | 0.745981 | 0 | 0.122344 | 0.636386 | 0.820835 | 0.91537 | 0.149838 |
| tossup_correctness | category | Popular Culture | 102 | 0.575926 | 0.471746 | 0.190473 | 0.150055 | 0.784314 | 0.882353 | -0.0980392 | 0.153569 | 0.475755 | 0.742034 | 0.869412 | 0.185264 |
| tossup_correctness | category | Religion | 358 | 0.625433 | 0.598617 | 0.070835 | 0.203701 | 0.692737 | 0.712291 | -0.0195531 | 0.136165 | 0.550858 | 0.788764 | 0.898422 | 0.166309 |
| tossup_correctness | category | Science | 1433 | 0.618457 | 0.565827 | 0.0446236 | 0.18845 | 0.734124 | 0.738311 | -0.00418702 | 0.140912 | 0.519488 | 0.757615 | 0.888426 | 0.178483 |
| tossup_correctness | category | Social Science | 324 | 0.581793 | 0.576977 | 0.0701555 | 0.192331 | 0.740741 | 0.731481 | 0.00925926 | 0.117288 | 0.563766 | 0.754052 | 0.877239 | 0.18033 |
| tossup_correctness | category | Unknown | 1937 | 0.598406 | 0.558297 | 0.0577988 | 0.18368 | 0.745999 | 0.758389 | -0.0123903 | 0.133492 | 0.58905 | 0.802605 | 0.917826 | 0.156426 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.573354 | 0.613586 | 0.0900324 | 0.209224 | 0.706587 | 0.712575 | -0.00598802 | 0.146098 | 0.469679 | 0.701732 | 0.847946 | 0.197621 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.597528 | 0.589398 | 0.0545184 | 0.198815 | 0.711623 | 0.729167 | -0.0175439 | 0.133697 | 0.515021 | 0.708737 | 0.856109 | 0.194326 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.61384 | 0.551094 | 0.0464119 | 0.182991 | 0.741844 | 0.755083 | -0.0132388 | 0.132872 | 0.548155 | 0.761166 | 0.888327 | 0.176612 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.602039 | 0.525491 | 0.0516935 | 0.170673 | 0.769339 | 0.780942 | -0.0116034 | 0.130312 | 0.585696 | 0.799392 | 0.912532 | 0.158856 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.612787 | 0.553371 | 0.0547105 | 0.179579 | 0.756792 | 0.762029 | -0.00523732 | 0.13757 | 0.590354 | 0.822075 | 0.933987 | 0.14732 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | -2.24745 | 0.709099 | -4.61216 | -3.49144 | -2.6908 | -2.2025 | -1.7758 | -1.15145 | -0.166151 |
| player | theta_2 | 1167 | -1.75963 | 0.873291 | -4.37961 | -3.19393 | -2.38296 | -1.75575 | -1.05841 | -0.451653 | 0.262322 |
| player | theta_norm | 1167 | 2.99301 | 0.673781 | 1.26023 | 2.01463 | 2.49687 | 2.95825 | 3.4292 | 4.16436 | 5.08355 |
| tossup | start_difficulty_d1 | 1220 | -2.28037 | 1.16617 | -4.30273 | -3.77074 | -3.25447 | -2.63742 | -1.24415 | -0.252181 | 0.305769 |
| tossup | start_difficulty_d2 | 1220 | -2.01508 | 1.16684 | -4.67898 | -3.6978 | -2.91646 | -2.29434 | -1.05917 | 0.0114368 | 1.47875 |
| tossup | end_difficulty_d1 | 1220 | -3.34212 | 1.28287 | -7.35458 | -5.16962 | -4.27671 | -3.58637 | -2.25746 | -1.22869 | -0.610884 |
| tossup | end_difficulty_d2 | 1220 | -3.08064 | 1.30913 | -8.06204 | -5.18067 | -3.99724 | -3.24132 | -2.03355 | -0.920087 | 0.676295 |
| tossup | total_drop_d1 | 1220 | 1.06174 | 0.401561 | 0.351743 | 0.663302 | 0.853241 | 0.98401 | 1.13809 | 1.74078 | 4.12879 |
| tossup | total_drop_d2 | 1220 | 1.06556 | 0.343232 | 0.495437 | 0.678397 | 0.894102 | 0.989114 | 1.14198 | 1.67565 | 3.92358 |
| tossup | drop_share_1_d1 | 1220 | 0.352102 | 0.048898 | 0.20441 | 0.295264 | 0.319037 | 0.341439 | 0.376691 | 0.447149 | 0.621127 |
| tossup | drop_share_2_d1 | 1220 | 0.337435 | 0.0199142 | 0.240804 | 0.306569 | 0.325061 | 0.337915 | 0.349086 | 0.365154 | 0.509947 |
| tossup | drop_share_3_d1 | 1220 | 0.310463 | 0.0447807 | 0.138069 | 0.226767 | 0.285543 | 0.31857 | 0.340096 | 0.370843 | 0.476586 |
| tossup | drop_share_1_d2 | 1220 | 0.346177 | 0.0462147 | 0.205658 | 0.290306 | 0.316076 | 0.337358 | 0.368064 | 0.428416 | 0.720945 |
| tossup | drop_share_2_d2 | 1220 | 0.339228 | 0.0176868 | 0.189646 | 0.309143 | 0.329707 | 0.340824 | 0.349311 | 0.364236 | 0.429076 |
| tossup | drop_share_3_d2 | 1220 | 0.314596 | 0.0431992 | 0.0894088 | 0.236754 | 0.292124 | 0.320037 | 0.341867 | 0.375264 | 0.4481 |
| tossup | r_1 | 1220 | 0.536715 | 0.328557 | 0.0330369 | 0.0739913 | 0.214057 | 0.500577 | 0.868983 | 0.944741 | 0.966858 |
| tossup | r_2 | 1220 | 0.463285 | 0.328557 | 0.0331421 | 0.0552586 | 0.131017 | 0.499423 | 0.785943 | 0.926009 | 0.966963 |
| tossup | r_norm | 1220 | 0.844492 | 0.0724953 | 0.707107 | 0.718125 | 0.785722 | 0.848783 | 0.907621 | 0.949907 | 0.967527 |
