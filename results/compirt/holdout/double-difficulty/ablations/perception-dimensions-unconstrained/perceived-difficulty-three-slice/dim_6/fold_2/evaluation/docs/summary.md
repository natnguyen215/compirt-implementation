# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_6/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_6/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 330328 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.659012 |
| log_loss | 0.516565 |
| ece | 0.01736 |
| brier | 0.168993 |
| accuracy | 0.766771 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00259263 |
| probability_std | 0.117815 |
| probability_p10 | 0.600709 |
| probability_p50 | 0.786989 |
| probability_p90 | 0.898286 |
| mean_predictive_variance | 0.165847 |
| integrated_brier_score | 0.101194 |
| joint_tossup_event_log_loss | 6.86935 |
| buzz_position_mae | 0.159663 |
| buzz_position_median_absolute_error | 0.143642 |
| buzz_position_bias | -0.064724 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.357567 |
| first_buzzer_mean_reciprocal_rank | 0.571724 |
| first_buzzer_log_loss | 1.64526 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.658421 |
| tossup_scorer_player_top1_accuracy | 0.326333 |
| tossup_scorer_team_top1_accuracy | 0.498401 |
| tossup_game_winner_accuracy | 0.8 |
| tossup_game_margin_mae | 35.8475 |
| tournament_player_ppg_spearman | 0.706693 |
| tournament_player_ppg_mae | 8.59415 |
| tournament_player_ppg_top10_overlap | 0.662069 |
| neg_auroc | 0.659012 |
| neg_average_precision | 0.382332 |
| neg_precision | 0.544444 |
| neg_recall | 0.0673385 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0566213 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0965508 |
| no_buzz_calibration_error | 0.0834378 |
| no_buzz_brier | 0.0268657 |
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
| tossup_correctness | aggregate | all | 9257 | 0.659012 | 0.516565 | 0.01736 | 0.168993 | 0.766771 | 0.764178 | 0.00259263 | 0.117815 | 0.600709 | 0.786989 | 0.898286 | 0.165847 |
| tossup_correctness | tier | fall | 2798 | 0.682118 | 0.483504 | 0.0126126 | 0.155613 | 0.78842 | 0.785204 | 0.00321658 | 0.101523 | 0.653114 | 0.814231 | 0.902514 | 0.154411 |
| tossup_correctness | tier | nationals | 1545 | 0.666799 | 0.565052 | 0.0528352 | 0.190363 | 0.719741 | 0.721036 | -0.0012945 | 0.10873 | 0.527797 | 0.680059 | 0.809069 | 0.209193 |
| tossup_correctness | tier | regionals | 2039 | 0.615627 | 0.53451 | 0.0316277 | 0.175648 | 0.766062 | 0.762138 | 0.00392349 | 0.107645 | 0.62393 | 0.791489 | 0.89434 | 0.163754 |
| tossup_correctness | tier | winter | 2875 | 0.662722 | 0.509957 | 0.0287262 | 0.16581 | 0.771478 | 0.768348 | 0.00313043 | 0.118928 | 0.625717 | 0.810049 | 0.911054 | 0.155168 |
| tossup_correctness | category | Current Events | 129 | 0.651433 | 0.612909 | 0.0540585 | 0.211714 | 0.674419 | 0.666667 | 0.00775194 | 0.10448 | 0.57885 | 0.723747 | 0.849474 | 0.191695 |
| tossup_correctness | category | Fine Arts | 1074 | 0.654362 | 0.509397 | 0.0417551 | 0.16626 | 0.768156 | 0.776536 | -0.00837989 | 0.124207 | 0.575 | 0.771472 | 0.893444 | 0.171302 |
| tossup_correctness | category | Geography | 180 | 0.734691 | 0.59828 | 0.0830825 | 0.204036 | 0.688889 | 0.616667 | 0.0722222 | 0.152553 | 0.474704 | 0.723875 | 0.870916 | 0.187433 |
| tossup_correctness | category | History | 1454 | 0.66161 | 0.521125 | 0.0319773 | 0.171297 | 0.757909 | 0.757909 | 0 | 0.112823 | 0.603244 | 0.777426 | 0.885514 | 0.171612 |
| tossup_correctness | category | Literature | 1435 | 0.642779 | 0.466034 | 0.0307549 | 0.146147 | 0.813937 | 0.810453 | 0.00348432 | 0.106974 | 0.645613 | 0.81923 | 0.917036 | 0.149728 |
| tossup_correctness | category | Mythology | 324 | 0.652303 | 0.48837 | 0.0446027 | 0.15689 | 0.790123 | 0.79321 | -0.00308642 | 0.116165 | 0.611167 | 0.769916 | 0.880358 | 0.173687 |
| tossup_correctness | category | Other Academic | 71 | 0.394336 | 0.592521 | 0.0976915 | 0.200048 | 0.746479 | 0.760563 | -0.0140845 | 0.080109 | 0.60558 | 0.732881 | 0.828745 | 0.194515 |
| tossup_correctness | category | Philosophy | 310 | 0.679455 | 0.512822 | 0.0339342 | 0.16953 | 0.767742 | 0.76129 | 0.00645161 | 0.113679 | 0.607274 | 0.790156 | 0.905628 | 0.164064 |
| tossup_correctness | category | Popular Culture | 108 | 0.564236 | 0.404359 | 0.132537 | 0.119757 | 0.898148 | 0.888889 | 0.00925926 | 0.100039 | 0.621418 | 0.78614 | 0.87825 | 0.169463 |
| tossup_correctness | category | Religion | 361 | 0.665704 | 0.538444 | 0.0380725 | 0.178846 | 0.736842 | 0.742382 | -0.00554017 | 0.122039 | 0.56981 | 0.7532 | 0.873512 | 0.181025 |
| tossup_correctness | category | Science | 1445 | 0.693594 | 0.523626 | 0.0354117 | 0.173325 | 0.747405 | 0.746021 | 0.00138408 | 0.127314 | 0.58924 | 0.805637 | 0.913421 | 0.159351 |
| tossup_correctness | category | Social Science | 327 | 0.698936 | 0.543388 | 0.0331025 | 0.18132 | 0.733945 | 0.718654 | 0.0152905 | 0.121945 | 0.552223 | 0.749103 | 0.878771 | 0.182473 |
| tossup_correctness | category | Unknown | 2039 | 0.615627 | 0.53451 | 0.0316277 | 0.175648 | 0.766062 | 0.762138 | 0.00392349 | 0.107645 | 0.62393 | 0.791489 | 0.89434 | 0.163754 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.609981 | 0.569086 | 0.0836415 | 0.190916 | 0.737705 | 0.743169 | -0.00546448 | 0.121737 | 0.521854 | 0.691644 | 0.823163 | 0.201892 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.662373 | 0.554047 | 0.0251548 | 0.185087 | 0.727749 | 0.728796 | -0.00104712 | 0.119423 | 0.551777 | 0.739071 | 0.854937 | 0.187554 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.681743 | 0.519121 | 0.00822402 | 0.170985 | 0.755695 | 0.752568 | 0.0031264 | 0.117505 | 0.585471 | 0.77812 | 0.885777 | 0.171546 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.651632 | 0.492515 | 0.0225192 | 0.158865 | 0.790261 | 0.786087 | 0.00417391 | 0.115173 | 0.612611 | 0.803673 | 0.90176 | 0.159985 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.648014 | 0.52256 | 0.0281906 | 0.170749 | 0.766722 | 0.764393 | 0.00232945 | 0.113068 | 0.618179 | 0.802528 | 0.912722 | 0.158117 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | -0.813473 | 0.969983 | -4.25411 | -3.19086 | -0.674014 | -0.435276 | -0.289819 | -0.113193 | 0.345277 |
| player | theta_2 | 1197 | -1.19546 | 0.941585 | -4.56884 | -2.94017 | -1.93887 | -0.85074 | -0.463966 | -0.149084 | 0.533379 |
| player | theta_3 | 1197 | -0.627722 | 0.360008 | -1.86497 | -1.31375 | -0.831998 | -0.557629 | -0.373236 | -0.169213 | 0.466164 |
| player | theta_4 | 1197 | -2.51902 | 0.675374 | -5.24403 | -3.66934 | -2.94337 | -2.48442 | -2.0929 | -1.35426 | -0.156399 |
| player | theta_5 | 1197 | -1.13182 | 0.742996 | -3.77346 | -2.36796 | -1.7338 | -0.965634 | -0.493951 | -0.220038 | 0.566348 |
| player | theta_6 | 1197 | -0.796627 | 0.705455 | -3.04729 | -2.42846 | -0.975442 | -0.575227 | -0.29798 | -0.109851 | 0.605054 |
| player | theta_norm | 1197 | 3.65484 | 0.921329 | 1.6096 | 2.30448 | 2.96289 | 3.49695 | 4.28035 | 5.36967 | 6.50724 |
| tossup | start_difficulty_d1 | 1240 | -1.02553 | 1.24073 | -3.84462 | -3.22049 | -2.46895 | -0.339418 | -0.113119 | 0.121717 | 0.372001 |
| tossup | start_difficulty_d2 | 1240 | -1.23603 | 1.13239 | -4.64544 | -3.37826 | -2.15709 | -0.833619 | -0.337551 | 0.0575296 | 0.59525 |
| tossup | start_difficulty_d3 | 1240 | -0.398667 | 0.630002 | -3.64626 | -1.81661 | -0.48779 | -0.192463 | -0.0337961 | 0.125363 | 0.529297 |
| tossup | start_difficulty_d4 | 1240 | -2.5073 | 1.39531 | -5.05773 | -4.24039 | -3.61454 | -3.00406 | -1.01517 | -0.224669 | 0.309745 |
| tossup | start_difficulty_d5 | 1240 | -0.899079 | 1.20702 | -5.25551 | -3.66225 | -1.32711 | -0.36679 | -0.092659 | 0.17372 | 0.731391 |
| tossup | start_difficulty_d6 | 1240 | -0.82833 | 0.948841 | -3.80379 | -2.82018 | -1.40175 | -0.422884 | -0.112926 | 0.121041 | 0.477322 |
| tossup | end_difficulty_d1 | 1240 | -2.08233 | 1.35691 | -6.10291 | -4.58551 | -3.45447 | -1.34421 | -1.09012 | -0.821165 | -0.556455 |
| tossup | end_difficulty_d2 | 1240 | -2.28669 | 1.20943 | -6.34454 | -4.50757 | -3.26958 | -1.8695 | -1.33233 | -0.884121 | -0.322898 |
| tossup | end_difficulty_d3 | 1240 | -1.41925 | 0.725841 | -5.99564 | -2.94159 | -1.5195 | -1.19748 | -1.00961 | -0.823961 | -0.347681 |
| tossup | end_difficulty_d4 | 1240 | -3.63182 | 1.52648 | -8.75701 | -5.72748 | -4.78845 | -3.98895 | -2.14288 | -1.1967 | -0.573896 |
| tossup | end_difficulty_d5 | 1240 | -1.9189 | 1.25483 | -6.79617 | -4.68312 | -2.38939 | -1.3967 | -1.07451 | -0.768398 | -0.0897303 |
| tossup | end_difficulty_d6 | 1240 | -1.87402 | 1.06766 | -6.26134 | -4.0748 | -2.46561 | -1.43129 | -1.08306 | -0.829231 | -0.459207 |
| tossup | total_drop_d1 | 1240 | 1.0568 | 0.18858 | 0.672273 | 0.915736 | 0.9656 | 1.00536 | 1.06702 | 1.38539 | 3.52515 |
| tossup | total_drop_d2 | 1240 | 1.05065 | 0.155627 | 0.612627 | 0.892659 | 0.966484 | 1.01586 | 1.08885 | 1.33156 | 2.24598 |
| tossup | total_drop_d3 | 1240 | 1.02058 | 0.12495 | 0.828013 | 0.917043 | 0.964175 | 0.996987 | 1.03861 | 1.19609 | 3.05872 |
| tossup | total_drop_d4 | 1240 | 1.12452 | 0.406328 | 0.403333 | 0.701781 | 0.930699 | 1.04355 | 1.20432 | 1.78219 | 5.10763 |
| tossup | total_drop_d5 | 1240 | 1.01982 | 0.156986 | 0.695004 | 0.854725 | 0.95469 | 1.00086 | 1.05648 | 1.22004 | 3.71388 |
| tossup | total_drop_d6 | 1240 | 1.04569 | 0.156148 | 0.839281 | 0.913553 | 0.961506 | 1.00533 | 1.07187 | 1.31475 | 2.73356 |
| tossup | drop_share_1_d1 | 1240 | 0.32963 | 0.0351646 | 0.281271 | 0.295242 | 0.305791 | 0.315602 | 0.345023 | 0.402062 | 0.460377 |
| tossup | drop_share_2_d1 | 1240 | 0.343856 | 0.0119703 | 0.295784 | 0.324219 | 0.33691 | 0.343939 | 0.351647 | 0.362904 | 0.409131 |
| tossup | drop_share_3_d1 | 1240 | 0.326514 | 0.031571 | 0.195851 | 0.256391 | 0.315749 | 0.337504 | 0.347993 | 0.359008 | 0.370697 |
| tossup | drop_share_1_d2 | 1240 | 0.330499 | 0.0312122 | 0.278615 | 0.29788 | 0.310807 | 0.321502 | 0.340233 | 0.392686 | 0.535256 |
| tossup | drop_share_2_d2 | 1240 | 0.343588 | 0.0120631 | 0.292265 | 0.323503 | 0.337205 | 0.344561 | 0.351683 | 0.360724 | 0.382997 |
| tossup | drop_share_3_d2 | 1240 | 0.325914 | 0.0273433 | 0.172479 | 0.270228 | 0.315721 | 0.333034 | 0.343606 | 0.355865 | 0.390458 |
| tossup | drop_share_1_d3 | 1240 | 0.312529 | 0.0148018 | 0.280292 | 0.293678 | 0.303827 | 0.31061 | 0.317947 | 0.33598 | 0.408384 |
| tossup | drop_share_2_d3 | 1240 | 0.346963 | 0.00961904 | 0.317222 | 0.331275 | 0.340703 | 0.346977 | 0.3534 | 0.362934 | 0.382283 |
| tossup | drop_share_3_d3 | 1240 | 0.340508 | 0.0151355 | 0.249747 | 0.316164 | 0.333646 | 0.342326 | 0.350278 | 0.35973 | 0.385554 |
| tossup | drop_share_1_d4 | 1240 | 0.360471 | 0.0526967 | 0.211466 | 0.302573 | 0.320441 | 0.346916 | 0.392413 | 0.461178 | 0.612819 |
| tossup | drop_share_2_d4 | 1240 | 0.334717 | 0.0212379 | 0.242689 | 0.303385 | 0.321568 | 0.335371 | 0.34787 | 0.364784 | 0.476249 |
| tossup | drop_share_3_d4 | 1240 | 0.304812 | 0.0458944 | 0.13921 | 0.217489 | 0.274917 | 0.317777 | 0.337974 | 0.359809 | 0.434964 |
| tossup | drop_share_1_d5 | 1240 | 0.318839 | 0.0219351 | 0.253477 | 0.295655 | 0.30627 | 0.313246 | 0.325402 | 0.364402 | 0.461358 |
| tossup | drop_share_2_d5 | 1240 | 0.344311 | 0.0126016 | 0.293828 | 0.321386 | 0.337949 | 0.345657 | 0.352718 | 0.361674 | 0.392274 |
| tossup | drop_share_3_d5 | 1240 | 0.33685 | 0.01969 | 0.221758 | 0.299098 | 0.328838 | 0.339536 | 0.348779 | 0.361856 | 0.40055 |
| tossup | drop_share_1_d6 | 1240 | 0.32205 | 0.0223308 | 0.279686 | 0.296347 | 0.307138 | 0.315836 | 0.330815 | 0.36652 | 0.442169 |
| tossup | drop_share_2_d6 | 1240 | 0.345151 | 0.00999981 | 0.314706 | 0.328378 | 0.338646 | 0.345445 | 0.351906 | 0.361597 | 0.374634 |
| tossup | drop_share_3_d6 | 1240 | 0.332799 | 0.021618 | 0.214177 | 0.288917 | 0.322257 | 0.338014 | 0.347761 | 0.358863 | 0.386189 |
| tossup | r_1 | 1240 | 0.162439 | 0.198784 | 0.0136475 | 0.0234262 | 0.0322056 | 0.0437445 | 0.350018 | 0.560895 | 0.707212 |
| tossup | r_2 | 1240 | 0.14785 | 0.156958 | 0.0147151 | 0.0256439 | 0.0449407 | 0.0771403 | 0.195461 | 0.488873 | 0.765206 |
| tossup | r_3 | 1240 | 0.0540444 | 0.0396231 | 0.0145755 | 0.0237587 | 0.0320899 | 0.0414924 | 0.0578145 | 0.135015 | 0.297795 |
| tossup | r_4 | 1240 | 0.415731 | 0.258906 | 0.0430798 | 0.0570509 | 0.112482 | 0.463139 | 0.642429 | 0.78485 | 0.920163 |
| tossup | r_5 | 1240 | 0.112183 | 0.11368 | 0.012788 | 0.0299499 | 0.0427909 | 0.0595472 | 0.126781 | 0.379233 | 0.63861 |
| tossup | r_6 | 1240 | 0.107752 | 0.110244 | 0.0126044 | 0.0241146 | 0.0397612 | 0.0571246 | 0.129295 | 0.375813 | 0.610232 |
| tossup | r_norm | 1240 | 0.631564 | 0.0838437 | 0.472466 | 0.520651 | 0.567215 | 0.614895 | 0.68354 | 0.791023 | 0.920872 |
