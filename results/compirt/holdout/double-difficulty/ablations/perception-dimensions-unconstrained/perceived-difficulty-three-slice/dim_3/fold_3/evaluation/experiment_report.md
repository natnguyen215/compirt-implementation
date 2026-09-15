# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.652376 |
| log_loss | 0.514444 |
| ece | 0.0280563 |
| brier | 0.167255 |
| accuracy | 0.774229 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00418502 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.130364 |
| probability_p10 | 0.58219 |
| probability_p50 | 0.785859 |
| probability_p90 | 0.90376 |
| mean_predictive_variance | 0.164992 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102237 |
| joint_tossup_event_log_loss | 6.85288 |
| buzz_position_mae | 0.161437 |
| buzz_position_median_absolute_error | 0.145781 |
| buzz_position_bias | -0.0720698 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.364978 |
| first_buzzer_mean_reciprocal_rank | 0.573001 |
| first_buzzer_log_loss | 1.66192 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.660793 |
| tossup_scorer_player_top1_accuracy | 0.324187 |
| tossup_scorer_team_top1_accuracy | 0.50423 |
| tossup_game_winner_accuracy | 0.780973 |
| tossup_game_margin_mae | 36.4434 |
| tournament_player_ppg_spearman | 0.698597 |
| tournament_player_ppg_mae | 8.92986 |
| tournament_player_ppg_top10_overlap | 0.662069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.652376 |
| neg_average_precision | 0.37605 |
| neg_precision | 0.543779 |
| neg_recall | 0.113027 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0542324 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0875792 |
| no_buzz_calibration_error | 0.0723948 |
| no_buzz_brier | 0.0247787 |
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
| overall | 9080 | -0.0720698 | -0.0889465 |
| Q1 (0-.2) | 192 | 0.364138 | 0.370177 |
| Q2 (.2-.4) | 889 | 0.196216 | 0.194319 |
| Q3 (.4-.6) | 2210 | 0.0418433 | 0.044317 |
| Q4 (.6-.8) | 2869 | -0.0956744 | -0.0912202 |
| Q5 (.8-1) | 2920 | -0.245455 | -0.2464 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0280563 | 0.167255 | 0.652376 | 0.514444 |
| tossup_correctness | tier | fall | 2817 | 0.0179426 | 0.161472 | 0.646984 | 0.501012 |
| tossup_correctness | tier | nationals | 1542 | 0.0653953 | 0.181756 | 0.689948 | 0.54433 |
| tossup_correctness | tier | regionals | 1934 | 0.0404108 | 0.177731 | 0.629007 | 0.540816 |
| tossup_correctness | tier | winter | 2787 | 0.0328536 | 0.157807 | 0.654011 | 0.493184 |
| tossup_correctness | category | Current Events | 125 | 0.0882455 | 0.189722 | 0.694103 | 0.559452 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0384152 | 0.168649 | 0.642956 | 0.516131 |
| tossup_correctness | category | Geography | 185 | 0.0613812 | 0.170278 | 0.769091 | 0.515525 |
| tossup_correctness | category | History | 1443 | 0.0412462 | 0.163927 | 0.699262 | 0.502874 |
| tossup_correctness | category | Literature | 1411 | 0.045207 | 0.152787 | 0.58494 | 0.487557 |
| tossup_correctness | category | Mythology | 320 | 0.0845523 | 0.164608 | 0.588165 | 0.514401 |
| tossup_correctness | category | Other Academic | 64 | 0.138391 | 0.194342 | 0.58724 | 0.576017 |
| tossup_correctness | category | Philosophy | 312 | 0.0563767 | 0.157046 | 0.604452 | 0.492137 |
| tossup_correctness | category | Popular Culture | 104 | 0.123796 | 0.145596 | 0.504261 | 0.47346 |
| tossup_correctness | category | Religion | 358 | 0.0282797 | 0.182809 | 0.680416 | 0.546899 |
| tossup_correctness | category | Science | 1431 | 0.0186866 | 0.163996 | 0.687119 | 0.50339 |
| tossup_correctness | category | Social Science | 321 | 0.0500665 | 0.178899 | 0.67114 | 0.537773 |
| tossup_correctness | category | Unknown | 1934 | 0.0404108 | 0.177731 | 0.629007 | 0.540816 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0501273 | 0.193948 | 0.695831 | 0.573058 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0377584 | 0.179611 | 0.676238 | 0.540536 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0254216 | 0.175619 | 0.636536 | 0.534514 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0309306 | 0.160027 | 0.637989 | 0.497788 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0279285 | 0.162509 | 0.660774 | 0.503822 |
