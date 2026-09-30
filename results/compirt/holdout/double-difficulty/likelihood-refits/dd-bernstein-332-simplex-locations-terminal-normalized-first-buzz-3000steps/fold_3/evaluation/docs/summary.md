# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 286269 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.710472 |
| log_loss | 0.486021 |
| ece | 0.00761757 |
| brier | 0.157115 |
| accuracy | 0.784141 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0140969 |
| probability_std | 0.140645 |
| probability_p10 | 0.584307 |
| probability_p50 | 0.813094 |
| probability_p90 | 0.918295 |
| mean_predictive_variance | 0.153136 |
| integrated_brier_score | 0.101597 |
| joint_tossup_event_log_loss | 6.58321 |
| buzz_position_mae | 0.154889 |
| buzz_position_median_absolute_error | 0.138491 |
| buzz_position_bias | -0.0539685 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.351211 |
| first_buzzer_mean_reciprocal_rank | 0.567336 |
| first_buzzer_log_loss | 1.67206 |
| first_buzzer_events | 9080 |
| first_buzzer_player_replay_accuracy | 0.179075 |
| first_buzzer_team_replay_accuracy | 0.418392 |
| tossup_scorer_player_replay_accuracy | 0.207267 |
| tossup_scorer_team_replay_accuracy | 0.386226 |
| tossup_game_winner_accuracy | 0.671111 |
| tossup_model_official_winner_accuracy | 0.676149 |
| tossup_game_margin_mae | 46.1605 |
| tossup_game_zero_margin_mae | 59.1757 |
| tournament_player_ppg_spearman | 0.545067 |
| tournament_player_ppg_mae | 13.345 |
| tournament_player_ppg_top10_overlap | 0.610345 |
| tournament_player_ppg_top10_random_overlap | 0.291734 |
| tournament_player_ppg_top10_adjusted_overlap | 0.426799 |
| neg_auroc | 0.710472 |
| neg_average_precision | 0.448519 |
| neg_precision | 0.635021 |
| neg_recall | 0.144157 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.171209 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0314012 |
| no_buzz_calibration_error | 0.0162169 |
| no_buzz_brier | 0.0153711 |
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
| tossup_game_winner_accuracy | 0.671111 |
| tossup_game_margin_mae | 46.1605 |
| tossup_game_zero_margin_mae | 59.1757 |
| tossup_game_margin_mae_games | 461 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 450 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.710472 | 0.486021 | 0.00761757 | 0.157115 | 0.784141 | 0.770044 | 0.0140969 | 0.140645 | 0.584307 | 0.813094 | 0.918295 | 0.153136 |
| tossup_correctness | tier | fall | 2817 | 0.702848 | 0.477789 | 0.0130392 | 0.15318 | 0.793042 | 0.781683 | 0.0113596 | 0.139144 | 0.579238 | 0.822813 | 0.922582 | 0.14992 |
| tossup_correctness | tier | nationals | 1542 | 0.725283 | 0.51584 | 0.0357701 | 0.170807 | 0.754215 | 0.73476 | 0.0194553 | 0.143993 | 0.563079 | 0.795875 | 0.911073 | 0.160463 |
| tossup_correctness | tier | regionals | 1934 | 0.717768 | 0.497579 | 0.022122 | 0.162291 | 0.76939 | 0.75698 | 0.0124095 | 0.137103 | 0.587261 | 0.807409 | 0.917125 | 0.155125 |
| tossup_correctness | tier | winter | 2787 | 0.699363 | 0.469822 | 0.0185441 | 0.149924 | 0.801938 | 0.786868 | 0.01507 | 0.142044 | 0.591365 | 0.816618 | 0.919731 | 0.150953 |
| tossup_correctness | category | Current Events | 125 | 0.742629 | 0.533273 | 0.0701688 | 0.180521 | 0.712 | 0.704 | 0.008 | 0.146085 | 0.540715 | 0.787109 | 0.907454 | 0.168141 |
| tossup_correctness | category | Fine Arts | 1072 | 0.726658 | 0.473997 | 0.019369 | 0.152306 | 0.794776 | 0.770522 | 0.0242537 | 0.146685 | 0.566779 | 0.816849 | 0.918325 | 0.152891 |
| tossup_correctness | category | Geography | 185 | 0.778462 | 0.491078 | 0.0558479 | 0.160747 | 0.762162 | 0.702703 | 0.0594595 | 0.205598 | 0.402712 | 0.761937 | 0.895591 | 0.16935 |
| tossup_correctness | category | History | 1443 | 0.727502 | 0.485827 | 0.025348 | 0.158975 | 0.776854 | 0.765073 | 0.011781 | 0.144823 | 0.564196 | 0.805055 | 0.917069 | 0.156877 |
| tossup_correctness | category | Literature | 1411 | 0.658481 | 0.459499 | 0.0285484 | 0.14447 | 0.81219 | 0.81219 | 0 | 0.114904 | 0.6587 | 0.844229 | 0.927264 | 0.137704 |
| tossup_correctness | category | Mythology | 320 | 0.665116 | 0.482442 | 0.0323705 | 0.151683 | 0.803125 | 0.79375 | 0.009375 | 0.113009 | 0.649549 | 0.827714 | 0.928422 | 0.144126 |
| tossup_correctness | category | Other Academic | 64 | 0.643229 | 0.567038 | 0.182584 | 0.19091 | 0.71875 | 0.75 | -0.03125 | 0.113648 | 0.648263 | 0.806525 | 0.900284 | 0.154132 |
| tossup_correctness | category | Philosophy | 312 | 0.658774 | 0.468594 | 0.0391661 | 0.149019 | 0.810897 | 0.801282 | 0.00961538 | 0.112082 | 0.651185 | 0.816336 | 0.916616 | 0.151479 |
| tossup_correctness | category | Popular Culture | 104 | 0.606534 | 0.421524 | 0.031032 | 0.125479 | 0.846154 | 0.846154 | 0 | 0.0713354 | 0.74498 | 0.863575 | 0.918228 | 0.126051 |
| tossup_correctness | category | Religion | 358 | 0.715463 | 0.532928 | 0.0350283 | 0.178752 | 0.73743 | 0.726257 | 0.0111732 | 0.139985 | 0.548023 | 0.77106 | 0.901401 | 0.169313 |
| tossup_correctness | category | Science | 1431 | 0.699299 | 0.493102 | 0.0183252 | 0.15952 | 0.786862 | 0.765199 | 0.0216632 | 0.14421 | 0.572463 | 0.801044 | 0.914707 | 0.157625 |
| tossup_correctness | category | Social Science | 321 | 0.733493 | 0.494041 | 0.0286651 | 0.159935 | 0.775701 | 0.744548 | 0.0311526 | 0.173484 | 0.51001 | 0.796321 | 0.915854 | 0.158912 |
| tossup_correctness | category | Unknown | 1934 | 0.717768 | 0.497579 | 0.022122 | 0.162291 | 0.76939 | 0.75698 | 0.0124095 | 0.137103 | 0.587261 | 0.807409 | 0.917125 | 0.155125 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.746912 | 0.544822 | 0.0859163 | 0.184742 | 0.713542 | 0.697917 | 0.015625 | 0.154969 | 0.484707 | 0.748024 | 0.873467 | 0.178928 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.751967 | 0.498019 | 0.0307657 | 0.163451 | 0.768279 | 0.733408 | 0.0348706 | 0.14553 | 0.557092 | 0.792246 | 0.906646 | 0.163067 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.685761 | 0.513045 | 0.0246879 | 0.167318 | 0.769231 | 0.759276 | 0.00995475 | 0.140135 | 0.588261 | 0.815477 | 0.919349 | 0.151692 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.692969 | 0.472773 | 0.015441 | 0.151409 | 0.799582 | 0.789125 | 0.0104566 | 0.123128 | 0.623039 | 0.828395 | 0.922491 | 0.146575 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.727594 | 0.471065 | 0.0145416 | 0.151252 | 0.789726 | 0.775342 | 0.0143836 | 0.151167 | 0.551768 | 0.806013 | 0.917627 | 0.155956 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1133 | 2.6437 | 0.74178 | 0.627449 | 1.43343 | 2.11802 | 2.64968 | 3.13204 | 3.96259 | 4.59067 |
| player | theta_1 | 1133 | -1.20666 | 0.857084 | -3.50852 | -2.49046 | -1.778 | -1.27448 | -0.706469 | 0.392071 | 2.35185 |
| player | theta_2 | 1133 | -0.967992 | 0.5989 | -3.23357 | -1.96005 | -1.3483 | -0.973624 | -0.573879 | 0.0140755 | 1.07213 |
| player | theta_3 | 1133 | -1.12622 | 0.766899 | -3.30503 | -2.32521 | -1.62797 | -1.18637 | -0.669019 | 0.223219 | 1.53023 |
| player | theta_norm | 1133 | 2.22186 | 0.636418 | 0.302997 | 1.20988 | 1.7901 | 2.20897 | 2.6216 | 3.33925 | 4.44969 |
| tossup | start_difficulty_d1 | 1240 | -1.77492 | 0.550361 | -3.67741 | -2.5226 | -2.14365 | -1.83962 | -1.46957 | -0.783624 | 1.38964 |
| tossup | start_difficulty_d2 | 1240 | -1.76065 | 0.504887 | -3.75537 | -2.54214 | -2.10502 | -1.79734 | -1.42307 | -0.909051 | 0.0312674 |
| tossup | start_difficulty_d3 | 1240 | -1.76277 | 0.512671 | -3.53749 | -2.54564 | -2.10875 | -1.79817 | -1.42232 | -0.868292 | 0.191625 |
| tossup | end_difficulty_d1 | 1240 | -2.76378 | 0.643513 | -5.18154 | -3.64094 | -3.19806 | -2.8352 | -2.40098 | -1.61886 | 0.712103 |
| tossup | end_difficulty_d2 | 1240 | -2.74618 | 0.592738 | -5.11306 | -3.66537 | -3.15653 | -2.77998 | -2.36163 | -1.72799 | -0.730236 |
| tossup | end_difficulty_d3 | 1240 | -2.74652 | 0.598718 | -4.82809 | -3.68415 | -3.15756 | -2.7762 | -2.3524 | -1.71988 | -0.543317 |
| tossup | total_drop_d1 | 1240 | 0.988859 | 0.112532 | 0.594535 | 0.796988 | 0.913966 | 0.994891 | 1.061 | 1.15807 | 1.50413 |
| tossup | total_drop_d2 | 1240 | 0.98553 | 0.104559 | 0.687445 | 0.820101 | 0.912792 | 0.980552 | 1.05671 | 1.15608 | 1.35769 |
| tossup | total_drop_d3 | 1240 | 0.983749 | 0.104289 | 0.598268 | 0.82206 | 0.912123 | 0.985555 | 1.05144 | 1.15351 | 1.32303 |
| tossup | drop_share_1_d1 | 1240 | 0.30412 | 0.015403 | 0.239377 | 0.279465 | 0.294345 | 0.304415 | 0.314531 | 0.32725 | 0.37293 |
| tossup | drop_share_2_d1 | 1240 | 0.347107 | 0.0114392 | 0.310336 | 0.328014 | 0.339589 | 0.347345 | 0.35496 | 0.365007 | 0.384759 |
| tossup | drop_share_3_d1 | 1240 | 0.348773 | 0.0164401 | 0.276506 | 0.322798 | 0.337604 | 0.348641 | 0.359292 | 0.37569 | 0.414901 |
| tossup | drop_share_1_d2 | 1240 | 0.30362 | 0.0141629 | 0.251331 | 0.27943 | 0.294807 | 0.303804 | 0.313155 | 0.326398 | 0.357413 |
| tossup | drop_share_2_d2 | 1240 | 0.346919 | 0.0113843 | 0.307723 | 0.328178 | 0.33936 | 0.346931 | 0.354569 | 0.365372 | 0.39112 |
| tossup | drop_share_3_d2 | 1240 | 0.34946 | 0.0154576 | 0.283714 | 0.324598 | 0.339452 | 0.349749 | 0.359322 | 0.374928 | 0.427219 |
| tossup | drop_share_1_d3 | 1240 | 0.303544 | 0.0149881 | 0.244535 | 0.278139 | 0.294263 | 0.303656 | 0.31378 | 0.326893 | 0.357075 |
| tossup | drop_share_2_d3 | 1240 | 0.347137 | 0.0112528 | 0.309765 | 0.328841 | 0.339923 | 0.346881 | 0.354394 | 0.365895 | 0.388926 |
| tossup | drop_share_3_d3 | 1240 | 0.349319 | 0.0157277 | 0.304135 | 0.324683 | 0.338798 | 0.348983 | 0.358867 | 0.376233 | 0.413953 |
| tossup | r_1 | 1240 | 0.32112 | 0.143253 | 0.0541099 | 0.134413 | 0.212692 | 0.290603 | 0.407174 | 0.602367 | 0.850987 |
| tossup | r_2 | 1240 | 0.335701 | 0.105179 | 0.0713642 | 0.172868 | 0.267113 | 0.33384 | 0.396123 | 0.525232 | 0.815221 |
| tossup | r_3 | 1240 | 0.34318 | 0.121289 | 0.0717194 | 0.164919 | 0.257538 | 0.33265 | 0.41358 | 0.573358 | 0.793192 |
| tossup | r_norm | 1240 | 0.614945 | 0.0410669 | 0.577351 | 0.578978 | 0.58644 | 0.600985 | 0.627755 | 0.700089 | 0.857494 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.4913 | 0.488037 | 2.18183 | 3.77274 | 4.20197 | 4.44231 | 4.74079 | 5.40344 | 6.35098 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.46617 | 0.408196 | 2.27263 | 3.84714 | 4.24222 | 4.45064 | 4.66388 | 5.18465 | 6.57037 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.48032 | 0.439144 | 2.49397 | 3.76672 | 4.23046 | 4.46334 | 4.73013 | 5.23894 | 6.08146 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.79659 | 2.21077 | -8.12744 | -2.70918 | 0.736312 | 2.85675 | 3.29093 | 3.62821 | 4.37823 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.46878 | 1.84757 | -7.79944 | -1.87278 | 2.59484 | 3.15585 | 3.41442 | 3.72571 | 4.12875 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.18308 | 2.01183 | -9.02777 | -2.22181 | 1.97469 | 3.04358 | 3.37698 | 3.75884 | 4.32221 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.69471 | 2.3797 | 0.855298 | 0.988896 | 1.06822 | 1.34271 | 4.05347 | 7.71546 | 12.7869 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 1.99739 | 1.9999 | 0.898364 | 0.96124 | 1.02359 | 1.16805 | 1.63063 | 6.84676 | 13.2398 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.29724 | 2.1368 | 0.877637 | 0.970964 | 1.03559 | 1.25946 | 2.4731 | 7.1486 | 13.602 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.236688 | 0.0792051 | 0.0334483 | 0.0833585 | 0.180211 | 0.269398 | 0.294229 | 0.31626 | 0.509019 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.34424 | 0.0728707 | 0.0605094 | 0.192391 | 0.335955 | 0.351582 | 0.365792 | 0.442857 | 0.698563 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.419072 | 0.126533 | 0.11678 | 0.305836 | 0.3484 | 0.369809 | 0.442831 | 0.70842 | 0.89618 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.256407 | 0.0648171 | 0.0408903 | 0.0957022 | 0.241232 | 0.279832 | 0.295795 | 0.314245 | 0.523231 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.349921 | 0.0542252 | 0.0573319 | 0.254665 | 0.341677 | 0.351443 | 0.363088 | 0.405335 | 0.683714 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.393672 | 0.0948007 | 0.188837 | 0.321387 | 0.34966 | 0.364687 | 0.395268 | 0.639758 | 0.901778 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.2468 | 0.0703293 | 0.0432705 | 0.0933094 | 0.217209 | 0.272096 | 0.294947 | 0.314643 | 0.563037 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.351094 | 0.0593805 | 0.0887526 | 0.242823 | 0.339635 | 0.351873 | 0.36702 | 0.435498 | 0.702244 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.402107 | 0.102429 | 0.0757966 | 0.316108 | 0.349907 | 0.368095 | 0.410297 | 0.658296 | 0.857659 |
| tossup_hazard | hazard_r_1 | 1240 | 0.379336 | 0.277641 | 0.0272106 | 0.062794 | 0.132579 | 0.285024 | 0.606208 | 0.88989 | 0.949759 |
| tossup_hazard | hazard_r_2 | 1240 | 0.277645 | 0.197716 | 0.030386 | 0.0586155 | 0.118605 | 0.21459 | 0.391354 | 0.683427 | 0.847758 |
| tossup_hazard | hazard_r_3 | 1240 | 0.34302 | 0.239457 | 0.0175764 | 0.0440386 | 0.143273 | 0.280826 | 0.535227 | 0.775807 | 0.926749 |
