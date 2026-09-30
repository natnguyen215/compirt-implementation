# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/likelihood-refits/multidim-5d-normalized-first-buzz-3000steps-5fold/fold_3/holdout/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/likelihood-refits/multidim-5d-normalized-first-buzz-3000steps-5fold/fold_3`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 300515 |
| pyramidal | calibrate_correctness | False |
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.157291 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.889469 |
| log_loss | 0.420593 |
| ece | 0.0233037 |
| brier | 0.134192 |
| part_accuracy | 0.808437 |
| part_all_correct_accuracy | 0.525685 |
| accuracy_lift_over_all_correct | 0.282752 |
| part_accuracy_macro_team | 0.811544 |
| part_accuracy_macro_bonus | 0.80738 |
| probability_std | 0.327829 |
| probability_p10 | 0.0856896 |
| probability_p50 | 0.475409 |
| probability_p90 | 0.933695 |
| mean_predictive_variance | 0.142517 |
| exact_acc | 0.509639 |
| ranked_probability_score | 0.117635 |
| bonus_total_score_log_loss | 1.02287 |
| ppb_mae | 2.34471 |
| ranked_probability_score_responses | 8455 |
| bonus_total_score_log_loss_responses | 8455 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.638571 |
| log_loss | 0.76454 |
| ece | 0.20997 |
| brier | 0.247901 |
| accuracy | 0.642511 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.127533 |
| probability_std | 0.289422 |
| probability_p10 | 0.121959 |
| probability_p50 | 0.637374 |
| probability_p90 | 0.921279 |
| mean_predictive_variance | 0.16031 |
| integrated_brier_score | 0.0943159 |
| joint_tossup_event_log_loss | 6.71727 |
| buzz_position_mae | 0.145291 |
| buzz_position_median_absolute_error | 0.125107 |
| buzz_position_bias | -0.0472669 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.395925 |
| first_buzzer_mean_reciprocal_rank | 0.602303 |
| first_buzzer_log_loss | 1.59041 |
| first_buzzer_events | 9080 |
| first_buzzer_player_replay_accuracy | 0.0139868 |
| first_buzzer_team_replay_accuracy | 0.0161894 |
| tossup_scorer_player_replay_accuracy | 0.0940347 |
| tossup_scorer_team_replay_accuracy | 0.0957701 |
| tossup_game_winner_accuracy | 0.186667 |
| tossup_model_official_winner_accuracy | 0.188184 |
| tossup_game_margin_mae | 57.6356 |
| tossup_game_zero_margin_mae | 59.1757 |
| tournament_player_ppg_spearman | 0.254011 |
| tournament_player_ppg_mae | 23.1984 |
| tournament_player_ppg_top10_overlap | 0.358621 |
| tournament_player_ppg_top10_random_overlap | 0.291734 |
| tournament_player_ppg_top10_adjusted_overlap | 0.0668237 |
| neg_auroc | 0.638571 |
| neg_average_precision | 0.33887 |
| neg_precision | 0.326854 |
| neg_recall | 0.523467 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0873719 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0591148 |
| no_buzz_calibration_error | 0.0439305 |
| no_buzz_brier | 0.0207693 |
| full_pmf_max_mass_error | 6.66134e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9220 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 457 |
| first_buzzer_player_replay_accuracy_events | 9080 |
| first_buzzer_team_replay_accuracy_events | 9080 |
| tossup_scorer_player_replay_accuracy_events | 9220 |
| tossup_scorer_team_replay_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 450 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.186667 |
| tossup_game_margin_mae | 57.6356 |
| tossup_game_zero_margin_mae | 59.1757 |
| tossup_game_margin_mae_games | 461 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 450 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.638571 | 0.76454 | 0.20997 | 0.247901 | 0.642511 | 0.770044 | -0.127533 | 0.289422 | 0.121959 | 0.637374 | 0.921279 | 0.16031 |
| tossup_correctness | tier | fall | 2817 | 0.640309 | 0.747904 | 0.21516 | 0.243844 | 0.648562 | 0.781683 | -0.13312 | 0.286902 | 0.126773 | 0.640389 | 0.918762 | 0.161247 |
| tossup_correctness | tier | nationals | 1542 | 0.624724 | 0.73607 | 0.181558 | 0.248716 | 0.629702 | 0.73476 | -0.105058 | 0.279667 | 0.155327 | 0.652691 | 0.921409 | 0.163692 |
| tossup_correctness | tier | regionals | 1934 | 0.64511 | 0.776827 | 0.20172 | 0.246752 | 0.649948 | 0.75698 | -0.107032 | 0.292966 | 0.12185 | 0.629918 | 0.92719 | 0.158342 |
| tossup_correctness | tier | winter | 2787 | 0.643908 | 0.788581 | 0.231346 | 0.252348 | 0.638321 | 0.786868 | -0.148547 | 0.294391 | 0.0987813 | 0.628819 | 0.916437 | 0.158859 |
| tossup_correctness | category | Current Events | 125 | 0.59613 | 0.813449 | 0.213449 | 0.27389 | 0.592 | 0.704 | -0.112 | 0.278451 | 0.0973849 | 0.605111 | 0.868953 | 0.170639 |
| tossup_correctness | category | Fine Arts | 1072 | 0.604599 | 0.804234 | 0.223117 | 0.265162 | 0.610075 | 0.770522 | -0.160448 | 0.290763 | 0.120333 | 0.629756 | 0.922102 | 0.160626 |
| tossup_correctness | category | Geography | 185 | 0.618462 | 0.826723 | 0.202921 | 0.275468 | 0.621622 | 0.702703 | -0.0810811 | 0.271204 | 0.106391 | 0.534933 | 0.85849 | 0.176313 |
| tossup_correctness | category | History | 1443 | 0.658707 | 0.744486 | 0.199053 | 0.240551 | 0.657658 | 0.765073 | -0.107415 | 0.288844 | 0.115394 | 0.639548 | 0.9095 | 0.16081 |
| tossup_correctness | category | Literature | 1411 | 0.632997 | 0.734497 | 0.213337 | 0.23671 | 0.665485 | 0.81219 | -0.146704 | 0.286988 | 0.141734 | 0.675268 | 0.930156 | 0.156151 |
| tossup_correctness | category | Mythology | 320 | 0.620795 | 0.80851 | 0.289443 | 0.275627 | 0.584375 | 0.79375 | -0.209375 | 0.277566 | 0.123969 | 0.562503 | 0.88096 | 0.172524 |
| tossup_correctness | category | Other Academic | 64 | 0.557292 | 0.70707 | 0.264418 | 0.250584 | 0.609375 | 0.75 | -0.140625 | 0.233188 | 0.190519 | 0.592285 | 0.829718 | 0.192512 |
| tossup_correctness | category | Philosophy | 312 | 0.656323 | 0.729301 | 0.240093 | 0.245438 | 0.637821 | 0.801282 | -0.163462 | 0.285803 | 0.132073 | 0.645716 | 0.908662 | 0.163869 |
| tossup_correctness | category | Popular Culture | 104 | 0.587358 | 0.888945 | 0.346393 | 0.296597 | 0.528846 | 0.846154 | -0.317308 | 0.25616 | 0.159802 | 0.517103 | 0.847347 | 0.184382 |
| tossup_correctness | category | Religion | 358 | 0.665699 | 0.762569 | 0.212421 | 0.25397 | 0.614525 | 0.726257 | -0.111732 | 0.296605 | 0.084742 | 0.579962 | 0.89537 | 0.161006 |
| tossup_correctness | category | Science | 1431 | 0.637065 | 0.758828 | 0.194968 | 0.240308 | 0.653389 | 0.765199 | -0.11181 | 0.290926 | 0.133198 | 0.678426 | 0.933932 | 0.155258 |
| tossup_correctness | category | Social Science | 321 | 0.661445 | 0.714513 | 0.192313 | 0.238927 | 0.657321 | 0.744548 | -0.0872274 | 0.281784 | 0.12573 | 0.61651 | 0.910772 | 0.1658 |
| tossup_correctness | category | Unknown | 1934 | 0.64511 | 0.776827 | 0.20172 | 0.246752 | 0.649948 | 0.75698 | -0.107032 | 0.292966 | 0.12185 | 0.629918 | 0.92719 | 0.158342 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.728127 | 1.20971 | 0.441191 | 0.381644 | 0.479167 | 0.697917 | -0.21875 | 0.236688 | 0.0200533 | 0.18383 | 0.60537 | 0.140965 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.693239 | 1.02267 | 0.360382 | 0.333894 | 0.519685 | 0.733408 | -0.213723 | 0.278802 | 0.0349905 | 0.324988 | 0.797961 | 0.156256 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.657135 | 0.828416 | 0.257883 | 0.270917 | 0.606335 | 0.759276 | -0.152941 | 0.286103 | 0.0847734 | 0.532595 | 0.883958 | 0.168106 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.637416 | 0.693115 | 0.178947 | 0.225048 | 0.668874 | 0.789125 | -0.120251 | 0.26872 | 0.201844 | 0.682316 | 0.928983 | 0.163352 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.615728 | 0.678514 | 0.149179 | 0.21796 | 0.692123 | 0.775342 | -0.0832192 | 0.259049 | 0.248594 | 0.746429 | 0.942425 | 0.153928 |
| bonus_part_correctness | aggregate | all | 25365 | 0.889469 | 0.420593 | 0.0233037 | 0.134192 | 0.808437 | 0.525685 | 0.282752 | 0.327829 | 0.0856896 | 0.475409 | 0.933695 | 0.142517 |
| bonus_part_correctness | tier | fall | 8094 | 0.885934 | 0.419781 | 0.0254303 | 0.134587 | 0.803929 | 0.595132 | 0.208797 | 0.318283 | 0.118253 | 0.606098 | 0.940564 | 0.143721 |
| bonus_part_correctness | tier | nationals | 4125 | 0.873895 | 0.446031 | 0.0333558 | 0.14324 | 0.794182 | 0.448485 | 0.345697 | 0.313615 | 0.0732931 | 0.331891 | 0.887499 | 0.145018 |
| bonus_part_correctness | tier | regionals | 5247 | 0.891 | 0.415072 | 0.0234554 | 0.131198 | 0.819706 | 0.481609 | 0.338098 | 0.324613 | 0.082751 | 0.418933 | 0.92417 | 0.143958 |
| bonus_part_correctness | tier | winter | 7899 | 0.894773 | 0.411809 | 0.028889 | 0.131051 | 0.813014 | 0.524117 | 0.288897 | 0.333132 | 0.0787806 | 0.453615 | 0.941914 | 0.13902 |
| bonus_part_correctness | category | Current Events | 243 | 0.898645 | 0.406498 | 0.0642096 | 0.126146 | 0.843621 | 0.506173 | 0.337449 | 0.33232 | 0.0708902 | 0.454605 | 0.906343 | 0.13864 |
| bonus_part_correctness | category | Fine Arts | 2937 | 0.873933 | 0.445855 | 0.0242577 | 0.14357 | 0.798774 | 0.508682 | 0.290092 | 0.320729 | 0.0832805 | 0.453508 | 0.927367 | 0.146929 |
| bonus_part_correctness | category | Geography | 456 | 0.884028 | 0.427869 | 0.0672414 | 0.137848 | 0.798246 | 0.622807 | 0.175439 | 0.320889 | 0.0976216 | 0.650882 | 0.929374 | 0.143172 |
| bonus_part_correctness | category | History | 4050 | 0.891061 | 0.418326 | 0.0336292 | 0.134155 | 0.803704 | 0.565185 | 0.238519 | 0.32824 | 0.0855368 | 0.546729 | 0.935642 | 0.1412 |
| bonus_part_correctness | category | Literature | 4029 | 0.894912 | 0.412569 | 0.0358407 | 0.131045 | 0.809878 | 0.536113 | 0.273765 | 0.330324 | 0.0900955 | 0.457087 | 0.938322 | 0.140884 |
| bonus_part_correctness | category | Mythology | 936 | 0.874254 | 0.432737 | 0.0380172 | 0.139329 | 0.792735 | 0.619658 | 0.173077 | 0.293011 | 0.170782 | 0.64527 | 0.940976 | 0.154227 |
| bonus_part_correctness | category | Other Academic | 255 | 0.914785 | 0.373473 | 0.0562281 | 0.115251 | 0.831373 | 0.545098 | 0.286275 | 0.350569 | 0.0662503 | 0.539988 | 0.946489 | 0.12683 |
| bonus_part_correctness | category | Philosophy | 948 | 0.860438 | 0.464143 | 0.0465171 | 0.152578 | 0.771097 | 0.504219 | 0.266878 | 0.321545 | 0.088507 | 0.407936 | 0.92198 | 0.145857 |
| bonus_part_correctness | category | Popular Culture | 285 | 0.886162 | 0.417073 | 0.0316669 | 0.132904 | 0.803509 | 0.578947 | 0.224561 | 0.305835 | 0.127865 | 0.600163 | 0.944919 | 0.14866 |
| bonus_part_correctness | category | Religion | 1014 | 0.896177 | 0.408582 | 0.0329647 | 0.129506 | 0.816568 | 0.50789 | 0.308679 | 0.335315 | 0.0692843 | 0.440729 | 0.93369 | 0.137479 |
| bonus_part_correctness | category | Science | 4059 | 0.890092 | 0.418902 | 0.0258808 | 0.133515 | 0.808574 | 0.530426 | 0.278147 | 0.328551 | 0.092048 | 0.485592 | 0.937582 | 0.141859 |
| bonus_part_correctness | category | Social Science | 906 | 0.903839 | 0.39389 | 0.0536127 | 0.125073 | 0.825607 | 0.471302 | 0.354305 | 0.344844 | 0.0657744 | 0.335749 | 0.935456 | 0.129211 |
| bonus_part_correctness | category | Unknown | 5247 | 0.891 | 0.415072 | 0.0234554 | 0.131198 | 0.819706 | 0.481609 | 0.338098 | 0.324613 | 0.082751 | 0.418933 | 0.92417 | 0.143958 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.889469 | 0.897739 | 0.00827021 | synergy |
| log_loss | 0.420593 | 0.406895 | -0.0136987 | synergy |
| ece | 0.0233037 | 0.0283473 | 0.00504365 | no-synergy |
| brier | 0.134192 | 0.12952 | -0.00467201 | synergy |
| accuracy_lift_over_all_correct | 0.282752 | 0.29044 | 0.00768776 | synergy |
| part_accuracy | 0.808437 | 0.816125 | 0.00768776 | synergy |
| part_accuracy_macro_team | 0.811544 | 0.815394 | 0.00385027 | synergy |
| part_accuracy_macro_bonus | 0.80738 | 0.815415 | 0.00803504 | synergy |
| exact_acc | 0.509639 | 0.526198 | 0.0165582 | synergy |
| ranked_probability_score | 0.117635 | 0.112225 | -0.00540967 | synergy |
| bonus_total_score_log_loss | 1.02287 | 0.988558 | -0.0343075 | synergy |
| ppb_mae | 2.34471 | 1.80908 | -0.535628 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 4.61237 | 1.16461 | 0.881338 | 2.10078 | 4.0507 | 4.83076 | 5.41034 | 6.15107 | 7.124 |
| player | theta_1 | 1133 | 0.0298149 | 0.744197 | -2.16285 | -1.41333 | -0.410117 | 0.159181 | 0.573718 | 1.03743 | 1.76642 |
| player | theta_2 | 1133 | -0.0259096 | 0.733165 | -2.42869 | -1.44533 | -0.420832 | 0.0893938 | 0.472285 | 1.07719 | 1.93569 |
| player | theta_3 | 1133 | 0.0912672 | 0.73994 | -2.4433 | -1.36744 | -0.331044 | 0.218059 | 0.592863 | 1.14965 | 2.09906 |
| player | theta_4 | 1133 | 0.0772214 | 0.750378 | -2.54205 | -1.35542 | -0.371589 | 0.204242 | 0.591134 | 1.20775 | 2.21145 |
| player | theta_5 | 1133 | 0.0163015 | 0.746553 | -2.59943 | -1.38853 | -0.428987 | 0.164409 | 0.549368 | 1.03849 | 1.67188 |
| player | theta_norm | 1133 | 1.55325 | 0.600581 | 0.212655 | 0.732375 | 1.09996 | 1.45675 | 1.90566 | 2.70533 | 3.64987 |
| tossup | beta_1 | 1240 | 0.736248 | 0.494575 | -1.22711 | 0.227885 | 0.397431 | 0.577706 | 0.927979 | 1.78149 | 2.70899 |
| tossup | beta_2 | 1240 | 0.833604 | 0.585202 | -1.4188 | 0.211615 | 0.410732 | 0.623408 | 1.21842 | 2.01567 | 2.66837 |
| tossup | beta_3 | 1240 | 0.736676 | 0.49254 | -0.392801 | 0.242466 | 0.417174 | 0.581025 | 0.868607 | 1.8405 | 2.91325 |
| tossup | beta_4 | 1240 | 0.753688 | 0.525649 | -0.213562 | 0.216742 | 0.407692 | 0.574205 | 0.911021 | 1.90682 | 3.80697 |
| tossup | beta_5 | 1240 | 0.827043 | 0.57976 | -0.614875 | 0.212602 | 0.401731 | 0.620562 | 1.17073 | 2.00911 | 2.75299 |
| tossup | gamma_1 | 1240 | 13.1965 | 75.676 | 0.456852 | 3.1792 | 4.47489 | 5.14037 | 6.09909 | 22.497 | 1901.01 |
| tossup | gamma_2 | 1240 | 13.672 | 73.9727 | 0.437857 | 3.30956 | 4.52412 | 5.15031 | 6.34364 | 21.2987 | 1445.49 |
| tossup | gamma_3 | 1240 | 10.7635 | 50.4252 | 1.12651 | 3.0917 | 4.44286 | 5.07193 | 5.87843 | 24.883 | 1185.44 |
| tossup | gamma_4 | 1240 | 11.4572 | 70.7792 | 1.39261 | 3.55882 | 4.53077 | 5.13651 | 5.94703 | 16.4058 | 1944.78 |
| tossup | gamma_5 | 1240 | 13.3987 | 68.8755 | 0.897572 | 3.34084 | 4.53167 | 5.20775 | 6.5326 | 23.3866 | 1447.36 |
| tossup | mu_1 | 1240 | 0.499558 | 0.100621 | 0.191286 | 0.386673 | 0.447937 | 0.478217 | 0.524624 | 0.712215 | 0.969388 |
| tossup | mu_2 | 1240 | 0.516452 | 0.120673 | 0.244032 | 0.385531 | 0.444375 | 0.47771 | 0.552018 | 0.785049 | 0.984188 |
| tossup | mu_3 | 1240 | 0.503769 | 0.100075 | 0.196329 | 0.394433 | 0.450604 | 0.480207 | 0.52653 | 0.712403 | 0.962411 |
| tossup | mu_4 | 1240 | 0.502321 | 0.105231 | 0.211664 | 0.395112 | 0.447159 | 0.478603 | 0.514783 | 0.733289 | 0.985533 |
| tossup | mu_5 | 1240 | 0.512132 | 0.112904 | 0.172599 | 0.379794 | 0.447486 | 0.483328 | 0.546647 | 0.756373 | 0.983641 |
| tossup | r_1 | 1240 | 0.972942 | 0.700025 | 0.0981602 | 0.207266 | 0.427539 | 0.778204 | 1.3705 | 2.41755 | 4.24232 |
| tossup | r_2 | 1240 | 1.26155 | 1.03052 | 0.0744496 | 0.22297 | 0.485585 | 0.901797 | 1.71448 | 3.45206 | 6.10269 |
| tossup | r_3 | 1240 | 1.01149 | 0.84341 | 0.0695015 | 0.205468 | 0.415654 | 0.735997 | 1.31808 | 2.80545 | 5.59022 |
| tossup | r_4 | 1240 | 1.04434 | 0.920999 | 0.077982 | 0.225432 | 0.419356 | 0.730299 | 1.24825 | 3.11252 | 5.40591 |
| tossup | r_5 | 1240 | 1.14453 | 0.816294 | 0.0783887 | 0.215353 | 0.496546 | 0.893191 | 1.6459 | 2.72933 | 4.39685 |
| tossup | r_norm | 1240 | 3.02339 | 0.772215 | 1.34303 | 1.9331 | 2.45072 | 2.94276 | 3.49484 | 4.43023 | 6.33984 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
