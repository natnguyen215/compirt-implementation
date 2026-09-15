# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_3/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_3/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 311437 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.654189 |
| log_loss | 0.522409 |
| ece | 0.0295586 |
| brier | 0.170602 |
| accuracy | 0.763959 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.00129102 |
| probability_std | 0.136436 |
| probability_p10 | 0.56103 |
| probability_p50 | 0.778376 |
| probability_p90 | 0.909699 |
| mean_predictive_variance | 0.167238 |
| integrated_brier_score | 0.105474 |
| joint_tossup_event_log_loss | 7.00849 |
| buzz_position_mae | 0.163605 |
| buzz_position_median_absolute_error | 0.148395 |
| buzz_position_bias | -0.0669745 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.341689 |
| first_buzzer_mean_reciprocal_rank | 0.555851 |
| first_buzzer_log_loss | 1.72134 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.637655 |
| tossup_scorer_player_top1_accuracy | 0.312739 |
| tossup_scorer_team_top1_accuracy | 0.478662 |
| tossup_game_winner_accuracy | 0.795154 |
| tossup_game_margin_mae | 35.0713 |
| tournament_player_ppg_spearman | 0.693886 |
| tournament_player_ppg_mae | 9.36101 |
| tournament_player_ppg_top10_overlap | 0.637931 |
| neg_auroc | 0.654189 |
| neg_average_precision | 0.37258 |
| neg_precision | 0.487755 |
| neg_recall | 0.109533 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0568494 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0901596 |
| no_buzz_calibration_error | 0.0768899 |
| no_buzz_brier | 0.0251231 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9420 |
| first_buzzer_team_top1_accuracy_events | 9295 |
| tossup_scorer_player_top1_accuracy_events | 9420 |
| tossup_scorer_team_top1_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 454 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.654189 | 0.522409 | 0.0295586 | 0.170602 | 0.763959 | 0.76525 | -0.00129102 | 0.136436 | 0.56103 | 0.778376 | 0.909699 | 0.167238 |
| tossup_correctness | tier | fall | 2933 | 0.646763 | 0.493863 | 0.0298021 | 0.157979 | 0.792363 | 0.791681 | 0.000681896 | 0.128057 | 0.598724 | 0.805835 | 0.918155 | 0.155842 |
| tossup_correctness | tier | nationals | 1584 | 0.650924 | 0.566711 | 0.0494824 | 0.191471 | 0.713384 | 0.724747 | -0.0113636 | 0.138932 | 0.487376 | 0.687427 | 0.84981 | 0.19955 |
| tossup_correctness | tier | regionals | 1886 | 0.638577 | 0.548156 | 0.025417 | 0.182274 | 0.744963 | 0.746023 | -0.00106045 | 0.134391 | 0.55961 | 0.768786 | 0.90413 | 0.170798 |
| tossup_correctness | tier | winter | 2892 | 0.658718 | 0.510304 | 0.024753 | 0.16436 | 0.775242 | 0.773167 | 0.00207469 | 0.128569 | 0.595505 | 0.7964 | 0.916807 | 0.158778 |
| tossup_correctness | category | Current Events | 124 | 0.703087 | 0.521274 | 0.0649795 | 0.171967 | 0.758065 | 0.75 | 0.00806452 | 0.129229 | 0.494217 | 0.695532 | 0.858183 | 0.196995 |
| tossup_correctness | category | Fine Arts | 1103 | 0.613158 | 0.544426 | 0.0485868 | 0.178141 | 0.765186 | 0.759746 | 0.00543971 | 0.128701 | 0.596904 | 0.795741 | 0.920978 | 0.159758 |
| tossup_correctness | category | Geography | 197 | 0.711772 | 0.570476 | 0.0721867 | 0.195145 | 0.71066 | 0.670051 | 0.0406091 | 0.152965 | 0.460114 | 0.686025 | 0.85615 | 0.196575 |
| tossup_correctness | category | History | 1491 | 0.684158 | 0.493092 | 0.0681515 | 0.158685 | 0.784038 | 0.787391 | -0.00335345 | 0.131333 | 0.529438 | 0.738212 | 0.873269 | 0.184371 |
| tossup_correctness | category | Literature | 1472 | 0.627487 | 0.491971 | 0.0363675 | 0.153019 | 0.800951 | 0.804348 | -0.00339674 | 0.114299 | 0.655309 | 0.855238 | 0.945664 | 0.129526 |
| tossup_correctness | category | Mythology | 332 | 0.692533 | 0.46514 | 0.0761055 | 0.148604 | 0.798193 | 0.813253 | -0.0150602 | 0.121785 | 0.566519 | 0.758209 | 0.883465 | 0.17893 |
| tossup_correctness | category | Other Academic | 69 | 0.571267 | 0.572842 | 0.128524 | 0.192 | 0.768116 | 0.753623 | 0.0144928 | 0.121294 | 0.506244 | 0.68075 | 0.825577 | 0.207613 |
| tossup_correctness | category | Philosophy | 324 | 0.678824 | 0.470369 | 0.0352024 | 0.150276 | 0.796296 | 0.799383 | -0.00308642 | 0.127621 | 0.610575 | 0.801652 | 0.915484 | 0.155786 |
| tossup_correctness | category | Popular Culture | 102 | 0.492042 | 0.52241 | 0.141108 | 0.170209 | 0.784314 | 0.833333 | -0.0490196 | 0.133971 | 0.563257 | 0.749028 | 0.87478 | 0.181697 |
| tossup_correctness | category | Religion | 372 | 0.666807 | 0.575307 | 0.0511526 | 0.195758 | 0.701613 | 0.709677 | -0.00806452 | 0.146565 | 0.533632 | 0.759089 | 0.89982 | 0.176731 |
| tossup_correctness | category | Science | 1487 | 0.675149 | 0.52366 | 0.0213515 | 0.172782 | 0.751177 | 0.752522 | -0.00134499 | 0.139402 | 0.540288 | 0.771241 | 0.894745 | 0.17199 |
| tossup_correctness | category | Social Science | 336 | 0.665636 | 0.573597 | 0.0234128 | 0.194902 | 0.702381 | 0.702381 | 0 | 0.125506 | 0.536747 | 0.73396 | 0.862745 | 0.188093 |
| tossup_correctness | category | Unknown | 1886 | 0.638577 | 0.548156 | 0.025417 | 0.182274 | 0.744963 | 0.746023 | -0.00106045 | 0.134391 | 0.55961 | 0.768786 | 0.90413 | 0.170798 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.60252 | 0.590977 | 0.0898989 | 0.199142 | 0.730964 | 0.736041 | -0.00507614 | 0.13797 | 0.496927 | 0.680558 | 0.829164 | 0.203497 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.636132 | 0.561785 | 0.0412096 | 0.18768 | 0.729949 | 0.735025 | -0.00507614 | 0.139887 | 0.512409 | 0.731017 | 0.864654 | 0.188225 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.657578 | 0.516339 | 0.0339941 | 0.168782 | 0.765882 | 0.769436 | -0.00355398 | 0.133001 | 0.552563 | 0.768668 | 0.891684 | 0.174525 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.660704 | 0.496963 | 0.0264417 | 0.160536 | 0.782973 | 0.78402 | -0.00104676 | 0.131603 | 0.581437 | 0.791963 | 0.913023 | 0.162318 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.656853 | 0.533857 | 0.0278693 | 0.174106 | 0.757677 | 0.756008 | 0.00166889 | 0.135286 | 0.578449 | 0.7964 | 0.927621 | 0.157187 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | -1.9584 | 1.27102 | -5.19152 | -3.65479 | -2.95812 | -2.25632 | -0.453789 | -0.0366955 | 1.13675 |
| player | theta_2 | 1186 | -1.30972 | 1.22235 | -4.79101 | -3.34329 | -2.42137 | -0.787291 | -0.282509 | 0.143369 | 1.25935 |
| player | theta_3 | 1186 | -0.590103 | 1.02778 | -4.20807 | -3.09171 | -0.488879 | -0.243282 | -0.0698835 | 0.296084 | 1.21131 |
| player | theta_norm | 1186 | 3.0708 | 0.795044 | 1.36248 | 1.89669 | 2.46719 | 3.02975 | 3.55488 | 4.51073 | 5.59245 |
| tossup | start_difficulty_d1 | 1240 | -1.82061 | 1.64676 | -6.18401 | -4.08112 | -3.38801 | -1.58042 | -0.183406 | 0.0787424 | 0.521054 |
| tossup | start_difficulty_d2 | 1240 | -0.880433 | 1.53243 | -5.303 | -3.9991 | -1.46297 | -0.166481 | 0.142965 | 0.578046 | 1.72447 |
| tossup | start_difficulty_d3 | 1240 | -0.860594 | 1.31897 | -3.71874 | -3.19555 | -2.43416 | -0.153347 | 0.0752854 | 0.370105 | 0.852648 |
| tossup | end_difficulty_d1 | 1240 | -2.94106 | 1.85523 | -11.0385 | -5.92862 | -4.42347 | -2.62437 | -1.18307 | -0.870736 | -0.309695 |
| tossup | end_difficulty_d2 | 1240 | -1.91387 | 1.61755 | -7.71126 | -5.17361 | -2.78569 | -1.16729 | -0.80805 | -0.271708 | 0.969052 |
| tossup | end_difficulty_d3 | 1240 | -1.93031 | 1.47925 | -6.94771 | -4.74571 | -3.39823 | -1.15771 | -0.891625 | -0.571938 | -0.0273643 |
| tossup | total_drop_d1 | 1240 | 1.12044 | 0.531363 | 0.373891 | 0.699417 | 0.926788 | 1.00374 | 1.10445 | 1.98087 | 7.55256 |
| tossup | total_drop_d2 | 1240 | 1.03343 | 0.281619 | 0.501656 | 0.719716 | 0.914945 | 0.981767 | 1.06968 | 1.49961 | 4.2108 |
| tossup | total_drop_d3 | 1240 | 1.06972 | 0.292791 | 0.581796 | 0.86474 | 0.951235 | 0.997162 | 1.0667 | 1.55577 | 4.20771 |
| tossup | drop_share_1_d1 | 1240 | 0.341696 | 0.054588 | 0.164082 | 0.290475 | 0.305815 | 0.319293 | 0.370689 | 0.450115 | 0.633294 |
| tossup | drop_share_2_d1 | 1240 | 0.339744 | 0.0211932 | 0.230334 | 0.308398 | 0.32854 | 0.340511 | 0.351111 | 0.368587 | 0.511251 |
| tossup | drop_share_3_d1 | 1240 | 0.31856 | 0.047372 | 0.128233 | 0.224885 | 0.295518 | 0.335448 | 0.349104 | 0.366644 | 0.492355 |
| tossup | drop_share_1_d2 | 1240 | 0.318075 | 0.0359803 | 0.203275 | 0.283603 | 0.300023 | 0.310022 | 0.326196 | 0.38469 | 0.673166 |
| tossup | drop_share_2_d2 | 1240 | 0.344763 | 0.0183564 | 0.217225 | 0.31431 | 0.33625 | 0.34562 | 0.354387 | 0.36775 | 0.463155 |
| tossup | drop_share_3_d2 | 1240 | 0.337162 | 0.0333154 | 0.109609 | 0.277066 | 0.327363 | 0.343185 | 0.354605 | 0.373574 | 0.484409 |
| tossup | drop_share_1_d3 | 1240 | 0.323321 | 0.0335929 | 0.247426 | 0.288608 | 0.302104 | 0.311877 | 0.33285 | 0.39878 | 0.496336 |
| tossup | drop_share_2_d3 | 1240 | 0.344597 | 0.0135371 | 0.301641 | 0.32281 | 0.336361 | 0.34456 | 0.352774 | 0.365224 | 0.412934 |
| tossup | drop_share_3_d3 | 1240 | 0.332083 | 0.0316224 | 0.186985 | 0.26369 | 0.322986 | 0.341679 | 0.353118 | 0.365519 | 0.40825 |
| tossup | r_1 | 1240 | 0.477127 | 0.387713 | 0.0148233 | 0.0340002 | 0.0683494 | 0.489259 | 0.871204 | 0.931767 | 0.975377 |
| tossup | r_2 | 1240 | 0.250936 | 0.324641 | 0.0137582 | 0.0299083 | 0.0506736 | 0.0862717 | 0.207327 | 0.935191 | 0.975882 |
| tossup | r_3 | 1240 | 0.271937 | 0.328178 | 0.0074056 | 0.020654 | 0.0423393 | 0.0726992 | 0.685211 | 0.863423 | 0.932061 |
| tossup | r_norm | 1240 | 0.850217 | 0.0694592 | 0.620042 | 0.728565 | 0.800637 | 0.856708 | 0.905731 | 0.949751 | 0.976039 |
