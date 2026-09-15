# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_6/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/three-slice-grid/perceived-difficulty-three-slice/dim_6/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 319701 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.669694 |
| log_loss | 0.514551 |
| ece | 0.0201813 |
| brier | 0.1676 |
| accuracy | 0.769256 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00507724 |
| probability_std | 0.132075 |
| probability_p10 | 0.566891 |
| probability_p50 | 0.776745 |
| probability_p90 | 0.90332 |
| mean_predictive_variance | 0.168268 |
| integrated_brier_score | 0.100834 |
| joint_tossup_event_log_loss | 6.88408 |
| buzz_position_mae | 0.158062 |
| buzz_position_median_absolute_error | 0.141977 |
| buzz_position_bias | -0.0592003 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.349141 |
| first_buzzer_mean_reciprocal_rank | 0.560838 |
| first_buzzer_log_loss | 1.67983 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.653884 |
| tossup_scorer_player_top1_accuracy | 0.322708 |
| tossup_scorer_team_top1_accuracy | 0.500107 |
| tossup_game_winner_accuracy | 0.786957 |
| tossup_game_margin_mae | 36.7927 |
| tournament_player_ppg_spearman | 0.700086 |
| tournament_player_ppg_mae | 8.96346 |
| tournament_player_ppg_top10_overlap | 0.665517 |
| neg_auroc | 0.669694 |
| neg_average_precision | 0.398579 |
| neg_precision | 0.551198 |
| neg_recall | 0.115896 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0581468 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0968015 |
| no_buzz_calibration_error | 0.0836885 |
| no_buzz_brier | 0.0266649 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9257 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 460 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.669694 | 0.514551 | 0.0201813 | 0.1676 | 0.769256 | 0.764178 | 0.00507724 | 0.132075 | 0.566891 | 0.776745 | 0.90332 | 0.168268 |
| tossup_correctness | tier | fall | 2798 | 0.681824 | 0.485924 | 0.0235049 | 0.156055 | 0.789135 | 0.785204 | 0.00393138 | 0.122514 | 0.595449 | 0.791622 | 0.898834 | 0.163827 |
| tossup_correctness | tier | nationals | 1545 | 0.699615 | 0.547588 | 0.0475771 | 0.183619 | 0.727508 | 0.721036 | 0.00647249 | 0.122223 | 0.514186 | 0.685907 | 0.832638 | 0.203668 |
| tossup_correctness | tier | regionals | 2039 | 0.63266 | 0.534443 | 0.0388167 | 0.174031 | 0.7641 | 0.762138 | 0.00196175 | 0.131535 | 0.583209 | 0.792406 | 0.915599 | 0.160151 |
| tossup_correctness | tier | winter | 2875 | 0.664581 | 0.510549 | 0.0241748 | 0.165666 | 0.776 | 0.768348 | 0.00765217 | 0.132253 | 0.590913 | 0.798128 | 0.914672 | 0.159322 |
| tossup_correctness | category | Current Events | 129 | 0.673607 | 0.598947 | 0.0601966 | 0.20642 | 0.682171 | 0.666667 | 0.0155039 | 0.127126 | 0.516436 | 0.694763 | 0.841152 | 0.199161 |
| tossup_correctness | category | Fine Arts | 1074 | 0.652298 | 0.51053 | 0.0353588 | 0.16654 | 0.774674 | 0.776536 | -0.0018622 | 0.132258 | 0.559037 | 0.772999 | 0.895016 | 0.171901 |
| tossup_correctness | category | Geography | 180 | 0.726727 | 0.592465 | 0.0652253 | 0.202168 | 0.716667 | 0.616667 | 0.1 | 0.157878 | 0.401371 | 0.671751 | 0.831019 | 0.203829 |
| tossup_correctness | category | History | 1454 | 0.67476 | 0.518755 | 0.0291121 | 0.1704 | 0.762036 | 0.757909 | 0.00412655 | 0.127324 | 0.551977 | 0.751565 | 0.876372 | 0.181327 |
| tossup_correctness | category | Literature | 1435 | 0.653587 | 0.463098 | 0.0335513 | 0.14366 | 0.812544 | 0.810453 | 0.00209059 | 0.115954 | 0.643926 | 0.841538 | 0.933207 | 0.139519 |
| tossup_correctness | category | Mythology | 324 | 0.664208 | 0.485969 | 0.0508916 | 0.156598 | 0.796296 | 0.79321 | 0.00308642 | 0.122581 | 0.587142 | 0.772329 | 0.884846 | 0.17354 |
| tossup_correctness | category | Other Academic | 71 | 0.380174 | 0.600709 | 0.10076 | 0.202239 | 0.746479 | 0.760563 | -0.0140845 | 0.0869003 | 0.601432 | 0.725166 | 0.834243 | 0.194189 |
| tossup_correctness | category | Philosophy | 310 | 0.65489 | 0.523165 | 0.0256278 | 0.172802 | 0.764516 | 0.76129 | 0.00322581 | 0.116324 | 0.596621 | 0.787358 | 0.907788 | 0.16622 |
| tossup_correctness | category | Popular Culture | 108 | 0.568576 | 0.441602 | 0.164549 | 0.134874 | 0.842593 | 0.888889 | -0.0462963 | 0.118091 | 0.571793 | 0.746908 | 0.856078 | 0.185726 |
| tossup_correctness | category | Religion | 361 | 0.680749 | 0.530435 | 0.0432386 | 0.175249 | 0.759003 | 0.742382 | 0.0166205 | 0.132877 | 0.521555 | 0.73732 | 0.861511 | 0.18769 |
| tossup_correctness | category | Science | 1445 | 0.707069 | 0.515063 | 0.00978156 | 0.169942 | 0.751557 | 0.746021 | 0.00553633 | 0.129479 | 0.560186 | 0.773554 | 0.895936 | 0.171604 |
| tossup_correctness | category | Social Science | 327 | 0.709852 | 0.540377 | 0.0403671 | 0.179706 | 0.737003 | 0.718654 | 0.0183486 | 0.130193 | 0.521557 | 0.716113 | 0.850052 | 0.192416 |
| tossup_correctness | category | Unknown | 2039 | 0.63266 | 0.534443 | 0.0388167 | 0.174031 | 0.7641 | 0.762138 | 0.00196175 | 0.131535 | 0.583209 | 0.792406 | 0.915599 | 0.160151 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.601377 | 0.577236 | 0.101532 | 0.194521 | 0.73224 | 0.743169 | -0.010929 | 0.137141 | 0.467897 | 0.664796 | 0.821325 | 0.204602 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.684679 | 0.544231 | 0.0321601 | 0.181344 | 0.737173 | 0.728796 | 0.00837696 | 0.133186 | 0.518083 | 0.726115 | 0.857321 | 0.190823 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.686512 | 0.516746 | 0.0164532 | 0.169656 | 0.763734 | 0.752568 | 0.0111657 | 0.129641 | 0.553486 | 0.764806 | 0.88618 | 0.175783 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.669947 | 0.488672 | 0.0242296 | 0.157056 | 0.789565 | 0.786087 | 0.00347826 | 0.127301 | 0.589074 | 0.791892 | 0.909138 | 0.162206 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.653192 | 0.524424 | 0.0220961 | 0.170149 | 0.766389 | 0.764393 | 0.00199667 | 0.130242 | 0.582859 | 0.794458 | 0.91809 | 0.159087 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | -0.680247 | 1.07097 | -4.67304 | -3.34528 | -0.486376 | -0.257601 | -0.145062 | 0.0406401 | 0.893004 |
| player | theta_2 | 1197 | -0.298849 | 0.411293 | -2.08887 | -1.00434 | -0.499782 | -0.251221 | -0.123286 | 0.358973 | 1.69365 |
| player | theta_3 | 1197 | -0.292113 | 0.294735 | -1.43429 | -0.769316 | -0.445208 | -0.26813 | -0.149012 | 0.138483 | 1.13177 |
| player | theta_4 | 1197 | -2.62786 | 0.837322 | -5.61443 | -3.88178 | -3.17622 | -2.65664 | -2.16693 | -0.73683 | 0.26652 |
| player | theta_5 | 1197 | -0.267782 | 0.361683 | -1.58178 | -0.817602 | -0.46985 | -0.258179 | -0.120026 | 0.308206 | 1.55083 |
| player | theta_6 | 1197 | -0.256487 | 0.352283 | -1.7005 | -0.840829 | -0.420324 | -0.245002 | -0.102625 | 0.30352 | 1.38532 |
| player | theta_norm | 1197 | 3.06888 | 0.787425 | 1.23792 | 1.9845 | 2.48472 | 2.99567 | 3.54509 | 4.47905 | 5.78593 |
| tossup | start_difficulty_d1 | 1240 | -0.976507 | 1.46235 | -4.20674 | -3.58797 | -2.76807 | -0.133455 | 0.0439552 | 0.244169 | 0.508404 |
| tossup | start_difficulty_d2 | 1240 | -0.0870644 | 0.40355 | -1.71022 | -1.04645 | -0.17323 | 0.0128287 | 0.161325 | 0.327683 | 0.600751 |
| tossup | start_difficulty_d3 | 1240 | -0.0367348 | 0.335196 | -2.19182 | -0.507864 | -0.104944 | 0.0278654 | 0.12491 | 0.290851 | 0.755024 |
| tossup | start_difficulty_d4 | 1240 | -2.64114 | 1.64905 | -5.88807 | -4.52536 | -3.81096 | -3.35508 | -0.370165 | 0.00894251 | 0.459257 |
| tossup | start_difficulty_d5 | 1240 | -0.00741758 | 0.321192 | -2.05921 | -0.497147 | -0.0877879 | 0.0357848 | 0.138963 | 0.386226 | 1.15607 |
| tossup | start_difficulty_d6 | 1240 | -0.00613186 | 0.26934 | -1.17535 | -0.548216 | -0.119901 | 0.0364219 | 0.161304 | 0.35807 | 0.725064 |
| tossup | end_difficulty_d1 | 1240 | -2.05217 | 1.61931 | -6.99916 | -5.132 | -3.72624 | -1.13713 | -0.934961 | -0.717876 | -0.401829 |
| tossup | end_difficulty_d2 | 1240 | -1.10427 | 0.515143 | -3.42309 | -2.28479 | -1.19722 | -0.966561 | -0.797197 | -0.599299 | -0.30106 |
| tossup | end_difficulty_d3 | 1240 | -1.04245 | 0.416048 | -3.84503 | -1.57757 | -1.12017 | -0.964603 | -0.8468 | -0.64332 | -0.141165 |
| tossup | end_difficulty_d4 | 1240 | -3.81633 | 1.88312 | -9.75011 | -6.28715 | -5.03066 | -4.36819 | -1.41514 | -0.961046 | -0.405784 |
| tossup | end_difficulty_d5 | 1240 | -1.00541 | 0.382451 | -3.37379 | -1.61768 | -1.10726 | -0.948547 | -0.835373 | -0.541803 | 0.352072 |
| tossup | end_difficulty_d6 | 1240 | -1.00389 | 0.325011 | -2.4285 | -1.66461 | -1.14108 | -0.95169 | -0.803815 | -0.563176 | -0.13488 |
| tossup | total_drop_d1 | 1240 | 1.07567 | 0.273562 | 0.614146 | 0.893299 | 0.96303 | 1.00189 | 1.06018 | 1.5812 | 3.07404 |
| tossup | total_drop_d2 | 1240 | 1.01721 | 0.125168 | 0.849112 | 0.909571 | 0.951291 | 0.988221 | 1.03551 | 1.24197 | 1.95934 |
| tossup | total_drop_d3 | 1240 | 1.00571 | 0.0932534 | 0.863647 | 0.91551 | 0.961356 | 0.993196 | 1.0267 | 1.10387 | 2.15393 |
| tossup | total_drop_d4 | 1240 | 1.1752 | 0.632815 | 0.409786 | 0.649693 | 0.883348 | 1.01444 | 1.20167 | 2.27846 | 6.11124 |
| tossup | total_drop_d5 | 1240 | 0.997993 | 0.074097 | 0.804 | 0.905959 | 0.957847 | 0.990751 | 1.02492 | 1.10363 | 1.75725 |
| tossup | total_drop_d6 | 1240 | 0.997759 | 0.0672807 | 0.84238 | 0.899691 | 0.95998 | 0.990137 | 1.02837 | 1.11671 | 1.41034 |
| tossup | drop_share_1_d1 | 1240 | 0.328451 | 0.0416886 | 0.251039 | 0.289518 | 0.30161 | 0.311714 | 0.34455 | 0.41657 | 0.513011 |
| tossup | drop_share_2_d1 | 1240 | 0.344495 | 0.0141384 | 0.278844 | 0.320154 | 0.336302 | 0.345102 | 0.353611 | 0.366423 | 0.41696 |
| tossup | drop_share_3_d1 | 1240 | 0.327055 | 0.0378577 | 0.176234 | 0.245266 | 0.317738 | 0.341408 | 0.351257 | 0.362966 | 0.386674 |
| tossup | drop_share_1_d2 | 1240 | 0.307764 | 0.012199 | 0.271721 | 0.289424 | 0.299808 | 0.306835 | 0.315372 | 0.329397 | 0.371409 |
| tossup | drop_share_2_d2 | 1240 | 0.347408 | 0.0107824 | 0.304713 | 0.330257 | 0.340482 | 0.34736 | 0.354585 | 0.364427 | 0.400872 |
| tossup | drop_share_3_d2 | 1240 | 0.344828 | 0.0129447 | 0.281305 | 0.322823 | 0.33711 | 0.345608 | 0.353514 | 0.364258 | 0.384898 |
| tossup | drop_share_1_d3 | 1240 | 0.307201 | 0.0117997 | 0.270722 | 0.288715 | 0.299581 | 0.306373 | 0.314247 | 0.326245 | 0.375144 |
| tossup | drop_share_2_d3 | 1240 | 0.347214 | 0.0108428 | 0.309003 | 0.329426 | 0.33999 | 0.347163 | 0.354014 | 0.365031 | 0.391273 |
| tossup | drop_share_3_d3 | 1240 | 0.345585 | 0.0129336 | 0.265685 | 0.324834 | 0.338405 | 0.346371 | 0.354098 | 0.364985 | 0.37802 |
| tossup | drop_share_1_d4 | 1240 | 0.36303 | 0.0672948 | 0.196112 | 0.289403 | 0.311844 | 0.348568 | 0.401257 | 0.495039 | 0.681167 |
| tossup | drop_share_2_d4 | 1240 | 0.334214 | 0.0266085 | 0.207363 | 0.292969 | 0.318674 | 0.334654 | 0.348548 | 0.370342 | 0.478952 |
| tossup | drop_share_3_d4 | 1240 | 0.302756 | 0.0582916 | 0.110414 | 0.192521 | 0.263768 | 0.318131 | 0.345421 | 0.37466 | 0.468234 |
| tossup | drop_share_1_d5 | 1240 | 0.305634 | 0.0115503 | 0.267656 | 0.287311 | 0.29774 | 0.305489 | 0.312216 | 0.324712 | 0.360848 |
| tossup | drop_share_2_d5 | 1240 | 0.347462 | 0.0109093 | 0.30951 | 0.329713 | 0.33987 | 0.347508 | 0.354988 | 0.365168 | 0.385749 |
| tossup | drop_share_3_d5 | 1240 | 0.346904 | 0.0121663 | 0.292719 | 0.327148 | 0.339507 | 0.347343 | 0.354808 | 0.366028 | 0.383137 |
| tossup | drop_share_1_d6 | 1240 | 0.306274 | 0.0111983 | 0.27252 | 0.288389 | 0.298676 | 0.305968 | 0.314007 | 0.324719 | 0.346643 |
| tossup | drop_share_2_d6 | 1240 | 0.346878 | 0.0106923 | 0.313277 | 0.329662 | 0.339499 | 0.346838 | 0.354486 | 0.364088 | 0.380069 |
| tossup | drop_share_3_d6 | 1240 | 0.346848 | 0.0112782 | 0.308301 | 0.327495 | 0.339708 | 0.346773 | 0.354435 | 0.364915 | 0.384301 |
| tossup | r_1 | 1240 | 0.208739 | 0.266036 | 0.0121675 | 0.0227078 | 0.0320793 | 0.0429659 | 0.550503 | 0.685189 | 0.788275 |
| tossup | r_2 | 1240 | 0.0533256 | 0.0406934 | 0.010371 | 0.0217831 | 0.0310194 | 0.0413645 | 0.0567623 | 0.145776 | 0.299578 |
| tossup | r_3 | 1240 | 0.0482667 | 0.0274185 | 0.0112168 | 0.0219724 | 0.0318954 | 0.0423958 | 0.0568333 | 0.0908246 | 0.243182 |
| tossup | r_4 | 1240 | 0.565074 | 0.311262 | 0.0429458 | 0.0651621 | 0.126546 | 0.717744 | 0.8009 | 0.869001 | 0.943241 |
| tossup | r_5 | 1240 | 0.062406 | 0.0380395 | 0.0110845 | 0.0235288 | 0.0383451 | 0.0528064 | 0.0736298 | 0.136261 | 0.275121 |
| tossup | r_6 | 1240 | 0.0621888 | 0.0349944 | 0.0113994 | 0.0239342 | 0.0388316 | 0.052991 | 0.0748959 | 0.139546 | 0.262323 |
| tossup | r_norm | 1240 | 0.735323 | 0.0878716 | 0.51402 | 0.59673 | 0.661588 | 0.738483 | 0.806432 | 0.871012 | 0.943583 |
