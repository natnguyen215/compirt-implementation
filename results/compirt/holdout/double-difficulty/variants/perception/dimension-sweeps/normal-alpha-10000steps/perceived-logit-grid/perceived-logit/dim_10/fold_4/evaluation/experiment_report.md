# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.6288 |
| log_loss | 0.587067 |
| ece | 0.162476 |
| brier | 0.200107 |
| accuracy | 0.696872 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0764833 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.152586 |
| probability_p10 | 0.403735 |
| probability_p50 | 0.619745 |
| probability_p90 | 0.808012 |
| mean_predictive_variance | 0.214057 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100679 |
| joint_tossup_event_log_loss | 6.66458 |
| buzz_position_mae | 0.163018 |
| buzz_position_median_absolute_error | 0.144561 |
| buzz_position_bias | -0.0770219 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.394606 |
| first_buzzer_mean_reciprocal_rank | 0.597818 |
| first_buzzer_log_loss | 1.6003 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.651456 |
| tossup_scorer_player_top1_accuracy | 0.274627 |
| tossup_scorer_team_top1_accuracy | 0.375373 |
| tossup_game_winner_accuracy | 0.798687 |
| tossup_game_margin_mae | 39.2652 |
| tournament_player_ppg_spearman | 0.648885 |
| tournament_player_ppg_mae | 12.1453 |
| tournament_player_ppg_top10_overlap | 0.651724 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.6288 |
| neg_average_precision | 0.323964 |
| neg_precision | 0.33879 |
| neg_recall | 0.354593 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0995859 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0795887 |
| no_buzz_calibration_error | 0.0678616 |
| no_buzz_brier | 0.0242444 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0770219 | -0.0885799 |
| Q1 (0-.2) | 179 | 0.339285 | 0.350296 |
| Q2 (.2-.4) | 957 | 0.187042 | 0.184453 |
| Q3 (.4-.6) | 2203 | 0.035324 | 0.0292791 |
| Q4 (.6-.8) | 2978 | -0.0983683 | -0.0997678 |
| Q5 (.8-1) | 2953 | -0.250119 | -0.242231 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.162476 | 0.200107 | 0.6288 | 0.587067 |
| tossup_correctness | tier | fall | 2876 | 0.144337 | 0.183088 | 0.629362 | 0.550534 |
| tossup_correctness | tier | nationals | 1579 | 0.162294 | 0.217808 | 0.632373 | 0.624059 |
| tossup_correctness | tier | regionals | 1990 | 0.16778 | 0.20652 | 0.615339 | 0.601535 |
| tossup_correctness | tier | winter | 2825 | 0.17748 | 0.203022 | 0.620231 | 0.59339 |
| tossup_correctness | category | Current Events | 123 | 0.164656 | 0.204325 | 0.619222 | 0.592034 |
| tossup_correctness | category | Fine Arts | 1093 | 0.176645 | 0.200547 | 0.662198 | 0.586841 |
| tossup_correctness | category | Geography | 191 | 0.130654 | 0.228223 | 0.595917 | 0.65123 |
| tossup_correctness | category | History | 1469 | 0.12516 | 0.189133 | 0.667388 | 0.561094 |
| tossup_correctness | category | Literature | 1436 | 0.1903 | 0.197758 | 0.579476 | 0.582396 |
| tossup_correctness | category | Mythology | 325 | 0.260486 | 0.209113 | 0.52841 | 0.606913 |
| tossup_correctness | category | Other Academic | 67 | 0.270325 | 0.234097 | 0.657682 | 0.66075 |
| tossup_correctness | category | Philosophy | 322 | 0.177894 | 0.202346 | 0.608638 | 0.590939 |
| tossup_correctness | category | Popular Culture | 100 | 0.291844 | 0.196506 | 0.52094 | 0.583051 |
| tossup_correctness | category | Religion | 365 | 0.129104 | 0.191445 | 0.720072 | 0.568127 |
| tossup_correctness | category | Science | 1456 | 0.140834 | 0.197897 | 0.622371 | 0.58385 |
| tossup_correctness | category | Social Science | 333 | 0.142802 | 0.203634 | 0.678418 | 0.595519 |
| tossup_correctness | category | Unknown | 1990 | 0.16778 | 0.20652 | 0.615339 | 0.601535 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.342772 | 0.303969 | 0.579602 | 0.816095 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.267495 | 0.251933 | 0.639217 | 0.699294 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.210951 | 0.218972 | 0.637544 | 0.627619 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.162457 | 0.186446 | 0.658596 | 0.55697 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0831786 | 0.176719 | 0.637228 | 0.536913 |
