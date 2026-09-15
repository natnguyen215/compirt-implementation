# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_2/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_2/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 310088 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.624508 |
| log_loss | 0.534808 |
| ece | 0.0401774 |
| brier | 0.175125 |
| accuracy | 0.760409 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.00484131 |
| probability_std | 0.131828 |
| probability_p10 | 0.577509 |
| probability_p50 | 0.785159 |
| probability_p90 | 0.908936 |
| mean_predictive_variance | 0.164965 |
| integrated_brier_score | 0.103709 |
| joint_tossup_event_log_loss | 6.97249 |
| buzz_position_mae | 0.162414 |
| buzz_position_median_absolute_error | 0.149089 |
| buzz_position_bias | -0.0649313 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.334158 |
| first_buzzer_mean_reciprocal_rank | 0.550878 |
| first_buzzer_log_loss | 1.70197 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.63206 |
| tossup_scorer_player_top1_accuracy | 0.303503 |
| tossup_scorer_team_top1_accuracy | 0.470276 |
| tossup_game_winner_accuracy | 0.788546 |
| tossup_game_margin_mae | 34.5952 |
| tournament_player_ppg_spearman | 0.679022 |
| tournament_player_ppg_mae | 9.13949 |
| tournament_player_ppg_top10_overlap | 0.648276 |
| neg_auroc | 0.624508 |
| neg_average_precision | 0.341518 |
| neg_precision | 0.449664 |
| neg_recall | 0.0921173 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0574527 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0925886 |
| no_buzz_calibration_error | 0.079319 |
| no_buzz_brier | 0.0253783 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| tossup_correctness | aggregate | all | 9295 | 0.624508 | 0.534808 | 0.0401774 | 0.175125 | 0.760409 | 0.76525 | -0.00484131 | 0.131828 | 0.577509 | 0.785159 | 0.908936 | 0.164965 |
| tossup_correctness | tier | fall | 2933 | 0.604106 | 0.512843 | 0.0463888 | 0.164154 | 0.786567 | 0.791681 | -0.00511422 | 0.122366 | 0.610553 | 0.805105 | 0.918291 | 0.155401 |
| tossup_correctness | tier | nationals | 1584 | 0.643538 | 0.570856 | 0.0588426 | 0.192884 | 0.710227 | 0.724747 | -0.0145202 | 0.142941 | 0.476593 | 0.69379 | 0.854897 | 0.19761 |
| tossup_correctness | tier | regionals | 1886 | 0.610513 | 0.563931 | 0.0548955 | 0.187909 | 0.741251 | 0.746023 | -0.004772 | 0.124366 | 0.604907 | 0.793167 | 0.91447 | 0.15998 |
| tossup_correctness | tier | winter | 2892 | 0.63195 | 0.518347 | 0.032622 | 0.168189 | 0.773859 | 0.773167 | 0.000691563 | 0.122379 | 0.610143 | 0.798435 | 0.909407 | 0.160035 |
| tossup_correctness | category | Current Events | 124 | 0.61984 | 0.558842 | 0.081465 | 0.187783 | 0.701613 | 0.75 | -0.0483871 | 0.126235 | 0.490223 | 0.708852 | 0.82326 | 0.203881 |
| tossup_correctness | category | Fine Arts | 1103 | 0.596244 | 0.551732 | 0.051085 | 0.180295 | 0.759746 | 0.759746 | 0 | 0.114628 | 0.629956 | 0.804246 | 0.911443 | 0.156144 |
| tossup_correctness | category | Geography | 197 | 0.700233 | 0.57949 | 0.0520373 | 0.1985 | 0.695431 | 0.670051 | 0.0253807 | 0.146602 | 0.489737 | 0.729719 | 0.865684 | 0.190116 |
| tossup_correctness | category | History | 1491 | 0.654923 | 0.503185 | 0.0620722 | 0.162715 | 0.780684 | 0.787391 | -0.00670691 | 0.131507 | 0.541691 | 0.752499 | 0.881723 | 0.180499 |
| tossup_correctness | category | Literature | 1472 | 0.595111 | 0.502072 | 0.0498394 | 0.157416 | 0.80163 | 0.804348 | -0.00271739 | 0.104916 | 0.684243 | 0.855105 | 0.941472 | 0.128719 |
| tossup_correctness | category | Mythology | 332 | 0.686858 | 0.470675 | 0.0885891 | 0.151226 | 0.789157 | 0.813253 | -0.0240964 | 0.125016 | 0.566084 | 0.742127 | 0.876327 | 0.182346 |
| tossup_correctness | category | Other Academic | 69 | 0.5 | 0.58254 | 0.157614 | 0.194356 | 0.797101 | 0.753623 | 0.0434783 | 0.113957 | 0.514364 | 0.692531 | 0.814345 | 0.204661 |
| tossup_correctness | category | Philosophy | 324 | 0.648946 | 0.481183 | 0.025117 | 0.152986 | 0.796296 | 0.799383 | -0.00308642 | 0.116499 | 0.640466 | 0.81668 | 0.910946 | 0.151949 |
| tossup_correctness | category | Popular Culture | 102 | 0.468512 | 0.566028 | 0.170389 | 0.18914 | 0.754902 | 0.833333 | -0.0784314 | 0.146168 | 0.51812 | 0.710157 | 0.839279 | 0.194335 |
| tossup_correctness | category | Religion | 372 | 0.647832 | 0.585023 | 0.0687497 | 0.198358 | 0.696237 | 0.709677 | -0.0134409 | 0.139437 | 0.55465 | 0.780392 | 0.900803 | 0.168238 |
| tossup_correctness | category | Science | 1487 | 0.652859 | 0.536659 | 0.0369722 | 0.176938 | 0.750504 | 0.752522 | -0.00201748 | 0.139129 | 0.518811 | 0.75093 | 0.876335 | 0.181276 |
| tossup_correctness | category | Social Science | 336 | 0.604153 | 0.596456 | 0.0513745 | 0.203695 | 0.705357 | 0.702381 | 0.00297619 | 0.120994 | 0.570375 | 0.738 | 0.860524 | 0.185152 |
| tossup_correctness | category | Unknown | 1886 | 0.610513 | 0.563931 | 0.0548955 | 0.187909 | 0.741251 | 0.746023 | -0.004772 | 0.124366 | 0.604907 | 0.793167 | 0.91447 | 0.15998 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.572414 | 0.60509 | 0.0948208 | 0.206153 | 0.700508 | 0.736041 | -0.035533 | 0.140954 | 0.480293 | 0.686601 | 0.82683 | 0.202559 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.585265 | 0.587318 | 0.0806039 | 0.197667 | 0.723858 | 0.735025 | -0.0111675 | 0.135964 | 0.512037 | 0.711716 | 0.859438 | 0.192984 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.619152 | 0.531154 | 0.0415843 | 0.174252 | 0.763216 | 0.769436 | -0.00621946 | 0.125842 | 0.567669 | 0.770387 | 0.878918 | 0.175429 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.643635 | 0.501918 | 0.0284352 | 0.161739 | 0.784717 | 0.78402 | 0.000697837 | 0.124062 | 0.599568 | 0.796705 | 0.909013 | 0.160364 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.633871 | 0.547131 | 0.0495161 | 0.179136 | 0.751001 | 0.756008 | -0.00500668 | 0.129556 | 0.611494 | 0.816308 | 0.927733 | 0.14982 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | -2.33823 | 0.662439 | -4.74022 | -3.4514 | -2.7552 | -2.3136 | -1.8873 | -1.28731 | 0.403921 |
| player | theta_2 | 1186 | -1.65381 | 0.889161 | -4.36925 | -3.12358 | -2.30446 | -1.64635 | -0.906157 | -0.369502 | 0.28707 |
| player | theta_norm | 1186 | 2.99856 | 0.663208 | 1.26063 | 1.98252 | 2.53104 | 2.95832 | 3.42136 | 4.15468 | 5.30266 |
| tossup | start_difficulty_d1 | 1240 | -2.34989 | 1.14855 | -4.57703 | -3.7522 | -3.26273 | -2.7317 | -1.43012 | -0.218192 | 0.422939 |
| tossup | start_difficulty_d2 | 1240 | -1.9137 | 1.20538 | -4.61685 | -3.72347 | -2.84455 | -2.18182 | -0.852586 | 0.031311 | 2.12245 |
| tossup | end_difficulty_d1 | 1240 | -3.41173 | 1.25795 | -7.69559 | -5.17058 | -4.31428 | -3.6565 | -2.4746 | -1.18878 | -0.457534 |
| tossup | end_difficulty_d2 | 1240 | -2.98531 | 1.35859 | -8.66604 | -5.12527 | -3.93065 | -3.13083 | -1.86062 | -0.871378 | 1.38879 |
| tossup | total_drop_d1 | 1240 | 1.06184 | 0.391388 | 0.347353 | 0.664458 | 0.850477 | 0.985315 | 1.14822 | 1.82036 | 4.33158 |
| tossup | total_drop_d2 | 1240 | 1.07161 | 0.346721 | 0.516323 | 0.70667 | 0.902115 | 0.993212 | 1.14531 | 1.65894 | 4.80028 |
| tossup | drop_share_1_d1 | 1240 | 0.353348 | 0.0491577 | 0.182272 | 0.295269 | 0.320097 | 0.341956 | 0.37945 | 0.448457 | 0.631784 |
| tossup | drop_share_2_d1 | 1240 | 0.337264 | 0.0203745 | 0.23482 | 0.306685 | 0.324302 | 0.338137 | 0.348934 | 0.367323 | 0.527023 |
| tossup | drop_share_3_d1 | 1240 | 0.309388 | 0.044878 | 0.133397 | 0.223136 | 0.284299 | 0.315713 | 0.339227 | 0.369095 | 0.483422 |
| tossup | drop_share_1_d2 | 1240 | 0.34385 | 0.0444957 | 0.195096 | 0.293043 | 0.315174 | 0.334539 | 0.365939 | 0.42632 | 0.695214 |
| tossup | drop_share_2_d2 | 1240 | 0.339784 | 0.0169878 | 0.202183 | 0.310697 | 0.330731 | 0.341285 | 0.349323 | 0.36256 | 0.415368 |
| tossup | drop_share_3_d2 | 1240 | 0.316366 | 0.0414884 | 0.102603 | 0.23949 | 0.292219 | 0.322567 | 0.342869 | 0.371925 | 0.455878 |
| tossup | r_1 | 1240 | 0.56711 | 0.322991 | 0.0350405 | 0.082369 | 0.246882 | 0.653353 | 0.886178 | 0.94698 | 0.971361 |
| tossup | r_2 | 1240 | 0.43289 | 0.322991 | 0.028639 | 0.0530199 | 0.113822 | 0.346647 | 0.753118 | 0.917631 | 0.964959 |
| tossup | r_norm | 1240 | 0.843473 | 0.0777415 | 0.707108 | 0.711241 | 0.778127 | 0.851698 | 0.910837 | 0.951219 | 0.971783 |
