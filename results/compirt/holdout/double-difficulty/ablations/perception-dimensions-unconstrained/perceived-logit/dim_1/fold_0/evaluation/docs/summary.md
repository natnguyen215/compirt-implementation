# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_1/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_1/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 330753 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.574321 |
| log_loss | 0.61936 |
| ece | 0.125048 |
| brier | 0.193529 |
| accuracy | 0.763852 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0013986 |
| probability_std | 0.075534 |
| probability_p10 | 0.797226 |
| probability_p50 | 0.903393 |
| probability_p90 | 0.958832 |
| mean_predictive_variance | 0.0949859 |
| integrated_brier_score | 0.170106 |
| joint_tossup_event_log_loss | 7.83156 |
| buzz_position_mae | 0.335345 |
| buzz_position_median_absolute_error | 0.337971 |
| buzz_position_bias | -0.32226 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.304465 |
| first_buzzer_mean_reciprocal_rank | 0.524606 |
| first_buzzer_log_loss | 1.74684 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.618612 |
| tossup_scorer_player_top1_accuracy | 0.25966 |
| tossup_scorer_team_top1_accuracy | 0.414968 |
| tossup_game_winner_accuracy | 0.746696 |
| tossup_game_margin_mae | 41.3866 |
| tournament_player_ppg_spearman | 0.621557 |
| tournament_player_ppg_mae | 9.74701 |
| tournament_player_ppg_top10_overlap | 0.606897 |
| neg_auroc | 0.574321 |
| neg_average_precision | 0.285217 |
| neg_precision | 0.24 |
| neg_recall | 0.00274977 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0293395 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.232472 |
| no_buzz_calibration_error | 0.219202 |
| no_buzz_brier | 0.0697304 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| tossup_correctness | aggregate | all | 9295 | 0.574321 | 0.61936 | 0.125048 | 0.193529 | 0.763852 | 0.76525 | -0.0013986 | 0.075534 | 0.797226 | 0.903393 | 0.958832 | 0.0949859 |
| tossup_correctness | tier | fall | 2933 | 0.599334 | 0.542249 | 0.0894719 | 0.169645 | 0.791681 | 0.791681 | 0 | 0.0713306 | 0.789503 | 0.891871 | 0.954908 | 0.10086 |
| tossup_correctness | tier | nationals | 1584 | 0.576735 | 0.714327 | 0.166781 | 0.225554 | 0.720328 | 0.724747 | -0.00441919 | 0.0961295 | 0.75576 | 0.91147 | 0.963714 | 0.0956568 |
| tossup_correctness | tier | regionals | 1886 | 0.544804 | 0.671018 | 0.14336 | 0.210772 | 0.742842 | 0.746023 | -0.00318134 | 0.0824636 | 0.78901 | 0.899901 | 0.956972 | 0.0978655 |
| tossup_correctness | tier | winter | 2892 | 0.576662 | 0.611861 | 0.126576 | 0.188966 | 0.773167 | 0.773167 | 0 | 0.0584927 | 0.827079 | 0.909513 | 0.961516 | 0.0867837 |
| tossup_correctness | category | Current Events | 124 | 0.52931 | 0.644238 | 0.124626 | 0.20165 | 0.75 | 0.75 | 0 | 0.097027 | 0.72068 | 0.88407 | 0.949441 | 0.112492 |
| tossup_correctness | category | Fine Arts | 1103 | 0.5188 | 0.671309 | 0.143824 | 0.204666 | 0.759746 | 0.759746 | 0 | 0.0691937 | 0.812456 | 0.913029 | 0.963218 | 0.0881879 |
| tossup_correctness | category | Geography | 197 | 0.678788 | 0.76725 | 0.221441 | 0.25651 | 0.664975 | 0.670051 | -0.00507614 | 0.0755139 | 0.793636 | 0.89978 | 0.963577 | 0.0956101 |
| tossup_correctness | category | History | 1491 | 0.592512 | 0.560122 | 0.101847 | 0.175665 | 0.783367 | 0.787391 | -0.00402414 | 0.0769201 | 0.79178 | 0.896399 | 0.953717 | 0.0993176 |
| tossup_correctness | category | Literature | 1472 | 0.569978 | 0.555889 | 0.103722 | 0.167083 | 0.803668 | 0.804348 | -0.000679348 | 0.070182 | 0.826436 | 0.919298 | 0.96582 | 0.0823774 |
| tossup_correctness | category | Mythology | 332 | 0.617682 | 0.501053 | 0.100623 | 0.155 | 0.816265 | 0.813253 | 0.00301205 | 0.0697824 | 0.807257 | 0.903021 | 0.956008 | 0.0931877 |
| tossup_correctness | category | Other Academic | 69 | 0.449095 | 0.664285 | 0.208859 | 0.19937 | 0.753623 | 0.753623 | 0 | 0.0720515 | 0.810808 | 0.903239 | 0.958312 | 0.0936061 |
| tossup_correctness | category | Philosophy | 324 | 0.589902 | 0.535577 | 0.0900768 | 0.165523 | 0.799383 | 0.799383 | 0 | 0.0712375 | 0.806772 | 0.900719 | 0.958593 | 0.0944561 |
| tossup_correctness | category | Popular Culture | 102 | 0.451211 | 0.503654 | 0.10196 | 0.150718 | 0.833333 | 0.833333 | 0 | 0.0658322 | 0.804587 | 0.896548 | 0.953476 | 0.0974167 |
| tossup_correctness | category | Religion | 372 | 0.652953 | 0.682647 | 0.170749 | 0.224428 | 0.709677 | 0.709677 | 0 | 0.0826 | 0.776385 | 0.89754 | 0.954297 | 0.100799 |
| tossup_correctness | category | Science | 1487 | 0.601578 | 0.617989 | 0.12805 | 0.196824 | 0.753194 | 0.752522 | 0.000672495 | 0.0704999 | 0.790515 | 0.892287 | 0.952449 | 0.101506 |
| tossup_correctness | category | Social Science | 336 | 0.541864 | 0.763499 | 0.185819 | 0.243471 | 0.699405 | 0.702381 | -0.00297619 | 0.0714823 | 0.804145 | 0.897019 | 0.956345 | 0.0968709 |
| tossup_correctness | category | Unknown | 1886 | 0.544804 | 0.671018 | 0.14336 | 0.210772 | 0.742842 | 0.746023 | -0.00318134 | 0.0824636 | 0.78901 | 0.899901 | 0.956972 | 0.0978655 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.580637 | 0.638489 | 0.132017 | 0.206397 | 0.741117 | 0.736041 | 0.00507614 | 0.0921724 | 0.749429 | 0.863113 | 0.944856 | 0.120282 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.566034 | 0.656164 | 0.135278 | 0.210707 | 0.735025 | 0.735025 | 0 | 0.0779796 | 0.781301 | 0.887416 | 0.946788 | 0.107028 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.599428 | 0.589347 | 0.113678 | 0.18681 | 0.767215 | 0.769436 | -0.00222124 | 0.0742302 | 0.795158 | 0.894373 | 0.952443 | 0.099817 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.585231 | 0.576587 | 0.110654 | 0.179634 | 0.781577 | 0.78402 | -0.00244243 | 0.0737924 | 0.805698 | 0.902871 | 0.958043 | 0.094548 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.553255 | 0.669469 | 0.146348 | 0.205376 | 0.75534 | 0.756008 | -0.000667557 | 0.0738014 | 0.810324 | 0.916586 | 0.965256 | 0.0861526 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1186 | -1.57962 | 0.518379 | -2.67255 | -2.27744 | -1.88726 | -1.63001 | -1.37999 | -0.774047 | 2.49736 |
| player | beta | 1186 | -2.63627 | 0.965426 | -6.58562 | -4.53995 | -3.08333 | -2.43464 | -1.98054 | -1.47128 | -1.13613 |
| player | theta_1 | 1186 | 0.900986 | 0.749853 | -2.15972 | -0.30812 | 0.407093 | 0.879427 | 1.42449 | 2.17997 | 2.48075 |
| player | theta_norm | 1186 | 0.993348 | 0.622228 | 0.00216158 | 0.106554 | 0.487865 | 0.914252 | 1.43401 | 2.17997 | 2.48075 |
| tossup | start_difficulty_d1 | 1240 | -1.54345 | 0.269419 | -2.32774 | -1.95383 | -1.73687 | -1.56302 | -1.37727 | -1.06824 | -0.672769 |
| tossup | end_difficulty_d1 | 1240 | -1.90319 | 0.336094 | -3.0082 | -2.47264 | -2.12869 | -1.90492 | -1.67052 | -1.34778 | -1.0572 |
| tossup | total_drop_d1 | 1240 | 0.359735 | 0.115646 | 0.168946 | 0.216701 | 0.26033 | 0.343673 | 0.435535 | 0.563631 | 1.00171 |
| tossup | drop_share_1_d1 | 1240 | 0.340053 | 0.0505321 | 0.172706 | 0.249377 | 0.309986 | 0.344165 | 0.374933 | 0.413332 | 0.491113 |
| tossup | drop_share_2_d1 | 1240 | 0.293552 | 0.0207697 | 0.222274 | 0.256413 | 0.280139 | 0.295692 | 0.308117 | 0.324743 | 0.35543 |
| tossup | drop_share_3_d1 | 1240 | 0.366395 | 0.0611053 | 0.229909 | 0.285384 | 0.320899 | 0.357326 | 0.4004 | 0.486599 | 0.563961 |
| tossup | r_1 | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| tossup | r_norm | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
