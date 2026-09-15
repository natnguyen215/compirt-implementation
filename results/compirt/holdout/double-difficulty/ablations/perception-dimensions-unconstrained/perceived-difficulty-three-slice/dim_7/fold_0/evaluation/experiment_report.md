# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.6649 |
| log_loss | 0.514092 |
| ece | 0.0121924 |
| brier | 0.167743 |
| accuracy | 0.767725 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00247445 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.116106 |
| probability_p10 | 0.606543 |
| probability_p50 | 0.787588 |
| probability_p90 | 0.8986 |
| mean_predictive_variance | 0.165034 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.105404 |
| joint_tossup_event_log_loss | 6.99917 |
| buzz_position_mae | 0.1654 |
| buzz_position_median_absolute_error | 0.151372 |
| buzz_position_bias | -0.072108 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.361269 |
| first_buzzer_mean_reciprocal_rank | 0.570679 |
| first_buzzer_log_loss | 1.69919 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.646799 |
| tossup_scorer_player_top1_accuracy | 0.323567 |
| tossup_scorer_team_top1_accuracy | 0.4931 |
| tossup_game_winner_accuracy | 0.788546 |
| tossup_game_margin_mae | 36.2939 |
| tournament_player_ppg_spearman | 0.674456 |
| tournament_player_ppg_mae | 9.61321 |
| tournament_player_ppg_top10_overlap | 0.655172 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.6649 |
| neg_average_precision | 0.386387 |
| neg_precision | 0.544061 |
| neg_recall | 0.0650779 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0542134 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0899874 |
| no_buzz_calibration_error | 0.0767178 |
| no_buzz_brier | 0.0252609 |
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
| overall | 9295 | -0.072108 | -0.0881951 |
| Q1 (0-.2) | 197 | 0.35282 | 0.360034 |
| Q2 (.2-.4) | 985 | 0.193058 | 0.192026 |
| Q3 (.4-.6) | 2251 | 0.0421681 | 0.0487445 |
| Q4 (.6-.8) | 2866 | -0.0975644 | -0.0901945 |
| Q5 (.8-1) | 2996 | -0.248736 | -0.24527 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0121924 | 0.167743 | 0.6649 | 0.514092 |
| tossup_correctness | tier | fall | 2933 | 0.0175481 | 0.155062 | 0.66038 | 0.484249 |
| tossup_correctness | tier | nationals | 1584 | 0.0220435 | 0.187064 | 0.656295 | 0.557427 |
| tossup_correctness | tier | regionals | 1886 | 0.0209102 | 0.179359 | 0.647941 | 0.54011 |
| tossup_correctness | tier | winter | 2892 | 0.0402146 | 0.162447 | 0.678802 | 0.503656 |
| tossup_correctness | category | Current Events | 124 | 0.0748789 | 0.168837 | 0.688866 | 0.518449 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0373627 | 0.174545 | 0.638218 | 0.534098 |
| tossup_correctness | category | Geography | 197 | 0.0534217 | 0.191235 | 0.734732 | 0.561722 |
| tossup_correctness | category | History | 1491 | 0.0342277 | 0.154084 | 0.69815 | 0.479622 |
| tossup_correctness | category | Literature | 1472 | 0.0215628 | 0.150277 | 0.637522 | 0.477711 |
| tossup_correctness | category | Mythology | 332 | 0.0590382 | 0.146273 | 0.666607 | 0.461312 |
| tossup_correctness | category | Other Academic | 69 | 0.104717 | 0.191739 | 0.514706 | 0.577335 |
| tossup_correctness | category | Philosophy | 324 | 0.0266211 | 0.149835 | 0.668607 | 0.472064 |
| tossup_correctness | category | Popular Culture | 102 | 0.0873982 | 0.162946 | 0.417301 | 0.511675 |
| tossup_correctness | category | Religion | 372 | 0.08771 | 0.190697 | 0.684449 | 0.561789 |
| tossup_correctness | category | Science | 1487 | 0.0401886 | 0.172501 | 0.678976 | 0.524559 |
| tossup_correctness | category | Social Science | 336 | 0.0638314 | 0.191714 | 0.687119 | 0.56648 |
| tossup_correctness | category | Unknown | 1886 | 0.0209102 | 0.179359 | 0.647941 | 0.54011 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0771664 | 0.188051 | 0.632759 | 0.566514 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0227057 | 0.181226 | 0.658755 | 0.546371 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0152853 | 0.164022 | 0.680355 | 0.504356 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0163871 | 0.15953 | 0.663111 | 0.493858 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0292462 | 0.172628 | 0.664633 | 0.526705 |
