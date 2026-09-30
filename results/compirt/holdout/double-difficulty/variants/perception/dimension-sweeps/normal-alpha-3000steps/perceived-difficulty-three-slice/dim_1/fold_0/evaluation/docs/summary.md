# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_1/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_1/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 300420 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.584548 |
| log_loss | 0.555323 |
| ece | 0.0592346 |
| brier | 0.182609 |
| accuracy | 0.75234 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0129102 |
| probability_std | 0.134187 |
| probability_p10 | 0.574852 |
| probability_p50 | 0.784902 |
| probability_p90 | 0.908821 |
| mean_predictive_variance | 0.16475 |
| integrated_brier_score | 0.106253 |
| joint_tossup_event_log_loss | 7.00722 |
| buzz_position_mae | 0.165263 |
| buzz_position_median_absolute_error | 0.151709 |
| buzz_position_bias | -0.0653575 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.310382 |
| first_buzzer_mean_reciprocal_rank | 0.529755 |
| first_buzzer_log_loss | 1.74427 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.625282 |
| tossup_scorer_player_top1_accuracy | 0.280998 |
| tossup_scorer_team_top1_accuracy | 0.452017 |
| tossup_game_winner_accuracy | 0.755507 |
| tossup_game_margin_mae | 38.3976 |
| tournament_player_ppg_spearman | 0.603059 |
| tournament_player_ppg_mae | 10.1489 |
| tournament_player_ppg_top10_overlap | 0.572414 |
| neg_auroc | 0.584548 |
| neg_average_precision | 0.301987 |
| neg_precision | 0.374477 |
| neg_recall | 0.0820348 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0576906 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.089322 |
| no_buzz_calibration_error | 0.0760524 |
| no_buzz_brier | 0.0237963 |
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
| tossup_correctness | aggregate | all | 9295 | 0.584548 | 0.555323 | 0.0592346 | 0.182609 | 0.75234 | 0.76525 | -0.0129102 | 0.134187 | 0.574852 | 0.784902 | 0.908821 | 0.16475 |
| tossup_correctness | tier | fall | 2933 | 0.577039 | 0.534739 | 0.0834035 | 0.174536 | 0.765769 | 0.791681 | -0.025912 | 0.143388 | 0.531373 | 0.762919 | 0.892445 | 0.175501 |
| tossup_correctness | tier | nationals | 1584 | 0.611972 | 0.604601 | 0.0744352 | 0.200785 | 0.717172 | 0.724747 | -0.00757576 | 0.140362 | 0.581585 | 0.815045 | 0.932719 | 0.150714 |
| tossup_correctness | tier | regionals | 1886 | 0.576398 | 0.577042 | 0.0648137 | 0.193639 | 0.732238 | 0.746023 | -0.0137858 | 0.129602 | 0.572268 | 0.769332 | 0.894566 | 0.1723 |
| tossup_correctness | tier | winter | 2892 | 0.595371 | 0.535044 | 0.0474241 | 0.173648 | 0.771093 | 0.773167 | -0.00207469 | 0.116664 | 0.626162 | 0.801477 | 0.915449 | 0.156611 |
| tossup_correctness | category | Current Events | 124 | 0.608394 | 0.588861 | 0.127155 | 0.199242 | 0.701613 | 0.75 | -0.0483871 | 0.161526 | 0.428708 | 0.656161 | 0.860862 | 0.200713 |
| tossup_correctness | category | Fine Arts | 1103 | 0.560706 | 0.573342 | 0.0640686 | 0.186892 | 0.75068 | 0.759746 | -0.00906618 | 0.111177 | 0.646715 | 0.823322 | 0.922079 | 0.147399 |
| tossup_correctness | category | Geography | 197 | 0.699883 | 0.574418 | 0.0789695 | 0.197643 | 0.695431 | 0.670051 | 0.0253807 | 0.147827 | 0.481307 | 0.719402 | 0.866619 | 0.188071 |
| tossup_correctness | category | History | 1491 | 0.610526 | 0.524891 | 0.0688482 | 0.171657 | 0.765929 | 0.787391 | -0.0214621 | 0.136648 | 0.534674 | 0.749377 | 0.882751 | 0.18077 |
| tossup_correctness | category | Literature | 1472 | 0.52993 | 0.527285 | 0.0772065 | 0.165051 | 0.800272 | 0.804348 | -0.00407609 | 0.101551 | 0.70152 | 0.857932 | 0.943652 | 0.126531 |
| tossup_correctness | category | Mythology | 332 | 0.613799 | 0.497647 | 0.0958784 | 0.161674 | 0.786145 | 0.813253 | -0.0271084 | 0.129713 | 0.54031 | 0.735406 | 0.87507 | 0.183649 |
| tossup_correctness | category | Other Academic | 69 | 0.558824 | 0.553592 | 0.124726 | 0.17953 | 0.797101 | 0.753623 | 0.0434783 | 0.138285 | 0.584019 | 0.770525 | 0.892553 | 0.17232 |
| tossup_correctness | category | Philosophy | 324 | 0.570359 | 0.511202 | 0.0470234 | 0.162756 | 0.790123 | 0.799383 | -0.00925926 | 0.108381 | 0.678059 | 0.835558 | 0.927665 | 0.138893 |
| tossup_correctness | category | Popular Culture | 102 | 0.468512 | 0.624663 | 0.253345 | 0.215338 | 0.656863 | 0.833333 | -0.176471 | 0.179337 | 0.392524 | 0.682804 | 0.856078 | 0.199146 |
| tossup_correctness | category | Religion | 372 | 0.630647 | 0.60052 | 0.0677956 | 0.203781 | 0.704301 | 0.709677 | -0.00537634 | 0.140626 | 0.573772 | 0.785612 | 0.919857 | 0.162909 |
| tossup_correctness | category | Science | 1487 | 0.599932 | 0.556992 | 0.0549631 | 0.18469 | 0.745797 | 0.752522 | -0.00672495 | 0.131632 | 0.548223 | 0.752467 | 0.877387 | 0.180921 |
| tossup_correctness | category | Social Science | 336 | 0.574619 | 0.629972 | 0.0725567 | 0.215076 | 0.684524 | 0.702381 | -0.0178571 | 0.122404 | 0.596386 | 0.767282 | 0.886381 | 0.173465 |
| tossup_correctness | category | Unknown | 1886 | 0.576398 | 0.577042 | 0.0648137 | 0.193639 | 0.732238 | 0.746023 | -0.0137858 | 0.129602 | 0.572268 | 0.769332 | 0.894566 | 0.1723 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.562997 | 0.629342 | 0.119573 | 0.216605 | 0.675127 | 0.736041 | -0.0609137 | 0.155018 | 0.43403 | 0.649291 | 0.81918 | 0.207013 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.541167 | 0.614343 | 0.0948063 | 0.210017 | 0.691371 | 0.735025 | -0.0436548 | 0.145183 | 0.4623 | 0.697055 | 0.848366 | 0.198069 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.577138 | 0.5507 | 0.0683456 | 0.182404 | 0.752999 | 0.769436 | -0.0164371 | 0.129027 | 0.548785 | 0.747866 | 0.873719 | 0.182706 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.614203 | 0.516569 | 0.0353431 | 0.167348 | 0.775645 | 0.78402 | -0.00837404 | 0.120561 | 0.601619 | 0.792814 | 0.901932 | 0.16321 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.592219 | 0.571597 | 0.0669105 | 0.186116 | 0.754673 | 0.756008 | -0.00133511 | 0.11822 | 0.65186 | 0.838368 | 0.935767 | 0.138999 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | -2.27128 | 0.631872 | -4.52106 | -3.37049 | -2.68533 | -2.24816 | -1.8417 | -1.27464 | -0.603093 |
| player | theta_norm | 1186 | 2.27128 | 0.631872 | 0.603093 | 1.27464 | 1.8417 | 2.24816 | 2.68533 | 3.37049 | 4.52106 |
| tossup | start_difficulty_d1 | 1240 | -2.96359 | 0.43369 | -4.21066 | -3.60498 | -3.27707 | -2.993 | -2.6777 | -2.24821 | -1.50595 |
| tossup | end_difficulty_d1 | 1240 | -3.97336 | 0.704965 | -7.27407 | -5.22745 | -4.39182 | -3.91918 | -3.47083 | -2.89171 | -2.09767 |
| tossup | total_drop_d1 | 1240 | 1.00978 | 0.435535 | 0.365931 | 0.52646 | 0.7173 | 0.919384 | 1.1749 | 1.80676 | 4.09896 |
| tossup | drop_share_1_d1 | 1240 | 0.370237 | 0.0604833 | 0.168508 | 0.270596 | 0.330097 | 0.371736 | 0.410491 | 0.467062 | 0.594975 |
| tossup | drop_share_2_d1 | 1240 | 0.332037 | 0.0255561 | 0.25344 | 0.296984 | 0.316896 | 0.329415 | 0.342712 | 0.376878 | 0.557102 |
| tossup | drop_share_3_d1 | 1240 | 0.297726 | 0.0604437 | 0.133939 | 0.208199 | 0.256638 | 0.292093 | 0.334492 | 0.407486 | 0.498991 |
| tossup | r_1 | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| tossup | r_norm | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
