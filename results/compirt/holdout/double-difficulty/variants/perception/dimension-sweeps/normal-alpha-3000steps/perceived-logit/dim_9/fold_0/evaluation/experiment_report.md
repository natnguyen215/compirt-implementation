# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.567084 |
| log_loss | 0.556982 |
| ece | 0.0689743 |
| brier | 0.18199 |
| accuracy | 0.765573 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.000322754 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.115639 |
| probability_p10 | 0.610967 |
| probability_p50 | 0.810482 |
| probability_p90 | 0.907955 |
| mean_predictive_variance | 0.157376 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.169632 |
| joint_tossup_event_log_loss | 7.65912 |
| buzz_position_mae | 0.316783 |
| buzz_position_median_absolute_error | 0.313634 |
| buzz_position_bias | -0.299084 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.295858 |
| first_buzzer_mean_reciprocal_rank | 0.517833 |
| first_buzzer_log_loss | 1.762 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.605487 |
| tossup_scorer_player_top1_accuracy | 0.257962 |
| tossup_scorer_team_top1_accuracy | 0.367834 |
| tossup_game_winner_accuracy | 0.696035 |
| tossup_game_margin_mae | 44.2279 |
| tournament_player_ppg_spearman | 0.527475 |
| tournament_player_ppg_mae | 10.9961 |
| tournament_player_ppg_top10_overlap | 0.544828 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.567084 |
| neg_average_precision | 0.304003 |
| neg_precision | 0.509934 |
| neg_recall | 0.0352887 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0374919 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.203993 |
| no_buzz_calibration_error | 0.190723 |
| no_buzz_brier | 0.0565729 |
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
| overall | 9295 | -0.299084 | -0.313014 |
| Q1 (0-.2) | 197 | 0.196743 | 0.186779 |
| Q2 (.2-.4) | 985 | 0.0256164 | 0.0185647 |
| Q3 (.4-.6) | 2251 | -0.15206 | -0.154122 |
| Q4 (.6-.8) | 2866 | -0.328127 | -0.326916 |
| Q5 (.8-1) | 2996 | -0.521121 | -0.519895 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0689743 | 0.18199 | 0.567084 | 0.556982 |
| tossup_correctness | tier | fall | 2933 | 0.0584003 | 0.165859 | 0.569167 | 0.518409 |
| tossup_correctness | tier | nationals | 1584 | 0.0829468 | 0.200149 | 0.599687 | 0.591663 |
| tossup_correctness | tier | regionals | 1886 | 0.0821803 | 0.196516 | 0.529524 | 0.591979 |
| tossup_correctness | tier | winter | 2892 | 0.0653521 | 0.178931 | 0.55536 | 0.554282 |
| tossup_correctness | category | Current Events | 124 | 0.114997 | 0.188122 | 0.570586 | 0.565459 |
| tossup_correctness | category | Fine Arts | 1103 | 0.101626 | 0.19205 | 0.518283 | 0.590167 |
| tossup_correctness | category | Geography | 197 | 0.120134 | 0.228022 | 0.623427 | 0.656324 |
| tossup_correctness | category | History | 1491 | 0.0624193 | 0.171031 | 0.567084 | 0.527388 |
| tossup_correctness | category | Literature | 1472 | 0.0622859 | 0.159522 | 0.567342 | 0.507093 |
| tossup_correctness | category | Mythology | 332 | 0.0762926 | 0.15764 | 0.556452 | 0.49439 |
| tossup_correctness | category | Other Academic | 69 | 0.131481 | 0.199527 | 0.5 | 0.594498 |
| tossup_correctness | category | Philosophy | 324 | 0.051098 | 0.155646 | 0.624235 | 0.488607 |
| tossup_correctness | category | Popular Culture | 102 | 0.143754 | 0.164153 | 0.397924 | 0.516816 |
| tossup_correctness | category | Religion | 372 | 0.0731189 | 0.20562 | 0.610866 | 0.610873 |
| tossup_correctness | category | Science | 1487 | 0.0577871 | 0.179564 | 0.619167 | 0.547202 |
| tossup_correctness | category | Social Science | 336 | 0.111944 | 0.22109 | 0.537712 | 0.655993 |
| tossup_correctness | category | Unknown | 1886 | 0.0821803 | 0.196516 | 0.529524 | 0.591979 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0902737 | 0.20677 | 0.514456 | 0.607477 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0764759 | 0.195684 | 0.568812 | 0.584652 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0525333 | 0.17603 | 0.58804 | 0.537715 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0693197 | 0.171745 | 0.568471 | 0.530807 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0891936 | 0.190137 | 0.55618 | 0.584079 |
