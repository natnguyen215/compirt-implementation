# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-10000steps/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-10000steps/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 279189 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.710937 |
| log_loss | 0.485657 |
| ece | 0.0089787 |
| brier | 0.156996 |
| accuracy | 0.784471 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0144273 |
| probability_std | 0.147977 |
| probability_p10 | 0.566561 |
| probability_p50 | 0.808526 |
| probability_p90 | 0.919973 |
| mean_predictive_variance | 0.15392 |
| integrated_brier_score | 0.0948729 |
| joint_tossup_event_log_loss | 6.428 |
| buzz_position_mae | 0.141754 |
| buzz_position_median_absolute_error | 0.121967 |
| buzz_position_bias | -0.0208054 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.364427 |
| first_buzzer_mean_reciprocal_rank | 0.577503 |
| first_buzzer_log_loss | 1.63571 |
| first_buzzer_events | 9080 |
| first_buzzer_player_replay_accuracy | 0.223348 |
| first_buzzer_team_replay_accuracy | 0.485242 |
| tossup_scorer_player_replay_accuracy | 0.241106 |
| tossup_scorer_team_replay_accuracy | 0.445553 |
| tossup_game_winner_accuracy | 0.695556 |
| tossup_model_official_winner_accuracy | 0.706783 |
| tossup_game_margin_mae | 46.6377 |
| tossup_game_zero_margin_mae | 59.1757 |
| tournament_player_ppg_spearman | 0.608659 |
| tournament_player_ppg_mae | 12.1543 |
| tournament_player_ppg_top10_overlap | 0.631034 |
| tournament_player_ppg_top10_random_overlap | 0.291734 |
| tournament_player_ppg_top10_adjusted_overlap | 0.458453 |
| neg_auroc | 0.710937 |
| neg_average_precision | 0.448633 |
| neg_precision | 0.619308 |
| neg_recall | 0.162835 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.168905 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0224393 |
| no_buzz_calibration_error | 0.00725495 |
| no_buzz_brier | 0.0143229 |
| full_pmf_max_mass_error | 5.55112e-16 |
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
| tossup_game_winner_accuracy | 0.695556 |
| tossup_game_margin_mae | 46.6377 |
| tossup_game_zero_margin_mae | 59.1757 |
| tossup_game_margin_mae_games | 461 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 450 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.710937 | 0.485657 | 0.0089787 | 0.156996 | 0.784471 | 0.770044 | 0.0144273 | 0.147977 | 0.566561 | 0.808526 | 0.919973 | 0.15392 |
| tossup_correctness | tier | fall | 2817 | 0.7034 | 0.477215 | 0.0172695 | 0.152931 | 0.794107 | 0.781683 | 0.0124246 | 0.14216 | 0.569945 | 0.817609 | 0.922156 | 0.151769 |
| tossup_correctness | tier | nationals | 1542 | 0.727061 | 0.5136 | 0.0319207 | 0.169876 | 0.756161 | 0.73476 | 0.0214008 | 0.156412 | 0.540062 | 0.79312 | 0.91688 | 0.159242 |
| tossup_correctness | tier | regionals | 1934 | 0.717308 | 0.496927 | 0.0218232 | 0.161923 | 0.768356 | 0.75698 | 0.0113754 | 0.147183 | 0.565604 | 0.804701 | 0.918705 | 0.155008 |
| tossup_correctness | tier | winter | 2787 | 0.700192 | 0.470909 | 0.0231808 | 0.150561 | 0.801579 | 0.786868 | 0.0147112 | 0.148885 | 0.581322 | 0.809881 | 0.920459 | 0.152394 |
| tossup_correctness | category | Current Events | 125 | 0.762592 | 0.523422 | 0.064233 | 0.177115 | 0.728 | 0.704 | 0.024 | 0.14515 | 0.530856 | 0.767731 | 0.905677 | 0.170503 |
| tossup_correctness | category | Fine Arts | 1072 | 0.728597 | 0.473509 | 0.0205947 | 0.152253 | 0.79291 | 0.770522 | 0.0223881 | 0.152201 | 0.563632 | 0.815509 | 0.921576 | 0.153984 |
| tossup_correctness | category | Geography | 185 | 0.787692 | 0.485741 | 0.0462772 | 0.158397 | 0.772973 | 0.702703 | 0.0702703 | 0.211124 | 0.396668 | 0.756616 | 0.906311 | 0.168791 |
| tossup_correctness | category | History | 1443 | 0.725413 | 0.487472 | 0.026132 | 0.159799 | 0.773389 | 0.765073 | 0.00831601 | 0.153939 | 0.53027 | 0.797307 | 0.914079 | 0.158697 |
| tossup_correctness | category | Literature | 1411 | 0.662521 | 0.459461 | 0.0255694 | 0.144601 | 0.812899 | 0.81219 | 0.000708717 | 0.122527 | 0.650484 | 0.841515 | 0.929617 | 0.139002 |
| tossup_correctness | category | Mythology | 320 | 0.661298 | 0.482937 | 0.0493256 | 0.152132 | 0.803125 | 0.79375 | 0.009375 | 0.118223 | 0.631537 | 0.825178 | 0.927654 | 0.145822 |
| tossup_correctness | category | Other Academic | 64 | 0.654948 | 0.555226 | 0.128758 | 0.18697 | 0.71875 | 0.75 | -0.03125 | 0.113473 | 0.63841 | 0.802731 | 0.904474 | 0.153213 |
| tossup_correctness | category | Philosophy | 312 | 0.660129 | 0.466875 | 0.0406996 | 0.148134 | 0.814103 | 0.801282 | 0.0128205 | 0.113527 | 0.635844 | 0.810602 | 0.917444 | 0.152969 |
| tossup_correctness | category | Popular Culture | 104 | 0.634233 | 0.413949 | 0.0453902 | 0.123861 | 0.846154 | 0.846154 | 0 | 0.0712552 | 0.738076 | 0.860379 | 0.919977 | 0.127293 |
| tossup_correctness | category | Religion | 358 | 0.700432 | 0.540525 | 0.0403296 | 0.180904 | 0.73743 | 0.726257 | 0.0111732 | 0.146966 | 0.556285 | 0.765496 | 0.892395 | 0.171817 |
| tossup_correctness | category | Science | 1431 | 0.702014 | 0.490493 | 0.0261239 | 0.158527 | 0.790356 | 0.765199 | 0.0251572 | 0.15041 | 0.555617 | 0.80165 | 0.917804 | 0.157158 |
| tossup_correctness | category | Social Science | 321 | 0.727472 | 0.498144 | 0.0330257 | 0.161136 | 0.778816 | 0.744548 | 0.0342679 | 0.181816 | 0.487285 | 0.785897 | 0.921382 | 0.159586 |
| tossup_correctness | category | Unknown | 1934 | 0.717308 | 0.496927 | 0.0218232 | 0.161923 | 0.768356 | 0.75698 | 0.0113754 | 0.147183 | 0.565604 | 0.804701 | 0.918705 | 0.155008 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.738291 | 0.544536 | 0.0443267 | 0.184605 | 0.713542 | 0.697917 | 0.015625 | 0.167612 | 0.479269 | 0.738362 | 0.879084 | 0.178839 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.751171 | 0.497466 | 0.0228658 | 0.16322 | 0.773903 | 0.733408 | 0.0404949 | 0.152205 | 0.542065 | 0.789251 | 0.911127 | 0.162248 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.685172 | 0.515121 | 0.0265316 | 0.167982 | 0.767421 | 0.759276 | 0.0081448 | 0.145989 | 0.573794 | 0.812687 | 0.921251 | 0.15243 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.698529 | 0.468734 | 0.0186004 | 0.14991 | 0.802022 | 0.789125 | 0.0128965 | 0.131832 | 0.608623 | 0.822591 | 0.922802 | 0.14791 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.725232 | 0.472519 | 0.0158089 | 0.151935 | 0.788014 | 0.775342 | 0.0126712 | 0.158502 | 0.538312 | 0.801824 | 0.919564 | 0.156778 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 1.27493 | 0.803572 | -0.859605 | -0.040366 | 0.718487 | 1.26543 | 1.78781 | 2.68493 | 3.44871 |
| player | theta_1 | 1133 | -0.542674 | 0.939075 | -3.08824 | -1.86651 | -1.16187 | -0.663025 | -0.0479699 | 1.2708 | 4.1531 |
| player | theta_2 | 1133 | -0.486905 | 0.788402 | -2.73564 | -1.78847 | -0.978526 | -0.544704 | 0.00252607 | 0.871204 | 2.50037 |
| player | theta_3 | 1133 | -0.580638 | 0.873594 | -2.96295 | -1.88055 | -1.16872 | -0.704111 | -0.0404706 | 1.02296 | 2.45625 |
| player | theta_norm | 1133 | 1.64944 | 0.642675 | 0.242863 | 0.675982 | 1.20607 | 1.59414 | 2.04878 | 2.7977 | 4.74329 |
| tossup | start_difficulty_d1 | 1240 | -1.11682 | 0.541217 | -3.00333 | -1.87289 | -1.47615 | -1.16045 | -0.831112 | -0.175641 | 2.04208 |
| tossup | start_difficulty_d2 | 1240 | -1.13021 | 0.488734 | -3.06322 | -1.90074 | -1.44182 | -1.15787 | -0.833365 | -0.328883 | 1.43851 |
| tossup | start_difficulty_d3 | 1240 | -1.12329 | 0.500896 | -2.92001 | -1.87481 | -1.4407 | -1.14751 | -0.802275 | -0.278227 | 0.874197 |
| tossup | end_difficulty_d1 | 1240 | -2.1126 | 0.632195 | -4.43888 | -3.02361 | -2.53207 | -2.16004 | -1.75606 | -1.03886 | 1.34108 |
| tossup | end_difficulty_d2 | 1240 | -2.12595 | 0.576203 | -4.37536 | -3.05153 | -2.49761 | -2.15381 | -1.7682 | -1.15677 | 0.825586 |
| tossup | end_difficulty_d3 | 1240 | -2.11826 | 0.58643 | -4.23158 | -3.00805 | -2.50325 | -2.14033 | -1.73446 | -1.1336 | 0.119801 |
| tossup | total_drop_d1 | 1240 | 0.995781 | 0.11139 | 0.600089 | 0.814882 | 0.926142 | 0.994653 | 1.06607 | 1.17034 | 1.51423 |
| tossup | total_drop_d2 | 1240 | 0.995741 | 0.104069 | 0.61292 | 0.821063 | 0.930197 | 0.994475 | 1.06148 | 1.1663 | 1.45031 |
| tossup | total_drop_d3 | 1240 | 0.994967 | 0.107827 | 0.630284 | 0.826082 | 0.92521 | 0.991565 | 1.06357 | 1.16171 | 1.78467 |
| tossup | drop_share_1_d1 | 1240 | 0.304264 | 0.0154063 | 0.232969 | 0.27916 | 0.29528 | 0.304942 | 0.313647 | 0.327925 | 0.368102 |
| tossup | drop_share_2_d1 | 1240 | 0.34668 | 0.011546 | 0.312622 | 0.328381 | 0.338737 | 0.346699 | 0.354452 | 0.366064 | 0.384663 |
| tossup | drop_share_3_d1 | 1240 | 0.349056 | 0.01625 | 0.299279 | 0.324939 | 0.338705 | 0.347829 | 0.359035 | 0.375753 | 0.444523 |
| tossup | drop_share_1_d2 | 1240 | 0.30507 | 0.0147281 | 0.249699 | 0.279794 | 0.295486 | 0.305193 | 0.31483 | 0.328302 | 0.375324 |
| tossup | drop_share_2_d2 | 1240 | 0.34718 | 0.0114458 | 0.314712 | 0.3288 | 0.339074 | 0.346949 | 0.355298 | 0.366625 | 0.381001 |
| tossup | drop_share_3_d2 | 1240 | 0.347751 | 0.0152467 | 0.294339 | 0.324065 | 0.338008 | 0.347039 | 0.356777 | 0.374526 | 0.400997 |
| tossup | drop_share_1_d3 | 1240 | 0.304358 | 0.0147275 | 0.225607 | 0.279582 | 0.295173 | 0.305072 | 0.313959 | 0.329001 | 0.358533 |
| tossup | drop_share_2_d3 | 1240 | 0.347074 | 0.0116542 | 0.312244 | 0.327491 | 0.339577 | 0.347119 | 0.354737 | 0.365502 | 0.419683 |
| tossup | drop_share_3_d3 | 1240 | 0.348568 | 0.0153575 | 0.30179 | 0.324697 | 0.338792 | 0.347918 | 0.358165 | 0.374685 | 0.421993 |
| tossup | r_1 | 1240 | 0.319193 | 0.161334 | 0.0425286 | 0.11294 | 0.195059 | 0.286686 | 0.419757 | 0.634489 | 0.866623 |
| tossup | r_2 | 1240 | 0.339265 | 0.156068 | 0.065472 | 0.122598 | 0.223035 | 0.311979 | 0.435522 | 0.640781 | 0.868855 |
| tossup | r_3 | 1240 | 0.341543 | 0.159914 | 0.0585097 | 0.12975 | 0.220952 | 0.308246 | 0.434642 | 0.655904 | 0.838111 |
| tossup | r_norm | 1240 | 0.637418 | 0.05687 | 0.577361 | 0.580819 | 0.595396 | 0.618295 | 0.660644 | 0.761965 | 0.87382 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 7.4338 | 0.522239 | 4.42488 | 6.50333 | 7.25357 | 7.43482 | 7.64177 | 8.34773 | 9.24908 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 7.51973 | 0.477682 | 4.72776 | 6.81409 | 7.35281 | 7.47302 | 7.67364 | 8.35042 | 9.9995 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 7.4744 | 0.513484 | 4.59366 | 6.53718 | 7.3072 | 7.4699 | 7.66664 | 8.38395 | 9.59376 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 4.02194 | 3.39012 | -9.67074 | -2.63595 | 1.65446 | 6.19649 | 6.43784 | 6.71466 | 7.34505 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 4.83088 | 3.14569 | -11.9326 | -2.44205 | 4.54253 | 6.3699 | 6.51727 | 6.86276 | 7.73835 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 4.47237 | 3.1234 | -9.05795 | -1.82463 | 2.27407 | 6.31271 | 6.51245 | 6.84031 | 7.9089 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.41186 | 3.45934 | 0.874936 | 0.955726 | 1.00935 | 1.06945 | 5.95809 | 10.5002 | 17.3257 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.68885 | 3.24852 | 0.884153 | 0.942652 | 0.990068 | 1.03354 | 2.62572 | 10.2202 | 19.3556 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 3.00203 | 3.16897 | 0.837879 | 0.936594 | 0.990223 | 1.04228 | 5.32325 | 9.51244 | 16.6663 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.264093 | 0.0921974 | 0.0429963 | 0.0978528 | 0.214902 | 0.29365 | 0.306508 | 0.356993 | 0.690925 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.332453 | 0.0815037 | 0.0627834 | 0.166472 | 0.326927 | 0.345183 | 0.357631 | 0.454302 | 0.727164 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.403454 | 0.135129 | 0.0895407 | 0.2443 | 0.341926 | 0.355694 | 0.413884 | 0.723596 | 0.886874 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.26875 | 0.0773684 | 0.0396502 | 0.0994285 | 0.270729 | 0.295386 | 0.306346 | 0.322478 | 0.725494 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.337835 | 0.0688134 | 0.0638511 | 0.187069 | 0.335794 | 0.346687 | 0.356944 | 0.417881 | 0.72267 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.393415 | 0.117902 | 0.147014 | 0.303092 | 0.34306 | 0.355432 | 0.376695 | 0.692146 | 0.892152 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.267428 | 0.0827871 | 0.0398563 | 0.0967072 | 0.252556 | 0.294311 | 0.306294 | 0.329854 | 0.704636 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.336731 | 0.0749911 | 0.0743111 | 0.182818 | 0.331895 | 0.346795 | 0.357914 | 0.45231 | 0.690275 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.395841 | 0.125054 | 0.0670008 | 0.267643 | 0.342157 | 0.355829 | 0.382506 | 0.712105 | 0.885833 |
| tossup_hazard | hazard_r_1 | 1240 | 0.362009 | 0.303166 | 0.0184174 | 0.0409859 | 0.09286 | 0.22521 | 0.622328 | 0.906936 | 0.961413 |
| tossup_hazard | hazard_r_2 | 1240 | 0.292565 | 0.267071 | 0.0204712 | 0.0348961 | 0.0749592 | 0.169288 | 0.476879 | 0.853851 | 0.938886 |
| tossup_hazard | hazard_r_3 | 1240 | 0.345427 | 0.296714 | 0.0153927 | 0.0369556 | 0.0808076 | 0.222303 | 0.618072 | 0.869828 | 0.960027 |
