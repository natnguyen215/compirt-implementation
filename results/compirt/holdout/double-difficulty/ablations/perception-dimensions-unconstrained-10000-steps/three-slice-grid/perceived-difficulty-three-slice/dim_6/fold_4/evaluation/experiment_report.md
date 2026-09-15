# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.661695 |
| log_loss | 0.507282 |
| ece | 0.0221173 |
| brier | 0.164587 |
| accuracy | 0.775944 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.002589 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.131296 |
| probability_p10 | 0.579097 |
| probability_p50 | 0.783126 |
| probability_p90 | 0.909321 |
| mean_predictive_variance | 0.164571 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100886 |
| joint_tossup_event_log_loss | 6.94517 |
| buzz_position_mae | 0.159007 |
| buzz_position_median_absolute_error | 0.144411 |
| buzz_position_bias | -0.0608312 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.34822 |
| first_buzzer_mean_reciprocal_rank | 0.557207 |
| first_buzzer_log_loss | 1.71215 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.637864 |
| tossup_scorer_player_top1_accuracy | 0.314392 |
| tossup_scorer_team_top1_accuracy | 0.495309 |
| tossup_game_winner_accuracy | 0.800875 |
| tossup_game_margin_mae | 33.7513 |
| tournament_player_ppg_spearman | 0.70001 |
| tournament_player_ppg_mae | 9.04653 |
| tournament_player_ppg_top10_overlap | 0.67931 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.661695 |
| neg_average_precision | 0.380979 |
| neg_precision | 0.528986 |
| neg_recall | 0.104236 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0562101 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.091796 |
| no_buzz_calibration_error | 0.0800689 |
| no_buzz_brier | 0.0250189 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| overall | 9270 | -0.0608312 | -0.0781823 |
| Q1 (0-.2) | 179 | 0.365841 | 0.367135 |
| Q2 (.2-.4) | 957 | 0.21025 | 0.208462 |
| Q3 (.4-.6) | 2203 | 0.0589342 | 0.0620119 |
| Q4 (.6-.8) | 2978 | -0.0844125 | -0.0815774 |
| Q5 (.8-1) | 2953 | -0.240112 | -0.240082 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0221173 | 0.164587 | 0.661695 | 0.507282 |
| tossup_correctness | tier | fall | 2876 | 0.0173012 | 0.154923 | 0.656805 | 0.483704 |
| tossup_correctness | tier | nationals | 1579 | 0.0546623 | 0.18576 | 0.665299 | 0.554931 |
| tossup_correctness | tier | regionals | 1990 | 0.0283164 | 0.166399 | 0.672395 | 0.511209 |
| tossup_correctness | tier | winter | 2825 | 0.0205207 | 0.161315 | 0.652686 | 0.501886 |
| tossup_correctness | category | Current Events | 123 | 0.0865629 | 0.168816 | 0.699193 | 0.518251 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0235658 | 0.166217 | 0.657683 | 0.511199 |
| tossup_correctness | category | Geography | 191 | 0.0674596 | 0.180279 | 0.74602 | 0.538433 |
| tossup_correctness | category | History | 1469 | 0.0326301 | 0.168758 | 0.68655 | 0.513346 |
| tossup_correctness | category | Literature | 1436 | 0.0537819 | 0.150543 | 0.609355 | 0.48214 |
| tossup_correctness | category | Mythology | 325 | 0.098991 | 0.141913 | 0.622871 | 0.455529 |
| tossup_correctness | category | Other Academic | 67 | 0.118524 | 0.180907 | 0.598383 | 0.547087 |
| tossup_correctness | category | Philosophy | 322 | 0.0505741 | 0.166344 | 0.609612 | 0.513459 |
| tossup_correctness | category | Popular Culture | 100 | 0.145835 | 0.129825 | 0.551583 | 0.428831 |
| tossup_correctness | category | Religion | 365 | 0.0445882 | 0.193346 | 0.645402 | 0.569674 |
| tossup_correctness | category | Science | 1456 | 0.0223853 | 0.164222 | 0.675329 | 0.504553 |
| tossup_correctness | category | Social Science | 333 | 0.0277064 | 0.177668 | 0.691312 | 0.534338 |
| tossup_correctness | category | Unknown | 1990 | 0.0283164 | 0.166399 | 0.672395 | 0.511209 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.083793 | 0.180658 | 0.642952 | 0.546033 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0556755 | 0.182625 | 0.619025 | 0.549984 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0206016 | 0.168047 | 0.660137 | 0.51403 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0190716 | 0.154778 | 0.678379 | 0.481409 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0262973 | 0.165078 | 0.660715 | 0.512152 |
