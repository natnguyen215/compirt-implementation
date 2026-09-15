# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-10000-20260913-195429/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-10000-20260913-195429/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 277353 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.724378 |
| log_loss | 0.476309 |
| ece | 0.0112732 |
| brier | 0.153939 |
| accuracy | 0.785868 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0125135 |
| probability_std | 0.147834 |
| probability_p10 | 0.564707 |
| probability_p50 | 0.807051 |
| probability_p90 | 0.919385 |
| mean_predictive_variance | 0.155359 |
| integrated_brier_score | 0.0951315 |
| joint_tossup_event_log_loss | 6.45976 |
| buzz_position_mae | 0.14112 |
| buzz_position_median_absolute_error | 0.120138 |
| buzz_position_bias | -0.0154183 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.36343 |
| first_buzzer_mean_reciprocal_rank | 0.573736 |
| first_buzzer_log_loss | 1.65097 |
| first_buzzer_events | 9270 |
| first_buzzer_player_replay_accuracy | 0.219957 |
| first_buzzer_team_replay_accuracy | 0.48425 |
| tossup_scorer_player_replay_accuracy | 0.240725 |
| tossup_scorer_team_replay_accuracy | 0.459595 |
| tossup_game_winner_accuracy | 0.676856 |
| tossup_model_official_winner_accuracy | 0.696121 |
| tossup_game_margin_mae | 50.3412 |
| tossup_game_zero_margin_mae | 58.0704 |
| tournament_player_ppg_spearman | 0.619928 |
| tournament_player_ppg_mae | 12.5652 |
| tournament_player_ppg_top10_overlap | 0.641379 |
| tournament_player_ppg_top10_random_overlap | 0.291672 |
| tournament_player_ppg_top10_adjusted_overlap | 0.482657 |
| neg_auroc | 0.724378 |
| neg_average_precision | 0.45018 |
| neg_precision | 0.596346 |
| neg_recall | 0.170871 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.171806 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0217473 |
| no_buzz_calibration_error | 0.0100202 |
| no_buzz_brier | 0.0122691 |
| full_pmf_max_mass_error | 5.55112e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9380 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 464 |
| first_buzzer_player_replay_accuracy_events | 9270 |
| first_buzzer_team_replay_accuracy_events | 9270 |
| tossup_scorer_player_replay_accuracy_events | 9380 |
| tossup_scorer_team_replay_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 458 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.676856 |
| tossup_game_margin_mae | 50.3412 |
| tossup_game_zero_margin_mae | 58.0704 |
| tossup_game_margin_mae_games | 469 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 458 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.724378 | 0.476309 | 0.0112732 | 0.153939 | 0.785868 | 0.773355 | 0.0125135 | 0.147834 | 0.564707 | 0.807051 | 0.919385 | 0.155359 |
| tossup_correctness | tier | fall | 2876 | 0.731299 | 0.451411 | 0.0130737 | 0.144025 | 0.80146 | 0.793115 | 0.00834492 | 0.141467 | 0.576299 | 0.816277 | 0.92377 | 0.151485 |
| tossup_correctness | tier | nationals | 1579 | 0.713251 | 0.528277 | 0.0347603 | 0.174824 | 0.748575 | 0.729576 | 0.0189994 | 0.16137 | 0.538275 | 0.803242 | 0.914303 | 0.157439 |
| tossup_correctness | tier | regionals | 1990 | 0.737353 | 0.478478 | 0.0183567 | 0.15541 | 0.78191 | 0.765829 | 0.0160804 | 0.149521 | 0.547614 | 0.797847 | 0.915529 | 0.159265 |
| tossup_correctness | tier | winter | 2825 | 0.713108 | 0.471082 | 0.020319 | 0.151323 | 0.793628 | 0.783009 | 0.0106195 | 0.14421 | 0.577375 | 0.806964 | 0.917793 | 0.155388 |
| tossup_correctness | category | Current Events | 123 | 0.804842 | 0.446304 | 0.0847238 | 0.143171 | 0.788618 | 0.764228 | 0.0243902 | 0.135738 | 0.552005 | 0.74403 | 0.907506 | 0.171907 |
| tossup_correctness | category | Fine Arts | 1093 | 0.739336 | 0.466898 | 0.0122396 | 0.149547 | 0.798719 | 0.769442 | 0.0292772 | 0.148907 | 0.567349 | 0.818145 | 0.921225 | 0.152283 |
| tossup_correctness | category | Geography | 191 | 0.785953 | 0.490103 | 0.078432 | 0.15863 | 0.790576 | 0.691099 | 0.0994764 | 0.207309 | 0.398275 | 0.761218 | 0.900916 | 0.168408 |
| tossup_correctness | category | History | 1469 | 0.710567 | 0.504059 | 0.0267759 | 0.166035 | 0.760381 | 0.758339 | 0.00204221 | 0.147494 | 0.561341 | 0.802729 | 0.919025 | 0.156703 |
| tossup_correctness | category | Literature | 1436 | 0.708251 | 0.436107 | 0.0181056 | 0.136748 | 0.817549 | 0.81546 | 0.00208914 | 0.125339 | 0.643278 | 0.843304 | 0.928628 | 0.139947 |
| tossup_correctness | category | Mythology | 325 | 0.663804 | 0.422841 | 0.0509297 | 0.131383 | 0.84 | 0.843077 | -0.00307692 | 0.108501 | 0.658087 | 0.80869 | 0.9116 | 0.150166 |
| tossup_correctness | category | Other Academic | 67 | 0.67655 | 0.498 | 0.0705016 | 0.162156 | 0.791045 | 0.791045 | 0 | 0.141103 | 0.533345 | 0.754889 | 0.89513 | 0.171376 |
| tossup_correctness | category | Philosophy | 322 | 0.68643 | 0.487496 | 0.0267415 | 0.1593 | 0.776398 | 0.785714 | -0.00931677 | 0.131203 | 0.610543 | 0.810923 | 0.931902 | 0.15166 |
| tossup_correctness | category | Popular Culture | 100 | 0.565884 | 0.362452 | 0.0475015 | 0.105381 | 0.89 | 0.89 | 0 | 0.0755261 | 0.745533 | 0.856818 | 0.924219 | 0.126991 |
| tossup_correctness | category | Religion | 365 | 0.664191 | 0.56033 | 0.0756889 | 0.187734 | 0.723288 | 0.723288 | 0 | 0.150519 | 0.540139 | 0.781075 | 0.908975 | 0.166329 |
| tossup_correctness | category | Science | 1456 | 0.721354 | 0.482966 | 0.0114327 | 0.156453 | 0.779533 | 0.76717 | 0.0123626 | 0.151705 | 0.548656 | 0.794328 | 0.910605 | 0.160695 |
| tossup_correctness | category | Social Science | 333 | 0.752812 | 0.498354 | 0.0246734 | 0.163348 | 0.75976 | 0.72973 | 0.03003 | 0.178209 | 0.447427 | 0.77306 | 0.912318 | 0.167628 |
| tossup_correctness | category | Unknown | 1990 | 0.737353 | 0.478478 | 0.0183567 | 0.15541 | 0.78191 | 0.765829 | 0.0160804 | 0.149521 | 0.547614 | 0.797847 | 0.915529 | 0.159265 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.760033 | 0.489579 | 0.0607521 | 0.160617 | 0.759777 | 0.748603 | 0.0111732 | 0.159362 | 0.476115 | 0.764019 | 0.886307 | 0.1759 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.70699 | 0.500276 | 0.0219718 | 0.163389 | 0.76698 | 0.754441 | 0.0125392 | 0.148052 | 0.542058 | 0.783458 | 0.905278 | 0.165419 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.727335 | 0.482218 | 0.0160469 | 0.156596 | 0.783931 | 0.766682 | 0.0172492 | 0.146143 | 0.574717 | 0.804828 | 0.918085 | 0.155653 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.714212 | 0.46353 | 0.0152227 | 0.148162 | 0.800537 | 0.787441 | 0.013096 | 0.136758 | 0.603677 | 0.818245 | 0.921148 | 0.150587 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.73287 | 0.476218 | 0.0150447 | 0.154316 | 0.780224 | 0.771758 | 0.00846597 | 0.157049 | 0.529051 | 0.809562 | 0.922717 | 0.155446 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 1.29012 | 0.79581 | -1.04055 | 0.00759271 | 0.751206 | 1.30124 | 1.79351 | 2.69434 | 3.4162 |
| player | theta_1 | 1196 | -0.531527 | 0.915092 | -3.46389 | -1.83458 | -1.12083 | -0.641333 | -0.018886 | 1.10156 | 3.6149 |
| player | theta_2 | 1196 | -0.492336 | 0.839357 | -2.56188 | -1.76232 | -1.05318 | -0.574593 | -0.00297843 | 1.0132 | 2.66473 |
| player | theta_3 | 1196 | -0.57456 | 0.859703 | -2.945 | -1.88343 | -1.11325 | -0.678981 | -0.0612863 | 0.994384 | 2.823 |
| player | theta_norm | 1196 | 1.65374 | 0.632139 | 0.181118 | 0.704596 | 1.20169 | 1.60771 | 2.02808 | 2.75922 | 4.3993 |
| tossup | start_difficulty_d1 | 1240 | -1.10028 | 0.53429 | -2.73967 | -1.85871 | -1.45079 | -1.13018 | -0.804112 | -0.202985 | 2.08077 |
| tossup | start_difficulty_d2 | 1240 | -1.09983 | 0.492748 | -2.9502 | -1.82408 | -1.41736 | -1.12537 | -0.805942 | -0.277372 | 0.970684 |
| tossup | start_difficulty_d3 | 1240 | -1.09982 | 0.500449 | -3.01983 | -1.84578 | -1.42893 | -1.13846 | -0.787041 | -0.285357 | 1.44131 |
| tossup | end_difficulty_d1 | 1240 | -2.09568 | 0.621681 | -3.8426 | -2.99504 | -2.51343 | -2.13741 | -1.73645 | -1.05699 | 1.37631 |
| tossup | end_difficulty_d2 | 1240 | -2.09476 | 0.579468 | -4.19248 | -2.95791 | -2.47047 | -2.13019 | -1.75424 | -1.10704 | 0.22357 |
| tossup | end_difficulty_d3 | 1240 | -2.09664 | 0.583456 | -4.34111 | -2.96676 | -2.47768 | -2.11548 | -1.72786 | -1.15729 | 0.735915 |
| tossup | total_drop_d1 | 1240 | 0.995392 | 0.10952 | 0.595031 | 0.823129 | 0.924098 | 0.997346 | 1.06342 | 1.17874 | 1.47499 |
| tossup | total_drop_d2 | 1240 | 0.994932 | 0.104465 | 0.612105 | 0.821949 | 0.926721 | 0.996061 | 1.06082 | 1.16289 | 1.3719 |
| tossup | total_drop_d3 | 1240 | 0.996823 | 0.116706 | 0.633384 | 0.836558 | 0.925686 | 0.993071 | 1.06624 | 1.15875 | 2.83419 |
| tossup | drop_share_1_d1 | 1240 | 0.304486 | 0.0152038 | 0.226104 | 0.279986 | 0.295201 | 0.305213 | 0.313967 | 0.327978 | 0.360717 |
| tossup | drop_share_2_d1 | 1240 | 0.346663 | 0.011538 | 0.311161 | 0.328421 | 0.338423 | 0.346785 | 0.354683 | 0.366039 | 0.382253 |
| tossup | drop_share_3_d1 | 1240 | 0.348851 | 0.0160319 | 0.299513 | 0.324653 | 0.338597 | 0.347758 | 0.358159 | 0.375189 | 0.454823 |
| tossup | drop_share_1_d2 | 1240 | 0.304846 | 0.015015 | 0.238717 | 0.280432 | 0.295518 | 0.305108 | 0.31487 | 0.328002 | 0.356045 |
| tossup | drop_share_2_d2 | 1240 | 0.347183 | 0.0114819 | 0.313891 | 0.328823 | 0.338828 | 0.347098 | 0.355387 | 0.366004 | 0.38132 |
| tossup | drop_share_3_d2 | 1240 | 0.347971 | 0.0154912 | 0.297744 | 0.3237 | 0.338068 | 0.3473 | 0.357007 | 0.374308 | 0.405224 |
| tossup | drop_share_1_d3 | 1240 | 0.304269 | 0.0151915 | 0.184863 | 0.280241 | 0.295502 | 0.304806 | 0.31397 | 0.328036 | 0.362602 |
| tossup | drop_share_2_d3 | 1240 | 0.347138 | 0.0121042 | 0.313408 | 0.328335 | 0.339483 | 0.347065 | 0.355045 | 0.365574 | 0.491322 |
| tossup | drop_share_3_d3 | 1240 | 0.348593 | 0.0155323 | 0.298916 | 0.324077 | 0.338396 | 0.34784 | 0.35827 | 0.374416 | 0.43219 |
| tossup | r_1 | 1240 | 0.31783 | 0.163327 | 0.042702 | 0.108213 | 0.189531 | 0.284084 | 0.422235 | 0.622632 | 0.880798 |
| tossup | r_2 | 1240 | 0.341771 | 0.163632 | 0.0562455 | 0.123301 | 0.216251 | 0.316667 | 0.449797 | 0.651277 | 0.834251 |
| tossup | r_3 | 1240 | 0.340399 | 0.163534 | 0.058546 | 0.124728 | 0.219014 | 0.306423 | 0.433688 | 0.659031 | 0.868437 |
| tossup | r_norm | 1240 | 0.64071 | 0.057597 | 0.577355 | 0.580446 | 0.597627 | 0.62431 | 0.665777 | 0.75684 | 0.884823 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 7.45667 | 0.491817 | 5.39828 | 6.62264 | 7.28841 | 7.44117 | 7.63609 | 8.38015 | 9.25193 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 7.52438 | 0.495533 | 4.11608 | 6.76777 | 7.36583 | 7.4921 | 7.68492 | 8.35326 | 10.0044 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 7.49116 | 0.521456 | 4.03961 | 6.63823 | 7.34123 | 7.47931 | 7.67477 | 8.39405 | 9.71692 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 4.14596 | 3.37626 | -12.5487 | -2.81922 | 1.99724 | 6.25563 | 6.45123 | 6.7269 | 7.41502 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 4.68824 | 3.31978 | -11.2307 | -2.75833 | 3.70379 | 6.37317 | 6.53439 | 6.84684 | 7.72592 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 4.52705 | 3.14786 | -18.2668 | -1.43487 | 2.24898 | 6.34796 | 6.52437 | 6.85456 | 8.15325 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.31071 | 3.45244 | 0.86631 | 0.956871 | 1.0065 | 1.06405 | 5.5385 | 10.2844 | 20.493 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.83614 | 3.41316 | 0.845348 | 0.944622 | 0.992713 | 1.03607 | 3.93745 | 10.3157 | 18.8416 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.96411 | 3.20046 | 0.817221 | 0.93743 | 0.991872 | 1.03979 | 5.28343 | 9.20427 | 26.0355 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.263452 | 0.0901054 | 0.0471601 | 0.0935539 | 0.210292 | 0.293623 | 0.306357 | 0.340456 | 0.722367 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.333885 | 0.0809587 | 0.0566283 | 0.169791 | 0.330804 | 0.345632 | 0.357061 | 0.457277 | 0.687078 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.402664 | 0.133299 | 0.116849 | 0.259815 | 0.341868 | 0.355718 | 0.399612 | 0.714458 | 0.892664 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.268139 | 0.0814321 | 0.0404176 | 0.10114 | 0.264407 | 0.294617 | 0.305952 | 0.323578 | 0.765557 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.337862 | 0.0724547 | 0.069565 | 0.183355 | 0.334606 | 0.346542 | 0.357435 | 0.43738 | 0.700657 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.393999 | 0.120594 | 0.0762679 | 0.28579 | 0.342856 | 0.355077 | 0.376832 | 0.687535 | 0.886759 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.268627 | 0.0836946 | 0.0369125 | 0.0973838 | 0.252775 | 0.294653 | 0.306769 | 0.332737 | 0.720265 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.336036 | 0.073908 | 0.0651502 | 0.180261 | 0.332317 | 0.346067 | 0.357659 | 0.445195 | 0.721216 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.395337 | 0.126577 | 0.0695457 | 0.269736 | 0.342344 | 0.355772 | 0.379608 | 0.71198 | 0.897937 |
| tossup_hazard | hazard_r_1 | 1240 | 0.357751 | 0.30457 | 0.0185401 | 0.0410309 | 0.0940326 | 0.217591 | 0.635884 | 0.896816 | 0.958184 |
| tossup_hazard | hazard_r_2 | 1240 | 0.303506 | 0.274062 | 0.0172393 | 0.0382314 | 0.0797909 | 0.173609 | 0.496825 | 0.857491 | 0.952237 |
| tossup_hazard | hazard_r_3 | 1240 | 0.338743 | 0.297359 | 0.0117323 | 0.0344523 | 0.0801952 | 0.203827 | 0.629265 | 0.857441 | 0.950305 |
