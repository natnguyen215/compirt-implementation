# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_5/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_5/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 322646 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.667897 |
| log_loss | 0.513142 |
| ece | 0.015045 |
| brier | 0.167866 |
| accuracy | 0.765475 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00129632 |
| probability_std | 0.121009 |
| probability_p10 | 0.593629 |
| probability_p50 | 0.786663 |
| probability_p90 | 0.896825 |
| mean_predictive_variance | 0.166622 |
| integrated_brier_score | 0.101784 |
| joint_tossup_event_log_loss | 6.88248 |
| buzz_position_mae | 0.160429 |
| buzz_position_median_absolute_error | 0.143952 |
| buzz_position_bias | -0.0667609 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.350762 |
| first_buzzer_mean_reciprocal_rank | 0.563455 |
| first_buzzer_log_loss | 1.66667 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.659501 |
| tossup_scorer_player_top1_accuracy | 0.321322 |
| tossup_scorer_team_top1_accuracy | 0.500107 |
| tossup_game_winner_accuracy | 0.793478 |
| tossup_game_margin_mae | 35.4009 |
| tournament_player_ppg_spearman | 0.710035 |
| tournament_player_ppg_mae | 8.52453 |
| tournament_player_ppg_top10_overlap | 0.655172 |
| neg_auroc | 0.667897 |
| neg_average_precision | 0.388654 |
| neg_precision | 0.518182 |
| neg_recall | 0.0783326 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0557846 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0926974 |
| no_buzz_calibration_error | 0.0795844 |
| no_buzz_brier | 0.0254164 |
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
| tossup_correctness | aggregate | all | 9257 | 0.667897 | 0.513142 | 0.015045 | 0.167866 | 0.765475 | 0.764178 | 0.00129632 | 0.121009 | 0.593629 | 0.786663 | 0.896825 | 0.166622 |
| tossup_correctness | tier | fall | 2798 | 0.682099 | 0.482983 | 0.0115506 | 0.155649 | 0.786633 | 0.785204 | 0.00142959 | 0.103139 | 0.644388 | 0.80855 | 0.902494 | 0.156488 |
| tossup_correctness | tier | nationals | 1545 | 0.678521 | 0.557947 | 0.0497468 | 0.18787 | 0.719094 | 0.721036 | -0.00194175 | 0.121238 | 0.507444 | 0.683263 | 0.819991 | 0.205961 |
| tossup_correctness | tier | regionals | 2039 | 0.641821 | 0.525537 | 0.0239331 | 0.172142 | 0.76459 | 0.762138 | 0.00245218 | 0.113046 | 0.612751 | 0.795805 | 0.896825 | 0.16283 |
| tossup_correctness | tier | winter | 2875 | 0.664173 | 0.509624 | 0.0205987 | 0.165973 | 0.770435 | 0.768348 | 0.00208696 | 0.120026 | 0.618942 | 0.804494 | 0.907265 | 0.158034 |
| tossup_correctness | category | Current Events | 129 | 0.659005 | 0.6078 | 0.0605523 | 0.209304 | 0.674419 | 0.666667 | 0.00775194 | 0.10575 | 0.579258 | 0.727799 | 0.855135 | 0.188494 |
| tossup_correctness | category | Fine Arts | 1074 | 0.653018 | 0.510721 | 0.0314977 | 0.167046 | 0.765363 | 0.776536 | -0.0111732 | 0.130076 | 0.569951 | 0.770808 | 0.895965 | 0.171489 |
| tossup_correctness | category | Geography | 180 | 0.73665 | 0.598353 | 0.100052 | 0.204472 | 0.683333 | 0.616667 | 0.0666667 | 0.15622 | 0.473303 | 0.737021 | 0.881468 | 0.184462 |
| tossup_correctness | category | History | 1454 | 0.671976 | 0.517278 | 0.0218266 | 0.170265 | 0.757909 | 0.757909 | 0 | 0.118486 | 0.58993 | 0.773779 | 0.886802 | 0.172059 |
| tossup_correctness | category | Literature | 1435 | 0.647947 | 0.465143 | 0.0445276 | 0.14591 | 0.806969 | 0.810453 | -0.00348432 | 0.114427 | 0.622258 | 0.808422 | 0.909884 | 0.156338 |
| tossup_correctness | category | Mythology | 324 | 0.662117 | 0.485392 | 0.053879 | 0.156873 | 0.783951 | 0.79321 | -0.00925926 | 0.123828 | 0.587145 | 0.77462 | 0.888647 | 0.17077 |
| tossup_correctness | category | Other Academic | 71 | 0.407407 | 0.599124 | 0.11651 | 0.203285 | 0.746479 | 0.760563 | -0.0140845 | 0.0914215 | 0.585002 | 0.744458 | 0.834862 | 0.192532 |
| tossup_correctness | category | Philosophy | 310 | 0.685925 | 0.509272 | 0.042712 | 0.167961 | 0.767742 | 0.76129 | 0.00645161 | 0.120139 | 0.584526 | 0.788437 | 0.903524 | 0.166472 |
| tossup_correctness | category | Popular Culture | 108 | 0.571181 | 0.422428 | 0.144237 | 0.127984 | 0.851852 | 0.888889 | -0.037037 | 0.110473 | 0.569613 | 0.76577 | 0.87136 | 0.177941 |
| tossup_correctness | category | Religion | 361 | 0.655152 | 0.541463 | 0.0340689 | 0.180073 | 0.747922 | 0.742382 | 0.00554017 | 0.127861 | 0.570789 | 0.754023 | 0.882168 | 0.178069 |
| tossup_correctness | category | Science | 1445 | 0.705871 | 0.518324 | 0.0351968 | 0.17143 | 0.752249 | 0.746021 | 0.00622837 | 0.11921 | 0.604622 | 0.802707 | 0.907203 | 0.15972 |
| tossup_correctness | category | Social Science | 327 | 0.707909 | 0.54009 | 0.0207014 | 0.180138 | 0.737003 | 0.718654 | 0.0183486 | 0.128133 | 0.542899 | 0.754396 | 0.878608 | 0.181321 |
| tossup_correctness | category | Unknown | 2039 | 0.641821 | 0.525537 | 0.0239331 | 0.172142 | 0.76459 | 0.762138 | 0.00245218 | 0.113046 | 0.612751 | 0.795805 | 0.896825 | 0.16283 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.615926 | 0.566479 | 0.0771046 | 0.19007 | 0.715847 | 0.743169 | -0.0273224 | 0.123626 | 0.498009 | 0.697865 | 0.824613 | 0.201047 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.669063 | 0.551448 | 0.0304312 | 0.184306 | 0.73089 | 0.728796 | 0.00209424 | 0.120995 | 0.55078 | 0.739022 | 0.854918 | 0.188073 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.687067 | 0.516899 | 0.0106356 | 0.170324 | 0.753461 | 0.752568 | 0.000893256 | 0.119521 | 0.577967 | 0.775276 | 0.882279 | 0.172762 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.659486 | 0.490624 | 0.0195191 | 0.158346 | 0.785043 | 0.786087 | -0.00104348 | 0.117617 | 0.607227 | 0.803185 | 0.901643 | 0.159977 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.661402 | 0.516464 | 0.0218743 | 0.168566 | 0.769717 | 0.764393 | 0.00532446 | 0.118979 | 0.608339 | 0.799139 | 0.909787 | 0.159492 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | -1.16572 | 1.05888 | -4.43142 | -3.34084 | -1.85281 | -0.685881 | -0.357697 | -0.146346 | 0.646105 |
| player | theta_2 | 1197 | -2.52983 | 0.739312 | -5.22212 | -3.68688 | -2.99465 | -2.52722 | -2.09086 | -1.14717 | 0.186229 |
| player | theta_3 | 1197 | -1.04286 | 0.789005 | -3.67235 | -2.44202 | -1.67471 | -0.854949 | -0.346151 | -0.121687 | 0.402664 |
| player | theta_4 | 1197 | -0.6603 | 0.444217 | -2.77961 | -1.53679 | -0.865544 | -0.58317 | -0.368873 | -0.0928575 | 0.609201 |
| player | theta_5 | 1197 | -0.503221 | 0.460753 | -2.6853 | -1.52989 | -0.63963 | -0.388498 | -0.236894 | 0.0279851 | 0.714 |
| player | theta_norm | 1197 | 3.40671 | 0.792631 | 1.57068 | 2.17891 | 2.83352 | 3.31828 | 3.94212 | 4.86403 | 5.88173 |
| tossup | start_difficulty_d1 | 1240 | -1.49835 | 1.27654 | -3.89235 | -3.40677 | -2.77502 | -1.3398 | -0.240775 | 0.111666 | 0.601996 |
| tossup | start_difficulty_d2 | 1240 | -2.54155 | 1.43483 | -4.93511 | -4.14735 | -3.58335 | -3.16875 | -0.85487 | -0.0743174 | 0.369329 |
| tossup | start_difficulty_d3 | 1240 | -0.847052 | 1.26384 | -5.19427 | -3.68805 | -1.29928 | -0.235146 | -0.0229883 | 0.196633 | 0.576116 |
| tossup | start_difficulty_d4 | 1240 | -0.4405 | 0.658127 | -3.03862 | -1.7896 | -0.724194 | -0.264164 | -0.00997542 | 0.315291 | 0.998113 |
| tossup | start_difficulty_d5 | 1240 | -0.349801 | 0.541423 | -2.41817 | -1.59388 | -0.539727 | -0.177421 | 0.0156735 | 0.211527 | 0.492182 |
| tossup | end_difficulty_d1 | 1240 | -2.58148 | 1.41734 | -6.19462 | -4.85125 | -3.85861 | -2.37063 | -1.22218 | -0.834564 | -0.282618 |
| tossup | end_difficulty_d2 | 1240 | -3.65888 | 1.57401 | -8.28571 | -5.67351 | -4.79675 | -4.13723 | -1.9723 | -1.02574 | -0.51977 |
| tossup | end_difficulty_d3 | 1240 | -1.86972 | 1.32111 | -7.11388 | -4.75276 | -2.43757 | -1.23536 | -0.999261 | -0.731948 | -0.33151 |
| tossup | end_difficulty_d4 | 1240 | -1.45991 | 0.746827 | -4.88826 | -2.96486 | -1.77471 | -1.26219 | -0.972228 | -0.59547 | 0.142008 |
| tossup | end_difficulty_d5 | 1240 | -1.36999 | 0.641246 | -4.32122 | -2.84102 | -1.5775 | -1.16173 | -0.945523 | -0.715782 | -0.395347 |
| tossup | total_drop_d1 | 1240 | 1.08313 | 0.245691 | 0.595171 | 0.880676 | 0.956302 | 1.00831 | 1.12137 | 1.5252 | 3.18009 |
| tossup | total_drop_d2 | 1240 | 1.11733 | 0.443826 | 0.402559 | 0.679817 | 0.894343 | 1.02172 | 1.1919 | 1.86079 | 4.66583 |
| tossup | total_drop_d3 | 1240 | 1.02267 | 0.176833 | 0.659392 | 0.85713 | 0.949269 | 0.991049 | 1.04726 | 1.29953 | 4.10601 |
| tossup | total_drop_d4 | 1240 | 1.01941 | 0.109227 | 0.799069 | 0.89135 | 0.951715 | 0.997773 | 1.05891 | 1.22351 | 1.89257 |
| tossup | total_drop_d5 | 1240 | 1.02019 | 0.11605 | 0.845391 | 0.908069 | 0.956626 | 0.99152 | 1.04593 | 1.231 | 2.04092 |
| tossup | drop_share_1_d1 | 1240 | 0.339569 | 0.0370262 | 0.252654 | 0.298609 | 0.310497 | 0.327698 | 0.363799 | 0.410558 | 0.49074 |
| tossup | drop_share_2_d1 | 1240 | 0.342941 | 0.0128193 | 0.295816 | 0.32108 | 0.335044 | 0.343488 | 0.350999 | 0.362783 | 0.423643 |
| tossup | drop_share_3_d1 | 1240 | 0.317491 | 0.0346227 | 0.175433 | 0.249513 | 0.297065 | 0.327631 | 0.343757 | 0.358205 | 0.385063 |
| tossup | drop_share_1_d2 | 1240 | 0.359605 | 0.0541936 | 0.209401 | 0.296695 | 0.316339 | 0.349075 | 0.393199 | 0.455183 | 0.646649 |
| tossup | drop_share_2_d2 | 1240 | 0.335382 | 0.0216515 | 0.224842 | 0.302709 | 0.321995 | 0.336536 | 0.348362 | 0.363833 | 0.464193 |
| tossup | drop_share_3_d2 | 1240 | 0.305013 | 0.0476158 | 0.128509 | 0.217896 | 0.273637 | 0.316443 | 0.340571 | 0.364736 | 0.444869 |
| tossup | drop_share_1_d3 | 1240 | 0.319137 | 0.0213148 | 0.242902 | 0.295206 | 0.306721 | 0.314167 | 0.325612 | 0.365627 | 0.461056 |
| tossup | drop_share_2_d3 | 1240 | 0.344913 | 0.0122062 | 0.292294 | 0.322133 | 0.33832 | 0.346189 | 0.35294 | 0.363132 | 0.388137 |
| tossup | drop_share_3_d3 | 1240 | 0.33595 | 0.019222 | 0.224431 | 0.298139 | 0.328073 | 0.338957 | 0.347432 | 0.35977 | 0.417218 |
| tossup | drop_share_1_d4 | 1240 | 0.313528 | 0.0142188 | 0.277512 | 0.29407 | 0.30455 | 0.311744 | 0.320332 | 0.338633 | 0.387078 |
| tossup | drop_share_2_d4 | 1240 | 0.346907 | 0.0095231 | 0.313995 | 0.331214 | 0.340787 | 0.346722 | 0.353189 | 0.362532 | 0.376143 |
| tossup | drop_share_3_d4 | 1240 | 0.339565 | 0.0148558 | 0.265003 | 0.312454 | 0.332134 | 0.340964 | 0.348814 | 0.360848 | 0.384189 |
| tossup | drop_share_1_d5 | 1240 | 0.312819 | 0.0129029 | 0.276673 | 0.294487 | 0.303708 | 0.311526 | 0.320177 | 0.336471 | 0.367699 |
| tossup | drop_share_2_d5 | 1240 | 0.346765 | 0.00902844 | 0.322039 | 0.331638 | 0.34028 | 0.34688 | 0.353128 | 0.361396 | 0.372027 |
| tossup | drop_share_3_d5 | 1240 | 0.340416 | 0.0136527 | 0.275641 | 0.31434 | 0.333163 | 0.341967 | 0.349667 | 0.36021 | 0.377068 |
| tossup | r_1 | 1240 | 0.241714 | 0.245126 | 0.0159938 | 0.0262337 | 0.0407258 | 0.116864 | 0.523509 | 0.682093 | 0.819782 |
| tossup | r_2 | 1240 | 0.481017 | 0.271959 | 0.0464625 | 0.0605147 | 0.136208 | 0.581421 | 0.700593 | 0.808868 | 0.928208 |
| tossup | r_3 | 1240 | 0.125444 | 0.127117 | 0.00967462 | 0.0278265 | 0.0449629 | 0.0644313 | 0.149889 | 0.411169 | 0.590873 |
| tossup | r_4 | 1240 | 0.0762957 | 0.0442704 | 0.0161785 | 0.0278985 | 0.0461544 | 0.0624503 | 0.093766 | 0.169819 | 0.27173 |
| tossup | r_5 | 1240 | 0.0755291 | 0.0558294 | 0.00898667 | 0.0221168 | 0.0390774 | 0.0592972 | 0.0858298 | 0.210104 | 0.354835 |
| tossup | r_norm | 1240 | 0.683189 | 0.0740355 | 0.521612 | 0.576344 | 0.626355 | 0.676602 | 0.731008 | 0.817434 | 0.928982 |
