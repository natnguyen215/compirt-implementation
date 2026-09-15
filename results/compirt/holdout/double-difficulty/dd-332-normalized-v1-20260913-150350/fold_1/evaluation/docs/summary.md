# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-20260913-150350/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-20260913-150350/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 285519 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.709295 |
| log_loss | 0.497365 |
| ece | 0.0159363 |
| brier | 0.161797 |
| accuracy | 0.772462 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0103376 |
| probability_std | 0.143633 |
| probability_p10 | 0.573603 |
| probability_p50 | 0.813244 |
| probability_p90 | 0.920299 |
| mean_predictive_variance | 0.153502 |
| integrated_brier_score | 0.100864 |
| joint_tossup_event_log_loss | 6.5888 |
| buzz_position_mae | 0.153638 |
| buzz_position_median_absolute_error | 0.135934 |
| buzz_position_bias | -0.0525324 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.351699 |
| first_buzzer_mean_reciprocal_rank | 0.565402 |
| first_buzzer_log_loss | 1.67565 |
| first_buzzer_events | 9093 |
| first_buzzer_player_replay_accuracy | 0.17277 |
| first_buzzer_team_replay_accuracy | 0.408996 |
| tossup_scorer_player_replay_accuracy | 0.205411 |
| tossup_scorer_team_replay_accuracy | 0.386364 |
| tossup_game_winner_accuracy | 0.665188 |
| tossup_model_official_winner_accuracy | 0.670306 |
| tossup_game_margin_mae | 46.6775 |
| tossup_game_zero_margin_mae | 55.2922 |
| tournament_player_ppg_spearman | 0.566533 |
| tournament_player_ppg_mae | 12.9145 |
| tournament_player_ppg_top10_overlap | 0.555172 |
| tournament_player_ppg_top10_random_overlap | 0.269705 |
| tournament_player_ppg_top10_adjusted_overlap | 0.397381 |
| neg_auroc | 0.709295 |
| neg_average_precision | 0.445851 |
| neg_precision | 0.587361 |
| neg_recall | 0.146093 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.176806 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0315763 |
| no_buzz_calibration_error | 0.0156672 |
| no_buzz_brier | 0.0174494 |
| full_pmf_max_mass_error | 5.55112e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9240 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 458 |
| first_buzzer_player_replay_accuracy_events | 9093 |
| first_buzzer_team_replay_accuracy_events | 9093 |
| tossup_scorer_player_replay_accuracy_events | 9240 |
| tossup_scorer_team_replay_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 451 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.665188 |
| tossup_game_margin_mae | 46.6775 |
| tossup_game_zero_margin_mae | 55.2922 |
| tossup_game_margin_mae_games | 462 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 451 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.709295 | 0.497365 | 0.0159363 | 0.161797 | 0.772462 | 0.762125 | 0.0103376 | 0.143633 | 0.573603 | 0.813244 | 0.920299 | 0.153502 |
| tossup_correctness | tier | fall | 2842 | 0.729105 | 0.463802 | 0.0125863 | 0.149035 | 0.790992 | 0.785362 | 0.00562984 | 0.140458 | 0.585713 | 0.825736 | 0.928508 | 0.148125 |
| tossup_correctness | tier | nationals | 1564 | 0.713759 | 0.540585 | 0.0461932 | 0.179816 | 0.73977 | 0.718031 | 0.0217391 | 0.145687 | 0.557739 | 0.800214 | 0.913731 | 0.159573 |
| tossup_correctness | tier | regionals | 1937 | 0.685609 | 0.513658 | 0.0247082 | 0.167794 | 0.763552 | 0.758389 | 0.00516262 | 0.138916 | 0.58066 | 0.808044 | 0.915062 | 0.156063 |
| tossup_correctness | tier | winter | 2750 | 0.700142 | 0.495993 | 0.0161514 | 0.160515 | 0.778182 | 0.765818 | 0.0123636 | 0.148105 | 0.567974 | 0.811658 | 0.919889 | 0.153803 |
| tossup_correctness | category | Current Events | 126 | 0.719161 | 0.492162 | 0.069468 | 0.16024 | 0.777778 | 0.769841 | 0.00793651 | 0.127256 | 0.553921 | 0.764343 | 0.885025 | 0.174726 |
| tossup_correctness | category | Fine Arts | 1071 | 0.750431 | 0.468372 | 0.0229838 | 0.151372 | 0.785247 | 0.766573 | 0.0186741 | 0.155495 | 0.544752 | 0.810688 | 0.924714 | 0.153838 |
| tossup_correctness | category | Geography | 185 | 0.797204 | 0.49496 | 0.0756891 | 0.162114 | 0.745946 | 0.697297 | 0.0486486 | 0.217917 | 0.362687 | 0.756758 | 0.89382 | 0.168141 |
| tossup_correctness | category | History | 1440 | 0.707442 | 0.511331 | 0.0299718 | 0.167877 | 0.761111 | 0.754167 | 0.00694444 | 0.140771 | 0.579733 | 0.815312 | 0.926689 | 0.151623 |
| tossup_correctness | category | Literature | 1422 | 0.67859 | 0.450994 | 0.014449 | 0.142147 | 0.81083 | 0.814346 | -0.00351617 | 0.123101 | 0.641953 | 0.839695 | 0.931337 | 0.140041 |
| tossup_correctness | category | Mythology | 318 | 0.664922 | 0.482322 | 0.0372636 | 0.15197 | 0.805031 | 0.789308 | 0.0157233 | 0.122761 | 0.643936 | 0.830901 | 0.928266 | 0.143818 |
| tossup_correctness | category | Other Academic | 66 | 0.802912 | 0.519738 | 0.173056 | 0.175794 | 0.727273 | 0.712121 | 0.0151515 | 0.135539 | 0.58073 | 0.798218 | 0.889916 | 0.161264 |
| tossup_correctness | category | Philosophy | 311 | 0.725338 | 0.508792 | 0.0885268 | 0.169469 | 0.73955 | 0.745981 | -0.00643087 | 0.13119 | 0.609257 | 0.816101 | 0.916857 | 0.152862 |
| tossup_correctness | category | Popular Culture | 102 | 0.52037 | 0.378202 | 0.0519927 | 0.107818 | 0.882353 | 0.882353 | 0 | 0.0698174 | 0.756658 | 0.853661 | 0.916174 | 0.129005 |
| tossup_correctness | category | Religion | 358 | 0.714335 | 0.541416 | 0.0309507 | 0.180073 | 0.73743 | 0.712291 | 0.0251397 | 0.154727 | 0.494251 | 0.784621 | 0.899408 | 0.170092 |
| tossup_correctness | category | Science | 1433 | 0.695112 | 0.528669 | 0.0374902 | 0.174346 | 0.757153 | 0.738311 | 0.0188416 | 0.145569 | 0.554503 | 0.801268 | 0.916743 | 0.158759 |
| tossup_correctness | category | Social Science | 324 | 0.775207 | 0.490256 | 0.055742 | 0.160779 | 0.759259 | 0.731481 | 0.0277778 | 0.15531 | 0.508382 | 0.797203 | 0.899294 | 0.162578 |
| tossup_correctness | category | Unknown | 1937 | 0.685609 | 0.513658 | 0.0247082 | 0.167794 | 0.763552 | 0.758389 | 0.00516262 | 0.138916 | 0.58066 | 0.808044 | 0.915062 | 0.156063 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.619048 | 0.602752 | 0.0775777 | 0.203359 | 0.676647 | 0.712575 | -0.0359281 | 0.134888 | 0.561027 | 0.778216 | 0.888207 | 0.172021 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.72248 | 0.52111 | 0.0238674 | 0.172739 | 0.742325 | 0.729167 | 0.0131579 | 0.157711 | 0.515037 | 0.78378 | 0.905985 | 0.165012 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.714341 | 0.502311 | 0.0289098 | 0.163803 | 0.77305 | 0.755083 | 0.0179669 | 0.136056 | 0.597467 | 0.813936 | 0.918852 | 0.152286 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.69283 | 0.484362 | 0.0179391 | 0.155741 | 0.787975 | 0.780942 | 0.00703235 | 0.128019 | 0.616947 | 0.824811 | 0.92182 | 0.148241 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.717418 | 0.493196 | 0.0124632 | 0.160508 | 0.771849 | 0.762029 | 0.00981997 | 0.155628 | 0.535268 | 0.809498 | 0.92454 | 0.154794 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 2.66729 | 0.737638 | 0.488558 | 1.48338 | 2.17265 | 2.66521 | 3.15864 | 3.94752 | 4.66526 |
| player | theta_1 | 1167 | -1.23191 | 0.833075 | -3.60199 | -2.48686 | -1.77339 | -1.29777 | -0.723125 | 0.221124 | 1.51772 |
| player | theta_2 | 1167 | -1.01453 | 0.716773 | -3.38126 | -2.09955 | -1.45482 | -1.07005 | -0.604416 | 0.25743 | 1.85817 |
| player | theta_3 | 1167 | -1.05464 | 0.766677 | -3.36254 | -2.21386 | -1.54165 | -1.09762 | -0.614325 | 0.347237 | 1.91406 |
| player | theta_norm | 1167 | 2.25575 | 0.604224 | 0.447772 | 1.33317 | 1.84374 | 2.22773 | 2.63151 | 3.33251 | 4.2637 |
| tossup | start_difficulty_d1 | 1220 | -1.78747 | 0.548755 | -3.33185 | -2.55001 | -2.1704 | -1.83206 | -1.47476 | -0.882463 | 1.26344 |
| tossup | start_difficulty_d2 | 1220 | -1.77557 | 0.517179 | -3.39816 | -2.54972 | -2.14862 | -1.81638 | -1.44694 | -0.84439 | 0.223075 |
| tossup | start_difficulty_d3 | 1220 | -1.77205 | 0.511141 | -3.60139 | -2.539 | -2.14346 | -1.79104 | -1.44003 | -0.901226 | 0.172484 |
| tossup | end_difficulty_d1 | 1220 | -2.77631 | 0.640083 | -4.63796 | -3.70615 | -3.20689 | -2.82478 | -2.39431 | -1.74013 | 0.599482 |
| tossup | end_difficulty_d2 | 1220 | -2.76248 | 0.604191 | -4.77986 | -3.67817 | -3.19361 | -2.79941 | -2.38076 | -1.68886 | -0.511047 |
| tossup | end_difficulty_d3 | 1220 | -2.75594 | 0.595371 | -4.88776 | -3.6776 | -3.18252 | -2.77127 | -2.37318 | -1.76039 | -0.527892 |
| tossup | total_drop_d1 | 1220 | 0.988837 | 0.111973 | 0.624129 | 0.803931 | 0.91431 | 0.992158 | 1.06357 | 1.16168 | 1.34215 |
| tossup | total_drop_d2 | 1220 | 0.986908 | 0.104209 | 0.663625 | 0.818856 | 0.917933 | 0.985702 | 1.05187 | 1.16235 | 1.3817 |
| tossup | total_drop_d3 | 1220 | 0.983895 | 0.102137 | 0.682559 | 0.819817 | 0.912634 | 0.983475 | 1.0515 | 1.15863 | 1.31671 |
| tossup | drop_share_1_d1 | 1220 | 0.30411 | 0.0154862 | 0.220638 | 0.2792 | 0.294629 | 0.304273 | 0.314631 | 0.327848 | 0.358826 |
| tossup | drop_share_2_d1 | 1220 | 0.347149 | 0.0113317 | 0.31165 | 0.327943 | 0.339759 | 0.347389 | 0.355114 | 0.364914 | 0.386659 |
| tossup | drop_share_3_d1 | 1220 | 0.348741 | 0.0163937 | 0.295749 | 0.322758 | 0.337489 | 0.348496 | 0.359025 | 0.375779 | 0.429828 |
| tossup | drop_share_1_d2 | 1220 | 0.303541 | 0.0143901 | 0.256616 | 0.279116 | 0.294199 | 0.304219 | 0.312887 | 0.32735 | 0.347176 |
| tossup | drop_share_2_d2 | 1220 | 0.346872 | 0.0114183 | 0.310516 | 0.328063 | 0.339151 | 0.346731 | 0.35444 | 0.365029 | 0.391876 |
| tossup | drop_share_3_d2 | 1220 | 0.349587 | 0.0154702 | 0.300004 | 0.325509 | 0.339389 | 0.349304 | 0.359285 | 0.374771 | 0.417028 |
| tossup | drop_share_1_d3 | 1220 | 0.303471 | 0.0149099 | 0.239342 | 0.27936 | 0.294261 | 0.303919 | 0.313544 | 0.327346 | 0.358127 |
| tossup | drop_share_2_d3 | 1220 | 0.347091 | 0.011149 | 0.311167 | 0.328751 | 0.33983 | 0.346814 | 0.354248 | 0.365738 | 0.383464 |
| tossup | drop_share_3_d3 | 1220 | 0.349439 | 0.0156513 | 0.308733 | 0.325715 | 0.338703 | 0.348923 | 0.358926 | 0.376799 | 0.419667 |
| tossup | r_1 | 1220 | 0.322731 | 0.144134 | 0.0642279 | 0.135178 | 0.212464 | 0.295746 | 0.409808 | 0.590722 | 0.846844 |
| tossup | r_2 | 1220 | 0.337308 | 0.122384 | 0.0558501 | 0.154053 | 0.253791 | 0.327374 | 0.408968 | 0.552999 | 0.803605 |
| tossup | r_3 | 1220 | 0.339961 | 0.123467 | 0.0702545 | 0.156526 | 0.252448 | 0.328477 | 0.412552 | 0.565066 | 0.782147 |
| tossup | r_norm | 1220 | 0.618475 | 0.0441616 | 0.577395 | 0.579137 | 0.588639 | 0.603624 | 0.632508 | 0.716148 | 0.853788 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 4.52106 | 0.480359 | 1.83009 | 3.82155 | 4.23203 | 4.46316 | 4.77548 | 5.422 | 6.40095 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 4.4534 | 0.420953 | 1.98549 | 3.80598 | 4.22552 | 4.43401 | 4.65715 | 5.17631 | 6.55088 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 4.46898 | 0.412722 | 2.20045 | 3.8067 | 4.24522 | 4.46472 | 4.69067 | 5.18086 | 6.05449 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | 1.76592 | 2.23092 | -10.6634 | -2.98934 | 0.74351 | 2.8244 | 3.28591 | 3.62673 | 4.42806 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | 2.2098 | 2.0856 | -9.398 | -2.31799 | 2.1791 | 3.12575 | 3.37557 | 3.69516 | 4.0589 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | 2.3272 | 2.08467 | -9.31404 | -2.61119 | 2.45123 | 3.18982 | 3.42974 | 3.7473 | 4.48438 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 2.75514 | 2.40349 | 0.909155 | 0.986047 | 1.05843 | 1.41573 | 3.96658 | 7.9275 | 15.2198 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 2.2436 | 2.22915 | 0.904917 | 0.964846 | 1.03184 | 1.17641 | 2.01295 | 7.14356 | 13.9294 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 2.14178 | 2.19799 | 0.874324 | 0.970764 | 1.02543 | 1.15846 | 1.78138 | 7.35772 | 13.8851 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.232096 | 0.0794147 | 0.0432702 | 0.0843175 | 0.170874 | 0.264305 | 0.294008 | 0.314978 | 0.523452 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.343908 | 0.0744094 | 0.0572014 | 0.18201 | 0.335701 | 0.351515 | 0.366707 | 0.452466 | 0.663237 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.423995 | 0.12722 | 0.112492 | 0.313574 | 0.348791 | 0.370918 | 0.457058 | 0.728214 | 0.899528 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.251681 | 0.070112 | 0.0330956 | 0.093185 | 0.229399 | 0.279716 | 0.296136 | 0.313985 | 0.526779 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.349434 | 0.0622769 | 0.071778 | 0.238068 | 0.340557 | 0.351302 | 0.36424 | 0.434753 | 0.698622 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.398885 | 0.105608 | 0.0980983 | 0.319143 | 0.350247 | 0.36437 | 0.399472 | 0.657355 | 0.879009 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.254466 | 0.0667849 | 0.0410956 | 0.0944211 | 0.237665 | 0.278718 | 0.295981 | 0.313692 | 0.56936 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.351655 | 0.0546866 | 0.0855045 | 0.265279 | 0.341195 | 0.351586 | 0.36447 | 0.424704 | 0.639213 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.393878 | 0.0957102 | 0.0781117 | 0.322547 | 0.349793 | 0.36627 | 0.394851 | 0.614063 | 0.862448 |
| tossup_hazard | hazard_r_1 | 1220 | 0.399192 | 0.280552 | 0.0322998 | 0.060332 | 0.128157 | 0.33617 | 0.659405 | 0.861542 | 0.939143 |
| tossup_hazard | hazard_r_2 | 1220 | 0.301145 | 0.229883 | 0.02168 | 0.0543047 | 0.116433 | 0.211742 | 0.463761 | 0.765957 | 0.891954 |
| tossup_hazard | hazard_r_3 | 1220 | 0.299664 | 0.226156 | 0.0243182 | 0.0523917 | 0.120537 | 0.218635 | 0.446201 | 0.766468 | 0.928764 |
