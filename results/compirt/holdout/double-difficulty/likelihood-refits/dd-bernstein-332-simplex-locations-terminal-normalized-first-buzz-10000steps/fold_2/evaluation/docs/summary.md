# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-10000steps/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-10000steps/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 277824 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.710862 |
| log_loss | 0.492603 |
| ece | 0.012187 |
| brier | 0.159959 |
| accuracy | 0.773577 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00939829 |
| probability_std | 0.147734 |
| probability_p10 | 0.564517 |
| probability_p50 | 0.806083 |
| probability_p90 | 0.919524 |
| mean_predictive_variance | 0.155972 |
| integrated_brier_score | 0.0959965 |
| joint_tossup_event_log_loss | 6.45697 |
| buzz_position_mae | 0.141967 |
| buzz_position_median_absolute_error | 0.122047 |
| buzz_position_bias | -0.0139569 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.370314 |
| first_buzzer_mean_reciprocal_rank | 0.581416 |
| first_buzzer_log_loss | 1.62552 |
| first_buzzer_events | 9257 |
| first_buzzer_player_replay_accuracy | 0.22743 |
| first_buzzer_team_replay_accuracy | 0.485928 |
| tossup_scorer_player_replay_accuracy | 0.238889 |
| tossup_scorer_team_replay_accuracy | 0.439744 |
| tossup_game_winner_accuracy | 0.687912 |
| tossup_model_official_winner_accuracy | 0.707792 |
| tossup_game_margin_mae | 49.4444 |
| tossup_game_zero_margin_mae | 58.4615 |
| tournament_player_ppg_spearman | 0.606732 |
| tournament_player_ppg_mae | 12.256 |
| tournament_player_ppg_top10_overlap | 0.575862 |
| tournament_player_ppg_top10_random_overlap | 0.280534 |
| tournament_player_ppg_top10_adjusted_overlap | 0.416166 |
| neg_auroc | 0.710862 |
| neg_average_precision | 0.450857 |
| neg_precision | 0.57645 |
| neg_recall | 0.150252 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.176219 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.019968 |
| no_buzz_calibration_error | 0.00685501 |
| no_buzz_brier | 0.0134646 |
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
| tossup_game_winner_accuracy | 0.687912 |
| tossup_game_margin_mae | 49.4444 |
| tossup_game_zero_margin_mae | 58.4615 |
| tossup_game_margin_mae_games | 468 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 455 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.710862 | 0.492603 | 0.012187 | 0.159959 | 0.773577 | 0.764178 | 0.00939829 | 0.147734 | 0.564517 | 0.806083 | 0.919524 | 0.155972 |
| tossup_correctness | tier | fall | 2798 | 0.735842 | 0.45828 | 0.024444 | 0.146377 | 0.792352 | 0.785204 | 0.00714796 | 0.144621 | 0.57428 | 0.812537 | 0.921232 | 0.153246 |
| tossup_correctness | tier | nationals | 1545 | 0.7115 | 0.535307 | 0.0381615 | 0.177837 | 0.744984 | 0.721036 | 0.0239482 | 0.156665 | 0.544889 | 0.792971 | 0.914169 | 0.160579 |
| tossup_correctness | tier | regionals | 2039 | 0.698895 | 0.500281 | 0.0165519 | 0.162697 | 0.770476 | 0.762138 | 0.00833742 | 0.145686 | 0.556297 | 0.796299 | 0.921621 | 0.158395 |
| tossup_correctness | tier | winter | 2875 | 0.69344 | 0.497611 | 0.0174832 | 0.161626 | 0.77287 | 0.768348 | 0.00452174 | 0.146655 | 0.575106 | 0.809005 | 0.917728 | 0.154431 |
| tossup_correctness | category | Current Events | 129 | 0.677664 | 0.612748 | 0.0954574 | 0.208371 | 0.674419 | 0.666667 | 0.00775194 | 0.15966 | 0.528375 | 0.784275 | 0.92487 | 0.162993 |
| tossup_correctness | category | Fine Arts | 1074 | 0.710532 | 0.476718 | 0.0260815 | 0.152836 | 0.793296 | 0.776536 | 0.0167598 | 0.157212 | 0.551179 | 0.793333 | 0.91435 | 0.159533 |
| tossup_correctness | category | Geography | 180 | 0.759499 | 0.563273 | 0.0769573 | 0.190427 | 0.727778 | 0.616667 | 0.111111 | 0.233208 | 0.248392 | 0.764241 | 0.912419 | 0.161837 |
| tossup_correctness | category | History | 1454 | 0.689439 | 0.512701 | 0.0263782 | 0.167829 | 0.76066 | 0.757909 | 0.00275103 | 0.146094 | 0.555884 | 0.808636 | 0.921274 | 0.155492 |
| tossup_correctness | category | Literature | 1435 | 0.723044 | 0.433993 | 0.0213322 | 0.135527 | 0.820209 | 0.810453 | 0.0097561 | 0.12877 | 0.624886 | 0.837381 | 0.928873 | 0.14069 |
| tossup_correctness | category | Mythology | 324 | 0.697892 | 0.471901 | 0.0541898 | 0.150967 | 0.780864 | 0.79321 | -0.0123457 | 0.115538 | 0.656828 | 0.830029 | 0.921289 | 0.144158 |
| tossup_correctness | category | Other Academic | 71 | 0.642702 | 0.534653 | 0.136893 | 0.1746 | 0.760563 | 0.760563 | 0 | 0.122745 | 0.571266 | 0.797071 | 0.904547 | 0.163998 |
| tossup_correctness | category | Philosophy | 310 | 0.712552 | 0.494238 | 0.0270972 | 0.16143 | 0.770968 | 0.76129 | 0.00967742 | 0.123689 | 0.611957 | 0.7995 | 0.918463 | 0.158414 |
| tossup_correctness | category | Popular Culture | 108 | 0.50434 | 0.377261 | 0.0837751 | 0.10826 | 0.87963 | 0.888889 | -0.00925926 | 0.0835615 | 0.722945 | 0.853628 | 0.920637 | 0.13166 |
| tossup_correctness | category | Religion | 361 | 0.695835 | 0.526908 | 0.0372943 | 0.174171 | 0.745152 | 0.742382 | 0.00277008 | 0.147716 | 0.512602 | 0.757306 | 0.889 | 0.176393 |
| tossup_correctness | category | Science | 1445 | 0.717266 | 0.508163 | 0.0303961 | 0.167713 | 0.755017 | 0.746021 | 0.00899654 | 0.143401 | 0.568245 | 0.795947 | 0.911538 | 0.160125 |
| tossup_correctness | category | Social Science | 327 | 0.747734 | 0.519719 | 0.0542267 | 0.174078 | 0.721713 | 0.718654 | 0.0030581 | 0.177697 | 0.474641 | 0.770713 | 0.912397 | 0.167148 |
| tossup_correctness | category | Unknown | 2039 | 0.698895 | 0.500281 | 0.0165519 | 0.162697 | 0.770476 | 0.762138 | 0.00833742 | 0.145686 | 0.556297 | 0.796299 | 0.921621 | 0.158395 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.67694 | 0.534112 | 0.0777469 | 0.179156 | 0.721311 | 0.743169 | -0.0218579 | 0.154572 | 0.507484 | 0.768132 | 0.905638 | 0.173058 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.723739 | 0.521376 | 0.0287721 | 0.171769 | 0.749738 | 0.728796 | 0.0209424 | 0.154405 | 0.527449 | 0.78741 | 0.910594 | 0.163754 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.721604 | 0.496933 | 0.0184199 | 0.162172 | 0.771326 | 0.752568 | 0.0187584 | 0.147166 | 0.5663 | 0.806778 | 0.918313 | 0.154908 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.701249 | 0.473921 | 0.0162018 | 0.152478 | 0.786783 | 0.786087 | 0.000695652 | 0.134325 | 0.610757 | 0.821936 | 0.922473 | 0.149444 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.706882 | 0.495578 | 0.0258011 | 0.160544 | 0.773378 | 0.764393 | 0.00898502 | 0.15538 | 0.541614 | 0.796299 | 0.919527 | 0.159498 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 1.27328 | 0.797871 | -0.946625 | -0.0461894 | 0.739072 | 1.24903 | 1.79588 | 2.66167 | 3.48668 |
| player | theta_1 | 1197 | -0.545025 | 0.919809 | -2.71514 | -1.89214 | -1.17054 | -0.616679 | -0.0399446 | 1.07046 | 3.48887 |
| player | theta_2 | 1197 | -0.503371 | 0.861387 | -3.02633 | -1.8281 | -1.07355 | -0.588853 | 0.0131959 | 1.01479 | 2.63724 |
| player | theta_3 | 1197 | -0.546647 | 0.882235 | -3.11779 | -1.84431 | -1.12928 | -0.674094 | -0.0421733 | 1.12141 | 3.21087 |
| player | theta_norm | 1197 | 1.67551 | 0.637703 | 0.275195 | 0.725234 | 1.21226 | 1.63015 | 2.06463 | 2.81208 | 4.5417 |
| tossup | start_difficulty_d1 | 1240 | -1.11332 | 0.542497 | -2.92039 | -1.89071 | -1.45822 | -1.1631 | -0.810766 | -0.233613 | 1.79524 |
| tossup | start_difficulty_d2 | 1240 | -1.11318 | 0.48614 | -2.68714 | -1.83523 | -1.42961 | -1.15655 | -0.827391 | -0.300523 | 1.39476 |
| tossup | start_difficulty_d3 | 1240 | -1.12248 | 0.4918 | -2.97146 | -1.86398 | -1.43448 | -1.13079 | -0.809085 | -0.3229 | 1.16156 |
| tossup | end_difficulty_d1 | 1240 | -2.10855 | 0.631748 | -4.09248 | -3.00378 | -2.51254 | -2.14764 | -1.75235 | -1.08154 | 1.17787 |
| tossup | end_difficulty_d2 | 1240 | -2.10781 | 0.573295 | -3.93108 | -2.94834 | -2.4784 | -2.16225 | -1.75883 | -1.15218 | 0.735105 |
| tossup | end_difficulty_d3 | 1240 | -2.11792 | 0.576313 | -4.2861 | -3.01361 | -2.49493 | -2.13336 | -1.74716 | -1.20179 | 0.475482 |
| tossup | total_drop_d1 | 1240 | 0.995231 | 0.110917 | 0.58072 | 0.820575 | 0.923333 | 0.996504 | 1.06734 | 1.17031 | 1.57559 |
| tossup | total_drop_d2 | 1240 | 0.994634 | 0.104083 | 0.588802 | 0.824402 | 0.929291 | 0.997736 | 1.06396 | 1.15477 | 1.39511 |
| tossup | total_drop_d3 | 1240 | 0.995441 | 0.103052 | 0.650324 | 0.832944 | 0.922933 | 0.994835 | 1.0604 | 1.1686 | 1.37876 |
| tossup | drop_share_1_d1 | 1240 | 0.304354 | 0.0153232 | 0.228015 | 0.279722 | 0.29528 | 0.304737 | 0.313646 | 0.328387 | 0.366544 |
| tossup | drop_share_2_d1 | 1240 | 0.346607 | 0.0116135 | 0.310201 | 0.328147 | 0.338675 | 0.346542 | 0.354444 | 0.365665 | 0.406019 |
| tossup | drop_share_3_d1 | 1240 | 0.34904 | 0.0161823 | 0.2811 | 0.324255 | 0.338734 | 0.347992 | 0.358138 | 0.375229 | 0.454059 |
| tossup | drop_share_1_d2 | 1240 | 0.304965 | 0.0143623 | 0.257797 | 0.28089 | 0.295931 | 0.305344 | 0.314285 | 0.327923 | 0.355932 |
| tossup | drop_share_2_d2 | 1240 | 0.347213 | 0.0114213 | 0.316207 | 0.329034 | 0.338929 | 0.347256 | 0.355143 | 0.36625 | 0.380252 |
| tossup | drop_share_3_d2 | 1240 | 0.347822 | 0.0149308 | 0.293273 | 0.32502 | 0.337922 | 0.347373 | 0.356894 | 0.373411 | 0.400973 |
| tossup | drop_share_1_d3 | 1240 | 0.304431 | 0.01441 | 0.243859 | 0.280031 | 0.295383 | 0.304888 | 0.313922 | 0.327218 | 0.360072 |
| tossup | drop_share_2_d3 | 1240 | 0.347097 | 0.0113259 | 0.311877 | 0.328317 | 0.339551 | 0.34714 | 0.354697 | 0.36562 | 0.381886 |
| tossup | drop_share_3_d3 | 1240 | 0.348472 | 0.0149853 | 0.298557 | 0.325313 | 0.339008 | 0.347937 | 0.357861 | 0.373805 | 0.411521 |
| tossup | r_1 | 1240 | 0.321867 | 0.168027 | 0.0494027 | 0.110066 | 0.193369 | 0.282571 | 0.426588 | 0.658878 | 0.856184 |
| tossup | r_2 | 1240 | 0.336808 | 0.159724 | 0.0597566 | 0.123203 | 0.208296 | 0.310602 | 0.439948 | 0.633963 | 0.854831 |
| tossup | r_3 | 1240 | 0.341325 | 0.162058 | 0.0638153 | 0.126401 | 0.213464 | 0.311852 | 0.448217 | 0.656922 | 0.849332 |
| tossup | r_norm | 1240 | 0.640657 | 0.0551811 | 0.577398 | 0.58166 | 0.598799 | 0.624703 | 0.669553 | 0.751046 | 0.862249 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 7.455 | 0.494614 | 5.56222 | 6.58133 | 7.28692 | 7.45018 | 7.65388 | 8.32195 | 9.26421 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 7.51786 | 0.5079 | 4.26486 | 6.72738 | 7.35807 | 7.48486 | 7.69147 | 8.39311 | 10.0118 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 7.49893 | 0.498284 | 3.77273 | 6.64902 | 7.34782 | 7.48492 | 7.68081 | 8.35567 | 9.47654 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 3.96544 | 3.49581 | -12.8777 | -3.11095 | 1.66016 | 6.22939 | 6.44819 | 6.70024 | 7.30634 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 4.66858 | 3.32441 | -12.9774 | -2.40258 | 3.59985 | 6.36409 | 6.53027 | 6.83927 | 7.69332 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 4.53846 | 3.32724 | -15.4534 | -2.15931 | 2.61887 | 6.3593 | 6.53552 | 6.85709 | 7.98648 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.48956 | 3.57074 | 0.868733 | 0.953784 | 1.00932 | 1.07064 | 5.84963 | 10.6821 | 20.4026 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.84928 | 3.41187 | 0.871473 | 0.943877 | 0.993216 | 1.04052 | 4.05425 | 10.1308 | 20.598 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.96047 | 3.38697 | 0.82279 | 0.93619 | 0.988111 | 1.03615 | 4.89177 | 9.63999 | 22.9625 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.262285 | 0.0917479 | 0.0570781 | 0.0971253 | 0.201603 | 0.292871 | 0.305951 | 0.345172 | 0.722078 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.333318 | 0.0817812 | 0.0729251 | 0.16967 | 0.327456 | 0.34537 | 0.357421 | 0.455583 | 0.710632 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.404397 | 0.133347 | 0.0807442 | 0.253526 | 0.341724 | 0.356285 | 0.414338 | 0.712156 | 0.861896 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.267251 | 0.0818351 | 0.0365847 | 0.101587 | 0.261433 | 0.293708 | 0.305172 | 0.324615 | 0.739609 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.335175 | 0.0728976 | 0.0672701 | 0.173027 | 0.334316 | 0.346135 | 0.356786 | 0.414487 | 0.723604 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.397575 | 0.124417 | 0.0838064 | 0.283971 | 0.343117 | 0.356158 | 0.380987 | 0.705847 | 0.8931 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.270182 | 0.0830729 | 0.0498257 | 0.0977609 | 0.266241 | 0.295668 | 0.307057 | 0.333364 | 0.724279 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.336634 | 0.0692273 | 0.0873267 | 0.183949 | 0.332343 | 0.346237 | 0.357159 | 0.429134 | 0.727259 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.393184 | 0.121158 | 0.0567416 | 0.286267 | 0.342759 | 0.354681 | 0.377646 | 0.700148 | 0.861282 |
| tossup_hazard | hazard_r_1 | 1240 | 0.361407 | 0.300754 | 0.0154104 | 0.0404184 | 0.0958738 | 0.227776 | 0.614214 | 0.888915 | 0.95206 |
| tossup_hazard | hazard_r_2 | 1240 | 0.311994 | 0.271613 | 0.0134045 | 0.0342581 | 0.0755232 | 0.195838 | 0.532398 | 0.841238 | 0.949973 |
| tossup_hazard | hazard_r_3 | 1240 | 0.326599 | 0.291982 | 0.0114555 | 0.0360191 | 0.0780045 | 0.196167 | 0.591342 | 0.867643 | 0.971185 |
