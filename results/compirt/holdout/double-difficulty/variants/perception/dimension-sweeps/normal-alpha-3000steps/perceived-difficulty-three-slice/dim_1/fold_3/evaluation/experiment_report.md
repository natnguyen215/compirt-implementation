# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.588191 |
| log_loss | 0.548829 |
| ece | 0.0567701 |
| brier | 0.180163 |
| accuracy | 0.756938 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0131057 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.134497 |
| probability_p10 | 0.566616 |
| probability_p50 | 0.781801 |
| probability_p90 | 0.907957 |
| mean_predictive_variance | 0.166019 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.106389 |
| joint_tossup_event_log_loss | 6.97983 |
| buzz_position_mae | 0.1658 |
| buzz_position_median_absolute_error | 0.151391 |
| buzz_position_bias | -0.0721161 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.31663 |
| first_buzzer_mean_reciprocal_rank | 0.533718 |
| first_buzzer_log_loss | 1.74575 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.630837 |
| tossup_scorer_player_top1_accuracy | 0.273319 |
| tossup_scorer_team_top1_accuracy | 0.469414 |
| tossup_game_winner_accuracy | 0.754425 |
| tossup_game_margin_mae | 40.5941 |
| tournament_player_ppg_spearman | 0.624106 |
| tournament_player_ppg_mae | 10.0786 |
| tournament_player_ppg_top10_overlap | 0.593103 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.588191 |
| neg_average_precision | 0.296512 |
| neg_precision | 0.368653 |
| neg_recall | 0.0799808 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.056099 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0858513 |
| no_buzz_calibration_error | 0.0706669 |
| no_buzz_brier | 0.0235903 |
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
| overall | 9080 | -0.0721161 | -0.0903442 |
| Q1 (0-.2) | 192 | 0.378157 | 0.384799 |
| Q2 (.2-.4) | 889 | 0.209546 | 0.210308 |
| Q3 (.4-.6) | 2210 | 0.0510428 | 0.0520261 |
| Q4 (.6-.8) | 2869 | -0.0975321 | -0.0953657 |
| Q5 (.8-1) | 2920 | -0.255716 | -0.255642 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0567701 | 0.180163 | 0.588191 | 0.548829 |
| tossup_correctness | tier | fall | 2817 | 0.0811047 | 0.180081 | 0.564999 | 0.547986 |
| tossup_correctness | tier | nationals | 1542 | 0.0639282 | 0.19138 | 0.634868 | 0.573386 |
| tossup_correctness | tier | regionals | 1934 | 0.0481367 | 0.185531 | 0.591922 | 0.562484 |
| tossup_correctness | tier | winter | 2787 | 0.0555518 | 0.170316 | 0.589681 | 0.52662 |
| tossup_correctness | category | Current Events | 125 | 0.125647 | 0.22678 | 0.534091 | 0.647427 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0531499 | 0.177359 | 0.591252 | 0.542315 |
| tossup_correctness | category | Geography | 185 | 0.0502227 | 0.184653 | 0.724336 | 0.552281 |
| tossup_correctness | category | History | 1443 | 0.0648492 | 0.18382 | 0.602184 | 0.550608 |
| tossup_correctness | category | Literature | 1411 | 0.0727462 | 0.161213 | 0.525681 | 0.516414 |
| tossup_correctness | category | Mythology | 320 | 0.103054 | 0.183641 | 0.531496 | 0.561821 |
| tossup_correctness | category | Other Academic | 64 | 0.163185 | 0.19456 | 0.561198 | 0.581001 |
| tossup_correctness | category | Philosophy | 312 | 0.0664886 | 0.165441 | 0.536 | 0.518629 |
| tossup_correctness | category | Popular Culture | 104 | 0.223901 | 0.196033 | 0.49858 | 0.57579 |
| tossup_correctness | category | Religion | 358 | 0.0782171 | 0.201134 | 0.607104 | 0.597925 |
| tossup_correctness | category | Science | 1431 | 0.0417989 | 0.177605 | 0.613902 | 0.538126 |
| tossup_correctness | category | Social Science | 321 | 0.0663853 | 0.194153 | 0.588172 | 0.576635 |
| tossup_correctness | category | Unknown | 1934 | 0.0481367 | 0.185531 | 0.591922 | 0.562484 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0798938 | 0.212981 | 0.60229 | 0.615625 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0978102 | 0.206118 | 0.573451 | 0.603004 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0670345 | 0.190879 | 0.563316 | 0.571636 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.049996 | 0.168861 | 0.588049 | 0.520873 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0445608 | 0.173098 | 0.599734 | 0.53815 |
