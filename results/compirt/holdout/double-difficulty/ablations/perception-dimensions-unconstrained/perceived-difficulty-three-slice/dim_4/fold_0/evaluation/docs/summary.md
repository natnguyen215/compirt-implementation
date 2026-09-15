# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_4/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_4/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 319097 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.648582 |
| log_loss | 0.521603 |
| ece | 0.0186405 |
| brier | 0.170689 |
| accuracy | 0.764605 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.000645508 |
| probability_std | 0.120058 |
| probability_p10 | 0.594096 |
| probability_p50 | 0.784035 |
| probability_p90 | 0.897958 |
| mean_predictive_variance | 0.166704 |
| integrated_brier_score | 0.108319 |
| joint_tossup_event_log_loss | 7.04682 |
| buzz_position_mae | 0.168114 |
| buzz_position_median_absolute_error | 0.151594 |
| buzz_position_bias | -0.0728031 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.360516 |
| first_buzzer_mean_reciprocal_rank | 0.570507 |
| first_buzzer_log_loss | 1.71734 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.637332 |
| tossup_scorer_player_top1_accuracy | 0.316242 |
| tossup_scorer_team_top1_accuracy | 0.487049 |
| tossup_game_winner_accuracy | 0.788546 |
| tossup_game_margin_mae | 36.797 |
| tournament_player_ppg_spearman | 0.647807 |
| tournament_player_ppg_mae | 9.95674 |
| tournament_player_ppg_top10_overlap | 0.634483 |
| neg_auroc | 0.648582 |
| neg_average_precision | 0.362559 |
| neg_precision | 0.490625 |
| neg_recall | 0.0719523 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0552965 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0902534 |
| no_buzz_calibration_error | 0.0769838 |
| no_buzz_brier | 0.0250225 |
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
| tossup_correctness | aggregate | all | 9295 | 0.648582 | 0.521603 | 0.0186405 | 0.170689 | 0.764605 | 0.76525 | -0.000645508 | 0.120058 | 0.594096 | 0.784035 | 0.897958 | 0.166704 |
| tossup_correctness | tier | fall | 2933 | 0.644553 | 0.491358 | 0.0284895 | 0.157605 | 0.793386 | 0.791681 | 0.00170474 | 0.119518 | 0.596166 | 0.796535 | 0.897732 | 0.163174 |
| tossup_correctness | tier | nationals | 1584 | 0.642685 | 0.56277 | 0.0282718 | 0.189403 | 0.72096 | 0.724747 | -0.00378788 | 0.121057 | 0.540929 | 0.725782 | 0.850033 | 0.191763 |
| tossup_correctness | tier | regionals | 1886 | 0.631992 | 0.546327 | 0.0181213 | 0.182105 | 0.742842 | 0.746023 | -0.00318134 | 0.11087 | 0.589959 | 0.75686 | 0.872802 | 0.178806 |
| tossup_correctness | tier | winter | 2892 | 0.654906 | 0.513606 | 0.0284524 | 0.166262 | 0.773513 | 0.773167 | 0.000345781 | 0.112556 | 0.642335 | 0.819947 | 0.919869 | 0.148667 |
| tossup_correctness | category | Current Events | 124 | 0.688866 | 0.520058 | 0.0675185 | 0.169284 | 0.782258 | 0.75 | 0.0322581 | 0.123085 | 0.533616 | 0.727133 | 0.859703 | 0.189735 |
| tossup_correctness | category | Fine Arts | 1103 | 0.619843 | 0.542285 | 0.0337072 | 0.177637 | 0.754306 | 0.759746 | -0.00543971 | 0.117197 | 0.611238 | 0.798817 | 0.904712 | 0.161113 |
| tossup_correctness | category | Geography | 197 | 0.722494 | 0.568903 | 0.0409104 | 0.19382 | 0.695431 | 0.670051 | 0.0253807 | 0.16122 | 0.479238 | 0.734503 | 0.895832 | 0.182385 |
| tossup_correctness | category | History | 1491 | 0.676917 | 0.487106 | 0.0223564 | 0.15679 | 0.784708 | 0.787391 | -0.00268276 | 0.113672 | 0.606341 | 0.789103 | 0.897405 | 0.165256 |
| tossup_correctness | category | Literature | 1472 | 0.620189 | 0.485207 | 0.0264066 | 0.153363 | 0.805707 | 0.804348 | 0.0013587 | 0.101322 | 0.673393 | 0.830682 | 0.925565 | 0.141414 |
| tossup_correctness | category | Mythology | 332 | 0.695818 | 0.463622 | 0.081492 | 0.14735 | 0.792169 | 0.813253 | -0.0210843 | 0.111178 | 0.587674 | 0.752242 | 0.868872 | 0.181086 |
| tossup_correctness | category | Other Academic | 69 | 0.471719 | 0.586034 | 0.101998 | 0.19606 | 0.753623 | 0.753623 | 0 | 0.101797 | 0.568471 | 0.720625 | 0.837949 | 0.194976 |
| tossup_correctness | category | Philosophy | 324 | 0.642946 | 0.482288 | 0.0471173 | 0.153254 | 0.805556 | 0.799383 | 0.00617284 | 0.119006 | 0.62055 | 0.804496 | 0.910281 | 0.156517 |
| tossup_correctness | category | Popular Culture | 102 | 0.447059 | 0.521517 | 0.0892059 | 0.166363 | 0.813725 | 0.833333 | -0.0196078 | 0.118866 | 0.603628 | 0.775547 | 0.881794 | 0.170756 |
| tossup_correctness | category | Religion | 372 | 0.667088 | 0.569387 | 0.0536111 | 0.193251 | 0.715054 | 0.709677 | 0.00537634 | 0.127172 | 0.565637 | 0.772567 | 0.890971 | 0.173907 |
| tossup_correctness | category | Science | 1487 | 0.649435 | 0.533015 | 0.0310307 | 0.175735 | 0.755884 | 0.752522 | 0.00336247 | 0.131803 | 0.568357 | 0.77539 | 0.894491 | 0.170593 |
| tossup_correctness | category | Social Science | 336 | 0.66928 | 0.578897 | 0.0551263 | 0.19699 | 0.699405 | 0.702381 | -0.00297619 | 0.118235 | 0.600385 | 0.751921 | 0.871158 | 0.180052 |
| tossup_correctness | category | Unknown | 1886 | 0.631992 | 0.546327 | 0.0181213 | 0.182105 | 0.742842 | 0.746023 | -0.00318134 | 0.11087 | 0.589959 | 0.75686 | 0.872802 | 0.178806 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.610212 | 0.586142 | 0.0863359 | 0.196533 | 0.736041 | 0.736041 | 0 | 0.134238 | 0.495224 | 0.686087 | 0.820704 | 0.202723 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.625913 | 0.561849 | 0.0307051 | 0.187728 | 0.735025 | 0.735025 | 0 | 0.123637 | 0.55278 | 0.725964 | 0.859916 | 0.189094 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.653542 | 0.515619 | 0.0248537 | 0.16826 | 0.769436 | 0.769436 | 0 | 0.118134 | 0.581675 | 0.772344 | 0.880865 | 0.174331 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.659198 | 0.495308 | 0.0174539 | 0.160081 | 0.783671 | 0.78402 | -0.000348918 | 0.114528 | 0.612278 | 0.796093 | 0.901721 | 0.162304 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.650955 | 0.533779 | 0.033642 | 0.17536 | 0.754339 | 0.756008 | -0.00166889 | 0.115678 | 0.630107 | 0.804187 | 0.915075 | 0.155454 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | -2.05316 | 1.1697 | -4.58988 | -3.64179 | -2.89636 | -2.35757 | -0.707279 | -0.127169 | 0.713714 |
| player | theta_2 | 1186 | -0.895357 | 0.681523 | -3.55789 | -2.35762 | -1.18278 | -0.730227 | -0.4085 | -0.147773 | 0.372965 |
| player | theta_3 | 1186 | -0.871378 | 0.683509 | -3.38948 | -2.15046 | -1.29525 | -0.742174 | -0.373177 | 0.0946669 | 1.0875 |
| player | theta_4 | 1186 | -1.61518 | 1.09348 | -4.92221 | -3.36181 | -2.52742 | -1.63663 | -0.518247 | -0.196661 | 0.181802 |
| player | theta_norm | 1186 | 3.33562 | 0.867244 | 1.54644 | 2.03313 | 2.68949 | 3.23494 | 3.9067 | 4.96989 | 6.01239 |
| tossup | start_difficulty_d1 | 1240 | -2.46501 | 1.31045 | -4.75746 | -3.86325 | -3.31286 | -2.96689 | -2.25279 | -0.00547859 | 0.458055 |
| tossup | start_difficulty_d2 | 1240 | -0.881728 | 0.940839 | -3.72332 | -2.7952 | -1.45341 | -0.555772 | -0.146603 | 0.162142 | 0.559568 |
| tossup | start_difficulty_d3 | 1240 | -0.813262 | 0.850181 | -3.40493 | -2.36101 | -1.3918 | -0.644402 | -0.137892 | 0.271353 | 1.34696 |
| tossup | start_difficulty_d4 | 1240 | -1.38268 | 1.47262 | -5.15674 | -4.06361 | -2.74159 | -0.620374 | -0.165713 | 0.0693234 | 0.458209 |
| tossup | end_difficulty_d1 | 1240 | -3.56717 | 1.4132 | -6.99953 | -5.25766 | -4.52193 | -4.03911 | -3.03923 | -0.96328 | -0.475511 |
| tossup | end_difficulty_d2 | 1240 | -1.92827 | 1.07974 | -6.48114 | -4.18593 | -2.52465 | -1.56009 | -1.11266 | -0.764509 | -0.266294 |
| tossup | end_difficulty_d3 | 1240 | -1.86515 | 0.979697 | -4.98289 | -3.68646 | -2.50858 | -1.66261 | -1.09016 | -0.630209 | 0.561381 |
| tossup | end_difficulty_d4 | 1240 | -2.4437 | 1.58468 | -8.48047 | -5.32287 | -3.85174 | -1.65242 | -1.14626 | -0.868724 | -0.439418 |
| tossup | total_drop_d1 | 1240 | 1.10216 | 0.332812 | 0.51316 | 0.703656 | 0.921888 | 1.02691 | 1.21503 | 1.74312 | 3.92699 |
| tossup | total_drop_d2 | 1240 | 1.04655 | 0.191272 | 0.773095 | 0.888941 | 0.949614 | 0.998085 | 1.07877 | 1.3668 | 3.39872 |
| tossup | total_drop_d3 | 1240 | 1.05189 | 0.156846 | 0.78558 | 0.891822 | 0.95147 | 1.00856 | 1.10141 | 1.35295 | 2.31938 |
| tossup | total_drop_d4 | 1240 | 1.06102 | 0.342346 | 0.371758 | 0.738452 | 0.944166 | 0.999198 | 1.08059 | 1.52405 | 6.31905 |
| tossup | drop_share_1_d1 | 1240 | 0.356116 | 0.0446194 | 0.215874 | 0.296616 | 0.317583 | 0.357425 | 0.38699 | 0.425948 | 0.608917 |
| tossup | drop_share_2_d1 | 1240 | 0.336917 | 0.019495 | 0.258389 | 0.306122 | 0.325534 | 0.337242 | 0.347683 | 0.365066 | 0.457337 |
| tossup | drop_share_3_d1 | 1240 | 0.306967 | 0.0422336 | 0.132694 | 0.237016 | 0.278189 | 0.308116 | 0.339886 | 0.365914 | 0.464889 |
| tossup | drop_share_1_d2 | 1240 | 0.322858 | 0.0242373 | 0.268063 | 0.295935 | 0.306709 | 0.3169 | 0.331952 | 0.372117 | 0.454786 |
| tossup | drop_share_2_d2 | 1240 | 0.345195 | 0.00989369 | 0.31366 | 0.329039 | 0.338575 | 0.345346 | 0.351843 | 0.361918 | 0.375482 |
| tossup | drop_share_3_d2 | 1240 | 0.331947 | 0.0237484 | 0.215741 | 0.284992 | 0.321069 | 0.336938 | 0.34744 | 0.360747 | 0.393275 |
| tossup | drop_share_1_d3 | 1240 | 0.321041 | 0.0180954 | 0.277102 | 0.29532 | 0.307994 | 0.318548 | 0.332874 | 0.354261 | 0.385257 |
| tossup | drop_share_2_d3 | 1240 | 0.346738 | 0.0092785 | 0.321233 | 0.33145 | 0.340253 | 0.346521 | 0.353011 | 0.361976 | 0.379756 |
| tossup | drop_share_3_d3 | 1240 | 0.332222 | 0.0185474 | 0.272442 | 0.29897 | 0.320137 | 0.33398 | 0.345925 | 0.359578 | 0.380095 |
| tossup | drop_share_1_d4 | 1240 | 0.334411 | 0.0447041 | 0.194438 | 0.296245 | 0.307748 | 0.318297 | 0.346301 | 0.432988 | 0.608429 |
| tossup | drop_share_2_d4 | 1240 | 0.341899 | 0.0177946 | 0.25375 | 0.308197 | 0.334589 | 0.34436 | 0.351754 | 0.362835 | 0.525825 |
| tossup | drop_share_3_d4 | 1240 | 0.32369 | 0.0380131 | 0.134169 | 0.243297 | 0.313433 | 0.335549 | 0.346509 | 0.360758 | 0.447806 |
| tossup | r_1 | 1240 | 0.497958 | 0.271606 | 0.0168202 | 0.0330174 | 0.395843 | 0.576748 | 0.68991 | 0.822793 | 0.936291 |
| tossup | r_2 | 1240 | 0.117166 | 0.0989364 | 0.0166564 | 0.027307 | 0.045423 | 0.0765858 | 0.159938 | 0.329124 | 0.546114 |
| tossup | r_3 | 1240 | 0.109835 | 0.0774952 | 0.0119696 | 0.0270571 | 0.0526285 | 0.0812965 | 0.150225 | 0.274372 | 0.390017 |
| tossup | r_4 | 1240 | 0.275041 | 0.310692 | 0.0236281 | 0.034574 | 0.0538407 | 0.105035 | 0.335233 | 0.861303 | 0.941957 |
| tossup | r_norm | 1240 | 0.725966 | 0.0912383 | 0.553329 | 0.592906 | 0.648354 | 0.715348 | 0.802533 | 0.877126 | 0.942558 |
