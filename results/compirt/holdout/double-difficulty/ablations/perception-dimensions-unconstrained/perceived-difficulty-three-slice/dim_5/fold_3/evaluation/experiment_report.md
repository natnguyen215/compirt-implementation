# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.665483 |
| log_loss | 0.507211 |
| ece | 0.0178723 |
| brier | 0.164604 |
| accuracy | 0.775771 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00572687 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.124347 |
| probability_p10 | 0.585015 |
| probability_p50 | 0.783413 |
| probability_p90 | 0.900264 |
| mean_predictive_variance | 0.166634 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102121 |
| joint_tossup_event_log_loss | 6.841 |
| buzz_position_mae | 0.1618 |
| buzz_position_median_absolute_error | 0.146712 |
| buzz_position_bias | -0.071238 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.366189 |
| first_buzzer_mean_reciprocal_rank | 0.575248 |
| first_buzzer_log_loss | 1.66509 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.65837 |
| tossup_scorer_player_top1_accuracy | 0.321041 |
| tossup_scorer_team_top1_accuracy | 0.507267 |
| tossup_game_winner_accuracy | 0.769912 |
| tossup_game_margin_mae | 36.2458 |
| tournament_player_ppg_spearman | 0.698908 |
| tournament_player_ppg_mae | 8.92046 |
| tournament_player_ppg_top10_overlap | 0.662069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.665483 |
| neg_average_precision | 0.398255 |
| neg_precision | 0.571429 |
| neg_recall | 0.0996169 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0541058 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0891545 |
| no_buzz_calibration_error | 0.0739701 |
| no_buzz_brier | 0.0253631 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| overall | 9080 | -0.071238 | -0.0893894 |
| Q1 (0-.2) | 192 | 0.368426 | 0.375272 |
| Q2 (.2-.4) | 889 | 0.199916 | 0.199217 |
| Q3 (.4-.6) | 2210 | 0.0442598 | 0.0479798 |
| Q4 (.6-.8) | 2869 | -0.0961451 | -0.0931078 |
| Q5 (.8-1) | 2920 | -0.245643 | -0.24606 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0178723 | 0.164604 | 0.665483 | 0.507211 |
| tossup_correctness | tier | fall | 2817 | 0.0176758 | 0.159001 | 0.664409 | 0.493646 |
| tossup_correctness | tier | nationals | 1542 | 0.0645234 | 0.178925 | 0.708764 | 0.538459 |
| tossup_correctness | tier | regionals | 1934 | 0.023919 | 0.17325 | 0.654138 | 0.5276 |
| tossup_correctness | tier | winter | 2787 | 0.0243043 | 0.156345 | 0.655191 | 0.489487 |
| tossup_correctness | category | Current Events | 125 | 0.0521299 | 0.186099 | 0.70086 | 0.553518 |
| tossup_correctness | category | Fine Arts | 1072 | 0.032836 | 0.162435 | 0.679113 | 0.500293 |
| tossup_correctness | category | Geography | 185 | 0.0607369 | 0.166429 | 0.780699 | 0.505032 |
| tossup_correctness | category | History | 1443 | 0.0182784 | 0.160656 | 0.706383 | 0.494653 |
| tossup_correctness | category | Literature | 1411 | 0.0459205 | 0.151789 | 0.596566 | 0.483369 |
| tossup_correctness | category | Mythology | 320 | 0.0862745 | 0.165483 | 0.589776 | 0.515651 |
| tossup_correctness | category | Other Academic | 64 | 0.0880655 | 0.187239 | 0.585938 | 0.561433 |
| tossup_correctness | category | Philosophy | 312 | 0.0428472 | 0.159243 | 0.589419 | 0.499009 |
| tossup_correctness | category | Popular Culture | 104 | 0.0687734 | 0.13692 | 0.524858 | 0.450273 |
| tossup_correctness | category | Religion | 358 | 0.0237247 | 0.184494 | 0.674882 | 0.549582 |
| tossup_correctness | category | Science | 1431 | 0.020468 | 0.16456 | 0.67859 | 0.505468 |
| tossup_correctness | category | Social Science | 321 | 0.0432756 | 0.171225 | 0.701908 | 0.519671 |
| tossup_correctness | category | Unknown | 1934 | 0.023919 | 0.17325 | 0.654138 | 0.5276 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0712719 | 0.194657 | 0.685409 | 0.574104 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0392026 | 0.178032 | 0.684677 | 0.536443 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0208862 | 0.173313 | 0.643852 | 0.528818 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0255583 | 0.156656 | 0.656317 | 0.488692 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0271568 | 0.159759 | 0.676113 | 0.495757 |
