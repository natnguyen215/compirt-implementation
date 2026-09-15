# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.574321 |
| log_loss | 0.61936 |
| ece | 0.125048 |
| brier | 0.193529 |
| accuracy | 0.763852 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0013986 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.075534 |
| probability_p10 | 0.797226 |
| probability_p50 | 0.903393 |
| probability_p90 | 0.958832 |
| mean_predictive_variance | 0.0949859 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.170106 |
| joint_tossup_event_log_loss | 7.83156 |
| buzz_position_mae | 0.335345 |
| buzz_position_median_absolute_error | 0.337971 |
| buzz_position_bias | -0.32226 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.304465 |
| first_buzzer_mean_reciprocal_rank | 0.524606 |
| first_buzzer_log_loss | 1.74684 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.618612 |
| tossup_scorer_player_top1_accuracy | 0.25966 |
| tossup_scorer_team_top1_accuracy | 0.414968 |
| tossup_game_winner_accuracy | 0.746696 |
| tossup_game_margin_mae | 41.3866 |
| tournament_player_ppg_spearman | 0.621557 |
| tournament_player_ppg_mae | 9.74701 |
| tournament_player_ppg_top10_overlap | 0.606897 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.574321 |
| neg_average_precision | 0.285217 |
| neg_precision | 0.24 |
| neg_recall | 0.00274977 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0293395 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.232472 |
| no_buzz_calibration_error | 0.219202 |
| no_buzz_brier | 0.0697304 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| overall | 9295 | -0.32226 | -0.337962 |
| Q1 (0-.2) | 197 | 0.170772 | 0.171037 |
| Q2 (.2-.4) | 985 | 0.00479672 | -0.0014737 |
| Q3 (.4-.6) | 2251 | -0.170994 | -0.172656 |
| Q4 (.6-.8) | 2866 | -0.351258 | -0.351776 |
| Q5 (.8-1) | 2996 | -0.548118 | -0.552891 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.125048 | 0.193529 | 0.574321 | 0.61936 |
| tossup_correctness | tier | fall | 2933 | 0.0894719 | 0.169645 | 0.599334 | 0.542249 |
| tossup_correctness | tier | nationals | 1584 | 0.166781 | 0.225554 | 0.576735 | 0.714327 |
| tossup_correctness | tier | regionals | 1886 | 0.14336 | 0.210772 | 0.544804 | 0.671018 |
| tossup_correctness | tier | winter | 2892 | 0.126576 | 0.188966 | 0.576662 | 0.611861 |
| tossup_correctness | category | Current Events | 124 | 0.124626 | 0.20165 | 0.52931 | 0.644238 |
| tossup_correctness | category | Fine Arts | 1103 | 0.143824 | 0.204666 | 0.5188 | 0.671309 |
| tossup_correctness | category | Geography | 197 | 0.221441 | 0.25651 | 0.678788 | 0.76725 |
| tossup_correctness | category | History | 1491 | 0.101847 | 0.175665 | 0.592512 | 0.560122 |
| tossup_correctness | category | Literature | 1472 | 0.103722 | 0.167083 | 0.569978 | 0.555889 |
| tossup_correctness | category | Mythology | 332 | 0.100623 | 0.155 | 0.617682 | 0.501053 |
| tossup_correctness | category | Other Academic | 69 | 0.208859 | 0.19937 | 0.449095 | 0.664285 |
| tossup_correctness | category | Philosophy | 324 | 0.0900768 | 0.165523 | 0.589902 | 0.535577 |
| tossup_correctness | category | Popular Culture | 102 | 0.10196 | 0.150718 | 0.451211 | 0.503654 |
| tossup_correctness | category | Religion | 372 | 0.170749 | 0.224428 | 0.652953 | 0.682647 |
| tossup_correctness | category | Science | 1487 | 0.12805 | 0.196824 | 0.601578 | 0.617989 |
| tossup_correctness | category | Social Science | 336 | 0.185819 | 0.243471 | 0.541864 | 0.763499 |
| tossup_correctness | category | Unknown | 1886 | 0.14336 | 0.210772 | 0.544804 | 0.671018 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.132017 | 0.206397 | 0.580637 | 0.638489 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.135278 | 0.210707 | 0.566034 | 0.656164 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.113678 | 0.18681 | 0.599428 | 0.589347 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.110654 | 0.179634 | 0.585231 | 0.576587 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.146348 | 0.205376 | 0.553255 | 0.669469 |
