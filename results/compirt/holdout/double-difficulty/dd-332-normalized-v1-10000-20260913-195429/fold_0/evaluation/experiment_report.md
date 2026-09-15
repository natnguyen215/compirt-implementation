# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.712223 |
| log_loss | 0.491092 |
| ece | 0.0112871 |
| brier | 0.159591 |
| accuracy | 0.777622 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0123722 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.148969 |
| probability_p10 | 0.562611 |
| probability_p50 | 0.810044 |
| probability_p90 | 0.920742 |
| mean_predictive_variance | 0.154274 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.095789 |
| joint_tossup_event_log_loss | 6.44735 |
| buzz_position_mae | 0.142788 |
| buzz_position_median_absolute_error | 0.122743 |
| buzz_position_bias | -0.0147595 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.379236 |
| first_buzzer_mean_reciprocal_rank | 0.58675 |
| first_buzzer_log_loss | 1.62148 |
| first_buzzer_events | 9295 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.217751 |
| first_buzzer_team_replay_accuracy | 0.473158 |
| tossup_scorer_player_replay_accuracy | 0.23758 |
| tossup_scorer_team_replay_accuracy | 0.446921 |
| tossup_game_winner_accuracy | 0.678492 |
| tossup_model_official_winner_accuracy | 0.709402 |
| tossup_game_margin_mae | 49.5966 |
| tossup_game_zero_margin_mae | 54.8195 |
| tournament_player_ppg_spearman | 0.595601 |
| tournament_player_ppg_mae | 12.411 |
| tournament_player_ppg_top10_overlap | 0.610345 |
| tournament_player_ppg_top10_random_overlap | 0.282327 |
| tournament_player_ppg_top10_adjusted_overlap | 0.455188 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.712223 |
| neg_average_precision | 0.44716 |
| neg_precision | 0.594417 |
| neg_recall | 0.165903 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.174105 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0227762 |
| no_buzz_calibration_error | 0.00950653 |
| no_buzz_brier | 0.0143201 |
| full_pmf_max_mass_error | 6.66134e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9420 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 468 |
| first_buzzer_player_replay_accuracy_events | 9295 |
| first_buzzer_team_replay_accuracy_events | 9295 |
| tossup_scorer_player_replay_accuracy_events | 9420 |
| tossup_scorer_team_replay_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 451 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0147595 | -0.0388105 |
| Q1 (0-.2) | 197 | 0.381935 | 0.376684 |
| Q2 (.2-.4) | 985 | 0.230914 | 0.224433 |
| Q3 (.4-.6) | 2251 | 0.0844976 | 0.0831572 |
| Q4 (.6-.8) | 2866 | -0.0434715 | -0.0451787 |
| Q5 (.8-1) | 2996 | -0.168724 | -0.162392 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0112871 | 0.159591 | 0.712223 | 0.491092 |
| tossup_correctness | tier | fall | 2933 | 0.0161002 | 0.148101 | 0.712337 | 0.462657 |
| tossup_correctness | tier | nationals | 1584 | 0.0348592 | 0.178016 | 0.699581 | 0.53867 |
| tossup_correctness | tier | regionals | 1886 | 0.0256069 | 0.170229 | 0.709153 | 0.515167 |
| tossup_correctness | tier | winter | 2892 | 0.0157628 | 0.154213 | 0.7188 | 0.478169 |
| tossup_correctness | category | Current Events | 124 | 0.082566 | 0.16711 | 0.688172 | 0.516067 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0193591 | 0.160851 | 0.708677 | 0.496802 |
| tossup_correctness | category | Geography | 197 | 0.0668304 | 0.1691 | 0.793124 | 0.511202 |
| tossup_correctness | category | History | 1491 | 0.0178042 | 0.149787 | 0.716569 | 0.465592 |
| tossup_correctness | category | Literature | 1472 | 0.0283998 | 0.137028 | 0.729478 | 0.436176 |
| tossup_correctness | category | Mythology | 332 | 0.0316411 | 0.142566 | 0.692234 | 0.450939 |
| tossup_correctness | category | Other Academic | 69 | 0.160739 | 0.171398 | 0.704751 | 0.513179 |
| tossup_correctness | category | Philosophy | 324 | 0.0387035 | 0.150427 | 0.676626 | 0.470753 |
| tossup_correctness | category | Popular Culture | 102 | 0.0695989 | 0.14948 | 0.440138 | 0.488305 |
| tossup_correctness | category | Religion | 372 | 0.0383207 | 0.185265 | 0.713033 | 0.548079 |
| tossup_correctness | category | Science | 1487 | 0.0319652 | 0.170903 | 0.682612 | 0.519737 |
| tossup_correctness | category | Social Science | 336 | 0.0315527 | 0.177552 | 0.728517 | 0.535666 |
| tossup_correctness | category | Unknown | 1886 | 0.0256069 | 0.170229 | 0.709153 | 0.515167 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0736454 | 0.168644 | 0.692971 | 0.51953 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0278059 | 0.171758 | 0.719613 | 0.518147 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0207973 | 0.162115 | 0.693233 | 0.49909 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0132908 | 0.154029 | 0.698653 | 0.478147 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0128142 | 0.158419 | 0.734383 | 0.4867 |
