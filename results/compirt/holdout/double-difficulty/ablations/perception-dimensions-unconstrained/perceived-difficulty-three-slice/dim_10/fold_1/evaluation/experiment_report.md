# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.653312 |
| log_loss | 0.521699 |
| ece | 0.0198413 |
| brier | 0.170477 |
| accuracy | 0.766084 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00395909 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.111799 |
| probability_p10 | 0.619428 |
| probability_p50 | 0.795717 |
| probability_p90 | 0.904352 |
| mean_predictive_variance | 0.161153 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101224 |
| joint_tossup_event_log_loss | 6.8962 |
| buzz_position_mae | 0.162917 |
| buzz_position_median_absolute_error | 0.150275 |
| buzz_position_bias | -0.0727133 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.343011 |
| first_buzzer_mean_reciprocal_rank | 0.557573 |
| first_buzzer_log_loss | 1.68951 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.638843 |
| tossup_scorer_player_top1_accuracy | 0.319156 |
| tossup_scorer_team_top1_accuracy | 0.495022 |
| tossup_game_winner_accuracy | 0.788288 |
| tossup_game_margin_mae | 33.6695 |
| tournament_player_ppg_spearman | 0.676432 |
| tournament_player_ppg_mae | 8.77955 |
| tournament_player_ppg_top10_overlap | 0.658621 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.653312 |
| neg_average_precision | 0.387242 |
| neg_precision | 0.608434 |
| neg_recall | 0.0466944 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0552067 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0941498 |
| no_buzz_calibration_error | 0.0782407 |
| no_buzz_brier | 0.0278022 |
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
| overall | 9093 | -0.0727133 | -0.0920682 |
| Q1 (0-.2) | 167 | 0.363151 | 0.377526 |
| Q2 (.2-.4) | 912 | 0.205236 | 0.207111 |
| Q3 (.4-.6) | 2115 | 0.0501091 | 0.0503857 |
| Q4 (.6-.8) | 2844 | -0.0909029 | -0.0891027 |
| Q5 (.8-1) | 3055 | -0.247612 | -0.247314 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0198413 | 0.170477 | 0.653312 | 0.521699 |
| tossup_correctness | tier | fall | 2842 | 0.0213482 | 0.15547 | 0.685842 | 0.48326 |
| tossup_correctness | tier | nationals | 1564 | 0.0427158 | 0.191954 | 0.647803 | 0.570364 |
| tossup_correctness | tier | regionals | 1937 | 0.0231806 | 0.175054 | 0.626175 | 0.532481 |
| tossup_correctness | tier | winter | 2750 | 0.0416919 | 0.170549 | 0.642602 | 0.526152 |
| tossup_correctness | category | Current Events | 126 | 0.0628477 | 0.170576 | 0.67117 | 0.5206 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0385648 | 0.166752 | 0.662251 | 0.512836 |
| tossup_correctness | category | Geography | 185 | 0.0484159 | 0.180878 | 0.719269 | 0.543636 |
| tossup_correctness | category | History | 1440 | 0.0284629 | 0.172445 | 0.672967 | 0.523956 |
| tossup_correctness | category | Literature | 1422 | 0.0402793 | 0.14942 | 0.606604 | 0.477079 |
| tossup_correctness | category | Mythology | 318 | 0.0576793 | 0.154603 | 0.683118 | 0.48504 |
| tossup_correctness | category | Other Academic | 66 | 0.0751035 | 0.204589 | 0.55991 | 0.604927 |
| tossup_correctness | category | Philosophy | 311 | 0.0561907 | 0.178067 | 0.677052 | 0.537228 |
| tossup_correctness | category | Popular Culture | 102 | 0.101443 | 0.115713 | 0.615741 | 0.392761 |
| tossup_correctness | category | Religion | 358 | 0.053336 | 0.19299 | 0.665981 | 0.570942 |
| tossup_correctness | category | Science | 1433 | 0.0325302 | 0.180162 | 0.666949 | 0.543475 |
| tossup_correctness | category | Social Science | 324 | 0.0478951 | 0.184011 | 0.640235 | 0.554218 |
| tossup_correctness | category | Unknown | 1937 | 0.0231806 | 0.175054 | 0.626175 | 0.532481 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0767331 | 0.19867 | 0.622374 | 0.587747 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0128777 | 0.182107 | 0.669605 | 0.547745 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0133983 | 0.173173 | 0.657235 | 0.526447 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0138347 | 0.162651 | 0.647016 | 0.502662 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.037796 | 0.170885 | 0.652025 | 0.524747 |
