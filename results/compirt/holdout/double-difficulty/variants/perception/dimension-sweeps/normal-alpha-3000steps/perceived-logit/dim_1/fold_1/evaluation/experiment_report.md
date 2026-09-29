# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.573844 |
| log_loss | 0.625281 |
| ece | 0.126011 |
| brier | 0.195293 |
| accuracy | 0.761355 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.000769823 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0792719 |
| probability_p10 | 0.793205 |
| probability_p50 | 0.904367 |
| probability_p90 | 0.959442 |
| mean_predictive_variance | 0.0956527 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.173865 |
| joint_tossup_event_log_loss | 7.84103 |
| buzz_position_mae | 0.342948 |
| buzz_position_median_absolute_error | 0.348638 |
| buzz_position_bias | -0.331129 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.299351 |
| first_buzzer_mean_reciprocal_rank | 0.521028 |
| first_buzzer_log_loss | 1.7573 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.619158 |
| tossup_scorer_player_top1_accuracy | 0.257359 |
| tossup_scorer_team_top1_accuracy | 0.425108 |
| tossup_game_winner_accuracy | 0.752252 |
| tossup_game_margin_mae | 40.4127 |
| tournament_player_ppg_spearman | 0.625517 |
| tournament_player_ppg_mae | 9.82414 |
| tournament_player_ppg_top10_overlap | 0.610345 |

### Other Metrics

| metric | value |
| --- | --- |
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

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.331129 | -0.348638 |
| Q1 (0-.2) | 167 | 0.167811 | 0.169233 |
| Q2 (.2-.4) | 912 | 0.00657907 | 0.00229414 |
| Q3 (.4-.6) | 2115 | -0.171861 | -0.17568 |
| Q4 (.6-.8) | 2844 | -0.351767 | -0.353988 |
| Q5 (.8-1) | 3055 | -0.55027 | -0.554826 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.126011 | 0.195293 | 0.573844 | 0.625281 |
| tossup_correctness | tier | fall | 2842 | 0.0984455 | 0.174845 | 0.601048 | 0.558271 |
| tossup_correctness | tier | nationals | 1564 | 0.160232 | 0.226147 | 0.581808 | 0.705035 |
| tossup_correctness | tier | regionals | 1937 | 0.13357 | 0.19979 | 0.55841 | 0.643579 |
| tossup_correctness | tier | winter | 2750 | 0.132134 | 0.19571 | 0.551195 | 0.636286 |
| tossup_correctness | category | Current Events | 126 | 0.13277 | 0.19086 | 0.549236 | 0.596778 |
| tossup_correctness | category | Fine Arts | 1071 | 0.133675 | 0.194131 | 0.584516 | 0.625591 |
| tossup_correctness | category | Geography | 185 | 0.182669 | 0.237058 | 0.600498 | 0.729864 |
| tossup_correctness | category | History | 1440 | 0.128483 | 0.20243 | 0.53798 | 0.644248 |
| tossup_correctness | category | Literature | 1422 | 0.0959249 | 0.159085 | 0.558336 | 0.536228 |
| tossup_correctness | category | Mythology | 318 | 0.0979109 | 0.169388 | 0.629839 | 0.540398 |
| tossup_correctness | category | Other Academic | 66 | 0.165969 | 0.234243 | 0.552072 | 0.737078 |
| tossup_correctness | category | Philosophy | 311 | 0.144773 | 0.204172 | 0.60383 | 0.64544 |
| tossup_correctness | category | Popular Culture | 102 | 0.0288795 | 0.104271 | 0.642593 | 0.359899 |
| tossup_correctness | category | Religion | 358 | 0.174222 | 0.232366 | 0.591776 | 0.718424 |
| tossup_correctness | category | Science | 1433 | 0.138713 | 0.209162 | 0.577515 | 0.654842 |
| tossup_correctness | category | Social Science | 324 | 0.147085 | 0.212635 | 0.578059 | 0.663847 |
| tossup_correctness | category | Unknown | 1937 | 0.13357 | 0.19979 | 0.55841 | 0.643579 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.165133 | 0.232005 | 0.512255 | 0.722658 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.139078 | 0.214461 | 0.57597 | 0.664367 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.125225 | 0.198829 | 0.566239 | 0.627734 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.110145 | 0.181749 | 0.575435 | 0.585971 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.137156 | 0.197725 | 0.576492 | 0.643187 |
