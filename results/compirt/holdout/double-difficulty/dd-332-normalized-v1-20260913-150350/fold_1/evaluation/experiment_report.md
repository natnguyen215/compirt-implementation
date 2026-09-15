# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.709295 |
| log_loss | 0.497365 |
| ece | 0.0159363 |
| brier | 0.161797 |
| accuracy | 0.772462 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0103376 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.143633 |
| probability_p10 | 0.573603 |
| probability_p50 | 0.813244 |
| probability_p90 | 0.920299 |
| mean_predictive_variance | 0.153502 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100864 |
| joint_tossup_event_log_loss | 6.5888 |
| buzz_position_mae | 0.153638 |
| buzz_position_median_absolute_error | 0.135934 |
| buzz_position_bias | -0.0525324 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.351699 |
| first_buzzer_mean_reciprocal_rank | 0.565402 |
| first_buzzer_log_loss | 1.67565 |
| first_buzzer_events | 9093 |

### Token Replay: Tossup Outcomes, Games, and Tournament PPG

These Stage-1 metrics use literal recorded tossup values, including post-neg bouncebacks and zero-point late misses. Predicted outcomes replay every token until a player reaches 0.5 buzz probability, resolve correctness at 0.5, and continue with the opponent after an early miss. Games sum replayed tossup points. Full tournament rankings pool each game's out-of-fold prediction before computing PPG and ranks.

| metric | value |
| --- | --- |
| first_buzzer_player_replay_accuracy | 0.17277 |
| first_buzzer_team_replay_accuracy | 0.408996 |
| tossup_scorer_player_replay_accuracy | 0.205411 |
| tossup_scorer_team_replay_accuracy | 0.386364 |
| tossup_game_winner_accuracy | 0.665188 |
| tossup_model_official_winner_accuracy | 0.670306 |
| tossup_game_margin_mae | 46.6775 |
| tossup_game_zero_margin_mae | 55.2922 |
| tournament_player_ppg_spearman | 0.566533 |
| tournament_player_ppg_mae | 12.9145 |
| tournament_player_ppg_top10_overlap | 0.555172 |
| tournament_player_ppg_top10_random_overlap | 0.269705 |
| tournament_player_ppg_top10_adjusted_overlap | 0.397381 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.709295 |
| neg_average_precision | 0.445851 |
| neg_precision | 0.587361 |
| neg_recall | 0.146093 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.176806 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0315763 |
| no_buzz_calibration_error | 0.0156672 |
| no_buzz_brier | 0.0174494 |
| full_pmf_max_mass_error | 5.55112e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9240 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 458 |
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
| overall | 9093 | -0.0525324 | -0.0714957 |
| Q1 (0-.2) | 167 | 0.371432 | 0.379099 |
| Q2 (.2-.4) | 912 | 0.211082 | 0.215215 |
| Q3 (.4-.6) | 2115 | 0.0607206 | 0.0582653 |
| Q4 (.6-.8) | 2844 | -0.0724907 | -0.0733128 |
| Q5 (.8-1) | 3055 | -0.21423 | -0.212341 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0159363 | 0.161797 | 0.709295 | 0.497365 |
| tossup_correctness | tier | fall | 2842 | 0.0125863 | 0.149035 | 0.729105 | 0.463802 |
| tossup_correctness | tier | nationals | 1564 | 0.0461932 | 0.179816 | 0.713759 | 0.540585 |
| tossup_correctness | tier | regionals | 1937 | 0.0247082 | 0.167794 | 0.685609 | 0.513658 |
| tossup_correctness | tier | winter | 2750 | 0.0161514 | 0.160515 | 0.700142 | 0.495993 |
| tossup_correctness | category | Current Events | 126 | 0.069468 | 0.16024 | 0.719161 | 0.492162 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0229838 | 0.151372 | 0.750431 | 0.468372 |
| tossup_correctness | category | Geography | 185 | 0.0756891 | 0.162114 | 0.797204 | 0.49496 |
| tossup_correctness | category | History | 1440 | 0.0299718 | 0.167877 | 0.707442 | 0.511331 |
| tossup_correctness | category | Literature | 1422 | 0.014449 | 0.142147 | 0.67859 | 0.450994 |
| tossup_correctness | category | Mythology | 318 | 0.0372636 | 0.15197 | 0.664922 | 0.482322 |
| tossup_correctness | category | Other Academic | 66 | 0.173056 | 0.175794 | 0.802912 | 0.519738 |
| tossup_correctness | category | Philosophy | 311 | 0.0885268 | 0.169469 | 0.725338 | 0.508792 |
| tossup_correctness | category | Popular Culture | 102 | 0.0519927 | 0.107818 | 0.52037 | 0.378202 |
| tossup_correctness | category | Religion | 358 | 0.0309507 | 0.180073 | 0.714335 | 0.541416 |
| tossup_correctness | category | Science | 1433 | 0.0374902 | 0.174346 | 0.695112 | 0.528669 |
| tossup_correctness | category | Social Science | 324 | 0.055742 | 0.160779 | 0.775207 | 0.490256 |
| tossup_correctness | category | Unknown | 1937 | 0.0247082 | 0.167794 | 0.685609 | 0.513658 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0775777 | 0.203359 | 0.619048 | 0.602752 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0238674 | 0.172739 | 0.72248 | 0.52111 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0289098 | 0.163803 | 0.714341 | 0.502311 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0179391 | 0.155741 | 0.69283 | 0.484362 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0124632 | 0.160508 | 0.717418 | 0.493196 |
