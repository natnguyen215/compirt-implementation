# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.573307 |
| log_loss | 0.556684 |
| ece | 0.0611633 |
| brier | 0.18308 |
| accuracy | 0.760805 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0013197 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.11626 |
| probability_p10 | 0.597133 |
| probability_p50 | 0.795607 |
| probability_p90 | 0.899717 |
| mean_predictive_variance | 0.163424 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.171855 |
| joint_tossup_event_log_loss | 7.64307 |
| buzz_position_mae | 0.320135 |
| buzz_position_median_absolute_error | 0.320026 |
| buzz_position_bias | -0.302698 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.284615 |
| first_buzzer_mean_reciprocal_rank | 0.507164 |
| first_buzzer_log_loss | 1.78041 |
| first_buzzer_events | 9093 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.611459 |
| tossup_scorer_player_top1_accuracy | 0.259307 |
| tossup_scorer_team_top1_accuracy | 0.364394 |
| tossup_game_winner_accuracy | 0.713964 |
| tossup_game_margin_mae | 44.8912 |
| tournament_player_ppg_spearman | 0.520228 |
| tournament_player_ppg_mae | 11.1577 |
| tournament_player_ppg_top10_overlap | 0.534483 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.573307 |
| neg_average_precision | 0.304707 |
| neg_precision | 0.462963 |
| neg_recall | 0.0346741 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0387741 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.198483 |
| no_buzz_calibration_error | 0.182573 |
| no_buzz_brier | 0.0555379 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| overall | 9093 | -0.302698 | -0.319389 |
| Q1 (0-.2) | 167 | 0.195909 | 0.185223 |
| Q2 (.2-.4) | 912 | 0.0337914 | 0.0301461 |
| Q3 (.4-.6) | 2115 | -0.146168 | -0.148252 |
| Q4 (.6-.8) | 2844 | -0.324952 | -0.324545 |
| Q5 (.8-1) | 3055 | -0.518053 | -0.516731 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0611633 | 0.18308 | 0.573307 | 0.556684 |
| tossup_correctness | tier | fall | 2842 | 0.0498014 | 0.168764 | 0.583803 | 0.522126 |
| tossup_correctness | tier | nationals | 1564 | 0.0825896 | 0.207085 | 0.577761 | 0.605088 |
| tossup_correctness | tier | regionals | 1937 | 0.0747523 | 0.185493 | 0.558596 | 0.563348 |
| tossup_correctness | tier | winter | 2750 | 0.0662445 | 0.182523 | 0.558786 | 0.560176 |
| tossup_correctness | category | Current Events | 126 | 0.108635 | 0.190708 | 0.531817 | 0.569829 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0597859 | 0.179292 | 0.589267 | 0.547526 |
| tossup_correctness | category | Geography | 185 | 0.137619 | 0.222555 | 0.557171 | 0.648081 |
| tossup_correctness | category | History | 1440 | 0.0562472 | 0.186134 | 0.577111 | 0.563087 |
| tossup_correctness | category | Literature | 1422 | 0.0680152 | 0.157033 | 0.555863 | 0.498706 |
| tossup_correctness | category | Mythology | 318 | 0.0468465 | 0.165996 | 0.589998 | 0.513791 |
| tossup_correctness | category | Other Academic | 66 | 0.152506 | 0.221406 | 0.516237 | 0.6422 |
| tossup_correctness | category | Philosophy | 311 | 0.0635485 | 0.188024 | 0.597938 | 0.56901 |
| tossup_correctness | category | Popular Culture | 102 | 0.104969 | 0.122094 | 0.536111 | 0.408201 |
| tossup_correctness | category | Religion | 358 | 0.0938848 | 0.21251 | 0.564249 | 0.627549 |
| tossup_correctness | category | Science | 1433 | 0.0773728 | 0.19453 | 0.583554 | 0.581202 |
| tossup_correctness | category | Social Science | 324 | 0.0616814 | 0.19667 | 0.578835 | 0.58868 |
| tossup_correctness | category | Unknown | 1937 | 0.0747523 | 0.185493 | 0.558596 | 0.563348 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0568341 | 0.200604 | 0.603641 | 0.590918 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0563619 | 0.19591 | 0.589699 | 0.580727 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.079332 | 0.190693 | 0.543699 | 0.573154 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0583412 | 0.172406 | 0.577052 | 0.53016 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0678086 | 0.182959 | 0.57757 | 0.560925 |
