# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/perceived-logit-grid/perceived-logit/dim_6/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained-10000-steps/perceived-logit-grid/perceived-logit/dim_6/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 323683 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.604728 |
| log_loss | 0.57677 |
| ece | 0.110685 |
| brier | 0.189964 |
| accuracy | 0.735443 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.028735 |
| probability_std | 0.166988 |
| probability_p10 | 0.464851 |
| probability_p50 | 0.704046 |
| probability_p90 | 0.912666 |
| mean_predictive_variance | 0.185038 |
| integrated_brier_score | 0.113913 |
| joint_tossup_event_log_loss | 6.88293 |
| buzz_position_mae | 0.185087 |
| buzz_position_median_absolute_error | 0.160257 |
| buzz_position_bias | -0.120277 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.390623 |
| first_buzzer_mean_reciprocal_rank | 0.595008 |
| first_buzzer_log_loss | 1.6041 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.656692 |
| tossup_scorer_player_top1_accuracy | 0.302239 |
| tossup_scorer_team_top1_accuracy | 0.452665 |
| tossup_game_winner_accuracy | 0.773913 |
| tossup_game_margin_mae | 41.9864 |
| tournament_player_ppg_spearman | 0.594879 |
| tournament_player_ppg_mae | 10.5956 |
| tournament_player_ppg_top10_overlap | 0.613793 |
| neg_auroc | 0.604728 |
| neg_average_precision | 0.333286 |
| neg_precision | 0.396417 |
| neg_recall | 0.233165 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.102566 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0926452 |
| no_buzz_calibration_error | 0.0795322 |
| no_buzz_brier | 0.0278067 |
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
| tossup_correctness | aggregate | all | 9257 | 0.604728 | 0.57677 | 0.110685 | 0.189964 | 0.735443 | 0.764178 | -0.028735 | 0.166988 | 0.464851 | 0.704046 | 0.912666 | 0.185038 |
| tossup_correctness | tier | fall | 2798 | 0.583372 | 0.556175 | 0.105356 | 0.177863 | 0.767334 | 0.785204 | -0.0178699 | 0.156641 | 0.529874 | 0.754713 | 0.947796 | 0.166276 |
| tossup_correctness | tier | nationals | 1545 | 0.62523 | 0.604145 | 0.0987275 | 0.207811 | 0.680906 | 0.721036 | -0.0401294 | 0.160852 | 0.396678 | 0.642009 | 0.820247 | 0.208701 |
| tossup_correctness | tier | regionals | 2039 | 0.614097 | 0.572291 | 0.110777 | 0.191569 | 0.727317 | 0.762138 | -0.034821 | 0.162409 | 0.444405 | 0.684346 | 0.862545 | 0.195533 |
| tossup_correctness | tier | winter | 2875 | 0.59086 | 0.58528 | 0.122821 | 0.19101 | 0.739478 | 0.768348 | -0.0288696 | 0.166767 | 0.472919 | 0.703461 | 0.926158 | 0.183138 |
| tossup_correctness | category | Current Events | 129 | 0.435911 | 0.753318 | 0.215953 | 0.264415 | 0.627907 | 0.666667 | -0.0387597 | 0.161671 | 0.477152 | 0.730277 | 0.900363 | 0.183928 |
| tossup_correctness | category | Fine Arts | 1074 | 0.611965 | 0.570721 | 0.12736 | 0.186535 | 0.736499 | 0.776536 | -0.0400372 | 0.175137 | 0.454428 | 0.697867 | 0.935586 | 0.182834 |
| tossup_correctness | category | Geography | 180 | 0.569004 | 0.702355 | 0.108924 | 0.245744 | 0.6 | 0.616667 | -0.0166667 | 0.163612 | 0.456341 | 0.658559 | 0.897118 | 0.197725 |
| tossup_correctness | category | History | 1454 | 0.600414 | 0.573245 | 0.100912 | 0.189522 | 0.741403 | 0.757909 | -0.0165062 | 0.160621 | 0.483915 | 0.717003 | 0.918204 | 0.182309 |
| tossup_correctness | category | Literature | 1435 | 0.563584 | 0.55344 | 0.12763 | 0.175146 | 0.769338 | 0.810453 | -0.041115 | 0.165794 | 0.489343 | 0.739603 | 0.948892 | 0.17202 |
| tossup_correctness | category | Mythology | 324 | 0.574714 | 0.565132 | 0.143927 | 0.186014 | 0.759259 | 0.79321 | -0.0339506 | 0.169338 | 0.473713 | 0.690143 | 0.941364 | 0.179835 |
| tossup_correctness | category | Other Academic | 71 | 0.434641 | 0.693906 | 0.19319 | 0.240409 | 0.633803 | 0.760563 | -0.126761 | 0.165625 | 0.402717 | 0.667466 | 0.84197 | 0.203009 |
| tossup_correctness | category | Philosophy | 310 | 0.615094 | 0.593834 | 0.124947 | 0.194948 | 0.716129 | 0.76129 | -0.0451613 | 0.178276 | 0.435974 | 0.68737 | 0.931899 | 0.187504 |
| tossup_correctness | category | Popular Culture | 108 | 0.568576 | 0.493 | 0.22115 | 0.157111 | 0.777778 | 0.888889 | -0.111111 | 0.173142 | 0.457808 | 0.684293 | 0.932005 | 0.180767 |
| tossup_correctness | category | Religion | 361 | 0.635973 | 0.595932 | 0.125802 | 0.196428 | 0.736842 | 0.742382 | -0.00554017 | 0.175055 | 0.438309 | 0.669231 | 0.917108 | 0.189816 |
| tossup_correctness | category | Science | 1445 | 0.638178 | 0.568024 | 0.0800971 | 0.187668 | 0.733564 | 0.746021 | -0.0124567 | 0.161341 | 0.479061 | 0.708831 | 0.903228 | 0.184367 |
| tossup_correctness | category | Social Science | 327 | 0.628677 | 0.618938 | 0.116279 | 0.200226 | 0.733945 | 0.718654 | 0.0152905 | 0.170469 | 0.462442 | 0.68334 | 0.92502 | 0.187562 |
| tossup_correctness | category | Unknown | 2039 | 0.614097 | 0.572291 | 0.110777 | 0.191569 | 0.727317 | 0.762138 | -0.034821 | 0.162409 | 0.444405 | 0.684346 | 0.862545 | 0.195533 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.585889 | 0.683607 | 0.222261 | 0.238772 | 0.650273 | 0.743169 | -0.0928962 | 0.193023 | 0.300079 | 0.580528 | 0.833938 | 0.207951 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.561205 | 0.668825 | 0.174993 | 0.232235 | 0.634555 | 0.728796 | -0.0942408 | 0.180638 | 0.358533 | 0.59692 | 0.846368 | 0.207547 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.614114 | 0.594213 | 0.138674 | 0.199723 | 0.710585 | 0.752568 | -0.041983 | 0.170136 | 0.423619 | 0.65568 | 0.887305 | 0.198655 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.615516 | 0.548845 | 0.114997 | 0.178632 | 0.76 | 0.786087 | -0.026087 | 0.157952 | 0.484713 | 0.700962 | 0.919424 | 0.18594 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.615977 | 0.55473 | 0.0590013 | 0.177127 | 0.76772 | 0.764393 | 0.00332779 | 0.136405 | 0.576605 | 0.764288 | 0.944125 | 0.16548 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1197 | 0.580174 | 1.50876 | -3.31379 | -2.09326 | -0.816124 | 1.42306 | 1.82905 | 2.15364 | 2.62735 |
| player | beta | 1197 | -5.48959 | 1.23865 | -7.70172 | -6.9698 | -6.37644 | -5.84963 | -4.84101 | -2.8638 | -1.98393 |
| player | theta_1 | 1197 | -0.647864 | 1.43994 | -4.0668 | -2.88577 | -1.77529 | -0.725745 | 0.469147 | 1.76755 | 2.8194 |
| player | theta_2 | 1197 | -0.611787 | 1.43079 | -3.67805 | -2.71608 | -1.76823 | -0.785287 | 0.658887 | 1.67331 | 3.03188 |
| player | theta_3 | 1197 | -0.859794 | 2.01159 | -4.64405 | -3.61613 | -2.62618 | -1.29547 | 1.19904 | 2.06643 | 3.73244 |
| player | theta_4 | 1197 | -0.422356 | 1.05634 | -3.32934 | -2.15154 | -1.19639 | -0.457447 | 0.35217 | 1.37512 | 2.51155 |
| player | theta_5 | 1197 | -0.382397 | 0.78897 | -2.88911 | -1.68895 | -0.994619 | -0.330091 | 0.265209 | 0.776974 | 1.58062 |
| player | theta_6 | 1197 | -0.437148 | 0.972571 | -3.03257 | -2.05855 | -1.20555 | -0.350271 | 0.380417 | 0.912083 | 2.33412 |
| player | theta_norm | 1197 | 3.37933 | 1.21348 | 0.273086 | 1.42972 | 2.48301 | 3.36412 | 4.33007 | 5.26779 | 6.65559 |
| tossup | start_difficulty_d1 | 1240 | -0.0947625 | 0.571837 | -1.96439 | -1.29218 | -0.353751 | 0.00264297 | 0.276244 | 0.644927 | 1.84565 |
| tossup | start_difficulty_d2 | 1240 | -0.0993874 | 0.641387 | -2.42444 | -1.52814 | -0.363714 | 0.0803798 | 0.312871 | 0.630168 | 1.61708 |
| tossup | start_difficulty_d3 | 1240 | -0.212197 | 0.747528 | -2.838 | -1.76335 | -0.55235 | -0.0253196 | 0.295149 | 0.722829 | 1.79551 |
| tossup | start_difficulty_d4 | 1240 | 0.0495512 | 0.569008 | -2.39155 | -1.44581 | -0.0635187 | 0.219921 | 0.374906 | 0.615822 | 0.985453 |
| tossup | start_difficulty_d5 | 1240 | 0.15995 | 0.381215 | -2.01665 | -0.542693 | 0.0429373 | 0.234301 | 0.38651 | 0.603726 | 1.38897 |
| tossup | start_difficulty_d6 | 1240 | 0.148362 | 0.359457 | -1.89368 | -0.530656 | 0.00542144 | 0.212028 | 0.366639 | 0.598841 | 1.43697 |
| tossup | end_difficulty_d1 | 1240 | -1.93567 | 1.87239 | -10.118 | -5.99526 | -2.1876 | -1.08791 | -0.774317 | -0.378984 | 0.348627 |
| tossup | end_difficulty_d2 | 1240 | -1.82897 | 1.80366 | -10.8099 | -5.69051 | -2.16796 | -1.02935 | -0.697347 | -0.404684 | 0.036345 |
| tossup | end_difficulty_d3 | 1240 | -2.52259 | 2.34677 | -14.7878 | -6.92946 | -4.65731 | -1.27669 | -0.789482 | -0.395122 | 0.414918 |
| tossup | end_difficulty_d4 | 1240 | -1.17155 | 1.29809 | -10.125 | -4.30256 | -1.13447 | -0.764935 | -0.575794 | -0.311618 | 0.0543222 |
| tossup | end_difficulty_d5 | 1240 | -0.959395 | 0.990003 | -10.3388 | -2.04154 | -0.99497 | -0.743094 | -0.577907 | -0.337923 | 0.0231643 |
| tossup | end_difficulty_d6 | 1240 | -1.03391 | 1.0715 | -12.4539 | -2.28715 | -1.08761 | -0.776296 | -0.603937 | -0.342838 | 0.0996574 |
| tossup | total_drop_d1 | 1240 | 1.8409 | 1.70692 | 0.754066 | 0.904511 | 0.966368 | 1.03398 | 1.42395 | 5.66586 | 11.2913 |
| tossup | total_drop_d2 | 1240 | 1.72959 | 1.60881 | 0.810886 | 0.906214 | 0.959368 | 1.01721 | 1.33173 | 5.6275 | 11.8591 |
| tossup | total_drop_d3 | 1240 | 2.31039 | 2.09758 | 0.831918 | 0.910677 | 0.978769 | 1.07001 | 3.66827 | 6.70025 | 13.435 |
| tossup | total_drop_d4 | 1240 | 1.2211 | 0.945824 | 0.78584 | 0.889745 | 0.937874 | 0.978267 | 1.05067 | 2.57908 | 10.0517 |
| tossup | total_drop_d5 | 1240 | 1.11934 | 0.931581 | 0.66229 | 0.893232 | 0.938993 | 0.97336 | 1.02899 | 1.30503 | 11.3962 |
| tossup | total_drop_d6 | 1240 | 1.18228 | 1.02716 | 0.823431 | 0.894231 | 0.941316 | 0.981052 | 1.03854 | 1.48539 | 13.0403 |
| tossup | drop_share_1_d1 | 1240 | 0.261408 | 0.066318 | 0.0326043 | 0.102041 | 0.263796 | 0.2869 | 0.298918 | 0.318929 | 0.453313 |
| tossup | drop_share_2_d1 | 1240 | 0.328062 | 0.0602535 | 0.0558393 | 0.172908 | 0.331296 | 0.343497 | 0.353404 | 0.372053 | 0.640691 |
| tossup | drop_share_3_d1 | 1240 | 0.410529 | 0.117389 | 0.20003 | 0.33292 | 0.352702 | 0.366809 | 0.390978 | 0.716044 | 0.911556 |
| tossup | drop_share_1_d2 | 1240 | 0.262184 | 0.0674914 | 0.0433801 | 0.10229 | 0.268272 | 0.289239 | 0.300862 | 0.318264 | 0.447128 |
| tossup | drop_share_2_d2 | 1240 | 0.326554 | 0.0611508 | 0.057797 | 0.157982 | 0.330805 | 0.343527 | 0.353009 | 0.370332 | 0.543975 |
| tossup | drop_share_3_d2 | 1240 | 0.411262 | 0.12072 | 0.21589 | 0.331361 | 0.35168 | 0.364729 | 0.387896 | 0.732301 | 0.887114 |
| tossup | drop_share_1_d3 | 1240 | 0.246699 | 0.0774765 | 0.0397968 | 0.0902243 | 0.19851 | 0.282863 | 0.297904 | 0.315524 | 0.536849 |
| tossup | drop_share_2_d3 | 1240 | 0.310413 | 0.0776145 | 0.0543812 | 0.134033 | 0.311079 | 0.340648 | 0.352911 | 0.370745 | 0.620001 |
| tossup | drop_share_3_d3 | 1240 | 0.442888 | 0.146544 | 0.183583 | 0.330185 | 0.353797 | 0.372073 | 0.475028 | 0.77159 | 0.905822 |
| tossup | drop_share_1_d4 | 1240 | 0.286078 | 0.0363826 | 0.059334 | 0.204085 | 0.283285 | 0.293121 | 0.302457 | 0.315611 | 0.38053 |
| tossup | drop_share_2_d4 | 1240 | 0.343057 | 0.0311092 | 0.0879552 | 0.320138 | 0.337025 | 0.345618 | 0.354115 | 0.369074 | 0.547125 |
| tossup | drop_share_3_d4 | 1240 | 0.370865 | 0.0580141 | 0.265261 | 0.335012 | 0.350611 | 0.360511 | 0.37083 | 0.420232 | 0.852711 |
| tossup | drop_share_1_d5 | 1240 | 0.290744 | 0.0282936 | 0.0546123 | 0.267195 | 0.284847 | 0.294013 | 0.302673 | 0.315436 | 0.364557 |
| tossup | drop_share_2_d5 | 1240 | 0.344206 | 0.0248803 | 0.0728362 | 0.325009 | 0.338185 | 0.345853 | 0.354571 | 0.367569 | 0.411445 |
| tossup | drop_share_3_d5 | 1240 | 0.365049 | 0.0475749 | 0.297858 | 0.333934 | 0.349994 | 0.359112 | 0.369425 | 0.389123 | 0.872551 |
| tossup | drop_share_1_d6 | 1240 | 0.28804 | 0.0360127 | 0.0593718 | 0.246151 | 0.284874 | 0.294925 | 0.303618 | 0.315425 | 0.351637 |
| tossup | drop_share_2_d6 | 1240 | 0.340779 | 0.0310394 | 0.0825365 | 0.320213 | 0.336278 | 0.344509 | 0.353199 | 0.36526 | 0.43157 |
| tossup | drop_share_3_d6 | 1240 | 0.371182 | 0.0625627 | 0.29901 | 0.335006 | 0.349371 | 0.359824 | 0.370448 | 0.417694 | 0.858092 |
| tossup | r_1 | 1240 | 0.206695 | 0.165332 | 0.0287499 | 0.0549797 | 0.088621 | 0.133901 | 0.263743 | 0.555205 | 0.697944 |
| tossup | r_2 | 1240 | 0.201238 | 0.177294 | 0.0308657 | 0.0540136 | 0.0828239 | 0.117537 | 0.226063 | 0.5806 | 0.695378 |
| tossup | r_3 | 1240 | 0.2488 | 0.189103 | 0.0323375 | 0.0623658 | 0.102693 | 0.156915 | 0.399413 | 0.618552 | 0.783666 |
| tossup | r_4 | 1240 | 0.123741 | 0.105442 | 0.0244898 | 0.0446304 | 0.0657371 | 0.088787 | 0.12805 | 0.393596 | 0.702525 |
| tossup | r_5 | 1240 | 0.104569 | 0.0677737 | 0.0272146 | 0.0441879 | 0.0644508 | 0.0866927 | 0.1189 | 0.228545 | 0.690878 |
| tossup | r_6 | 1240 | 0.114958 | 0.0859515 | 0.0258657 | 0.046327 | 0.0673016 | 0.0874328 | 0.125874 | 0.307416 | 0.698914 |
| tossup | r_norm | 1240 | 0.545107 | 0.0705423 | 0.410844 | 0.438412 | 0.491589 | 0.541457 | 0.592792 | 0.675376 | 0.790014 |
