# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.585709 |
| log_loss | 0.557552 |
| ece | 0.062671 |
| brier | 0.184132 |
| accuracy | 0.749163 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0150157 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.13552 |
| probability_p10 | 0.566359 |
| probability_p50 | 0.78315 |
| probability_p90 | 0.908746 |
| mean_predictive_variance | 0.165771 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.107017 |
| joint_tossup_event_log_loss | 7.01625 |
| buzz_position_mae | 0.16488 |
| buzz_position_median_absolute_error | 0.14928 |
| buzz_position_bias | -0.0665867 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.316841 |
| first_buzzer_mean_reciprocal_rank | 0.533133 |
| first_buzzer_log_loss | 1.73721 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.637572 |
| tossup_scorer_player_top1_accuracy | 0.281343 |
| tossup_scorer_team_top1_accuracy | 0.451812 |
| tossup_game_winner_accuracy | 0.752174 |
| tossup_game_margin_mae | 41.1641 |
| tournament_player_ppg_spearman | 0.626222 |
| tournament_player_ppg_mae | 10.149 |
| tournament_player_ppg_top10_overlap | 0.568966 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.585709 |
| neg_average_precision | 0.294011 |
| neg_precision | 0.350538 |
| neg_recall | 0.0746679 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0583656 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0885753 |
| no_buzz_calibration_error | 0.0754623 |
| no_buzz_brier | 0.0231979 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| overall | 9257 | -0.0665867 | -0.0798389 |
| Q1 (0-.2) | 183 | 0.385215 | 0.391604 |
| Q2 (.2-.4) | 955 | 0.215936 | 0.222492 |
| Q3 (.4-.6) | 2239 | 0.0578346 | 0.0602855 |
| Q4 (.6-.8) | 2875 | -0.0885403 | -0.0832279 |
| Q5 (.8-1) | 3005 | -0.255589 | -0.256369 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.062671 | 0.184132 | 0.585709 | 0.557552 |
| tossup_correctness | tier | fall | 2798 | 0.0821216 | 0.178278 | 0.574489 | 0.542424 |
| tossup_correctness | tier | nationals | 1545 | 0.0766368 | 0.199936 | 0.620141 | 0.596753 |
| tossup_correctness | tier | regionals | 2039 | 0.07401 | 0.188878 | 0.563405 | 0.569533 |
| tossup_correctness | tier | winter | 2875 | 0.0481436 | 0.177971 | 0.605366 | 0.542713 |
| tossup_correctness | category | Current Events | 129 | 0.106384 | 0.237052 | 0.524608 | 0.6775 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0607304 | 0.175815 | 0.576824 | 0.54101 |
| tossup_correctness | category | Geography | 180 | 0.0843083 | 0.2274 | 0.650999 | 0.652638 |
| tossup_correctness | category | History | 1454 | 0.0867515 | 0.194222 | 0.567048 | 0.575129 |
| tossup_correctness | category | Literature | 1435 | 0.0577276 | 0.156692 | 0.562898 | 0.503593 |
| tossup_correctness | category | Mythology | 324 | 0.0803955 | 0.173451 | 0.598583 | 0.525094 |
| tossup_correctness | category | Other Academic | 71 | 0.128021 | 0.204538 | 0.461874 | 0.621368 |
| tossup_correctness | category | Philosophy | 310 | 0.06576 | 0.180215 | 0.615323 | 0.548197 |
| tossup_correctness | category | Popular Culture | 108 | 0.231171 | 0.176926 | 0.541667 | 0.532476 |
| tossup_correctness | category | Religion | 361 | 0.0821559 | 0.195126 | 0.581568 | 0.585959 |
| tossup_correctness | category | Science | 1445 | 0.0616854 | 0.189536 | 0.592529 | 0.56687 |
| tossup_correctness | category | Social Science | 327 | 0.0406672 | 0.188952 | 0.672202 | 0.559077 |
| tossup_correctness | category | Unknown | 2039 | 0.07401 | 0.188878 | 0.563405 | 0.569533 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.155525 | 0.219467 | 0.522372 | 0.635798 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0875006 | 0.207761 | 0.566691 | 0.606563 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0659467 | 0.192921 | 0.571759 | 0.575017 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.048709 | 0.167473 | 0.610859 | 0.516026 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.071646 | 0.183861 | 0.585629 | 0.563928 |
