# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_2/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_2/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 333069 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.553929 |
| log_loss | 0.620572 |
| ece | 0.116765 |
| brier | 0.193381 |
| accuracy | 0.764174 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.00107585 |
| probability_std | 0.083096 |
| probability_p10 | 0.772515 |
| probability_p50 | 0.901224 |
| probability_p90 | 0.955759 |
| mean_predictive_variance | 0.0994755 |
| integrated_brier_score | 0.172352 |
| joint_tossup_event_log_loss | 7.80613 |
| buzz_position_mae | 0.338135 |
| buzz_position_median_absolute_error | 0.341464 |
| buzz_position_bias | -0.325195 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.329424 |
| first_buzzer_mean_reciprocal_rank | 0.550561 |
| first_buzzer_log_loss | 1.691 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.615492 |
| tossup_scorer_player_top1_accuracy | 0.264119 |
| tossup_scorer_team_top1_accuracy | 0.401486 |
| tossup_game_winner_accuracy | 0.742291 |
| tossup_game_margin_mae | 42.2208 |
| tournament_player_ppg_spearman | 0.615632 |
| tournament_player_ppg_mae | 9.84308 |
| tournament_player_ppg_top10_overlap | 0.610345 |
| neg_auroc | 0.553929 |
| neg_average_precision | 0.276963 |
| neg_precision | 0.291667 |
| neg_recall | 0.00320807 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0286675 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.238267 |
| no_buzz_calibration_error | 0.224998 |
| no_buzz_brier | 0.0733907 |
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
| tossup_correctness | aggregate | all | 9295 | 0.553929 | 0.620572 | 0.116765 | 0.193381 | 0.764174 | 0.76525 | -0.00107585 | 0.083096 | 0.772515 | 0.901224 | 0.955759 | 0.0994755 |
| tossup_correctness | tier | fall | 2933 | 0.578978 | 0.542473 | 0.0833377 | 0.169923 | 0.792022 | 0.791681 | 0.000340948 | 0.0754879 | 0.773643 | 0.892082 | 0.945736 | 0.105227 |
| tossup_correctness | tier | nationals | 1584 | 0.566973 | 0.700887 | 0.147933 | 0.220415 | 0.72096 | 0.724747 | -0.00378788 | 0.107696 | 0.704047 | 0.901562 | 0.96334 | 0.104771 |
| tossup_correctness | tier | regionals | 1886 | 0.517986 | 0.677855 | 0.140827 | 0.211772 | 0.743372 | 0.746023 | -0.00265111 | 0.0916236 | 0.76079 | 0.896982 | 0.958999 | 0.102988 |
| tossup_correctness | tier | winter | 2892 | 0.554276 | 0.618432 | 0.124584 | 0.19037 | 0.773167 | 0.773167 | 0 | 0.0640628 | 0.819659 | 0.91055 | 0.957491 | 0.088452 |
| tossup_correctness | category | Current Events | 124 | 0.502948 | 0.638153 | 0.111454 | 0.200563 | 0.758065 | 0.75 | 0.00806452 | 0.0915147 | 0.734312 | 0.873944 | 0.936868 | 0.119319 |
| tossup_correctness | category | Fine Arts | 1103 | 0.519242 | 0.664884 | 0.136321 | 0.202847 | 0.759746 | 0.759746 | 0 | 0.0761885 | 0.783553 | 0.91219 | 0.961211 | 0.0918029 |
| tossup_correctness | category | Geography | 197 | 0.667949 | 0.765693 | 0.218228 | 0.256142 | 0.664975 | 0.670051 | -0.00507614 | 0.0743063 | 0.790479 | 0.898175 | 0.95367 | 0.0976812 |
| tossup_correctness | category | History | 1491 | 0.569555 | 0.560819 | 0.09284 | 0.175223 | 0.785379 | 0.787391 | -0.00201207 | 0.0861721 | 0.759734 | 0.895255 | 0.94876 | 0.104733 |
| tossup_correctness | category | Literature | 1472 | 0.528517 | 0.555438 | 0.0916778 | 0.166867 | 0.803668 | 0.804348 | -0.000679348 | 0.0772052 | 0.785018 | 0.911593 | 0.961769 | 0.0914319 |
| tossup_correctness | category | Mythology | 332 | 0.625448 | 0.504336 | 0.100277 | 0.15661 | 0.816265 | 0.813253 | 0.00301205 | 0.073562 | 0.803727 | 0.906806 | 0.955552 | 0.0921981 |
| tossup_correctness | category | Other Academic | 69 | 0.419683 | 0.673244 | 0.193822 | 0.202916 | 0.753623 | 0.753623 | 0 | 0.0763217 | 0.812969 | 0.911787 | 0.951377 | 0.0960008 |
| tossup_correctness | category | Philosophy | 324 | 0.590971 | 0.534127 | 0.0936339 | 0.16469 | 0.799383 | 0.799383 | 0 | 0.0742657 | 0.795265 | 0.904785 | 0.957528 | 0.0940691 |
| tossup_correctness | category | Popular Culture | 102 | 0.393772 | 0.52365 | 0.108747 | 0.15321 | 0.833333 | 0.833333 | 0 | 0.0655115 | 0.789 | 0.896364 | 0.950591 | 0.0995059 |
| tossup_correctness | category | Religion | 372 | 0.643764 | 0.691221 | 0.169955 | 0.22545 | 0.704301 | 0.709677 | -0.00537634 | 0.0925211 | 0.746252 | 0.900791 | 0.953561 | 0.102356 |
| tossup_correctness | category | Science | 1487 | 0.588768 | 0.618205 | 0.121599 | 0.19612 | 0.753194 | 0.752522 | 0.000672495 | 0.079992 | 0.770508 | 0.893298 | 0.948315 | 0.104617 |
| tossup_correctness | category | Social Science | 336 | 0.546102 | 0.761577 | 0.188528 | 0.242963 | 0.699405 | 0.702381 | -0.00297619 | 0.0786835 | 0.781658 | 0.903876 | 0.954963 | 0.0977521 |
| tossup_correctness | category | Unknown | 1886 | 0.517986 | 0.677855 | 0.140827 | 0.211772 | 0.743372 | 0.746023 | -0.00265111 | 0.0916236 | 0.76079 | 0.896982 | 0.958999 | 0.102988 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.536605 | 0.637532 | 0.117009 | 0.20804 | 0.736041 | 0.736041 | 0 | 0.0984551 | 0.723643 | 0.8523 | 0.930526 | 0.129345 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.522047 | 0.662447 | 0.124757 | 0.211056 | 0.73401 | 0.735025 | -0.00101523 | 0.0850727 | 0.750664 | 0.879478 | 0.938982 | 0.114299 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.585664 | 0.586352 | 0.105244 | 0.18615 | 0.767659 | 0.769436 | -0.00177699 | 0.0816555 | 0.771377 | 0.892644 | 0.947217 | 0.104899 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.558909 | 0.580356 | 0.106321 | 0.180135 | 0.782624 | 0.78402 | -0.00139567 | 0.0799934 | 0.777076 | 0.900998 | 0.953898 | 0.0991046 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.541669 | 0.669872 | 0.140353 | 0.20471 | 0.755674 | 0.756008 | -0.000333778 | 0.0822698 | 0.785116 | 0.918138 | 0.964181 | 0.0889173 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1186 | -1.48654 | 0.594961 | -2.76941 | -2.30124 | -1.84737 | -1.54495 | -1.2238 | -0.496945 | 2.13626 |
| player | beta | 1186 | -2.94699 | 1.02424 | -6.75052 | -5.08319 | -3.44723 | -2.71654 | -2.22365 | -1.71025 | -1.39268 |
| player | theta_1 | 1186 | 0.915616 | 0.8349 | -2.32901 | -0.59412 | 0.424754 | 0.977707 | 1.49413 | 2.17956 | 3.15006 |
| player | theta_2 | 1186 | 0.939518 | 0.863051 | -2.19075 | -0.507675 | 0.410726 | 0.961846 | 1.5622 | 2.22018 | 3.56343 |
| player | theta_norm | 1186 | 1.64858 | 0.666573 | 0.101937 | 0.542113 | 1.13615 | 1.68225 | 2.15986 | 2.65843 | 3.59606 |
| tossup | start_difficulty_d1 | 1240 | -1.19342 | 0.481683 | -2.21277 | -1.93369 | -1.58632 | -1.21534 | -0.824912 | -0.401084 | -0.0916335 |
| tossup | start_difficulty_d2 | 1240 | -1.16346 | 0.431627 | -2.1375 | -1.7863 | -1.51544 | -1.23752 | -0.803752 | -0.424292 | -0.193884 |
| tossup | end_difficulty_d1 | 1240 | -1.75124 | 0.416737 | -3.07389 | -2.48161 | -2.06612 | -1.70663 | -1.43504 | -1.12482 | -0.891511 |
| tossup | end_difficulty_d2 | 1240 | -1.73253 | 0.383681 | -3.01447 | -2.38635 | -2.00072 | -1.71644 | -1.42508 | -1.15405 | -0.987821 |
| tossup | total_drop_d1 | 1240 | 0.557818 | 0.191054 | 0.196939 | 0.269777 | 0.397487 | 0.546263 | 0.714974 | 0.864092 | 1.09362 |
| tossup | total_drop_d2 | 1240 | 0.569069 | 0.181563 | 0.212885 | 0.286305 | 0.41956 | 0.564374 | 0.722433 | 0.848321 | 1.11233 |
| tossup | drop_share_1_d1 | 1240 | 0.331233 | 0.0353414 | 0.179226 | 0.277234 | 0.310318 | 0.328971 | 0.352608 | 0.390297 | 0.469735 |
| tossup | drop_share_2_d1 | 1240 | 0.313787 | 0.0197107 | 0.24305 | 0.27833 | 0.301247 | 0.316178 | 0.328357 | 0.342468 | 0.374352 |
| tossup | drop_share_3_d1 | 1240 | 0.35498 | 0.0403383 | 0.237064 | 0.29741 | 0.32939 | 0.350513 | 0.373062 | 0.433287 | 0.548801 |
| tossup | drop_share_1_d2 | 1240 | 0.326624 | 0.0326887 | 0.180362 | 0.266944 | 0.310846 | 0.326742 | 0.346549 | 0.376835 | 0.445221 |
| tossup | drop_share_2_d2 | 1240 | 0.313915 | 0.0206214 | 0.246432 | 0.275885 | 0.300576 | 0.316759 | 0.329294 | 0.34323 | 0.355493 |
| tossup | drop_share_3_d2 | 1240 | 0.359461 | 0.041712 | 0.256595 | 0.30816 | 0.33303 | 0.351127 | 0.376758 | 0.445931 | 0.548262 |
| tossup | r_1 | 1240 | 0.510117 | 0.285745 | 0.037238 | 0.0848768 | 0.241186 | 0.51936 | 0.773864 | 0.921992 | 0.96914 |
| tossup | r_2 | 1240 | 0.489883 | 0.285745 | 0.0308599 | 0.0780075 | 0.226136 | 0.48064 | 0.758814 | 0.915123 | 0.962762 |
| tossup | r_norm | 1240 | 0.810698 | 0.0784022 | 0.707107 | 0.708223 | 0.73468 | 0.802062 | 0.879941 | 0.938937 | 0.969631 |
