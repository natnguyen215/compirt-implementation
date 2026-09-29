# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.630389 |
| log_loss | 0.589475 |
| ece | 0.154242 |
| brier | 0.20103 |
| accuracy | 0.69575 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0694997 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.154909 |
| probability_p10 | 0.403647 |
| probability_p50 | 0.61964 |
| probability_p90 | 0.812749 |
| mean_predictive_variance | 0.213093 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100797 |
| joint_tossup_event_log_loss | 6.67161 |
| buzz_position_mae | 0.164932 |
| buzz_position_median_absolute_error | 0.147615 |
| buzz_position_bias | -0.0781859 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.400538 |
| first_buzzer_mean_reciprocal_rank | 0.604493 |
| first_buzzer_log_loss | 1.57919 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.657343 |
| tossup_scorer_player_top1_accuracy | 0.291826 |
| tossup_scorer_team_top1_accuracy | 0.386093 |
| tossup_game_winner_accuracy | 0.773128 |
| tossup_game_margin_mae | 38.1182 |
| tournament_player_ppg_spearman | 0.62756 |
| tournament_player_ppg_mae | 11.4443 |
| tournament_player_ppg_top10_overlap | 0.644828 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.630389 |
| neg_average_precision | 0.340182 |
| neg_precision | 0.356061 |
| neg_recall | 0.366178 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0988873 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0849782 |
| no_buzz_calibration_error | 0.0717085 |
| no_buzz_brier | 0.0278234 |
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
| overall | 9295 | -0.0781859 | -0.092401 |
| Q1 (0-.2) | 197 | 0.333826 | 0.33501 |
| Q2 (.2-.4) | 985 | 0.181084 | 0.1705 |
| Q3 (.4-.6) | 2251 | 0.0334258 | 0.0284656 |
| Q4 (.6-.8) | 2866 | -0.102889 | -0.104917 |
| Q5 (.8-1) | 2996 | -0.250745 | -0.248438 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.154242 | 0.20103 | 0.630389 | 0.589475 |
| tossup_correctness | tier | fall | 2933 | 0.145424 | 0.186913 | 0.623173 | 0.559303 |
| tossup_correctness | tier | nationals | 1584 | 0.154882 | 0.222342 | 0.607219 | 0.635558 |
| tossup_correctness | tier | regionals | 1886 | 0.15329 | 0.211688 | 0.609963 | 0.612991 |
| tossup_correctness | tier | winter | 2892 | 0.163454 | 0.196723 | 0.650256 | 0.579498 |
| tossup_correctness | category | Current Events | 124 | 0.154388 | 0.201997 | 0.605966 | 0.596226 |
| tossup_correctness | category | Fine Arts | 1103 | 0.180097 | 0.212191 | 0.611379 | 0.616002 |
| tossup_correctness | category | Geography | 197 | 0.0914453 | 0.220249 | 0.63951 | 0.635321 |
| tossup_correctness | category | History | 1491 | 0.155248 | 0.18289 | 0.674614 | 0.550636 |
| tossup_correctness | category | Literature | 1472 | 0.168361 | 0.191705 | 0.608319 | 0.568552 |
| tossup_correctness | category | Mythology | 332 | 0.240016 | 0.207007 | 0.63405 | 0.600113 |
| tossup_correctness | category | Other Academic | 69 | 0.21441 | 0.231516 | 0.574661 | 0.651941 |
| tossup_correctness | category | Philosophy | 324 | 0.201611 | 0.19669 | 0.66338 | 0.579261 |
| tossup_correctness | category | Popular Culture | 102 | 0.238443 | 0.213361 | 0.50173 | 0.614041 |
| tossup_correctness | category | Religion | 372 | 0.126091 | 0.208139 | 0.65881 | 0.602326 |
| tossup_correctness | category | Science | 1487 | 0.119415 | 0.196508 | 0.639604 | 0.577981 |
| tossup_correctness | category | Social Science | 336 | 0.115001 | 0.2147 | 0.62572 | 0.620726 |
| tossup_correctness | category | Unknown | 1886 | 0.15329 | 0.211688 | 0.609963 | 0.612991 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.312148 | 0.28434 | 0.632891 | 0.771207 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.246832 | 0.245288 | 0.661359 | 0.684542 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.206939 | 0.215152 | 0.638298 | 0.619123 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.153479 | 0.188031 | 0.646883 | 0.561164 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.07668 | 0.182825 | 0.632134 | 0.551076 |
