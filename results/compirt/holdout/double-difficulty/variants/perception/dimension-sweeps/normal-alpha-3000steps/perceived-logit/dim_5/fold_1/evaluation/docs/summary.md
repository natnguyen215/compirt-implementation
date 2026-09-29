# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_5/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_5/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 337031 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.563571 |
| log_loss | 0.591767 |
| ece | 0.090725 |
| brier | 0.189595 |
| accuracy | 0.760915 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00120972 |
| probability_std | 0.108686 |
| probability_p10 | 0.671533 |
| probability_p50 | 0.875619 |
| probability_p90 | 0.942404 |
| mean_predictive_variance | 0.123435 |
| integrated_brier_score | 0.174931 |
| joint_tossup_event_log_loss | 7.7351 |
| buzz_position_mae | 0.340234 |
| buzz_position_median_absolute_error | 0.345077 |
| buzz_position_bias | -0.327523 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.339822 |
| first_buzzer_mean_reciprocal_rank | 0.554384 |
| first_buzzer_log_loss | 1.69205 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.620587 |
| tossup_scorer_player_top1_accuracy | 0.267316 |
| tossup_scorer_team_top1_accuracy | 0.39026 |
| tossup_game_winner_accuracy | 0.718468 |
| tossup_game_margin_mae | 42.8859 |
| tournament_player_ppg_spearman | 0.573756 |
| tournament_player_ppg_mae | 10.4568 |
| tournament_player_ppg_top10_overlap | 0.586207 |
| neg_auroc | 0.563571 |
| neg_average_precision | 0.290313 |
| neg_precision | 0.438202 |
| neg_recall | 0.0180305 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.031128 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.227189 |
| no_buzz_calibration_error | 0.21128 |
| no_buzz_brier | 0.0679926 |
| full_pmf_max_mass_error | 1.22125e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.563571 | 0.591767 | 0.090725 | 0.189595 | 0.760915 | 0.762125 | -0.00120972 | 0.108686 | 0.671533 | 0.875619 | 0.942404 | 0.123435 |
| tossup_correctness | tier | fall | 2842 | 0.571401 | 0.544857 | 0.0767081 | 0.173304 | 0.785362 | 0.785362 | 0 | 0.0889399 | 0.732606 | 0.879206 | 0.935452 | 0.117095 |
| tossup_correctness | tier | nationals | 1564 | 0.554996 | 0.628064 | 0.0877415 | 0.211367 | 0.710997 | 0.718031 | -0.00703325 | 0.132589 | 0.574874 | 0.768485 | 0.926669 | 0.165869 |
| tossup_correctness | tier | regionals | 1937 | 0.541264 | 0.604513 | 0.0869307 | 0.192485 | 0.758389 | 0.758389 | 0 | 0.111869 | 0.657203 | 0.865909 | 0.943781 | 0.128434 |
| tossup_correctness | tier | winter | 2750 | 0.554359 | 0.610626 | 0.111989 | 0.192014 | 0.765818 | 0.765818 | 0 | 0.0820932 | 0.753714 | 0.900639 | 0.949959 | 0.102334 |
| tossup_correctness | category | Current Events | 126 | 0.483825 | 0.600001 | 0.110031 | 0.195446 | 0.746032 | 0.769841 | -0.0238095 | 0.11363 | 0.648799 | 0.848702 | 0.916873 | 0.138803 |
| tossup_correctness | category | Fine Arts | 1071 | 0.589554 | 0.583723 | 0.100582 | 0.186661 | 0.764706 | 0.766573 | -0.00186741 | 0.100227 | 0.689866 | 0.890039 | 0.945692 | 0.114149 |
| tossup_correctness | category | Geography | 185 | 0.543189 | 0.722729 | 0.165707 | 0.238356 | 0.697297 | 0.697297 | 0 | 0.118063 | 0.670895 | 0.879811 | 0.941968 | 0.121685 |
| tossup_correctness | category | History | 1440 | 0.554944 | 0.605363 | 0.103243 | 0.196162 | 0.75625 | 0.754167 | 0.00208333 | 0.108597 | 0.667264 | 0.869051 | 0.937423 | 0.127746 |
| tossup_correctness | category | Literature | 1422 | 0.552163 | 0.510144 | 0.066752 | 0.156215 | 0.809423 | 0.814346 | -0.00492264 | 0.0999546 | 0.699079 | 0.896114 | 0.949148 | 0.111548 |
| tossup_correctness | category | Mythology | 318 | 0.590593 | 0.541541 | 0.1018 | 0.171274 | 0.795597 | 0.789308 | 0.00628931 | 0.0997187 | 0.702575 | 0.893064 | 0.938906 | 0.112106 |
| tossup_correctness | category | Other Academic | 66 | 0.453527 | 0.741365 | 0.214046 | 0.246386 | 0.712121 | 0.712121 | 0 | 0.125186 | 0.610268 | 0.858706 | 0.94076 | 0.137338 |
| tossup_correctness | category | Philosophy | 311 | 0.593682 | 0.62136 | 0.117139 | 0.198782 | 0.73955 | 0.745981 | -0.00643087 | 0.108105 | 0.663445 | 0.895511 | 0.948424 | 0.111744 |
| tossup_correctness | category | Popular Culture | 102 | 0.584259 | 0.37579 | 0.0489728 | 0.110523 | 0.862745 | 0.882353 | -0.0196078 | 0.0809108 | 0.785759 | 0.873346 | 0.930791 | 0.115556 |
| tossup_correctness | category | Religion | 358 | 0.581611 | 0.683053 | 0.150011 | 0.226154 | 0.703911 | 0.712291 | -0.00837989 | 0.117806 | 0.645939 | 0.885926 | 0.938326 | 0.121338 |
| tossup_correctness | category | Science | 1433 | 0.565704 | 0.612282 | 0.0876095 | 0.199897 | 0.739707 | 0.738311 | 0.00139567 | 0.112497 | 0.651617 | 0.846026 | 0.93535 | 0.135867 |
| tossup_correctness | category | Social Science | 324 | 0.593773 | 0.628797 | 0.11558 | 0.205751 | 0.734568 | 0.731481 | 0.00308642 | 0.102913 | 0.683008 | 0.881768 | 0.934274 | 0.121611 |
| tossup_correctness | category | Unknown | 1937 | 0.541264 | 0.604513 | 0.0869307 | 0.192485 | 0.758389 | 0.758389 | 0 | 0.111869 | 0.657203 | 0.865909 | 0.943781 | 0.128434 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.531688 | 0.654917 | 0.108557 | 0.218105 | 0.694611 | 0.712575 | -0.0179641 | 0.11097 | 0.639134 | 0.819 | 0.916214 | 0.148176 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.559922 | 0.622889 | 0.0921679 | 0.206528 | 0.724781 | 0.729167 | -0.00438596 | 0.109445 | 0.649369 | 0.843767 | 0.917347 | 0.14127 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.535367 | 0.602754 | 0.0975971 | 0.195473 | 0.756028 | 0.755083 | 0.000945626 | 0.10394 | 0.677045 | 0.860891 | 0.930877 | 0.129969 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.573617 | 0.555343 | 0.08093 | 0.176741 | 0.781294 | 0.780942 | 0.000351617 | 0.104349 | 0.684434 | 0.88077 | 0.939542 | 0.121189 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.567615 | 0.605326 | 0.0973015 | 0.190879 | 0.759738 | 0.762029 | -0.00229133 | 0.113016 | 0.667936 | 0.895821 | 0.95125 | 0.114326 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1167 | -1.19779 | 0.906076 | -3.35483 | -2.4188 | -1.75245 | -1.32833 | -0.830583 | 0.816403 | 2.14636 |
| player | beta | 1167 | -3.78524 | 1.2449 | -7.21183 | -6.36437 | -4.47303 | -3.51873 | -2.81813 | -2.25865 | -1.86036 |
| player | theta_1 | 1167 | 0.807637 | 1.04142 | -2.35545 | -1.06084 | 0.0455871 | 1.01921 | 1.561 | 2.26617 | 3.49911 |
| player | theta_2 | 1167 | 0.757249 | 0.878596 | -2.29467 | -0.917202 | 0.312601 | 0.877447 | 1.34332 | 1.96747 | 3.37315 |
| player | theta_3 | 1167 | 0.728748 | 0.775524 | -1.66977 | -0.751138 | 0.248841 | 0.829912 | 1.30391 | 1.81452 | 2.3855 |
| player | theta_4 | 1167 | 0.6699 | 0.739042 | -1.97289 | -0.762905 | 0.290623 | 0.772496 | 1.14226 | 1.67805 | 3.5441 |
| player | theta_5 | 1167 | 0.681046 | 0.735691 | -1.73972 | -0.758357 | 0.274786 | 0.797803 | 1.15298 | 1.73219 | 2.66323 |
| player | theta_norm | 1167 | 2.3853 | 0.722812 | 0.261458 | 1.11754 | 1.93022 | 2.4386 | 2.84996 | 3.50105 | 5.06458 |
| tossup | start_difficulty_d1 | 1220 | -0.843703 | 0.41835 | -2.11971 | -1.62617 | -1.13296 | -0.787718 | -0.509597 | -0.267496 | 0.124337 |
| tossup | start_difficulty_d2 | 1220 | -0.811122 | 0.462482 | -2.43137 | -1.64966 | -1.13153 | -0.734866 | -0.467061 | -0.17617 | 0.264938 |
| tossup | start_difficulty_d3 | 1220 | -0.759804 | 0.377668 | -2.05247 | -1.44381 | -0.996946 | -0.708441 | -0.484206 | -0.223393 | 0.180431 |
| tossup | start_difficulty_d4 | 1220 | -0.711175 | 0.339973 | -2.05579 | -1.38086 | -0.885263 | -0.665547 | -0.487857 | -0.22657 | 0.206806 |
| tossup | start_difficulty_d5 | 1220 | -0.725244 | 0.368593 | -1.99368 | -1.41232 | -0.951311 | -0.679495 | -0.47087 | -0.198288 | 0.190388 |
| tossup | end_difficulty_d1 | 1220 | -1.63795 | 0.336141 | -2.79355 | -2.2116 | -1.87258 | -1.62085 | -1.39134 | -1.12886 | -0.668634 |
| tossup | end_difficulty_d2 | 1220 | -1.63195 | 0.42078 | -2.98862 | -2.38641 | -1.91439 | -1.58154 | -1.31356 | -1.01802 | -0.565322 |
| tossup | end_difficulty_d3 | 1220 | -1.58814 | 0.329956 | -2.55306 | -2.14245 | -1.81344 | -1.57788 | -1.35778 | -1.05498 | -0.724166 |
| tossup | end_difficulty_d4 | 1220 | -1.55683 | 0.306524 | -2.48958 | -2.09735 | -1.75475 | -1.5323 | -1.35004 | -1.08907 | -0.601293 |
| tossup | end_difficulty_d5 | 1220 | -1.57002 | 0.337598 | -2.56526 | -2.14978 | -1.80433 | -1.55986 | -1.31779 | -1.04706 | -0.597033 |
| tossup | total_drop_d1 | 1220 | 0.794247 | 0.218842 | 0.262451 | 0.384828 | 0.649775 | 0.815334 | 0.95873 | 1.11849 | 1.3212 |
| tossup | total_drop_d2 | 1220 | 0.820826 | 0.183889 | 0.31893 | 0.506354 | 0.707229 | 0.8269 | 0.93839 | 1.12096 | 1.48802 |
| tossup | total_drop_d3 | 1220 | 0.828335 | 0.181988 | 0.314713 | 0.484025 | 0.730472 | 0.833835 | 0.951336 | 1.1081 | 1.31606 |
| tossup | total_drop_d4 | 1220 | 0.845656 | 0.163924 | 0.241421 | 0.556298 | 0.752309 | 0.84383 | 0.951799 | 1.10663 | 1.34691 |
| tossup | total_drop_d5 | 1220 | 0.84478 | 0.166873 | 0.320985 | 0.55218 | 0.75618 | 0.841145 | 0.946878 | 1.11193 | 1.34271 |
| tossup | drop_share_1_d1 | 1220 | 0.31647 | 0.0211484 | 0.245175 | 0.285254 | 0.303954 | 0.314509 | 0.327966 | 0.353663 | 0.412876 |
| tossup | drop_share_2_d1 | 1220 | 0.330481 | 0.0181453 | 0.257751 | 0.295881 | 0.320437 | 0.33348 | 0.342983 | 0.355612 | 0.376842 |
| tossup | drop_share_3_d1 | 1220 | 0.353049 | 0.025649 | 0.285509 | 0.319262 | 0.337597 | 0.349333 | 0.363105 | 0.403238 | 0.474686 |
| tossup | drop_share_1_d2 | 1220 | 0.316107 | 0.02093 | 0.244937 | 0.287182 | 0.303299 | 0.314127 | 0.326293 | 0.351998 | 0.418789 |
| tossup | drop_share_2_d2 | 1220 | 0.333014 | 0.0142667 | 0.275615 | 0.307196 | 0.324515 | 0.334235 | 0.342923 | 0.354193 | 0.370349 |
| tossup | drop_share_3_d2 | 1220 | 0.350879 | 0.0209851 | 0.274455 | 0.318695 | 0.338027 | 0.350385 | 0.362252 | 0.388039 | 0.443107 |
| tossup | drop_share_1_d3 | 1220 | 0.315824 | 0.0189771 | 0.222144 | 0.287308 | 0.304506 | 0.315601 | 0.32651 | 0.344876 | 0.40913 |
| tossup | drop_share_2_d3 | 1220 | 0.332957 | 0.0157604 | 0.264701 | 0.303548 | 0.323855 | 0.334934 | 0.343226 | 0.354684 | 0.369332 |
| tossup | drop_share_3_d3 | 1220 | 0.351219 | 0.0232633 | 0.292426 | 0.321876 | 0.337181 | 0.348394 | 0.360322 | 0.392186 | 0.480116 |
| tossup | drop_share_1_d4 | 1220 | 0.313852 | 0.0159413 | 0.247414 | 0.288726 | 0.303879 | 0.313688 | 0.324304 | 0.340047 | 0.387813 |
| tossup | drop_share_2_d4 | 1220 | 0.334491 | 0.0145497 | 0.272091 | 0.308352 | 0.326883 | 0.335691 | 0.343999 | 0.356357 | 0.378814 |
| tossup | drop_share_3_d4 | 1220 | 0.351657 | 0.0195089 | 0.296917 | 0.325494 | 0.338313 | 0.349388 | 0.361868 | 0.387776 | 0.445776 |
| tossup | drop_share_1_d5 | 1220 | 0.315966 | 0.0183859 | 0.229806 | 0.289996 | 0.304327 | 0.31456 | 0.325862 | 0.347184 | 0.410531 |
| tossup | drop_share_2_d5 | 1220 | 0.33421 | 0.0135897 | 0.281751 | 0.311178 | 0.326066 | 0.335396 | 0.343523 | 0.354185 | 0.373925 |
| tossup | drop_share_3_d5 | 1220 | 0.349824 | 0.0189237 | 0.26232 | 0.321242 | 0.338586 | 0.349129 | 0.359459 | 0.380401 | 0.462118 |
| tossup | r_1 | 1220 | 0.239707 | 0.189862 | 0.0315231 | 0.0615601 | 0.110244 | 0.165381 | 0.308745 | 0.692676 | 0.83809 |
| tossup | r_2 | 1220 | 0.205823 | 0.119388 | 0.0309255 | 0.0557074 | 0.114978 | 0.187988 | 0.261048 | 0.448762 | 0.700778 |
| tossup | r_3 | 1220 | 0.189239 | 0.121801 | 0.0329329 | 0.0658153 | 0.115975 | 0.167147 | 0.212968 | 0.464368 | 0.82222 |
| tossup | r_4 | 1220 | 0.181818 | 0.105825 | 0.0320403 | 0.0637821 | 0.106924 | 0.170201 | 0.218618 | 0.368036 | 0.807633 |
| tossup | r_5 | 1220 | 0.183413 | 0.0947052 | 0.0361192 | 0.0595252 | 0.116086 | 0.179838 | 0.227748 | 0.345552 | 0.673078 |
| tossup | r_norm | 1220 | 0.528867 | 0.088731 | 0.447521 | 0.450809 | 0.462178 | 0.492507 | 0.564747 | 0.739209 | 0.842028 |
