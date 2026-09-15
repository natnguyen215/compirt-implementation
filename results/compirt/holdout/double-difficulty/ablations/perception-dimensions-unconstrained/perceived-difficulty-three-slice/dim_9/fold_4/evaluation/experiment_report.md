# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.652947 |
| log_loss | 0.507784 |
| ece | 0.0138311 |
| brier | 0.164972 |
| accuracy | 0.778964 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00560949 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.107768 |
| probability_p10 | 0.631053 |
| probability_p50 | 0.801157 |
| probability_p90 | 0.899497 |
| mean_predictive_variance | 0.15966 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102423 |
| joint_tossup_event_log_loss | 6.93979 |
| buzz_position_mae | 0.163258 |
| buzz_position_median_absolute_error | 0.149264 |
| buzz_position_bias | -0.0726487 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.364401 |
| first_buzzer_mean_reciprocal_rank | 0.569405 |
| first_buzzer_log_loss | 1.68853 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.63808 |
| tossup_scorer_player_top1_accuracy | 0.32484 |
| tossup_scorer_team_top1_accuracy | 0.502665 |
| tossup_game_winner_accuracy | 0.78337 |
| tossup_game_margin_mae | 35.0463 |
| tournament_player_ppg_spearman | 0.686273 |
| tournament_player_ppg_mae | 9.29056 |
| tournament_player_ppg_top10_overlap | 0.672414 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.652947 |
| neg_average_precision | 0.372682 |
| neg_precision | 0.644444 |
| neg_recall | 0.0552118 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0532795 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0895065 |
| no_buzz_calibration_error | 0.0777794 |
| no_buzz_brier | 0.0242644 |
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
| overall | 9270 | -0.0726487 | -0.0901499 |
| Q1 (0-.2) | 179 | 0.354953 | 0.35464 |
| Q2 (.2-.4) | 957 | 0.199263 | 0.199237 |
| Q3 (.4-.6) | 2203 | 0.0463216 | 0.0498232 |
| Q4 (.6-.8) | 2978 | -0.0954868 | -0.0922941 |
| Q5 (.8-1) | 2953 | -0.252411 | -0.251843 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0138311 | 0.164972 | 0.652947 | 0.507784 |
| tossup_correctness | tier | fall | 2876 | 0.00955515 | 0.154498 | 0.654634 | 0.48241 |
| tossup_correctness | tier | nationals | 1579 | 0.0429701 | 0.184574 | 0.661218 | 0.552869 |
| tossup_correctness | tier | regionals | 1990 | 0.0152457 | 0.166317 | 0.670941 | 0.50934 |
| tossup_correctness | tier | winter | 2825 | 0.0393665 | 0.163733 | 0.641969 | 0.507319 |
| tossup_correctness | category | Current Events | 123 | 0.0908176 | 0.163787 | 0.709831 | 0.505852 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0224998 | 0.167062 | 0.655507 | 0.510942 |
| tossup_correctness | category | Geography | 191 | 0.0749231 | 0.177911 | 0.757576 | 0.534979 |
| tossup_correctness | category | History | 1469 | 0.0248676 | 0.171234 | 0.671411 | 0.521031 |
| tossup_correctness | category | Literature | 1436 | 0.0494447 | 0.150254 | 0.591692 | 0.478555 |
| tossup_correctness | category | Mythology | 325 | 0.0715328 | 0.135714 | 0.626664 | 0.440559 |
| tossup_correctness | category | Other Academic | 67 | 0.0759703 | 0.174694 | 0.563342 | 0.532309 |
| tossup_correctness | category | Philosophy | 322 | 0.048966 | 0.166549 | 0.600791 | 0.513996 |
| tossup_correctness | category | Popular Culture | 100 | 0.127535 | 0.122349 | 0.515832 | 0.411619 |
| tossup_correctness | category | Religion | 365 | 0.0654405 | 0.194858 | 0.636739 | 0.577164 |
| tossup_correctness | category | Science | 1456 | 0.024374 | 0.165097 | 0.660981 | 0.507729 |
| tossup_correctness | category | Social Science | 333 | 0.0382373 | 0.18351 | 0.6738 | 0.548577 |
| tossup_correctness | category | Unknown | 1990 | 0.0152457 | 0.166317 | 0.670941 | 0.50934 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.0691127 | 0.183487 | 0.585075 | 0.55369 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0409107 | 0.179818 | 0.608911 | 0.544333 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0096242 | 0.169007 | 0.646717 | 0.516758 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0128103 | 0.15553 | 0.667729 | 0.484149 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0293683 | 0.165551 | 0.661393 | 0.510297 |
