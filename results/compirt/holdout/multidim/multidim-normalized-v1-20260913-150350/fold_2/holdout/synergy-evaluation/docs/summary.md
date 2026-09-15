# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/multidim-normalized-v1-20260913-150350/fold_2/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/multidim-normalized-v1-20260913-150350/fold_2`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 298584 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.548224 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.893986 |
| log_loss | 0.414747 |
| ece | 0.0331832 |
| brier | 0.132227 |
| part_accuracy | 0.812144 |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.292777 |
| part_accuracy_macro_team | 0.81594 |
| part_accuracy_macro_bonus | 0.808567 |
| probability_std | 0.340539 |
| probability_p10 | 0.060908 |
| probability_p50 | 0.452959 |
| probability_p90 | 0.945891 |
| mean_predictive_variance | 0.133843 |
| exact_acc | 0.523904 |
| ranked_probability_score | 0.112309 |
| bonus_total_score_log_loss | 0.993031 |
| ppb_mae | 1.88191 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.625497 |
| log_loss | 0.816903 |
| ece | 0.219935 |
| brier | 0.261412 |
| accuracy | 0.619099 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.145079 |
| probability_std | 0.290538 |
| probability_p10 | 0.103815 |
| probability_p50 | 0.616161 |
| probability_p90 | 0.907097 |
| mean_predictive_variance | 0.162195 |
| integrated_brier_score | 0.0957555 |
| joint_tossup_event_log_loss | 6.79486 |
| buzz_position_mae | 0.14565 |
| buzz_position_median_absolute_error | 0.125779 |
| buzz_position_bias | -0.0381238 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.396565 |
| first_buzzer_mean_reciprocal_rank | 0.604003 |
| first_buzzer_log_loss | 1.59599 |
| first_buzzer_events | 9257 |
| first_buzzer_player_replay_accuracy | 0.00822689 |
| first_buzzer_team_replay_accuracy | 0.00985062 |
| tossup_scorer_player_replay_accuracy | 0.0904915 |
| tossup_scorer_team_replay_accuracy | 0.092094 |
| tossup_game_winner_accuracy | 0.138462 |
| tossup_model_official_winner_accuracy | 0.138528 |
| tossup_game_margin_mae | 57.265 |
| tossup_game_zero_margin_mae | 58.4615 |
| tournament_player_ppg_spearman | 0.225162 |
| tournament_player_ppg_mae | 23.4047 |
| tournament_player_ppg_top10_overlap | 0.331034 |
| tournament_player_ppg_top10_random_overlap | 0.280534 |
| tournament_player_ppg_top10_adjusted_overlap | 0.0587342 |
| neg_auroc | 0.625497 |
| neg_average_precision | 0.325025 |
| neg_precision | 0.314452 |
| neg_recall | 0.521301 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.093734 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.062718 |
| no_buzz_calibration_error | 0.049605 |
| no_buzz_brier | 0.0216847 |
| full_pmf_max_mass_error | 5.55112e-16 |
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
| tossup_game_winner_accuracy | 0.138462 |
| tossup_game_margin_mae | 57.265 |
| tossup_game_zero_margin_mae | 58.4615 |
| tossup_game_margin_mae_games | 468 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 455 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.625497 | 0.816903 | 0.219935 | 0.261412 | 0.619099 | 0.764178 | -0.145079 | 0.290538 | 0.103815 | 0.616161 | 0.907097 | 0.162195 |
| tossup_correctness | tier | fall | 2798 | 0.641885 | 0.82931 | 0.242273 | 0.261876 | 0.619014 | 0.785204 | -0.16619 | 0.28905 | 0.0935066 | 0.596794 | 0.894611 | 0.164414 |
| tossup_correctness | tier | nationals | 1545 | 0.611894 | 0.767793 | 0.190727 | 0.257506 | 0.616828 | 0.721036 | -0.104207 | 0.286809 | 0.125645 | 0.63864 | 0.919858 | 0.161505 |
| tossup_correctness | tier | regionals | 2039 | 0.621669 | 0.837953 | 0.219762 | 0.262299 | 0.627268 | 0.762138 | -0.13487 | 0.29725 | 0.0925075 | 0.632238 | 0.922354 | 0.157225 |
| tossup_correctness | tier | winter | 2875 | 0.627343 | 0.816291 | 0.224146 | 0.26243 | 0.614609 | 0.768348 | -0.153739 | 0.288353 | 0.111227 | 0.608443 | 0.902806 | 0.163931 |
| tossup_correctness | category | Current Events | 129 | 0.583018 | 0.885802 | 0.266282 | 0.294886 | 0.550388 | 0.666667 | -0.116279 | 0.3051 | 0.0650594 | 0.608147 | 0.891202 | 0.155903 |
| tossup_correctness | category | Fine Arts | 1074 | 0.605346 | 0.884314 | 0.262273 | 0.285303 | 0.588454 | 0.776536 | -0.188082 | 0.29546 | 0.0808962 | 0.567101 | 0.897943 | 0.161889 |
| tossup_correctness | category | Geography | 180 | 0.600862 | 0.809501 | 0.183502 | 0.277558 | 0.544444 | 0.616667 | -0.0722222 | 0.257276 | 0.112074 | 0.491835 | 0.813971 | 0.183532 |
| tossup_correctness | category | History | 1454 | 0.639519 | 0.777272 | 0.207609 | 0.250326 | 0.643054 | 0.757909 | -0.114856 | 0.284994 | 0.112505 | 0.625657 | 0.901577 | 0.16442 |
| tossup_correctness | category | Literature | 1435 | 0.597975 | 0.80519 | 0.232712 | 0.25395 | 0.633449 | 0.810453 | -0.177003 | 0.288238 | 0.120614 | 0.661785 | 0.921028 | 0.158374 |
| tossup_correctness | category | Mythology | 324 | 0.627388 | 0.895737 | 0.261127 | 0.271638 | 0.589506 | 0.79321 | -0.203704 | 0.282487 | 0.0991229 | 0.559621 | 0.893718 | 0.169112 |
| tossup_correctness | category | Other Academic | 71 | 0.592593 | 0.778608 | 0.242795 | 0.265854 | 0.577465 | 0.760563 | -0.183099 | 0.275249 | 0.162717 | 0.575138 | 0.899739 | 0.170183 |
| tossup_correctness | category | Philosophy | 310 | 0.689132 | 0.749782 | 0.228899 | 0.249912 | 0.612903 | 0.76129 | -0.148387 | 0.291824 | 0.0842282 | 0.563531 | 0.910509 | 0.16379 |
| tossup_correctness | category | Popular Culture | 108 | 0.545139 | 1.00622 | 0.423073 | 0.33206 | 0.490741 | 0.888889 | -0.398148 | 0.252074 | 0.112451 | 0.468107 | 0.814905 | 0.18529 |
| tossup_correctness | category | Religion | 361 | 0.644559 | 0.800607 | 0.242395 | 0.26777 | 0.617729 | 0.742382 | -0.124654 | 0.28429 | 0.0902611 | 0.551742 | 0.864396 | 0.168947 |
| tossup_correctness | category | Science | 1445 | 0.636346 | 0.792905 | 0.192138 | 0.253003 | 0.624221 | 0.746021 | -0.121799 | 0.288608 | 0.113409 | 0.621907 | 0.913159 | 0.162072 |
| tossup_correctness | category | Social Science | 327 | 0.665772 | 0.724105 | 0.174964 | 0.243966 | 0.633028 | 0.718654 | -0.0856269 | 0.282592 | 0.121484 | 0.628803 | 0.886591 | 0.167163 |
| tossup_correctness | category | Unknown | 2039 | 0.621669 | 0.837953 | 0.219762 | 0.262299 | 0.627268 | 0.762138 | -0.13487 | 0.29725 | 0.0925075 | 0.632238 | 0.922354 | 0.157225 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.70729 | 1.38374 | 0.499462 | 0.430719 | 0.393443 | 0.743169 | -0.349727 | 0.212601 | 0.0142494 | 0.193571 | 0.551173 | 0.139115 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.658384 | 1.10872 | 0.378491 | 0.355191 | 0.470157 | 0.728796 | -0.258639 | 0.262983 | 0.0399802 | 0.304278 | 0.745597 | 0.15844 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.657289 | 0.877331 | 0.267666 | 0.280311 | 0.598928 | 0.752568 | -0.15364 | 0.283893 | 0.07454 | 0.514882 | 0.860675 | 0.169204 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.629505 | 0.748607 | 0.200656 | 0.240975 | 0.642087 | 0.786087 | -0.144 | 0.274725 | 0.170304 | 0.651014 | 0.913568 | 0.165957 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.598522 | 0.709959 | 0.150583 | 0.226769 | 0.673211 | 0.764393 | -0.0911814 | 0.258716 | 0.242141 | 0.737638 | 0.934373 | 0.155973 |
| bonus_part_correctness | aggregate | all | 25791 | 0.893986 | 0.414747 | 0.0331832 | 0.132227 | 0.812144 | 0.519367 | 0.292777 | 0.340539 | 0.060908 | 0.452959 | 0.945891 | 0.133843 |
| bonus_part_correctness | tier | fall | 7995 | 0.898346 | 0.398722 | 0.0263749 | 0.126894 | 0.815385 | 0.595122 | 0.220263 | 0.328301 | 0.104775 | 0.621043 | 0.955444 | 0.13726 |
| bonus_part_correctness | tier | nationals | 4095 | 0.885081 | 0.435641 | 0.0599056 | 0.139877 | 0.801709 | 0.425153 | 0.376557 | 0.313911 | 0.042073 | 0.242515 | 0.857246 | 0.133302 |
| bonus_part_correctness | tier | regionals | 5580 | 0.887837 | 0.427154 | 0.0417539 | 0.136177 | 0.812366 | 0.495878 | 0.316487 | 0.339582 | 0.0550904 | 0.375808 | 0.93785 | 0.132579 |
| bonus_part_correctness | tier | winter | 8121 | 0.894549 | 0.411463 | 0.0221693 | 0.130906 | 0.814062 | 0.508435 | 0.305627 | 0.34379 | 0.0594036 | 0.445013 | 0.952753 | 0.13162 |
| bonus_part_correctness | category | Current Events | 216 | 0.893672 | 0.407933 | 0.0628831 | 0.128089 | 0.842593 | 0.467593 | 0.375 | 0.344106 | 0.0448726 | 0.360082 | 0.919955 | 0.129097 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.879642 | 0.440496 | 0.040564 | 0.142906 | 0.786532 | 0.512795 | 0.273737 | 0.335394 | 0.0635151 | 0.432103 | 0.940569 | 0.136883 |
| bonus_part_correctness | category | Geography | 501 | 0.892996 | 0.408442 | 0.0266036 | 0.13047 | 0.816367 | 0.572854 | 0.243513 | 0.332032 | 0.0766689 | 0.59752 | 0.943547 | 0.136906 |
| bonus_part_correctness | category | History | 4068 | 0.896858 | 0.409206 | 0.0368009 | 0.130651 | 0.811455 | 0.549164 | 0.262291 | 0.339591 | 0.0634327 | 0.516408 | 0.949311 | 0.134499 |
| bonus_part_correctness | category | Literature | 4065 | 0.904493 | 0.393082 | 0.0252943 | 0.123697 | 0.827798 | 0.510947 | 0.316851 | 0.342279 | 0.0629596 | 0.447493 | 0.94967 | 0.132661 |
| bonus_part_correctness | category | Mythology | 945 | 0.861519 | 0.454611 | 0.0363361 | 0.148807 | 0.780952 | 0.606349 | 0.174603 | 0.317698 | 0.125593 | 0.605118 | 0.953727 | 0.143495 |
| bonus_part_correctness | category | Other Academic | 219 | 0.865782 | 0.47252 | 0.0685676 | 0.155609 | 0.762557 | 0.493151 | 0.269406 | 0.35101 | 0.0432788 | 0.458432 | 0.927471 | 0.125721 |
| bonus_part_correctness | category | Philosophy | 963 | 0.898196 | 0.407571 | 0.0370086 | 0.129916 | 0.811007 | 0.483904 | 0.327103 | 0.330688 | 0.0651755 | 0.393516 | 0.932506 | 0.138772 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.840278 | 0.485363 | 0.0553763 | 0.159704 | 0.763889 | 0.625 | 0.138889 | 0.328074 | 0.113287 | 0.674513 | 0.965672 | 0.129634 |
| bonus_part_correctness | category | Religion | 1008 | 0.900949 | 0.404136 | 0.0423564 | 0.129409 | 0.820437 | 0.503968 | 0.316468 | 0.347245 | 0.0507431 | 0.417359 | 0.937671 | 0.128524 |
| bonus_part_correctness | category | Science | 4059 | 0.898446 | 0.407823 | 0.0369864 | 0.129026 | 0.817196 | 0.530673 | 0.286524 | 0.339862 | 0.0632792 | 0.463017 | 0.948707 | 0.134463 |
| bonus_part_correctness | category | Social Science | 909 | 0.922087 | 0.353792 | 0.0316941 | 0.10853 | 0.847085 | 0.458746 | 0.388339 | 0.350967 | 0.0528893 | 0.35715 | 0.948602 | 0.124611 |
| bonus_part_correctness | category | Unknown | 5580 | 0.887837 | 0.427154 | 0.0417539 | 0.136177 | 0.812366 | 0.495878 | 0.316487 | 0.339582 | 0.0550904 | 0.375808 | 0.93785 | 0.132579 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.886586 | 0.893986 | 0.00739965 | synergy |
| log_loss | 0.425413 | 0.414747 | -0.0106656 | synergy |
| ece | 0.0192293 | 0.0331832 | 0.0139539 | no-synergy |
| brier | 0.13543 | 0.132227 | -0.00320306 | synergy |
| accuracy_lift_over_all_correct | 0.286728 | 0.292777 | 0.00604862 | synergy |
| part_accuracy | 0.806095 | 0.812144 | 0.00604862 | synergy |
| part_accuracy_macro_team | 0.810061 | 0.81594 | 0.00587905 | synergy |
| part_accuracy_macro_bonus | 0.805663 | 0.808567 | 0.0029038 | synergy |
| exact_acc | 0.509131 | 0.523904 | 0.0147726 | synergy |
| ranked_probability_score | 0.116545 | 0.112309 | -0.0042358 | synergy |
| bonus_total_score_log_loss | 1.02119 | 0.993031 | -0.0281562 | synergy |
| ppb_mae | 2.34809 | 1.88191 | -0.466179 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 4.61439 | 1.16268 | 0.867703 | 2.0387 | 4.06675 | 4.83641 | 5.40649 | 6.11426 | 7.14651 |
| player | theta_1 | 1197 | 0.0598482 | 0.731191 | -2.48167 | -1.32579 | -0.344341 | 0.173991 | 0.564807 | 1.07057 | 2.08566 |
| player | theta_2 | 1197 | 0.0392967 | 0.741118 | -2.86853 | -1.42805 | -0.366735 | 0.149361 | 0.543326 | 1.10073 | 1.8377 |
| player | theta_3 | 1197 | 0.0834153 | 0.723115 | -2.19532 | -1.33291 | -0.320838 | 0.166695 | 0.572831 | 1.18878 | 2.14186 |
| player | theta_4 | 1197 | 0.0613022 | 0.727318 | -2.71095 | -1.33465 | -0.364011 | 0.179332 | 0.554204 | 1.12822 | 1.88824 |
| player | theta_5 | 1197 | -0.0236254 | 0.747048 | -2.67097 | -1.45687 | -0.445669 | 0.107697 | 0.49604 | 1.0234 | 1.5774 |
| player | theta_norm | 1197 | 1.53321 | 0.597984 | 0.319809 | 0.725456 | 1.09 | 1.42743 | 1.89254 | 2.68678 | 3.49461 |
| tossup | beta_1 | 1240 | 0.751929 | 0.512096 | -1.23516 | 0.230253 | 0.403411 | 0.583726 | 0.963037 | 1.85352 | 2.74491 |
| tossup | beta_2 | 1240 | 0.870996 | 0.590758 | -1.01563 | 0.220325 | 0.431654 | 0.651322 | 1.24481 | 2.03237 | 2.86723 |
| tossup | beta_3 | 1240 | 0.739748 | 0.52461 | -0.760325 | 0.221268 | 0.402904 | 0.56493 | 0.8829 | 1.91847 | 2.95484 |
| tossup | beta_4 | 1240 | 0.735878 | 0.521783 | -1.13153 | 0.219055 | 0.400029 | 0.563293 | 0.892914 | 1.91821 | 2.70187 |
| tossup | beta_5 | 1240 | 0.798954 | 0.581141 | -1.83964 | 0.199241 | 0.387195 | 0.585128 | 1.11994 | 1.99441 | 2.80297 |
| tossup | gamma_1 | 1240 | 11.8977 | 70.9628 | 0.548917 | 3.27966 | 4.50211 | 5.12362 | 6.0253 | 21.8944 | 1923.23 |
| tossup | gamma_2 | 1240 | 11.4988 | 55.1251 | 1.08578 | 3.23047 | 4.47487 | 5.1662 | 6.35708 | 21.774 | 1183.59 |
| tossup | gamma_3 | 1240 | 11.4061 | 48.0302 | 0.957975 | 3.27356 | 4.49825 | 5.05293 | 5.93353 | 21.9231 | 1038.52 |
| tossup | gamma_4 | 1240 | 12.8819 | 70.1839 | 0.475958 | 3.2175 | 4.5083 | 5.1163 | 5.95771 | 19.2067 | 1511.28 |
| tossup | gamma_5 | 1240 | 12.4641 | 62.262 | 0.605335 | 3.31055 | 4.56867 | 5.16284 | 6.33526 | 23.0122 | 1453.27 |
| tossup | mu_1 | 1240 | 0.501626 | 0.0984561 | 0.142649 | 0.395372 | 0.449168 | 0.478041 | 0.523107 | 0.708692 | 0.974401 |
| tossup | mu_2 | 1240 | 0.524889 | 0.124865 | 0.138373 | 0.389761 | 0.446563 | 0.485596 | 0.582171 | 0.782168 | 0.974742 |
| tossup | mu_3 | 1240 | 0.502381 | 0.105718 | 0.118296 | 0.389161 | 0.447311 | 0.478816 | 0.517086 | 0.730567 | 0.986674 |
| tossup | mu_4 | 1240 | 0.502404 | 0.106542 | 0.215199 | 0.391534 | 0.449242 | 0.478192 | 0.5147 | 0.738344 | 0.969124 |
| tossup | mu_5 | 1240 | 0.508107 | 0.111298 | 0.142394 | 0.379823 | 0.446945 | 0.47884 | 0.537878 | 0.738601 | 0.983899 |
| tossup | r_1 | 1240 | 0.990638 | 0.772245 | 0.0919517 | 0.231628 | 0.431001 | 0.743462 | 1.33733 | 2.59253 | 5.37652 |
| tossup | r_2 | 1240 | 1.3844 | 1.1109 | 0.0766842 | 0.242065 | 0.532107 | 0.983559 | 2.02599 | 3.65287 | 5.96232 |
| tossup | r_3 | 1240 | 1.00192 | 0.866659 | 0.101003 | 0.211063 | 0.415387 | 0.709131 | 1.25131 | 2.94018 | 5.75533 |
| tossup | r_4 | 1240 | 0.984242 | 0.772977 | 0.0852409 | 0.217451 | 0.433317 | 0.715114 | 1.33591 | 2.67107 | 4.46242 |
| tossup | r_5 | 1240 | 1.12616 | 0.827376 | 0.053081 | 0.220297 | 0.47369 | 0.869889 | 1.61708 | 2.75635 | 4.2474 |
| tossup | r_norm | 1240 | 3.06095 | 0.79393 | 1.20116 | 1.92584 | 2.48636 | 2.98628 | 3.55142 | 4.50454 | 6.34415 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
