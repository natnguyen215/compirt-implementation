# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-20260913-150350/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-20260913-150350/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 284524 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.715926 |
| log_loss | 0.489687 |
| ece | 0.0130247 |
| brier | 0.15918 |
| accuracy | 0.776762 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0115116 |
| probability_std | 0.139542 |
| probability_p10 | 0.582291 |
| probability_p50 | 0.815234 |
| probability_p90 | 0.916691 |
| mean_predictive_variance | 0.153756 |
| integrated_brier_score | 0.102274 |
| joint_tossup_event_log_loss | 6.61322 |
| buzz_position_mae | 0.15537 |
| buzz_position_median_absolute_error | 0.13828 |
| buzz_position_bias | -0.0475459 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.357181 |
| first_buzzer_mean_reciprocal_rank | 0.569737 |
| first_buzzer_log_loss | 1.6655 |
| first_buzzer_events | 9295 |
| first_buzzer_player_replay_accuracy | 0.177192 |
| first_buzzer_team_replay_accuracy | 0.402044 |
| tossup_scorer_player_replay_accuracy | 0.211465 |
| tossup_scorer_team_replay_accuracy | 0.392887 |
| tossup_game_winner_accuracy | 0.654102 |
| tossup_model_official_winner_accuracy | 0.67735 |
| tossup_game_margin_mae | 49.4904 |
| tossup_game_zero_margin_mae | 54.8195 |
| tournament_player_ppg_spearman | 0.54796 |
| tournament_player_ppg_mae | 12.8284 |
| tournament_player_ppg_top10_overlap | 0.596552 |
| tournament_player_ppg_top10_random_overlap | 0.282327 |
| tournament_player_ppg_top10_adjusted_overlap | 0.444004 |
| neg_auroc | 0.715926 |
| neg_average_precision | 0.44876 |
| neg_precision | 0.606362 |
| neg_recall | 0.13978 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.175218 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0331827 |
| no_buzz_calibration_error | 0.0199131 |
| no_buzz_brier | 0.0156462 |
| full_pmf_max_mass_error | 5.55112e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9420 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 468 |
| first_buzzer_player_replay_accuracy_events | 9295 |
| first_buzzer_team_replay_accuracy_events | 9295 |
| tossup_scorer_player_replay_accuracy_events | 9420 |
| tossup_scorer_team_replay_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 451 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.654102 |
| tossup_game_margin_mae | 49.4904 |
| tossup_game_zero_margin_mae | 54.8195 |
| tossup_game_margin_mae_games | 471 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 451 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.715926 | 0.489687 | 0.0130247 | 0.15918 | 0.776762 | 0.76525 | 0.0115116 | 0.139542 | 0.582291 | 0.815234 | 0.916691 | 0.153756 |
| tossup_correctness | tier | fall | 2933 | 0.712451 | 0.462283 | 0.0110293 | 0.147861 | 0.797477 | 0.791681 | 0.00579611 | 0.140951 | 0.582789 | 0.823076 | 0.922388 | 0.150097 |
| tossup_correctness | tier | nationals | 1584 | 0.711155 | 0.531931 | 0.040146 | 0.175886 | 0.748737 | 0.724747 | 0.0239899 | 0.145927 | 0.554964 | 0.808191 | 0.910682 | 0.158537 |
| tossup_correctness | tier | regionals | 1886 | 0.711561 | 0.515392 | 0.0285129 | 0.170519 | 0.755037 | 0.746023 | 0.00901379 | 0.132997 | 0.584209 | 0.801391 | 0.907876 | 0.159979 |
| tossup_correctness | tier | winter | 2892 | 0.720996 | 0.477578 | 0.0121186 | 0.154115 | 0.78527 | 0.773167 | 0.0121024 | 0.137987 | 0.599796 | 0.818937 | 0.9195 | 0.150791 |
| tossup_correctness | category | Current Events | 124 | 0.675338 | 0.524325 | 0.106583 | 0.169482 | 0.758065 | 0.75 | 0.00806452 | 0.155467 | 0.545407 | 0.766448 | 0.916863 | 0.166707 |
| tossup_correctness | category | Fine Arts | 1103 | 0.709934 | 0.497256 | 0.0214265 | 0.161472 | 0.774252 | 0.759746 | 0.0145059 | 0.144741 | 0.59302 | 0.820399 | 0.921543 | 0.150917 |
| tossup_correctness | category | Geography | 197 | 0.78683 | 0.517775 | 0.0752701 | 0.171035 | 0.741117 | 0.670051 | 0.071066 | 0.207629 | 0.405977 | 0.744539 | 0.907923 | 0.169346 |
| tossup_correctness | category | History | 1491 | 0.726576 | 0.4617 | 0.0171648 | 0.14824 | 0.791415 | 0.787391 | 0.00402414 | 0.132314 | 0.594278 | 0.815997 | 0.920033 | 0.153166 |
| tossup_correctness | category | Literature | 1472 | 0.730035 | 0.437528 | 0.0276985 | 0.137701 | 0.8125 | 0.804348 | 0.00815217 | 0.115504 | 0.652964 | 0.848849 | 0.923324 | 0.137455 |
| tossup_correctness | category | Mythology | 332 | 0.692712 | 0.447868 | 0.0198716 | 0.140986 | 0.816265 | 0.813253 | 0.00301205 | 0.111608 | 0.637495 | 0.83192 | 0.913877 | 0.145097 |
| tossup_correctness | category | Other Academic | 69 | 0.702489 | 0.507186 | 0.0775224 | 0.166984 | 0.782609 | 0.753623 | 0.0289855 | 0.0992152 | 0.646645 | 0.789012 | 0.89715 | 0.163879 |
| tossup_correctness | category | Philosophy | 324 | 0.691773 | 0.463294 | 0.0293421 | 0.147915 | 0.79321 | 0.799383 | -0.00617284 | 0.121275 | 0.615404 | 0.815826 | 0.920988 | 0.152162 |
| tossup_correctness | category | Popular Culture | 102 | 0.431142 | 0.484542 | 0.0531024 | 0.1483 | 0.823529 | 0.833333 | -0.00980392 | 0.078497 | 0.738575 | 0.850897 | 0.907633 | 0.13056 |
| tossup_correctness | category | Religion | 372 | 0.718996 | 0.54149 | 0.0475316 | 0.182823 | 0.733871 | 0.709677 | 0.0241935 | 0.146555 | 0.531982 | 0.769271 | 0.906163 | 0.169708 |
| tossup_correctness | category | Science | 1487 | 0.688741 | 0.515548 | 0.0275766 | 0.169498 | 0.766644 | 0.752522 | 0.0141224 | 0.14921 | 0.536651 | 0.803576 | 0.915966 | 0.158966 |
| tossup_correctness | category | Social Science | 336 | 0.730593 | 0.536937 | 0.0410663 | 0.178594 | 0.735119 | 0.702381 | 0.0327381 | 0.174939 | 0.47736 | 0.790653 | 0.91413 | 0.162597 |
| tossup_correctness | category | Unknown | 1886 | 0.711561 | 0.515392 | 0.0285129 | 0.170519 | 0.755037 | 0.746023 | 0.00901379 | 0.132997 | 0.584209 | 0.801391 | 0.907876 | 0.159979 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.694562 | 0.522705 | 0.0685664 | 0.16736 | 0.786802 | 0.736041 | 0.0507614 | 0.143033 | 0.536004 | 0.75965 | 0.890057 | 0.175253 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.716782 | 0.520173 | 0.0269102 | 0.172544 | 0.747208 | 0.735025 | 0.0121827 | 0.142279 | 0.558906 | 0.796617 | 0.905368 | 0.162378 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.700183 | 0.495223 | 0.0191933 | 0.161137 | 0.773434 | 0.769436 | 0.00399822 | 0.136113 | 0.600832 | 0.818073 | 0.916622 | 0.152172 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.703434 | 0.475131 | 0.0158393 | 0.152679 | 0.794487 | 0.78402 | 0.0104676 | 0.130932 | 0.610055 | 0.828216 | 0.922204 | 0.147794 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.737085 | 0.487258 | 0.0242566 | 0.158997 | 0.771362 | 0.756008 | 0.0153538 | 0.146862 | 0.55797 | 0.811951 | 0.916275 | 0.156402 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 2.65875 | 0.734018 | 0.47835 | 1.4409 | 2.15977 | 2.64658 | 3.12634 | 3.93248 | 4.58401 |
| player | theta_1 | 1186 | -1.19315 | 0.827285 | -3.64195 | -2.48455 | -1.71728 | -1.25379 | -0.709609 | 0.249875 | 1.90901 |
| player | theta_2 | 1186 | -1.01057 | 0.668999 | -3.49548 | -2.04405 | -1.45295 | -1.04627 | -0.599414 | 0.116771 | 1.53165 |
| player | theta_3 | 1186 | -1.11401 | 0.781236 | -3.39163 | -2.30535 | -1.65431 | -1.17047 | -0.629571 | 0.299109 | 2.26422 |
| player | theta_norm | 1186 | 2.25026 | 0.602779 | 0.108407 | 1.34236 | 1.83 | 2.21138 | 2.62838 | 3.28792 | 4.40152 |
| tossup | start_difficulty_d1 | 1240 | -1.77543 | 0.5509 | -3.74568 | -2.52765 | -2.15507 | -1.83903 | -1.45062 | -0.813857 | 1.10997 |
| tossup | start_difficulty_d2 | 1240 | -1.76542 | 0.511975 | -3.26014 | -2.51903 | -2.11588 | -1.82528 | -1.4446 | -0.802179 | 0.322979 |
| tossup | start_difficulty_d3 | 1240 | -1.7649 | 0.513605 | -3.6115 | -2.55377 | -2.12367 | -1.8041 | -1.43401 | -0.891608 | 0.986473 |
| tossup | end_difficulty_d1 | 1240 | -2.76436 | 0.641503 | -4.94299 | -3.65697 | -3.2079 | -2.84284 | -2.38797 | -1.676 | 0.514132 |
| tossup | end_difficulty_d2 | 1240 | -2.75158 | 0.599474 | -4.59041 | -3.67502 | -3.15385 | -2.80324 | -2.37255 | -1.65718 | -0.320686 |
| tossup | end_difficulty_d3 | 1240 | -2.74892 | 0.598881 | -4.89819 | -3.68693 | -3.16832 | -2.77816 | -2.36617 | -1.75195 | 0.25686 |
| tossup | total_drop_d1 | 1240 | 0.98893 | 0.110865 | 0.59584 | 0.801991 | 0.916153 | 0.994352 | 1.06175 | 1.15213 | 1.45382 |
| tossup | total_drop_d2 | 1240 | 0.986164 | 0.103082 | 0.643664 | 0.815929 | 0.916555 | 0.988935 | 1.05664 | 1.15492 | 1.33028 |
| tossup | total_drop_d3 | 1240 | 0.98402 | 0.103445 | 0.6128 | 0.818288 | 0.912618 | 0.986244 | 1.0509 | 1.15747 | 1.38049 |
| tossup | drop_share_1_d1 | 1240 | 0.30411 | 0.0154339 | 0.231161 | 0.279061 | 0.294485 | 0.304511 | 0.314115 | 0.327875 | 0.366518 |
| tossup | drop_share_2_d1 | 1240 | 0.347125 | 0.01146 | 0.310466 | 0.327662 | 0.339489 | 0.347129 | 0.354931 | 0.365023 | 0.400573 |
| tossup | drop_share_3_d1 | 1240 | 0.348765 | 0.0164135 | 0.296442 | 0.324126 | 0.337715 | 0.347994 | 0.359107 | 0.375415 | 0.416508 |
| tossup | drop_share_1_d2 | 1240 | 0.303646 | 0.0140256 | 0.254206 | 0.278998 | 0.29475 | 0.303951 | 0.313163 | 0.326538 | 0.342438 |
| tossup | drop_share_2_d2 | 1240 | 0.346938 | 0.0114264 | 0.309548 | 0.327578 | 0.339288 | 0.346667 | 0.354796 | 0.365452 | 0.386142 |
| tossup | drop_share_3_d2 | 1240 | 0.349416 | 0.015545 | 0.303359 | 0.325009 | 0.338881 | 0.349668 | 0.359396 | 0.375715 | 0.417248 |
| tossup | drop_share_1_d3 | 1240 | 0.303565 | 0.0148738 | 0.246454 | 0.278722 | 0.29401 | 0.303843 | 0.313977 | 0.326996 | 0.357694 |
| tossup | drop_share_2_d3 | 1240 | 0.347139 | 0.0111721 | 0.306485 | 0.329142 | 0.340035 | 0.347007 | 0.354414 | 0.365585 | 0.385759 |
| tossup | drop_share_3_d3 | 1240 | 0.349296 | 0.0157405 | 0.303311 | 0.325434 | 0.33864 | 0.348838 | 0.358633 | 0.3764 | 0.430981 |
| tossup | r_1 | 1240 | 0.32009 | 0.140199 | 0.0742168 | 0.136606 | 0.218354 | 0.294687 | 0.403899 | 0.584566 | 0.82104 |
| tossup | r_2 | 1240 | 0.334566 | 0.117994 | 0.0568751 | 0.158924 | 0.251663 | 0.324245 | 0.400455 | 0.551092 | 0.794968 |
| tossup | r_3 | 1240 | 0.345345 | 0.126037 | 0.0756469 | 0.159112 | 0.254904 | 0.338653 | 0.415454 | 0.583927 | 0.828646 |
| tossup | r_norm | 1240 | 0.617515 | 0.0418915 | 0.577444 | 0.57922 | 0.58834 | 0.604716 | 0.632404 | 0.699773 | 0.837528 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.49831 | 0.478339 | 1.84835 | 3.80224 | 4.22849 | 4.45467 | 4.75044 | 5.38981 | 6.37709 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.45486 | 0.427826 | 2.33822 | 3.764 | 4.23399 | 4.438 | 4.66316 | 5.16835 | 6.57488 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.48906 | 0.437204 | 2.61679 | 3.78079 | 4.24765 | 4.47207 | 4.72995 | 5.22498 | 6.20299 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.85035 | 2.21082 | -10.2502 | -3.03666 | 0.862531 | 2.87769 | 3.28943 | 3.66678 | 4.39591 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.26611 | 2.09412 | -8.21838 | -2.8009 | 2.34015 | 3.12177 | 3.39349 | 3.70094 | 4.27278 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.26693 | 2.08773 | -8.49424 | -2.61932 | 2.28507 | 3.13111 | 3.40306 | 3.7413 | 4.32744 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.64796 | 2.38563 | 0.898762 | 0.983695 | 1.06039 | 1.35354 | 3.79313 | 7.92364 | 14.9543 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.18875 | 2.22778 | 0.899319 | 0.963427 | 1.02983 | 1.17873 | 1.91001 | 7.66238 | 12.8776 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.22214 | 2.22622 | 0.860568 | 0.971226 | 1.03316 | 1.20374 | 1.90373 | 7.20873 | 13.5943 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.236945 | 0.0776369 | 0.0440488 | 0.0856519 | 0.181567 | 0.267706 | 0.29374 | 0.31623 | 0.523544 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.344918 | 0.0695006 | 0.0605191 | 0.202219 | 0.336635 | 0.351986 | 0.366339 | 0.438987 | 0.706427 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.418137 | 0.121573 | 0.134912 | 0.312566 | 0.348969 | 0.369371 | 0.438966 | 0.69341 | 0.895058 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.253606 | 0.0685377 | 0.0312677 | 0.0922879 | 0.234501 | 0.2792 | 0.295926 | 0.314237 | 0.577622 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.350016 | 0.0607989 | 0.073354 | 0.233108 | 0.341292 | 0.351635 | 0.364002 | 0.427885 | 0.693009 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.396378 | 0.103338 | 0.104852 | 0.317727 | 0.349857 | 0.364781 | 0.395971 | 0.664276 | 0.879727 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.250224 | 0.0691186 | 0.0374071 | 0.0903968 | 0.228756 | 0.274983 | 0.296029 | 0.314347 | 0.563598 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.350506 | 0.0606546 | 0.0981963 | 0.233576 | 0.340899 | 0.352018 | 0.365365 | 0.429181 | 0.701597 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.399271 | 0.102745 | 0.130941 | 0.319342 | 0.34974 | 0.367177 | 0.403231 | 0.67278 | 0.864397 |
| tossup_hazard | hazard_r_1 | 1240 | 0.379391 | 0.270136 | 0.028944 | 0.0619347 | 0.132815 | 0.307407 | 0.601803 | 0.85903 | 0.935827 |
| tossup_hazard | hazard_r_2 | 1240 | 0.299219 | 0.215699 | 0.0238533 | 0.0532179 | 0.118856 | 0.233396 | 0.459911 | 0.715815 | 0.853668 |
| tossup_hazard | hazard_r_3 | 1240 | 0.32139 | 0.232055 | 0.0213129 | 0.0472027 | 0.131479 | 0.264129 | 0.473416 | 0.78555 | 0.94149 |
