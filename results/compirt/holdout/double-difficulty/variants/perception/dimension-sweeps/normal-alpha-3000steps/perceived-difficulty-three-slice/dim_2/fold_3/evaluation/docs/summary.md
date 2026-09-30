# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_2/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_2/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 312024 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.631536 |
| log_loss | 0.528069 |
| ece | 0.0401181 |
| brier | 0.17212 |
| accuracy | 0.76685 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.00319383 |
| probability_std | 0.135005 |
| probability_p10 | 0.569315 |
| probability_p50 | 0.783937 |
| probability_p90 | 0.911014 |
| mean_predictive_variance | 0.164835 |
| integrated_brier_score | 0.10428 |
| joint_tossup_event_log_loss | 6.92067 |
| buzz_position_mae | 0.163756 |
| buzz_position_median_absolute_error | 0.147599 |
| buzz_position_bias | -0.0736129 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.34185 |
| first_buzzer_mean_reciprocal_rank | 0.55468 |
| first_buzzer_log_loss | 1.70651 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.647137 |
| tossup_scorer_player_top1_accuracy | 0.307375 |
| tossup_scorer_team_top1_accuracy | 0.486876 |
| tossup_game_winner_accuracy | 0.772124 |
| tossup_game_margin_mae | 36.1602 |
| tournament_player_ppg_spearman | 0.706108 |
| tournament_player_ppg_mae | 8.81494 |
| tournament_player_ppg_top10_overlap | 0.672414 |
| neg_auroc | 0.631536 |
| neg_average_precision | 0.343072 |
| neg_precision | 0.468132 |
| neg_recall | 0.102011 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0548206 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0853905 |
| no_buzz_calibration_error | 0.0702061 |
| no_buzz_brier | 0.0240688 |
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
| tossup_correctness | aggregate | all | 9080 | 0.631536 | 0.528069 | 0.0401181 | 0.17212 | 0.76685 | 0.770044 | -0.00319383 | 0.135005 | 0.569315 | 0.783937 | 0.911014 | 0.164835 |
| tossup_correctness | tier | fall | 2817 | 0.605132 | 0.523411 | 0.0406828 | 0.168826 | 0.780263 | 0.781683 | -0.00141995 | 0.120709 | 0.611392 | 0.803103 | 0.91577 | 0.157497 |
| tossup_correctness | tier | nationals | 1542 | 0.683468 | 0.549702 | 0.0659474 | 0.184583 | 0.722438 | 0.73476 | -0.0123217 | 0.144496 | 0.474188 | 0.686689 | 0.847241 | 0.200143 |
| tossup_correctness | tier | regionals | 1934 | 0.620332 | 0.549687 | 0.0413125 | 0.18112 | 0.750776 | 0.75698 | -0.00620476 | 0.125381 | 0.604258 | 0.798324 | 0.917317 | 0.157772 |
| tossup_correctness | tier | winter | 2787 | 0.630877 | 0.505806 | 0.0392511 | 0.16231 | 0.78902 | 0.786868 | 0.00215285 | 0.13024 | 0.592543 | 0.799554 | 0.91805 | 0.157616 |
| tossup_correctness | category | Current Events | 125 | 0.657555 | 0.574799 | 0.0705054 | 0.194902 | 0.72 | 0.704 | 0.016 | 0.11268 | 0.523125 | 0.704075 | 0.81612 | 0.204519 |
| tossup_correctness | category | Fine Arts | 1072 | 0.625908 | 0.525801 | 0.0403759 | 0.171848 | 0.767724 | 0.770522 | -0.00279851 | 0.124856 | 0.608798 | 0.806795 | 0.916406 | 0.157113 |
| tossup_correctness | category | Geography | 185 | 0.757203 | 0.521172 | 0.0671464 | 0.172558 | 0.762162 | 0.702703 | 0.0594595 | 0.148529 | 0.482177 | 0.733933 | 0.871246 | 0.186452 |
| tossup_correctness | category | History | 1443 | 0.687626 | 0.506388 | 0.0266156 | 0.165397 | 0.772003 | 0.765073 | 0.00693001 | 0.136842 | 0.547542 | 0.766254 | 0.893045 | 0.17433 |
| tossup_correctness | category | Literature | 1411 | 0.567314 | 0.501642 | 0.0475572 | 0.154907 | 0.811481 | 0.81219 | -0.000708717 | 0.108714 | 0.678203 | 0.853394 | 0.943082 | 0.130487 |
| tossup_correctness | category | Mythology | 320 | 0.578144 | 0.524791 | 0.11315 | 0.169999 | 0.771875 | 0.79375 | -0.021875 | 0.132511 | 0.556448 | 0.759607 | 0.879209 | 0.178931 |
| tossup_correctness | category | Other Academic | 64 | 0.595052 | 0.564429 | 0.0705121 | 0.18808 | 0.734375 | 0.75 | -0.015625 | 0.109302 | 0.565886 | 0.705461 | 0.865382 | 0.194929 |
| tossup_correctness | category | Philosophy | 312 | 0.58129 | 0.501344 | 0.0556721 | 0.160095 | 0.794872 | 0.801282 | -0.00641026 | 0.114095 | 0.635482 | 0.809434 | 0.915288 | 0.152257 |
| tossup_correctness | category | Popular Culture | 104 | 0.50142 | 0.508343 | 0.16371 | 0.162093 | 0.817308 | 0.846154 | -0.0288462 | 0.135781 | 0.554898 | 0.720858 | 0.873599 | 0.184525 |
| tossup_correctness | category | Religion | 358 | 0.641091 | 0.573727 | 0.0603032 | 0.192301 | 0.715084 | 0.726257 | -0.0111732 | 0.142223 | 0.569526 | 0.78087 | 0.910332 | 0.164667 |
| tossup_correctness | category | Science | 1431 | 0.648163 | 0.534455 | 0.0689973 | 0.176774 | 0.755416 | 0.765199 | -0.00978337 | 0.140431 | 0.504406 | 0.721271 | 0.85713 | 0.191235 |
| tossup_correctness | category | Social Science | 321 | 0.636136 | 0.553793 | 0.050096 | 0.186185 | 0.728972 | 0.744548 | -0.0155763 | 0.12398 | 0.564871 | 0.750448 | 0.869981 | 0.181846 |
| tossup_correctness | category | Unknown | 1934 | 0.620332 | 0.549687 | 0.0413125 | 0.18112 | 0.750776 | 0.75698 | -0.00620476 | 0.125381 | 0.604258 | 0.798324 | 0.917317 | 0.157772 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.681163 | 0.584676 | 0.0791721 | 0.200321 | 0.661458 | 0.697917 | -0.0364583 | 0.139571 | 0.465475 | 0.684486 | 0.819702 | 0.205304 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.628802 | 0.570367 | 0.0540263 | 0.192265 | 0.734533 | 0.733408 | 0.00112486 | 0.143104 | 0.49658 | 0.708023 | 0.861158 | 0.19366 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.612267 | 0.549365 | 0.0417356 | 0.18136 | 0.748869 | 0.759276 | -0.0104072 | 0.130138 | 0.560163 | 0.760063 | 0.887909 | 0.176306 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.632471 | 0.503092 | 0.0378879 | 0.161624 | 0.787382 | 0.789125 | -0.00174277 | 0.126484 | 0.594626 | 0.791891 | 0.907963 | 0.162172 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.634693 | 0.519891 | 0.0385475 | 0.167452 | 0.777055 | 0.775342 | 0.00171233 | 0.130153 | 0.607826 | 0.82128 | 0.931386 | 0.147332 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | -2.35614 | 0.673703 | -4.49929 | -3.47879 | -2.76512 | -2.31543 | -1.97313 | -1.29793 | 0.396401 |
| player | theta_2 | 1133 | -1.69998 | 0.883829 | -4.18381 | -3.11161 | -2.34363 | -1.73832 | -1.01686 | -0.309294 | 0.517725 |
| player | theta_norm | 1133 | 3.03814 | 0.667364 | 1.25935 | 2.04175 | 2.5597 | 2.9863 | 3.49904 | 4.22853 | 5.80971 |
| tossup | start_difficulty_d1 | 1240 | -2.34656 | 1.16098 | -4.2618 | -3.81444 | -3.2525 | -2.70886 | -1.33736 | -0.231944 | 0.389272 |
| tossup | start_difficulty_d2 | 1240 | -1.98018 | 1.15121 | -4.86059 | -3.66429 | -2.84346 | -2.21999 | -1.083 | 0.0153895 | 1.17614 |
| tossup | end_difficulty_d1 | 1240 | -3.40679 | 1.27011 | -7.63324 | -5.21024 | -4.29598 | -3.62399 | -2.43795 | -1.20444 | -0.51443 |
| tossup | end_difficulty_d2 | 1240 | -3.04673 | 1.30403 | -8.39284 | -5.06039 | -3.96295 | -3.16537 | -2.07638 | -0.897802 | 0.397845 |
| tossup | total_drop_d1 | 1240 | 1.06023 | 0.393378 | 0.342594 | 0.642623 | 0.847992 | 0.992133 | 1.15073 | 1.71391 | 4.18419 |
| tossup | total_drop_d2 | 1240 | 1.06655 | 0.328358 | 0.543842 | 0.717301 | 0.901771 | 0.991615 | 1.1307 | 1.6476 | 4.05696 |
| tossup | drop_share_1_d1 | 1240 | 0.352641 | 0.049841 | 0.214888 | 0.295876 | 0.319518 | 0.339471 | 0.378827 | 0.447377 | 0.603715 |
| tossup | drop_share_2_d1 | 1240 | 0.336989 | 0.0200887 | 0.248519 | 0.305952 | 0.3247 | 0.337787 | 0.348981 | 0.365626 | 0.505533 |
| tossup | drop_share_3_d1 | 1240 | 0.31037 | 0.0452702 | 0.147765 | 0.224159 | 0.283905 | 0.31804 | 0.33977 | 0.374275 | 0.467791 |
| tossup | drop_share_1_d2 | 1240 | 0.345285 | 0.0441303 | 0.202747 | 0.292185 | 0.315493 | 0.338341 | 0.368616 | 0.424322 | 0.636533 |
| tossup | drop_share_2_d2 | 1240 | 0.339614 | 0.0164355 | 0.237936 | 0.31282 | 0.330852 | 0.340506 | 0.349391 | 0.361652 | 0.422909 |
| tossup | drop_share_3_d2 | 1240 | 0.315101 | 0.0413149 | 0.125531 | 0.240615 | 0.291969 | 0.321341 | 0.342291 | 0.371398 | 0.442933 |
| tossup | r_1 | 1240 | 0.563846 | 0.310735 | 0.0361409 | 0.0819037 | 0.248576 | 0.623236 | 0.860281 | 0.950648 | 0.973953 |
| tossup | r_2 | 1240 | 0.436154 | 0.310735 | 0.0260469 | 0.0493523 | 0.139719 | 0.376764 | 0.751424 | 0.918096 | 0.963859 |
| tossup | r_norm | 1240 | 0.833365 | 0.0813507 | 0.707109 | 0.710035 | 0.759468 | 0.835641 | 0.906497 | 0.953007 | 0.974301 |
