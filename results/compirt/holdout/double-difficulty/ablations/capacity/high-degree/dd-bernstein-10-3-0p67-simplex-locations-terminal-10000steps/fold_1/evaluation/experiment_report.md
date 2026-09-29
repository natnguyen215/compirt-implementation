# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.708196 |
| log_loss | 0.498371 |
| ece | 0.0167132 |
| brier | 0.162236 |
| accuracy | 0.769493 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00736831 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.156364 |
| probability_p10 | 0.52828 |
| probability_p50 | 0.790258 |
| probability_p90 | 0.91646 |
| mean_predictive_variance | 0.162243 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.098018 |
| joint_tossup_event_log_loss | 6.50193 |
| buzz_position_mae | 0.138167 |
| buzz_position_median_absolute_error | 0.111758 |
| buzz_position_bias | 0.0243281 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.372264 |
| first_buzzer_mean_reciprocal_rank | 0.581808 |
| first_buzzer_log_loss | 1.63356 |
| first_buzzer_events | 9093 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.212251 |
| first_buzzer_team_replay_accuracy | 0.47696 |
| tossup_scorer_player_replay_accuracy | 0.232359 |
| tossup_scorer_team_replay_accuracy | 0.434524 |
| tossup_game_winner_accuracy | 0.696231 |
| tossup_game_margin_mae | 45.6602 |
| tossup_game_zero_margin_mae | 55.2922 |
| tournament_player_ppg_spearman | 0.594428 |
| tournament_player_ppg_mae | 12.3455 |
| tournament_player_ppg_top10_overlap | 0.562069 |
| tournament_player_ppg_top10_random_overlap | 0.269705 |
| tournament_player_ppg_top10_adjusted_overlap | 0.397156 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.708196 |
| neg_average_precision | 0.443312 |
| neg_precision | 0.545209 |
| neg_recall | 0.186778 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.251657 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0269618 |
| no_buzz_calibration_error | 0.0110527 |
| no_buzz_brier | 0.0174036 |
| full_pmf_max_mass_error | 5.55112e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9240 |
| tossup_replay_seed | 42 |
| first_buzzer_player_replay_accuracy_events | 9093 |
| first_buzzer_team_replay_accuracy_events | 9093 |
| tossup_scorer_player_replay_accuracy_events | 9240 |
| tossup_scorer_team_replay_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 451 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | 0.0243281 | 3.76251e-05 |
| Q1 (0-.2) | 167 | 0.434335 | 0.456122 |
| Q2 (.2-.4) | 912 | 0.274992 | 0.27638 |
| Q3 (.4-.6) | 2115 | 0.129013 | 0.127895 |
| Q4 (.6-.8) | 2844 | 0.00453914 | 0.00448644 |
| Q5 (.8-1) | 3055 | -0.126967 | -0.121138 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0167132 | 0.162236 | 0.708196 | 0.498371 |
| tossup_correctness | tier | fall | 2842 | 0.022779 | 0.149668 | 0.726138 | 0.466136 |
| tossup_correctness | tier | nationals | 1564 | 0.0307608 | 0.178373 | 0.715838 | 0.536102 |
| tossup_correctness | tier | regionals | 1937 | 0.0233985 | 0.167598 | 0.690239 | 0.511577 |
| tossup_correctness | tier | winter | 2750 | 0.0280655 | 0.162269 | 0.696005 | 0.500924 |
| tossup_correctness | category | Current Events | 126 | 0.0775486 | 0.159837 | 0.729826 | 0.491608 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0266045 | 0.152941 | 0.744667 | 0.473215 |
| tossup_correctness | category | Geography | 185 | 0.0818391 | 0.164488 | 0.790144 | 0.499739 |
| tossup_correctness | category | History | 1440 | 0.0186381 | 0.168348 | 0.70122 | 0.512749 |
| tossup_correctness | category | Literature | 1422 | 0.0368546 | 0.144719 | 0.672414 | 0.458392 |
| tossup_correctness | category | Mythology | 318 | 0.0570507 | 0.155148 | 0.651662 | 0.488908 |
| tossup_correctness | category | Other Academic | 66 | 0.0907762 | 0.167983 | 0.796193 | 0.502586 |
| tossup_correctness | category | Philosophy | 311 | 0.0443129 | 0.170883 | 0.709897 | 0.513081 |
| tossup_correctness | category | Popular Culture | 102 | 0.0857607 | 0.110103 | 0.536111 | 0.385421 |
| tossup_correctness | category | Religion | 358 | 0.0340741 | 0.179754 | 0.716238 | 0.540299 |
| tossup_correctness | category | Science | 1433 | 0.0304565 | 0.172931 | 0.700466 | 0.524263 |
| tossup_correctness | category | Social Science | 324 | 0.0577603 | 0.157499 | 0.775983 | 0.48501 |
| tossup_correctness | category | Unknown | 1937 | 0.0233985 | 0.167598 | 0.690239 | 0.511577 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0696519 | 0.20874 | 0.591912 | 0.61832 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0178468 | 0.173514 | 0.718292 | 0.524301 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.022394 | 0.164321 | 0.712272 | 0.502701 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0256568 | 0.156144 | 0.691736 | 0.485845 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0227654 | 0.160554 | 0.719732 | 0.492736 |
