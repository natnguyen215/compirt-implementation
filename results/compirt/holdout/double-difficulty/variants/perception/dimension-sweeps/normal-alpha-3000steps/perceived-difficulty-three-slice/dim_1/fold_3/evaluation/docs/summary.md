# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_1/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_1/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 302131 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.588191 |
| log_loss | 0.548829 |
| ece | 0.0567701 |
| brier | 0.180163 |
| accuracy | 0.756938 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0131057 |
| probability_std | 0.134497 |
| probability_p10 | 0.566616 |
| probability_p50 | 0.781801 |
| probability_p90 | 0.907957 |
| mean_predictive_variance | 0.166019 |
| integrated_brier_score | 0.106389 |
| joint_tossup_event_log_loss | 6.97983 |
| buzz_position_mae | 0.1658 |
| buzz_position_median_absolute_error | 0.151391 |
| buzz_position_bias | -0.0721161 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.31663 |
| first_buzzer_mean_reciprocal_rank | 0.533718 |
| first_buzzer_log_loss | 1.74575 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.630837 |
| tossup_scorer_player_top1_accuracy | 0.273319 |
| tossup_scorer_team_top1_accuracy | 0.469414 |
| tossup_game_winner_accuracy | 0.754425 |
| tossup_game_margin_mae | 40.5941 |
| tournament_player_ppg_spearman | 0.624106 |
| tournament_player_ppg_mae | 10.0786 |
| tournament_player_ppg_top10_overlap | 0.593103 |
| neg_auroc | 0.588191 |
| neg_average_precision | 0.296512 |
| neg_precision | 0.368653 |
| neg_recall | 0.0799808 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.056099 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0858513 |
| no_buzz_calibration_error | 0.0706669 |
| no_buzz_brier | 0.0235903 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9220 |
| first_buzzer_team_top1_accuracy_events | 9080 |
| tossup_scorer_player_top1_accuracy_events | 9220 |
| tossup_scorer_team_top1_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 452 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.588191 | 0.548829 | 0.0567701 | 0.180163 | 0.756938 | 0.770044 | -0.0131057 | 0.134497 | 0.566616 | 0.781801 | 0.907957 | 0.166019 |
| tossup_correctness | tier | fall | 2817 | 0.564999 | 0.547986 | 0.0811047 | 0.180081 | 0.759673 | 0.781683 | -0.0220092 | 0.137909 | 0.541398 | 0.757398 | 0.889947 | 0.176571 |
| tossup_correctness | tier | nationals | 1542 | 0.634868 | 0.573386 | 0.0639282 | 0.19138 | 0.728275 | 0.73476 | -0.00648508 | 0.132309 | 0.588563 | 0.807964 | 0.921297 | 0.154736 |
| tossup_correctness | tier | regionals | 1934 | 0.591922 | 0.562484 | 0.0481367 | 0.185531 | 0.745605 | 0.75698 | -0.0113754 | 0.132978 | 0.565735 | 0.779816 | 0.90343 | 0.168139 |
| tossup_correctness | tier | winter | 2787 | 0.589681 | 0.52662 | 0.0555518 | 0.170316 | 0.777897 | 0.786868 | -0.00897022 | 0.129347 | 0.589233 | 0.79262 | 0.915968 | 0.160126 |
| tossup_correctness | category | Current Events | 125 | 0.534091 | 0.647427 | 0.125647 | 0.22678 | 0.632 | 0.704 | -0.072 | 0.153436 | 0.45532 | 0.70383 | 0.856951 | 0.195545 |
| tossup_correctness | category | Fine Arts | 1072 | 0.591252 | 0.542315 | 0.0531499 | 0.177359 | 0.762127 | 0.770522 | -0.00839552 | 0.111535 | 0.643868 | 0.81903 | 0.918226 | 0.15064 |
| tossup_correctness | category | Geography | 185 | 0.724336 | 0.552281 | 0.0502227 | 0.184653 | 0.713514 | 0.702703 | 0.0108108 | 0.141386 | 0.497532 | 0.711989 | 0.851661 | 0.193932 |
| tossup_correctness | category | History | 1443 | 0.602184 | 0.550608 | 0.0648492 | 0.18382 | 0.742204 | 0.765073 | -0.022869 | 0.14282 | 0.520381 | 0.738379 | 0.88306 | 0.182802 |
| tossup_correctness | category | Literature | 1411 | 0.525681 | 0.516414 | 0.0727462 | 0.161213 | 0.810064 | 0.81219 | -0.00212615 | 0.10323 | 0.690996 | 0.852428 | 0.939383 | 0.130819 |
| tossup_correctness | category | Mythology | 320 | 0.531496 | 0.561821 | 0.103054 | 0.183641 | 0.7625 | 0.79375 | -0.03125 | 0.136741 | 0.53675 | 0.744222 | 0.870165 | 0.183519 |
| tossup_correctness | category | Other Academic | 64 | 0.561198 | 0.581001 | 0.163185 | 0.19456 | 0.734375 | 0.75 | -0.015625 | 0.121536 | 0.596479 | 0.778854 | 0.90868 | 0.168684 |
| tossup_correctness | category | Philosophy | 312 | 0.536 | 0.518629 | 0.0664886 | 0.165441 | 0.798077 | 0.801282 | -0.00320513 | 0.110881 | 0.648988 | 0.834323 | 0.923027 | 0.144844 |
| tossup_correctness | category | Popular Culture | 104 | 0.49858 | 0.57579 | 0.223901 | 0.196033 | 0.721154 | 0.846154 | -0.125 | 0.165105 | 0.40929 | 0.63075 | 0.848611 | 0.203269 |
| tossup_correctness | category | Religion | 358 | 0.607104 | 0.597925 | 0.0782171 | 0.201134 | 0.701117 | 0.726257 | -0.0251397 | 0.146835 | 0.561409 | 0.789648 | 0.914438 | 0.163401 |
| tossup_correctness | category | Science | 1431 | 0.613902 | 0.538126 | 0.0417989 | 0.177605 | 0.761705 | 0.765199 | -0.00349406 | 0.125723 | 0.553703 | 0.747081 | 0.867917 | 0.182919 |
| tossup_correctness | category | Social Science | 321 | 0.588172 | 0.576635 | 0.0663853 | 0.194153 | 0.725857 | 0.744548 | -0.0186916 | 0.120706 | 0.589103 | 0.769588 | 0.880012 | 0.174434 |
| tossup_correctness | category | Unknown | 1934 | 0.591922 | 0.562484 | 0.0481367 | 0.185531 | 0.745605 | 0.75698 | -0.0113754 | 0.132978 | 0.565735 | 0.779816 | 0.90343 | 0.168139 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.60229 | 0.615625 | 0.0798938 | 0.212981 | 0.666667 | 0.697917 | -0.03125 | 0.149265 | 0.429435 | 0.644581 | 0.815384 | 0.208639 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.573451 | 0.603004 | 0.0978102 | 0.206118 | 0.703037 | 0.733408 | -0.0303712 | 0.146675 | 0.459707 | 0.676344 | 0.83879 | 0.201971 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.563316 | 0.571636 | 0.0670345 | 0.190879 | 0.738009 | 0.759276 | -0.021267 | 0.130338 | 0.540351 | 0.739044 | 0.87343 | 0.1847 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.588049 | 0.520873 | 0.049996 | 0.168861 | 0.779714 | 0.789125 | -0.00941094 | 0.121437 | 0.599 | 0.790314 | 0.903306 | 0.163776 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.599734 | 0.53815 | 0.0445608 | 0.173098 | 0.771233 | 0.775342 | -0.00410959 | 0.115084 | 0.647921 | 0.835622 | 0.932452 | 0.140337 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | -2.28829 | 0.635212 | -4.56248 | -3.42053 | -2.69391 | -2.26785 | -1.85323 | -1.29476 | -0.398435 |
| player | theta_norm | 1133 | 2.28829 | 0.635212 | 0.398435 | 1.29476 | 1.85323 | 2.26785 | 2.69391 | 3.42053 | 4.56248 |
| tossup | start_difficulty_d1 | 1240 | -2.96305 | 0.435537 | -4.18503 | -3.62118 | -3.26444 | -2.99631 | -2.66549 | -2.23381 | -1.4797 |
| tossup | end_difficulty_d1 | 1240 | -3.95802 | 0.685933 | -7.24402 | -5.0916 | -4.38677 | -3.92389 | -3.48171 | -2.88373 | -2.13998 |
| tossup | total_drop_d1 | 1240 | 0.994968 | 0.406744 | 0.360637 | 0.528868 | 0.708305 | 0.909166 | 1.1607 | 1.70208 | 4.07048 |
| tossup | drop_share_1_d1 | 1240 | 0.369782 | 0.0608087 | 0.162993 | 0.27311 | 0.33063 | 0.371341 | 0.409058 | 0.466549 | 0.600383 |
| tossup | drop_share_2_d1 | 1240 | 0.331944 | 0.0252012 | 0.254577 | 0.297617 | 0.317284 | 0.330014 | 0.342179 | 0.372675 | 0.508836 |
| tossup | drop_share_3_d1 | 1240 | 0.298273 | 0.0607038 | 0.135879 | 0.207232 | 0.256779 | 0.29372 | 0.335648 | 0.408739 | 0.486121 |
| tossup | r_1 | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| tossup | r_norm | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
