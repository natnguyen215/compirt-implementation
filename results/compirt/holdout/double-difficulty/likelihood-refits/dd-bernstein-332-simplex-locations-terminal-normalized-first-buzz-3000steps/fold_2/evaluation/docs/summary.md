# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 284830 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.714647 |
| log_loss | 0.491587 |
| ece | 0.0126121 |
| brier | 0.15997 |
| accuracy | 0.774225 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0100465 |
| probability_std | 0.139642 |
| probability_p10 | 0.583622 |
| probability_p50 | 0.810937 |
| probability_p90 | 0.917207 |
| mean_predictive_variance | 0.154779 |
| integrated_brier_score | 0.102866 |
| joint_tossup_event_log_loss | 6.62213 |
| buzz_position_mae | 0.155044 |
| buzz_position_median_absolute_error | 0.136308 |
| buzz_position_bias | -0.0483728 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.353138 |
| first_buzzer_mean_reciprocal_rank | 0.566676 |
| first_buzzer_log_loss | 1.66501 |
| first_buzzer_events | 9257 |
| first_buzzer_player_replay_accuracy | 0.17612 |
| first_buzzer_team_replay_accuracy | 0.408855 |
| tossup_scorer_player_replay_accuracy | 0.201709 |
| tossup_scorer_team_replay_accuracy | 0.382692 |
| tossup_game_winner_accuracy | 0.646154 |
| tossup_model_official_winner_accuracy | 0.660173 |
| tossup_game_margin_mae | 50.3846 |
| tossup_game_zero_margin_mae | 58.4615 |
| tournament_player_ppg_spearman | 0.569195 |
| tournament_player_ppg_mae | 12.7879 |
| tournament_player_ppg_top10_overlap | 0.558621 |
| tournament_player_ppg_top10_random_overlap | 0.280534 |
| tournament_player_ppg_top10_adjusted_overlap | 0.380153 |
| neg_auroc | 0.714647 |
| neg_average_precision | 0.448392 |
| neg_precision | 0.596674 |
| neg_recall | 0.13147 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.177697 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.030367 |
| no_buzz_calibration_error | 0.017254 |
| no_buzz_brier | 0.0148778 |
| full_pmf_max_mass_error | 6.66134e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9360 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 462 |
| first_buzzer_player_replay_accuracy_events | 9238 |
| first_buzzer_team_replay_accuracy_events | 9238 |
| tossup_scorer_player_replay_accuracy_events | 9360 |
| tossup_scorer_team_replay_accuracy_events | 9360 |
| tossup_game_winner_accuracy_games | 455 |
| tossup_game_margin_mae_games | 468 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 1 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.646154 |
| tossup_game_margin_mae | 50.3846 |
| tossup_game_zero_margin_mae | 58.4615 |
| tossup_game_margin_mae_games | 468 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 455 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.714647 | 0.491587 | 0.0126121 | 0.15997 | 0.774225 | 0.764178 | 0.0100465 | 0.139642 | 0.583622 | 0.810937 | 0.917207 | 0.154779 |
| tossup_correctness | tier | fall | 2798 | 0.740494 | 0.456732 | 0.0228095 | 0.146372 | 0.793781 | 0.785204 | 0.00857756 | 0.140694 | 0.584019 | 0.822007 | 0.920333 | 0.151196 |
| tossup_correctness | tier | nationals | 1545 | 0.713678 | 0.536344 | 0.0478646 | 0.178501 | 0.744337 | 0.721036 | 0.023301 | 0.142751 | 0.569639 | 0.794359 | 0.912182 | 0.161046 |
| tossup_correctness | tier | regionals | 2039 | 0.708046 | 0.497038 | 0.013081 | 0.162081 | 0.770966 | 0.762138 | 0.00882786 | 0.132793 | 0.583669 | 0.803021 | 0.914754 | 0.157737 |
| tossup_correctness | tier | winter | 2875 | 0.692105 | 0.497589 | 0.0199458 | 0.161748 | 0.773565 | 0.768348 | 0.00521739 | 0.141153 | 0.593852 | 0.813068 | 0.917226 | 0.152799 |
| tossup_correctness | category | Current Events | 129 | 0.690644 | 0.606427 | 0.0891103 | 0.20838 | 0.689922 | 0.666667 | 0.0232558 | 0.149606 | 0.516484 | 0.785979 | 0.926652 | 0.162196 |
| tossup_correctness | category | Fine Arts | 1074 | 0.710197 | 0.475545 | 0.0268016 | 0.152679 | 0.795158 | 0.776536 | 0.018622 | 0.151726 | 0.575994 | 0.798061 | 0.916805 | 0.157576 |
| tossup_correctness | category | Geography | 180 | 0.752187 | 0.565794 | 0.0748987 | 0.191196 | 0.727778 | 0.616667 | 0.111111 | 0.228583 | 0.234163 | 0.772409 | 0.91186 | 0.162192 |
| tossup_correctness | category | History | 1454 | 0.696087 | 0.508894 | 0.0235653 | 0.166661 | 0.764099 | 0.757909 | 0.00618982 | 0.138354 | 0.573614 | 0.812013 | 0.921084 | 0.154184 |
| tossup_correctness | category | Literature | 1435 | 0.728852 | 0.432223 | 0.0238061 | 0.135291 | 0.816028 | 0.810453 | 0.00557491 | 0.118846 | 0.643446 | 0.843888 | 0.924657 | 0.139394 |
| tossup_correctness | category | Mythology | 324 | 0.683199 | 0.476315 | 0.0328964 | 0.152428 | 0.780864 | 0.79321 | -0.0123457 | 0.112663 | 0.680206 | 0.838683 | 0.917494 | 0.141797 |
| tossup_correctness | category | Other Academic | 71 | 0.592593 | 0.547913 | 0.0986813 | 0.177462 | 0.760563 | 0.760563 | 0 | 0.106622 | 0.645969 | 0.807752 | 0.905238 | 0.159664 |
| tossup_correctness | category | Philosophy | 310 | 0.726809 | 0.49037 | 0.0315422 | 0.160863 | 0.770968 | 0.76129 | 0.00967742 | 0.118911 | 0.618928 | 0.801343 | 0.916607 | 0.157744 |
| tossup_correctness | category | Popular Culture | 108 | 0.492187 | 0.372597 | 0.111058 | 0.106287 | 0.888889 | 0.888889 | 0 | 0.0737229 | 0.744361 | 0.851155 | 0.914545 | 0.129357 |
| tossup_correctness | category | Religion | 361 | 0.679907 | 0.533372 | 0.0178478 | 0.177621 | 0.736842 | 0.742382 | -0.00554017 | 0.140135 | 0.528106 | 0.756147 | 0.887669 | 0.174509 |
| tossup_correctness | category | Science | 1445 | 0.721414 | 0.508933 | 0.0295246 | 0.168373 | 0.757093 | 0.746021 | 0.0110727 | 0.136496 | 0.579812 | 0.800275 | 0.907874 | 0.159633 |
| tossup_correctness | category | Social Science | 327 | 0.737327 | 0.528258 | 0.0470794 | 0.176957 | 0.724771 | 0.718654 | 0.00611621 | 0.176234 | 0.472929 | 0.780333 | 0.913832 | 0.164451 |
| tossup_correctness | category | Unknown | 2039 | 0.708046 | 0.497038 | 0.013081 | 0.162081 | 0.770966 | 0.762138 | 0.00882786 | 0.132793 | 0.583669 | 0.803021 | 0.914754 | 0.157737 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.659418 | 0.539909 | 0.0711975 | 0.181551 | 0.726776 | 0.743169 | -0.0163934 | 0.143148 | 0.525585 | 0.768334 | 0.899107 | 0.172304 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.72274 | 0.522842 | 0.0277523 | 0.173376 | 0.744503 | 0.728796 | 0.0157068 | 0.143229 | 0.547259 | 0.790982 | 0.906675 | 0.164164 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.730302 | 0.494845 | 0.0251348 | 0.161636 | 0.767753 | 0.752568 | 0.0151854 | 0.14147 | 0.586594 | 0.80991 | 0.914266 | 0.154639 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.709365 | 0.471291 | 0.0177861 | 0.15182 | 0.790609 | 0.786087 | 0.00452174 | 0.125721 | 0.62376 | 0.825031 | 0.921122 | 0.147487 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.705399 | 0.495701 | 0.0221886 | 0.160952 | 0.775707 | 0.764393 | 0.0113145 | 0.147038 | 0.559239 | 0.802364 | 0.918959 | 0.157809 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 2.63748 | 0.737141 | 0.567382 | 1.43004 | 2.15512 | 2.62367 | 3.13926 | 3.90751 | 4.56448 |
| player | theta_1 | 1197 | -1.20388 | 0.837934 | -3.54886 | -2.51211 | -1.75746 | -1.24889 | -0.707944 | 0.281328 | 1.85115 |
| player | theta_2 | 1197 | -0.979239 | 0.631081 | -3.22399 | -2.07024 | -1.37894 | -0.979941 | -0.579261 | 0.0329426 | 1.44471 |
| player | theta_3 | 1197 | -1.09719 | 0.769493 | -3.29737 | -2.23471 | -1.61017 | -1.16916 | -0.642029 | 0.276511 | 1.91121 |
| player | theta_norm | 1197 | 2.2174 | 0.62179 | 0.383088 | 1.26632 | 1.77015 | 2.18769 | 2.62982 | 3.26485 | 4.28867 |
| tossup | start_difficulty_d1 | 1240 | -1.77248 | 0.545941 | -3.54809 | -2.55033 | -2.13628 | -1.83835 | -1.46948 | -0.814542 | 1.09524 |
| tossup | start_difficulty_d2 | 1240 | -1.76291 | 0.500114 | -3.31047 | -2.51712 | -2.09975 | -1.79441 | -1.44604 | -0.909632 | 0.294552 |
| tossup | start_difficulty_d3 | 1240 | -1.76657 | 0.508845 | -3.54415 | -2.54034 | -2.11962 | -1.79801 | -1.44195 | -0.891833 | 0.0870517 |
| tossup | end_difficulty_d1 | 1240 | -2.76 | 0.637215 | -4.65182 | -3.66549 | -3.17468 | -2.83523 | -2.41077 | -1.64061 | 0.398349 |
| tossup | end_difficulty_d2 | 1240 | -2.74844 | 0.586126 | -4.61486 | -3.64091 | -3.1398 | -2.78974 | -2.37354 | -1.748 | -0.434443 |
| tossup | end_difficulty_d3 | 1240 | -2.7505 | 0.593297 | -4.83099 | -3.66968 | -3.16126 | -2.78915 | -2.37673 | -1.75019 | -0.650901 |
| tossup | total_drop_d1 | 1240 | 0.987522 | 0.112229 | 0.600564 | 0.798825 | 0.912006 | 0.991782 | 1.06568 | 1.14943 | 1.62804 |
| tossup | total_drop_d2 | 1240 | 0.985527 | 0.102611 | 0.659198 | 0.822915 | 0.913422 | 0.986013 | 1.05529 | 1.16193 | 1.34168 |
| tossup | total_drop_d3 | 1240 | 0.983936 | 0.102237 | 0.648733 | 0.818095 | 0.908991 | 0.985212 | 1.05092 | 1.15845 | 1.28683 |
| tossup | drop_share_1_d1 | 1240 | 0.304067 | 0.0154244 | 0.23142 | 0.278831 | 0.294752 | 0.303872 | 0.314825 | 0.327374 | 0.366017 |
| tossup | drop_share_2_d1 | 1240 | 0.347015 | 0.011466 | 0.305786 | 0.327938 | 0.339418 | 0.347203 | 0.35492 | 0.365134 | 0.387688 |
| tossup | drop_share_3_d1 | 1240 | 0.348918 | 0.0164755 | 0.29894 | 0.323911 | 0.338011 | 0.348736 | 0.359375 | 0.375601 | 0.418838 |
| tossup | drop_share_1_d2 | 1240 | 0.303675 | 0.0140388 | 0.244688 | 0.280519 | 0.294588 | 0.303638 | 0.313157 | 0.327036 | 0.344324 |
| tossup | drop_share_2_d2 | 1240 | 0.346955 | 0.0113509 | 0.310731 | 0.328277 | 0.339431 | 0.34683 | 0.354725 | 0.365697 | 0.385739 |
| tossup | drop_share_3_d2 | 1240 | 0.34937 | 0.0151472 | 0.30309 | 0.32538 | 0.339165 | 0.349376 | 0.359417 | 0.373629 | 0.410426 |
| tossup | drop_share_1_d3 | 1240 | 0.303606 | 0.0147213 | 0.244718 | 0.279735 | 0.294061 | 0.303882 | 0.313772 | 0.326843 | 0.357228 |
| tossup | drop_share_2_d3 | 1240 | 0.347163 | 0.0111596 | 0.311556 | 0.329224 | 0.339908 | 0.346699 | 0.354507 | 0.365719 | 0.385279 |
| tossup | drop_share_3_d3 | 1240 | 0.349231 | 0.0153661 | 0.309455 | 0.324949 | 0.338582 | 0.348911 | 0.359161 | 0.375511 | 0.412261 |
| tossup | r_1 | 1240 | 0.322236 | 0.146132 | 0.069352 | 0.132915 | 0.210925 | 0.291019 | 0.409289 | 0.62389 | 0.864152 |
| tossup | r_2 | 1240 | 0.332917 | 0.111737 | 0.067031 | 0.163763 | 0.25761 | 0.324536 | 0.396343 | 0.540515 | 0.687571 |
| tossup | r_3 | 1240 | 0.344847 | 0.123213 | 0.068032 | 0.160618 | 0.255441 | 0.338302 | 0.418454 | 0.56148 | 0.808882 |
| tossup | r_norm | 1240 | 0.617078 | 0.0422781 | 0.577375 | 0.579579 | 0.587758 | 0.603014 | 0.630408 | 0.707816 | 0.869475 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 4.49455 | 0.485868 | 2.06553 | 3.76296 | 4.22331 | 4.45088 | 4.7188 | 5.36997 | 6.20327 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 4.46458 | 0.423001 | 2.49109 | 3.77699 | 4.23672 | 4.44478 | 4.68416 | 5.16395 | 6.67857 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 4.47606 | 0.435016 | 2.35016 | 3.7763 | 4.23698 | 4.46214 | 4.70982 | 5.27479 | 6.10356 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 1.80041 | 2.24725 | -10.7373 | -3.02456 | 0.721461 | 2.87664 | 3.30057 | 3.64897 | 4.3511 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 2.39701 | 1.87889 | -8.53429 | -1.91104 | 2.45402 | 3.12132 | 3.40106 | 3.71856 | 4.15577 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 2.21186 | 2.11566 | -10.8037 | -2.40907 | 2.18172 | 3.08779 | 3.38188 | 3.72381 | 4.2203 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 2.69414 | 2.40975 | 0.904335 | 0.989969 | 1.06998 | 1.35872 | 3.97258 | 7.96484 | 15.2517 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.06757 | 2.01884 | 0.90351 | 0.964134 | 1.02698 | 1.1831 | 1.77208 | 6.73491 | 13.6048 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.26419 | 2.25413 | 0.871094 | 0.971304 | 1.03862 | 1.21199 | 2.086 | 7.21965 | 15.5066 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.236202 | 0.0779731 | 0.0457189 | 0.0835395 | 0.181013 | 0.268678 | 0.294004 | 0.315023 | 0.523001 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.346169 | 0.0729042 | 0.0711663 | 0.19761 | 0.336773 | 0.352063 | 0.367026 | 0.447269 | 0.67157 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.417629 | 0.123866 | 0.12089 | 0.308338 | 0.347971 | 0.370778 | 0.437431 | 0.705616 | 0.877149 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.254649 | 0.0671175 | 0.0294205 | 0.102427 | 0.238187 | 0.278489 | 0.295777 | 0.314266 | 0.606082 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.349517 | 0.0591488 | 0.0700297 | 0.247307 | 0.341095 | 0.351404 | 0.364016 | 0.410929 | 0.682703 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.395834 | 0.100291 | 0.107524 | 0.31923 | 0.350312 | 0.365106 | 0.39494 | 0.637614 | 0.881408 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.249656 | 0.0693843 | 0.042346 | 0.0927272 | 0.22737 | 0.275304 | 0.296073 | 0.313942 | 0.52735 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.350084 | 0.0569802 | 0.0935717 | 0.239274 | 0.340608 | 0.351919 | 0.366424 | 0.428694 | 0.701965 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.400261 | 0.102856 | 0.0659251 | 0.3212 | 0.349701 | 0.367719 | 0.40336 | 0.652226 | 0.858219 |
| tossup_hazard | hazard_r_1 | 1240 | 0.383819 | 0.275101 | 0.0269716 | 0.0644689 | 0.135439 | 0.298752 | 0.609369 | 0.864865 | 0.944474 |
| tossup_hazard | hazard_r_2 | 1240 | 0.291914 | 0.203068 | 0.0241023 | 0.0549693 | 0.118441 | 0.23483 | 0.429704 | 0.682614 | 0.827984 |
| tossup_hazard | hazard_r_3 | 1240 | 0.324267 | 0.238115 | 0.0229923 | 0.0502632 | 0.127853 | 0.247645 | 0.494785 | 0.792161 | 0.925702 |
