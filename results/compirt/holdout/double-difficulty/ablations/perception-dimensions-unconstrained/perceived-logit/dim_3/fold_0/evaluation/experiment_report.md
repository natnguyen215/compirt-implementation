# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.547051 |
| log_loss | 0.612538 |
| ece | 0.107105 |
| brier | 0.192045 |
| accuracy | 0.764497 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.000753093 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0901657 |
| probability_p10 | 0.745281 |
| probability_p50 | 0.89438 |
| probability_p90 | 0.952616 |
| mean_predictive_variance | 0.106108 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.172722 |
| joint_tossup_event_log_loss | 7.771 |
| buzz_position_mae | 0.338888 |
| buzz_position_median_absolute_error | 0.341908 |
| buzz_position_bias | -0.326054 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.356105 |
| first_buzzer_mean_reciprocal_rank | 0.570113 |
| first_buzzer_log_loss | 1.65542 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.626358 |
| tossup_scorer_player_top1_accuracy | 0.267304 |
| tossup_scorer_team_top1_accuracy | 0.400318 |
| tossup_game_winner_accuracy | 0.729075 |
| tossup_game_margin_mae | 42.9344 |
| tournament_player_ppg_spearman | 0.596718 |
| tournament_player_ppg_mae | 10.0456 |
| tournament_player_ppg_top10_overlap | 0.6 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.547051 |
| neg_average_precision | 0.275811 |
| neg_precision | 0.405405 |
| neg_recall | 0.00687443 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.028613 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.240581 |
| no_buzz_calibration_error | 0.227311 |
| no_buzz_brier | 0.0741429 |
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
| overall | 9295 | -0.326054 | -0.341846 |
| Q1 (0-.2) | 197 | 0.169146 | 0.162561 |
| Q2 (.2-.4) | 985 | 0.00259898 | -0.00213117 |
| Q3 (.4-.6) | 2251 | -0.173986 | -0.176499 |
| Q4 (.6-.8) | 2866 | -0.355236 | -0.354698 |
| Q5 (.8-1) | 2996 | -0.553004 | -0.558135 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.107105 | 0.192045 | 0.547051 | 0.612538 |
| tossup_correctness | tier | fall | 2933 | 0.0783577 | 0.171045 | 0.557074 | 0.545971 |
| tossup_correctness | tier | nationals | 1584 | 0.126314 | 0.215825 | 0.561381 | 0.674914 |
| tossup_correctness | tier | regionals | 1886 | 0.121272 | 0.208109 | 0.524667 | 0.657384 |
| tossup_correctness | tier | winter | 2892 | 0.121321 | 0.189842 | 0.542906 | 0.616637 |
| tossup_correctness | category | Current Events | 124 | 0.100439 | 0.198038 | 0.492196 | 0.618458 |
| tossup_correctness | category | Fine Arts | 1103 | 0.134798 | 0.202962 | 0.513996 | 0.655973 |
| tossup_correctness | category | Geography | 197 | 0.202249 | 0.253401 | 0.638578 | 0.759723 |
| tossup_correctness | category | History | 1491 | 0.08691 | 0.17712 | 0.533787 | 0.571176 |
| tossup_correctness | category | Literature | 1472 | 0.0931504 | 0.164469 | 0.54046 | 0.543389 |
| tossup_correctness | category | Mythology | 332 | 0.0891613 | 0.156163 | 0.622282 | 0.502123 |
| tossup_correctness | category | Other Academic | 69 | 0.163291 | 0.199046 | 0.461538 | 0.657872 |
| tossup_correctness | category | Philosophy | 324 | 0.0858017 | 0.164325 | 0.571429 | 0.537634 |
| tossup_correctness | category | Popular Culture | 102 | 0.119671 | 0.153173 | 0.428374 | 0.5123 |
| tossup_correctness | category | Religion | 372 | 0.162198 | 0.223991 | 0.629489 | 0.687878 |
| tossup_correctness | category | Science | 1487 | 0.103403 | 0.193526 | 0.579307 | 0.605444 |
| tossup_correctness | category | Social Science | 336 | 0.194965 | 0.245516 | 0.529068 | 0.766648 |
| tossup_correctness | category | Unknown | 1886 | 0.121272 | 0.208109 | 0.524667 | 0.657384 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.109617 | 0.205717 | 0.55756 | 0.618022 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.117352 | 0.209688 | 0.523666 | 0.652279 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0933381 | 0.185598 | 0.565023 | 0.583591 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0943329 | 0.17821 | 0.551209 | 0.572433 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.133051 | 0.203424 | 0.541452 | 0.659224 |
