# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.659012 |
| log_loss | 0.516565 |
| ece | 0.01736 |
| brier | 0.168993 |
| accuracy | 0.766771 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00259263 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.117815 |
| probability_p10 | 0.600709 |
| probability_p50 | 0.786989 |
| probability_p90 | 0.898286 |
| mean_predictive_variance | 0.165847 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101194 |
| joint_tossup_event_log_loss | 6.86935 |
| buzz_position_mae | 0.159663 |
| buzz_position_median_absolute_error | 0.143642 |
| buzz_position_bias | -0.064724 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.357567 |
| first_buzzer_mean_reciprocal_rank | 0.571724 |
| first_buzzer_log_loss | 1.64526 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.658421 |
| tossup_scorer_player_top1_accuracy | 0.326333 |
| tossup_scorer_team_top1_accuracy | 0.498401 |
| tossup_game_winner_accuracy | 0.8 |
| tossup_game_margin_mae | 35.8475 |
| tournament_player_ppg_spearman | 0.706693 |
| tournament_player_ppg_mae | 8.59415 |
| tournament_player_ppg_top10_overlap | 0.662069 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.659012 |
| neg_average_precision | 0.382332 |
| neg_precision | 0.544444 |
| neg_recall | 0.0673385 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0566213 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0965508 |
| no_buzz_calibration_error | 0.0834378 |
| no_buzz_brier | 0.0268657 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9257 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 460 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.064724 | -0.0802399 |
| Q1 (0-.2) | 183 | 0.376355 | 0.385931 |
| Q2 (.2-.4) | 955 | 0.206543 | 0.209141 |
| Q3 (.4-.6) | 2239 | 0.0520763 | 0.0536022 |
| Q4 (.6-.8) | 2875 | -0.0864678 | -0.0818275 |
| Q5 (.8-1) | 3005 | -0.244019 | -0.244044 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.01736 | 0.168993 | 0.659012 | 0.516565 |
| tossup_correctness | tier | fall | 2798 | 0.0126126 | 0.155613 | 0.682118 | 0.483504 |
| tossup_correctness | tier | nationals | 1545 | 0.0528352 | 0.190363 | 0.666799 | 0.565052 |
| tossup_correctness | tier | regionals | 2039 | 0.0316277 | 0.175648 | 0.615627 | 0.53451 |
| tossup_correctness | tier | winter | 2875 | 0.0287262 | 0.16581 | 0.662722 | 0.509957 |
| tossup_correctness | category | Current Events | 129 | 0.0540585 | 0.211714 | 0.651433 | 0.612909 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0417551 | 0.16626 | 0.654362 | 0.509397 |
| tossup_correctness | category | Geography | 180 | 0.0830825 | 0.204036 | 0.734691 | 0.59828 |
| tossup_correctness | category | History | 1454 | 0.0319773 | 0.171297 | 0.66161 | 0.521125 |
| tossup_correctness | category | Literature | 1435 | 0.0307549 | 0.146147 | 0.642779 | 0.466034 |
| tossup_correctness | category | Mythology | 324 | 0.0446027 | 0.15689 | 0.652303 | 0.48837 |
| tossup_correctness | category | Other Academic | 71 | 0.0976915 | 0.200048 | 0.394336 | 0.592521 |
| tossup_correctness | category | Philosophy | 310 | 0.0339342 | 0.16953 | 0.679455 | 0.512822 |
| tossup_correctness | category | Popular Culture | 108 | 0.132537 | 0.119757 | 0.564236 | 0.404359 |
| tossup_correctness | category | Religion | 361 | 0.0380725 | 0.178846 | 0.665704 | 0.538444 |
| tossup_correctness | category | Science | 1445 | 0.0354117 | 0.173325 | 0.693594 | 0.523626 |
| tossup_correctness | category | Social Science | 327 | 0.0331025 | 0.18132 | 0.698936 | 0.543388 |
| tossup_correctness | category | Unknown | 2039 | 0.0316277 | 0.175648 | 0.615627 | 0.53451 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0836415 | 0.190916 | 0.609981 | 0.569086 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0251548 | 0.185087 | 0.662373 | 0.554047 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.00822402 | 0.170985 | 0.681743 | 0.519121 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0225192 | 0.158865 | 0.651632 | 0.492515 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0281906 | 0.170749 | 0.648014 | 0.52256 |
