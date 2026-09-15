# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_6/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_6/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 330167 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.659226 |
| log_loss | 0.516273 |
| ece | 0.0103505 |
| brier | 0.168537 |
| accuracy | 0.769338 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00408822 |
| probability_std | 0.115444 |
| probability_p10 | 0.609056 |
| probability_p50 | 0.790971 |
| probability_p90 | 0.899975 |
| mean_predictive_variance | 0.163846 |
| integrated_brier_score | 0.10296 |
| joint_tossup_event_log_loss | 6.92291 |
| buzz_position_mae | 0.162436 |
| buzz_position_median_absolute_error | 0.147951 |
| buzz_position_bias | -0.0673615 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.367079 |
| first_buzzer_mean_reciprocal_rank | 0.577333 |
| first_buzzer_log_loss | 1.65481 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.646692 |
| tossup_scorer_player_top1_accuracy | 0.334076 |
| tossup_scorer_team_top1_accuracy | 0.49034 |
| tossup_game_winner_accuracy | 0.799559 |
| tossup_game_margin_mae | 34.6627 |
| tournament_player_ppg_spearman | 0.69366 |
| tournament_player_ppg_mae | 9.01635 |
| tournament_player_ppg_top10_overlap | 0.665517 |
| neg_auroc | 0.659226 |
| neg_average_precision | 0.379849 |
| neg_precision | 0.576613 |
| neg_recall | 0.0655362 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0558003 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0957192 |
| no_buzz_calibration_error | 0.0824496 |
| no_buzz_brier | 0.0270295 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9420 |
| first_buzzer_team_top1_accuracy_events | 9295 |
| tossup_scorer_player_top1_accuracy_events | 9420 |
| tossup_scorer_team_top1_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 454 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.659226 | 0.516273 | 0.0103505 | 0.168537 | 0.769338 | 0.76525 | 0.00408822 | 0.115444 | 0.609056 | 0.790971 | 0.899975 | 0.163846 |
| tossup_correctness | tier | fall | 2933 | 0.65236 | 0.486471 | 0.0129056 | 0.15557 | 0.795431 | 0.791681 | 0.00375043 | 0.104094 | 0.647904 | 0.815308 | 0.906638 | 0.15297 |
| tossup_correctness | tier | nationals | 1584 | 0.652237 | 0.56425 | 0.0499514 | 0.18996 | 0.731061 | 0.724747 | 0.00631313 | 0.114474 | 0.513501 | 0.687346 | 0.816682 | 0.206041 |
| tossup_correctness | tier | regionals | 1886 | 0.629416 | 0.547253 | 0.0206512 | 0.181583 | 0.746554 | 0.746023 | 0.000530223 | 0.0951553 | 0.637676 | 0.779573 | 0.874046 | 0.170567 |
| tossup_correctness | tier | winter | 2892 | 0.679886 | 0.500018 | 0.0296972 | 0.161445 | 0.7787 | 0.773167 | 0.0055325 | 0.111292 | 0.648613 | 0.82507 | 0.918381 | 0.147381 |
| tossup_correctness | category | Current Events | 124 | 0.710024 | 0.515488 | 0.0852386 | 0.167614 | 0.790323 | 0.75 | 0.0403226 | 0.110117 | 0.533831 | 0.715013 | 0.838293 | 0.197575 |
| tossup_correctness | category | Fine Arts | 1103 | 0.628279 | 0.536382 | 0.0352956 | 0.175829 | 0.765186 | 0.759746 | 0.00543971 | 0.112678 | 0.630776 | 0.800482 | 0.905017 | 0.15915 |
| tossup_correctness | category | Geography | 197 | 0.742308 | 0.557146 | 0.0474989 | 0.188576 | 0.695431 | 0.670051 | 0.0253807 | 0.148016 | 0.490696 | 0.699399 | 0.87472 | 0.193224 |
| tossup_correctness | category | History | 1491 | 0.683567 | 0.489895 | 0.0518014 | 0.157817 | 0.785379 | 0.787391 | -0.00201207 | 0.120937 | 0.562787 | 0.756743 | 0.874436 | 0.179872 |
| tossup_correctness | category | Literature | 1472 | 0.641986 | 0.477448 | 0.0282283 | 0.150451 | 0.805707 | 0.804348 | 0.0013587 | 0.0989569 | 0.684264 | 0.853344 | 0.928906 | 0.132769 |
| tossup_correctness | category | Mythology | 332 | 0.686559 | 0.457894 | 0.0552223 | 0.145271 | 0.810241 | 0.813253 | -0.00301205 | 0.0995999 | 0.624089 | 0.77654 | 0.879476 | 0.171627 |
| tossup_correctness | category | Other Academic | 69 | 0.49095 | 0.586313 | 0.117802 | 0.197532 | 0.768116 | 0.753623 | 0.0144928 | 0.0992197 | 0.53302 | 0.705283 | 0.821984 | 0.204802 |
| tossup_correctness | category | Philosophy | 324 | 0.695515 | 0.462751 | 0.0213607 | 0.146971 | 0.805556 | 0.799383 | 0.00617284 | 0.11101 | 0.626652 | 0.799628 | 0.903098 | 0.158107 |
| tossup_correctness | category | Popular Culture | 102 | 0.391003 | 0.511679 | 0.142076 | 0.161365 | 0.813725 | 0.833333 | -0.0196078 | 0.0968741 | 0.669745 | 0.787837 | 0.896822 | 0.163416 |
| tossup_correctness | category | Religion | 372 | 0.677504 | 0.56616 | 0.0398256 | 0.192142 | 0.706989 | 0.709677 | -0.00268817 | 0.126295 | 0.558369 | 0.760661 | 0.877411 | 0.178362 |
| tossup_correctness | category | Science | 1487 | 0.684213 | 0.519475 | 0.0293196 | 0.170428 | 0.762609 | 0.752522 | 0.0100874 | 0.117831 | 0.613118 | 0.807805 | 0.909547 | 0.156681 |
| tossup_correctness | category | Social Science | 336 | 0.679068 | 0.56675 | 0.0517074 | 0.192262 | 0.72619 | 0.702381 | 0.0238095 | 0.119473 | 0.572881 | 0.750022 | 0.867024 | 0.18209 |
| tossup_correctness | category | Unknown | 1886 | 0.629416 | 0.547253 | 0.0206512 | 0.181583 | 0.746554 | 0.746023 | 0.000530223 | 0.0951553 | 0.637676 | 0.779573 | 0.874046 | 0.170567 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.632626 | 0.56295 | 0.0561095 | 0.186537 | 0.746193 | 0.736041 | 0.0101523 | 0.122408 | 0.537912 | 0.702395 | 0.830958 | 0.199478 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.658538 | 0.547365 | 0.0176766 | 0.18175 | 0.742132 | 0.735025 | 0.0071066 | 0.119621 | 0.558525 | 0.748237 | 0.8631 | 0.182784 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.677653 | 0.504921 | 0.0173418 | 0.164362 | 0.772546 | 0.769436 | 0.00310973 | 0.111442 | 0.604034 | 0.781972 | 0.885828 | 0.169509 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.655884 | 0.494614 | 0.0160663 | 0.159468 | 0.788207 | 0.78402 | 0.00418702 | 0.11211 | 0.624267 | 0.802564 | 0.90432 | 0.159216 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.654753 | 0.532231 | 0.0296593 | 0.174821 | 0.759346 | 0.756008 | 0.00333778 | 0.113774 | 0.626684 | 0.805261 | 0.913982 | 0.15545 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | -0.788767 | 0.99382 | -4.62425 | -3.20303 | -0.690068 | -0.418603 | -0.254223 | -0.0360816 | 0.534023 |
| player | theta_2 | 1186 | -1.0985 | 1.00747 | -4.30862 | -3.04523 | -1.95367 | -0.563404 | -0.361096 | -0.157757 | 0.317925 |
| player | theta_3 | 1186 | -1.31445 | 0.679032 | -3.65807 | -2.46454 | -1.79523 | -1.31233 | -0.747135 | -0.344997 | 0.221645 |
| player | theta_4 | 1186 | -2.47088 | 0.69195 | -4.98322 | -3.54988 | -2.89858 | -2.46596 | -2.10859 | -1.12412 | -0.0635591 |
| player | theta_5 | 1186 | -0.728311 | 0.432386 | -2.29925 | -1.44807 | -1.01877 | -0.714445 | -0.4154 | -0.0781779 | 0.719319 |
| player | theta_6 | 1186 | -0.757451 | 0.478022 | -2.71964 | -1.61446 | -1.07622 | -0.71457 | -0.334398 | -0.150625 | 0.0574902 |
| player | theta_norm | 1186 | 3.66129 | 0.846638 | 1.6412 | 2.41318 | 3.05514 | 3.54367 | 4.22102 | 5.17904 | 6.30862 |
| tossup | start_difficulty_d1 | 1240 | -1.09575 | 1.3643 | -3.90361 | -3.47847 | -2.71821 | -0.307555 | -0.0730481 | 0.115486 | 0.413763 |
| tossup | start_difficulty_d2 | 1240 | -1.10921 | 1.22385 | -4.47186 | -3.53547 | -1.9542 | -0.515576 | -0.191425 | 0.0574535 | 0.385699 |
| tossup | start_difficulty_d3 | 1240 | -1.02913 | 1.22361 | -4.93616 | -3.53059 | -1.84767 | -0.392841 | -0.107441 | 0.0689621 | 0.345052 |
| tossup | start_difficulty_d4 | 1240 | -2.44663 | 1.44376 | -5.18953 | -4.17749 | -3.59009 | -3.02552 | -0.793045 | -0.105034 | 0.368246 |
| tossup | start_difficulty_d5 | 1240 | -0.497634 | 0.772089 | -3.79513 | -2.29705 | -0.622862 | -0.238975 | -0.0270819 | 0.192883 | 0.831558 |
| tossup | start_difficulty_d6 | 1240 | -0.593472 | 0.722684 | -3.51579 | -2.1347 | -0.895683 | -0.333208 | -0.0722524 | 0.136898 | 0.560095 |
| tossup | end_difficulty_d1 | 1240 | -2.17072 | 1.5136 | -6.61994 | -4.9855 | -3.70103 | -1.31622 | -1.05671 | -0.84045 | -0.542677 |
| tossup | end_difficulty_d2 | 1240 | -2.16153 | 1.31858 | -6.73634 | -4.79981 | -3.11813 | -1.52873 | -1.16579 | -0.902346 | -0.494452 |
| tossup | end_difficulty_d3 | 1240 | -2.06872 | 1.31353 | -7.23748 | -4.8452 | -2.85305 | -1.41757 | -1.10299 | -0.8836 | -0.522242 |
| tossup | end_difficulty_d4 | 1240 | -3.52979 | 1.51621 | -7.14076 | -5.45048 | -4.71047 | -4.02327 | -1.83964 | -1.08298 | -0.5663 |
| tossup | end_difficulty_d5 | 1240 | -1.51679 | 0.849623 | -5.14959 | -3.5585 | -1.679 | -1.23519 | -0.998299 | -0.735449 | -0.0415191 |
| tossup | end_difficulty_d6 | 1240 | -1.61062 | 0.791792 | -4.87031 | -3.32765 | -1.93904 | -1.3373 | -1.04173 | -0.808828 | -0.317949 |
| tossup | total_drop_d1 | 1240 | 1.07496 | 0.252764 | 0.650845 | 0.903227 | 0.964938 | 1.00428 | 1.06865 | 1.54259 | 3.68338 |
| tossup | total_drop_d2 | 1240 | 1.05232 | 0.190353 | 0.601443 | 0.883799 | 0.962062 | 1.00582 | 1.07168 | 1.42286 | 2.96358 |
| tossup | total_drop_d3 | 1240 | 1.03958 | 0.206977 | 0.692201 | 0.87283 | 0.957631 | 1.00232 | 1.05779 | 1.32562 | 3.67366 |
| tossup | total_drop_d4 | 1240 | 1.08316 | 0.297647 | 0.380387 | 0.716401 | 0.92969 | 1.03107 | 1.18615 | 1.57222 | 3.54829 |
| tossup | total_drop_d5 | 1240 | 1.01915 | 0.11274 | 0.843619 | 0.907429 | 0.954355 | 0.995904 | 1.04614 | 1.25137 | 1.86867 |
| tossup | total_drop_d6 | 1240 | 1.01714 | 0.0992368 | 0.839681 | 0.909299 | 0.956673 | 0.99595 | 1.04683 | 1.20235 | 1.84143 |
| tossup | drop_share_1_d1 | 1240 | 0.332054 | 0.0406643 | 0.266768 | 0.295267 | 0.305587 | 0.314708 | 0.35012 | 0.416652 | 0.503619 |
| tossup | drop_share_2_d1 | 1240 | 0.343445 | 0.013027 | 0.291783 | 0.321733 | 0.3366 | 0.343475 | 0.351805 | 0.363186 | 0.410836 |
| tossup | drop_share_3_d1 | 1240 | 0.324501 | 0.0361872 | 0.179405 | 0.245463 | 0.311971 | 0.338333 | 0.348034 | 0.359685 | 0.374019 |
| tossup | drop_share_1_d2 | 1240 | 0.329734 | 0.034898 | 0.279654 | 0.297261 | 0.307869 | 0.317657 | 0.338525 | 0.40543 | 0.5298 |
| tossup | drop_share_2_d2 | 1240 | 0.343596 | 0.0124771 | 0.298186 | 0.321262 | 0.336808 | 0.344493 | 0.352004 | 0.361534 | 0.386565 |
| tossup | drop_share_3_d2 | 1240 | 0.32667 | 0.0302088 | 0.169676 | 0.258939 | 0.317865 | 0.336183 | 0.345768 | 0.357407 | 0.391701 |
| tossup | drop_share_1_d3 | 1240 | 0.323107 | 0.0308621 | 0.261682 | 0.294312 | 0.305728 | 0.314194 | 0.327898 | 0.391838 | 0.622308 |
| tossup | drop_share_2_d3 | 1240 | 0.343838 | 0.0125564 | 0.246437 | 0.32282 | 0.336743 | 0.344774 | 0.351929 | 0.362028 | 0.381693 |
| tossup | drop_share_3_d3 | 1240 | 0.333055 | 0.0275898 | 0.131255 | 0.271817 | 0.3273 | 0.339587 | 0.34957 | 0.361884 | 0.405459 |
| tossup | drop_share_1_d4 | 1240 | 0.35562 | 0.0473489 | 0.197499 | 0.300111 | 0.319037 | 0.347482 | 0.384462 | 0.443264 | 0.587695 |
| tossup | drop_share_2_d4 | 1240 | 0.335402 | 0.0207177 | 0.258898 | 0.303091 | 0.321579 | 0.336631 | 0.348467 | 0.36475 | 0.542452 |
| tossup | drop_share_3_d4 | 1240 | 0.308979 | 0.041427 | 0.148514 | 0.234548 | 0.282706 | 0.318285 | 0.338614 | 0.359532 | 0.445769 |
| tossup | drop_share_1_d5 | 1240 | 0.313641 | 0.0150399 | 0.279443 | 0.294892 | 0.304423 | 0.310972 | 0.319811 | 0.342493 | 0.395167 |
| tossup | drop_share_2_d5 | 1240 | 0.346179 | 0.0099261 | 0.31184 | 0.329782 | 0.339284 | 0.34645 | 0.353263 | 0.361527 | 0.37562 |
| tossup | drop_share_3_d5 | 1240 | 0.34018 | 0.0151925 | 0.244661 | 0.312497 | 0.332943 | 0.342002 | 0.349535 | 0.362193 | 0.380677 |
| tossup | drop_share_1_d6 | 1240 | 0.315819 | 0.0146356 | 0.278535 | 0.295925 | 0.306086 | 0.313748 | 0.322905 | 0.341167 | 0.392294 |
| tossup | drop_share_2_d6 | 1240 | 0.346278 | 0.00970087 | 0.308912 | 0.330042 | 0.339852 | 0.346684 | 0.352671 | 0.362792 | 0.375427 |
| tossup | drop_share_3_d6 | 1240 | 0.337903 | 0.015096 | 0.269512 | 0.310684 | 0.32925 | 0.340025 | 0.348077 | 0.359707 | 0.374202 |
| tossup | r_1 | 1240 | 0.191868 | 0.237465 | 0.0131976 | 0.0201381 | 0.0305623 | 0.0451749 | 0.4787 | 0.619692 | 0.752189 |
| tossup | r_2 | 1240 | 0.159015 | 0.181861 | 0.0157743 | 0.0231215 | 0.0381492 | 0.0655925 | 0.226756 | 0.543625 | 0.749779 |
| tossup | r_3 | 1240 | 0.106565 | 0.0964511 | 0.0147785 | 0.029943 | 0.0434643 | 0.063909 | 0.132095 | 0.336302 | 0.521213 |
| tossup | r_4 | 1240 | 0.395755 | 0.245855 | 0.0369239 | 0.0561315 | 0.126374 | 0.40849 | 0.609173 | 0.761297 | 0.899045 |
| tossup | r_5 | 1240 | 0.0703895 | 0.0493324 | 0.012892 | 0.0259776 | 0.0392325 | 0.0538663 | 0.0805036 | 0.185082 | 0.311242 |
| tossup | r_6 | 1240 | 0.0764075 | 0.0488381 | 0.0147648 | 0.0281309 | 0.0421095 | 0.0593606 | 0.0962437 | 0.187005 | 0.290893 |
| tossup | r_norm | 1240 | 0.631833 | 0.0745562 | 0.465921 | 0.527862 | 0.578622 | 0.619158 | 0.677555 | 0.770497 | 0.900483 |
