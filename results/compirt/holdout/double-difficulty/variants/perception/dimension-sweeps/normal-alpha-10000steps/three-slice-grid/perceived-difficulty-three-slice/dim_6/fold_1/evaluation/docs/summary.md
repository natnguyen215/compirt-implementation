# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_6/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_6/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 322819 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.656053 |
| log_loss | 0.52294 |
| ece | 0.0268204 |
| brier | 0.170601 |
| accuracy | 0.764654 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00252942 |
| probability_std | 0.130847 |
| probability_p10 | 0.575987 |
| probability_p50 | 0.784894 |
| probability_p90 | 0.910285 |
| mean_predictive_variance | 0.164265 |
| integrated_brier_score | 0.100138 |
| joint_tossup_event_log_loss | 6.88489 |
| buzz_position_mae | 0.160255 |
| buzz_position_median_absolute_error | 0.145667 |
| buzz_position_bias | -0.0679996 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.344661 |
| first_buzzer_mean_reciprocal_rank | 0.557887 |
| first_buzzer_log_loss | 1.68853 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.640273 |
| tossup_scorer_player_top1_accuracy | 0.318615 |
| tossup_scorer_team_top1_accuracy | 0.491017 |
| tossup_game_winner_accuracy | 0.772523 |
| tossup_game_margin_mae | 33.9018 |
| tournament_player_ppg_spearman | 0.677856 |
| tournament_player_ppg_mae | 8.79414 |
| tournament_player_ppg_top10_overlap | 0.651724 |
| neg_auroc | 0.656053 |
| neg_average_precision | 0.387387 |
| neg_precision | 0.528536 |
| neg_recall | 0.0984743 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0567792 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0942014 |
| no_buzz_calibration_error | 0.0782923 |
| no_buzz_brier | 0.0276599 |
| full_pmf_max_mass_error | 1.55431e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.656053 | 0.52294 | 0.0268204 | 0.170601 | 0.764654 | 0.762125 | 0.00252942 | 0.130847 | 0.575987 | 0.784894 | 0.910285 | 0.164265 |
| tossup_correctness | tier | fall | 2842 | 0.685566 | 0.482249 | 0.0103145 | 0.155109 | 0.788177 | 0.785362 | 0.00281492 | 0.114139 | 0.629724 | 0.817125 | 0.917327 | 0.151027 |
| tossup_correctness | tier | nationals | 1564 | 0.659365 | 0.568324 | 0.0496961 | 0.190636 | 0.721228 | 0.718031 | 0.00319693 | 0.129005 | 0.503383 | 0.685546 | 0.832481 | 0.20302 |
| tossup_correctness | tier | regionals | 1937 | 0.627524 | 0.536116 | 0.0384398 | 0.176235 | 0.759422 | 0.758389 | 0.00103252 | 0.123934 | 0.58448 | 0.776065 | 0.894221 | 0.169839 |
| tossup_correctness | tier | winter | 2750 | 0.642013 | 0.529901 | 0.0305719 | 0.171248 | 0.768727 | 0.765818 | 0.00290909 | 0.130059 | 0.597516 | 0.814889 | 0.927769 | 0.151979 |
| tossup_correctness | category | Current Events | 126 | 0.69321 | 0.522257 | 0.0919123 | 0.171305 | 0.761905 | 0.769841 | -0.00793651 | 0.123796 | 0.512572 | 0.694348 | 0.836317 | 0.200879 |
| tossup_correctness | category | Fine Arts | 1071 | 0.659245 | 0.515138 | 0.0325038 | 0.167735 | 0.779645 | 0.766573 | 0.0130719 | 0.135172 | 0.575854 | 0.783665 | 0.911844 | 0.163003 |
| tossup_correctness | category | Geography | 185 | 0.694491 | 0.558628 | 0.0575746 | 0.188057 | 0.708108 | 0.697297 | 0.0108108 | 0.151755 | 0.470736 | 0.71251 | 0.862286 | 0.19443 |
| tossup_correctness | category | History | 1440 | 0.675167 | 0.521376 | 0.0153759 | 0.171602 | 0.755556 | 0.754167 | 0.00138889 | 0.127878 | 0.556657 | 0.768194 | 0.886678 | 0.174379 |
| tossup_correctness | category | Literature | 1422 | 0.606509 | 0.48382 | 0.0491949 | 0.150076 | 0.812236 | 0.814346 | -0.0021097 | 0.114259 | 0.651561 | 0.847774 | 0.944517 | 0.133368 |
| tossup_correctness | category | Mythology | 318 | 0.689005 | 0.487991 | 0.0713262 | 0.156663 | 0.779874 | 0.789308 | -0.00943396 | 0.126497 | 0.573663 | 0.769671 | 0.901792 | 0.171903 |
| tossup_correctness | category | Other Academic | 66 | 0.617021 | 0.581111 | 0.0754756 | 0.195953 | 0.727273 | 0.712121 | 0.0151515 | 0.115118 | 0.534949 | 0.710624 | 0.847059 | 0.201074 |
| tossup_correctness | category | Philosophy | 311 | 0.675087 | 0.537156 | 0.0594128 | 0.177487 | 0.736334 | 0.745981 | -0.0096463 | 0.125743 | 0.618269 | 0.803252 | 0.92488 | 0.15542 |
| tossup_correctness | category | Popular Culture | 102 | 0.637037 | 0.400236 | 0.12791 | 0.118186 | 0.882353 | 0.882353 | 0 | 0.114548 | 0.610963 | 0.764712 | 0.878295 | 0.172138 |
| tossup_correctness | category | Religion | 358 | 0.662364 | 0.569778 | 0.0359913 | 0.19229 | 0.712291 | 0.712291 | 0 | 0.128108 | 0.55281 | 0.765001 | 0.889997 | 0.175299 |
| tossup_correctness | category | Science | 1433 | 0.670374 | 0.541623 | 0.0358001 | 0.178997 | 0.740405 | 0.738311 | 0.00209351 | 0.136221 | 0.555296 | 0.795229 | 0.909482 | 0.162804 |
| tossup_correctness | category | Social Science | 324 | 0.668801 | 0.541551 | 0.0460108 | 0.179096 | 0.759259 | 0.731481 | 0.0277778 | 0.121512 | 0.579566 | 0.753635 | 0.873211 | 0.179594 |
| tossup_correctness | category | Unknown | 1937 | 0.627524 | 0.536116 | 0.0384398 | 0.176235 | 0.759422 | 0.758389 | 0.00103252 | 0.123934 | 0.58448 | 0.776065 | 0.894221 | 0.169839 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.615021 | 0.59222 | 0.0684255 | 0.199675 | 0.718563 | 0.712575 | 0.00598802 | 0.119627 | 0.549036 | 0.725476 | 0.851011 | 0.193892 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.673222 | 0.548845 | 0.0317983 | 0.182355 | 0.735746 | 0.729167 | 0.00657895 | 0.136995 | 0.515641 | 0.739977 | 0.866352 | 0.187071 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.663214 | 0.52436 | 0.0135448 | 0.172373 | 0.760284 | 0.755083 | 0.00520095 | 0.126068 | 0.575498 | 0.775511 | 0.891462 | 0.170925 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.649647 | 0.503857 | 0.0316662 | 0.163083 | 0.779887 | 0.780942 | -0.00105485 | 0.124941 | 0.599895 | 0.798486 | 0.912279 | 0.159533 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.651464 | 0.528202 | 0.0352521 | 0.171274 | 0.764648 | 0.762029 | 0.00261866 | 0.132764 | 0.585871 | 0.800381 | 0.92849 | 0.155633 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | -0.691126 | 1.08348 | -4.71376 | -3.37401 | -0.456756 | -0.245428 | -0.138651 | -0.0135834 | 0.162749 |
| player | theta_2 | 1167 | -1.02399 | 1.25732 | -5.03847 | -3.49871 | -2.11258 | -0.291262 | -0.156335 | -0.0318548 | 0.245183 |
| player | theta_3 | 1167 | -1.27209 | 1.24035 | -4.5635 | -3.42042 | -2.42744 | -0.657052 | -0.256578 | 0.122686 | 1.41196 |
| player | theta_4 | 1167 | -1.41565 | 1.32712 | -5.17532 | -3.58393 | -2.58024 | -0.829069 | -0.215124 | 0.046176 | 0.985591 |
| player | theta_5 | 1167 | -0.339293 | 0.42468 | -1.93653 | -1.06387 | -0.559845 | -0.32017 | -0.13706 | 0.351051 | 1.62959 |
| player | theta_6 | 1167 | -0.251235 | 0.302111 | -1.63148 | -0.725488 | -0.398509 | -0.246112 | -0.108474 | 0.253337 | 1.08562 |
| player | theta_norm | 1167 | 3.27891 | 0.947066 | 1.2634 | 1.97604 | 2.53159 | 3.16842 | 3.90657 | 4.99344 | 7.08395 |
| tossup | start_difficulty_d1 | 1220 | -0.984079 | 1.46186 | -4.44306 | -3.60002 | -2.75583 | -0.13251 | 0.0389512 | 0.193519 | 0.510614 |
| tossup | start_difficulty_d2 | 1220 | -0.948935 | 1.52606 | -4.70194 | -3.91935 | -0.808751 | -0.142696 | 0.0190616 | 0.146255 | 0.442005 |
| tossup | start_difficulty_d3 | 1220 | -0.864771 | 1.6125 | -5.51437 | -4.28647 | -0.570458 | -0.0570463 | 0.0814397 | 0.232841 | 0.46292 |
| tossup | start_difficulty_d4 | 1220 | -1.02167 | 1.65219 | -5.83626 | -4.32402 | -1.0556 | -0.158433 | 0.055105 | 0.220759 | 0.527867 |
| tossup | start_difficulty_d5 | 1220 | -0.105676 | 0.530071 | -2.06914 | -1.36032 | -0.237709 | 0.0614169 | 0.231295 | 0.439237 | 0.939559 |
| tossup | start_difficulty_d6 | 1220 | -0.00575437 | 0.248772 | -1.65167 | -0.462633 | -0.0927059 | 0.0318453 | 0.153865 | 0.296391 | 0.583463 |
| tossup | end_difficulty_d1 | 1220 | -2.07088 | 1.64463 | -7.92291 | -5.16177 | -3.67172 | -1.13714 | -0.944427 | -0.763225 | -0.417901 |
| tossup | end_difficulty_d2 | 1220 | -2.00924 | 1.68406 | -10.2619 | -5.37987 | -1.93579 | -1.14367 | -0.965082 | -0.816001 | -0.462524 |
| tossup | end_difficulty_d3 | 1220 | -1.88281 | 1.66922 | -8.02702 | -5.52543 | -1.65736 | -1.06401 | -0.903246 | -0.713481 | -0.453349 |
| tossup | end_difficulty_d4 | 1220 | -2.06684 | 1.77212 | -10.2027 | -5.70373 | -2.2624 | -1.1669 | -0.917602 | -0.722136 | -0.37687 |
| tossup | end_difficulty_d5 | 1220 | -1.13333 | 0.66799 | -4.20412 | -2.7088 | -1.25868 | -0.920338 | -0.722739 | -0.485021 | 0.0433061 |
| tossup | end_difficulty_d6 | 1220 | -1.00329 | 0.29145 | -2.81751 | -1.51099 | -1.11568 | -0.959858 | -0.819024 | -0.658269 | -0.296484 |
| tossup | total_drop_d1 | 1220 | 1.08681 | 0.323972 | 0.586052 | 0.883881 | 0.963694 | 1.00435 | 1.05848 | 1.64454 | 4.5071 |
| tossup | total_drop_d2 | 1220 | 1.0603 | 0.348555 | 0.495887 | 0.830274 | 0.960906 | 0.996129 | 1.04254 | 1.51852 | 6.24626 |
| tossup | total_drop_d3 | 1220 | 1.01804 | 0.240214 | 0.542014 | 0.740724 | 0.949474 | 0.989349 | 1.03651 | 1.26064 | 4.01375 |
| tossup | total_drop_d4 | 1220 | 1.04518 | 0.32067 | 0.388343 | 0.758624 | 0.948892 | 0.993656 | 1.047 | 1.52038 | 6.02177 |
| tossup | total_drop_d5 | 1220 | 1.02766 | 0.153176 | 0.843754 | 0.896092 | 0.943988 | 0.985056 | 1.04522 | 1.33925 | 2.29801 |
| tossup | total_drop_d6 | 1220 | 0.997537 | 0.0565049 | 0.854435 | 0.915031 | 0.961351 | 0.991743 | 1.02713 | 1.09488 | 1.26948 |
| tossup | drop_share_1_d1 | 1220 | 0.328769 | 0.0431121 | 0.258078 | 0.289542 | 0.301821 | 0.31172 | 0.341504 | 0.416382 | 0.591583 |
| tossup | drop_share_2_d1 | 1220 | 0.344244 | 0.0149567 | 0.26156 | 0.319529 | 0.336269 | 0.345124 | 0.353344 | 0.365738 | 0.43394 |
| tossup | drop_share_3_d1 | 1220 | 0.326986 | 0.03868 | 0.146857 | 0.241831 | 0.319581 | 0.341349 | 0.351072 | 0.362676 | 0.401644 |
| tossup | drop_share_1_d2 | 1220 | 0.327587 | 0.0451187 | 0.229382 | 0.290561 | 0.302369 | 0.311703 | 0.327887 | 0.423198 | 0.649879 |
| tossup | drop_share_2_d2 | 1220 | 0.342809 | 0.0158379 | 0.221507 | 0.315873 | 0.335245 | 0.344048 | 0.352482 | 0.363338 | 0.437486 |
| tossup | drop_share_3_d2 | 1220 | 0.329604 | 0.0379565 | 0.128615 | 0.243584 | 0.327834 | 0.341881 | 0.350995 | 0.362735 | 0.422844 |
| tossup | drop_share_1_d3 | 1220 | 0.319013 | 0.0380795 | 0.197155 | 0.287785 | 0.30088 | 0.309401 | 0.320192 | 0.400524 | 0.594301 |
| tossup | drop_share_2_d3 | 1220 | 0.343765 | 0.0179317 | 0.250558 | 0.311677 | 0.3356 | 0.344869 | 0.353508 | 0.366971 | 0.434199 |
| tossup | drop_share_3_d3 | 1220 | 0.337223 | 0.0333446 | 0.138558 | 0.263807 | 0.332901 | 0.344335 | 0.353645 | 0.367413 | 0.475254 |
| tossup | drop_share_1_d4 | 1220 | 0.327518 | 0.050332 | 0.218778 | 0.291007 | 0.30145 | 0.31116 | 0.325195 | 0.433676 | 0.737883 |
| tossup | drop_share_2_d4 | 1220 | 0.341718 | 0.0201023 | 0.165404 | 0.304711 | 0.334215 | 0.343631 | 0.352994 | 0.365754 | 0.510297 |
| tossup | drop_share_3_d4 | 1220 | 0.330764 | 0.0411464 | 0.0967131 | 0.234904 | 0.32841 | 0.342658 | 0.353017 | 0.36477 | 0.463946 |
| tossup | drop_share_1_d5 | 1220 | 0.307973 | 0.0141197 | 0.273937 | 0.288467 | 0.298458 | 0.306728 | 0.315323 | 0.335034 | 0.379698 |
| tossup | drop_share_2_d5 | 1220 | 0.347953 | 0.0109761 | 0.307215 | 0.32999 | 0.340338 | 0.347931 | 0.355718 | 0.365631 | 0.38538 |
| tossup | drop_share_3_d5 | 1220 | 0.344074 | 0.0152626 | 0.257312 | 0.316513 | 0.336234 | 0.345477 | 0.354027 | 0.365885 | 0.381931 |
| tossup | drop_share_1_d6 | 1220 | 0.306425 | 0.0113057 | 0.2724 | 0.28761 | 0.298711 | 0.306079 | 0.31384 | 0.325259 | 0.35031 |
| tossup | drop_share_2_d6 | 1220 | 0.346769 | 0.010694 | 0.313133 | 0.329305 | 0.339464 | 0.34662 | 0.354316 | 0.364063 | 0.37998 |
| tossup | drop_share_3_d6 | 1220 | 0.346806 | 0.0112263 | 0.307013 | 0.327723 | 0.339791 | 0.346968 | 0.354529 | 0.364623 | 0.386758 |
| tossup | r_1 | 1220 | 0.210115 | 0.267509 | 0.00983124 | 0.0198693 | 0.0312481 | 0.0436688 | 0.554777 | 0.688086 | 0.793067 |
| tossup | r_2 | 1220 | 0.212438 | 0.286257 | 0.0107552 | 0.0221898 | 0.0338792 | 0.0567017 | 0.131465 | 0.767021 | 0.882456 |
| tossup | r_3 | 1220 | 0.207452 | 0.292352 | 0.0125692 | 0.0233866 | 0.038997 | 0.0560415 | 0.132482 | 0.831528 | 0.934688 |
| tossup | r_4 | 1220 | 0.24381 | 0.31344 | 0.0167957 | 0.030714 | 0.0487765 | 0.0698808 | 0.192912 | 0.848215 | 0.943265 |
| tossup | r_5 | 1220 | 0.0672307 | 0.0418854 | 0.0106133 | 0.0244927 | 0.041077 | 0.0551639 | 0.0773048 | 0.16394 | 0.245354 |
| tossup | r_6 | 1220 | 0.0589531 | 0.0304526 | 0.010237 | 0.0226404 | 0.0376782 | 0.0533005 | 0.0725567 | 0.115109 | 0.23584 |
| tossup | r_norm | 1220 | 0.729336 | 0.086313 | 0.494809 | 0.596104 | 0.65921 | 0.730091 | 0.793036 | 0.875031 | 0.943609 |
