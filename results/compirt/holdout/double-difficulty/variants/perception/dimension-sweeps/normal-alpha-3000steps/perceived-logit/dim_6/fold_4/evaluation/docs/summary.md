# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_6/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_6/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 335302 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.560969 |
| log_loss | 0.562318 |
| ece | 0.0777519 |
| brier | 0.180273 |
| accuracy | 0.771521 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00183387 |
| probability_std | 0.115447 |
| probability_p10 | 0.642867 |
| probability_p50 | 0.852781 |
| probability_p90 | 0.934532 |
| mean_predictive_variance | 0.136521 |
| integrated_brier_score | 0.171184 |
| joint_tossup_event_log_loss | 7.69551 |
| buzz_position_mae | 0.32845 |
| buzz_position_median_absolute_error | 0.327257 |
| buzz_position_bias | -0.313898 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.339051 |
| first_buzzer_mean_reciprocal_rank | 0.550723 |
| first_buzzer_log_loss | 1.70857 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.620928 |
| tossup_scorer_player_top1_accuracy | 0.254478 |
| tossup_scorer_team_top1_accuracy | 0.39435 |
| tossup_game_winner_accuracy | 0.693654 |
| tossup_game_margin_mae | 46.1425 |
| tournament_player_ppg_spearman | 0.56467 |
| tournament_player_ppg_mae | 11.0227 |
| tournament_player_ppg_top10_overlap | 0.603448 |
| neg_auroc | 0.560969 |
| neg_average_precision | 0.285242 |
| neg_precision | 0.42735 |
| neg_recall | 0.0237982 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.033282 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.218854 |
| no_buzz_calibration_error | 0.207127 |
| no_buzz_brier | 0.0635808 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.560969 | 0.562318 | 0.0777519 | 0.180273 | 0.771521 | 0.773355 | -0.00183387 | 0.115447 | 0.642867 | 0.852781 | 0.934532 | 0.136521 |
| tossup_correctness | tier | fall | 2876 | 0.541561 | 0.538819 | 0.0708041 | 0.169561 | 0.791725 | 0.793115 | -0.00139082 | 0.0903363 | 0.715503 | 0.871932 | 0.934308 | 0.122059 |
| tossup_correctness | tier | nationals | 1579 | 0.591697 | 0.590599 | 0.0728735 | 0.197757 | 0.724509 | 0.729576 | -0.0050665 | 0.133752 | 0.542815 | 0.722697 | 0.904954 | 0.183194 |
| tossup_correctness | tier | regionals | 1990 | 0.539179 | 0.579782 | 0.0910499 | 0.187172 | 0.762312 | 0.765829 | -0.00351759 | 0.120376 | 0.622854 | 0.809553 | 0.92961 | 0.151322 |
| tossup_correctness | tier | winter | 2825 | 0.558089 | 0.558133 | 0.0808022 | 0.176545 | 0.783717 | 0.783009 | 0.000707965 | 0.0838417 | 0.733395 | 0.882797 | 0.941335 | 0.114731 |
| tossup_correctness | category | Current Events | 123 | 0.635363 | 0.529004 | 0.0795697 | 0.172766 | 0.756098 | 0.764228 | -0.00813008 | 0.128062 | 0.596244 | 0.826754 | 0.920793 | 0.14973 |
| tossup_correctness | category | Fine Arts | 1093 | 0.569862 | 0.573465 | 0.0857638 | 0.183559 | 0.767612 | 0.769442 | -0.00182983 | 0.108256 | 0.680146 | 0.876767 | 0.939194 | 0.124629 |
| tossup_correctness | category | Geography | 191 | 0.675783 | 0.622871 | 0.125985 | 0.212452 | 0.680628 | 0.691099 | -0.0104712 | 0.12097 | 0.621206 | 0.848483 | 0.920342 | 0.14353 |
| tossup_correctness | category | History | 1469 | 0.567515 | 0.574562 | 0.0738078 | 0.1869 | 0.761062 | 0.758339 | 0.00272294 | 0.10793 | 0.644446 | 0.846924 | 0.923545 | 0.140771 |
| tossup_correctness | category | Literature | 1436 | 0.53222 | 0.515348 | 0.084817 | 0.157892 | 0.811978 | 0.81546 | -0.00348189 | 0.106715 | 0.683612 | 0.88562 | 0.948166 | 0.11711 |
| tossup_correctness | category | Mythology | 325 | 0.620366 | 0.430598 | 0.0432933 | 0.132096 | 0.84 | 0.843077 | -0.00307692 | 0.111586 | 0.659278 | 0.882396 | 0.933255 | 0.123221 |
| tossup_correctness | category | Other Academic | 67 | 0.606469 | 0.513621 | 0.100319 | 0.162992 | 0.791045 | 0.791045 | 0 | 0.136351 | 0.581242 | 0.779917 | 0.923292 | 0.160984 |
| tossup_correctness | category | Philosophy | 322 | 0.489431 | 0.589653 | 0.123963 | 0.184948 | 0.782609 | 0.785714 | -0.00310559 | 0.111994 | 0.667262 | 0.880866 | 0.94068 | 0.123088 |
| tossup_correctness | category | Popular Culture | 100 | 0.615935 | 0.371688 | 0.0606607 | 0.109209 | 0.87 | 0.89 | -0.02 | 0.0976156 | 0.712678 | 0.856851 | 0.906586 | 0.132007 |
| tossup_correctness | category | Religion | 365 | 0.584421 | 0.643133 | 0.125495 | 0.210748 | 0.717808 | 0.723288 | -0.00547945 | 0.112751 | 0.653076 | 0.881461 | 0.930856 | 0.125345 |
| tossup_correctness | category | Science | 1456 | 0.57299 | 0.557443 | 0.0561805 | 0.180264 | 0.767857 | 0.76717 | 0.000686813 | 0.117354 | 0.619403 | 0.833482 | 0.924383 | 0.145444 |
| tossup_correctness | category | Social Science | 333 | 0.509145 | 0.649381 | 0.121055 | 0.2138 | 0.732733 | 0.72973 | 0.003003 | 0.112682 | 0.643284 | 0.853984 | 0.923289 | 0.138806 |
| tossup_correctness | category | Unknown | 1990 | 0.539179 | 0.579782 | 0.0910499 | 0.187172 | 0.762312 | 0.765829 | -0.00351759 | 0.120376 | 0.622854 | 0.809553 | 0.92961 | 0.151322 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.529353 | 0.580922 | 0.0951182 | 0.189573 | 0.765363 | 0.748603 | 0.0167598 | 0.1112 | 0.641919 | 0.805861 | 0.893522 | 0.159123 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.491495 | 0.603631 | 0.104286 | 0.197679 | 0.749216 | 0.754441 | -0.00522466 | 0.117518 | 0.611975 | 0.823664 | 0.907919 | 0.152836 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.546409 | 0.569661 | 0.0731065 | 0.185037 | 0.763958 | 0.766682 | -0.00272356 | 0.108904 | 0.647934 | 0.841032 | 0.919781 | 0.14267 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.581701 | 0.529748 | 0.0667979 | 0.168577 | 0.788113 | 0.787441 | 0.000671592 | 0.112033 | 0.650843 | 0.862237 | 0.932653 | 0.133456 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.568017 | 0.57517 | 0.0839042 | 0.182309 | 0.768033 | 0.771758 | -0.00372503 | 0.120773 | 0.641459 | 0.872954 | 0.945938 | 0.128368 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1196 | -1.05403 | 1.01598 | -3.53201 | -2.43985 | -1.70108 | -1.24779 | -0.660631 | 1.12505 | 2.11998 |
| player | beta | 1196 | -4.11542 | 1.30542 | -7.33485 | -6.66809 | -4.94758 | -3.79363 | -3.07922 | -2.46621 | -2.03289 |
| player | theta_1 | 1196 | 0.627046 | 0.749581 | -2.11589 | -0.802 | 0.192038 | 0.804611 | 1.15312 | 1.60092 | 2.78172 |
| player | theta_2 | 1196 | 0.698452 | 0.971382 | -2.45289 | -1.11198 | 0.0279366 | 0.911525 | 1.45284 | 1.96213 | 2.96845 |
| player | theta_3 | 1196 | 0.660386 | 0.824842 | -2.60567 | -0.91201 | 0.145425 | 0.825356 | 1.22729 | 1.82011 | 2.62197 |
| player | theta_4 | 1196 | 0.6416 | 0.777935 | -1.72205 | -0.796588 | 0.177079 | 0.760758 | 1.21812 | 1.72572 | 2.57378 |
| player | theta_5 | 1196 | 0.570528 | 0.614743 | -1.69399 | -0.665123 | 0.31427 | 0.678283 | 0.937964 | 1.37684 | 2.69135 |
| player | theta_6 | 1196 | 0.580903 | 0.621954 | -1.69312 | -0.682852 | 0.294181 | 0.717876 | 0.975059 | 1.37016 | 2.353 |
| player | theta_norm | 1196 | 2.30852 | 0.784692 | 0.182458 | 0.868233 | 1.81367 | 2.37797 | 2.81989 | 3.51042 | 5.45536 |
| tossup | start_difficulty_d1 | 1240 | -0.694979 | 0.381875 | -2.01392 | -1.38052 | -0.924327 | -0.685005 | -0.424671 | -0.0916516 | 0.274484 |
| tossup | start_difficulty_d2 | 1240 | -0.720748 | 0.405265 | -2.00791 | -1.45275 | -0.974908 | -0.704802 | -0.389852 | -0.143691 | 0.210039 |
| tossup | start_difficulty_d3 | 1240 | -0.706265 | 0.446381 | -2.26951 | -1.56806 | -0.966298 | -0.630908 | -0.40088 | -0.0645178 | 0.21606 |
| tossup | start_difficulty_d4 | 1240 | -0.684681 | 0.392249 | -1.89442 | -1.36891 | -0.972338 | -0.670842 | -0.385161 | -0.0665423 | 0.269114 |
| tossup | start_difficulty_d5 | 1240 | -0.644821 | 0.341554 | -1.52639 | -1.17503 | -0.888294 | -0.657937 | -0.389218 | -0.0628272 | 0.30427 |
| tossup | start_difficulty_d6 | 1240 | -0.653167 | 0.360861 | -1.82995 | -1.27368 | -0.903957 | -0.661622 | -0.388253 | -0.0700734 | 0.259937 |
| tossup | end_difficulty_d1 | 1240 | -1.59027 | 0.340641 | -2.71148 | -2.1656 | -1.81643 | -1.57791 | -1.37795 | -1.0223 | -0.523737 |
| tossup | end_difficulty_d2 | 1240 | -1.59416 | 0.332524 | -2.53333 | -2.1324 | -1.82803 | -1.58368 | -1.37593 | -1.05757 | -0.517236 |
| tossup | end_difficulty_d3 | 1240 | -1.60295 | 0.395704 | -3.02879 | -2.35929 | -1.82617 | -1.55972 | -1.33795 | -1.01571 | -0.56355 |
| tossup | end_difficulty_d4 | 1240 | -1.58821 | 0.355719 | -2.56047 | -2.19435 | -1.82907 | -1.58334 | -1.34726 | -0.993869 | -0.545516 |
| tossup | end_difficulty_d5 | 1240 | -1.56078 | 0.325399 | -2.48385 | -2.09007 | -1.78601 | -1.56027 | -1.35364 | -0.998917 | -0.465973 |
| tossup | end_difficulty_d6 | 1240 | -1.5666 | 0.339546 | -2.52321 | -2.13492 | -1.77893 | -1.55366 | -1.35084 | -1.02052 | -0.504567 |
| tossup | total_drop_d1 | 1240 | 0.895294 | 0.187481 | 0.325065 | 0.589621 | 0.774106 | 0.885635 | 1.02836 | 1.20398 | 1.46978 |
| tossup | total_drop_d2 | 1240 | 0.873409 | 0.210083 | 0.289871 | 0.466991 | 0.745754 | 0.885368 | 1.03178 | 1.17914 | 1.62551 |
| tossup | total_drop_d3 | 1240 | 0.896683 | 0.200281 | 0.352635 | 0.549361 | 0.778687 | 0.888351 | 1.03265 | 1.20527 | 1.56043 |
| tossup | total_drop_d4 | 1240 | 0.903531 | 0.189826 | 0.360501 | 0.580045 | 0.783114 | 0.898511 | 1.02498 | 1.21687 | 1.49424 |
| tossup | total_drop_d5 | 1240 | 0.915961 | 0.16316 | 0.556238 | 0.688812 | 0.789625 | 0.894142 | 1.0286 | 1.20433 | 1.50492 |
| tossup | total_drop_d6 | 1240 | 0.913437 | 0.164517 | 0.480196 | 0.689058 | 0.787922 | 0.892545 | 1.02416 | 1.20677 | 1.49628 |
| tossup | drop_share_1_d1 | 1240 | 0.311995 | 0.0174318 | 0.247978 | 0.283827 | 0.300346 | 0.311719 | 0.322563 | 0.341917 | 0.386387 |
| tossup | drop_share_2_d1 | 1240 | 0.336884 | 0.0142164 | 0.258241 | 0.312571 | 0.328181 | 0.337757 | 0.346189 | 0.359249 | 0.382935 |
| tossup | drop_share_3_d1 | 1240 | 0.35112 | 0.0185803 | 0.287181 | 0.323921 | 0.339022 | 0.349441 | 0.361226 | 0.382016 | 0.46272 |
| tossup | drop_share_1_d2 | 1240 | 0.313077 | 0.0191235 | 0.243652 | 0.285456 | 0.300688 | 0.312317 | 0.323845 | 0.344431 | 0.413443 |
| tossup | drop_share_2_d2 | 1240 | 0.33545 | 0.016578 | 0.260804 | 0.303239 | 0.326482 | 0.337366 | 0.346911 | 0.358256 | 0.381701 |
| tossup | drop_share_3_d2 | 1240 | 0.351473 | 0.0220382 | 0.27025 | 0.321434 | 0.337712 | 0.349114 | 0.361131 | 0.391851 | 0.460222 |
| tossup | drop_share_1_d3 | 1240 | 0.312925 | 0.02062 | 0.24063 | 0.283315 | 0.300136 | 0.310922 | 0.323115 | 0.350932 | 0.422927 |
| tossup | drop_share_2_d3 | 1240 | 0.336997 | 0.0146315 | 0.270886 | 0.31155 | 0.328118 | 0.337828 | 0.346862 | 0.359576 | 0.377588 |
| tossup | drop_share_3_d3 | 1240 | 0.350077 | 0.019718 | 0.261117 | 0.318683 | 0.338736 | 0.349724 | 0.360323 | 0.381171 | 0.446002 |
| tossup | drop_share_1_d4 | 1240 | 0.311879 | 0.01824 | 0.241553 | 0.283664 | 0.299887 | 0.311469 | 0.323036 | 0.342892 | 0.379548 |
| tossup | drop_share_2_d4 | 1240 | 0.336933 | 0.0142768 | 0.275021 | 0.311787 | 0.328758 | 0.337829 | 0.346626 | 0.358188 | 0.379378 |
| tossup | drop_share_3_d4 | 1240 | 0.351189 | 0.0195188 | 0.295885 | 0.323793 | 0.339398 | 0.349622 | 0.360631 | 0.383334 | 0.455252 |
| tossup | drop_share_1_d5 | 1240 | 0.311408 | 0.0165897 | 0.254954 | 0.284612 | 0.300587 | 0.311422 | 0.321959 | 0.338107 | 0.366638 |
| tossup | drop_share_2_d5 | 1240 | 0.338171 | 0.0127706 | 0.297392 | 0.317485 | 0.32937 | 0.338333 | 0.347216 | 0.359416 | 0.374819 |
| tossup | drop_share_3_d5 | 1240 | 0.350421 | 0.016849 | 0.295906 | 0.324772 | 0.338607 | 0.349864 | 0.361372 | 0.378808 | 0.419564 |
| tossup | drop_share_1_d6 | 1240 | 0.312217 | 0.0170314 | 0.258945 | 0.284794 | 0.301001 | 0.31147 | 0.322968 | 0.340095 | 0.381598 |
| tossup | drop_share_2_d6 | 1240 | 0.338112 | 0.012798 | 0.28793 | 0.316961 | 0.329271 | 0.338171 | 0.34683 | 0.358537 | 0.382088 |
| tossup | drop_share_3_d6 | 1240 | 0.349671 | 0.0168295 | 0.296872 | 0.322129 | 0.339219 | 0.349564 | 0.360055 | 0.378172 | 0.40866 |
| tossup | r_1 | 1240 | 0.152716 | 0.0797095 | 0.0382959 | 0.0657354 | 0.118572 | 0.142857 | 0.16093 | 0.316179 | 0.673093 |
| tossup | r_2 | 1240 | 0.18972 | 0.151037 | 0.0367394 | 0.0684315 | 0.10291 | 0.130876 | 0.204511 | 0.588994 | 0.790063 |
| tossup | r_3 | 1240 | 0.171763 | 0.103899 | 0.0334636 | 0.0608696 | 0.11482 | 0.154877 | 0.1818 | 0.418283 | 0.740121 |
| tossup | r_4 | 1240 | 0.169321 | 0.0886194 | 0.0384226 | 0.0640788 | 0.123277 | 0.162539 | 0.188907 | 0.320454 | 0.767891 |
| tossup | r_5 | 1240 | 0.15744 | 0.0451242 | 0.0471824 | 0.0741076 | 0.123571 | 0.165422 | 0.190816 | 0.221122 | 0.27296 |
| tossup | r_6 | 1240 | 0.15904 | 0.0455008 | 0.0456172 | 0.07348 | 0.126941 | 0.173173 | 0.191047 | 0.208976 | 0.412947 |
| tossup | r_norm | 1240 | 0.462096 | 0.076943 | 0.40838 | 0.410298 | 0.414238 | 0.42289 | 0.480523 | 0.646113 | 0.79573 |
