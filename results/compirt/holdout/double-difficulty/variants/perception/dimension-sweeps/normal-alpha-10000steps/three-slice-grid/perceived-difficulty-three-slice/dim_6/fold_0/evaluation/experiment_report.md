# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.666496 |
| log_loss | 0.51462 |
| ece | 0.0202235 |
| brier | 0.167686 |
| accuracy | 0.768478 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00322754 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.128116 |
| probability_p10 | 0.581201 |
| probability_p50 | 0.781225 |
| probability_p90 | 0.90523 |
| mean_predictive_variance | 0.166276 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.104496 |
| joint_tossup_event_log_loss | 7.05442 |
| buzz_position_mae | 0.163158 |
| buzz_position_median_absolute_error | 0.148803 |
| buzz_position_bias | -0.0658499 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.344917 |
| first_buzzer_mean_reciprocal_rank | 0.558554 |
| first_buzzer_log_loss | 1.71877 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.640667 |
| tossup_scorer_player_top1_accuracy | 0.322187 |
| tossup_scorer_team_top1_accuracy | 0.489384 |
| tossup_game_winner_accuracy | 0.795154 |
| tossup_game_margin_mae | 35.5767 |
| tournament_player_ppg_spearman | 0.684889 |
| tournament_player_ppg_mae | 9.2972 |
| tournament_player_ppg_top10_overlap | 0.668966 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.666496 |
| neg_average_precision | 0.389992 |
| neg_precision | 0.5375 |
| neg_recall | 0.0985335 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0563588 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.093564 |
| no_buzz_calibration_error | 0.0802944 |
| no_buzz_brier | 0.026434 |
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
| overall | 9295 | -0.0658499 | -0.0814665 |
| Q1 (0-.2) | 197 | 0.358205 | 0.367047 |
| Q2 (.2-.4) | 985 | 0.199858 | 0.200061 |
| Q3 (.4-.6) | 2251 | 0.0480962 | 0.0555581 |
| Q4 (.6-.8) | 2866 | -0.091629 | -0.0837398 |
| Q5 (.8-1) | 2996 | -0.242042 | -0.239555 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0202235 | 0.167686 | 0.666496 | 0.51462 |
| tossup_correctness | tier | fall | 2933 | 0.0251796 | 0.155712 | 0.661002 | 0.485828 |
| tossup_correctness | tier | nationals | 1584 | 0.0476841 | 0.185562 | 0.675706 | 0.554193 |
| tossup_correctness | tier | regionals | 1886 | 0.0175814 | 0.179628 | 0.647176 | 0.541378 |
| tossup_correctness | tier | winter | 2892 | 0.025826 | 0.162251 | 0.675194 | 0.504695 |
| tossup_correctness | category | Current Events | 124 | 0.0910704 | 0.170488 | 0.694762 | 0.521951 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0285626 | 0.174646 | 0.637713 | 0.533958 |
| tossup_correctness | category | Geography | 197 | 0.0444569 | 0.188946 | 0.737995 | 0.556813 |
| tossup_correctness | category | History | 1491 | 0.0488128 | 0.155502 | 0.694197 | 0.484092 |
| tossup_correctness | category | Literature | 1472 | 0.0361115 | 0.150283 | 0.641742 | 0.481923 |
| tossup_correctness | category | Mythology | 332 | 0.0627407 | 0.147925 | 0.67264 | 0.465243 |
| tossup_correctness | category | Other Academic | 69 | 0.138788 | 0.19703 | 0.504525 | 0.588085 |
| tossup_correctness | category | Philosophy | 324 | 0.0301783 | 0.150711 | 0.675854 | 0.472508 |
| tossup_correctness | category | Popular Culture | 102 | 0.128135 | 0.167281 | 0.490657 | 0.516624 |
| tossup_correctness | category | Religion | 372 | 0.0622416 | 0.1928 | 0.672559 | 0.566524 |
| tossup_correctness | category | Science | 1487 | 0.00966742 | 0.169433 | 0.68726 | 0.516152 |
| tossup_correctness | category | Social Science | 336 | 0.0567527 | 0.189083 | 0.686017 | 0.561662 |
| tossup_correctness | category | Unknown | 1886 | 0.0175814 | 0.179628 | 0.647176 | 0.541378 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0678945 | 0.192823 | 0.602785 | 0.576279 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0289204 | 0.182616 | 0.66111 | 0.548842 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0233492 | 0.164031 | 0.679607 | 0.504357 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0232054 | 0.159099 | 0.665447 | 0.493535 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0234622 | 0.172087 | 0.665651 | 0.527195 |
