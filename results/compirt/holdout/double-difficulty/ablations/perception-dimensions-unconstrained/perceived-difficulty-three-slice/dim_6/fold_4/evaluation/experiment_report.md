# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.657833 |
| log_loss | 0.506599 |
| ece | 0.0185872 |
| brier | 0.164315 |
| accuracy | 0.77918 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00582524 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.11947 |
| probability_p10 | 0.604476 |
| probability_p50 | 0.793268 |
| probability_p90 | 0.9043 |
| mean_predictive_variance | 0.162154 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10022 |
| joint_tossup_event_log_loss | 6.88809 |
| buzz_position_mae | 0.158636 |
| buzz_position_median_absolute_error | 0.144711 |
| buzz_position_bias | -0.063634 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.362567 |
| first_buzzer_mean_reciprocal_rank | 0.5684 |
| first_buzzer_log_loss | 1.67237 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.643366 |
| tossup_scorer_player_top1_accuracy | 0.321109 |
| tossup_scorer_team_top1_accuracy | 0.494989 |
| tossup_game_winner_accuracy | 0.800875 |
| tossup_game_margin_mae | 33.2407 |
| tournament_player_ppg_spearman | 0.698657 |
| tournament_player_ppg_mae | 8.98954 |
| tournament_player_ppg_top10_overlap | 0.696552 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.657833 |
| neg_average_precision | 0.381059 |
| neg_precision | 0.6 |
| neg_recall | 0.0771061 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0555623 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0925704 |
| no_buzz_calibration_error | 0.0808434 |
| no_buzz_brier | 0.025221 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| overall | 9270 | -0.063634 | -0.0826212 |
| Q1 (0-.2) | 179 | 0.358687 | 0.362774 |
| Q2 (.2-.4) | 957 | 0.204581 | 0.203271 |
| Q3 (.4-.6) | 2203 | 0.0552009 | 0.0572509 |
| Q4 (.6-.8) | 2978 | -0.0871486 | -0.0847828 |
| Q5 (.8-1) | 2953 | -0.241096 | -0.240722 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0185872 | 0.164315 | 0.657833 | 0.506599 |
| tossup_correctness | tier | fall | 2876 | 0.0262552 | 0.157371 | 0.637432 | 0.491877 |
| tossup_correctness | tier | nationals | 1579 | 0.0610856 | 0.186322 | 0.662353 | 0.55728 |
| tossup_correctness | tier | regionals | 1990 | 0.0158145 | 0.164789 | 0.680832 | 0.5058 |
| tossup_correctness | tier | winter | 2825 | 0.0135351 | 0.15875 | 0.665044 | 0.49382 |
| tossup_correctness | category | Current Events | 123 | 0.0465511 | 0.167395 | 0.681218 | 0.513753 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0278241 | 0.168129 | 0.64674 | 0.515689 |
| tossup_correctness | category | Geography | 191 | 0.0576821 | 0.176342 | 0.75963 | 0.52966 |
| tossup_correctness | category | History | 1469 | 0.0220297 | 0.168909 | 0.680846 | 0.514744 |
| tossup_correctness | category | Literature | 1436 | 0.0607267 | 0.151259 | 0.593835 | 0.483817 |
| tossup_correctness | category | Mythology | 325 | 0.0912343 | 0.137739 | 0.63518 | 0.444186 |
| tossup_correctness | category | Other Academic | 67 | 0.108286 | 0.17551 | 0.607817 | 0.53452 |
| tossup_correctness | category | Philosophy | 322 | 0.0228842 | 0.16381 | 0.622444 | 0.505785 |
| tossup_correctness | category | Popular Culture | 100 | 0.120284 | 0.121799 | 0.537283 | 0.407521 |
| tossup_correctness | category | Religion | 365 | 0.0445964 | 0.190203 | 0.666629 | 0.563483 |
| tossup_correctness | category | Science | 1456 | 0.0336208 | 0.165915 | 0.657376 | 0.51045 |
| tossup_correctness | category | Social Science | 333 | 0.0343361 | 0.178533 | 0.69433 | 0.534622 |
| tossup_correctness | category | Unknown | 1990 | 0.0158145 | 0.164789 | 0.680832 | 0.5058 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.099077 | 0.181366 | 0.615091 | 0.548696 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0428007 | 0.180462 | 0.615984 | 0.54574 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0196729 | 0.168142 | 0.653706 | 0.514718 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0198382 | 0.155557 | 0.667086 | 0.484216 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0200306 | 0.164026 | 0.66641 | 0.507877 |
