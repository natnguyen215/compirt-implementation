# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.550922 |
| log_loss | 0.620449 |
| ece | 0.11605 |
| brier | 0.194082 |
| accuracy | 0.764178 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0883224 |
| probability_p10 | 0.753773 |
| probability_p50 | 0.89884 |
| probability_p90 | 0.956099 |
| mean_predictive_variance | 0.102682 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.173534 |
| joint_tossup_event_log_loss | 7.78943 |
| buzz_position_mae | 0.340517 |
| buzz_position_median_absolute_error | 0.343783 |
| buzz_position_bias | -0.327752 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.340499 |
| first_buzzer_mean_reciprocal_rank | 0.558183 |
| first_buzzer_log_loss | 1.67303 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.63876 |
| tossup_scorer_player_top1_accuracy | 0.266738 |
| tossup_scorer_team_top1_accuracy | 0.417804 |
| tossup_game_winner_accuracy | 0.719565 |
| tossup_game_margin_mae | 45.5193 |
| tournament_player_ppg_spearman | 0.639253 |
| tournament_player_ppg_mae | 9.89492 |
| tournament_player_ppg_top10_overlap | 0.6 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.550922 |
| neg_average_precision | 0.274118 |
| neg_precision | 0.5 |
| neg_recall | 0.0032066 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0287908 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.235452 |
| no_buzz_calibration_error | 0.222339 |
| no_buzz_brier | 0.0713256 |
| full_pmf_max_mass_error | 1.55431e-15 |
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
| overall | 9257 | -0.327752 | -0.343783 |
| Q1 (0-.2) | 183 | 0.180359 | 0.17997 |
| Q2 (.2-.4) | 955 | 0.00319321 | -0.00014576 |
| Q3 (.4-.6) | 2239 | -0.177499 | -0.180199 |
| Q4 (.6-.8) | 2875 | -0.353994 | -0.355269 |
| Q5 (.8-1) | 3005 | -0.550716 | -0.553464 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.11605 | 0.194082 | 0.550922 | 0.620449 |
| tossup_correctness | tier | fall | 2798 | 0.0967083 | 0.17791 | 0.550391 | 0.568305 |
| tossup_correctness | tier | nationals | 1545 | 0.141986 | 0.221816 | 0.569122 | 0.698721 |
| tossup_correctness | tier | regionals | 2039 | 0.112299 | 0.194694 | 0.552465 | 0.623828 |
| tossup_correctness | tier | winter | 2875 | 0.126464 | 0.194482 | 0.543847 | 0.626736 |
| tossup_correctness | category | Current Events | 129 | 0.195695 | 0.258519 | 0.555976 | 0.778345 |
| tossup_correctness | category | Fine Arts | 1074 | 0.114539 | 0.186608 | 0.553652 | 0.603402 |
| tossup_correctness | category | Geography | 180 | 0.26589 | 0.302735 | 0.589241 | 0.902741 |
| tossup_correctness | category | History | 1454 | 0.121643 | 0.197265 | 0.563908 | 0.618783 |
| tossup_correctness | category | Literature | 1435 | 0.0921942 | 0.164781 | 0.509291 | 0.552837 |
| tossup_correctness | category | Mythology | 324 | 0.115968 | 0.170167 | 0.584471 | 0.546942 |
| tossup_correctness | category | Other Academic | 71 | 0.198511 | 0.22111 | 0.385621 | 0.740414 |
| tossup_correctness | category | Philosophy | 310 | 0.156009 | 0.203584 | 0.509047 | 0.662754 |
| tossup_correctness | category | Popular Culture | 108 | 0.0563794 | 0.0976169 | 0.634549 | 0.34004 |
| tossup_correctness | category | Religion | 361 | 0.137376 | 0.209128 | 0.537875 | 0.669688 |
| tossup_correctness | category | Science | 1445 | 0.118207 | 0.203224 | 0.552335 | 0.637023 |
| tossup_correctness | category | Social Science | 327 | 0.161066 | 0.227681 | 0.566605 | 0.713486 |
| tossup_correctness | category | Unknown | 2039 | 0.112299 | 0.194694 | 0.552465 | 0.623828 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.135426 | 0.2153 | 0.449937 | 0.677121 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.135327 | 0.215871 | 0.550598 | 0.65962 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.116717 | 0.200056 | 0.545808 | 0.631329 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0967178 | 0.177827 | 0.55165 | 0.575344 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.127501 | 0.196965 | 0.554882 | 0.639595 |
