# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_2/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_2/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 332733 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.553942 |
| log_loss | 0.599362 |
| ece | 0.105356 |
| brier | 0.186551 |
| accuracy | 0.773031 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.000323625 |
| probability_std | 0.0877394 |
| probability_p10 | 0.762258 |
| probability_p50 | 0.897293 |
| probability_p90 | 0.955917 |
| mean_predictive_variance | 0.102986 |
| integrated_brier_score | 0.173209 |
| joint_tossup_event_log_loss | 7.79412 |
| buzz_position_mae | 0.33942 |
| buzz_position_median_absolute_error | 0.342914 |
| buzz_position_bias | -0.327296 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.339374 |
| first_buzzer_mean_reciprocal_rank | 0.554933 |
| first_buzzer_log_loss | 1.69072 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.62438 |
| tossup_scorer_player_top1_accuracy | 0.256397 |
| tossup_scorer_team_top1_accuracy | 0.423774 |
| tossup_game_winner_accuracy | 0.719912 |
| tossup_game_margin_mae | 43.9089 |
| tournament_player_ppg_spearman | 0.628428 |
| tournament_player_ppg_mae | 10.3888 |
| tournament_player_ppg_top10_overlap | 0.62069 |
| neg_auroc | 0.553942 |
| neg_average_precision | 0.269618 |
| neg_precision | 0.454545 |
| neg_recall | 0.00713946 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0285527 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.234717 |
| no_buzz_calibration_error | 0.22299 |
| no_buzz_brier | 0.0717722 |
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
| tossup_correctness | aggregate | all | 9270 | 0.553942 | 0.599362 | 0.105356 | 0.186551 | 0.773031 | 0.773355 | -0.000323625 | 0.0877394 | 0.762258 | 0.897293 | 0.955917 | 0.102986 |
| tossup_correctness | tier | fall | 2876 | 0.543458 | 0.554935 | 0.0864977 | 0.171846 | 0.792768 | 0.793115 | -0.000347705 | 0.075139 | 0.777199 | 0.894553 | 0.949027 | 0.104019 |
| tossup_correctness | tier | nationals | 1579 | 0.571756 | 0.679678 | 0.13463 | 0.21504 | 0.728942 | 0.729576 | -0.000633312 | 0.108571 | 0.694747 | 0.889749 | 0.961845 | 0.108548 |
| tossup_correctness | tier | regionals | 1990 | 0.531623 | 0.624687 | 0.119326 | 0.194223 | 0.765327 | 0.765829 | -0.000502513 | 0.102751 | 0.712108 | 0.894075 | 0.960253 | 0.1087 |
| tossup_correctness | tier | winter | 2825 | 0.567378 | 0.581861 | 0.108955 | 0.180193 | 0.783009 | 0.783009 | 0 | 0.0713563 | 0.800202 | 0.903704 | 0.95748 | 0.094802 |
| tossup_correctness | category | Current Events | 123 | 0.591709 | 0.583709 | 0.115959 | 0.185683 | 0.756098 | 0.764228 | -0.00813008 | 0.108466 | 0.716764 | 0.88206 | 0.948579 | 0.11559 |
| tossup_correctness | category | Fine Arts | 1093 | 0.564256 | 0.616689 | 0.126917 | 0.19128 | 0.770357 | 0.769442 | 0.000914913 | 0.0711208 | 0.806914 | 0.911466 | 0.958025 | 0.0913169 |
| tossup_correctness | category | Geography | 191 | 0.6849 | 0.687185 | 0.184435 | 0.228609 | 0.685864 | 0.691099 | -0.0052356 | 0.0860065 | 0.766292 | 0.893765 | 0.951571 | 0.106064 |
| tossup_correctness | category | History | 1469 | 0.567929 | 0.612692 | 0.113576 | 0.194921 | 0.758339 | 0.758339 | 0 | 0.0873705 | 0.751909 | 0.886655 | 0.949825 | 0.109076 |
| tossup_correctness | category | Literature | 1436 | 0.537512 | 0.531003 | 0.0825913 | 0.158119 | 0.814763 | 0.81546 | -0.000696379 | 0.0718192 | 0.806245 | 0.91301 | 0.961074 | 0.089494 |
| tossup_correctness | category | Mythology | 325 | 0.574639 | 0.451515 | 0.0617121 | 0.135526 | 0.84 | 0.843077 | -0.00307692 | 0.0713559 | 0.79766 | 0.905818 | 0.951937 | 0.0961747 |
| tossup_correctness | category | Other Academic | 67 | 0.528302 | 0.567452 | 0.0962241 | 0.173651 | 0.791045 | 0.791045 | 0 | 0.082127 | 0.793255 | 0.89995 | 0.943196 | 0.102251 |
| tossup_correctness | category | Philosophy | 322 | 0.502205 | 0.608596 | 0.115806 | 0.184911 | 0.785714 | 0.785714 | 0 | 0.078333 | 0.798079 | 0.911818 | 0.954383 | 0.0932125 |
| tossup_correctness | category | Popular Culture | 100 | 0.537283 | 0.374195 | 0.0337301 | 0.1062 | 0.89 | 0.89 | 0 | 0.0828147 | 0.788542 | 0.896779 | 0.947627 | 0.104644 |
| tossup_correctness | category | Religion | 365 | 0.571595 | 0.699396 | 0.161048 | 0.223192 | 0.720548 | 0.723288 | -0.00273973 | 0.0862979 | 0.785535 | 0.903991 | 0.953004 | 0.0975458 |
| tossup_correctness | category | Science | 1456 | 0.552259 | 0.59638 | 0.0933445 | 0.187737 | 0.767857 | 0.76717 | 0.000686813 | 0.0886005 | 0.74242 | 0.876876 | 0.950347 | 0.113937 |
| tossup_correctness | category | Social Science | 333 | 0.513992 | 0.695348 | 0.145373 | 0.219816 | 0.732733 | 0.72973 | 0.003003 | 0.0866223 | 0.767957 | 0.8952 | 0.947148 | 0.105872 |
| tossup_correctness | category | Unknown | 1990 | 0.531623 | 0.624687 | 0.119326 | 0.194223 | 0.765327 | 0.765829 | -0.000502513 | 0.102751 | 0.712108 | 0.894075 | 0.960253 | 0.1087 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.514096 | 0.624807 | 0.110935 | 0.19521 | 0.759777 | 0.748603 | 0.0111732 | 0.0943104 | 0.720884 | 0.868479 | 0.938249 | 0.123508 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.49517 | 0.63153 | 0.103295 | 0.200855 | 0.753396 | 0.754441 | -0.00104493 | 0.0923704 | 0.737879 | 0.870418 | 0.942592 | 0.119394 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.548768 | 0.600613 | 0.107271 | 0.190488 | 0.764866 | 0.766682 | -0.00181571 | 0.0864339 | 0.759022 | 0.881489 | 0.948253 | 0.111317 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.571601 | 0.563727 | 0.0939097 | 0.174432 | 0.788784 | 0.787441 | 0.00134318 | 0.0852998 | 0.768352 | 0.899737 | 0.955399 | 0.101196 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.560521 | 0.622399 | 0.124625 | 0.190674 | 0.770403 | 0.771758 | -0.00135455 | 0.0859751 | 0.77952 | 0.913353 | 0.963564 | 0.092015 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1196 | -1.49088 | 0.584648 | -2.78487 | -2.28397 | -1.8411 | -1.56265 | -1.23237 | -0.542781 | 2.08447 |
| player | beta | 1196 | -2.94137 | 1.02385 | -6.70352 | -5.04071 | -3.44039 | -2.70698 | -2.19156 | -1.68363 | -1.42413 |
| player | theta_1 | 1196 | 0.946167 | 0.864068 | -1.77018 | -0.467667 | 0.373802 | 0.945689 | 1.54253 | 2.2972 | 3.43802 |
| player | theta_2 | 1196 | 0.918094 | 0.871815 | -2.22703 | -0.598192 | 0.339008 | 1.01304 | 1.55597 | 2.16655 | 3.46871 |
| player | theta_norm | 1196 | 1.66607 | 0.684204 | 0.116928 | 0.485943 | 1.16031 | 1.69554 | 2.18473 | 2.68619 | 3.48661 |
| tossup | start_difficulty_d1 | 1240 | -1.24405 | 0.487894 | -2.21312 | -1.92154 | -1.61147 | -1.31372 | -0.942811 | -0.320307 | -0.144664 |
| tossup | start_difficulty_d2 | 1240 | -1.09651 | 0.412401 | -2.13007 | -1.72945 | -1.45207 | -1.09677 | -0.752411 | -0.471649 | -0.192994 |
| tossup | end_difficulty_d1 | 1240 | -1.77234 | 0.430522 | -3.03004 | -2.50666 | -2.07659 | -1.78905 | -1.42114 | -1.09253 | -0.840721 |
| tossup | end_difficulty_d2 | 1240 | -1.68858 | 0.352581 | -2.85597 | -2.29042 | -1.94493 | -1.64779 | -1.40641 | -1.17805 | -1.00033 |
| tossup | total_drop_d1 | 1240 | 0.528289 | 0.189862 | 0.21252 | 0.258331 | 0.35899 | 0.518809 | 0.688511 | 0.834096 | 1.00434 |
| tossup | total_drop_d2 | 1240 | 0.592074 | 0.173859 | 0.199502 | 0.29833 | 0.457903 | 0.599011 | 0.724473 | 0.862066 | 1.02668 |
| tossup | drop_share_1_d1 | 1240 | 0.331425 | 0.0377849 | 0.172683 | 0.267636 | 0.309876 | 0.331287 | 0.354089 | 0.391651 | 0.470641 |
| tossup | drop_share_2_d1 | 1240 | 0.310982 | 0.0209594 | 0.243214 | 0.273629 | 0.297056 | 0.313254 | 0.326949 | 0.340924 | 0.378612 |
| tossup | drop_share_3_d1 | 1240 | 0.357593 | 0.0449537 | 0.237107 | 0.29654 | 0.330091 | 0.350129 | 0.376323 | 0.449898 | 0.554562 |
| tossup | drop_share_1_d2 | 1240 | 0.327683 | 0.0315218 | 0.202385 | 0.273296 | 0.309712 | 0.327899 | 0.346511 | 0.378926 | 0.461493 |
| tossup | drop_share_2_d2 | 1240 | 0.316367 | 0.0191222 | 0.241446 | 0.280144 | 0.304966 | 0.31895 | 0.330317 | 0.342793 | 0.35801 |
| tossup | drop_share_3_d2 | 1240 | 0.35595 | 0.0386023 | 0.244728 | 0.303658 | 0.331421 | 0.349534 | 0.372708 | 0.434081 | 0.534695 |
| tossup | r_1 | 1240 | 0.583899 | 0.280491 | 0.0315046 | 0.0694483 | 0.395354 | 0.657821 | 0.823363 | 0.919126 | 0.965845 |
| tossup | r_2 | 1240 | 0.416101 | 0.280491 | 0.034155 | 0.0808744 | 0.176637 | 0.342179 | 0.604646 | 0.930552 | 0.968495 |
| tossup | r_norm | 1240 | 0.815343 | 0.0807701 | 0.707107 | 0.70827 | 0.736288 | 0.810726 | 0.890089 | 0.941389 | 0.969008 |
