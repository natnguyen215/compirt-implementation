# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_2/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_2/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 334244 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.562686 |
| log_loss | 0.621626 |
| ece | 0.120017 |
| brier | 0.194425 |
| accuracy | 0.761795 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.000329924 |
| probability_std | 0.0858528 |
| probability_p10 | 0.769594 |
| probability_p50 | 0.900706 |
| probability_p90 | 0.955427 |
| mean_predictive_variance | 0.100523 |
| integrated_brier_score | 0.175309 |
| joint_tossup_event_log_loss | 7.80779 |
| buzz_position_mae | 0.34585 |
| buzz_position_median_absolute_error | 0.353516 |
| buzz_position_bias | -0.334303 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.334213 |
| first_buzzer_mean_reciprocal_rank | 0.551504 |
| first_buzzer_log_loss | 1.69985 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.619597 |
| tossup_scorer_player_top1_accuracy | 0.265368 |
| tossup_scorer_team_top1_accuracy | 0.410931 |
| tossup_game_winner_accuracy | 0.745495 |
| tossup_game_margin_mae | 41.2662 |
| tournament_player_ppg_spearman | 0.609368 |
| tournament_player_ppg_mae | 10.0515 |
| tournament_player_ppg_top10_overlap | 0.593103 |
| neg_auroc | 0.562686 |
| neg_average_precision | 0.287662 |
| neg_precision | 0.44 |
| neg_recall | 0.00508553 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0285451 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.233759 |
| no_buzz_calibration_error | 0.217849 |
| no_buzz_brier | 0.071348 |
| full_pmf_max_mass_error | 1.44329e-15 |
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
| tossup_correctness | aggregate | all | 9093 | 0.562686 | 0.621626 | 0.120017 | 0.194425 | 0.761795 | 0.762125 | -0.000329924 | 0.0858528 | 0.769594 | 0.900706 | 0.955427 | 0.100523 |
| tossup_correctness | tier | fall | 2842 | 0.579977 | 0.557805 | 0.0933387 | 0.175464 | 0.784659 | 0.785362 | -0.00070373 | 0.0800374 | 0.776491 | 0.895857 | 0.947488 | 0.10436 |
| tossup_correctness | tier | nationals | 1564 | 0.576622 | 0.694793 | 0.146336 | 0.222592 | 0.719309 | 0.718031 | 0.00127877 | 0.102033 | 0.711419 | 0.891963 | 0.961403 | 0.107886 |
| tossup_correctness | tier | regionals | 1937 | 0.53803 | 0.644448 | 0.127935 | 0.199004 | 0.756324 | 0.758389 | -0.00206505 | 0.0943448 | 0.756314 | 0.901209 | 0.957872 | 0.101153 |
| tossup_correctness | tier | winter | 2750 | 0.555293 | 0.629896 | 0.127899 | 0.194776 | 0.766182 | 0.765818 | 0.000363636 | 0.072333 | 0.799552 | 0.908817 | 0.957799 | 0.0919275 |
| tossup_correctness | category | Current Events | 126 | 0.495912 | 0.619252 | 0.138056 | 0.196908 | 0.761905 | 0.769841 | -0.00793651 | 0.094436 | 0.755151 | 0.888504 | 0.942576 | 0.110847 |
| tossup_correctness | category | Fine Arts | 1071 | 0.568831 | 0.619645 | 0.125305 | 0.193244 | 0.76564 | 0.766573 | -0.000933707 | 0.0769814 | 0.797574 | 0.906354 | 0.956799 | 0.0946962 |
| tossup_correctness | category | Geography | 185 | 0.61448 | 0.71824 | 0.182687 | 0.235946 | 0.702703 | 0.697297 | 0.00540541 | 0.0850494 | 0.780027 | 0.901169 | 0.951777 | 0.10062 |
| tossup_correctness | category | History | 1440 | 0.55002 | 0.639079 | 0.129699 | 0.201925 | 0.754167 | 0.754167 | 0 | 0.0882658 | 0.753821 | 0.900639 | 0.952518 | 0.10287 |
| tossup_correctness | category | Literature | 1422 | 0.546099 | 0.525897 | 0.0819573 | 0.157516 | 0.814346 | 0.814346 | 0 | 0.0780918 | 0.786068 | 0.902863 | 0.959768 | 0.0964132 |
| tossup_correctness | category | Mythology | 318 | 0.620444 | 0.54073 | 0.0964029 | 0.169031 | 0.795597 | 0.789308 | 0.00628931 | 0.0817198 | 0.793576 | 0.904065 | 0.94885 | 0.0980146 |
| tossup_correctness | category | Other Academic | 66 | 0.539754 | 0.751094 | 0.176794 | 0.236063 | 0.712121 | 0.712121 | 0 | 0.0861611 | 0.745876 | 0.907239 | 0.966774 | 0.0990722 |
| tossup_correctness | category | Philosophy | 311 | 0.605031 | 0.648767 | 0.146162 | 0.203963 | 0.742765 | 0.745981 | -0.00321543 | 0.0809085 | 0.784481 | 0.911162 | 0.961164 | 0.0922601 |
| tossup_correctness | category | Popular Culture | 102 | 0.572222 | 0.380118 | 0.0213827 | 0.109358 | 0.872549 | 0.882353 | -0.00980392 | 0.0834271 | 0.791236 | 0.893124 | 0.949914 | 0.103024 |
| tossup_correctness | category | Religion | 358 | 0.597982 | 0.712176 | 0.175917 | 0.23196 | 0.712291 | 0.712291 | 0 | 0.0896996 | 0.759791 | 0.904087 | 0.953216 | 0.100722 |
| tossup_correctness | category | Science | 1433 | 0.571749 | 0.651556 | 0.132561 | 0.207581 | 0.739707 | 0.738311 | 0.00139567 | 0.0859753 | 0.758748 | 0.890046 | 0.952089 | 0.106884 |
| tossup_correctness | category | Social Science | 324 | 0.611911 | 0.650652 | 0.14688 | 0.209345 | 0.731481 | 0.731481 | 0 | 0.0756833 | 0.780528 | 0.900734 | 0.947832 | 0.101115 |
| tossup_correctness | category | Unknown | 1937 | 0.53803 | 0.644448 | 0.127935 | 0.199004 | 0.756324 | 0.758389 | -0.00206505 | 0.0943448 | 0.756314 | 0.901209 | 0.957872 | 0.101153 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.482143 | 0.714702 | 0.151335 | 0.231234 | 0.706587 | 0.712575 | -0.00598802 | 0.0863468 | 0.742377 | 0.869621 | 0.940938 | 0.122228 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.575979 | 0.651522 | 0.134075 | 0.212498 | 0.726974 | 0.729167 | -0.00219298 | 0.0913666 | 0.737884 | 0.874718 | 0.939649 | 0.119261 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.556568 | 0.622403 | 0.114882 | 0.19825 | 0.754137 | 0.755083 | -0.000945626 | 0.0862553 | 0.763393 | 0.891422 | 0.947554 | 0.107882 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.558482 | 0.583008 | 0.104639 | 0.181082 | 0.781294 | 0.780942 | 0.000351617 | 0.0824596 | 0.779755 | 0.902024 | 0.952877 | 0.0992312 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.563663 | 0.643027 | 0.13264 | 0.196791 | 0.762357 | 0.762029 | 0.000327332 | 0.0837134 | 0.789359 | 0.914615 | 0.964115 | 0.0898519 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1167 | -1.48915 | 0.571323 | -2.78155 | -2.27623 | -1.81972 | -1.55166 | -1.21417 | -0.520128 | 1.80072 |
| player | beta | 1167 | -2.93473 | 1.01262 | -6.6542 | -5.07255 | -3.45059 | -2.70646 | -2.19121 | -1.68209 | -1.40835 |
| player | theta_1 | 1167 | 0.940322 | 0.882839 | -2.40411 | -0.55867 | 0.422096 | 0.980966 | 1.54541 | 2.27205 | 3.30462 |
| player | theta_2 | 1167 | 0.931463 | 0.8565 | -1.99223 | -0.532242 | 0.35804 | 0.991948 | 1.5424 | 2.20699 | 3.6363 |
| player | theta_norm | 1167 | 1.67596 | 0.6746 | 0.0592832 | 0.542059 | 1.14984 | 1.69926 | 2.21214 | 2.681 | 3.64574 |
| tossup | start_difficulty_d1 | 1220 | -1.21878 | 0.503646 | -2.23322 | -1.95541 | -1.6338 | -1.2653 | -0.807398 | -0.36019 | -0.185099 |
| tossup | start_difficulty_d2 | 1220 | -1.13567 | 0.423725 | -2.33386 | -1.78231 | -1.46999 | -1.17671 | -0.805116 | -0.416621 | -0.146002 |
| tossup | end_difficulty_d1 | 1220 | -1.75659 | 0.433144 | -2.98328 | -2.48967 | -2.09431 | -1.73394 | -1.4039 | -1.10522 | -0.918866 |
| tossup | end_difficulty_d2 | 1220 | -1.69989 | 0.358839 | -3.0465 | -2.32062 | -1.95773 | -1.65898 | -1.42114 | -1.16601 | -0.978365 |
| tossup | total_drop_d1 | 1220 | 0.537812 | 0.183306 | 0.204915 | 0.262471 | 0.376616 | 0.535531 | 0.692351 | 0.827307 | 0.969162 |
| tossup | total_drop_d2 | 1220 | 0.56422 | 0.17623 | 0.210175 | 0.287692 | 0.423997 | 0.556989 | 0.705837 | 0.849934 | 0.999758 |
| tossup | drop_share_1_d1 | 1220 | 0.332098 | 0.0362324 | 0.175015 | 0.275943 | 0.310584 | 0.330814 | 0.354628 | 0.392283 | 0.471969 |
| tossup | drop_share_2_d1 | 1220 | 0.312126 | 0.019726 | 0.239758 | 0.277173 | 0.29891 | 0.314969 | 0.325854 | 0.340936 | 0.373096 |
| tossup | drop_share_3_d1 | 1220 | 0.355775 | 0.0413634 | 0.231929 | 0.29546 | 0.329368 | 0.351645 | 0.374599 | 0.436347 | 0.555096 |
| tossup | drop_share_1_d2 | 1220 | 0.326929 | 0.0330896 | 0.189406 | 0.2664 | 0.310495 | 0.327188 | 0.346509 | 0.378715 | 0.45256 |
| tossup | drop_share_2_d2 | 1220 | 0.313673 | 0.0201894 | 0.24477 | 0.275862 | 0.30027 | 0.315897 | 0.329176 | 0.343023 | 0.354689 |
| tossup | drop_share_3_d2 | 1220 | 0.359397 | 0.041915 | 0.253688 | 0.305798 | 0.332536 | 0.351375 | 0.377528 | 0.442963 | 0.53204 |
| tossup | r_1 | 1220 | 0.533247 | 0.284821 | 0.0293536 | 0.0683161 | 0.277771 | 0.551038 | 0.800984 | 0.928625 | 0.968434 |
| tossup | r_2 | 1220 | 0.466753 | 0.284821 | 0.0315659 | 0.0713749 | 0.199016 | 0.448962 | 0.722229 | 0.931684 | 0.970646 |
| tossup | r_norm | 1220 | 0.810892 | 0.0823586 | 0.707111 | 0.70811 | 0.729947 | 0.80211 | 0.884144 | 0.946515 | 0.97109 |
