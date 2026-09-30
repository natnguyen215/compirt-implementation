# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.662618 |
| log_loss | 0.51526 |
| ece | 0.013141 |
| brier | 0.168241 |
| accuracy | 0.7685 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00432105 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.111203 |
| probability_p10 | 0.619482 |
| probability_p50 | 0.790226 |
| probability_p90 | 0.899914 |
| mean_predictive_variance | 0.163687 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.103392 |
| joint_tossup_event_log_loss | 6.94297 |
| buzz_position_mae | 0.16266 |
| buzz_position_median_absolute_error | 0.145832 |
| buzz_position_bias | -0.068662 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.340499 |
| first_buzzer_mean_reciprocal_rank | 0.55678 |
| first_buzzer_log_loss | 1.69316 |
| first_buzzer_events | 9257 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.658205 |
| tossup_scorer_player_top1_accuracy | 0.317271 |
| tossup_scorer_team_top1_accuracy | 0.505224 |
| tossup_game_winner_accuracy | 0.806522 |
| tossup_game_margin_mae | 35.7605 |
| tournament_player_ppg_spearman | 0.707276 |
| tournament_player_ppg_mae | 8.7319 |
| tournament_player_ppg_top10_overlap | 0.655172 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.662618 |
| neg_average_precision | 0.390647 |
| neg_precision | 0.597087 |
| neg_recall | 0.0563445 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0553026 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0928968 |
| no_buzz_calibration_error | 0.0797838 |
| no_buzz_brier | 0.0256288 |
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
| overall | 9257 | -0.068662 | -0.0840643 |
| Q1 (0-.2) | 183 | 0.381471 | 0.391641 |
| Q2 (.2-.4) | 955 | 0.206982 | 0.208734 |
| Q3 (.4-.6) | 2239 | 0.0501428 | 0.0524469 |
| Q4 (.6-.8) | 2875 | -0.0909742 | -0.0865363 |
| Q5 (.8-1) | 3005 | -0.250849 | -0.248383 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.013141 | 0.168241 | 0.662618 | 0.51526 |
| tossup_correctness | tier | fall | 2798 | 0.0156078 | 0.156586 | 0.668246 | 0.488074 |
| tossup_correctness | tier | nationals | 1545 | 0.0343673 | 0.186137 | 0.6806 | 0.553186 |
| tossup_correctness | tier | regionals | 2039 | 0.0188443 | 0.17207 | 0.635832 | 0.524927 |
| tossup_correctness | tier | winter | 2875 | 0.0330969 | 0.16725 | 0.659123 | 0.514481 |
| tossup_correctness | category | Current Events | 129 | 0.0571466 | 0.215944 | 0.616009 | 0.623798 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0216541 | 0.164165 | 0.652848 | 0.505919 |
| tossup_correctness | category | Geography | 180 | 0.110971 | 0.210552 | 0.728946 | 0.611293 |
| tossup_correctness | category | History | 1454 | 0.0267085 | 0.171908 | 0.661481 | 0.522032 |
| tossup_correctness | category | Literature | 1435 | 0.0219925 | 0.145197 | 0.649746 | 0.464914 |
| tossup_correctness | category | Mythology | 324 | 0.0496282 | 0.157159 | 0.633544 | 0.489922 |
| tossup_correctness | category | Other Academic | 71 | 0.11643 | 0.207576 | 0.357298 | 0.612853 |
| tossup_correctness | category | Philosophy | 310 | 0.0461115 | 0.173362 | 0.649164 | 0.525985 |
| tossup_correctness | category | Popular Culture | 108 | 0.113129 | 0.117417 | 0.570312 | 0.397873 |
| tossup_correctness | category | Religion | 361 | 0.0302009 | 0.180752 | 0.643597 | 0.544943 |
| tossup_correctness | category | Science | 1445 | 0.0214327 | 0.172552 | 0.693233 | 0.523181 |
| tossup_correctness | category | Social Science | 327 | 0.0255004 | 0.181963 | 0.698797 | 0.545555 |
| tossup_correctness | category | Unknown | 2039 | 0.0188443 | 0.17207 | 0.635832 | 0.524927 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0755985 | 0.192055 | 0.59903 | 0.573697 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0352468 | 0.185644 | 0.65261 | 0.55547 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0127937 | 0.170974 | 0.678495 | 0.519994 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0183676 | 0.156837 | 0.665026 | 0.487809 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0274521 | 0.170133 | 0.65363 | 0.52166 |
