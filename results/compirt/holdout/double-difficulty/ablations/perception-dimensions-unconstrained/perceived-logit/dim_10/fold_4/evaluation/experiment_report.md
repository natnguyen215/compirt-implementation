# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.571535 |
| log_loss | 0.544391 |
| ece | 0.0688023 |
| brier | 0.177629 |
| accuracy | 0.771953 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.00140237 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.118077 |
| probability_p10 | 0.596212 |
| probability_p50 | 0.791447 |
| probability_p90 | 0.901339 |
| mean_predictive_variance | 0.164782 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.169219 |
| joint_tossup_event_log_loss | 7.65426 |
| buzz_position_mae | 0.313901 |
| buzz_position_median_absolute_error | 0.310163 |
| buzz_position_bias | -0.295322 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.30151 |
| first_buzzer_mean_reciprocal_rank | 0.51494 |
| first_buzzer_log_loss | 1.78419 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.610572 |
| tossup_scorer_player_top1_accuracy | 0.245736 |
| tossup_scorer_team_top1_accuracy | 0.359915 |
| tossup_game_winner_accuracy | 0.693654 |
| tossup_game_margin_mae | 47.0903 |
| tournament_player_ppg_spearman | 0.532651 |
| tournament_player_ppg_mae | 11.5462 |
| tournament_player_ppg_top10_overlap | 0.568966 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.571535 |
| neg_average_precision | 0.295608 |
| neg_precision | 0.464481 |
| neg_recall | 0.0404569 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0390128 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.198155 |
| no_buzz_calibration_error | 0.186428 |
| no_buzz_brier | 0.0537891 |
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
| overall | 9270 | -0.295322 | -0.309392 |
| Q1 (0-.2) | 179 | 0.197035 | 0.196432 |
| Q2 (.2-.4) | 957 | 0.0374289 | 0.0361411 |
| Q3 (.4-.6) | 2203 | -0.146222 | -0.149269 |
| Q4 (.6-.8) | 2978 | -0.323117 | -0.323109 |
| Q5 (.8-1) | 2953 | -0.516206 | -0.513343 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0688023 | 0.177629 | 0.571535 | 0.544391 |
| tossup_correctness | tier | fall | 2876 | 0.0528253 | 0.165927 | 0.558639 | 0.51893 |
| tossup_correctness | tier | nationals | 1579 | 0.092615 | 0.199115 | 0.61341 | 0.587132 |
| tossup_correctness | tier | regionals | 1990 | 0.0910679 | 0.186149 | 0.543234 | 0.564777 |
| tossup_correctness | tier | winter | 2825 | 0.0576139 | 0.17153 | 0.563419 | 0.532061 |
| tossup_correctness | category | Current Events | 123 | 0.0606801 | 0.170717 | 0.656273 | 0.520662 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0623974 | 0.177264 | 0.58204 | 0.544869 |
| tossup_correctness | category | Geography | 191 | 0.0694632 | 0.199526 | 0.678223 | 0.586069 |
| tossup_correctness | category | History | 1469 | 0.0540611 | 0.182237 | 0.591575 | 0.552562 |
| tossup_correctness | category | Literature | 1436 | 0.0865568 | 0.160071 | 0.525714 | 0.509672 |
| tossup_correctness | category | Mythology | 325 | 0.0638947 | 0.135933 | 0.610849 | 0.439736 |
| tossup_correctness | category | Other Academic | 67 | 0.155146 | 0.174536 | 0.597035 | 0.53553 |
| tossup_correctness | category | Philosophy | 322 | 0.0923708 | 0.180595 | 0.490749 | 0.562465 |
| tossup_correctness | category | Popular Culture | 100 | 0.109823 | 0.119848 | 0.558733 | 0.402088 |
| tossup_correctness | category | Religion | 365 | 0.0816327 | 0.201858 | 0.591247 | 0.601924 |
| tossup_correctness | category | Science | 1456 | 0.055767 | 0.17774 | 0.589997 | 0.54145 |
| tossup_correctness | category | Social Science | 333 | 0.0867905 | 0.202034 | 0.555738 | 0.598506 |
| tossup_correctness | category | Unknown | 1990 | 0.0910679 | 0.186149 | 0.543234 | 0.564777 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0966693 | 0.194993 | 0.532172 | 0.581935 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0824912 | 0.193225 | 0.527265 | 0.578948 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0692472 | 0.183004 | 0.555006 | 0.554936 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0621491 | 0.166849 | 0.592625 | 0.51698 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0721731 | 0.178382 | 0.575597 | 0.550692 |
