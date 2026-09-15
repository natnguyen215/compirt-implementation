# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.634959 |
| log_loss | 0.520132 |
| ece | 0.0367107 |
| brier | 0.169207 |
| accuracy | 0.771197 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0021575 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.132128 |
| probability_p10 | 0.57673 |
| probability_p50 | 0.788293 |
| probability_p90 | 0.911199 |
| mean_predictive_variance | 0.163357 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101723 |
| joint_tossup_event_log_loss | 6.90892 |
| buzz_position_mae | 0.160406 |
| buzz_position_median_absolute_error | 0.145959 |
| buzz_position_bias | -0.0667397 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.361273 |
| first_buzzer_mean_reciprocal_rank | 0.569721 |
| first_buzzer_log_loss | 1.67062 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.645739 |
| tossup_scorer_player_top1_accuracy | 0.316951 |
| tossup_scorer_team_top1_accuracy | 0.490832 |
| tossup_game_winner_accuracy | 0.814004 |
| tossup_game_margin_mae | 33.7777 |
| tournament_player_ppg_spearman | 0.686855 |
| tournament_player_ppg_mae | 9.19128 |
| tournament_player_ppg_top10_overlap | 0.686207 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.634959 |
| neg_average_precision | 0.348932 |
| neg_precision | 0.477064 |
| neg_recall | 0.0990005 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0553962 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0900601 |
| no_buzz_calibration_error | 0.0783331 |
| no_buzz_brier | 0.0244289 |
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
| overall | 9270 | -0.0667397 | -0.0844654 |
| Q1 (0-.2) | 179 | 0.361206 | 0.358565 |
| Q2 (.2-.4) | 957 | 0.202169 | 0.199633 |
| Q3 (.4-.6) | 2203 | 0.0517542 | 0.0529529 |
| Q4 (.6-.8) | 2978 | -0.0901122 | -0.0882649 |
| Q5 (.8-1) | 2953 | -0.244656 | -0.24256 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0367107 | 0.169207 | 0.634959 | 0.520132 |
| tossup_correctness | tier | fall | 2876 | 0.0496586 | 0.164642 | 0.584777 | 0.515709 |
| tossup_correctness | tier | nationals | 1579 | 0.0633532 | 0.189292 | 0.656522 | 0.562828 |
| tossup_correctness | tier | regionals | 1990 | 0.02227 | 0.171157 | 0.647207 | 0.522533 |
| tossup_correctness | tier | winter | 2825 | 0.0244841 | 0.161255 | 0.656097 | 0.499077 |
| tossup_correctness | category | Current Events | 123 | 0.134452 | 0.189428 | 0.588775 | 0.565368 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0358497 | 0.17162 | 0.61985 | 0.527796 |
| tossup_correctness | category | Geography | 191 | 0.0336118 | 0.180306 | 0.741911 | 0.540476 |
| tossup_correctness | category | History | 1469 | 0.0474814 | 0.17574 | 0.656844 | 0.531042 |
| tossup_correctness | category | Literature | 1436 | 0.059614 | 0.153159 | 0.58352 | 0.491593 |
| tossup_correctness | category | Mythology | 325 | 0.1116 | 0.148957 | 0.609417 | 0.469194 |
| tossup_correctness | category | Other Academic | 67 | 0.16276 | 0.188037 | 0.607817 | 0.568946 |
| tossup_correctness | category | Philosophy | 322 | 0.0383246 | 0.163979 | 0.625823 | 0.508033 |
| tossup_correctness | category | Popular Culture | 100 | 0.172943 | 0.134154 | 0.543412 | 0.441977 |
| tossup_correctness | category | Religion | 365 | 0.0453322 | 0.195968 | 0.634788 | 0.57903 |
| tossup_correctness | category | Science | 1456 | 0.0424524 | 0.167591 | 0.637995 | 0.516663 |
| tossup_correctness | category | Social Science | 333 | 0.0207971 | 0.18548 | 0.659305 | 0.552846 |
| tossup_correctness | category | Unknown | 1990 | 0.02227 | 0.171157 | 0.647207 | 0.522533 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.101354 | 0.187324 | 0.618076 | 0.56335 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0606958 | 0.187825 | 0.596806 | 0.56121 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0424476 | 0.174783 | 0.621248 | 0.532137 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0332438 | 0.15956 | 0.644511 | 0.495918 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0306737 | 0.167644 | 0.647332 | 0.519661 |
