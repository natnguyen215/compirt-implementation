# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_1/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_1/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 332163 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.573844 |
| log_loss | 0.625281 |
| ece | 0.126011 |
| brier | 0.195293 |
| accuracy | 0.761355 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.000769823 |
| probability_std | 0.0792719 |
| probability_p10 | 0.793205 |
| probability_p50 | 0.904367 |
| probability_p90 | 0.959442 |
| mean_predictive_variance | 0.0956527 |
| integrated_brier_score | 0.173865 |
| joint_tossup_event_log_loss | 7.84103 |
| buzz_position_mae | 0.342948 |
| buzz_position_median_absolute_error | 0.348638 |
| buzz_position_bias | -0.331129 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.299351 |
| first_buzzer_mean_reciprocal_rank | 0.521028 |
| first_buzzer_log_loss | 1.7573 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.619158 |
| tossup_scorer_player_top1_accuracy | 0.257359 |
| tossup_scorer_team_top1_accuracy | 0.425108 |
| tossup_game_winner_accuracy | 0.752252 |
| tossup_game_margin_mae | 40.4127 |
| tournament_player_ppg_spearman | 0.625517 |
| tournament_player_ppg_mae | 9.82414 |
| tournament_player_ppg_top10_overlap | 0.610345 |
| neg_auroc | 0.573844 |
| neg_average_precision | 0.292413 |
| neg_precision | 0.347826 |
| neg_recall | 0.00369857 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0292741 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.227745 |
| no_buzz_calibration_error | 0.211836 |
| no_buzz_brier | 0.0679362 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| tossup_correctness | aggregate | all | 9093 | 0.573844 | 0.625281 | 0.126011 | 0.195293 | 0.761355 | 0.762125 | -0.000769823 | 0.0792719 | 0.793205 | 0.904367 | 0.959442 | 0.0956527 |
| tossup_correctness | tier | fall | 2842 | 0.601048 | 0.558271 | 0.0984455 | 0.174845 | 0.784307 | 0.785362 | -0.00105559 | 0.0759381 | 0.785236 | 0.899861 | 0.954787 | 0.099469 |
| tossup_correctness | tier | nationals | 1564 | 0.581808 | 0.705035 | 0.160232 | 0.226147 | 0.719309 | 0.718031 | 0.00127877 | 0.0873105 | 0.766119 | 0.900199 | 0.962301 | 0.10038 |
| tossup_correctness | tier | regionals | 1937 | 0.55841 | 0.643579 | 0.13357 | 0.19979 | 0.755292 | 0.758389 | -0.00309757 | 0.0900434 | 0.787238 | 0.90424 | 0.959639 | 0.0957823 |
| tossup_correctness | tier | winter | 2750 | 0.551195 | 0.636286 | 0.132134 | 0.19571 | 0.765818 | 0.765818 | 0 | 0.067798 | 0.813569 | 0.911106 | 0.962001 | 0.0889288 |
| tossup_correctness | category | Current Events | 126 | 0.549236 | 0.596778 | 0.13277 | 0.19086 | 0.769841 | 0.769841 | 0 | 0.0836922 | 0.754462 | 0.883058 | 0.948222 | 0.109122 |
| tossup_correctness | category | Fine Arts | 1071 | 0.584516 | 0.625591 | 0.133675 | 0.194131 | 0.76564 | 0.766573 | -0.000933707 | 0.0682048 | 0.819121 | 0.90996 | 0.962872 | 0.0891534 |
| tossup_correctness | category | Geography | 185 | 0.600498 | 0.729864 | 0.182669 | 0.237058 | 0.702703 | 0.697297 | 0.00540541 | 0.0832497 | 0.774466 | 0.902676 | 0.95801 | 0.0986949 |
| tossup_correctness | category | History | 1440 | 0.53798 | 0.644248 | 0.128483 | 0.20243 | 0.754167 | 0.754167 | 0 | 0.0811371 | 0.775343 | 0.898144 | 0.953787 | 0.102164 |
| tossup_correctness | category | Literature | 1422 | 0.558336 | 0.536228 | 0.0959249 | 0.159085 | 0.814346 | 0.814346 | 0 | 0.0685067 | 0.822074 | 0.921444 | 0.967241 | 0.0822831 |
| tossup_correctness | category | Mythology | 318 | 0.629839 | 0.540398 | 0.0979109 | 0.169388 | 0.786164 | 0.789308 | -0.00314465 | 0.0760698 | 0.798644 | 0.901428 | 0.955546 | 0.0980149 |
| tossup_correctness | category | Other Academic | 66 | 0.552072 | 0.737078 | 0.165969 | 0.234243 | 0.712121 | 0.712121 | 0 | 0.0797423 | 0.76305 | 0.89985 | 0.95984 | 0.101033 |
| tossup_correctness | category | Philosophy | 311 | 0.60383 | 0.64544 | 0.144773 | 0.204172 | 0.745981 | 0.745981 | 0 | 0.0758353 | 0.797616 | 0.907535 | 0.960627 | 0.094014 |
| tossup_correctness | category | Popular Culture | 102 | 0.642593 | 0.359899 | 0.0288795 | 0.104271 | 0.872549 | 0.882353 | -0.00980392 | 0.0783528 | 0.809712 | 0.907793 | 0.966521 | 0.0935066 |
| tossup_correctness | category | Religion | 358 | 0.591776 | 0.718424 | 0.174222 | 0.232366 | 0.709497 | 0.712291 | -0.0027933 | 0.0837842 | 0.771351 | 0.902125 | 0.957229 | 0.0999999 |
| tossup_correctness | category | Science | 1433 | 0.577515 | 0.654842 | 0.138713 | 0.209162 | 0.739707 | 0.738311 | 0.00139567 | 0.0763822 | 0.789922 | 0.891984 | 0.950993 | 0.102777 |
| tossup_correctness | category | Social Science | 324 | 0.578059 | 0.663847 | 0.147085 | 0.212635 | 0.731481 | 0.731481 | 0 | 0.0710252 | 0.793683 | 0.89668 | 0.946597 | 0.101643 |
| tossup_correctness | category | Unknown | 1937 | 0.55841 | 0.643579 | 0.13357 | 0.19979 | 0.755292 | 0.758389 | -0.00309757 | 0.0900434 | 0.787238 | 0.90424 | 0.959639 | 0.0957823 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.512255 | 0.722658 | 0.165133 | 0.232005 | 0.712575 | 0.712575 | 0 | 0.0821038 | 0.757128 | 0.873611 | 0.941869 | 0.112682 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.57597 | 0.664367 | 0.139078 | 0.214461 | 0.72807 | 0.729167 | -0.00109649 | 0.0857291 | 0.752715 | 0.882655 | 0.948907 | 0.111107 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.566239 | 0.627734 | 0.125225 | 0.198829 | 0.75461 | 0.755083 | -0.000472813 | 0.0787502 | 0.788927 | 0.894518 | 0.95089 | 0.102118 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.575435 | 0.585971 | 0.110145 | 0.181749 | 0.779887 | 0.780942 | -0.00105485 | 0.0780584 | 0.800025 | 0.905525 | 0.958931 | 0.0942063 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.576492 | 0.643187 | 0.137156 | 0.197725 | 0.761375 | 0.762029 | -0.000654664 | 0.0762234 | 0.808442 | 0.915869 | 0.966214 | 0.0869788 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1167 | -1.57553 | 0.496582 | -2.61095 | -2.26489 | -1.87214 | -1.6227 | -1.35563 | -0.797362 | 2.08921 |
| player | beta | 1167 | -2.63339 | 0.963438 | -6.41525 | -4.63548 | -3.0787 | -2.42944 | -1.94684 | -1.41149 | -1.08507 |
| player | theta_1 | 1167 | 0.906682 | 0.75277 | -1.82963 | -0.316616 | 0.398076 | 0.881319 | 1.45683 | 2.18065 | 2.52306 |
| player | theta_norm | 1167 | 0.994435 | 0.632211 | 0.000692281 | 0.0994052 | 0.457191 | 0.916343 | 1.46876 | 2.18065 | 2.52306 |
| tossup | start_difficulty_d1 | 1220 | -1.5414 | 0.267643 | -2.28402 | -1.94201 | -1.73621 | -1.56618 | -1.37536 | -1.06342 | -0.697481 |
| tossup | end_difficulty_d1 | 1220 | -1.89169 | 0.327492 | -2.85983 | -2.43806 | -2.11615 | -1.89814 | -1.66875 | -1.33971 | -1.04793 |
| tossup | total_drop_d1 | 1220 | 0.350292 | 0.10416 | 0.175245 | 0.215379 | 0.258865 | 0.339237 | 0.423287 | 0.53865 | 0.707175 |
| tossup | drop_share_1_d1 | 1220 | 0.340732 | 0.0514604 | 0.171048 | 0.245451 | 0.308759 | 0.346063 | 0.377304 | 0.416265 | 0.490492 |
| tossup | drop_share_2_d1 | 1220 | 0.292562 | 0.0202054 | 0.224149 | 0.256649 | 0.279322 | 0.294566 | 0.306907 | 0.323249 | 0.350727 |
| tossup | drop_share_3_d1 | 1220 | 0.366706 | 0.0621034 | 0.229265 | 0.28183 | 0.320561 | 0.357882 | 0.402485 | 0.486718 | 0.580172 |
| tossup | r_1 | 1220 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| tossup | r_norm | 1220 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
