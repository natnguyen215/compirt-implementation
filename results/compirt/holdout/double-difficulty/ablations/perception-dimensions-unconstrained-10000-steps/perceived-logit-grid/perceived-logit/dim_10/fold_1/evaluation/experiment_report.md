# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.629434 |
| log_loss | 0.586434 |
| ece | 0.144918 |
| brier | 0.200051 |
| accuracy | 0.69647 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0656549 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.154384 |
| probability_p10 | 0.411833 |
| probability_p50 | 0.626171 |
| probability_p90 | 0.816439 |
| mean_predictive_variance | 0.211946 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100554 |
| joint_tossup_event_log_loss | 6.65305 |
| buzz_position_mae | 0.164387 |
| buzz_position_median_absolute_error | 0.145361 |
| buzz_position_bias | -0.0811764 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.39261 |
| first_buzzer_mean_reciprocal_rank | 0.597073 |
| first_buzzer_log_loss | 1.5952 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.65347 |
| tossup_scorer_player_top1_accuracy | 0.289502 |
| tossup_scorer_team_top1_accuracy | 0.39026 |
| tossup_game_winner_accuracy | 0.77027 |
| tossup_game_margin_mae | 38.5933 |
| tournament_player_ppg_spearman | 0.637901 |
| tournament_player_ppg_mae | 11.3798 |
| tournament_player_ppg_top10_overlap | 0.641379 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.629434 |
| neg_average_precision | 0.335264 |
| neg_precision | 0.356421 |
| neg_recall | 0.34258 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.100521 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0847308 |
| no_buzz_calibration_error | 0.0688217 |
| no_buzz_brier | 0.0293392 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0811764 | -0.094871 |
| Q1 (0-.2) | 167 | 0.342268 | 0.356237 |
| Q2 (.2-.4) | 912 | 0.184391 | 0.186791 |
| Q3 (.4-.6) | 2115 | 0.0360887 | 0.0341374 |
| Q4 (.6-.8) | 2844 | -0.0966904 | -0.0995631 |
| Q5 (.8-1) | 3055 | -0.250344 | -0.247758 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.144918 | 0.200051 | 0.629434 | 0.586434 |
| tossup_correctness | tier | fall | 2842 | 0.13158 | 0.183757 | 0.637083 | 0.549762 |
| tossup_correctness | tier | nationals | 1564 | 0.14859 | 0.221208 | 0.615752 | 0.63326 |
| tossup_correctness | tier | regionals | 1937 | 0.146295 | 0.204014 | 0.616666 | 0.594917 |
| tossup_correctness | tier | winter | 2750 | 0.155645 | 0.202066 | 0.63014 | 0.591728 |
| tossup_correctness | category | Current Events | 126 | 0.166809 | 0.202983 | 0.639175 | 0.592095 |
| tossup_correctness | category | Fine Arts | 1071 | 0.169722 | 0.202618 | 0.645184 | 0.591091 |
| tossup_correctness | category | Geography | 185 | 0.128249 | 0.21917 | 0.645072 | 0.625521 |
| tossup_correctness | category | History | 1440 | 0.112401 | 0.190439 | 0.653286 | 0.565691 |
| tossup_correctness | category | Literature | 1422 | 0.181388 | 0.195333 | 0.57793 | 0.577255 |
| tossup_correctness | category | Mythology | 318 | 0.206551 | 0.206974 | 0.623952 | 0.601332 |
| tossup_correctness | category | Other Academic | 66 | 0.203383 | 0.218214 | 0.681971 | 0.629456 |
| tossup_correctness | category | Philosophy | 311 | 0.151711 | 0.199953 | 0.679452 | 0.579815 |
| tossup_correctness | category | Popular Culture | 102 | 0.306063 | 0.219019 | 0.471296 | 0.628662 |
| tossup_correctness | category | Religion | 358 | 0.110732 | 0.207909 | 0.641576 | 0.605724 |
| tossup_correctness | category | Science | 1433 | 0.110473 | 0.200262 | 0.630427 | 0.588106 |
| tossup_correctness | category | Social Science | 324 | 0.122498 | 0.193249 | 0.695766 | 0.569256 |
| tossup_correctness | category | Unknown | 1937 | 0.146295 | 0.204014 | 0.616666 | 0.594917 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.30555 | 0.288609 | 0.602066 | 0.776909 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.243787 | 0.255354 | 0.604791 | 0.706995 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.19164 | 0.216673 | 0.637016 | 0.623715 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.151539 | 0.190587 | 0.634839 | 0.565321 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0709009 | 0.176002 | 0.658252 | 0.533876 |
