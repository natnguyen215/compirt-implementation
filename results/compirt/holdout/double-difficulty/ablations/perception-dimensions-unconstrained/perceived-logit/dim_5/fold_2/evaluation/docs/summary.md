# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_5/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_5/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 336055 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.552855 |
| log_loss | 0.5906 |
| ece | 0.0925174 |
| brier | 0.188842 |
| accuracy | 0.763746 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.000432105 |
| probability_std | 0.109868 |
| probability_p10 | 0.665827 |
| probability_p50 | 0.870759 |
| probability_p90 | 0.941793 |
| mean_predictive_variance | 0.12529 |
| integrated_brier_score | 0.174711 |
| joint_tossup_event_log_loss | 7.73144 |
| buzz_position_mae | 0.335664 |
| buzz_position_median_absolute_error | 0.336204 |
| buzz_position_bias | -0.321998 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.343848 |
| first_buzzer_mean_reciprocal_rank | 0.558609 |
| first_buzzer_log_loss | 1.67591 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.632494 |
| tossup_scorer_player_top1_accuracy | 0.26887 |
| tossup_scorer_team_top1_accuracy | 0.401919 |
| tossup_game_winner_accuracy | 0.693478 |
| tossup_game_margin_mae | 47.3987 |
| tournament_player_ppg_spearman | 0.597048 |
| tournament_player_ppg_mae | 10.3695 |
| tournament_player_ppg_top10_overlap | 0.582759 |
| neg_auroc | 0.552855 |
| neg_average_precision | 0.285316 |
| neg_precision | 0.477778 |
| neg_recall | 0.0196977 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0312253 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.22626 |
| no_buzz_calibration_error | 0.213147 |
| no_buzz_brier | 0.0666989 |
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
| tossup_correctness | aggregate | all | 9257 | 0.552855 | 0.5906 | 0.0925174 | 0.188842 | 0.763746 | 0.764178 | -0.000432105 | 0.109868 | 0.665827 | 0.870759 | 0.941793 | 0.12529 |
| tossup_correctness | tier | fall | 2798 | 0.548163 | 0.554364 | 0.0809835 | 0.1755 | 0.784132 | 0.785204 | -0.00107219 | 0.084662 | 0.745139 | 0.876737 | 0.93664 | 0.116731 |
| tossup_correctness | tier | nationals | 1545 | 0.573402 | 0.620731 | 0.083886 | 0.206823 | 0.721036 | 0.721036 | 0 | 0.134802 | 0.576419 | 0.792987 | 0.926548 | 0.160566 |
| tossup_correctness | tier | regionals | 2039 | 0.539072 | 0.595012 | 0.088685 | 0.189772 | 0.761157 | 0.762138 | -0.000980873 | 0.119878 | 0.634078 | 0.854552 | 0.941819 | 0.134327 |
| tossup_correctness | tier | winter | 2875 | 0.544876 | 0.606546 | 0.118629 | 0.191504 | 0.768696 | 0.768348 | 0.000347826 | 0.0889004 | 0.728371 | 0.893973 | 0.948022 | 0.108254 |
| tossup_correctness | category | Current Events | 129 | 0.541374 | 0.730629 | 0.176665 | 0.249289 | 0.666667 | 0.666667 | 0 | 0.111777 | 0.646106 | 0.85278 | 0.908693 | 0.138809 |
| tossup_correctness | category | Fine Arts | 1074 | 0.552823 | 0.580165 | 0.104912 | 0.183899 | 0.775605 | 0.776536 | -0.000931099 | 0.103553 | 0.697228 | 0.889909 | 0.944667 | 0.115502 |
| tossup_correctness | category | Geography | 180 | 0.597989 | 0.834811 | 0.23926 | 0.288156 | 0.611111 | 0.616667 | -0.00555556 | 0.106015 | 0.673456 | 0.874718 | 0.936621 | 0.124554 |
| tossup_correctness | category | History | 1454 | 0.547308 | 0.59703 | 0.0939869 | 0.192641 | 0.757221 | 0.757909 | -0.000687758 | 0.107274 | 0.658936 | 0.862499 | 0.936086 | 0.129111 |
| tossup_correctness | category | Literature | 1435 | 0.541706 | 0.519649 | 0.0766601 | 0.159185 | 0.810453 | 0.810453 | 0 | 0.0987237 | 0.70711 | 0.894987 | 0.948743 | 0.11093 |
| tossup_correctness | category | Mythology | 324 | 0.562983 | 0.548665 | 0.113457 | 0.172724 | 0.796296 | 0.79321 | 0.00308642 | 0.105374 | 0.696488 | 0.89604 | 0.942764 | 0.110416 |
| tossup_correctness | category | Other Academic | 71 | 0.312636 | 0.738868 | 0.224964 | 0.234725 | 0.732394 | 0.760563 | -0.028169 | 0.13314 | 0.594827 | 0.883579 | 0.935815 | 0.128771 |
| tossup_correctness | category | Philosophy | 310 | 0.510765 | 0.63732 | 0.140512 | 0.200133 | 0.758065 | 0.76129 | -0.00322581 | 0.101636 | 0.682793 | 0.893471 | 0.949191 | 0.111212 |
| tossup_correctness | category | Popular Culture | 108 | 0.59375 | 0.354195 | 0.0374089 | 0.102149 | 0.87963 | 0.888889 | -0.00925926 | 0.073132 | 0.781847 | 0.871362 | 0.925407 | 0.116354 |
| tossup_correctness | category | Religion | 361 | 0.562009 | 0.63312 | 0.138813 | 0.204046 | 0.745152 | 0.742382 | 0.00277008 | 0.105285 | 0.686953 | 0.881095 | 0.940256 | 0.118486 |
| tossup_correctness | category | Science | 1445 | 0.572285 | 0.597946 | 0.0875653 | 0.194822 | 0.746713 | 0.746021 | 0.000692042 | 0.110687 | 0.645159 | 0.842238 | 0.93396 | 0.138085 |
| tossup_correctness | category | Social Science | 327 | 0.594218 | 0.654224 | 0.132696 | 0.214745 | 0.724771 | 0.718654 | 0.00611621 | 0.101728 | 0.679931 | 0.873115 | 0.933519 | 0.123443 |
| tossup_correctness | category | Unknown | 2039 | 0.539072 | 0.595012 | 0.088685 | 0.189772 | 0.761157 | 0.762138 | -0.000980873 | 0.119878 | 0.634078 | 0.854552 | 0.941819 | 0.134327 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.468867 | 0.647563 | 0.111037 | 0.209965 | 0.721311 | 0.743169 | -0.0218579 | 0.110147 | 0.645072 | 0.831209 | 0.920077 | 0.143249 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.525599 | 0.6373 | 0.105396 | 0.211798 | 0.724607 | 0.728796 | -0.00418848 | 0.106843 | 0.660462 | 0.84219 | 0.919364 | 0.140477 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.544955 | 0.600923 | 0.0907473 | 0.194679 | 0.753015 | 0.752568 | 0.000446628 | 0.103297 | 0.673729 | 0.856713 | 0.931594 | 0.131973 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.556415 | 0.551214 | 0.0854891 | 0.173753 | 0.787478 | 0.786087 | 0.0013913 | 0.109232 | 0.668809 | 0.877709 | 0.940322 | 0.123308 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.561908 | 0.602281 | 0.102149 | 0.190347 | 0.76406 | 0.764393 | -0.000332779 | 0.11424 | 0.654197 | 0.89301 | 0.950702 | 0.116287 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1197 | -1.19533 | 0.898707 | -3.36559 | -2.39552 | -1.74394 | -1.33248 | -0.841151 | 0.717632 | 2.20743 |
| player | beta | 1197 | -3.78712 | 1.23549 | -7.26611 | -6.37498 | -4.41393 | -3.48474 | -2.82915 | -2.26687 | -1.94311 |
| player | theta_1 | 1197 | 0.790922 | 1.02212 | -2.64955 | -1.06308 | 0.110994 | 0.965709 | 1.58685 | 2.23959 | 3.24397 |
| player | theta_2 | 1197 | 0.768076 | 0.929133 | -2.32637 | -0.924345 | 0.220023 | 0.902503 | 1.42006 | 2.10795 | 3.32909 |
| player | theta_3 | 1197 | 0.720025 | 0.767203 | -1.85591 | -0.728111 | 0.240888 | 0.851938 | 1.27378 | 1.81951 | 2.55133 |
| player | theta_4 | 1197 | 0.643701 | 0.649069 | -2.07747 | -0.682578 | 0.332729 | 0.741184 | 1.04663 | 1.54787 | 3.31122 |
| player | theta_5 | 1197 | 0.697535 | 0.797009 | -2.16938 | -0.844297 | 0.247806 | 0.829806 | 1.23775 | 1.82926 | 2.64359 |
| player | theta_norm | 1197 | 2.38127 | 0.717632 | 0.278424 | 1.12259 | 1.96524 | 2.41551 | 2.82854 | 3.53838 | 5.00268 |
| tossup | start_difficulty_d1 | 1240 | -0.83595 | 0.403043 | -2.09286 | -1.6055 | -1.10281 | -0.766606 | -0.527078 | -0.283202 | -0.0319204 |
| tossup | start_difficulty_d2 | 1240 | -0.834349 | 0.474503 | -2.43309 | -1.70657 | -1.16839 | -0.7472 | -0.478185 | -0.17373 | 0.0479269 |
| tossup | start_difficulty_d3 | 1240 | -0.753013 | 0.361346 | -2.12883 | -1.43247 | -0.969934 | -0.699814 | -0.49434 | -0.226269 | 0.0506342 |
| tossup | start_difficulty_d4 | 1240 | -0.700764 | 0.300625 | -1.86378 | -1.20501 | -0.887553 | -0.689094 | -0.499012 | -0.229102 | 0.103986 |
| tossup | start_difficulty_d5 | 1240 | -0.734383 | 0.389221 | -2.24855 | -1.46843 | -0.949717 | -0.655271 | -0.464184 | -0.208903 | 0.108726 |
| tossup | end_difficulty_d1 | 1240 | -1.63419 | 0.327651 | -2.67785 | -2.21757 | -1.84865 | -1.60613 | -1.39826 | -1.14074 | -0.813672 |
| tossup | end_difficulty_d2 | 1240 | -1.64744 | 0.424825 | -3.38852 | -2.3817 | -1.94274 | -1.61828 | -1.31524 | -1.0294 | -0.729104 |
| tossup | end_difficulty_d3 | 1240 | -1.58762 | 0.323197 | -2.62409 | -2.12932 | -1.81161 | -1.57391 | -1.35114 | -1.0695 | -0.669685 |
| tossup | end_difficulty_d4 | 1240 | -1.55882 | 0.303207 | -2.54346 | -2.06676 | -1.7556 | -1.54975 | -1.34978 | -1.07454 | -0.611439 |
| tossup | end_difficulty_d5 | 1240 | -1.57948 | 0.356365 | -2.74655 | -2.23081 | -1.80399 | -1.54628 | -1.315 | -1.06484 | -0.621133 |
| tossup | total_drop_d1 | 1240 | 0.79824 | 0.217654 | 0.280736 | 0.390323 | 0.662222 | 0.815457 | 0.959997 | 1.10467 | 1.48318 |
| tossup | total_drop_d2 | 1240 | 0.813093 | 0.19745 | 0.26379 | 0.454021 | 0.699072 | 0.826294 | 0.937634 | 1.11843 | 1.57325 |
| tossup | total_drop_d3 | 1240 | 0.834605 | 0.180153 | 0.307416 | 0.489159 | 0.735409 | 0.840533 | 0.951971 | 1.11759 | 1.33617 |
| tossup | total_drop_d4 | 1240 | 0.858061 | 0.15197 | 0.293554 | 0.632864 | 0.76157 | 0.842233 | 0.953743 | 1.12177 | 1.58324 |
| tossup | total_drop_d5 | 1240 | 0.845097 | 0.172067 | 0.286824 | 0.541167 | 0.751351 | 0.844754 | 0.950801 | 1.11168 | 1.45068 |
| tossup | drop_share_1_d1 | 1240 | 0.316442 | 0.0212116 | 0.233381 | 0.283512 | 0.304832 | 0.314608 | 0.327813 | 0.352015 | 0.406166 |
| tossup | drop_share_2_d1 | 1240 | 0.330668 | 0.01807 | 0.261322 | 0.295041 | 0.321054 | 0.333448 | 0.343293 | 0.356075 | 0.372877 |
| tossup | drop_share_3_d1 | 1240 | 0.352891 | 0.0259772 | 0.272649 | 0.318438 | 0.337221 | 0.349128 | 0.362523 | 0.406104 | 0.470856 |
| tossup | drop_share_1_d2 | 1240 | 0.316277 | 0.021456 | 0.233336 | 0.286797 | 0.303141 | 0.314519 | 0.326678 | 0.354449 | 0.440099 |
| tossup | drop_share_2_d2 | 1240 | 0.332195 | 0.0154549 | 0.275528 | 0.303618 | 0.323597 | 0.334191 | 0.343083 | 0.353965 | 0.374188 |
| tossup | drop_share_3_d2 | 1240 | 0.351528 | 0.022619 | 0.266303 | 0.318329 | 0.337316 | 0.350255 | 0.362674 | 0.389742 | 0.491119 |
| tossup | drop_share_1_d3 | 1240 | 0.315699 | 0.0185465 | 0.218406 | 0.287775 | 0.304545 | 0.316056 | 0.326734 | 0.345268 | 0.387324 |
| tossup | drop_share_2_d3 | 1240 | 0.333336 | 0.0155085 | 0.267777 | 0.304548 | 0.325776 | 0.335325 | 0.343313 | 0.355046 | 0.371633 |
| tossup | drop_share_3_d3 | 1240 | 0.350965 | 0.0230298 | 0.297997 | 0.321319 | 0.336683 | 0.348228 | 0.359749 | 0.392647 | 0.487026 |
| tossup | drop_share_1_d4 | 1240 | 0.314163 | 0.0155285 | 0.248096 | 0.289698 | 0.303933 | 0.313977 | 0.324355 | 0.339251 | 0.379122 |
| tossup | drop_share_2_d4 | 1240 | 0.335355 | 0.0130793 | 0.283488 | 0.311782 | 0.327483 | 0.335787 | 0.344149 | 0.356192 | 0.374436 |
| tossup | drop_share_3_d4 | 1240 | 0.350483 | 0.0179696 | 0.288498 | 0.324745 | 0.337935 | 0.34897 | 0.360834 | 0.382042 | 0.437993 |
| tossup | drop_share_1_d5 | 1240 | 0.316374 | 0.0188666 | 0.241246 | 0.289818 | 0.30446 | 0.315057 | 0.325776 | 0.350804 | 0.397077 |
| tossup | drop_share_2_d5 | 1240 | 0.33424 | 0.0137531 | 0.272249 | 0.3111 | 0.326014 | 0.335381 | 0.343446 | 0.354426 | 0.374986 |
| tossup | drop_share_3_d5 | 1240 | 0.349387 | 0.018942 | 0.274032 | 0.31931 | 0.338293 | 0.348824 | 0.359927 | 0.381307 | 0.449538 |
| tossup | r_1 | 1240 | 0.234152 | 0.187762 | 0.0320638 | 0.0653231 | 0.108838 | 0.155459 | 0.291545 | 0.680365 | 0.828446 |
| tossup | r_2 | 1240 | 0.222062 | 0.141425 | 0.033694 | 0.05757 | 0.118228 | 0.192458 | 0.278312 | 0.526322 | 0.792224 |
| tossup | r_3 | 1240 | 0.185468 | 0.118518 | 0.0338441 | 0.0634239 | 0.116396 | 0.166769 | 0.206031 | 0.4606 | 0.805018 |
| tossup | r_4 | 1240 | 0.169262 | 0.0751818 | 0.0438424 | 0.0660308 | 0.110038 | 0.170259 | 0.218231 | 0.261283 | 0.663066 |
| tossup | r_5 | 1240 | 0.189056 | 0.100361 | 0.0339211 | 0.0577429 | 0.118233 | 0.185786 | 0.231925 | 0.36658 | 0.748332 |
| tossup | r_norm | 1240 | 0.528922 | 0.0901969 | 0.447394 | 0.450847 | 0.460623 | 0.490889 | 0.570796 | 0.740176 | 0.83292 |
