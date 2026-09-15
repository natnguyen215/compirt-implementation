# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_1/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_1/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 301651 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.582314 |
| log_loss | 0.561158 |
| ece | 0.0629349 |
| brier | 0.184712 |
| accuracy | 0.749368 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0127571 |
| probability_std | 0.133293 |
| probability_p10 | 0.569926 |
| probability_p50 | 0.783086 |
| probability_p90 | 0.909957 |
| mean_predictive_variance | 0.16536 |
| integrated_brier_score | 0.1059 |
| joint_tossup_event_log_loss | 7.00937 |
| buzz_position_mae | 0.165939 |
| buzz_position_median_absolute_error | 0.151107 |
| buzz_position_bias | -0.0706788 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.30419 |
| first_buzzer_mean_reciprocal_rank | 0.524935 |
| first_buzzer_log_loss | 1.75506 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.623996 |
| tossup_scorer_player_top1_accuracy | 0.280628 |
| tossup_scorer_team_top1_accuracy | 0.451299 |
| tossup_game_winner_accuracy | 0.734234 |
| tossup_game_margin_mae | 38.3286 |
| tournament_player_ppg_spearman | 0.59074 |
| tournament_player_ppg_mae | 10.1481 |
| tournament_player_ppg_top10_overlap | 0.6 |
| neg_auroc | 0.582314 |
| neg_average_precision | 0.29981 |
| neg_precision | 0.36385 |
| neg_recall | 0.0716597 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0584017 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0894556 |
| no_buzz_calibration_error | 0.0735465 |
| no_buzz_brier | 0.0252384 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| tossup_correctness | aggregate | all | 9093 | 0.582314 | 0.561158 | 0.0629349 | 0.184712 | 0.749368 | 0.762125 | -0.0127571 | 0.133293 | 0.569926 | 0.783086 | 0.909957 | 0.16536 |
| tossup_correctness | tier | fall | 2842 | 0.585192 | 0.534392 | 0.0770019 | 0.175338 | 0.761436 | 0.785362 | -0.0239268 | 0.139233 | 0.540072 | 0.762454 | 0.898065 | 0.173768 |
| tossup_correctness | tier | nationals | 1564 | 0.615708 | 0.609893 | 0.0729082 | 0.202536 | 0.713555 | 0.718031 | -0.0044757 | 0.129715 | 0.600607 | 0.805295 | 0.927539 | 0.154075 |
| tossup_correctness | tier | regionals | 1937 | 0.575617 | 0.56888 | 0.0637493 | 0.18829 | 0.742385 | 0.758389 | -0.0160041 | 0.135603 | 0.564366 | 0.779052 | 0.905134 | 0.167091 |
| tossup_correctness | tier | winter | 2750 | 0.576787 | 0.555664 | 0.0582521 | 0.181741 | 0.762182 | 0.765818 | -0.00363636 | 0.123852 | 0.595536 | 0.790768 | 0.911267 | 0.16187 |
| tossup_correctness | category | Current Events | 126 | 0.477426 | 0.618005 | 0.152991 | 0.211971 | 0.690476 | 0.769841 | -0.0793651 | 0.144756 | 0.473377 | 0.679792 | 0.860863 | 0.201932 |
| tossup_correctness | category | Fine Arts | 1071 | 0.588068 | 0.553499 | 0.0533631 | 0.181087 | 0.760037 | 0.766573 | -0.00653595 | 0.115332 | 0.636408 | 0.80884 | 0.92345 | 0.150915 |
| tossup_correctness | category | Geography | 185 | 0.693937 | 0.563717 | 0.0277304 | 0.192024 | 0.713514 | 0.697297 | 0.0162162 | 0.145727 | 0.485455 | 0.722738 | 0.86591 | 0.188718 |
| tossup_correctness | category | History | 1440 | 0.561744 | 0.578851 | 0.07688 | 0.194978 | 0.722917 | 0.754167 | -0.03125 | 0.139245 | 0.530139 | 0.742131 | 0.888361 | 0.180887 |
| tossup_correctness | category | Literature | 1422 | 0.547525 | 0.509937 | 0.0588567 | 0.157207 | 0.807314 | 0.814346 | -0.00703235 | 0.104037 | 0.695928 | 0.852123 | 0.940639 | 0.129838 |
| tossup_correctness | category | Mythology | 318 | 0.616816 | 0.518094 | 0.0878007 | 0.168193 | 0.77673 | 0.789308 | -0.0125786 | 0.132512 | 0.524778 | 0.733124 | 0.880129 | 0.184979 |
| tossup_correctness | category | Other Academic | 66 | 0.681971 | 0.549369 | 0.0695836 | 0.187337 | 0.727273 | 0.712121 | 0.0151515 | 0.136188 | 0.584359 | 0.746252 | 0.876503 | 0.178595 |
| tossup_correctness | category | Philosophy | 311 | 0.583042 | 0.581658 | 0.0711747 | 0.19083 | 0.752412 | 0.745981 | 0.00643087 | 0.10173 | 0.680371 | 0.83367 | 0.923821 | 0.142323 |
| tossup_correctness | category | Popular Culture | 102 | 0.612037 | 0.506554 | 0.229642 | 0.165593 | 0.735294 | 0.882353 | -0.147059 | 0.170924 | 0.434981 | 0.686833 | 0.845893 | 0.19356 |
| tossup_correctness | category | Religion | 358 | 0.620484 | 0.607423 | 0.0670678 | 0.205088 | 0.703911 | 0.712291 | -0.00837989 | 0.128701 | 0.575158 | 0.788659 | 0.894001 | 0.166135 |
| tossup_correctness | category | Science | 1433 | 0.590888 | 0.572697 | 0.0762077 | 0.190572 | 0.741103 | 0.738311 | 0.00279135 | 0.125329 | 0.553546 | 0.742427 | 0.878703 | 0.182813 |
| tossup_correctness | category | Social Science | 324 | 0.538872 | 0.602946 | 0.0770096 | 0.203003 | 0.728395 | 0.731481 | -0.00308642 | 0.114821 | 0.594705 | 0.763634 | 0.890054 | 0.175336 |
| tossup_correctness | category | Unknown | 1937 | 0.575617 | 0.56888 | 0.0637493 | 0.18829 | 0.742385 | 0.758389 | -0.0160041 | 0.135603 | 0.564366 | 0.779052 | 0.905134 | 0.167091 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.537815 | 0.640806 | 0.0974503 | 0.221946 | 0.676647 | 0.712575 | -0.0359281 | 0.14334 | 0.454524 | 0.675559 | 0.832114 | 0.204332 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.578777 | 0.605436 | 0.0825842 | 0.205962 | 0.70614 | 0.729167 | -0.0230263 | 0.135946 | 0.497823 | 0.683412 | 0.835704 | 0.202828 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.578659 | 0.566186 | 0.0661133 | 0.189259 | 0.734752 | 0.755083 | -0.020331 | 0.13265 | 0.527858 | 0.738568 | 0.873963 | 0.185287 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.573953 | 0.536246 | 0.062863 | 0.174664 | 0.769339 | 0.780942 | -0.0116034 | 0.120928 | 0.598092 | 0.791648 | 0.903201 | 0.163312 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.5995 | 0.563297 | 0.064913 | 0.182538 | 0.757774 | 0.762029 | -0.00425532 | 0.116476 | 0.651702 | 0.834802 | 0.935064 | 0.140156 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | -2.2602 | 0.63813 | -4.36261 | -3.38034 | -2.65552 | -2.23411 | -1.83538 | -1.25205 | -0.416869 |
| player | theta_norm | 1167 | 2.2602 | 0.63813 | 0.416869 | 1.25205 | 1.83538 | 2.23411 | 2.65552 | 3.38034 | 4.36261 |
| tossup | start_difficulty_d1 | 1220 | -2.96986 | 0.434131 | -4.39527 | -3.6283 | -3.28675 | -2.99324 | -2.68451 | -2.24986 | -1.3075 |
| tossup | end_difficulty_d1 | 1220 | -3.9699 | 0.710682 | -9.4048 | -5.12572 | -4.39965 | -3.93284 | -3.5014 | -2.89267 | -2.00366 |
| tossup | total_drop_d1 | 1220 | 1.00004 | 0.451269 | 0.365964 | 0.526831 | 0.711498 | 0.913116 | 1.156 | 1.7174 | 6.44687 |
| tossup | drop_share_1_d1 | 1220 | 0.370512 | 0.0612644 | 0.178515 | 0.272172 | 0.330038 | 0.372021 | 0.409319 | 0.468275 | 0.575291 |
| tossup | drop_share_2_d1 | 1220 | 0.331695 | 0.0252909 | 0.254881 | 0.297168 | 0.316541 | 0.329185 | 0.342497 | 0.374163 | 0.512082 |
| tossup | drop_share_3_d1 | 1220 | 0.297793 | 0.0610328 | 0.133389 | 0.204135 | 0.255234 | 0.294011 | 0.335413 | 0.408429 | 0.490687 |
| tossup | r_1 | 1220 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| tossup | r_norm | 1220 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
