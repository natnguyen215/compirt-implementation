# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710862 |
| log_loss | 0.492603 |
| ece | 0.012187 |
| brier | 0.159959 |
| accuracy | 0.773577 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00939829 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.147734 |
| probability_p10 | 0.564517 |
| probability_p50 | 0.806083 |
| probability_p90 | 0.919524 |
| mean_predictive_variance | 0.155972 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0959965 |
| joint_tossup_event_log_loss | 6.45697 |
| buzz_position_mae | 0.141967 |
| buzz_position_median_absolute_error | 0.122047 |
| buzz_position_bias | -0.0139569 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.370314 |
| first_buzzer_mean_reciprocal_rank | 0.581416 |
| first_buzzer_log_loss | 1.62552 |
| first_buzzer_events | 9257 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.22743 |
| first_buzzer_team_replay_accuracy | 0.485928 |
| tossup_scorer_player_replay_accuracy | 0.238889 |
| tossup_scorer_team_replay_accuracy | 0.439744 |
| tossup_game_winner_accuracy | 0.687912 |
| tossup_model_official_winner_accuracy | 0.707792 |
| tossup_game_margin_mae | 49.4444 |
| tossup_game_zero_margin_mae | 58.4615 |
| tournament_player_ppg_spearman | 0.606732 |
| tournament_player_ppg_mae | 12.256 |
| tournament_player_ppg_top10_overlap | 0.575862 |
| tournament_player_ppg_top10_random_overlap | 0.280534 |
| tournament_player_ppg_top10_adjusted_overlap | 0.416166 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710862 |
| neg_average_precision | 0.450857 |
| neg_precision | 0.57645 |
| neg_recall | 0.150252 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.176219 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.019968 |
| no_buzz_calibration_error | 0.00685501 |
| no_buzz_brier | 0.0134646 |
| full_pmf_max_mass_error | 6.66134e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9360 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 462 |
| first_buzzer_player_replay_accuracy_events | 9238 |
| first_buzzer_team_replay_accuracy_events | 9238 |
| tossup_scorer_player_replay_accuracy_events | 9360 |
| tossup_scorer_team_replay_accuracy_events | 9360 |
| tossup_game_winner_accuracy_games | 455 |
| tossup_game_margin_mae_games | 468 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 1 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0139569 | -0.0366617 |
| Q1 (0-.2) | 183 | 0.406972 | 0.425129 |
| Q2 (.2-.4) | 955 | 0.235948 | 0.231489 |
| Q3 (.4-.6) | 2239 | 0.0854071 | 0.0822993 |
| Q4 (.6-.8) | 2875 | -0.0398834 | -0.0416786 |
| Q5 (.8-1) | 3005 | -0.168242 | -0.163326 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in the diagnostic CSVs under `csvs/`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.012187 | 0.159959 | 0.710862 | 0.492603 |
| tossup_correctness | tier | fall | 2798 | 0.024444 | 0.146377 | 0.735842 | 0.45828 |
| tossup_correctness | tier | nationals | 1545 | 0.0381615 | 0.177837 | 0.7115 | 0.535307 |
| tossup_correctness | tier | regionals | 2039 | 0.0165519 | 0.162697 | 0.698895 | 0.500281 |
| tossup_correctness | tier | winter | 2875 | 0.0174832 | 0.161626 | 0.69344 | 0.497611 |
| tossup_correctness | category | Current Events | 129 | 0.0954574 | 0.208371 | 0.677664 | 0.612748 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0260815 | 0.152836 | 0.710532 | 0.476718 |
| tossup_correctness | category | Geography | 180 | 0.0769573 | 0.190427 | 0.759499 | 0.563273 |
| tossup_correctness | category | History | 1454 | 0.0263782 | 0.167829 | 0.689439 | 0.512701 |
| tossup_correctness | category | Literature | 1435 | 0.0213322 | 0.135527 | 0.723044 | 0.433993 |
| tossup_correctness | category | Mythology | 324 | 0.0541898 | 0.150967 | 0.697892 | 0.471901 |
| tossup_correctness | category | Other Academic | 71 | 0.136893 | 0.1746 | 0.642702 | 0.534653 |
| tossup_correctness | category | Philosophy | 310 | 0.0270972 | 0.16143 | 0.712552 | 0.494238 |
| tossup_correctness | category | Popular Culture | 108 | 0.0837751 | 0.10826 | 0.50434 | 0.377261 |
| tossup_correctness | category | Religion | 361 | 0.0372943 | 0.174171 | 0.695835 | 0.526908 |
| tossup_correctness | category | Science | 1445 | 0.0303961 | 0.167713 | 0.717266 | 0.508163 |
| tossup_correctness | category | Social Science | 327 | 0.0542267 | 0.174078 | 0.747734 | 0.519719 |
| tossup_correctness | category | Unknown | 2039 | 0.0165519 | 0.162697 | 0.698895 | 0.500281 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0777469 | 0.179156 | 0.67694 | 0.534112 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0287721 | 0.171769 | 0.723739 | 0.521376 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0184199 | 0.162172 | 0.721604 | 0.496933 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0162018 | 0.152478 | 0.701249 | 0.473921 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0258011 | 0.160544 | 0.706882 | 0.495578 |
