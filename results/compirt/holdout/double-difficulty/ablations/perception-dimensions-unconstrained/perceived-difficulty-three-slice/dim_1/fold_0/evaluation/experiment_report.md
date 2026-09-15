# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.584548 |
| log_loss | 0.555323 |
| ece | 0.0592346 |
| brier | 0.182609 |
| accuracy | 0.75234 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0129102 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.134187 |
| probability_p10 | 0.574852 |
| probability_p50 | 0.784902 |
| probability_p90 | 0.908821 |
| mean_predictive_variance | 0.16475 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.106253 |
| joint_tossup_event_log_loss | 7.00722 |
| buzz_position_mae | 0.165263 |
| buzz_position_median_absolute_error | 0.151709 |
| buzz_position_bias | -0.0653575 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.310382 |
| first_buzzer_mean_reciprocal_rank | 0.529755 |
| first_buzzer_log_loss | 1.74427 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.625282 |
| tossup_scorer_player_top1_accuracy | 0.280998 |
| tossup_scorer_team_top1_accuracy | 0.452017 |
| tossup_game_winner_accuracy | 0.755507 |
| tossup_game_margin_mae | 38.3976 |
| tournament_player_ppg_spearman | 0.603059 |
| tournament_player_ppg_mae | 10.1489 |
| tournament_player_ppg_top10_overlap | 0.572414 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.584548 |
| neg_average_precision | 0.301987 |
| neg_precision | 0.374477 |
| neg_recall | 0.0820348 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0576906 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.089322 |
| no_buzz_calibration_error | 0.0760524 |
| no_buzz_brier | 0.0237963 |
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
| overall | 9295 | -0.0653575 | -0.0814343 |
| Q1 (0-.2) | 197 | 0.365688 | 0.365245 |
| Q2 (.2-.4) | 985 | 0.213208 | 0.210354 |
| Q3 (.4-.6) | 2251 | 0.0579488 | 0.0581296 |
| Q4 (.6-.8) | 2866 | -0.0908453 | -0.0870925 |
| Q5 (.8-1) | 2996 | -0.253548 | -0.252923 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0592346 | 0.182609 | 0.584548 | 0.555323 |
| tossup_correctness | tier | fall | 2933 | 0.0834035 | 0.174536 | 0.577039 | 0.534739 |
| tossup_correctness | tier | nationals | 1584 | 0.0744352 | 0.200785 | 0.611972 | 0.604601 |
| tossup_correctness | tier | regionals | 1886 | 0.0648137 | 0.193639 | 0.576398 | 0.577042 |
| tossup_correctness | tier | winter | 2892 | 0.0474241 | 0.173648 | 0.595371 | 0.535044 |
| tossup_correctness | category | Current Events | 124 | 0.127155 | 0.199242 | 0.608394 | 0.588861 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0640686 | 0.186892 | 0.560706 | 0.573342 |
| tossup_correctness | category | Geography | 197 | 0.0789695 | 0.197643 | 0.699883 | 0.574418 |
| tossup_correctness | category | History | 1491 | 0.0688482 | 0.171657 | 0.610526 | 0.524891 |
| tossup_correctness | category | Literature | 1472 | 0.0772065 | 0.165051 | 0.52993 | 0.527285 |
| tossup_correctness | category | Mythology | 332 | 0.0958784 | 0.161674 | 0.613799 | 0.497647 |
| tossup_correctness | category | Other Academic | 69 | 0.124726 | 0.17953 | 0.558824 | 0.553592 |
| tossup_correctness | category | Philosophy | 324 | 0.0470234 | 0.162756 | 0.570359 | 0.511202 |
| tossup_correctness | category | Popular Culture | 102 | 0.253345 | 0.215338 | 0.468512 | 0.624663 |
| tossup_correctness | category | Religion | 372 | 0.0677956 | 0.203781 | 0.630647 | 0.60052 |
| tossup_correctness | category | Science | 1487 | 0.0549631 | 0.18469 | 0.599932 | 0.556992 |
| tossup_correctness | category | Social Science | 336 | 0.0725567 | 0.215076 | 0.574619 | 0.629972 |
| tossup_correctness | category | Unknown | 1886 | 0.0648137 | 0.193639 | 0.576398 | 0.577042 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.119573 | 0.216605 | 0.562997 | 0.629342 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0948063 | 0.210017 | 0.541167 | 0.614343 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0683456 | 0.182404 | 0.577138 | 0.5507 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0353431 | 0.167348 | 0.614203 | 0.516569 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0669105 | 0.186116 | 0.592219 | 0.571597 |
