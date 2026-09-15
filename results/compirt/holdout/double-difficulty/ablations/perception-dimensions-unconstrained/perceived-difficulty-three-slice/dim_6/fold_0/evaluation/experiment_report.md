# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.659226 |
| log_loss | 0.516273 |
| ece | 0.0103505 |
| brier | 0.168537 |
| accuracy | 0.769338 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00408822 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.115444 |
| probability_p10 | 0.609056 |
| probability_p50 | 0.790971 |
| probability_p90 | 0.899975 |
| mean_predictive_variance | 0.163846 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10296 |
| joint_tossup_event_log_loss | 6.92291 |
| buzz_position_mae | 0.162436 |
| buzz_position_median_absolute_error | 0.147951 |
| buzz_position_bias | -0.0673615 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.367079 |
| first_buzzer_mean_reciprocal_rank | 0.577333 |
| first_buzzer_log_loss | 1.65481 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.646692 |
| tossup_scorer_player_top1_accuracy | 0.334076 |
| tossup_scorer_team_top1_accuracy | 0.49034 |
| tossup_game_winner_accuracy | 0.799559 |
| tossup_game_margin_mae | 34.6627 |
| tournament_player_ppg_spearman | 0.69366 |
| tournament_player_ppg_mae | 9.01635 |
| tournament_player_ppg_top10_overlap | 0.665517 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.659226 |
| neg_average_precision | 0.379849 |
| neg_precision | 0.576613 |
| neg_recall | 0.0655362 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0558003 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0957192 |
| no_buzz_calibration_error | 0.0824496 |
| no_buzz_brier | 0.0270295 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9420 |
| first_buzzer_team_top1_accuracy_events | 9295 |
| tossup_scorer_player_top1_accuracy_events | 9420 |
| tossup_scorer_team_top1_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 454 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0673615 | -0.0837157 |
| Q1 (0-.2) | 197 | 0.352945 | 0.362867 |
| Q2 (.2-.4) | 985 | 0.197044 | 0.198404 |
| Q3 (.4-.6) | 2251 | 0.0488566 | 0.0514432 |
| Q4 (.6-.8) | 2866 | -0.0926546 | -0.0874513 |
| Q5 (.8-1) | 2996 | -0.245051 | -0.243063 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0103505 | 0.168537 | 0.659226 | 0.516273 |
| tossup_correctness | tier | fall | 2933 | 0.0129056 | 0.15557 | 0.65236 | 0.486471 |
| tossup_correctness | tier | nationals | 1584 | 0.0499514 | 0.18996 | 0.652237 | 0.56425 |
| tossup_correctness | tier | regionals | 1886 | 0.0206512 | 0.181583 | 0.629416 | 0.547253 |
| tossup_correctness | tier | winter | 2892 | 0.0296972 | 0.161445 | 0.679886 | 0.500018 |
| tossup_correctness | category | Current Events | 124 | 0.0852386 | 0.167614 | 0.710024 | 0.515488 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0352956 | 0.175829 | 0.628279 | 0.536382 |
| tossup_correctness | category | Geography | 197 | 0.0474989 | 0.188576 | 0.742308 | 0.557146 |
| tossup_correctness | category | History | 1491 | 0.0518014 | 0.157817 | 0.683567 | 0.489895 |
| tossup_correctness | category | Literature | 1472 | 0.0282283 | 0.150451 | 0.641986 | 0.477448 |
| tossup_correctness | category | Mythology | 332 | 0.0552223 | 0.145271 | 0.686559 | 0.457894 |
| tossup_correctness | category | Other Academic | 69 | 0.117802 | 0.197532 | 0.49095 | 0.586313 |
| tossup_correctness | category | Philosophy | 324 | 0.0213607 | 0.146971 | 0.695515 | 0.462751 |
| tossup_correctness | category | Popular Culture | 102 | 0.142076 | 0.161365 | 0.391003 | 0.511679 |
| tossup_correctness | category | Religion | 372 | 0.0398256 | 0.192142 | 0.677504 | 0.56616 |
| tossup_correctness | category | Science | 1487 | 0.0293196 | 0.170428 | 0.684213 | 0.519475 |
| tossup_correctness | category | Social Science | 336 | 0.0517074 | 0.192262 | 0.679068 | 0.56675 |
| tossup_correctness | category | Unknown | 1886 | 0.0206512 | 0.181583 | 0.629416 | 0.547253 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0561095 | 0.186537 | 0.632626 | 0.56295 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0176766 | 0.18175 | 0.658538 | 0.547365 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0173418 | 0.164362 | 0.677653 | 0.504921 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0160663 | 0.159468 | 0.655884 | 0.494614 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0296593 | 0.174821 | 0.654753 | 0.532231 |
