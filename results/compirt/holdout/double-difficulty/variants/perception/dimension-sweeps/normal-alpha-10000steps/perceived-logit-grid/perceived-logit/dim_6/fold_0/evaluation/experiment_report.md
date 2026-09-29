# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.600645 |
| log_loss | 0.577217 |
| ece | 0.106681 |
| brier | 0.188841 |
| accuracy | 0.741044 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0242066 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.16518 |
| probability_p10 | 0.478315 |
| probability_p50 | 0.712921 |
| probability_p90 | 0.915143 |
| mean_predictive_variance | 0.182477 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.115174 |
| joint_tossup_event_log_loss | 6.89459 |
| buzz_position_mae | 0.188863 |
| buzz_position_median_absolute_error | 0.167143 |
| buzz_position_bias | -0.125608 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.391716 |
| first_buzzer_mean_reciprocal_rank | 0.596336 |
| first_buzzer_log_loss | 1.60121 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.653577 |
| tossup_scorer_player_top1_accuracy | 0.31104 |
| tossup_scorer_team_top1_accuracy | 0.453397 |
| tossup_game_winner_accuracy | 0.777533 |
| tossup_game_margin_mae | 37.4995 |
| tournament_player_ppg_spearman | 0.554747 |
| tournament_player_ppg_mae | 10.6301 |
| tournament_player_ppg_top10_overlap | 0.575862 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.600645 |
| neg_average_precision | 0.331983 |
| neg_precision | 0.4 |
| neg_recall | 0.206233 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.100259 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0987895 |
| no_buzz_calibration_error | 0.0855198 |
| no_buzz_brier | 0.0297298 |
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
| overall | 9295 | -0.125608 | -0.132538 |
| Q1 (0-.2) | 197 | 0.289156 | 0.272352 |
| Q2 (.2-.4) | 985 | 0.133964 | 0.118258 |
| Q3 (.4-.6) | 2251 | -0.0181301 | -0.030461 |
| Q4 (.6-.8) | 2866 | -0.154062 | -0.164136 |
| Q5 (.8-1) | 2996 | -0.291754 | -0.286876 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.106681 | 0.188841 | 0.600645 | 0.577217 |
| tossup_correctness | tier | fall | 2933 | 0.111843 | 0.177658 | 0.567883 | 0.559236 |
| tossup_correctness | tier | nationals | 1584 | 0.107573 | 0.209642 | 0.605219 | 0.610622 |
| tossup_correctness | tier | regionals | 1886 | 0.107651 | 0.199456 | 0.610902 | 0.594026 |
| tossup_correctness | tier | winter | 2892 | 0.105289 | 0.181866 | 0.59914 | 0.566195 |
| tossup_correctness | category | Current Events | 124 | 0.138024 | 0.203815 | 0.532431 | 0.621922 |
| tossup_correctness | category | Fine Arts | 1103 | 0.146739 | 0.203503 | 0.539618 | 0.630631 |
| tossup_correctness | category | Geography | 197 | 0.135903 | 0.231768 | 0.575291 | 0.676325 |
| tossup_correctness | category | History | 1491 | 0.103144 | 0.173846 | 0.61483 | 0.539252 |
| tossup_correctness | category | Literature | 1472 | 0.107721 | 0.171801 | 0.585964 | 0.544318 |
| tossup_correctness | category | Mythology | 332 | 0.147389 | 0.174019 | 0.596655 | 0.533466 |
| tossup_correctness | category | Other Academic | 69 | 0.192797 | 0.231035 | 0.473982 | 0.66512 |
| tossup_correctness | category | Philosophy | 324 | 0.117533 | 0.167476 | 0.667716 | 0.51299 |
| tossup_correctness | category | Popular Culture | 102 | 0.1689 | 0.186298 | 0.473356 | 0.563203 |
| tossup_correctness | category | Religion | 372 | 0.0636777 | 0.198503 | 0.652252 | 0.593986 |
| tossup_correctness | category | Science | 1487 | 0.0852875 | 0.185164 | 0.626425 | 0.564065 |
| tossup_correctness | category | Social Science | 336 | 0.123466 | 0.224541 | 0.550127 | 0.676521 |
| tossup_correctness | category | Unknown | 1886 | 0.107651 | 0.199456 | 0.610902 | 0.594026 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.214853 | 0.248164 | 0.500133 | 0.703206 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.159271 | 0.216298 | 0.598654 | 0.628025 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.131808 | 0.192105 | 0.613026 | 0.573863 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.117244 | 0.18066 | 0.60057 | 0.556208 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0554011 | 0.181285 | 0.614664 | 0.574845 |
