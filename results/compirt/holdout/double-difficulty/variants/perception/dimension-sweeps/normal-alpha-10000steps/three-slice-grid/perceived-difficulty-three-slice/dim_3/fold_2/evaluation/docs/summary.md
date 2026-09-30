# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_3/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_3/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 311599 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.655053 |
| log_loss | 0.522655 |
| ece | 0.0360398 |
| brier | 0.170718 |
| accuracy | 0.764286 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.000108026 |
| probability_std | 0.14105 |
| probability_p10 | 0.550532 |
| probability_p50 | 0.776373 |
| probability_p90 | 0.911368 |
| mean_predictive_variance | 0.167348 |
| integrated_brier_score | 0.103608 |
| joint_tossup_event_log_loss | 6.94209 |
| buzz_position_mae | 0.160791 |
| buzz_position_median_absolute_error | 0.142527 |
| buzz_position_bias | -0.0644277 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.346981 |
| first_buzzer_mean_reciprocal_rank | 0.560167 |
| first_buzzer_log_loss | 1.69262 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.659069 |
| tossup_scorer_player_top1_accuracy | 0.316951 |
| tossup_scorer_team_top1_accuracy | 0.489872 |
| tossup_game_winner_accuracy | 0.780435 |
| tossup_game_margin_mae | 36.7763 |
| tournament_player_ppg_spearman | 0.70622 |
| tournament_player_ppg_mae | 8.8492 |
| tournament_player_ppg_top10_overlap | 0.651724 |
| neg_auroc | 0.655053 |
| neg_average_precision | 0.383168 |
| neg_precision | 0.500882 |
| neg_recall | 0.130096 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0573642 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0899574 |
| no_buzz_calibration_error | 0.0768444 |
| no_buzz_brier | 0.0243601 |
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
| tossup_correctness | aggregate | all | 9257 | 0.655053 | 0.522655 | 0.0360398 | 0.170718 | 0.764286 | 0.764178 | 0.000108026 | 0.14105 | 0.550532 | 0.776373 | 0.911368 | 0.167348 |
| tossup_correctness | tier | fall | 2798 | 0.646165 | 0.500206 | 0.0385458 | 0.160511 | 0.786633 | 0.785204 | 0.00142959 | 0.130339 | 0.598284 | 0.805417 | 0.922458 | 0.154657 |
| tossup_correctness | tier | nationals | 1545 | 0.685102 | 0.553502 | 0.0479344 | 0.18684 | 0.714563 | 0.721036 | -0.00647249 | 0.137343 | 0.493363 | 0.681856 | 0.848017 | 0.201096 |
| tossup_correctness | tier | regionals | 2039 | 0.621624 | 0.540921 | 0.0533426 | 0.177 | 0.755763 | 0.762138 | -0.00637567 | 0.140206 | 0.560793 | 0.783145 | 0.913738 | 0.165126 |
| tossup_correctness | tier | winter | 2875 | 0.657667 | 0.51497 | 0.027578 | 0.167532 | 0.775304 | 0.768348 | 0.00695652 | 0.138916 | 0.566351 | 0.790168 | 0.912315 | 0.16314 |
| tossup_correctness | category | Current Events | 129 | 0.650352 | 0.603202 | 0.0626562 | 0.207925 | 0.697674 | 0.666667 | 0.0310078 | 0.125631 | 0.524581 | 0.709181 | 0.849577 | 0.193087 |
| tossup_correctness | category | Fine Arts | 1074 | 0.622552 | 0.524748 | 0.0476424 | 0.171267 | 0.764432 | 0.776536 | -0.0121043 | 0.13693 | 0.57539 | 0.789262 | 0.91167 | 0.163557 |
| tossup_correctness | category | Geography | 180 | 0.721635 | 0.594067 | 0.0696175 | 0.203106 | 0.711111 | 0.616667 | 0.0944444 | 0.162631 | 0.419646 | 0.685779 | 0.834739 | 0.201432 |
| tossup_correctness | category | History | 1454 | 0.673177 | 0.521205 | 0.0359838 | 0.172144 | 0.75447 | 0.757909 | -0.00343879 | 0.142578 | 0.519675 | 0.746301 | 0.89362 | 0.178744 |
| tossup_correctness | category | Literature | 1435 | 0.646831 | 0.467772 | 0.035341 | 0.144813 | 0.813937 | 0.810453 | 0.00348432 | 0.117548 | 0.657645 | 0.849392 | 0.944809 | 0.132908 |
| tossup_correctness | category | Mythology | 324 | 0.647366 | 0.493157 | 0.052736 | 0.158937 | 0.799383 | 0.79321 | 0.00617284 | 0.131633 | 0.574678 | 0.776719 | 0.900698 | 0.170098 |
| tossup_correctness | category | Other Academic | 71 | 0.417211 | 0.606415 | 0.127163 | 0.205684 | 0.746479 | 0.760563 | -0.0140845 | 0.105975 | 0.551093 | 0.715066 | 0.842871 | 0.200558 |
| tossup_correctness | category | Philosophy | 310 | 0.659929 | 0.521921 | 0.0316482 | 0.172668 | 0.758065 | 0.76129 | -0.00322581 | 0.126388 | 0.59441 | 0.794262 | 0.920361 | 0.15956 |
| tossup_correctness | category | Popular Culture | 108 | 0.576389 | 0.454192 | 0.184968 | 0.141375 | 0.833333 | 0.888889 | -0.0555556 | 0.127448 | 0.518251 | 0.736534 | 0.845226 | 0.189263 |
| tossup_correctness | category | Religion | 361 | 0.650457 | 0.54713 | 0.0701392 | 0.181881 | 0.756233 | 0.742382 | 0.0138504 | 0.151307 | 0.517412 | 0.74295 | 0.883769 | 0.180323 |
| tossup_correctness | category | Science | 1445 | 0.672628 | 0.53164 | 0.0224548 | 0.175934 | 0.746713 | 0.746021 | 0.000692042 | 0.138459 | 0.531202 | 0.749877 | 0.889696 | 0.179143 |
| tossup_correctness | category | Social Science | 327 | 0.695328 | 0.54571 | 0.031355 | 0.181124 | 0.737003 | 0.718654 | 0.0183486 | 0.134567 | 0.518531 | 0.728979 | 0.86565 | 0.188977 |
| tossup_correctness | category | Unknown | 2039 | 0.621624 | 0.540921 | 0.0533426 | 0.177 | 0.755763 | 0.762138 | -0.00637567 | 0.140206 | 0.560793 | 0.783145 | 0.913738 | 0.165126 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.61311 | 0.581226 | 0.112481 | 0.195563 | 0.710383 | 0.743169 | -0.0327869 | 0.144152 | 0.471464 | 0.682331 | 0.829633 | 0.203567 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.647301 | 0.560044 | 0.0388526 | 0.187649 | 0.737173 | 0.728796 | 0.00837696 | 0.143417 | 0.491382 | 0.724112 | 0.857781 | 0.190233 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.670105 | 0.524749 | 0.0251552 | 0.172887 | 0.756588 | 0.752568 | 0.00401965 | 0.140039 | 0.531603 | 0.76226 | 0.892756 | 0.175425 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.66387 | 0.491591 | 0.0385545 | 0.158349 | 0.786087 | 0.786087 | 0 | 0.134779 | 0.574203 | 0.79025 | 0.917662 | 0.16201 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.638307 | 0.535365 | 0.0379774 | 0.174042 | 0.761065 | 0.764393 | -0.00332779 | 0.13894 | 0.575458 | 0.799644 | 0.927326 | 0.156959 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | -1.96661 | 1.27441 | -5.47811 | -3.76553 | -2.91538 | -2.3069 | -0.530947 | -0.00596951 | 0.917164 |
| player | theta_2 | 1197 | -1.31652 | 1.20997 | -4.66943 | -3.36645 | -2.44231 | -0.852348 | -0.315969 | 0.147076 | 1.14113 |
| player | theta_3 | 1197 | -0.60576 | 1.04642 | -4.30259 | -3.12624 | -0.548925 | -0.257491 | -0.075015 | 0.37414 | 1.12712 |
| player | theta_norm | 1197 | 3.08027 | 0.81232 | 1.06768 | 1.91323 | 2.49967 | 3.00188 | 3.58583 | 4.5613 | 5.73746 |
| tossup | start_difficulty_d1 | 1240 | -1.8269 | 1.6476 | -5.97231 | -4.10227 | -3.38817 | -1.63568 | -0.193057 | 0.103659 | 0.471814 |
| tossup | start_difficulty_d2 | 1240 | -0.886953 | 1.55131 | -5.20588 | -4.02369 | -1.49398 | -0.189401 | 0.137998 | 0.663929 | 1.88401 |
| tossup | start_difficulty_d3 | 1240 | -0.86289 | 1.31438 | -3.78904 | -3.17701 | -2.42946 | -0.149407 | 0.0776361 | 0.375073 | 1.47938 |
| tossup | end_difficulty_d1 | 1240 | -2.94637 | 1.84662 | -8.74603 | -5.91153 | -4.45812 | -2.56668 | -1.19398 | -0.844553 | -0.376048 |
| tossup | end_difficulty_d2 | 1240 | -1.9216 | 1.64244 | -7.93411 | -5.25053 | -2.91659 | -1.20079 | -0.816065 | -0.181604 | 1.08523 |
| tossup | end_difficulty_d3 | 1240 | -1.93467 | 1.48362 | -8.75049 | -4.68829 | -3.36002 | -1.16016 | -0.89871 | -0.55046 | 0.679239 |
| tossup | total_drop_d1 | 1240 | 1.11947 | 0.513718 | 0.388175 | 0.694234 | 0.93095 | 1.00881 | 1.10681 | 1.97492 | 5.67648 |
| tossup | total_drop_d2 | 1240 | 1.03465 | 0.287015 | 0.470657 | 0.723788 | 0.911296 | 0.978845 | 1.08064 | 1.52395 | 4.46868 |
| tossup | total_drop_d3 | 1240 | 1.07178 | 0.31636 | 0.587517 | 0.857052 | 0.950538 | 0.996634 | 1.06751 | 1.5549 | 5.50262 |
| tossup | drop_share_1_d1 | 1240 | 0.341277 | 0.0534641 | 0.203569 | 0.290352 | 0.305982 | 0.319741 | 0.368235 | 0.445545 | 0.655314 |
| tossup | drop_share_2_d1 | 1240 | 0.339918 | 0.0204681 | 0.226374 | 0.30577 | 0.329039 | 0.34073 | 0.351162 | 0.367913 | 0.45828 |
| tossup | drop_share_3_d1 | 1240 | 0.318806 | 0.0467704 | 0.118312 | 0.224261 | 0.294143 | 0.335173 | 0.35017 | 0.366294 | 0.47 |
| tossup | drop_share_1_d2 | 1240 | 0.318387 | 0.0350929 | 0.19319 | 0.283267 | 0.299989 | 0.310335 | 0.326192 | 0.390935 | 0.562284 |
| tossup | drop_share_2_d2 | 1240 | 0.345007 | 0.0179158 | 0.272237 | 0.314176 | 0.336264 | 0.345612 | 0.354334 | 0.368463 | 0.475115 |
| tossup | drop_share_3_d2 | 1240 | 0.336606 | 0.034012 | 0.158635 | 0.274018 | 0.326914 | 0.342226 | 0.354932 | 0.373984 | 0.503754 |
| tossup | drop_share_1_d3 | 1240 | 0.323935 | 0.0345787 | 0.247178 | 0.28908 | 0.302066 | 0.312206 | 0.33334 | 0.399298 | 0.550911 |
| tossup | drop_share_2_d3 | 1240 | 0.344654 | 0.0134924 | 0.274591 | 0.32232 | 0.336098 | 0.345067 | 0.353068 | 0.364328 | 0.413411 |
| tossup | drop_share_3_d3 | 1240 | 0.331411 | 0.0326631 | 0.174498 | 0.259639 | 0.321624 | 0.341681 | 0.352665 | 0.365943 | 0.39351 |
| tossup | r_1 | 1240 | 0.473086 | 0.387417 | 0.0164642 | 0.0335409 | 0.0730308 | 0.492941 | 0.866926 | 0.931432 | 0.975822 |
| tossup | r_2 | 1240 | 0.253279 | 0.323109 | 0.0137136 | 0.0294752 | 0.0514891 | 0.0883446 | 0.218536 | 0.93782 | 0.973498 |
| tossup | r_3 | 1240 | 0.273635 | 0.329377 | 0.00916791 | 0.0210798 | 0.0420206 | 0.0747036 | 0.687596 | 0.859684 | 0.930388 |
| tossup | r_norm | 1240 | 0.849099 | 0.0675265 | 0.670887 | 0.729489 | 0.79927 | 0.855252 | 0.900776 | 0.948249 | 0.975974 |
