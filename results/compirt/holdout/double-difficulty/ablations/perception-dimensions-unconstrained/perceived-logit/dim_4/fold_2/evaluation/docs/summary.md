# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_4/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_4/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 335562 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.543366 |
| log_loss | 0.604961 |
| ece | 0.0994544 |
| brier | 0.191262 |
| accuracy | 0.762882 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00129632 |
| probability_std | 0.100338 |
| probability_p10 | 0.700611 |
| probability_p50 | 0.882068 |
| probability_p90 | 0.948353 |
| mean_predictive_variance | 0.115898 |
| integrated_brier_score | 0.174643 |
| joint_tossup_event_log_loss | 7.73804 |
| buzz_position_mae | 0.339815 |
| buzz_position_median_absolute_error | 0.342066 |
| buzz_position_bias | -0.326749 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.362753 |
| first_buzzer_mean_reciprocal_rank | 0.577204 |
| first_buzzer_log_loss | 1.63278 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.637139 |
| tossup_scorer_player_top1_accuracy | 0.271322 |
| tossup_scorer_team_top1_accuracy | 0.401173 |
| tossup_game_winner_accuracy | 0.695652 |
| tossup_game_margin_mae | 47.0165 |
| tournament_player_ppg_spearman | 0.6169 |
| tournament_player_ppg_mae | 10.1763 |
| tournament_player_ppg_top10_overlap | 0.603448 |
| neg_auroc | 0.543366 |
| neg_average_precision | 0.278039 |
| neg_precision | 0.384615 |
| neg_recall | 0.0091617 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0294183 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.236512 |
| no_buzz_calibration_error | 0.223399 |
| no_buzz_brier | 0.0717813 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| tossup_correctness | aggregate | all | 9257 | 0.543366 | 0.604961 | 0.0994544 | 0.191262 | 0.762882 | 0.764178 | -0.00129632 | 0.100338 | 0.700611 | 0.882068 | 0.948353 | 0.115898 |
| tossup_correctness | tier | fall | 2798 | 0.529812 | 0.563482 | 0.0860292 | 0.177027 | 0.786276 | 0.785204 | 0.00107219 | 0.0789651 | 0.759464 | 0.878817 | 0.940493 | 0.113457 |
| tossup_correctness | tier | nationals | 1545 | 0.57606 | 0.64509 | 0.10806 | 0.211568 | 0.715858 | 0.721036 | -0.00517799 | 0.123215 | 0.62304 | 0.849904 | 0.943644 | 0.13637 |
| tossup_correctness | tier | regionals | 2039 | 0.539963 | 0.609167 | 0.0975102 | 0.192009 | 0.758705 | 0.762138 | -0.00343306 | 0.115027 | 0.654826 | 0.880153 | 0.95011 | 0.121598 |
| tossup_correctness | tier | winter | 2875 | 0.529047 | 0.620779 | 0.119147 | 0.193673 | 0.768348 | 0.768348 | 0 | 0.0858584 | 0.742369 | 0.899708 | 0.954321 | 0.10323 |
| tossup_correctness | category | Current Events | 129 | 0.566793 | 0.750301 | 0.202679 | 0.252188 | 0.658915 | 0.666667 | -0.00775194 | 0.0938645 | 0.71694 | 0.859709 | 0.926568 | 0.127502 |
| tossup_correctness | category | Fine Arts | 1074 | 0.541492 | 0.591134 | 0.10418 | 0.185409 | 0.774674 | 0.776536 | -0.0018622 | 0.0923231 | 0.727731 | 0.895754 | 0.947867 | 0.106945 |
| tossup_correctness | category | Geography | 180 | 0.552161 | 0.891391 | 0.25405 | 0.299311 | 0.611111 | 0.616667 | -0.00555556 | 0.0972177 | 0.704365 | 0.884204 | 0.946326 | 0.114855 |
| tossup_correctness | category | History | 1454 | 0.553789 | 0.602393 | 0.095728 | 0.192413 | 0.759972 | 0.757909 | 0.00206327 | 0.0979323 | 0.69626 | 0.870932 | 0.943247 | 0.121117 |
| tossup_correctness | category | Literature | 1435 | 0.518038 | 0.531523 | 0.08138 | 0.161312 | 0.809756 | 0.810453 | -0.000696864 | 0.0887355 | 0.739909 | 0.891446 | 0.954207 | 0.106546 |
| tossup_correctness | category | Mythology | 324 | 0.564435 | 0.552239 | 0.126589 | 0.172055 | 0.799383 | 0.79321 | 0.00617284 | 0.0962078 | 0.733463 | 0.90392 | 0.949233 | 0.104247 |
| tossup_correctness | category | Other Academic | 71 | 0.361656 | 0.751721 | 0.20505 | 0.22911 | 0.732394 | 0.760563 | -0.028169 | 0.116297 | 0.703038 | 0.91055 | 0.952908 | 0.102484 |
| tossup_correctness | category | Philosophy | 310 | 0.502348 | 0.656124 | 0.132022 | 0.203163 | 0.758065 | 0.76129 | -0.00322581 | 0.0859973 | 0.758151 | 0.908727 | 0.954497 | 0.0992595 |
| tossup_correctness | category | Popular Culture | 108 | 0.529514 | 0.357325 | 0.0771058 | 0.101969 | 0.87963 | 0.888889 | -0.00925926 | 0.072328 | 0.774477 | 0.884742 | 0.936252 | 0.1106 |
| tossup_correctness | category | Religion | 361 | 0.536712 | 0.656076 | 0.132987 | 0.20863 | 0.736842 | 0.742382 | -0.00554017 | 0.0935077 | 0.726402 | 0.890266 | 0.94852 | 0.109236 |
| tossup_correctness | category | Science | 1445 | 0.557486 | 0.615314 | 0.103738 | 0.199041 | 0.748097 | 0.746021 | 0.00207612 | 0.0997032 | 0.689874 | 0.857137 | 0.941028 | 0.127789 |
| tossup_correctness | category | Social Science | 327 | 0.555828 | 0.6943 | 0.150101 | 0.2241 | 0.712538 | 0.718654 | -0.00611621 | 0.0919598 | 0.720431 | 0.887084 | 0.943833 | 0.110381 |
| tossup_correctness | category | Unknown | 2039 | 0.539963 | 0.609167 | 0.0975102 | 0.192009 | 0.758705 | 0.762138 | -0.00343306 | 0.115027 | 0.654826 | 0.880153 | 0.95011 | 0.121598 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.451502 | 0.657424 | 0.138063 | 0.210539 | 0.737705 | 0.743169 | -0.00546448 | 0.0989721 | 0.690878 | 0.841062 | 0.924035 | 0.13713 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.514895 | 0.653605 | 0.118061 | 0.215354 | 0.727749 | 0.728796 | -0.00104712 | 0.0980855 | 0.699057 | 0.854722 | 0.928274 | 0.131512 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.539957 | 0.611988 | 0.100797 | 0.196455 | 0.751228 | 0.752568 | -0.00133988 | 0.0960048 | 0.704943 | 0.866162 | 0.937152 | 0.124115 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.542115 | 0.563476 | 0.0876901 | 0.175623 | 0.784696 | 0.786087 | -0.0013913 | 0.0984531 | 0.703068 | 0.885655 | 0.947014 | 0.114113 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.553274 | 0.62076 | 0.113334 | 0.193524 | 0.763394 | 0.764393 | -0.000998336 | 0.103513 | 0.69977 | 0.9042 | 0.956828 | 0.105228 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1197 | -1.34593 | 0.750706 | -3.16978 | -2.35333 | -1.78851 | -1.41882 | -1.01546 | -0.0157748 | 2.28607 |
| player | beta | 1197 | -3.43835 | 1.11017 | -6.81758 | -5.81745 | -3.96178 | -3.17985 | -2.59163 | -2.09053 | -1.76337 |
| player | theta_1 | 1197 | 0.84431 | 0.984585 | -2.11055 | -0.980308 | 0.198439 | 0.995821 | 1.5741 | 2.26943 | 3.22533 |
| player | theta_2 | 1197 | 0.836344 | 0.977655 | -2.53546 | -0.910131 | 0.243146 | 0.939224 | 1.50444 | 2.31042 | 3.33304 |
| player | theta_3 | 1197 | 0.835192 | 0.95391 | -2.58835 | -0.993258 | 0.283583 | 0.997544 | 1.49702 | 2.20081 | 3.10547 |
| player | theta_4 | 1197 | 0.764438 | 0.75518 | -1.91343 | -0.62988 | 0.300236 | 0.854982 | 1.26933 | 1.83887 | 3.09834 |
| player | theta_norm | 1197 | 2.38501 | 0.639481 | 0.520675 | 1.24521 | 1.97913 | 2.40139 | 2.79154 | 3.4531 | 4.81068 |
| tossup | start_difficulty_d1 | 1240 | -0.894294 | 0.394261 | -2.08354 | -1.66943 | -1.17561 | -0.816951 | -0.580926 | -0.370753 | -0.138716 |
| tossup | start_difficulty_d2 | 1240 | -0.900113 | 0.443692 | -2.17713 | -1.71076 | -1.21398 | -0.847874 | -0.547182 | -0.245405 | -0.0847817 |
| tossup | start_difficulty_d3 | 1240 | -0.875008 | 0.498638 | -2.34295 | -1.86677 | -1.19963 | -0.758611 | -0.447217 | -0.287289 | -0.0912169 |
| tossup | start_difficulty_d4 | 1240 | -0.802688 | 0.340502 | -2.10621 | -1.41762 | -1.03862 | -0.765333 | -0.534841 | -0.322284 | -0.123413 |
| tossup | end_difficulty_d1 | 1240 | -1.6256 | 0.307593 | -2.54146 | -2.18745 | -1.82138 | -1.59566 | -1.38804 | -1.17125 | -1.01914 |
| tossup | end_difficulty_d2 | 1240 | -1.63691 | 0.380752 | -2.854 | -2.28061 | -1.91184 | -1.62193 | -1.32325 | -1.07729 | -0.895025 |
| tossup | end_difficulty_d3 | 1240 | -1.62021 | 0.42688 | -2.87797 | -2.40543 | -1.92565 | -1.5263 | -1.25957 | -1.09578 | -0.940172 |
| tossup | end_difficulty_d4 | 1240 | -1.57481 | 0.31723 | -2.53108 | -2.14884 | -1.79159 | -1.53742 | -1.32338 | -1.12173 | -0.929669 |
| tossup | total_drop_d1 | 1240 | 0.731309 | 0.196389 | 0.24804 | 0.351739 | 0.592301 | 0.76491 | 0.884385 | 1.0018 | 1.14676 |
| tossup | total_drop_d2 | 1240 | 0.736794 | 0.176615 | 0.251701 | 0.382667 | 0.634262 | 0.764568 | 0.856749 | 0.98674 | 1.193 |
| tossup | total_drop_d3 | 1240 | 0.745204 | 0.186809 | 0.259824 | 0.360266 | 0.659643 | 0.788629 | 0.871078 | 0.987633 | 1.265 |
| tossup | total_drop_d4 | 1240 | 0.772122 | 0.152847 | 0.306564 | 0.462254 | 0.699244 | 0.792505 | 0.870662 | 0.984614 | 1.21367 |
| tossup | drop_share_1_d1 | 1240 | 0.320382 | 0.0225842 | 0.226498 | 0.286036 | 0.308305 | 0.320351 | 0.331684 | 0.357592 | 0.421813 |
| tossup | drop_share_2_d1 | 1240 | 0.326428 | 0.0186278 | 0.25893 | 0.28833 | 0.317365 | 0.329354 | 0.339541 | 0.350684 | 0.36695 |
| tossup | drop_share_3_d1 | 1240 | 0.35319 | 0.0288558 | 0.268913 | 0.31816 | 0.335776 | 0.347997 | 0.364045 | 0.412319 | 0.494182 |
| tossup | drop_share_1_d2 | 1240 | 0.319186 | 0.021626 | 0.223707 | 0.285251 | 0.307516 | 0.319459 | 0.331011 | 0.351559 | 0.408224 |
| tossup | drop_share_2_d2 | 1240 | 0.327168 | 0.0177061 | 0.25108 | 0.292025 | 0.318816 | 0.330481 | 0.33923 | 0.350486 | 0.362349 |
| tossup | drop_share_3_d2 | 1240 | 0.353646 | 0.0275263 | 0.267816 | 0.319291 | 0.336556 | 0.348971 | 0.363396 | 0.406871 | 0.499672 |
| tossup | drop_share_1_d3 | 1240 | 0.322271 | 0.0245684 | 0.212729 | 0.290434 | 0.306506 | 0.318653 | 0.333757 | 0.368282 | 0.432453 |
| tossup | drop_share_2_d3 | 1240 | 0.32896 | 0.0160195 | 0.272025 | 0.296566 | 0.321264 | 0.33148 | 0.340164 | 0.350965 | 0.365543 |
| tossup | drop_share_3_d3 | 1240 | 0.348769 | 0.0243642 | 0.261369 | 0.313182 | 0.335251 | 0.347606 | 0.360622 | 0.389274 | 0.484839 |
| tossup | drop_share_1_d4 | 1240 | 0.318905 | 0.0196174 | 0.21723 | 0.287589 | 0.308159 | 0.318968 | 0.330218 | 0.34722 | 0.418716 |
| tossup | drop_share_2_d4 | 1240 | 0.330435 | 0.014478 | 0.270955 | 0.301269 | 0.323406 | 0.332553 | 0.340368 | 0.350324 | 0.364275 |
| tossup | drop_share_3_d4 | 1240 | 0.35066 | 0.0244497 | 0.280692 | 0.319727 | 0.335995 | 0.346879 | 0.359778 | 0.39842 | 0.488558 |
| tossup | r_1 | 1240 | 0.259191 | 0.217113 | 0.0314642 | 0.0627956 | 0.110046 | 0.164212 | 0.329885 | 0.759346 | 0.872852 |
| tossup | r_2 | 1240 | 0.27126 | 0.211211 | 0.0330311 | 0.0568768 | 0.10603 | 0.183193 | 0.41084 | 0.71135 | 0.879775 |
| tossup | r_3 | 1240 | 0.264143 | 0.19775 | 0.0354886 | 0.0578278 | 0.110604 | 0.190018 | 0.380814 | 0.681911 | 0.835881 |
| tossup | r_4 | 1240 | 0.205406 | 0.131615 | 0.0341062 | 0.0570774 | 0.11157 | 0.177131 | 0.262659 | 0.456853 | 0.822505 |
| tossup | r_norm | 1240 | 0.625998 | 0.094418 | 0.500334 | 0.514301 | 0.547275 | 0.602014 | 0.688594 | 0.810109 | 0.882543 |
