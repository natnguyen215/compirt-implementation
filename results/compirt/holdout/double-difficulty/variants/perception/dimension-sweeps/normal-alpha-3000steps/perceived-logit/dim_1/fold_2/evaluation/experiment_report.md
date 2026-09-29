# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.565387 |
| log_loss | 0.622771 |
| ece | 0.124362 |
| brier | 0.194707 |
| accuracy | 0.762774 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.00140434 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0817838 |
| probability_p10 | 0.78345 |
| probability_p50 | 0.903835 |
| probability_p90 | 0.957599 |
| mean_predictive_variance | 0.0973161 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.172705 |
| joint_tossup_event_log_loss | 7.8371 |
| buzz_position_mae | 0.338312 |
| buzz_position_median_absolute_error | 0.340765 |
| buzz_position_bias | -0.32511 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.306579 |
| first_buzzer_mean_reciprocal_rank | 0.526899 |
| first_buzzer_log_loss | 1.74464 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.63876 |
| tossup_scorer_player_top1_accuracy | 0.258849 |
| tossup_scorer_team_top1_accuracy | 0.427292 |
| tossup_game_winner_accuracy | 0.756522 |
| tossup_game_margin_mae | 44.3261 |
| tournament_player_ppg_spearman | 0.64405 |
| tournament_player_ppg_mae | 9.83468 |
| tournament_player_ppg_top10_overlap | 0.596552 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.565387 |
| neg_average_precision | 0.277587 |
| neg_precision | 0.217391 |
| neg_recall | 0.00229043 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0294768 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.228434 |
| no_buzz_calibration_error | 0.215321 |
| no_buzz_brier | 0.0669599 |
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
| overall | 9257 | -0.32511 | -0.340765 |
| Q1 (0-.2) | 183 | 0.184543 | 0.186521 |
| Q2 (.2-.4) | 955 | 0.00552121 | 0.00131978 |
| Q3 (.4-.6) | 2239 | -0.17524 | -0.178829 |
| Q4 (.6-.8) | 2875 | -0.351335 | -0.353577 |
| Q5 (.8-1) | 3005 | -0.5478 | -0.551116 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.124362 | 0.194707 | 0.565387 | 0.622771 |
| tossup_correctness | tier | fall | 2798 | 0.101907 | 0.176389 | 0.579633 | 0.563012 |
| tossup_correctness | tier | nationals | 1545 | 0.159076 | 0.226117 | 0.57033 | 0.712922 |
| tossup_correctness | tier | regionals | 2039 | 0.126805 | 0.197486 | 0.553549 | 0.634661 |
| tossup_correctness | tier | winter | 2875 | 0.12908 | 0.193684 | 0.565639 | 0.624051 |
| tossup_correctness | category | Current Events | 129 | 0.207033 | 0.261681 | 0.568145 | 0.79547 |
| tossup_correctness | category | Fine Arts | 1074 | 0.118383 | 0.185991 | 0.566662 | 0.602567 |
| tossup_correctness | category | Geography | 180 | 0.259072 | 0.301662 | 0.578535 | 0.911074 |
| tossup_correctness | category | History | 1454 | 0.133992 | 0.200037 | 0.564967 | 0.630118 |
| tossup_correctness | category | Literature | 1435 | 0.0967535 | 0.163558 | 0.546561 | 0.547597 |
| tossup_correctness | category | Mythology | 324 | 0.103059 | 0.169111 | 0.581567 | 0.542264 |
| tossup_correctness | category | Other Academic | 71 | 0.186527 | 0.214577 | 0.432462 | 0.716872 |
| tossup_correctness | category | Philosophy | 310 | 0.13845 | 0.202859 | 0.507043 | 0.660487 |
| tossup_correctness | category | Popular Culture | 108 | 0.0652725 | 0.0973943 | 0.617188 | 0.342973 |
| tossup_correctness | category | Religion | 361 | 0.139984 | 0.206429 | 0.562269 | 0.657325 |
| tossup_correctness | category | Science | 1445 | 0.129458 | 0.203772 | 0.571681 | 0.637659 |
| tossup_correctness | category | Social Science | 327 | 0.168923 | 0.226163 | 0.604302 | 0.697438 |
| tossup_correctness | category | Unknown | 2039 | 0.126805 | 0.197486 | 0.553549 | 0.634661 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.137271 | 0.209995 | 0.517522 | 0.656485 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.14189 | 0.216056 | 0.580465 | 0.662671 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.130503 | 0.201348 | 0.564458 | 0.635348 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.103466 | 0.178251 | 0.56561 | 0.577703 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.133455 | 0.197786 | 0.559224 | 0.641785 |
