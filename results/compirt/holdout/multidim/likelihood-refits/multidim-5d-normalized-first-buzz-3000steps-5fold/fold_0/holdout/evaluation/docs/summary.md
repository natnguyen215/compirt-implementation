# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/likelihood-refits/multidim-5d-normalized-first-buzz-3000steps-5fold/fold_0/holdout/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/likelihood-refits/multidim-5d-normalized-first-buzz-3000steps-5fold/fold_0`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 299053 |
| pyramidal | calibrate_correctness | False |
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.144612 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.887122 |
| log_loss | 0.42405 |
| ece | 0.0166041 |
| brier | 0.134864 |
| part_accuracy | 0.809861 |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.291425 |
| part_accuracy_macro_team | 0.811903 |
| part_accuracy_macro_bonus | 0.805403 |
| probability_std | 0.326718 |
| probability_p10 | 0.0859546 |
| probability_p50 | 0.478096 |
| probability_p90 | 0.932025 |
| mean_predictive_variance | 0.143243 |
| exact_acc | 0.51313 |
| ranked_probability_score | 0.117189 |
| bonus_total_score_log_loss | 1.02505 |
| ppb_mae | 2.36785 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.635681 |
| log_loss | 0.808871 |
| ece | 0.220271 |
| brier | 0.258067 |
| accuracy | 0.629801 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.135449 |
| probability_std | 0.29347 |
| probability_p10 | 0.103289 |
| probability_p50 | 0.619857 |
| probability_p90 | 0.912607 |
| mean_predictive_variance | 0.160332 |
| integrated_brier_score | 0.0948929 |
| joint_tossup_event_log_loss | 6.79924 |
| buzz_position_mae | 0.144941 |
| buzz_position_median_absolute_error | 0.12523 |
| buzz_position_bias | -0.0389374 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.402797 |
| first_buzzer_mean_reciprocal_rank | 0.605685 |
| first_buzzer_log_loss | 1.60382 |
| first_buzzer_events | 9295 |
| first_buzzer_player_replay_accuracy | 0.00860678 |
| first_buzzer_team_replay_accuracy | 0.0104357 |
| tossup_scorer_player_replay_accuracy | 0.0932059 |
| tossup_scorer_team_replay_accuracy | 0.0949045 |
| tossup_game_winner_accuracy | 0.137472 |
| tossup_model_official_winner_accuracy | 0.143162 |
| tossup_game_margin_mae | 53.8217 |
| tossup_game_zero_margin_mae | 54.8195 |
| tournament_player_ppg_spearman | 0.214224 |
| tournament_player_ppg_mae | 23.1421 |
| tournament_player_ppg_top10_overlap | 0.286207 |
| tournament_player_ppg_top10_random_overlap | 0.282327 |
| tournament_player_ppg_top10_adjusted_overlap | -0.0157208 |
| neg_auroc | 0.635681 |
| neg_average_precision | 0.333078 |
| neg_precision | 0.326632 |
| neg_recall | 0.543538 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0907123 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0633615 |
| no_buzz_calibration_error | 0.0500918 |
| no_buzz_brier | 0.0226461 |
| full_pmf_max_mass_error | 5.55112e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9420 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 468 |
| first_buzzer_player_replay_accuracy_events | 9295 |
| first_buzzer_team_replay_accuracy_events | 9295 |
| tossup_scorer_player_replay_accuracy_events | 9420 |
| tossup_scorer_team_replay_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 451 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.137472 |
| tossup_game_margin_mae | 53.8217 |
| tossup_game_zero_margin_mae | 54.8195 |
| tossup_game_margin_mae_games | 471 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 451 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.635681 | 0.808871 | 0.220271 | 0.258067 | 0.629801 | 0.76525 | -0.135449 | 0.29347 | 0.103289 | 0.619857 | 0.912607 | 0.160332 |
| tossup_correctness | tier | fall | 2933 | 0.650265 | 0.81313 | 0.249203 | 0.254557 | 0.642346 | 0.791681 | -0.149335 | 0.29139 | 0.103174 | 0.608217 | 0.902956 | 0.162179 |
| tossup_correctness | tier | nationals | 1584 | 0.616787 | 0.769935 | 0.168285 | 0.252947 | 0.632576 | 0.724747 | -0.0921717 | 0.286888 | 0.141526 | 0.67768 | 0.923305 | 0.15733 |
| tossup_correctness | tier | regionals | 1886 | 0.63736 | 0.829775 | 0.217961 | 0.263941 | 0.611877 | 0.746023 | -0.134146 | 0.299555 | 0.0923581 | 0.6012 | 0.91803 | 0.157948 |
| tossup_correctness | tier | winter | 2892 | 0.642171 | 0.812244 | 0.230142 | 0.260599 | 0.627248 | 0.773167 | -0.14592 | 0.293088 | 0.097937 | 0.60635 | 0.905252 | 0.161657 |
| tossup_correctness | category | Current Events | 124 | 0.586889 | 0.856001 | 0.262217 | 0.275882 | 0.596774 | 0.75 | -0.153226 | 0.282012 | 0.117479 | 0.596656 | 0.892192 | 0.16888 |
| tossup_correctness | category | Fine Arts | 1103 | 0.660076 | 0.771412 | 0.220756 | 0.247077 | 0.651859 | 0.759746 | -0.107888 | 0.28559 | 0.11132 | 0.609991 | 0.895974 | 0.16542 |
| tossup_correctness | category | Geography | 197 | 0.619814 | 0.937449 | 0.245 | 0.300376 | 0.604061 | 0.670051 | -0.0659898 | 0.295389 | 0.0527306 | 0.499883 | 0.843799 | 0.160615 |
| tossup_correctness | category | History | 1491 | 0.665021 | 0.772663 | 0.219877 | 0.241518 | 0.657277 | 0.787391 | -0.130114 | 0.289878 | 0.119307 | 0.634017 | 0.906949 | 0.160826 |
| tossup_correctness | category | Literature | 1472 | 0.606354 | 0.796917 | 0.223381 | 0.252407 | 0.644701 | 0.804348 | -0.159647 | 0.297107 | 0.118476 | 0.685158 | 0.930272 | 0.151348 |
| tossup_correctness | category | Mythology | 332 | 0.617981 | 0.858599 | 0.294876 | 0.274812 | 0.61747 | 0.813253 | -0.195783 | 0.273578 | 0.101336 | 0.572347 | 0.863726 | 0.174707 |
| tossup_correctness | category | Other Academic | 69 | 0.569005 | 0.819017 | 0.27445 | 0.280618 | 0.57971 | 0.753623 | -0.173913 | 0.271308 | 0.135686 | 0.620668 | 0.834529 | 0.175046 |
| tossup_correctness | category | Philosophy | 324 | 0.581467 | 0.758783 | 0.220374 | 0.256582 | 0.611111 | 0.799383 | -0.188272 | 0.275227 | 0.179855 | 0.667107 | 0.91578 | 0.165247 |
| tossup_correctness | category | Popular Culture | 102 | 0.444983 | 1.2149 | 0.398492 | 0.382151 | 0.480392 | 0.833333 | -0.352941 | 0.296095 | 0.065409 | 0.489436 | 0.826921 | 0.160255 |
| tossup_correctness | category | Religion | 372 | 0.617284 | 0.84513 | 0.188925 | 0.273854 | 0.58871 | 0.709677 | -0.120968 | 0.290903 | 0.0983237 | 0.57953 | 0.897349 | 0.163938 |
| tossup_correctness | category | Science | 1487 | 0.638517 | 0.791738 | 0.212861 | 0.254079 | 0.630128 | 0.752522 | -0.122394 | 0.292221 | 0.112848 | 0.626408 | 0.91869 | 0.160278 |
| tossup_correctness | category | Social Science | 336 | 0.64089 | 0.844266 | 0.221723 | 0.270775 | 0.627976 | 0.702381 | -0.0744048 | 0.291259 | 0.0690606 | 0.551813 | 0.868186 | 0.165147 |
| tossup_correctness | category | Unknown | 1886 | 0.63736 | 0.829775 | 0.217961 | 0.263941 | 0.611877 | 0.746023 | -0.134146 | 0.299555 | 0.0923581 | 0.6012 | 0.91803 | 0.157948 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.678249 | 1.3236 | 0.485614 | 0.421197 | 0.390863 | 0.736041 | -0.345178 | 0.223852 | 0.0251933 | 0.183285 | 0.622078 | 0.141828 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.663306 | 1.12967 | 0.388184 | 0.356168 | 0.492386 | 0.735025 | -0.24264 | 0.265307 | 0.0332453 | 0.288813 | 0.742934 | 0.156819 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.643806 | 0.875379 | 0.274953 | 0.283812 | 0.591737 | 0.769436 | -0.177699 | 0.285565 | 0.0856024 | 0.518058 | 0.871286 | 0.168427 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.643783 | 0.725883 | 0.193286 | 0.234051 | 0.660851 | 0.78402 | -0.123168 | 0.276314 | 0.159378 | 0.6563 | 0.919153 | 0.164012 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.6316 | 0.698974 | 0.138294 | 0.218718 | 0.689586 | 0.756008 | -0.0664219 | 0.267003 | 0.217937 | 0.742484 | 0.934603 | 0.1531 |
| bonus_part_correctness | aggregate | all | 25818 | 0.887122 | 0.42405 | 0.0166041 | 0.134864 | 0.809861 | 0.518437 | 0.291425 | 0.326718 | 0.0859546 | 0.478096 | 0.932025 | 0.143243 |
| bonus_part_correctness | tier | fall | 8415 | 0.882054 | 0.425145 | 0.0263991 | 0.136379 | 0.804159 | 0.600475 | 0.203684 | 0.318134 | 0.121911 | 0.621329 | 0.941334 | 0.143304 |
| bonus_part_correctness | tier | nationals | 4179 | 0.87302 | 0.44003 | 0.0179744 | 0.139363 | 0.802345 | 0.413975 | 0.38837 | 0.310551 | 0.0741539 | 0.339566 | 0.879469 | 0.147771 |
| bonus_part_correctness | tier | regionals | 5070 | 0.887987 | 0.419741 | 0.0238859 | 0.132481 | 0.816568 | 0.477318 | 0.33925 | 0.322856 | 0.0812348 | 0.409838 | 0.920197 | 0.144793 |
| bonus_part_correctness | tier | winter | 8154 | 0.890701 | 0.417408 | 0.0216623 | 0.132475 | 0.815428 | 0.512877 | 0.302551 | 0.331754 | 0.0777499 | 0.448788 | 0.935447 | 0.139895 |
| bonus_part_correctness | category | Current Events | 258 | 0.926502 | 0.356229 | 0.0556625 | 0.106461 | 0.864341 | 0.496124 | 0.368217 | 0.332663 | 0.0723068 | 0.472325 | 0.913528 | 0.139006 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.872915 | 0.447988 | 0.022781 | 0.14429 | 0.791545 | 0.506667 | 0.284878 | 0.317784 | 0.0888143 | 0.463337 | 0.922683 | 0.148909 |
| bonus_part_correctness | category | Geography | 453 | 0.870166 | 0.440815 | 0.0339919 | 0.140057 | 0.801325 | 0.600442 | 0.200883 | 0.318923 | 0.100968 | 0.654632 | 0.940193 | 0.142019 |
| bonus_part_correctness | category | History | 4176 | 0.882152 | 0.431576 | 0.0231263 | 0.138166 | 0.800527 | 0.55364 | 0.246887 | 0.328235 | 0.0832749 | 0.551917 | 0.937037 | 0.141212 |
| bonus_part_correctness | category | Literature | 4197 | 0.903382 | 0.395151 | 0.0294431 | 0.123643 | 0.82964 | 0.508458 | 0.321182 | 0.328632 | 0.091275 | 0.457665 | 0.933672 | 0.142 |
| bonus_part_correctness | category | Mythology | 951 | 0.863618 | 0.450399 | 0.0402188 | 0.148188 | 0.784437 | 0.608833 | 0.175605 | 0.304873 | 0.162205 | 0.637869 | 0.940645 | 0.148871 |
| bonus_part_correctness | category | Other Academic | 258 | 0.922576 | 0.368502 | 0.0735019 | 0.114207 | 0.852713 | 0.55814 | 0.294574 | 0.336187 | 0.0686223 | 0.543567 | 0.932302 | 0.136723 |
| bonus_part_correctness | category | Philosophy | 969 | 0.873593 | 0.445868 | 0.0338867 | 0.143201 | 0.794634 | 0.493292 | 0.301342 | 0.312338 | 0.091705 | 0.434418 | 0.918839 | 0.15199 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.855088 | 0.459266 | 0.0643032 | 0.15302 | 0.755776 | 0.620462 | 0.135314 | 0.306751 | 0.130585 | 0.629599 | 0.944151 | 0.14873 |
| bonus_part_correctness | category | Religion | 1041 | 0.88257 | 0.431282 | 0.0284359 | 0.136803 | 0.807877 | 0.509126 | 0.298751 | 0.33262 | 0.0661737 | 0.465189 | 0.920481 | 0.139348 |
| bonus_part_correctness | category | Science | 4152 | 0.886693 | 0.424014 | 0.0189606 | 0.134853 | 0.80973 | 0.529383 | 0.280347 | 0.329776 | 0.0875591 | 0.485459 | 0.935446 | 0.14109 |
| bonus_part_correctness | category | Social Science | 915 | 0.887024 | 0.421952 | 0.0368472 | 0.133201 | 0.82623 | 0.485246 | 0.340984 | 0.342496 | 0.0611007 | 0.37101 | 0.934652 | 0.13148 |
| bonus_part_correctness | category | Unknown | 5070 | 0.887987 | 0.419741 | 0.0238859 | 0.132481 | 0.816568 | 0.477318 | 0.33925 | 0.322856 | 0.0812348 | 0.409838 | 0.920197 | 0.144793 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.887122 | 0.893603 | 0.00648163 | synergy |
| log_loss | 0.42405 | 0.413455 | -0.0105948 | synergy |
| ece | 0.0166041 | 0.0239176 | 0.00731347 | no-synergy |
| brier | 0.134864 | 0.131928 | -0.00293557 | synergy |
| accuracy_lift_over_all_correct | 0.291425 | 0.292664 | 0.00123945 | synergy |
| part_accuracy | 0.809861 | 0.811101 | 0.00123945 | synergy |
| part_accuracy_macro_team | 0.811903 | 0.812432 | 0.000528696 | synergy |
| part_accuracy_macro_bonus | 0.805403 | 0.808617 | 0.00321426 | synergy |
| exact_acc | 0.51313 | 0.515571 | 0.00244016 | synergy |
| ranked_probability_score | 0.117189 | 0.113096 | -0.00409343 | synergy |
| bonus_total_score_log_loss | 1.02505 | 0.996407 | -0.0286404 | synergy |
| ppb_mae | 2.36785 | 1.81969 | -0.548168 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 4.58547 | 1.18912 | 0.88123 | 1.87191 | 4.04502 | 4.79258 | 5.39001 | 6.13523 | 7.12706 |
| player | theta_1 | 1186 | 0.0116578 | 0.754047 | -2.65581 | -1.41105 | -0.428493 | 0.127796 | 0.570272 | 1.04118 | 1.73554 |
| player | theta_2 | 1186 | -0.06155 | 0.746727 | -2.70184 | -1.48565 | -0.50386 | 0.0300899 | 0.45235 | 1.058 | 1.68405 |
| player | theta_3 | 1186 | 0.0742741 | 0.721555 | -2.38459 | -1.28847 | -0.34887 | 0.185003 | 0.56568 | 1.14647 | 1.66899 |
| player | theta_4 | 1186 | 0.0886936 | 0.727055 | -2.88367 | -1.35885 | -0.301534 | 0.222597 | 0.568892 | 1.08824 | 2.00542 |
| player | theta_5 | 1186 | 0.0235752 | 0.769072 | -2.90203 | -1.47111 | -0.396436 | 0.1759 | 0.570145 | 1.04167 | 1.86222 |
| player | theta_norm | 1186 | 1.56096 | 0.588343 | 0.349006 | 0.784965 | 1.13492 | 1.45366 | 1.86474 | 2.74886 | 3.43446 |
| tossup | beta_1 | 1240 | 0.761012 | 0.505207 | -0.916394 | 0.214016 | 0.410784 | 0.602593 | 1.00034 | 1.78057 | 2.89775 |
| tossup | beta_2 | 1240 | 0.825781 | 0.576842 | -1.70534 | 0.190516 | 0.413016 | 0.613012 | 1.17886 | 1.9777 | 3.1531 |
| tossup | beta_3 | 1240 | 0.742568 | 0.509969 | -0.457762 | 0.232513 | 0.411687 | 0.571404 | 0.871337 | 1.90555 | 2.85832 |
| tossup | beta_4 | 1240 | 0.76761 | 0.541083 | -1.28236 | 0.225454 | 0.408957 | 0.586957 | 0.944318 | 1.97106 | 2.81374 |
| tossup | beta_5 | 1240 | 0.804526 | 0.561336 | -0.187339 | 0.209171 | 0.411165 | 0.598136 | 1.08127 | 2.03727 | 2.75417 |
| tossup | gamma_1 | 1240 | 12.5264 | 68.6749 | 0.498091 | 3.35628 | 4.55414 | 5.17628 | 6.24635 | 21.4743 | 1865.3 |
| tossup | gamma_2 | 1240 | 14.1856 | 78.5599 | 0.487463 | 3.3531 | 4.54822 | 5.15229 | 6.31019 | 22.5282 | 1761.95 |
| tossup | gamma_3 | 1240 | 10.6535 | 33.8625 | 1.54288 | 3.36969 | 4.55224 | 5.12256 | 6.00538 | 23.58 | 591.882 |
| tossup | gamma_4 | 1240 | 13.0899 | 75.3656 | 0.610255 | 3.1995 | 4.48093 | 5.11128 | 5.96297 | 21.0742 | 1500.32 |
| tossup | gamma_5 | 1240 | 13.3411 | 79.2629 | 0.823266 | 3.22481 | 4.49578 | 5.18201 | 6.30627 | 20.4134 | 1548.99 |
| tossup | mu_1 | 1240 | 0.500851 | 0.0978373 | 0.108293 | 0.388873 | 0.446361 | 0.480364 | 0.529126 | 0.705102 | 0.939342 |
| tossup | mu_2 | 1240 | 0.51898 | 0.122507 | 0.18736 | 0.390769 | 0.441826 | 0.478791 | 0.569801 | 0.785622 | 0.975223 |
| tossup | mu_3 | 1240 | 0.500222 | 0.103734 | 0.125322 | 0.391258 | 0.447852 | 0.47687 | 0.514945 | 0.733969 | 0.978512 |
| tossup | mu_4 | 1240 | 0.506658 | 0.110417 | 0.181176 | 0.380039 | 0.448917 | 0.4817 | 0.531056 | 0.748593 | 0.984075 |
| tossup | mu_5 | 1240 | 0.509451 | 0.107817 | 0.181949 | 0.382457 | 0.449868 | 0.485329 | 0.537854 | 0.729432 | 0.986621 |
| tossup | r_1 | 1240 | 1.03425 | 0.763746 | 0.0526536 | 0.22506 | 0.446731 | 0.812819 | 1.4515 | 2.55454 | 4.18767 |
| tossup | r_2 | 1240 | 1.28035 | 1.03891 | 0.0553624 | 0.22569 | 0.509677 | 0.887703 | 1.84206 | 3.42714 | 6.0756 |
| tossup | r_3 | 1240 | 0.978942 | 0.809005 | 0.0958271 | 0.208202 | 0.415318 | 0.709769 | 1.23089 | 2.76482 | 4.37581 |
| tossup | r_4 | 1240 | 1.05345 | 0.818114 | 0.0937845 | 0.215547 | 0.437021 | 0.7984 | 1.48315 | 2.73232 | 6.14664 |
| tossup | r_5 | 1240 | 1.12434 | 0.820254 | 0.0753563 | 0.208173 | 0.49835 | 0.919288 | 1.54347 | 2.76872 | 6.77396 |
| tossup | r_norm | 1240 | 3.01975 | 0.760957 | 0.798214 | 1.93021 | 2.47219 | 2.9444 | 3.51478 | 4.34739 | 7.00936 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
