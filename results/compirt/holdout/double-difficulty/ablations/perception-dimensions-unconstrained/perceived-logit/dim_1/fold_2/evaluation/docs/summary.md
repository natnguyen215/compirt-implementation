# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_1/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_1/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 331063 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.565387 |
| log_loss | 0.622771 |
| ece | 0.124362 |
| brier | 0.194707 |
| accuracy | 0.762774 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00140434 |
| probability_std | 0.0817838 |
| probability_p10 | 0.78345 |
| probability_p50 | 0.903835 |
| probability_p90 | 0.957599 |
| mean_predictive_variance | 0.0973161 |
| integrated_brier_score | 0.172705 |
| joint_tossup_event_log_loss | 7.8371 |
| buzz_position_mae | 0.338312 |
| buzz_position_median_absolute_error | 0.340765 |
| buzz_position_bias | -0.32511 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.306579 |
| first_buzzer_mean_reciprocal_rank | 0.526899 |
| first_buzzer_log_loss | 1.74464 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.63876 |
| tossup_scorer_player_top1_accuracy | 0.258849 |
| tossup_scorer_team_top1_accuracy | 0.427292 |
| tossup_game_winner_accuracy | 0.756522 |
| tossup_game_margin_mae | 44.3261 |
| tournament_player_ppg_spearman | 0.64405 |
| tournament_player_ppg_mae | 9.83468 |
| tournament_player_ppg_top10_overlap | 0.596552 |
| neg_auroc | 0.565387 |
| neg_average_precision | 0.277587 |
| neg_precision | 0.217391 |
| neg_recall | 0.00229043 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0294768 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.228434 |
| no_buzz_calibration_error | 0.215321 |
| no_buzz_brier | 0.0669599 |
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
| tossup_correctness | aggregate | all | 9257 | 0.565387 | 0.622771 | 0.124362 | 0.194707 | 0.762774 | 0.764178 | -0.00140434 | 0.0817838 | 0.78345 | 0.903835 | 0.957599 | 0.0973161 |
| tossup_correctness | tier | fall | 2798 | 0.579633 | 0.563012 | 0.101907 | 0.176389 | 0.785204 | 0.785204 | 0 | 0.0690499 | 0.790253 | 0.894211 | 0.953172 | 0.10087 |
| tossup_correctness | tier | nationals | 1545 | 0.57033 | 0.712922 | 0.159076 | 0.226117 | 0.72233 | 0.721036 | 0.0012945 | 0.0927631 | 0.768692 | 0.907339 | 0.961184 | 0.0984031 |
| tossup_correctness | tier | regionals | 2039 | 0.553549 | 0.634661 | 0.126805 | 0.197486 | 0.754782 | 0.762138 | -0.00735655 | 0.101054 | 0.739274 | 0.906589 | 0.960896 | 0.0995855 |
| tossup_correctness | tier | winter | 2875 | 0.565639 | 0.624051 | 0.12908 | 0.193684 | 0.768348 | 0.768348 | 0 | 0.0698702 | 0.800213 | 0.909351 | 0.958793 | 0.0916636 |
| tossup_correctness | category | Current Events | 129 | 0.568145 | 0.79547 | 0.207033 | 0.261681 | 0.674419 | 0.666667 | 0.00775194 | 0.0877422 | 0.78509 | 0.895859 | 0.942969 | 0.106497 |
| tossup_correctness | category | Fine Arts | 1074 | 0.566662 | 0.602567 | 0.118383 | 0.185991 | 0.776536 | 0.776536 | 0 | 0.0717684 | 0.803693 | 0.909231 | 0.96175 | 0.0918371 |
| tossup_correctness | category | Geography | 180 | 0.578535 | 0.911074 | 0.259072 | 0.301662 | 0.616667 | 0.616667 | 0 | 0.0805499 | 0.765063 | 0.895568 | 0.952757 | 0.102718 |
| tossup_correctness | category | History | 1454 | 0.564967 | 0.630118 | 0.133992 | 0.200037 | 0.758597 | 0.757909 | 0.000687758 | 0.0791556 | 0.780158 | 0.8991 | 0.951968 | 0.100228 |
| tossup_correctness | category | Literature | 1435 | 0.546561 | 0.547597 | 0.0967535 | 0.163558 | 0.810453 | 0.810453 | 0 | 0.0703465 | 0.814125 | 0.917894 | 0.965079 | 0.0849712 |
| tossup_correctness | category | Mythology | 324 | 0.581567 | 0.542264 | 0.103059 | 0.169111 | 0.79321 | 0.79321 | 0 | 0.0833931 | 0.775718 | 0.902021 | 0.95182 | 0.100886 |
| tossup_correctness | category | Other Academic | 71 | 0.432462 | 0.716872 | 0.186527 | 0.214577 | 0.760563 | 0.760563 | 0 | 0.0710967 | 0.802301 | 0.909507 | 0.95667 | 0.0908795 |
| tossup_correctness | category | Philosophy | 310 | 0.507043 | 0.660487 | 0.13845 | 0.202859 | 0.76129 | 0.76129 | 0 | 0.0733485 | 0.81849 | 0.906123 | 0.957233 | 0.0925381 |
| tossup_correctness | category | Popular Culture | 108 | 0.617188 | 0.342973 | 0.0652725 | 0.0973943 | 0.888889 | 0.888889 | 0 | 0.0646589 | 0.798271 | 0.901952 | 0.956501 | 0.0949543 |
| tossup_correctness | category | Religion | 361 | 0.562269 | 0.657325 | 0.139984 | 0.206429 | 0.742382 | 0.742382 | 0 | 0.0743626 | 0.786927 | 0.902802 | 0.95386 | 0.0982664 |
| tossup_correctness | category | Science | 1445 | 0.571681 | 0.637659 | 0.129458 | 0.203772 | 0.746021 | 0.746021 | 0 | 0.0724695 | 0.778755 | 0.890395 | 0.947301 | 0.105586 |
| tossup_correctness | category | Social Science | 327 | 0.604302 | 0.697438 | 0.168923 | 0.226163 | 0.718654 | 0.718654 | 0 | 0.0779623 | 0.784888 | 0.894194 | 0.950401 | 0.10137 |
| tossup_correctness | category | Unknown | 2039 | 0.553549 | 0.634661 | 0.126805 | 0.197486 | 0.754782 | 0.762138 | -0.00735655 | 0.101054 | 0.739274 | 0.906589 | 0.960896 | 0.0995855 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.517522 | 0.656485 | 0.137271 | 0.209995 | 0.743169 | 0.743169 | 0 | 0.0761141 | 0.776142 | 0.877115 | 0.941729 | 0.110753 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.580465 | 0.662671 | 0.14189 | 0.216056 | 0.726702 | 0.728796 | -0.00209424 | 0.0760612 | 0.777077 | 0.885931 | 0.94137 | 0.108556 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.564458 | 0.635348 | 0.130503 | 0.201348 | 0.751228 | 0.752568 | -0.00133988 | 0.0813489 | 0.776321 | 0.894897 | 0.95165 | 0.103134 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.56561 | 0.577703 | 0.103466 | 0.178251 | 0.785391 | 0.786087 | -0.000695652 | 0.0828773 | 0.784713 | 0.908027 | 0.957135 | 0.0957641 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.559224 | 0.641785 | 0.133455 | 0.197786 | 0.762396 | 0.764393 | -0.00199667 | 0.081853 | 0.792573 | 0.914562 | 0.964103 | 0.0900756 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1197 | -1.57007 | 0.514931 | -2.68062 | -2.27027 | -1.88467 | -1.62508 | -1.35394 | -0.739541 | 2.1753 |
| player | beta | 1197 | -2.64519 | 0.969644 | -6.41185 | -4.54165 | -3.09034 | -2.43717 | -1.98111 | -1.46576 | -1.13237 |
| player | theta_1 | 1197 | 0.897893 | 0.755713 | -2.03574 | -0.350364 | 0.398785 | 0.894511 | 1.44218 | 2.17447 | 2.48114 |
| player | theta_norm | 1197 | 0.994628 | 0.622796 | 4.59594e-05 | 0.100262 | 0.480679 | 0.921376 | 1.46511 | 2.17447 | 2.48114 |
| tossup | start_difficulty_d1 | 1240 | -1.53989 | 0.264849 | -2.26112 | -1.94052 | -1.73469 | -1.55771 | -1.37358 | -1.06564 | -0.639999 |
| tossup | end_difficulty_d1 | 1240 | -1.89754 | 0.330835 | -2.91995 | -2.4498 | -2.11972 | -1.89123 | -1.67562 | -1.34453 | -1.01863 |
| tossup | total_drop_d1 | 1240 | 0.357645 | 0.111826 | 0.168272 | 0.217428 | 0.26068 | 0.339604 | 0.436055 | 0.558292 | 0.916416 |
| tossup | drop_share_1_d1 | 1240 | 0.340382 | 0.0509279 | 0.171524 | 0.24636 | 0.309405 | 0.346613 | 0.376072 | 0.414136 | 0.495282 |
| tossup | drop_share_2_d1 | 1240 | 0.29351 | 0.0207543 | 0.225196 | 0.256634 | 0.280342 | 0.295852 | 0.308809 | 0.323805 | 0.354305 |
| tossup | drop_share_3_d1 | 1240 | 0.366107 | 0.0617117 | 0.22477 | 0.282055 | 0.321449 | 0.35656 | 0.399315 | 0.487215 | 0.571305 |
| tossup | r_1 | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| tossup | r_norm | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
