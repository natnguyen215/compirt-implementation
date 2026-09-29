# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_3/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_3/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 312787 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.647454 |
| log_loss | 0.530671 |
| ece | 0.0384622 |
| brier | 0.173589 |
| accuracy | 0.760585 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00153965 |
| probability_std | 0.143003 |
| probability_p10 | 0.545896 |
| probability_p50 | 0.776664 |
| probability_p90 | 0.912838 |
| mean_predictive_variance | 0.167287 |
| integrated_brier_score | 0.101795 |
| joint_tossup_event_log_loss | 6.91662 |
| buzz_position_mae | 0.161818 |
| buzz_position_median_absolute_error | 0.14754 |
| buzz_position_bias | -0.0687676 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.338722 |
| first_buzzer_mean_reciprocal_rank | 0.552018 |
| first_buzzer_log_loss | 1.70686 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.634114 |
| tossup_scorer_player_top1_accuracy | 0.318506 |
| tossup_scorer_team_top1_accuracy | 0.483766 |
| tossup_game_winner_accuracy | 0.745495 |
| tossup_game_margin_mae | 35.3394 |
| tournament_player_ppg_spearman | 0.673321 |
| tournament_player_ppg_mae | 9.00354 |
| tournament_player_ppg_top10_overlap | 0.655172 |
| neg_auroc | 0.647454 |
| neg_average_precision | 0.37259 |
| neg_precision | 0.488255 |
| neg_recall | 0.134535 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0572329 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0903992 |
| no_buzz_calibration_error | 0.0744901 |
| no_buzz_brier | 0.0264023 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| tossup_correctness | aggregate | all | 9093 | 0.647454 | 0.530671 | 0.0384622 | 0.173589 | 0.760585 | 0.762125 | -0.00153965 | 0.143003 | 0.545896 | 0.776664 | 0.912838 | 0.167287 |
| tossup_correctness | tier | fall | 2842 | 0.674084 | 0.488583 | 0.0155722 | 0.15717 | 0.789585 | 0.785362 | 0.00422238 | 0.124405 | 0.602395 | 0.806911 | 0.918975 | 0.155455 |
| tossup_correctness | tier | nationals | 1564 | 0.634811 | 0.583864 | 0.0644484 | 0.197689 | 0.707161 | 0.718031 | -0.0108696 | 0.144982 | 0.466274 | 0.677416 | 0.845572 | 0.201162 |
| tossup_correctness | tier | regionals | 1937 | 0.623968 | 0.544487 | 0.054896 | 0.178894 | 0.752194 | 0.758389 | -0.00619515 | 0.142675 | 0.549066 | 0.77513 | 0.912737 | 0.167054 |
| tossup_correctness | tier | winter | 2750 | 0.636108 | 0.534183 | 0.0399609 | 0.173114 | 0.766909 | 0.765818 | 0.00109091 | 0.14216 | 0.560072 | 0.793109 | 0.921452 | 0.160412 |
| tossup_correctness | category | Current Events | 126 | 0.675791 | 0.530048 | 0.0901605 | 0.174662 | 0.761905 | 0.769841 | -0.00793651 | 0.131004 | 0.504725 | 0.698206 | 0.840829 | 0.200553 |
| tossup_correctness | category | Fine Arts | 1071 | 0.647893 | 0.523206 | 0.0333018 | 0.171152 | 0.770308 | 0.766573 | 0.00373483 | 0.140003 | 0.557921 | 0.778788 | 0.910736 | 0.165571 |
| tossup_correctness | category | Geography | 185 | 0.693798 | 0.571608 | 0.0652251 | 0.194579 | 0.686486 | 0.697297 | -0.0108108 | 0.165528 | 0.415227 | 0.660196 | 0.859945 | 0.201874 |
| tossup_correctness | category | History | 1440 | 0.659594 | 0.531829 | 0.0332028 | 0.175876 | 0.751389 | 0.754167 | -0.00277778 | 0.137645 | 0.526134 | 0.750217 | 0.883281 | 0.180191 |
| tossup_correctness | category | Literature | 1422 | 0.586487 | 0.495042 | 0.057524 | 0.154201 | 0.808017 | 0.814346 | -0.00632911 | 0.126217 | 0.625281 | 0.838244 | 0.941667 | 0.139459 |
| tossup_correctness | category | Mythology | 318 | 0.669144 | 0.498099 | 0.0650445 | 0.160209 | 0.783019 | 0.789308 | -0.00628931 | 0.136804 | 0.549656 | 0.761175 | 0.901083 | 0.173795 |
| tossup_correctness | category | Other Academic | 66 | 0.714446 | 0.5388 | 0.0602851 | 0.18051 | 0.757576 | 0.712121 | 0.0454545 | 0.123659 | 0.534028 | 0.703224 | 0.855706 | 0.198263 |
| tossup_correctness | category | Philosophy | 311 | 0.676179 | 0.535885 | 0.0675049 | 0.177087 | 0.73955 | 0.745981 | -0.00643087 | 0.132544 | 0.598283 | 0.797251 | 0.921979 | 0.159167 |
| tossup_correctness | category | Popular Culture | 102 | 0.644444 | 0.435616 | 0.181156 | 0.132546 | 0.882353 | 0.882353 | 0 | 0.130397 | 0.547005 | 0.723821 | 0.857979 | 0.188582 |
| tossup_correctness | category | Religion | 358 | 0.65277 | 0.574587 | 0.0440536 | 0.192869 | 0.726257 | 0.712291 | 0.0139665 | 0.130115 | 0.539286 | 0.759524 | 0.887652 | 0.177193 |
| tossup_correctness | category | Science | 1433 | 0.668827 | 0.54587 | 0.0321565 | 0.181161 | 0.737613 | 0.738311 | -0.000697837 | 0.152704 | 0.51929 | 0.78178 | 0.909813 | 0.167321 |
| tossup_correctness | category | Social Science | 324 | 0.668364 | 0.540322 | 0.0371572 | 0.178937 | 0.753086 | 0.731481 | 0.0216049 | 0.130205 | 0.547332 | 0.742534 | 0.868971 | 0.183735 |
| tossup_correctness | category | Unknown | 1937 | 0.623968 | 0.544487 | 0.054896 | 0.178894 | 0.752194 | 0.758389 | -0.00619515 | 0.142675 | 0.549066 | 0.77513 | 0.912737 | 0.167054 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.606443 | 0.605177 | 0.0660272 | 0.205951 | 0.694611 | 0.712575 | -0.0179641 | 0.136841 | 0.499636 | 0.702367 | 0.843006 | 0.198304 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.66541 | 0.5568 | 0.0481843 | 0.185505 | 0.737939 | 0.729167 | 0.00877193 | 0.144726 | 0.486021 | 0.717916 | 0.860785 | 0.192109 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.660478 | 0.529132 | 0.0285849 | 0.1741 | 0.756974 | 0.755083 | 0.00189125 | 0.138268 | 0.532993 | 0.7642 | 0.892933 | 0.175346 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.641717 | 0.51092 | 0.0400009 | 0.165935 | 0.77602 | 0.780942 | -0.00492264 | 0.138351 | 0.564329 | 0.789264 | 0.914806 | 0.162755 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.639413 | 0.53825 | 0.0415759 | 0.175033 | 0.759083 | 0.762029 | -0.00294599 | 0.143728 | 0.567307 | 0.796574 | 0.93087 | 0.15682 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | -1.99434 | 1.27809 | -5.03993 | -3.79556 | -2.96848 | -2.3115 | -0.63088 | 0.0163613 | 0.787709 |
| player | theta_2 | 1167 | -0.247186 | 0.408979 | -2.03073 | -0.852591 | -0.490291 | -0.271771 | -0.0361173 | 0.489335 | 1.14983 |
| player | theta_3 | 1167 | -1.60258 | 1.30132 | -4.33706 | -3.53628 | -2.73525 | -1.95905 | -0.250179 | -0.0422521 | 0.45625 |
| player | theta_norm | 1167 | 3.07578 | 0.798786 | 1.22227 | 1.94942 | 2.46496 | 3.01163 | 3.61903 | 4.50806 | 5.8043 |
| tossup | start_difficulty_d1 | 1220 | -1.81515 | 1.66068 | -5.85947 | -4.18194 | -3.41831 | -1.37785 | -0.168165 | 0.14052 | 1.20245 |
| tossup | start_difficulty_d2 | 1220 | -0.0606163 | 0.61698 | -2.37926 | -1.41352 | -0.24265 | 0.0339907 | 0.251935 | 0.772833 | 1.81418 |
| tossup | start_difficulty_d3 | 1220 | -1.6627 | 1.6327 | -5.0694 | -4.0458 | -3.12723 | -2.01456 | -0.0945576 | 0.28215 | 1.57221 |
| tossup | end_difficulty_d1 | 1220 | -2.9327 | 1.8634 | -10.4619 | -5.91342 | -4.46191 | -2.71271 | -1.16562 | -0.804165 | 0.459111 |
| tossup | end_difficulty_d2 | 1220 | -1.07731 | 0.75975 | -4.06205 | -2.79171 | -1.28411 | -0.943311 | -0.689299 | -0.101255 | 1.07196 |
| tossup | end_difficulty_d3 | 1220 | -2.76755 | 1.79532 | -8.17367 | -5.5469 | -4.38643 | -2.77116 | -1.06988 | -0.648568 | 0.739419 |
| tossup | total_drop_d1 | 1220 | 1.11755 | 0.518955 | 0.378807 | 0.68813 | 0.919715 | 1.0005 | 1.12409 | 1.96486 | 7.32392 |
| tossup | total_drop_d2 | 1220 | 1.01669 | 0.158391 | 0.722153 | 0.856336 | 0.933905 | 0.981475 | 1.04495 | 1.32998 | 2.11753 |
| tossup | total_drop_d3 | 1220 | 1.10486 | 0.42302 | 0.521889 | 0.703186 | 0.928112 | 0.999077 | 1.10651 | 1.90586 | 4.88827 |
| tossup | drop_share_1_d1 | 1220 | 0.341544 | 0.0537458 | 0.20158 | 0.289801 | 0.306236 | 0.320433 | 0.367899 | 0.442197 | 0.68573 |
| tossup | drop_share_2_d1 | 1220 | 0.339881 | 0.0210899 | 0.202707 | 0.307559 | 0.329097 | 0.340958 | 0.35144 | 0.367661 | 0.510567 |
| tossup | drop_share_3_d1 | 1220 | 0.318575 | 0.0471939 | 0.111562 | 0.224584 | 0.296193 | 0.334423 | 0.349694 | 0.367756 | 0.488861 |
| tossup | drop_share_1_d2 | 1220 | 0.307485 | 0.0169336 | 0.252927 | 0.283514 | 0.297099 | 0.305982 | 0.315037 | 0.337408 | 0.389983 |
| tossup | drop_share_2_d2 | 1220 | 0.347435 | 0.0107874 | 0.313982 | 0.329839 | 0.340338 | 0.347284 | 0.354363 | 0.365185 | 0.399807 |
| tossup | drop_share_3_d2 | 1220 | 0.34508 | 0.0177075 | 0.244384 | 0.313863 | 0.336564 | 0.346835 | 0.356642 | 0.369493 | 0.392831 |
| tossup | drop_share_1_d3 | 1220 | 0.334115 | 0.0424275 | 0.193349 | 0.28873 | 0.305003 | 0.319045 | 0.360471 | 0.413009 | 0.5968 |
| tossup | drop_share_2_d3 | 1220 | 0.341678 | 0.0190496 | 0.258067 | 0.311061 | 0.331326 | 0.342285 | 0.351717 | 0.369139 | 0.447513 |
| tossup | drop_share_3_d3 | 1220 | 0.324206 | 0.0400777 | 0.145133 | 0.246085 | 0.300103 | 0.33578 | 0.350598 | 0.369996 | 0.490809 |
| tossup | r_1 | 1220 | 0.471377 | 0.3864 | 0.0132873 | 0.0320753 | 0.0753268 | 0.270094 | 0.870477 | 0.932111 | 0.97514 |
| tossup | r_2 | 1220 | 0.0790128 | 0.0577753 | 0.00752915 | 0.0193528 | 0.0372832 | 0.0606059 | 0.103022 | 0.19607 | 0.432378 |
| tossup | r_3 | 1220 | 0.44961 | 0.383259 | 0.013994 | 0.0359385 | 0.0600675 | 0.595239 | 0.83317 | 0.929986 | 0.975011 |
| tossup | r_norm | 1220 | 0.85158 | 0.0684799 | 0.627176 | 0.727002 | 0.803597 | 0.862953 | 0.906565 | 0.947091 | 0.975301 |
