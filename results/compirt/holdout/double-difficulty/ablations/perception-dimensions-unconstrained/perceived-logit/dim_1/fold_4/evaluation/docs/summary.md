# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_1/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_1/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 330960 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.569059 |
| log_loss | 0.601421 |
| ece | 0.114961 |
| brier | 0.18699 |
| accuracy | 0.772816 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.000539374 |
| probability_std | 0.0803842 |
| probability_p10 | 0.789926 |
| probability_p50 | 0.901739 |
| probability_p90 | 0.959314 |
| mean_predictive_variance | 0.0971994 |
| integrated_brier_score | 0.172559 |
| joint_tossup_event_log_loss | 7.84346 |
| buzz_position_mae | 0.337116 |
| buzz_position_median_absolute_error | 0.340396 |
| buzz_position_bias | -0.324663 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.309061 |
| first_buzzer_mean_reciprocal_rank | 0.52467 |
| first_buzzer_log_loss | 1.76321 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.612621 |
| tossup_scorer_player_top1_accuracy | 0.248934 |
| tossup_scorer_team_top1_accuracy | 0.4258 |
| tossup_game_winner_accuracy | 0.724289 |
| tossup_game_margin_mae | 42.9532 |
| tournament_player_ppg_spearman | 0.633196 |
| tournament_player_ppg_mae | 10.2034 |
| tournament_player_ppg_top10_overlap | 0.634483 |
| neg_auroc | 0.569059 |
| neg_average_precision | 0.27553 |
| neg_precision | 0.407407 |
| neg_recall | 0.0052356 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0292159 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.227944 |
| no_buzz_calibration_error | 0.216217 |
| no_buzz_brier | 0.0674018 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.569059 | 0.601421 | 0.114961 | 0.18699 | 0.772816 | 0.773355 | -0.000539374 | 0.0803842 | 0.789926 | 0.901739 | 0.959314 | 0.0971994 |
| tossup_correctness | tier | fall | 2876 | 0.565083 | 0.556115 | 0.0903138 | 0.171497 | 0.793115 | 0.793115 | 0 | 0.07081 | 0.789957 | 0.895767 | 0.956402 | 0.0990222 |
| tossup_correctness | tier | nationals | 1579 | 0.587155 | 0.687602 | 0.156387 | 0.218188 | 0.728309 | 0.729576 | -0.00126662 | 0.0967644 | 0.745334 | 0.904568 | 0.960305 | 0.0988613 |
| tossup_correctness | tier | regionals | 1990 | 0.55647 | 0.620472 | 0.120227 | 0.193189 | 0.764322 | 0.765829 | -0.00150754 | 0.0962486 | 0.743319 | 0.897108 | 0.961131 | 0.102599 |
| tossup_correctness | tier | winter | 2825 | 0.57289 | 0.585955 | 0.116161 | 0.180957 | 0.783009 | 0.783009 | 0 | 0.0640547 | 0.820285 | 0.90722 | 0.960841 | 0.0906109 |
| tossup_correctness | category | Current Events | 123 | 0.595011 | 0.595576 | 0.115128 | 0.189414 | 0.756098 | 0.764228 | -0.00813008 | 0.0946922 | 0.724086 | 0.88424 | 0.952926 | 0.114095 |
| tossup_correctness | category | Fine Arts | 1093 | 0.571042 | 0.621099 | 0.133104 | 0.191868 | 0.770357 | 0.769442 | 0.000914913 | 0.068881 | 0.822551 | 0.91181 | 0.96124 | 0.0877948 |
| tossup_correctness | category | Geography | 191 | 0.704802 | 0.691497 | 0.191142 | 0.231942 | 0.685864 | 0.691099 | -0.0052356 | 0.0801814 | 0.778271 | 0.89605 | 0.957461 | 0.101809 |
| tossup_correctness | category | History | 1469 | 0.580274 | 0.620863 | 0.123179 | 0.196508 | 0.758339 | 0.758339 | 0 | 0.0810267 | 0.779658 | 0.893249 | 0.954788 | 0.101891 |
| tossup_correctness | category | Literature | 1436 | 0.55308 | 0.534998 | 0.0966767 | 0.158484 | 0.81546 | 0.81546 | 0 | 0.066504 | 0.835933 | 0.923603 | 0.966357 | 0.0810157 |
| tossup_correctness | category | Mythology | 325 | 0.581437 | 0.455214 | 0.0574899 | 0.135819 | 0.843077 | 0.843077 | 0 | 0.0693394 | 0.813812 | 0.900012 | 0.959972 | 0.0945135 |
| tossup_correctness | category | Other Academic | 67 | 0.586253 | 0.558261 | 0.102319 | 0.173457 | 0.791045 | 0.791045 | 0 | 0.0696902 | 0.796163 | 0.887585 | 0.951862 | 0.100959 |
| tossup_correctness | category | Philosophy | 322 | 0.501862 | 0.610557 | 0.124906 | 0.184666 | 0.785714 | 0.785714 | 0 | 0.0707679 | 0.819827 | 0.910852 | 0.954889 | 0.0909901 |
| tossup_correctness | category | Popular Culture | 100 | 0.496425 | 0.377452 | 0.0387596 | 0.105383 | 0.89 | 0.89 | 0 | 0.0751256 | 0.798893 | 0.901595 | 0.956113 | 0.0990502 |
| tossup_correctness | category | Religion | 365 | 0.596835 | 0.68947 | 0.165494 | 0.220991 | 0.717808 | 0.723288 | -0.00547945 | 0.0792835 | 0.787114 | 0.902189 | 0.954225 | 0.0970754 |
| tossup_correctness | category | Science | 1456 | 0.559822 | 0.59924 | 0.107793 | 0.189406 | 0.76717 | 0.76717 | 0 | 0.0739838 | 0.786191 | 0.88471 | 0.951086 | 0.105822 |
| tossup_correctness | category | Social Science | 333 | 0.510562 | 0.696977 | 0.14201 | 0.219772 | 0.732733 | 0.72973 | 0.003003 | 0.0778249 | 0.776541 | 0.891999 | 0.949575 | 0.105753 |
| tossup_correctness | category | Unknown | 1990 | 0.55647 | 0.620472 | 0.120227 | 0.193189 | 0.764322 | 0.765829 | -0.00150754 | 0.0962486 | 0.743319 | 0.897108 | 0.961131 | 0.102599 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.523217 | 0.629733 | 0.12263 | 0.195571 | 0.75419 | 0.748603 | 0.00558659 | 0.0894289 | 0.756857 | 0.882596 | 0.94577 | 0.112249 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.514605 | 0.638827 | 0.116595 | 0.201354 | 0.751306 | 0.754441 | -0.0031348 | 0.0837654 | 0.772362 | 0.880563 | 0.948803 | 0.109928 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.565575 | 0.608279 | 0.121307 | 0.191835 | 0.766228 | 0.766682 | -0.000453926 | 0.0790131 | 0.787508 | 0.890491 | 0.95554 | 0.103012 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.588224 | 0.564193 | 0.104671 | 0.174588 | 0.788113 | 0.787441 | 0.000671592 | 0.0784296 | 0.795191 | 0.904845 | 0.958497 | 0.0956208 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.575006 | 0.620009 | 0.12664 | 0.190706 | 0.770403 | 0.771758 | -0.00135455 | 0.0798905 | 0.800397 | 0.91379 | 0.964989 | 0.0894173 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1196 | -1.5776 | 0.517417 | -2.7067 | -2.2489 | -1.898 | -1.62845 | -1.35963 | -0.804428 | 2.44053 |
| player | beta | 1196 | -2.63676 | 0.963489 | -6.33741 | -4.58006 | -3.09834 | -2.42936 | -1.95551 | -1.43678 | -1.08169 |
| player | theta_1 | 1196 | 0.90935 | 0.759315 | -1.98197 | -0.256063 | 0.422615 | 0.871102 | 1.45315 | 2.21018 | 2.55402 |
| player | theta_norm | 1196 | 0.996121 | 0.641155 | 4.01549e-05 | 0.0947876 | 0.47877 | 0.89744 | 1.46426 | 2.21018 | 2.55402 |
| tossup | start_difficulty_d1 | 1240 | -1.53323 | 0.2664 | -2.21447 | -1.94751 | -1.7251 | -1.54861 | -1.37364 | -1.05693 | -0.621246 |
| tossup | end_difficulty_d1 | 1240 | -1.89061 | 0.331014 | -2.89463 | -2.45019 | -2.11238 | -1.89712 | -1.67147 | -1.33221 | -1.02224 |
| tossup | total_drop_d1 | 1240 | 0.357382 | 0.113489 | 0.173762 | 0.216451 | 0.264023 | 0.338957 | 0.431386 | 0.561531 | 1.0757 |
| tossup | drop_share_1_d1 | 1240 | 0.34083 | 0.0512704 | 0.166311 | 0.248865 | 0.308701 | 0.346101 | 0.377059 | 0.413649 | 0.494481 |
| tossup | drop_share_2_d1 | 1240 | 0.293468 | 0.0205865 | 0.21759 | 0.257366 | 0.280341 | 0.295747 | 0.307955 | 0.323214 | 0.361885 |
| tossup | drop_share_3_d1 | 1240 | 0.365703 | 0.0618947 | 0.223668 | 0.281918 | 0.320545 | 0.355996 | 0.400713 | 0.48565 | 0.582151 |
| tossup | r_1 | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| tossup | r_norm | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
