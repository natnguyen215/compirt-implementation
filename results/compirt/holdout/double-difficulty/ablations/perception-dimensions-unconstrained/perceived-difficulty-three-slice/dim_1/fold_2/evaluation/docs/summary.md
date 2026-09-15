# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_1/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_1/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 300619 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.585709 |
| log_loss | 0.557552 |
| ece | 0.062671 |
| brier | 0.184132 |
| accuracy | 0.749163 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0150157 |
| probability_std | 0.13552 |
| probability_p10 | 0.566359 |
| probability_p50 | 0.78315 |
| probability_p90 | 0.908746 |
| mean_predictive_variance | 0.165771 |
| integrated_brier_score | 0.107017 |
| joint_tossup_event_log_loss | 7.01625 |
| buzz_position_mae | 0.16488 |
| buzz_position_median_absolute_error | 0.14928 |
| buzz_position_bias | -0.0665867 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.316841 |
| first_buzzer_mean_reciprocal_rank | 0.533133 |
| first_buzzer_log_loss | 1.73721 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.637572 |
| tossup_scorer_player_top1_accuracy | 0.281343 |
| tossup_scorer_team_top1_accuracy | 0.451812 |
| tossup_game_winner_accuracy | 0.752174 |
| tossup_game_margin_mae | 41.1641 |
| tournament_player_ppg_spearman | 0.626222 |
| tournament_player_ppg_mae | 10.149 |
| tournament_player_ppg_top10_overlap | 0.568966 |
| neg_auroc | 0.585709 |
| neg_average_precision | 0.294011 |
| neg_precision | 0.350538 |
| neg_recall | 0.0746679 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0583656 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0885753 |
| no_buzz_calibration_error | 0.0754623 |
| no_buzz_brier | 0.0231979 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| tossup_correctness | aggregate | all | 9257 | 0.585709 | 0.557552 | 0.062671 | 0.184132 | 0.749163 | 0.764178 | -0.0150157 | 0.13552 | 0.566359 | 0.78315 | 0.908746 | 0.165771 |
| tossup_correctness | tier | fall | 2798 | 0.574489 | 0.542424 | 0.0821216 | 0.178278 | 0.758756 | 0.785204 | -0.0264475 | 0.139975 | 0.539987 | 0.763556 | 0.895514 | 0.174752 |
| tossup_correctness | tier | nationals | 1545 | 0.620141 | 0.596753 | 0.0766368 | 0.199936 | 0.72233 | 0.721036 | 0.0012945 | 0.131269 | 0.596301 | 0.806657 | 0.930422 | 0.154249 |
| tossup_correctness | tier | regionals | 2039 | 0.563405 | 0.569533 | 0.07401 | 0.188878 | 0.745954 | 0.762138 | -0.0161844 | 0.135267 | 0.55671 | 0.778275 | 0.901469 | 0.168738 |
| tossup_correctness | tier | winter | 2875 | 0.605366 | 0.542713 | 0.0481436 | 0.177971 | 0.756522 | 0.768348 | -0.0118261 | 0.130216 | 0.587311 | 0.794623 | 0.913035 | 0.161118 |
| tossup_correctness | category | Current Events | 129 | 0.524608 | 0.6775 | 0.106384 | 0.237052 | 0.651163 | 0.666667 | -0.0155039 | 0.143207 | 0.468103 | 0.694436 | 0.86036 | 0.199476 |
| tossup_correctness | category | Fine Arts | 1074 | 0.576824 | 0.54101 | 0.0607304 | 0.175815 | 0.769088 | 0.776536 | -0.00744879 | 0.116511 | 0.628119 | 0.815318 | 0.917042 | 0.151146 |
| tossup_correctness | category | Geography | 180 | 0.650999 | 0.652638 | 0.0843083 | 0.2274 | 0.65 | 0.616667 | 0.0333333 | 0.14443 | 0.497407 | 0.708756 | 0.875167 | 0.188749 |
| tossup_correctness | category | History | 1454 | 0.567048 | 0.575129 | 0.0867515 | 0.194222 | 0.723521 | 0.757909 | -0.0343879 | 0.143768 | 0.516362 | 0.749297 | 0.890549 | 0.178885 |
| tossup_correctness | category | Literature | 1435 | 0.562898 | 0.503593 | 0.0577276 | 0.156692 | 0.806969 | 0.810453 | -0.00348432 | 0.105672 | 0.673092 | 0.845488 | 0.94143 | 0.132975 |
| tossup_correctness | category | Mythology | 324 | 0.598583 | 0.525094 | 0.0803955 | 0.173451 | 0.753086 | 0.79321 | -0.0401235 | 0.139402 | 0.509997 | 0.740869 | 0.886912 | 0.182092 |
| tossup_correctness | category | Other Academic | 71 | 0.461874 | 0.621368 | 0.128021 | 0.204538 | 0.732394 | 0.760563 | -0.028169 | 0.115423 | 0.544313 | 0.759521 | 0.893926 | 0.175243 |
| tossup_correctness | category | Philosophy | 310 | 0.615323 | 0.548197 | 0.06576 | 0.180215 | 0.764516 | 0.76129 | 0.00322581 | 0.102521 | 0.67328 | 0.829541 | 0.930689 | 0.144556 |
| tossup_correctness | category | Popular Culture | 108 | 0.541667 | 0.532476 | 0.231171 | 0.176926 | 0.777778 | 0.888889 | -0.111111 | 0.164417 | 0.428334 | 0.688984 | 0.847114 | 0.198092 |
| tossup_correctness | category | Religion | 361 | 0.581568 | 0.585959 | 0.0821559 | 0.195126 | 0.739612 | 0.742382 | -0.00277008 | 0.142514 | 0.566527 | 0.788394 | 0.91172 | 0.16319 |
| tossup_correctness | category | Science | 1445 | 0.592529 | 0.56687 | 0.0616854 | 0.189536 | 0.732872 | 0.746021 | -0.0131488 | 0.131438 | 0.550671 | 0.742642 | 0.879709 | 0.182708 |
| tossup_correctness | category | Social Science | 327 | 0.672202 | 0.559077 | 0.0406672 | 0.188952 | 0.715596 | 0.718654 | -0.0030581 | 0.122111 | 0.562043 | 0.769686 | 0.88564 | 0.174184 |
| tossup_correctness | category | Unknown | 2039 | 0.563405 | 0.569533 | 0.07401 | 0.188878 | 0.745954 | 0.762138 | -0.0161844 | 0.135267 | 0.55671 | 0.778275 | 0.901469 | 0.168738 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.522372 | 0.635798 | 0.155525 | 0.219467 | 0.693989 | 0.743169 | -0.0491803 | 0.151117 | 0.412759 | 0.645857 | 0.816732 | 0.208058 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.566691 | 0.606563 | 0.0875006 | 0.207761 | 0.697382 | 0.728796 | -0.0314136 | 0.146739 | 0.463823 | 0.695252 | 0.843223 | 0.198909 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.571759 | 0.575017 | 0.0659467 | 0.192921 | 0.730683 | 0.752568 | -0.0218848 | 0.133995 | 0.528232 | 0.738224 | 0.876203 | 0.18408 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.610859 | 0.516026 | 0.048709 | 0.167473 | 0.776348 | 0.786087 | -0.00973913 | 0.122306 | 0.594156 | 0.791432 | 0.905318 | 0.163233 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.585629 | 0.563928 | 0.071646 | 0.183861 | 0.756739 | 0.764393 | -0.00765391 | 0.117072 | 0.637259 | 0.834874 | 0.93462 | 0.14145 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | -2.25829 | 0.635917 | -4.50591 | -3.34699 | -2.64614 | -2.24469 | -1.8422 | -1.26957 | -0.260879 |
| player | theta_norm | 1197 | 2.25829 | 0.635917 | 0.260879 | 1.26957 | 1.8422 | 2.24469 | 2.64614 | 3.34699 | 4.50591 |
| tossup | start_difficulty_d1 | 1240 | -2.96572 | 0.426986 | -4.2857 | -3.59739 | -3.28388 | -2.99573 | -2.67553 | -2.2555 | -1.51389 |
| tossup | end_difficulty_d1 | 1240 | -3.96668 | 0.690123 | -6.84679 | -5.15533 | -4.39149 | -3.92463 | -3.47688 | -2.90423 | -2.10709 |
| tossup | total_drop_d1 | 1240 | 1.00096 | 0.417066 | 0.384357 | 0.527119 | 0.715716 | 0.918356 | 1.16741 | 1.7507 | 3.59411 |
| tossup | drop_share_1_d1 | 1240 | 0.37047 | 0.0606826 | 0.175218 | 0.271044 | 0.330933 | 0.373018 | 0.410852 | 0.466574 | 0.592757 |
| tossup | drop_share_2_d1 | 1240 | 0.332027 | 0.0251258 | 0.257582 | 0.297581 | 0.317095 | 0.32942 | 0.342542 | 0.375018 | 0.479963 |
| tossup | drop_share_3_d1 | 1240 | 0.297503 | 0.060782 | 0.138063 | 0.20613 | 0.256023 | 0.292533 | 0.335578 | 0.4062 | 0.504019 |
| tossup | r_1 | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| tossup | r_norm | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
