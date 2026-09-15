# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.632494 |
| log_loss | 0.574484 |
| ece | 0.130748 |
| brier | 0.193433 |
| accuracy | 0.717267 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0479828 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.16057 |
| probability_p10 | 0.423548 |
| probability_p50 | 0.654425 |
| probability_p90 | 0.84475 |
| mean_predictive_variance | 0.203766 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101603 |
| joint_tossup_event_log_loss | 6.67296 |
| buzz_position_mae | 0.165568 |
| buzz_position_median_absolute_error | 0.147472 |
| buzz_position_bias | -0.0817901 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.408714 |
| first_buzzer_mean_reciprocal_rank | 0.607873 |
| first_buzzer_log_loss | 1.57836 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.661323 |
| tossup_scorer_player_top1_accuracy | 0.300637 |
| tossup_scorer_team_top1_accuracy | 0.421231 |
| tossup_game_winner_accuracy | 0.773128 |
| tossup_game_margin_mae | 37.5258 |
| tournament_player_ppg_spearman | 0.620207 |
| tournament_player_ppg_mae | 10.9204 |
| tournament_player_ppg_top10_overlap | 0.641379 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.632494 |
| neg_average_precision | 0.342979 |
| neg_precision | 0.377875 |
| neg_recall | 0.316224 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.100251 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0783983 |
| no_buzz_calibration_error | 0.0651286 |
| no_buzz_brier | 0.025895 |
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
| overall | 9295 | -0.0817901 | -0.0963057 |
| Q1 (0-.2) | 197 | 0.32982 | 0.335467 |
| Q2 (.2-.4) | 985 | 0.174713 | 0.165885 |
| Q3 (.4-.6) | 2251 | 0.0274746 | 0.0230584 |
| Q4 (.6-.8) | 2866 | -0.107736 | -0.110505 |
| Q5 (.8-1) | 2996 | -0.250461 | -0.245838 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.130748 | 0.193433 | 0.632494 | 0.574484 |
| tossup_correctness | tier | fall | 2933 | 0.120288 | 0.178034 | 0.630056 | 0.541055 |
| tossup_correctness | tier | nationals | 1584 | 0.126432 | 0.216392 | 0.603441 | 0.622981 |
| tossup_correctness | tier | regionals | 1886 | 0.136271 | 0.205941 | 0.615061 | 0.60259 |
| tossup_correctness | tier | winter | 2892 | 0.140118 | 0.188319 | 0.649529 | 0.563497 |
| tossup_correctness | category | Current Events | 124 | 0.113405 | 0.197337 | 0.587929 | 0.5956 |
| tossup_correctness | category | Fine Arts | 1103 | 0.146248 | 0.202624 | 0.601941 | 0.598671 |
| tossup_correctness | category | Geography | 197 | 0.114045 | 0.217355 | 0.641725 | 0.634246 |
| tossup_correctness | category | History | 1491 | 0.130558 | 0.176603 | 0.670293 | 0.537777 |
| tossup_correctness | category | Literature | 1472 | 0.144944 | 0.18302 | 0.611422 | 0.550787 |
| tossup_correctness | category | Mythology | 332 | 0.193311 | 0.183238 | 0.663381 | 0.549151 |
| tossup_correctness | category | Other Academic | 69 | 0.164413 | 0.227106 | 0.533937 | 0.642595 |
| tossup_correctness | category | Philosophy | 324 | 0.163175 | 0.185248 | 0.656311 | 0.554115 |
| tossup_correctness | category | Popular Culture | 102 | 0.197825 | 0.19635 | 0.547405 | 0.574179 |
| tossup_correctness | category | Religion | 372 | 0.0898055 | 0.198289 | 0.681503 | 0.580249 |
| tossup_correctness | category | Science | 1487 | 0.097716 | 0.191138 | 0.641142 | 0.566394 |
| tossup_correctness | category | Social Science | 336 | 0.116301 | 0.212837 | 0.622203 | 0.621407 |
| tossup_correctness | category | Unknown | 1886 | 0.136271 | 0.205941 | 0.615061 | 0.60259 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.27662 | 0.26828 | 0.632891 | 0.73492 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.215429 | 0.232099 | 0.658295 | 0.655453 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.180884 | 0.204647 | 0.645132 | 0.59663 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.131924 | 0.182242 | 0.641844 | 0.548977 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0568621 | 0.17808 | 0.640048 | 0.545077 |
