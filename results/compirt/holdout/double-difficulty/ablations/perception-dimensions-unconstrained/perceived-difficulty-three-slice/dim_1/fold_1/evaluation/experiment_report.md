# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.582314 |
| log_loss | 0.561158 |
| ece | 0.0629349 |
| brier | 0.184712 |
| accuracy | 0.749368 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0127571 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.133293 |
| probability_p10 | 0.569926 |
| probability_p50 | 0.783086 |
| probability_p90 | 0.909957 |
| mean_predictive_variance | 0.16536 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.1059 |
| joint_tossup_event_log_loss | 7.00937 |
| buzz_position_mae | 0.165939 |
| buzz_position_median_absolute_error | 0.151107 |
| buzz_position_bias | -0.0706788 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.30419 |
| first_buzzer_mean_reciprocal_rank | 0.524935 |
| first_buzzer_log_loss | 1.75506 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.623996 |
| tossup_scorer_player_top1_accuracy | 0.280628 |
| tossup_scorer_team_top1_accuracy | 0.451299 |
| tossup_game_winner_accuracy | 0.734234 |
| tossup_game_margin_mae | 38.3286 |
| tournament_player_ppg_spearman | 0.59074 |
| tournament_player_ppg_mae | 10.1481 |
| tournament_player_ppg_top10_overlap | 0.6 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.582314 |
| neg_average_precision | 0.29981 |
| neg_precision | 0.36385 |
| neg_recall | 0.0716597 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0584017 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0894556 |
| no_buzz_calibration_error | 0.0735465 |
| no_buzz_brier | 0.0252384 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| overall | 9093 | -0.0706788 | -0.0902823 |
| Q1 (0-.2) | 167 | 0.37463 | 0.386639 |
| Q2 (.2-.4) | 912 | 0.216601 | 0.222435 |
| Q3 (.4-.6) | 2115 | 0.0589674 | 0.0589799 |
| Q4 (.6-.8) | 2844 | -0.0885021 | -0.087506 |
| Q5 (.8-1) | 3055 | -0.253945 | -0.254787 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0629349 | 0.184712 | 0.582314 | 0.561158 |
| tossup_correctness | tier | fall | 2842 | 0.0770019 | 0.175338 | 0.585192 | 0.534392 |
| tossup_correctness | tier | nationals | 1564 | 0.0729082 | 0.202536 | 0.615708 | 0.609893 |
| tossup_correctness | tier | regionals | 1937 | 0.0637493 | 0.18829 | 0.575617 | 0.56888 |
| tossup_correctness | tier | winter | 2750 | 0.0582521 | 0.181741 | 0.576787 | 0.555664 |
| tossup_correctness | category | Current Events | 126 | 0.152991 | 0.211971 | 0.477426 | 0.618005 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0533631 | 0.181087 | 0.588068 | 0.553499 |
| tossup_correctness | category | Geography | 185 | 0.0277304 | 0.192024 | 0.693937 | 0.563717 |
| tossup_correctness | category | History | 1440 | 0.07688 | 0.194978 | 0.561744 | 0.578851 |
| tossup_correctness | category | Literature | 1422 | 0.0588567 | 0.157207 | 0.547525 | 0.509937 |
| tossup_correctness | category | Mythology | 318 | 0.0878007 | 0.168193 | 0.616816 | 0.518094 |
| tossup_correctness | category | Other Academic | 66 | 0.0695836 | 0.187337 | 0.681971 | 0.549369 |
| tossup_correctness | category | Philosophy | 311 | 0.0711747 | 0.19083 | 0.583042 | 0.581658 |
| tossup_correctness | category | Popular Culture | 102 | 0.229642 | 0.165593 | 0.612037 | 0.506554 |
| tossup_correctness | category | Religion | 358 | 0.0670678 | 0.205088 | 0.620484 | 0.607423 |
| tossup_correctness | category | Science | 1433 | 0.0762077 | 0.190572 | 0.590888 | 0.572697 |
| tossup_correctness | category | Social Science | 324 | 0.0770096 | 0.203003 | 0.538872 | 0.602946 |
| tossup_correctness | category | Unknown | 1937 | 0.0637493 | 0.18829 | 0.575617 | 0.56888 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0974503 | 0.221946 | 0.537815 | 0.640806 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0825842 | 0.205962 | 0.578777 | 0.605436 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0661133 | 0.189259 | 0.578659 | 0.566186 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.062863 | 0.174664 | 0.573953 | 0.536246 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.064913 | 0.182538 | 0.5995 | 0.563297 |
