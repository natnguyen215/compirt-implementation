# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.668226 |
| log_loss | 0.509196 |
| ece | 0.0320278 |
| brier | 0.164541 |
| accuracy | 0.776322 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00627753 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.135082 |
| probability_p10 | 0.562293 |
| probability_p50 | 0.775066 |
| probability_p90 | 0.904376 |
| mean_predictive_variance | 0.168297 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10168 |
| joint_tossup_event_log_loss | 6.86213 |
| buzz_position_mae | 0.161491 |
| buzz_position_median_absolute_error | 0.14599 |
| buzz_position_bias | -0.070415 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.346916 |
| first_buzzer_mean_reciprocal_rank | 0.559222 |
| first_buzzer_log_loss | 1.69449 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.652313 |
| tossup_scorer_player_top1_accuracy | 0.317137 |
| tossup_scorer_team_top1_accuracy | 0.502928 |
| tossup_game_winner_accuracy | 0.769912 |
| tossup_game_margin_mae | 36.354 |
| tournament_player_ppg_spearman | 0.696288 |
| tournament_player_ppg_mae | 9.1197 |
| tournament_player_ppg_top10_overlap | 0.641379 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.668226 |
| neg_average_precision | 0.407247 |
| neg_precision | 0.55666 |
| neg_recall | 0.1341 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0543241 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0879263 |
| no_buzz_calibration_error | 0.0727419 |
| no_buzz_brier | 0.0251007 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9220 |
| first_buzzer_team_top1_accuracy_events | 9080 |
| tossup_scorer_player_top1_accuracy_events | 9220 |
| tossup_scorer_team_top1_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 452 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.070415 | -0.0887837 |
| Q1 (0-.2) | 192 | 0.372129 | 0.383253 |
| Q2 (.2-.4) | 889 | 0.200868 | 0.201499 |
| Q3 (.4-.6) | 2210 | 0.0454424 | 0.0487628 |
| Q4 (.6-.8) | 2869 | -0.0958622 | -0.0926013 |
| Q5 (.8-1) | 2920 | -0.24479 | -0.246061 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0320278 | 0.164541 | 0.668226 | 0.509196 |
| tossup_correctness | tier | fall | 2817 | 0.0321317 | 0.159699 | 0.658431 | 0.496759 |
| tossup_correctness | tier | nationals | 1542 | 0.0651493 | 0.176345 | 0.718649 | 0.531716 |
| tossup_correctness | tier | regionals | 1934 | 0.0225731 | 0.171382 | 0.665787 | 0.52361 |
| tossup_correctness | tier | winter | 2787 | 0.0355232 | 0.158156 | 0.646163 | 0.499304 |
| tossup_correctness | category | Current Events | 125 | 0.132543 | 0.18068 | 0.738329 | 0.540321 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0435841 | 0.165222 | 0.663202 | 0.507719 |
| tossup_correctness | category | Geography | 185 | 0.0794595 | 0.165634 | 0.793846 | 0.506222 |
| tossup_correctness | category | History | 1443 | 0.0357532 | 0.159284 | 0.717423 | 0.491934 |
| tossup_correctness | category | Literature | 1411 | 0.0538886 | 0.154037 | 0.579405 | 0.500011 |
| tossup_correctness | category | Mythology | 320 | 0.0858102 | 0.16401 | 0.595085 | 0.511389 |
| tossup_correctness | category | Other Academic | 64 | 0.0972905 | 0.183288 | 0.602865 | 0.551822 |
| tossup_correctness | category | Philosophy | 312 | 0.0576301 | 0.159426 | 0.600323 | 0.499509 |
| tossup_correctness | category | Popular Culture | 104 | 0.118046 | 0.146333 | 0.490057 | 0.474266 |
| tossup_correctness | category | Religion | 358 | 0.0300251 | 0.181273 | 0.691758 | 0.542273 |
| tossup_correctness | category | Science | 1431 | 0.0439495 | 0.164517 | 0.683526 | 0.505343 |
| tossup_correctness | category | Social Science | 321 | 0.0493244 | 0.173038 | 0.698183 | 0.525179 |
| tossup_correctness | category | Unknown | 1934 | 0.0225731 | 0.171382 | 0.665787 | 0.52361 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0781805 | 0.188372 | 0.715775 | 0.559348 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0434743 | 0.177964 | 0.690935 | 0.536396 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0354695 | 0.173886 | 0.644971 | 0.532461 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0360922 | 0.155972 | 0.666381 | 0.487962 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0417403 | 0.160234 | 0.669689 | 0.500871 |
