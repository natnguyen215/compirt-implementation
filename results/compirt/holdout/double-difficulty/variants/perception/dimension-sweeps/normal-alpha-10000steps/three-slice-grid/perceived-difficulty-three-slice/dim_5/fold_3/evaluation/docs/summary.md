# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_5/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_5/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 317578 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.668226 |
| log_loss | 0.509196 |
| ece | 0.0320278 |
| brier | 0.164541 |
| accuracy | 0.776322 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00627753 |
| probability_std | 0.135082 |
| probability_p10 | 0.562293 |
| probability_p50 | 0.775066 |
| probability_p90 | 0.904376 |
| mean_predictive_variance | 0.168297 |
| integrated_brier_score | 0.10168 |
| joint_tossup_event_log_loss | 6.86213 |
| buzz_position_mae | 0.161491 |
| buzz_position_median_absolute_error | 0.14599 |
| buzz_position_bias | -0.070415 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.346916 |
| first_buzzer_mean_reciprocal_rank | 0.559222 |
| first_buzzer_log_loss | 1.69449 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.652313 |
| tossup_scorer_player_top1_accuracy | 0.317137 |
| tossup_scorer_team_top1_accuracy | 0.502928 |
| tossup_game_winner_accuracy | 0.769912 |
| tossup_game_margin_mae | 36.354 |
| tournament_player_ppg_spearman | 0.696288 |
| tournament_player_ppg_mae | 9.1197 |
| tournament_player_ppg_top10_overlap | 0.641379 |
| neg_auroc | 0.668226 |
| neg_average_precision | 0.407247 |
| neg_precision | 0.55666 |
| neg_recall | 0.1341 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0543241 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0879263 |
| no_buzz_calibration_error | 0.0727419 |
| no_buzz_brier | 0.0251007 |
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
| tossup_correctness | aggregate | all | 9080 | 0.668226 | 0.509196 | 0.0320278 | 0.164541 | 0.776322 | 0.770044 | 0.00627753 | 0.135082 | 0.562293 | 0.775066 | 0.904376 | 0.168297 |
| tossup_correctness | tier | fall | 2817 | 0.658431 | 0.496759 | 0.0321317 | 0.159699 | 0.785942 | 0.781683 | 0.00425985 | 0.126354 | 0.581749 | 0.790611 | 0.899566 | 0.164472 |
| tossup_correctness | tier | nationals | 1542 | 0.718649 | 0.531716 | 0.0651493 | 0.176345 | 0.740597 | 0.73476 | 0.00583658 | 0.132787 | 0.489401 | 0.685899 | 0.83168 | 0.202625 |
| tossup_correctness | tier | regionals | 1934 | 0.665787 | 0.52361 | 0.0225731 | 0.171382 | 0.764219 | 0.75698 | 0.00723888 | 0.131889 | 0.577247 | 0.780302 | 0.911327 | 0.164326 |
| tossup_correctness | tier | winter | 2787 | 0.646163 | 0.499304 | 0.0355232 | 0.158156 | 0.794761 | 0.786868 | 0.00789379 | 0.130928 | 0.598085 | 0.802482 | 0.920488 | 0.155927 |
| tossup_correctness | category | Current Events | 125 | 0.738329 | 0.540321 | 0.132543 | 0.18068 | 0.688 | 0.704 | -0.016 | 0.125094 | 0.507741 | 0.715081 | 0.816415 | 0.201444 |
| tossup_correctness | category | Fine Arts | 1072 | 0.663202 | 0.507719 | 0.0435841 | 0.165222 | 0.774254 | 0.770522 | 0.00373134 | 0.134908 | 0.559643 | 0.774244 | 0.899222 | 0.170084 |
| tossup_correctness | category | Geography | 185 | 0.793846 | 0.506222 | 0.0794595 | 0.165634 | 0.756757 | 0.702703 | 0.0540541 | 0.160108 | 0.430426 | 0.700876 | 0.855864 | 0.197899 |
| tossup_correctness | category | History | 1443 | 0.717423 | 0.491934 | 0.0357532 | 0.159284 | 0.779626 | 0.765073 | 0.014553 | 0.129025 | 0.556564 | 0.760281 | 0.880333 | 0.177766 |
| tossup_correctness | category | Literature | 1411 | 0.579405 | 0.500011 | 0.0538886 | 0.154037 | 0.802977 | 0.81219 | -0.00921332 | 0.120854 | 0.642515 | 0.840919 | 0.944789 | 0.136548 |
| tossup_correctness | category | Mythology | 320 | 0.595085 | 0.511389 | 0.0858102 | 0.16401 | 0.784375 | 0.79375 | -0.009375 | 0.127509 | 0.551934 | 0.769007 | 0.881105 | 0.175843 |
| tossup_correctness | category | Other Academic | 64 | 0.602865 | 0.551822 | 0.0972905 | 0.183288 | 0.765625 | 0.75 | 0.015625 | 0.104799 | 0.58259 | 0.727783 | 0.846745 | 0.194202 |
| tossup_correctness | category | Philosophy | 312 | 0.600323 | 0.499509 | 0.0576301 | 0.159426 | 0.794872 | 0.801282 | -0.00641026 | 0.121286 | 0.600634 | 0.79267 | 0.910796 | 0.162672 |
| tossup_correctness | category | Popular Culture | 104 | 0.490057 | 0.474266 | 0.118046 | 0.146333 | 0.836538 | 0.846154 | -0.00961538 | 0.102391 | 0.621993 | 0.774705 | 0.88967 | 0.171404 |
| tossup_correctness | category | Religion | 358 | 0.691758 | 0.542273 | 0.0300251 | 0.181273 | 0.72905 | 0.726257 | 0.0027933 | 0.137405 | 0.536642 | 0.745314 | 0.885568 | 0.181835 |
| tossup_correctness | category | Science | 1431 | 0.683526 | 0.505343 | 0.0439495 | 0.164517 | 0.781272 | 0.765199 | 0.0160727 | 0.138447 | 0.529817 | 0.750549 | 0.885447 | 0.178399 |
| tossup_correctness | category | Social Science | 321 | 0.698183 | 0.525179 | 0.0493244 | 0.173038 | 0.757009 | 0.744548 | 0.0124611 | 0.131886 | 0.536486 | 0.734329 | 0.876819 | 0.184925 |
| tossup_correctness | category | Unknown | 1934 | 0.665787 | 0.52361 | 0.0225731 | 0.171382 | 0.764219 | 0.75698 | 0.00723888 | 0.131889 | 0.577247 | 0.780302 | 0.911327 | 0.164326 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.715775 | 0.559348 | 0.0781805 | 0.188372 | 0.697917 | 0.697917 | 0 | 0.132334 | 0.467263 | 0.666068 | 0.795486 | 0.21036 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.690935 | 0.536396 | 0.0434743 | 0.177964 | 0.742407 | 0.733408 | 0.00899888 | 0.137986 | 0.499429 | 0.716379 | 0.855081 | 0.192728 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.644971 | 0.532461 | 0.0354695 | 0.173886 | 0.760633 | 0.759276 | 0.00135747 | 0.133172 | 0.555757 | 0.76469 | 0.888619 | 0.174646 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.666381 | 0.487962 | 0.0360922 | 0.155972 | 0.793656 | 0.789125 | 0.0045312 | 0.124854 | 0.590362 | 0.787083 | 0.904067 | 0.164214 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.669689 | 0.500871 | 0.0417403 | 0.160234 | 0.786644 | 0.775342 | 0.0113014 | 0.136781 | 0.582785 | 0.797883 | 0.923382 | 0.157301 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | -0.688408 | 1.07668 | -4.91599 | -3.29299 | -0.499736 | -0.258568 | -0.133642 | 0.0843287 | 0.924814 |
| player | theta_2 | 1133 | -2.65188 | 0.837148 | -5.18062 | -3.92119 | -3.21968 | -2.687 | -2.19792 | -0.763787 | 0.205577 |
| player | theta_3 | 1133 | -0.263064 | 0.363357 | -1.64756 | -0.873397 | -0.448498 | -0.231228 | -0.0974335 | 0.320009 | 1.48607 |
| player | theta_4 | 1133 | -0.265084 | 0.384291 | -2.18442 | -0.924009 | -0.433714 | -0.241928 | -0.0899753 | 0.376546 | 1.89756 |
| player | theta_5 | 1133 | -0.242062 | 0.263946 | -1.29109 | -0.691934 | -0.388217 | -0.234974 | -0.10592 | 0.182982 | 0.872916 |
| player | theta_norm | 1133 | 3.05386 | 0.76574 | 1.3261 | 1.94622 | 2.51383 | 2.99496 | 3.52125 | 4.41466 | 5.51044 |
| tossup | start_difficulty_d1 | 1240 | -0.942681 | 1.41816 | -4.05375 | -3.48859 | -2.61884 | -0.131877 | 0.0507274 | 0.266635 | 0.553648 |
| tossup | start_difficulty_d2 | 1240 | -2.62659 | 1.63744 | -5.96743 | -4.50887 | -3.79088 | -3.32348 | -0.41965 | 0.0415433 | 0.586005 |
| tossup | start_difficulty_d3 | 1240 | -0.0320646 | 0.402665 | -1.90185 | -0.926987 | -0.140481 | 0.0236782 | 0.189258 | 0.481379 | 1.41209 |
| tossup | start_difficulty_d4 | 1240 | -0.0349681 | 0.364712 | -1.91601 | -0.746567 | -0.151833 | 0.031415 | 0.186707 | 0.41731 | 0.80225 |
| tossup | start_difficulty_d5 | 1240 | -0.000407007 | 0.331448 | -2.15693 | -0.527745 | -0.103898 | 0.0428459 | 0.167982 | 0.392783 | 1.24736 |
| tossup | end_difficulty_d1 | 1240 | -2.01346 | 1.57436 | -7.2781 | -5.05837 | -3.56183 | -1.14066 | -0.931329 | -0.680275 | -0.349429 |
| tossup | end_difficulty_d2 | 1240 | -3.7958 | 1.87604 | -10.6584 | -6.36588 | -4.98737 | -4.31809 | -1.46767 | -0.924291 | -0.196772 |
| tossup | end_difficulty_d3 | 1240 | -1.0402 | 0.503499 | -3.93225 | -2.15374 | -1.16395 | -0.962943 | -0.763218 | -0.434195 | 0.683923 |
| tossup | end_difficulty_d4 | 1240 | -1.0383 | 0.436736 | -3.49827 | -1.91927 | -1.17831 | -0.95075 | -0.772172 | -0.521958 | -0.0373102 |
| tossup | end_difficulty_d5 | 1240 | -0.997987 | 0.407533 | -3.90973 | -1.62056 | -1.11378 | -0.940245 | -0.790796 | -0.530297 | 0.373814 |
| tossup | total_drop_d1 | 1240 | 1.07078 | 0.278015 | 0.588155 | 0.876694 | 0.960064 | 1.00009 | 1.05951 | 1.59143 | 4.11309 |
| tossup | total_drop_d2 | 1240 | 1.16921 | 0.64542 | 0.361793 | 0.643285 | 0.872904 | 1.00988 | 1.19239 | 2.29022 | 7.10693 |
| tossup | total_drop_d3 | 1240 | 1.00813 | 0.116804 | 0.728166 | 0.896967 | 0.948275 | 0.986705 | 1.03396 | 1.19497 | 2.32743 |
| tossup | total_drop_d4 | 1240 | 1.00333 | 0.0830586 | 0.806175 | 0.901027 | 0.95141 | 0.991059 | 1.03581 | 1.16285 | 1.58225 |
| tossup | total_drop_d5 | 1240 | 0.99758 | 0.0864516 | 0.812126 | 0.90183 | 0.952433 | 0.985482 | 1.02604 | 1.10976 | 1.92284 |
| tossup | drop_share_1_d1 | 1240 | 0.327476 | 0.0391854 | 0.261422 | 0.29082 | 0.302197 | 0.312274 | 0.340828 | 0.411341 | 0.502788 |
| tossup | drop_share_2_d1 | 1240 | 0.344392 | 0.0134181 | 0.293644 | 0.320641 | 0.336257 | 0.345136 | 0.35297 | 0.363978 | 0.411504 |
| tossup | drop_share_3_d1 | 1240 | 0.328132 | 0.0359041 | 0.180525 | 0.250236 | 0.317433 | 0.340636 | 0.351038 | 0.36384 | 0.394773 |
| tossup | drop_share_1_d2 | 1240 | 0.35821 | 0.0667872 | 0.202029 | 0.286826 | 0.310507 | 0.343687 | 0.392631 | 0.488798 | 0.68861 |
| tossup | drop_share_2_d2 | 1240 | 0.335421 | 0.027016 | 0.211596 | 0.294937 | 0.320912 | 0.336453 | 0.348686 | 0.373326 | 0.507254 |
| tossup | drop_share_3_d2 | 1240 | 0.306369 | 0.0572588 | 0.0997945 | 0.192187 | 0.269848 | 0.323608 | 0.345997 | 0.377364 | 0.449866 |
| tossup | drop_share_1_d3 | 1240 | 0.306235 | 0.012098 | 0.270663 | 0.286396 | 0.29819 | 0.30628 | 0.313234 | 0.326872 | 0.368668 |
| tossup | drop_share_2_d3 | 1240 | 0.34734 | 0.0111781 | 0.308043 | 0.329865 | 0.339611 | 0.347102 | 0.354871 | 0.365758 | 0.387525 |
| tossup | drop_share_3_d3 | 1240 | 0.346425 | 0.0130431 | 0.300028 | 0.32441 | 0.338706 | 0.34701 | 0.354597 | 0.367043 | 0.382851 |
| tossup | drop_share_1_d4 | 1240 | 0.306607 | 0.0116593 | 0.273051 | 0.289329 | 0.29819 | 0.306039 | 0.314053 | 0.326169 | 0.363223 |
| tossup | drop_share_2_d4 | 1240 | 0.347507 | 0.010404 | 0.319078 | 0.330143 | 0.340582 | 0.34718 | 0.354176 | 0.365277 | 0.382169 |
| tossup | drop_share_3_d4 | 1240 | 0.345885 | 0.0122156 | 0.293442 | 0.325194 | 0.337752 | 0.346142 | 0.354703 | 0.364745 | 0.379195 |
| tossup | drop_share_1_d5 | 1240 | 0.306265 | 0.0121787 | 0.264445 | 0.288289 | 0.298367 | 0.305263 | 0.313472 | 0.325843 | 0.371776 |
| tossup | drop_share_2_d5 | 1240 | 0.346951 | 0.011113 | 0.310351 | 0.328825 | 0.339052 | 0.347049 | 0.354911 | 0.365521 | 0.388335 |
| tossup | drop_share_3_d5 | 1240 | 0.346784 | 0.0130058 | 0.267008 | 0.326874 | 0.339511 | 0.347545 | 0.355134 | 0.365328 | 0.388078 |
| tossup | r_1 | 1240 | 0.223011 | 0.284059 | 0.0116109 | 0.0228751 | 0.0333986 | 0.0461791 | 0.589965 | 0.732206 | 0.826079 |
| tossup | r_2 | 1240 | 0.581583 | 0.320013 | 0.0403499 | 0.0661284 | 0.126328 | 0.740603 | 0.822319 | 0.889152 | 0.950253 |
| tossup | r_3 | 1240 | 0.0628027 | 0.0402309 | 0.0114407 | 0.0242971 | 0.0384136 | 0.0530178 | 0.0713045 | 0.147744 | 0.291344 |
| tossup | r_4 | 1240 | 0.0685541 | 0.0405821 | 0.0124112 | 0.0265167 | 0.0420389 | 0.0571663 | 0.0803609 | 0.156903 | 0.266276 |
| tossup | r_5 | 1240 | 0.0640495 | 0.0325506 | 0.013332 | 0.0272578 | 0.0426332 | 0.0559107 | 0.0771525 | 0.127726 | 0.280677 |
| tossup | r_norm | 1240 | 0.762329 | 0.082765 | 0.542467 | 0.631799 | 0.696638 | 0.76407 | 0.827439 | 0.890881 | 0.950579 |
