# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_5/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_5/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 321348 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.665483 |
| log_loss | 0.507211 |
| ece | 0.0178723 |
| brier | 0.164604 |
| accuracy | 0.775771 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00572687 |
| probability_std | 0.124347 |
| probability_p10 | 0.585015 |
| probability_p50 | 0.783413 |
| probability_p90 | 0.900264 |
| mean_predictive_variance | 0.166634 |
| integrated_brier_score | 0.102121 |
| joint_tossup_event_log_loss | 6.841 |
| buzz_position_mae | 0.1618 |
| buzz_position_median_absolute_error | 0.146712 |
| buzz_position_bias | -0.071238 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.366189 |
| first_buzzer_mean_reciprocal_rank | 0.575248 |
| first_buzzer_log_loss | 1.66509 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.65837 |
| tossup_scorer_player_top1_accuracy | 0.321041 |
| tossup_scorer_team_top1_accuracy | 0.507267 |
| tossup_game_winner_accuracy | 0.769912 |
| tossup_game_margin_mae | 36.2458 |
| tournament_player_ppg_spearman | 0.698908 |
| tournament_player_ppg_mae | 8.92046 |
| tournament_player_ppg_top10_overlap | 0.662069 |
| neg_auroc | 0.665483 |
| neg_average_precision | 0.398255 |
| neg_precision | 0.571429 |
| neg_recall | 0.0996169 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0541058 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0891545 |
| no_buzz_calibration_error | 0.0739701 |
| no_buzz_brier | 0.0253631 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| tossup_correctness | aggregate | all | 9080 | 0.665483 | 0.507211 | 0.0178723 | 0.164604 | 0.775771 | 0.770044 | 0.00572687 | 0.124347 | 0.585015 | 0.783413 | 0.900264 | 0.166634 |
| tossup_correctness | tier | fall | 2817 | 0.664409 | 0.493646 | 0.0176758 | 0.159001 | 0.786297 | 0.781683 | 0.00461484 | 0.118223 | 0.599867 | 0.794316 | 0.897305 | 0.163659 |
| tossup_correctness | tier | nationals | 1542 | 0.708764 | 0.538459 | 0.0645234 | 0.178925 | 0.743839 | 0.73476 | 0.00907912 | 0.121694 | 0.497165 | 0.685647 | 0.817183 | 0.206026 |
| tossup_correctness | tier | regionals | 1934 | 0.654138 | 0.5276 | 0.023919 | 0.17325 | 0.757497 | 0.75698 | 0.000517063 | 0.109261 | 0.626875 | 0.795265 | 0.903574 | 0.160477 |
| tossup_correctness | tier | winter | 2787 | 0.655191 | 0.489487 | 0.0243043 | 0.156345 | 0.795479 | 0.786868 | 0.00861141 | 0.119114 | 0.629763 | 0.81419 | 0.914658 | 0.152119 |
| tossup_correctness | category | Current Events | 125 | 0.70086 | 0.553518 | 0.0521299 | 0.186099 | 0.704 | 0.704 | 0 | 0.118833 | 0.555051 | 0.736297 | 0.828463 | 0.194674 |
| tossup_correctness | category | Fine Arts | 1072 | 0.679113 | 0.500293 | 0.032836 | 0.162435 | 0.777985 | 0.770522 | 0.00746269 | 0.122718 | 0.583239 | 0.776745 | 0.893753 | 0.169884 |
| tossup_correctness | category | Geography | 185 | 0.780699 | 0.505032 | 0.0607369 | 0.166429 | 0.772973 | 0.702703 | 0.0702703 | 0.164727 | 0.449157 | 0.744061 | 0.877526 | 0.185265 |
| tossup_correctness | category | History | 1443 | 0.706383 | 0.494653 | 0.0182784 | 0.160656 | 0.777547 | 0.765073 | 0.012474 | 0.136666 | 0.551192 | 0.780278 | 0.902171 | 0.168501 |
| tossup_correctness | category | Literature | 1411 | 0.596566 | 0.483369 | 0.0459205 | 0.151789 | 0.810773 | 0.81219 | -0.00141743 | 0.108503 | 0.646017 | 0.814414 | 0.916249 | 0.151125 |
| tossup_correctness | category | Mythology | 320 | 0.589776 | 0.515651 | 0.0862745 | 0.165483 | 0.771875 | 0.79375 | -0.021875 | 0.131242 | 0.549678 | 0.762852 | 0.875063 | 0.178236 |
| tossup_correctness | category | Other Academic | 64 | 0.585938 | 0.561433 | 0.0880655 | 0.187239 | 0.78125 | 0.75 | 0.03125 | 0.114364 | 0.533212 | 0.691249 | 0.833913 | 0.201449 |
| tossup_correctness | category | Philosophy | 312 | 0.589419 | 0.499009 | 0.0428472 | 0.159243 | 0.804487 | 0.801282 | 0.00320513 | 0.11546 | 0.60209 | 0.789678 | 0.895736 | 0.165836 |
| tossup_correctness | category | Popular Culture | 104 | 0.524858 | 0.450273 | 0.0687734 | 0.13692 | 0.846154 | 0.846154 | 0 | 0.0920141 | 0.657294 | 0.793584 | 0.90049 | 0.158703 |
| tossup_correctness | category | Religion | 358 | 0.674882 | 0.549582 | 0.0237247 | 0.184494 | 0.72905 | 0.726257 | 0.0027933 | 0.1343 | 0.568482 | 0.758151 | 0.899433 | 0.175678 |
| tossup_correctness | category | Science | 1431 | 0.67859 | 0.505468 | 0.020468 | 0.16456 | 0.775681 | 0.765199 | 0.0104822 | 0.12421 | 0.574789 | 0.767719 | 0.892173 | 0.172316 |
| tossup_correctness | category | Social Science | 321 | 0.701908 | 0.519671 | 0.0432756 | 0.171225 | 0.750779 | 0.744548 | 0.00623053 | 0.134262 | 0.532128 | 0.737459 | 0.887242 | 0.180421 |
| tossup_correctness | category | Unknown | 1934 | 0.654138 | 0.5276 | 0.023919 | 0.17325 | 0.757497 | 0.75698 | 0.000517063 | 0.109261 | 0.626875 | 0.795265 | 0.903574 | 0.160477 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.685409 | 0.574104 | 0.0712719 | 0.194657 | 0.682292 | 0.697917 | -0.015625 | 0.126626 | 0.481737 | 0.672715 | 0.801188 | 0.208061 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.684677 | 0.536443 | 0.0392026 | 0.178032 | 0.742407 | 0.733408 | 0.00899888 | 0.129429 | 0.518125 | 0.72435 | 0.853542 | 0.191005 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.643852 | 0.528818 | 0.0208862 | 0.173313 | 0.761991 | 0.759276 | 0.00271493 | 0.122462 | 0.578727 | 0.774751 | 0.88357 | 0.173379 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.656317 | 0.488692 | 0.0255583 | 0.156656 | 0.795399 | 0.789125 | 0.00627396 | 0.116942 | 0.608804 | 0.796435 | 0.901436 | 0.162383 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.676113 | 0.495757 | 0.0271568 | 0.159759 | 0.783219 | 0.775342 | 0.00787671 | 0.121901 | 0.615792 | 0.804662 | 0.914801 | 0.155562 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | -1.03543 | 1.02432 | -4.56297 | -3.27199 | -1.41421 | -0.549592 | -0.318949 | -0.126538 | 0.194754 |
| player | theta_2 | 1133 | -2.60307 | 0.747356 | -5.13012 | -3.77073 | -3.08395 | -2.59276 | -2.18972 | -1.07184 | -0.318418 |
| player | theta_3 | 1133 | -0.783162 | 0.56342 | -2.7229 | -1.7814 | -1.20511 | -0.676196 | -0.28807 | -0.101577 | 0.463302 |
| player | theta_4 | 1133 | -0.576036 | 0.404335 | -2.60067 | -1.28355 | -0.801237 | -0.539755 | -0.334552 | 0.0613632 | 0.925168 |
| player | theta_5 | 1133 | -0.617958 | 0.567211 | -3.04366 | -1.86094 | -0.816206 | -0.448119 | -0.269828 | 0.00912841 | 0.864532 |
| player | theta_norm | 1133 | 3.30492 | 0.813356 | 1.62434 | 2.1532 | 2.67697 | 3.2282 | 3.84477 | 4.79193 | 5.90214 |
| tossup | start_difficulty_d1 | 1240 | -1.32831 | 1.24443 | -3.66784 | -3.31953 | -2.65112 | -0.966356 | -0.210327 | 0.192258 | 0.569333 |
| tossup | start_difficulty_d2 | 1240 | -2.63483 | 1.49779 | -4.93431 | -4.20495 | -3.72915 | -3.30891 | -0.703873 | -0.132945 | 0.291921 |
| tossup | start_difficulty_d3 | 1240 | -0.667341 | 0.926881 | -4.2057 | -2.60363 | -1.00972 | -0.277607 | -0.0460844 | 0.216271 | 0.6359 |
| tossup | start_difficulty_d4 | 1240 | -0.373479 | 0.582737 | -2.8181 | -1.61019 | -0.627144 | -0.226791 | -0.00636043 | 0.327073 | 1.22701 |
| tossup | start_difficulty_d5 | 1240 | -0.494544 | 0.699615 | -2.57954 | -1.96044 | -0.891967 | -0.25425 | 0.00200184 | 0.287476 | 1.31478 |
| tossup | end_difficulty_d1 | 1240 | -2.40141 | 1.379 | -6.70414 | -4.77736 | -3.66897 | -1.98703 | -1.1863 | -0.723637 | -0.287655 |
| tossup | end_difficulty_d2 | 1240 | -3.75256 | 1.63887 | -8.63863 | -5.80091 | -4.90217 | -4.2986 | -1.79279 | -1.11859 | -0.578334 |
| tossup | end_difficulty_d3 | 1240 | -1.69353 | 1.02462 | -6.87346 | -3.84239 | -2.09631 | -1.27306 | -1.01368 | -0.713011 | -0.254534 |
| tossup | end_difficulty_d4 | 1240 | -1.38774 | 0.665837 | -5.07258 | -2.7635 | -1.66499 | -1.22284 | -0.979961 | -0.57535 | 0.406433 |
| tossup | end_difficulty_d5 | 1240 | -1.52531 | 0.819387 | -4.42257 | -3.24853 | -1.95517 | -1.23658 | -0.953672 | -0.621841 | 0.50808 |
| tossup | total_drop_d1 | 1240 | 1.0731 | 0.227852 | 0.611246 | 0.884992 | 0.955386 | 1.00924 | 1.11217 | 1.51315 | 3.47884 |
| tossup | total_drop_d2 | 1240 | 1.11773 | 0.461836 | 0.374315 | 0.657871 | 0.875529 | 1.02002 | 1.18681 | 2.01114 | 4.97208 |
| tossup | total_drop_d3 | 1240 | 1.02619 | 0.184638 | 0.75927 | 0.888709 | 0.949838 | 0.992807 | 1.05207 | 1.28889 | 5.00393 |
| tossup | total_drop_d4 | 1240 | 1.01426 | 0.101037 | 0.789708 | 0.897093 | 0.952347 | 0.999351 | 1.04979 | 1.1973 | 2.25448 |
| tossup | total_drop_d5 | 1240 | 1.03076 | 0.139254 | 0.806696 | 0.893906 | 0.9488 | 0.994176 | 1.06019 | 1.31724 | 1.99175 |
| tossup | drop_share_1_d1 | 1240 | 0.33516 | 0.0355294 | 0.253295 | 0.297112 | 0.309235 | 0.322753 | 0.354203 | 0.405294 | 0.504103 |
| tossup | drop_share_2_d1 | 1240 | 0.343443 | 0.0123026 | 0.294036 | 0.32166 | 0.336054 | 0.344279 | 0.351561 | 0.361819 | 0.403807 |
| tossup | drop_share_3_d1 | 1240 | 0.321396 | 0.0324108 | 0.181476 | 0.255463 | 0.305333 | 0.331456 | 0.344631 | 0.357849 | 0.383421 |
| tossup | drop_share_1_d2 | 1240 | 0.361892 | 0.0589214 | 0.203194 | 0.294941 | 0.315671 | 0.350408 | 0.398164 | 0.468064 | 0.650512 |
| tossup | drop_share_2_d2 | 1240 | 0.334401 | 0.0239915 | 0.225268 | 0.297599 | 0.319591 | 0.335627 | 0.347986 | 0.367173 | 0.491376 |
| tossup | drop_share_3_d2 | 1240 | 0.303707 | 0.0514912 | 0.124221 | 0.210497 | 0.269664 | 0.315047 | 0.341855 | 0.368472 | 0.46072 |
| tossup | drop_share_1_d3 | 1240 | 0.316885 | 0.0161932 | 0.270795 | 0.294309 | 0.306379 | 0.314406 | 0.324504 | 0.347945 | 0.411464 |
| tossup | drop_share_2_d3 | 1240 | 0.346275 | 0.00985927 | 0.315918 | 0.329572 | 0.339771 | 0.346564 | 0.352954 | 0.362917 | 0.380934 |
| tossup | drop_share_3_d3 | 1240 | 0.33684 | 0.0168489 | 0.237963 | 0.305235 | 0.328314 | 0.338937 | 0.348239 | 0.360403 | 0.393936 |
| tossup | drop_share_1_d4 | 1240 | 0.311828 | 0.0125159 | 0.277094 | 0.293826 | 0.30364 | 0.310458 | 0.318159 | 0.334109 | 0.370166 |
| tossup | drop_share_2_d4 | 1240 | 0.347065 | 0.00932523 | 0.314873 | 0.331698 | 0.341051 | 0.346891 | 0.353406 | 0.362363 | 0.375176 |
| tossup | drop_share_3_d4 | 1240 | 0.341108 | 0.0132673 | 0.279344 | 0.318858 | 0.333548 | 0.342075 | 0.349752 | 0.360406 | 0.37786 |
| tossup | drop_share_1_d5 | 1240 | 0.316319 | 0.0161266 | 0.268068 | 0.294475 | 0.305083 | 0.313797 | 0.324703 | 0.3486 | 0.380886 |
| tossup | drop_share_2_d5 | 1240 | 0.346777 | 0.00913864 | 0.320475 | 0.331503 | 0.340654 | 0.347023 | 0.35326 | 0.361291 | 0.37566 |
| tossup | drop_share_3_d5 | 1240 | 0.336904 | 0.0174075 | 0.266851 | 0.30315 | 0.327702 | 0.339838 | 0.348873 | 0.360247 | 0.380645 |
| tossup | r_1 | 1240 | 0.217767 | 0.238534 | 0.0158575 | 0.0259046 | 0.0415326 | 0.0804599 | 0.48395 | 0.658556 | 0.782191 |
| tossup | r_2 | 1240 | 0.524546 | 0.292113 | 0.0437374 | 0.0593755 | 0.110937 | 0.663101 | 0.740716 | 0.834039 | 0.92993 |
| tossup | r_3 | 1240 | 0.0961039 | 0.0756021 | 0.0111678 | 0.0263902 | 0.0441652 | 0.0656008 | 0.122487 | 0.265371 | 0.388611 |
| tossup | r_4 | 1240 | 0.0742066 | 0.0461479 | 0.0119216 | 0.0278225 | 0.0424909 | 0.0594553 | 0.0915062 | 0.175213 | 0.271031 |
| tossup | r_5 | 1240 | 0.0873764 | 0.0633082 | 0.0134803 | 0.0274534 | 0.0435108 | 0.0650947 | 0.106889 | 0.23077 | 0.357762 |
| tossup | r_norm | 1240 | 0.701907 | 0.0789741 | 0.521021 | 0.574251 | 0.641505 | 0.700933 | 0.758033 | 0.83911 | 0.93065 |
