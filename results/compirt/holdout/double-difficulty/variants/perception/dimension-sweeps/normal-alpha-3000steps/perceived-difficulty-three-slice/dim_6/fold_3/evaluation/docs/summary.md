# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_6/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_6/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 326187 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.666696 |
| log_loss | 0.507506 |
| ece | 0.0214079 |
| brier | 0.164469 |
| accuracy | 0.773899 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00385463 |
| probability_std | 0.122317 |
| probability_p10 | 0.593332 |
| probability_p50 | 0.78304 |
| probability_p90 | 0.902615 |
| mean_predictive_variance | 0.16579 |
| integrated_brier_score | 0.100379 |
| joint_tossup_event_log_loss | 6.83639 |
| buzz_position_mae | 0.159723 |
| buzz_position_median_absolute_error | 0.145222 |
| buzz_position_bias | -0.0677459 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.361784 |
| first_buzzer_mean_reciprocal_rank | 0.572549 |
| first_buzzer_log_loss | 1.66273 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.662115 |
| tossup_scorer_player_top1_accuracy | 0.321367 |
| tossup_scorer_team_top1_accuracy | 0.510954 |
| tossup_game_winner_accuracy | 0.803097 |
| tossup_game_margin_mae | 35.6575 |
| tournament_player_ppg_spearman | 0.71231 |
| tournament_player_ppg_mae | 8.90446 |
| tournament_player_ppg_top10_overlap | 0.672414 |
| neg_auroc | 0.666696 |
| neg_average_precision | 0.398354 |
| neg_precision | 0.55287 |
| neg_recall | 0.0876437 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0554334 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0929333 |
| no_buzz_calibration_error | 0.0777489 |
| no_buzz_brier | 0.0263363 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9220 |
| first_buzzer_team_top1_accuracy_events | 9080 |
| tossup_scorer_player_top1_accuracy_events | 9220 |
| tossup_scorer_team_top1_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 452 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.666696 | 0.507506 | 0.0214079 | 0.164469 | 0.773899 | 0.770044 | 0.00385463 | 0.122317 | 0.593332 | 0.78304 | 0.902615 | 0.16579 |
| tossup_correctness | tier | fall | 2817 | 0.657738 | 0.495321 | 0.0209203 | 0.159274 | 0.784878 | 0.781683 | 0.00319489 | 0.116298 | 0.611803 | 0.798707 | 0.900337 | 0.161271 |
| tossup_correctness | tier | nationals | 1542 | 0.715572 | 0.537493 | 0.0689639 | 0.178377 | 0.738651 | 0.73476 | 0.00389105 | 0.116511 | 0.507695 | 0.680341 | 0.810501 | 0.207489 |
| tossup_correctness | tier | regionals | 1934 | 0.658768 | 0.525235 | 0.0153094 | 0.172557 | 0.759566 | 0.75698 | 0.00258532 | 0.0969738 | 0.634944 | 0.777003 | 0.875486 | 0.170878 |
| tossup_correctness | tier | winter | 2787 | 0.659223 | 0.490929 | 0.0220196 | 0.156412 | 0.79225 | 0.786868 | 0.00538213 | 0.120623 | 0.643006 | 0.829859 | 0.927522 | 0.143756 |
| tossup_correctness | category | Current Events | 125 | 0.719595 | 0.547998 | 0.103176 | 0.18365 | 0.728 | 0.704 | 0.024 | 0.120998 | 0.521504 | 0.713333 | 0.823995 | 0.199791 |
| tossup_correctness | category | Fine Arts | 1072 | 0.674103 | 0.502164 | 0.0316099 | 0.162971 | 0.772388 | 0.770522 | 0.00186567 | 0.126667 | 0.586329 | 0.78934 | 0.906549 | 0.163351 |
| tossup_correctness | category | Geography | 185 | 0.761678 | 0.519383 | 0.0505324 | 0.171484 | 0.756757 | 0.702703 | 0.0540541 | 0.161435 | 0.418957 | 0.720815 | 0.865678 | 0.192474 |
| tossup_correctness | category | History | 1443 | 0.705579 | 0.499661 | 0.0423397 | 0.162267 | 0.769924 | 0.765073 | 0.004851 | 0.125794 | 0.555668 | 0.74674 | 0.87418 | 0.18172 |
| tossup_correctness | category | Literature | 1411 | 0.59891 | 0.484209 | 0.0454002 | 0.151107 | 0.80652 | 0.81219 | -0.00566974 | 0.112822 | 0.655389 | 0.839812 | 0.934539 | 0.138735 |
| tossup_correctness | category | Mythology | 320 | 0.59592 | 0.507255 | 0.0855916 | 0.161567 | 0.80625 | 0.79375 | 0.0125 | 0.115664 | 0.580854 | 0.78006 | 0.880151 | 0.171732 |
| tossup_correctness | category | Other Academic | 64 | 0.601562 | 0.553627 | 0.0736771 | 0.183884 | 0.78125 | 0.75 | 0.03125 | 0.101844 | 0.58115 | 0.703116 | 0.852885 | 0.197215 |
| tossup_correctness | category | Philosophy | 312 | 0.585161 | 0.498647 | 0.0535207 | 0.158848 | 0.807692 | 0.801282 | 0.00641026 | 0.116567 | 0.608773 | 0.805352 | 0.901963 | 0.158369 |
| tossup_correctness | category | Popular Culture | 104 | 0.549716 | 0.451375 | 0.0866787 | 0.138343 | 0.836538 | 0.846154 | -0.00961538 | 0.0974204 | 0.639016 | 0.794435 | 0.898729 | 0.163697 |
| tossup_correctness | category | Religion | 358 | 0.681201 | 0.549217 | 0.0400657 | 0.183925 | 0.717877 | 0.726257 | -0.00837989 | 0.13172 | 0.560472 | 0.752168 | 0.901362 | 0.177283 |
| tossup_correctness | category | Science | 1431 | 0.686032 | 0.50267 | 0.0229144 | 0.163231 | 0.774983 | 0.765199 | 0.00978337 | 0.127035 | 0.602218 | 0.803147 | 0.915542 | 0.157727 |
| tossup_correctness | category | Social Science | 321 | 0.690019 | 0.526484 | 0.0404089 | 0.174638 | 0.738318 | 0.744548 | -0.00623053 | 0.124775 | 0.563755 | 0.73624 | 0.878562 | 0.180799 |
| tossup_correctness | category | Unknown | 1934 | 0.658768 | 0.525235 | 0.0153094 | 0.172557 | 0.759566 | 0.75698 | 0.00258532 | 0.0969738 | 0.634944 | 0.777003 | 0.875486 | 0.170878 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.694416 | 0.56909 | 0.0482668 | 0.192939 | 0.703125 | 0.697917 | 0.00520833 | 0.12302 | 0.512729 | 0.68236 | 0.809356 | 0.206993 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.700008 | 0.530144 | 0.0319893 | 0.175981 | 0.742407 | 0.733408 | 0.00899888 | 0.1308 | 0.530982 | 0.734187 | 0.86033 | 0.1883 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.646942 | 0.528691 | 0.0208584 | 0.172861 | 0.760181 | 0.759276 | 0.000904977 | 0.121117 | 0.582418 | 0.774077 | 0.888621 | 0.171687 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.652955 | 0.490217 | 0.0290444 | 0.156847 | 0.792959 | 0.789125 | 0.00383409 | 0.114264 | 0.617659 | 0.794744 | 0.905534 | 0.1613 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.673837 | 0.497518 | 0.0277422 | 0.160229 | 0.779795 | 0.775342 | 0.00445205 | 0.119917 | 0.617247 | 0.803179 | 0.916088 | 0.156175 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | -0.800178 | 1.02179 | -4.75866 | -3.28513 | -0.663165 | -0.39775 | -0.247636 | -0.0583654 | 0.445994 |
| player | theta_2 | 1133 | -1.2462 | 1.06862 | -4.43679 | -3.20415 | -2.14489 | -0.818195 | -0.350404 | -0.105527 | 0.510696 |
| player | theta_3 | 1133 | -0.60941 | 0.38463 | -1.98394 | -1.38317 | -0.823536 | -0.539755 | -0.335122 | -0.110733 | 0.79648 |
| player | theta_4 | 1133 | -2.44598 | 0.756786 | -5.1713 | -3.63948 | -2.93424 | -2.4641 | -2.0268 | -0.958173 | -0.14103 |
| player | theta_5 | 1133 | -0.605046 | 0.400721 | -2.3483 | -1.29759 | -0.823341 | -0.576577 | -0.35921 | 0.00613562 | 0.939602 |
| player | theta_6 | 1133 | -0.480269 | 0.323029 | -1.95586 | -1.08711 | -0.660108 | -0.427679 | -0.263052 | -0.042863 | 0.630042 |
| player | theta_norm | 1133 | 3.40295 | 0.85651 | 1.55961 | 2.16493 | 2.74116 | 3.31263 | 3.96891 | 4.90907 | 6.12249 |
| tossup | start_difficulty_d1 | 1240 | -1.08951 | 1.36231 | -3.99495 | -3.48256 | -2.71552 | -0.314538 | -0.0773757 | 0.120338 | 0.399851 |
| tossup | start_difficulty_d2 | 1240 | -1.32622 | 1.30266 | -4.36561 | -3.63386 | -2.47401 | -0.763285 | -0.194777 | 0.0479513 | 0.319945 |
| tossup | start_difficulty_d3 | 1240 | -0.400932 | 0.641206 | -3.42181 | -1.86011 | -0.548669 | -0.183418 | -0.00202862 | 0.171673 | 0.601446 |
| tossup | start_difficulty_d4 | 1240 | -2.37761 | 1.5574 | -5.01513 | -4.37568 | -3.68316 | -2.96162 | -0.600768 | -0.0481054 | 0.442553 |
| tossup | start_difficulty_d5 | 1240 | -0.393543 | 0.608906 | -3.20109 | -1.7587 | -0.54706 | -0.221276 | 2.03073e-05 | 0.216637 | 0.49739 |
| tossup | start_difficulty_d6 | 1240 | -0.253235 | 0.39256 | -2.32575 | -1.05422 | -0.381357 | -0.148106 | -0.00507826 | 0.162884 | 0.501578 |
| tossup | end_difficulty_d1 | 1240 | -2.15955 | 1.50908 | -6.76061 | -4.93953 | -3.67 | -1.31718 | -1.05818 | -0.828065 | -0.478686 |
| tossup | end_difficulty_d2 | 1240 | -2.38333 | 1.39529 | -6.06941 | -4.87861 | -3.61796 | -1.78618 | -1.18339 | -0.919272 | -0.566881 |
| tossup | end_difficulty_d3 | 1240 | -1.42323 | 0.741807 | -6.80701 | -3.01907 | -1.58369 | -1.18644 | -0.974795 | -0.766552 | -0.275073 |
| tossup | end_difficulty_d4 | 1240 | -3.46056 | 1.64261 | -7.97288 | -5.66298 | -4.80844 | -3.92875 | -1.65393 | -1.01459 | -0.479562 |
| tossup | end_difficulty_d5 | 1240 | -1.41306 | 0.70729 | -4.59953 | -3.04395 | -1.58031 | -1.21673 | -0.965397 | -0.711391 | -0.372506 |
| tossup | end_difficulty_d6 | 1240 | -1.25292 | 0.445753 | -4.10266 | -2.1322 | -1.4016 | -1.14264 | -0.973419 | -0.773733 | -0.414751 |
| tossup | total_drop_d1 | 1240 | 1.07004 | 0.244588 | 0.627535 | 0.890554 | 0.960156 | 1.00155 | 1.06845 | 1.53679 | 3.41981 |
| tossup | total_drop_d2 | 1240 | 1.05711 | 0.19762 | 0.624072 | 0.872864 | 0.959674 | 1.00599 | 1.0887 | 1.44016 | 3.26566 |
| tossup | total_drop_d3 | 1240 | 1.02229 | 0.146928 | 0.822519 | 0.915383 | 0.9591 | 0.996651 | 1.04292 | 1.19312 | 3.7 |
| tossup | total_drop_d4 | 1240 | 1.08295 | 0.330311 | 0.375943 | 0.6684 | 0.925448 | 1.02641 | 1.16726 | 1.68428 | 4.03356 |
| tossup | total_drop_d5 | 1240 | 1.01952 | 0.120436 | 0.844636 | 0.902588 | 0.950913 | 0.992181 | 1.04399 | 1.24022 | 1.86929 |
| tossup | total_drop_d6 | 1240 | 0.99969 | 0.0706263 | 0.864364 | 0.914422 | 0.957091 | 0.989197 | 1.02814 | 1.11057 | 1.83731 |
| tossup | drop_share_1_d1 | 1240 | 0.332166 | 0.0412402 | 0.25191 | 0.295003 | 0.305062 | 0.314581 | 0.35223 | 0.416144 | 0.498993 |
| tossup | drop_share_2_d1 | 1240 | 0.34352 | 0.013051 | 0.293379 | 0.320061 | 0.336438 | 0.343855 | 0.351708 | 0.363032 | 0.417847 |
| tossup | drop_share_3_d1 | 1240 | 0.324314 | 0.0366742 | 0.183767 | 0.2447 | 0.311075 | 0.338767 | 0.348343 | 0.359258 | 0.371449 |
| tossup | drop_share_1_d2 | 1240 | 0.333384 | 0.0369783 | 0.274594 | 0.297023 | 0.309395 | 0.319796 | 0.34535 | 0.413002 | 0.508277 |
| tossup | drop_share_2_d2 | 1240 | 0.342804 | 0.0131373 | 0.292721 | 0.318581 | 0.335873 | 0.344021 | 0.351892 | 0.36126 | 0.392107 |
| tossup | drop_share_3_d2 | 1240 | 0.323812 | 0.0318586 | 0.19201 | 0.255399 | 0.311972 | 0.333744 | 0.344935 | 0.356935 | 0.395676 |
| tossup | drop_share_1_d3 | 1240 | 0.312662 | 0.0167414 | 0.282893 | 0.29282 | 0.303176 | 0.310254 | 0.318445 | 0.336722 | 0.454431 |
| tossup | drop_share_2_d3 | 1240 | 0.346982 | 0.00958424 | 0.316048 | 0.331241 | 0.340379 | 0.34714 | 0.353065 | 0.362584 | 0.381365 |
| tossup | drop_share_3_d3 | 1240 | 0.340356 | 0.0170774 | 0.214993 | 0.315318 | 0.334021 | 0.342728 | 0.350433 | 0.36071 | 0.381821 |
| tossup | drop_share_1_d4 | 1240 | 0.353998 | 0.0530929 | 0.201801 | 0.297025 | 0.315523 | 0.34008 | 0.381566 | 0.455731 | 0.608554 |
| tossup | drop_share_2_d4 | 1240 | 0.335993 | 0.0231558 | 0.246186 | 0.299921 | 0.321256 | 0.337821 | 0.349427 | 0.366624 | 0.501481 |
| tossup | drop_share_3_d4 | 1240 | 0.310008 | 0.0466936 | 0.138342 | 0.220141 | 0.286544 | 0.322788 | 0.341187 | 0.363985 | 0.462865 |
| tossup | drop_share_1_d5 | 1240 | 0.312551 | 0.0138008 | 0.276477 | 0.294838 | 0.303873 | 0.310334 | 0.318429 | 0.337488 | 0.382221 |
| tossup | drop_share_2_d5 | 1240 | 0.346793 | 0.00952277 | 0.316605 | 0.331037 | 0.340167 | 0.34689 | 0.35351 | 0.36186 | 0.376689 |
| tossup | drop_share_3_d5 | 1240 | 0.340656 | 0.0146902 | 0.255207 | 0.315919 | 0.333259 | 0.342068 | 0.349735 | 0.361417 | 0.379142 |
| tossup | drop_share_1_d6 | 1240 | 0.310368 | 0.0103703 | 0.27935 | 0.294919 | 0.303278 | 0.309686 | 0.316396 | 0.329012 | 0.349897 |
| tossup | drop_share_2_d6 | 1240 | 0.34681 | 0.00926793 | 0.314514 | 0.331374 | 0.340549 | 0.346889 | 0.352885 | 0.363 | 0.375348 |
| tossup | drop_share_3_d6 | 1240 | 0.342822 | 0.0112531 | 0.296678 | 0.322876 | 0.335872 | 0.343409 | 0.350415 | 0.360206 | 0.379008 |
| tossup | r_1 | 1240 | 0.193897 | 0.237687 | 0.0132814 | 0.0222702 | 0.0334825 | 0.0473556 | 0.480283 | 0.621414 | 0.749606 |
| tossup | r_2 | 1240 | 0.195901 | 0.207587 | 0.0146426 | 0.0257873 | 0.0438456 | 0.0862401 | 0.316369 | 0.621362 | 0.79148 |
| tossup | r_3 | 1240 | 0.0584326 | 0.0376966 | 0.0150769 | 0.0248075 | 0.0348983 | 0.0466599 | 0.0661349 | 0.135755 | 0.274365 |
| tossup | r_4 | 1240 | 0.419348 | 0.285959 | 0.0372149 | 0.0575287 | 0.103976 | 0.396748 | 0.699202 | 0.819427 | 0.918753 |
| tossup | r_5 | 1240 | 0.0715811 | 0.0451883 | 0.0159982 | 0.026495 | 0.0413633 | 0.0574304 | 0.0851161 | 0.173631 | 0.286132 |
| tossup | r_6 | 1240 | 0.0608407 | 0.0314944 | 0.0115477 | 0.0254166 | 0.0386792 | 0.0537502 | 0.073254 | 0.120106 | 0.232858 |
| tossup | r_norm | 1240 | 0.665268 | 0.0845878 | 0.486715 | 0.552842 | 0.600134 | 0.648285 | 0.724472 | 0.823692 | 0.91952 |
