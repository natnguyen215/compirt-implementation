# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.541251 |
| log_loss | 0.603626 |
| ece | 0.0975108 |
| brier | 0.190663 |
| accuracy | 0.763959 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.00129102 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0978194 |
| probability_p10 | 0.716799 |
| probability_p50 | 0.882088 |
| probability_p90 | 0.947906 |
| mean_predictive_variance | 0.114835 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.172061 |
| joint_tossup_event_log_loss | 7.73115 |
| buzz_position_mae | 0.336909 |
| buzz_position_median_absolute_error | 0.338166 |
| buzz_position_bias | -0.323691 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.366541 |
| first_buzzer_mean_reciprocal_rank | 0.578021 |
| first_buzzer_log_loss | 1.63446 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.62496 |
| tossup_scorer_player_top1_accuracy | 0.270382 |
| tossup_scorer_team_top1_accuracy | 0.400425 |
| tossup_game_winner_accuracy | 0.711454 |
| tossup_game_margin_mae | 43.3735 |
| tournament_player_ppg_spearman | 0.591695 |
| tournament_player_ppg_mae | 10.0468 |
| tournament_player_ppg_top10_overlap | 0.603448 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.541251 |
| neg_average_precision | 0.274456 |
| neg_precision | 0.403226 |
| neg_recall | 0.0114574 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0294529 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.239375 |
| no_buzz_calibration_error | 0.226105 |
| no_buzz_brier | 0.0735066 |
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
| overall | 9295 | -0.323691 | -0.338166 |
| Q1 (0-.2) | 197 | 0.172092 | 0.165971 |
| Q2 (.2-.4) | 985 | 0.00408844 | -0.0021959 |
| Q3 (.4-.6) | 2251 | -0.171737 | -0.173547 |
| Q4 (.6-.8) | 2866 | -0.35238 | -0.351684 |
| Q5 (.8-1) | 2996 | -0.550781 | -0.555293 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0975108 | 0.190663 | 0.541251 | 0.603626 |
| tossup_correctness | tier | fall | 2933 | 0.0764766 | 0.171568 | 0.545083 | 0.546105 |
| tossup_correctness | tier | nationals | 1584 | 0.103866 | 0.211393 | 0.562128 | 0.647904 |
| tossup_correctness | tier | regionals | 1886 | 0.112936 | 0.205013 | 0.527035 | 0.64186 |
| tossup_correctness | tier | winter | 2892 | 0.112815 | 0.189316 | 0.523028 | 0.612775 |
| tossup_correctness | category | Current Events | 124 | 0.131297 | 0.199513 | 0.491502 | 0.615152 |
| tossup_correctness | category | Fine Arts | 1103 | 0.137608 | 0.202575 | 0.50082 | 0.650169 |
| tossup_correctness | category | Geography | 197 | 0.197694 | 0.247923 | 0.651399 | 0.735173 |
| tossup_correctness | category | History | 1491 | 0.0736427 | 0.175339 | 0.539581 | 0.558136 |
| tossup_correctness | category | Literature | 1472 | 0.087305 | 0.164968 | 0.532162 | 0.541406 |
| tossup_correctness | category | Mythology | 332 | 0.0954997 | 0.155128 | 0.621864 | 0.496171 |
| tossup_correctness | category | Other Academic | 69 | 0.135886 | 0.197498 | 0.477376 | 0.643455 |
| tossup_correctness | category | Philosophy | 324 | 0.0837299 | 0.16467 | 0.549569 | 0.538355 |
| tossup_correctness | category | Popular Culture | 102 | 0.0660052 | 0.151166 | 0.413149 | 0.507453 |
| tossup_correctness | category | Religion | 372 | 0.157424 | 0.220488 | 0.61767 | 0.673708 |
| tossup_correctness | category | Science | 1487 | 0.0875068 | 0.192853 | 0.559649 | 0.601524 |
| tossup_correctness | category | Social Science | 336 | 0.182667 | 0.242788 | 0.517331 | 0.751122 |
| tossup_correctness | category | Unknown | 1886 | 0.112936 | 0.205013 | 0.527035 | 0.64186 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.113686 | 0.203858 | 0.54443 | 0.612645 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0956701 | 0.20781 | 0.517231 | 0.640847 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0856107 | 0.18463 | 0.558104 | 0.576628 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0853853 | 0.176887 | 0.55119 | 0.563593 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.123033 | 0.201868 | 0.530105 | 0.649374 |
