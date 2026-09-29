# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_2/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_2/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 310034 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.614225 |
| log_loss | 0.544188 |
| ece | 0.051396 |
| brier | 0.178763 |
| accuracy | 0.756185 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00799395 |
| probability_std | 0.138264 |
| probability_p10 | 0.56204 |
| probability_p50 | 0.786623 |
| probability_p90 | 0.913303 |
| mean_predictive_variance | 0.163792 |
| integrated_brier_score | 0.104294 |
| joint_tossup_event_log_loss | 6.95396 |
| buzz_position_mae | 0.161831 |
| buzz_position_median_absolute_error | 0.145258 |
| buzz_position_bias | -0.0654451 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.331857 |
| first_buzzer_mean_reciprocal_rank | 0.548524 |
| first_buzzer_log_loss | 1.69314 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.651183 |
| tossup_scorer_player_top1_accuracy | 0.303198 |
| tossup_scorer_team_top1_accuracy | 0.472495 |
| tossup_game_winner_accuracy | 0.771739 |
| tossup_game_margin_mae | 36.7052 |
| tournament_player_ppg_spearman | 0.693987 |
| tournament_player_ppg_mae | 8.67886 |
| tournament_player_ppg_top10_overlap | 0.648276 |
| neg_auroc | 0.614225 |
| neg_average_precision | 0.324826 |
| neg_precision | 0.426 |
| neg_recall | 0.0975721 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0575287 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0895 |
| no_buzz_calibration_error | 0.076387 |
| no_buzz_brier | 0.023951 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| tossup_correctness | aggregate | all | 9257 | 0.614225 | 0.544188 | 0.051396 | 0.178763 | 0.756185 | 0.764178 | -0.00799395 | 0.138264 | 0.56204 | 0.786623 | 0.913303 | 0.163792 |
| tossup_correctness | tier | fall | 2798 | 0.578003 | 0.539096 | 0.0625802 | 0.174254 | 0.772695 | 0.785204 | -0.0125089 | 0.12967 | 0.604154 | 0.814325 | 0.928303 | 0.151154 |
| tossup_correctness | tier | nationals | 1545 | 0.653461 | 0.567479 | 0.0483098 | 0.192632 | 0.71521 | 0.721036 | -0.00582524 | 0.143188 | 0.46953 | 0.687284 | 0.852823 | 0.199663 |
| tossup_correctness | tier | regionals | 2039 | 0.586501 | 0.556164 | 0.0618604 | 0.182552 | 0.758705 | 0.762138 | -0.00343306 | 0.129174 | 0.592118 | 0.800746 | 0.914932 | 0.157694 |
| tossup_correctness | tier | winter | 2875 | 0.632515 | 0.528132 | 0.0413516 | 0.17301 | 0.760348 | 0.768348 | -0.008 | 0.131734 | 0.577002 | 0.794678 | 0.911929 | 0.161139 |
| tossup_correctness | category | Current Events | 129 | 0.570038 | 0.641523 | 0.0760744 | 0.224289 | 0.604651 | 0.666667 | -0.0620155 | 0.118452 | 0.497856 | 0.674913 | 0.809983 | 0.207021 |
| tossup_correctness | category | Fine Arts | 1074 | 0.584512 | 0.545284 | 0.0640846 | 0.177156 | 0.763501 | 0.776536 | -0.0130354 | 0.131568 | 0.602347 | 0.810813 | 0.92509 | 0.151425 |
| tossup_correctness | category | Geography | 180 | 0.691996 | 0.632563 | 0.0996178 | 0.218336 | 0.666667 | 0.616667 | 0.05 | 0.146549 | 0.496997 | 0.735183 | 0.868253 | 0.185253 |
| tossup_correctness | category | History | 1454 | 0.610094 | 0.553205 | 0.0587718 | 0.185047 | 0.740028 | 0.757909 | -0.0178817 | 0.138946 | 0.527733 | 0.731637 | 0.881659 | 0.183575 |
| tossup_correctness | category | Literature | 1435 | 0.614037 | 0.487528 | 0.0400446 | 0.15187 | 0.807666 | 0.810453 | -0.00278746 | 0.118141 | 0.659369 | 0.852763 | 0.948858 | 0.131523 |
| tossup_correctness | category | Mythology | 324 | 0.602764 | 0.518498 | 0.0792907 | 0.17 | 0.774691 | 0.79321 | -0.0185185 | 0.13851 | 0.536862 | 0.743891 | 0.900025 | 0.180019 |
| tossup_correctness | category | Other Academic | 71 | 0.368192 | 0.614261 | 0.169615 | 0.208502 | 0.732394 | 0.760563 | -0.028169 | 0.102369 | 0.587376 | 0.731532 | 0.831902 | 0.193089 |
| tossup_correctness | category | Philosophy | 310 | 0.662277 | 0.522993 | 0.058408 | 0.170968 | 0.770968 | 0.76129 | 0.00967742 | 0.119918 | 0.61574 | 0.826093 | 0.923473 | 0.14804 |
| tossup_correctness | category | Popular Culture | 108 | 0.527778 | 0.493831 | 0.191103 | 0.160385 | 0.777778 | 0.888889 | -0.111111 | 0.157928 | 0.49799 | 0.72257 | 0.87365 | 0.185939 |
| tossup_correctness | category | Religion | 361 | 0.596654 | 0.577142 | 0.0729518 | 0.19192 | 0.728532 | 0.742382 | -0.0138504 | 0.145873 | 0.54825 | 0.780326 | 0.911384 | 0.166947 |
| tossup_correctness | category | Science | 1445 | 0.626119 | 0.556042 | 0.0441639 | 0.185454 | 0.741176 | 0.746021 | -0.00484429 | 0.141786 | 0.516021 | 0.754803 | 0.879144 | 0.179407 |
| tossup_correctness | category | Social Science | 327 | 0.692322 | 0.545616 | 0.0186838 | 0.182326 | 0.733945 | 0.718654 | 0.0152905 | 0.126262 | 0.548185 | 0.755225 | 0.876223 | 0.1799 |
| tossup_correctness | category | Unknown | 2039 | 0.586501 | 0.556164 | 0.0618604 | 0.182552 | 0.758705 | 0.762138 | -0.00343306 | 0.129174 | 0.592118 | 0.800746 | 0.914932 | 0.157694 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.545839 | 0.610387 | 0.103255 | 0.208243 | 0.710383 | 0.743169 | -0.0327869 | 0.138497 | 0.475903 | 0.686794 | 0.82983 | 0.203194 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.576088 | 0.600663 | 0.0766283 | 0.20449 | 0.704712 | 0.728796 | -0.0240838 | 0.144047 | 0.498942 | 0.722699 | 0.859788 | 0.192581 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.613456 | 0.553557 | 0.0507349 | 0.184416 | 0.742296 | 0.752568 | -0.0102724 | 0.134956 | 0.542829 | 0.761588 | 0.890724 | 0.175917 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.630339 | 0.50651 | 0.0390459 | 0.163757 | 0.782261 | 0.786087 | -0.00382609 | 0.131343 | 0.585038 | 0.798322 | 0.914228 | 0.158807 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.611184 | 0.551275 | 0.0544884 | 0.178935 | 0.760732 | 0.764393 | -0.00366057 | 0.132423 | 0.600963 | 0.822017 | 0.931911 | 0.147978 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | -2.15233 | 0.76337 | -4.87826 | -3.41481 | -2.69295 | -2.15147 | -1.59638 | -0.949389 | 0.0220012 |
| player | theta_2 | 1197 | -1.81937 | 0.890901 | -4.31614 | -3.21474 | -2.46879 | -1.85383 | -1.06168 | -0.429751 | 0.103981 |
| player | theta_norm | 1197 | 2.97189 | 0.697279 | 1.20229 | 1.94715 | 2.47399 | 2.92636 | 3.40971 | 4.18157 | 5.32897 |
| tossup | start_difficulty_d1 | 1240 | -2.1919 | 1.19417 | -4.35746 | -3.7483 | -3.21686 | -2.53703 | -1.10154 | -0.251351 | 0.388761 |
| tossup | start_difficulty_d2 | 1240 | -2.06849 | 1.13475 | -4.64381 | -3.70573 | -2.93263 | -2.33359 | -1.1693 | -0.127412 | 1.31896 |
| tossup | end_difficulty_d1 | 1240 | -3.26045 | 1.31912 | -8.02979 | -5.17591 | -4.23597 | -3.49671 | -2.11053 | -1.18834 | -0.505139 |
| tossup | end_difficulty_d2 | 1240 | -3.12399 | 1.25636 | -7.29927 | -5.0568 | -4.00554 | -3.28611 | -2.15721 | -1.04292 | 0.487548 |
| tossup | total_drop_d1 | 1240 | 1.06855 | 0.397736 | 0.370049 | 0.6748 | 0.869348 | 0.990459 | 1.14803 | 1.702 | 4.80843 |
| tossup | total_drop_d2 | 1240 | 1.0555 | 0.321652 | 0.470594 | 0.673238 | 0.888407 | 0.989699 | 1.13323 | 1.62922 | 2.90549 |
| tossup | drop_share_1_d1 | 1240 | 0.350024 | 0.0478289 | 0.211764 | 0.295669 | 0.318323 | 0.336812 | 0.373902 | 0.439202 | 0.589476 |
| tossup | drop_share_2_d1 | 1240 | 0.338224 | 0.018909 | 0.25405 | 0.307069 | 0.327382 | 0.339407 | 0.349611 | 0.365169 | 0.46092 |
| tossup | drop_share_3_d1 | 1240 | 0.311752 | 0.0433461 | 0.14582 | 0.229586 | 0.290296 | 0.318288 | 0.339865 | 0.368783 | 0.44892 |
| tossup | drop_share_1_d2 | 1240 | 0.347243 | 0.0456933 | 0.202802 | 0.290665 | 0.317494 | 0.340787 | 0.370139 | 0.429394 | 0.691361 |
| tossup | drop_share_2_d2 | 1240 | 0.339064 | 0.0180512 | 0.204953 | 0.308771 | 0.329661 | 0.340173 | 0.349107 | 0.362113 | 0.449911 |
| tossup | drop_share_3_d2 | 1240 | 0.313693 | 0.043789 | 0.103686 | 0.236099 | 0.289804 | 0.319133 | 0.340946 | 0.374444 | 0.459362 |
| tossup | r_1 | 1240 | 0.514839 | 0.334704 | 0.036302 | 0.0679038 | 0.183813 | 0.510209 | 0.851328 | 0.941606 | 0.970142 |
| tossup | r_2 | 1240 | 0.485161 | 0.334704 | 0.0298583 | 0.0583943 | 0.148672 | 0.489791 | 0.816187 | 0.932096 | 0.963698 |
| tossup | r_norm | 1240 | 0.848238 | 0.0693466 | 0.707205 | 0.728783 | 0.792963 | 0.852439 | 0.908121 | 0.950469 | 0.970601 |
