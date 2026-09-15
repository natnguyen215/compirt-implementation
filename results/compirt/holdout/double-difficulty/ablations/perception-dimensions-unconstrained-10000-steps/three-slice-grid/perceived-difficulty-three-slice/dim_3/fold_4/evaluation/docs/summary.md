# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_3/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_3/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 311536 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.654032 |
| log_loss | 0.513467 |
| ece | 0.0352335 |
| brier | 0.167042 |
| accuracy | 0.774326 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.000970874 |
| probability_std | 0.140826 |
| probability_p10 | 0.553127 |
| probability_p50 | 0.776434 |
| probability_p90 | 0.911862 |
| mean_predictive_variance | 0.166264 |
| integrated_brier_score | 0.102194 |
| joint_tossup_event_log_loss | 6.95115 |
| buzz_position_mae | 0.16028 |
| buzz_position_median_absolute_error | 0.145845 |
| buzz_position_bias | -0.0639059 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.344768 |
| first_buzzer_mean_reciprocal_rank | 0.555256 |
| first_buzzer_log_loss | 1.71193 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.634196 |
| tossup_scorer_player_top1_accuracy | 0.310768 |
| tossup_scorer_team_top1_accuracy | 0.486141 |
| tossup_game_winner_accuracy | 0.792123 |
| tossup_game_margin_mae | 34.5976 |
| tournament_player_ppg_spearman | 0.676919 |
| tournament_player_ppg_mae | 9.39106 |
| tournament_player_ppg_top10_overlap | 0.686207 |
| neg_auroc | 0.654032 |
| neg_average_precision | 0.368155 |
| neg_precision | 0.507881 |
| neg_recall | 0.13803 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0559827 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0874351 |
| no_buzz_calibration_error | 0.075708 |
| no_buzz_brier | 0.0235765 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.654032 | 0.513467 | 0.0352335 | 0.167042 | 0.774326 | 0.773355 | 0.000970874 | 0.140826 | 0.553127 | 0.776434 | 0.911862 | 0.166264 |
| tossup_correctness | tier | fall | 2876 | 0.650236 | 0.488393 | 0.0294469 | 0.156966 | 0.794854 | 0.793115 | 0.00173853 | 0.128803 | 0.609352 | 0.813726 | 0.922013 | 0.151853 |
| tossup_correctness | tier | nationals | 1579 | 0.661088 | 0.560362 | 0.0580312 | 0.188013 | 0.733376 | 0.729576 | 0.00379987 | 0.142289 | 0.476844 | 0.686869 | 0.851439 | 0.200101 |
| tossup_correctness | tier | regionals | 1990 | 0.64736 | 0.526517 | 0.038052 | 0.17183 | 0.763317 | 0.765829 | -0.00251256 | 0.141948 | 0.556889 | 0.773386 | 0.912173 | 0.166987 |
| tossup_correctness | tier | winter | 2825 | 0.652011 | 0.503589 | 0.0332906 | 0.162205 | 0.784071 | 0.783009 | 0.00106195 | 0.133331 | 0.576925 | 0.787823 | 0.916312 | 0.161513 |
| tossup_correctness | category | Current Events | 123 | 0.666178 | 0.538917 | 0.102533 | 0.177454 | 0.764228 | 0.764228 | 0 | 0.152233 | 0.464635 | 0.701216 | 0.84942 | 0.196824 |
| tossup_correctness | category | Fine Arts | 1093 | 0.638091 | 0.519076 | 0.0426231 | 0.168929 | 0.778591 | 0.769442 | 0.00914913 | 0.127173 | 0.599392 | 0.797022 | 0.914256 | 0.158569 |
| tossup_correctness | category | Geography | 191 | 0.744735 | 0.536235 | 0.0322306 | 0.179274 | 0.732984 | 0.691099 | 0.0418848 | 0.15697 | 0.435079 | 0.710856 | 0.855672 | 0.196482 |
| tossup_correctness | category | History | 1469 | 0.690798 | 0.51299 | 0.0332925 | 0.169148 | 0.760381 | 0.758339 | 0.00204221 | 0.139172 | 0.519876 | 0.749107 | 0.888992 | 0.179385 |
| tossup_correctness | category | Literature | 1436 | 0.60581 | 0.485365 | 0.0593507 | 0.151684 | 0.807799 | 0.81546 | -0.00766017 | 0.122877 | 0.642481 | 0.858328 | 0.949276 | 0.130449 |
| tossup_correctness | category | Mythology | 325 | 0.610992 | 0.470659 | 0.114339 | 0.149267 | 0.809231 | 0.843077 | -0.0338462 | 0.133447 | 0.556229 | 0.759998 | 0.897073 | 0.175454 |
| tossup_correctness | category | Other Academic | 67 | 0.59973 | 0.568501 | 0.154697 | 0.18845 | 0.731343 | 0.791045 | -0.0597015 | 0.136827 | 0.475968 | 0.671243 | 0.830551 | 0.205152 |
| tossup_correctness | category | Philosophy | 322 | 0.623246 | 0.508237 | 0.0470045 | 0.164723 | 0.791925 | 0.785714 | 0.00621118 | 0.123192 | 0.607715 | 0.802382 | 0.918106 | 0.156857 |
| tossup_correctness | category | Popular Culture | 100 | 0.586313 | 0.432554 | 0.151246 | 0.131885 | 0.84 | 0.89 | -0.05 | 0.122807 | 0.565474 | 0.745384 | 0.891624 | 0.177915 |
| tossup_correctness | category | Religion | 365 | 0.643864 | 0.571134 | 0.0598549 | 0.193401 | 0.712329 | 0.723288 | -0.0109589 | 0.143383 | 0.532906 | 0.764486 | 0.895098 | 0.174101 |
| tossup_correctness | category | Science | 1456 | 0.667813 | 0.50913 | 0.0409835 | 0.166383 | 0.781593 | 0.76717 | 0.0144231 | 0.138733 | 0.534457 | 0.755946 | 0.882324 | 0.177699 |
| tossup_correctness | category | Social Science | 333 | 0.697074 | 0.533714 | 0.0236894 | 0.178143 | 0.744745 | 0.72973 | 0.015015 | 0.138846 | 0.52916 | 0.733889 | 0.868719 | 0.185363 |
| tossup_correctness | category | Unknown | 1990 | 0.64736 | 0.526517 | 0.038052 | 0.17183 | 0.763317 | 0.765829 | -0.00251256 | 0.141948 | 0.556889 | 0.773386 | 0.912173 | 0.166987 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.677612 | 0.538859 | 0.0844465 | 0.178447 | 0.759777 | 0.748603 | 0.0111732 | 0.146515 | 0.477222 | 0.695346 | 0.82137 | 0.200597 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.609548 | 0.559852 | 0.0670629 | 0.186899 | 0.737722 | 0.754441 | -0.0167189 | 0.143382 | 0.492909 | 0.726355 | 0.863189 | 0.189045 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.65498 | 0.519191 | 0.0386727 | 0.17035 | 0.764866 | 0.766682 | -0.00181571 | 0.138394 | 0.536456 | 0.759798 | 0.889443 | 0.176143 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.667526 | 0.488922 | 0.028346 | 0.157596 | 0.792142 | 0.787441 | 0.00470114 | 0.134477 | 0.577451 | 0.788028 | 0.914171 | 0.161417 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.653128 | 0.517378 | 0.032997 | 0.166973 | 0.77616 | 0.771758 | 0.0044023 | 0.139577 | 0.577042 | 0.802428 | 0.930826 | 0.154318 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | -1.96568 | 1.28205 | -4.83048 | -3.68105 | -2.96881 | -2.30105 | -0.429113 | -0.0397698 | 1.17363 |
| player | theta_2 | 1196 | -1.32262 | 1.21571 | -4.84194 | -3.33212 | -2.43962 | -0.826199 | -0.306778 | 0.152096 | 1.12717 |
| player | theta_3 | 1196 | -0.592146 | 1.0308 | -4.38262 | -3.06782 | -0.523609 | -0.24968 | -0.071407 | 0.342051 | 1.14253 |
| player | theta_norm | 1196 | 3.08106 | 0.807529 | 1.06708 | 1.89094 | 2.47523 | 3.03254 | 3.61764 | 4.537 | 5.49149 |
| tossup | start_difficulty_d1 | 1240 | -1.82095 | 1.64495 | -5.94021 | -4.08072 | -3.37427 | -1.58176 | -0.189167 | 0.101091 | 0.503001 |
| tossup | start_difficulty_d2 | 1240 | -0.885024 | 1.54644 | -5.20972 | -4.03772 | -1.42887 | -0.175295 | 0.142255 | 0.651731 | 1.84246 |
| tossup | start_difficulty_d3 | 1240 | -0.861841 | 1.33018 | -3.73738 | -3.21955 | -2.45248 | -0.166558 | 0.0928409 | 0.407909 | 1.36874 |
| tossup | end_difficulty_d1 | 1240 | -2.94559 | 1.86393 | -10.101 | -5.9379 | -4.48028 | -2.62102 | -1.18758 | -0.841351 | -0.363005 |
| tossup | end_difficulty_d2 | 1240 | -1.91524 | 1.62333 | -7.62609 | -5.19219 | -2.7658 | -1.18257 | -0.812457 | -0.204578 | 1.07424 |
| tossup | end_difficulty_d3 | 1240 | -1.93338 | 1.49408 | -6.7744 | -4.78306 | -3.35635 | -1.17621 | -0.875374 | -0.52368 | 0.524366 |
| tossup | total_drop_d1 | 1240 | 1.12464 | 0.546808 | 0.360291 | 0.682163 | 0.926019 | 1.00687 | 1.11304 | 1.96645 | 7.00465 |
| tossup | total_drop_d2 | 1240 | 1.03022 | 0.269062 | 0.509434 | 0.74879 | 0.913732 | 0.980408 | 1.07843 | 1.43111 | 3.84655 |
| tossup | total_drop_d3 | 1240 | 1.07154 | 0.286026 | 0.558203 | 0.856408 | 0.945731 | 0.997141 | 1.07425 | 1.54794 | 3.63071 |
| tossup | drop_share_1_d1 | 1240 | 0.341814 | 0.0546518 | 0.213369 | 0.290034 | 0.306341 | 0.319467 | 0.368909 | 0.445268 | 0.625193 |
| tossup | drop_share_2_d1 | 1240 | 0.339794 | 0.0209391 | 0.241825 | 0.306279 | 0.328727 | 0.340964 | 0.35102 | 0.368421 | 0.502215 |
| tossup | drop_share_3_d1 | 1240 | 0.318392 | 0.0474239 | 0.117867 | 0.222795 | 0.296393 | 0.334654 | 0.349829 | 0.3673 | 0.459694 |
| tossup | drop_share_1_d2 | 1240 | 0.317941 | 0.034252 | 0.213629 | 0.283846 | 0.300197 | 0.310614 | 0.326417 | 0.383136 | 0.558918 |
| tossup | drop_share_2_d2 | 1240 | 0.344884 | 0.0175749 | 0.266058 | 0.313798 | 0.336663 | 0.34592 | 0.354226 | 0.368836 | 0.501535 |
| tossup | drop_share_3_d2 | 1240 | 0.337175 | 0.0322259 | 0.159658 | 0.278093 | 0.327792 | 0.343158 | 0.35421 | 0.372927 | 0.47387 |
| tossup | drop_share_1_d3 | 1240 | 0.323786 | 0.0344676 | 0.263306 | 0.288361 | 0.301621 | 0.311708 | 0.334398 | 0.399174 | 0.502844 |
| tossup | drop_share_2_d3 | 1240 | 0.344598 | 0.0134884 | 0.299068 | 0.32281 | 0.335935 | 0.344992 | 0.35298 | 0.364884 | 0.411904 |
| tossup | drop_share_3_d3 | 1240 | 0.331616 | 0.0323442 | 0.185213 | 0.26255 | 0.320378 | 0.34152 | 0.353105 | 0.366615 | 0.391884 |
| tossup | r_1 | 1240 | 0.47632 | 0.386416 | 0.0128965 | 0.0345593 | 0.0716628 | 0.525218 | 0.868101 | 0.93113 | 0.977132 |
| tossup | r_2 | 1240 | 0.251177 | 0.323485 | 0.0131759 | 0.0297619 | 0.0507578 | 0.0896739 | 0.212066 | 0.933082 | 0.97818 |
| tossup | r_3 | 1240 | 0.272503 | 0.327302 | 0.00876881 | 0.0211693 | 0.0435599 | 0.0734114 | 0.681109 | 0.859285 | 0.929089 |
| tossup | r_norm | 1240 | 0.848668 | 0.0692146 | 0.647138 | 0.726337 | 0.801885 | 0.856923 | 0.904252 | 0.948899 | 0.978305 |
