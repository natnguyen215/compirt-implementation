# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.587846 |
| log_loss | 0.54432 |
| ece | 0.0630534 |
| brier | 0.178911 |
| accuracy | 0.759008 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0143474 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.134458 |
| probability_p10 | 0.563781 |
| probability_p50 | 0.77891 |
| probability_p90 | 0.909806 |
| mean_predictive_variance | 0.166907 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.105897 |
| joint_tossup_event_log_loss | 7.02497 |
| buzz_position_mae | 0.164522 |
| buzz_position_median_absolute_error | 0.150686 |
| buzz_position_bias | -0.0640262 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.302913 |
| first_buzzer_mean_reciprocal_rank | 0.522182 |
| first_buzzer_log_loss | 1.75851 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.618662 |
| tossup_scorer_player_top1_accuracy | 0.276652 |
| tossup_scorer_team_top1_accuracy | 0.45565 |
| tossup_game_winner_accuracy | 0.730853 |
| tossup_game_margin_mae | 39.177 |
| tournament_player_ppg_spearman | 0.617237 |
| tournament_player_ppg_mae | 10.4355 |
| tournament_player_ppg_top10_overlap | 0.610345 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.587846 |
| neg_average_precision | 0.290012 |
| neg_precision | 0.35512 |
| neg_recall | 0.0775821 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0577407 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0888938 |
| no_buzz_calibration_error | 0.0771667 |
| no_buzz_brier | 0.0231966 |
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
| overall | 9270 | -0.0640262 | -0.0810922 |
| Q1 (0-.2) | 179 | 0.374962 | 0.376136 |
| Q2 (.2-.4) | 957 | 0.220588 | 0.218911 |
| Q3 (.4-.6) | 2203 | 0.0639126 | 0.0650239 |
| Q4 (.6-.8) | 2978 | -0.0879305 | -0.084639 |
| Q5 (.8-1) | 2953 | -0.254211 | -0.252741 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0630534 | 0.178911 | 0.587846 | 0.54432 |
| tossup_correctness | tier | fall | 2876 | 0.0838459 | 0.174605 | 0.571341 | 0.533929 |
| tossup_correctness | tier | nationals | 1579 | 0.0673327 | 0.194726 | 0.624652 | 0.581887 |
| tossup_correctness | tier | regionals | 1990 | 0.0609593 | 0.181535 | 0.592597 | 0.55011 |
| tossup_correctness | tier | winter | 2825 | 0.0570037 | 0.172606 | 0.588947 | 0.529823 |
| tossup_correctness | category | Current Events | 123 | 0.121234 | 0.192034 | 0.60675 | 0.569946 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0629875 | 0.178349 | 0.597475 | 0.54424 |
| tossup_correctness | category | Geography | 191 | 0.10432 | 0.179655 | 0.749615 | 0.538874 |
| tossup_correctness | category | History | 1469 | 0.0601917 | 0.189283 | 0.59357 | 0.562906 |
| tossup_correctness | category | Literature | 1436 | 0.0625352 | 0.155189 | 0.5585 | 0.497596 |
| tossup_correctness | category | Mythology | 325 | 0.125865 | 0.161661 | 0.532417 | 0.49905 |
| tossup_correctness | category | Other Academic | 67 | 0.120354 | 0.185725 | 0.566038 | 0.567161 |
| tossup_correctness | category | Philosophy | 322 | 0.0465009 | 0.165497 | 0.624678 | 0.511663 |
| tossup_correctness | category | Popular Culture | 100 | 0.27873 | 0.176871 | 0.594484 | 0.538338 |
| tossup_correctness | category | Religion | 365 | 0.0840146 | 0.207792 | 0.597772 | 0.609448 |
| tossup_correctness | category | Science | 1456 | 0.085563 | 0.182147 | 0.571614 | 0.55129 |
| tossup_correctness | category | Social Science | 333 | 0.0627164 | 0.199578 | 0.566895 | 0.594241 |
| tossup_correctness | category | Unknown | 1990 | 0.0609593 | 0.181535 | 0.592597 | 0.55011 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.145329 | 0.20164 | 0.566003 | 0.59529 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.1106 | 0.209578 | 0.523964 | 0.610936 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0738245 | 0.185132 | 0.57865 | 0.55634 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0504527 | 0.167643 | 0.601665 | 0.516387 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0553259 | 0.174317 | 0.61148 | 0.538845 |
