# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.654032 |
| log_loss | 0.513467 |
| ece | 0.0352335 |
| brier | 0.167042 |
| accuracy | 0.774326 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.000970874 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.140826 |
| probability_p10 | 0.553127 |
| probability_p50 | 0.776434 |
| probability_p90 | 0.911862 |
| mean_predictive_variance | 0.166264 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102194 |
| joint_tossup_event_log_loss | 6.95115 |
| buzz_position_mae | 0.16028 |
| buzz_position_median_absolute_error | 0.145845 |
| buzz_position_bias | -0.0639059 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.344768 |
| first_buzzer_mean_reciprocal_rank | 0.555256 |
| first_buzzer_log_loss | 1.71193 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.634196 |
| tossup_scorer_player_top1_accuracy | 0.310768 |
| tossup_scorer_team_top1_accuracy | 0.486141 |
| tossup_game_winner_accuracy | 0.792123 |
| tossup_game_margin_mae | 34.5976 |
| tournament_player_ppg_spearman | 0.676919 |
| tournament_player_ppg_mae | 9.39106 |
| tournament_player_ppg_top10_overlap | 0.686207 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.654032 |
| neg_average_precision | 0.368155 |
| neg_precision | 0.507881 |
| neg_recall | 0.13803 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0559827 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0874351 |
| no_buzz_calibration_error | 0.075708 |
| no_buzz_brier | 0.0235765 |
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
| overall | 9270 | -0.0639059 | -0.0818199 |
| Q1 (0-.2) | 179 | 0.361043 | 0.357181 |
| Q2 (.2-.4) | 957 | 0.207305 | 0.204772 |
| Q3 (.4-.6) | 2203 | 0.0557795 | 0.0582394 |
| Q4 (.6-.8) | 2978 | -0.0876945 | -0.084714 |
| Q5 (.8-1) | 2953 | -0.242856 | -0.240457 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0352335 | 0.167042 | 0.654032 | 0.513467 |
| tossup_correctness | tier | fall | 2876 | 0.0294469 | 0.156966 | 0.650236 | 0.488393 |
| tossup_correctness | tier | nationals | 1579 | 0.0580312 | 0.188013 | 0.661088 | 0.560362 |
| tossup_correctness | tier | regionals | 1990 | 0.038052 | 0.17183 | 0.64736 | 0.526517 |
| tossup_correctness | tier | winter | 2825 | 0.0332906 | 0.162205 | 0.652011 | 0.503589 |
| tossup_correctness | category | Current Events | 123 | 0.102533 | 0.177454 | 0.666178 | 0.538917 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0426231 | 0.168929 | 0.638091 | 0.519076 |
| tossup_correctness | category | Geography | 191 | 0.0322306 | 0.179274 | 0.744735 | 0.536235 |
| tossup_correctness | category | History | 1469 | 0.0332925 | 0.169148 | 0.690798 | 0.51299 |
| tossup_correctness | category | Literature | 1436 | 0.0593507 | 0.151684 | 0.60581 | 0.485365 |
| tossup_correctness | category | Mythology | 325 | 0.114339 | 0.149267 | 0.610992 | 0.470659 |
| tossup_correctness | category | Other Academic | 67 | 0.154697 | 0.18845 | 0.59973 | 0.568501 |
| tossup_correctness | category | Philosophy | 322 | 0.0470045 | 0.164723 | 0.623246 | 0.508237 |
| tossup_correctness | category | Popular Culture | 100 | 0.151246 | 0.131885 | 0.586313 | 0.432554 |
| tossup_correctness | category | Religion | 365 | 0.0598549 | 0.193401 | 0.643864 | 0.571134 |
| tossup_correctness | category | Science | 1456 | 0.0409835 | 0.166383 | 0.667813 | 0.50913 |
| tossup_correctness | category | Social Science | 333 | 0.0236894 | 0.178143 | 0.697074 | 0.533714 |
| tossup_correctness | category | Unknown | 1990 | 0.038052 | 0.17183 | 0.64736 | 0.526517 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0844465 | 0.178447 | 0.677612 | 0.538859 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0670629 | 0.186899 | 0.609548 | 0.559852 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0386727 | 0.17035 | 0.65498 | 0.519191 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.028346 | 0.157596 | 0.667526 | 0.488922 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.032997 | 0.166973 | 0.653128 | 0.517378 |
