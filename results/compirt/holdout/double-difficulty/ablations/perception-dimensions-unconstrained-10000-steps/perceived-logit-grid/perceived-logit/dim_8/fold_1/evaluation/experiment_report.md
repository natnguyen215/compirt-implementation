# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.632812 |
| log_loss | 0.57063 |
| ece | 0.117752 |
| brier | 0.192281 |
| accuracy | 0.713406 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0487188 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.160944 |
| probability_p10 | 0.431105 |
| probability_p50 | 0.664851 |
| probability_p90 | 0.851583 |
| mean_predictive_variance | 0.201344 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102332 |
| joint_tossup_event_log_loss | 6.6674 |
| buzz_position_mae | 0.166314 |
| buzz_position_median_absolute_error | 0.148777 |
| buzz_position_bias | -0.0871808 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.3925 |
| first_buzzer_mean_reciprocal_rank | 0.597311 |
| first_buzzer_log_loss | 1.59861 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.6538 |
| tossup_scorer_player_top1_accuracy | 0.299567 |
| tossup_scorer_team_top1_accuracy | 0.430195 |
| tossup_game_winner_accuracy | 0.795045 |
| tossup_game_margin_mae | 37.6948 |
| tournament_player_ppg_spearman | 0.618283 |
| tournament_player_ppg_mae | 10.9443 |
| tournament_player_ppg_top10_overlap | 0.658621 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.632812 |
| neg_average_precision | 0.342147 |
| neg_precision | 0.369782 |
| neg_recall | 0.2908 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.102872 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0777148 |
| no_buzz_calibration_error | 0.0618058 |
| no_buzz_brier | 0.0269881 |
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
| overall | 9093 | -0.0871808 | -0.100055 |
| Q1 (0-.2) | 167 | 0.331722 | 0.339117 |
| Q2 (.2-.4) | 912 | 0.1767 | 0.173727 |
| Q3 (.4-.6) | 2115 | 0.0274459 | 0.0223024 |
| Q4 (.6-.8) | 2844 | -0.10501 | -0.107635 |
| Q5 (.8-1) | 3055 | -0.251615 | -0.248175 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.117752 | 0.192281 | 0.632812 | 0.57063 |
| tossup_correctness | tier | fall | 2842 | 0.101281 | 0.175455 | 0.642569 | 0.532427 |
| tossup_correctness | tier | nationals | 1564 | 0.116406 | 0.213404 | 0.62137 | 0.615691 |
| tossup_correctness | tier | regionals | 1937 | 0.123227 | 0.196845 | 0.621066 | 0.579713 |
| tossup_correctness | tier | winter | 2750 | 0.131683 | 0.194443 | 0.625821 | 0.578086 |
| tossup_correctness | category | Current Events | 126 | 0.134447 | 0.193018 | 0.66797 | 0.565178 |
| tossup_correctness | category | Fine Arts | 1071 | 0.135935 | 0.191899 | 0.648063 | 0.569784 |
| tossup_correctness | category | Geography | 185 | 0.0987541 | 0.210352 | 0.653516 | 0.602708 |
| tossup_correctness | category | History | 1440 | 0.0872874 | 0.187291 | 0.646058 | 0.558686 |
| tossup_correctness | category | Literature | 1422 | 0.154862 | 0.184901 | 0.574184 | 0.558579 |
| tossup_correctness | category | Mythology | 318 | 0.158951 | 0.187886 | 0.644407 | 0.558481 |
| tossup_correctness | category | Other Academic | 66 | 0.168353 | 0.210773 | 0.676372 | 0.613499 |
| tossup_correctness | category | Philosophy | 311 | 0.114444 | 0.187187 | 0.692765 | 0.552061 |
| tossup_correctness | category | Popular Culture | 102 | 0.271403 | 0.196794 | 0.506481 | 0.578835 |
| tossup_correctness | category | Religion | 358 | 0.082211 | 0.197701 | 0.669408 | 0.58613 |
| tossup_correctness | category | Science | 1433 | 0.0875945 | 0.195792 | 0.629545 | 0.580381 |
| tossup_correctness | category | Social Science | 324 | 0.0956467 | 0.192729 | 0.675202 | 0.567082 |
| tossup_correctness | category | Unknown | 1937 | 0.123227 | 0.196845 | 0.621066 | 0.579713 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.277877 | 0.271772 | 0.604692 | 0.740253 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.223014 | 0.244378 | 0.604998 | 0.684509 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.164933 | 0.206437 | 0.645029 | 0.601861 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.126099 | 0.182432 | 0.640613 | 0.548185 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0427316 | 0.171753 | 0.663913 | 0.526636 |
