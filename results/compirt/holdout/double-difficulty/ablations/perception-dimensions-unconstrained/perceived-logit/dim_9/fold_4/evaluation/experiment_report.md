# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.570462 |
| log_loss | 0.546596 |
| ece | 0.0712036 |
| brier | 0.177885 |
| accuracy | 0.77206 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0012945 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.118871 |
| probability_p10 | 0.603689 |
| probability_p50 | 0.80693 |
| probability_p90 | 0.909404 |
| mean_predictive_variance | 0.158644 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.170361 |
| joint_tossup_event_log_loss | 7.67489 |
| buzz_position_mae | 0.317652 |
| buzz_position_median_absolute_error | 0.314135 |
| buzz_position_bias | -0.300082 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.305394 |
| first_buzzer_mean_reciprocal_rank | 0.517465 |
| first_buzzer_log_loss | 1.78041 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.611435 |
| tossup_scorer_player_top1_accuracy | 0.245842 |
| tossup_scorer_team_top1_accuracy | 0.368017 |
| tossup_game_winner_accuracy | 0.698031 |
| tossup_game_margin_mae | 46.9743 |
| tournament_player_ppg_spearman | 0.542244 |
| tournament_player_ppg_mae | 11.4225 |
| tournament_player_ppg_top10_overlap | 0.575862 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.570462 |
| neg_average_precision | 0.293904 |
| neg_precision | 0.464286 |
| neg_recall | 0.0371252 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0376708 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.2012 |
| no_buzz_calibration_error | 0.189473 |
| no_buzz_brier | 0.0550898 |
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
| overall | 9270 | -0.300082 | -0.313894 |
| Q1 (0-.2) | 179 | 0.192476 | 0.188389 |
| Q2 (.2-.4) | 957 | 0.032996 | 0.0309718 |
| Q3 (.4-.6) | 2203 | -0.150433 | -0.153467 |
| Q4 (.6-.8) | 2978 | -0.327797 | -0.328093 |
| Q5 (.8-1) | 2953 | -0.521574 | -0.518195 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0712036 | 0.177885 | 0.570462 | 0.546596 |
| tossup_correctness | tier | fall | 2876 | 0.0594549 | 0.166642 | 0.556994 | 0.522327 |
| tossup_correctness | tier | nationals | 1579 | 0.0809386 | 0.197858 | 0.61183 | 0.584724 |
| tossup_correctness | tier | regionals | 1990 | 0.0914969 | 0.185875 | 0.543406 | 0.56573 |
| tossup_correctness | tier | winter | 2825 | 0.0634282 | 0.172539 | 0.563725 | 0.536515 |
| tossup_correctness | category | Current Events | 123 | 0.0524979 | 0.167879 | 0.666178 | 0.513681 |
| tossup_correctness | category | Fine Arts | 1093 | 0.063042 | 0.178488 | 0.579554 | 0.549563 |
| tossup_correctness | category | Geography | 191 | 0.0835091 | 0.201781 | 0.677067 | 0.592063 |
| tossup_correctness | category | History | 1469 | 0.0567913 | 0.182882 | 0.589676 | 0.555425 |
| tossup_correctness | category | Literature | 1436 | 0.0798398 | 0.1596 | 0.525543 | 0.511068 |
| tossup_correctness | category | Mythology | 325 | 0.0521638 | 0.135079 | 0.610205 | 0.437827 |
| tossup_correctness | category | Other Academic | 67 | 0.143993 | 0.172319 | 0.605121 | 0.530277 |
| tossup_correctness | category | Philosophy | 322 | 0.0903126 | 0.181286 | 0.486739 | 0.567398 |
| tossup_correctness | category | Popular Culture | 100 | 0.0990295 | 0.118036 | 0.552605 | 0.396568 |
| tossup_correctness | category | Religion | 365 | 0.0986846 | 0.203565 | 0.588921 | 0.609054 |
| tossup_correctness | category | Science | 1456 | 0.0625532 | 0.178122 | 0.590462 | 0.5431 |
| tossup_correctness | category | Social Science | 333 | 0.0941573 | 0.203352 | 0.552218 | 0.604067 |
| tossup_correctness | category | Unknown | 1990 | 0.0914969 | 0.185875 | 0.543406 | 0.56573 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.092286 | 0.194336 | 0.529022 | 0.58211 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.084489 | 0.193388 | 0.524035 | 0.580936 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0734428 | 0.183353 | 0.554542 | 0.557165 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0636852 | 0.166921 | 0.59046 | 0.518402 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0752988 | 0.178842 | 0.575596 | 0.553864 |
