# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.640472 |
| log_loss | 0.514227 |
| ece | 0.0249283 |
| brier | 0.167328 |
| accuracy | 0.774973 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00161812 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.116662 |
| probability_p10 | 0.605782 |
| probability_p50 | 0.785152 |
| probability_p90 | 0.899555 |
| mean_predictive_variance | 0.165268 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102662 |
| joint_tossup_event_log_loss | 6.90431 |
| buzz_position_mae | 0.162239 |
| buzz_position_median_absolute_error | 0.148129 |
| buzz_position_bias | -0.0684378 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.369903 |
| first_buzzer_mean_reciprocal_rank | 0.578704 |
| first_buzzer_log_loss | 1.64918 |
| first_buzzer_events | 9270 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.642179 |
| tossup_scorer_player_top1_accuracy | 0.323241 |
| tossup_scorer_team_top1_accuracy | 0.492857 |
| tossup_game_winner_accuracy | 0.792123 |
| tossup_game_margin_mae | 35.546 |
| tournament_player_ppg_spearman | 0.687782 |
| tournament_player_ppg_mae | 9.24887 |
| tournament_player_ppg_top10_overlap | 0.641379 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.640472 |
| neg_average_precision | 0.355432 |
| neg_precision | 0.527076 |
| neg_recall | 0.0694907 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0552449 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.090979 |
| no_buzz_calibration_error | 0.0792519 |
| no_buzz_brier | 0.0245967 |
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
| overall | 9270 | -0.0684378 | -0.0853999 |
| Q1 (0-.2) | 179 | 0.351064 | 0.350937 |
| Q2 (.2-.4) | 957 | 0.205757 | 0.207361 |
| Q3 (.4-.6) | 2203 | 0.0518585 | 0.057204 |
| Q4 (.6-.8) | 2978 | -0.0918277 | -0.0863251 |
| Q5 (.8-1) | 2953 | -0.248882 | -0.247261 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0249283 | 0.167328 | 0.640472 | 0.514227 |
| tossup_correctness | tier | fall | 2876 | 0.0357535 | 0.159684 | 0.616397 | 0.497253 |
| tossup_correctness | tier | nationals | 1579 | 0.034557 | 0.184866 | 0.660029 | 0.552935 |
| tossup_correctness | tier | regionals | 1990 | 0.018887 | 0.168543 | 0.662914 | 0.514439 |
| tossup_correctness | tier | winter | 2825 | 0.0295005 | 0.164451 | 0.631661 | 0.509722 |
| tossup_correctness | category | Current Events | 123 | 0.0734351 | 0.173568 | 0.641966 | 0.529494 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0239916 | 0.168842 | 0.644108 | 0.516461 |
| tossup_correctness | category | Geography | 191 | 0.0592037 | 0.178233 | 0.755008 | 0.536416 |
| tossup_correctness | category | History | 1469 | 0.0387062 | 0.173798 | 0.653926 | 0.528359 |
| tossup_correctness | category | Literature | 1436 | 0.0418547 | 0.150574 | 0.590566 | 0.481024 |
| tossup_correctness | category | Mythology | 325 | 0.126943 | 0.150153 | 0.595034 | 0.476545 |
| tossup_correctness | category | Other Academic | 67 | 0.115551 | 0.1763 | 0.626685 | 0.536675 |
| tossup_correctness | category | Philosophy | 322 | 0.0305716 | 0.161015 | 0.651601 | 0.496199 |
| tossup_correctness | category | Popular Culture | 100 | 0.124962 | 0.124331 | 0.480082 | 0.416461 |
| tossup_correctness | category | Religion | 365 | 0.0589554 | 0.195663 | 0.630963 | 0.578679 |
| tossup_correctness | category | Science | 1456 | 0.0536752 | 0.169181 | 0.640776 | 0.519389 |
| tossup_correctness | category | Social Science | 333 | 0.0272879 | 0.18506 | 0.647005 | 0.553927 |
| tossup_correctness | category | Unknown | 1990 | 0.018887 | 0.168543 | 0.662914 | 0.514439 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.131711 | 0.191989 | 0.54942 | 0.574101 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0607588 | 0.186491 | 0.58866 | 0.560851 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0286295 | 0.17144 | 0.635533 | 0.523637 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0205436 | 0.157679 | 0.654813 | 0.490349 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0229163 | 0.166286 | 0.656034 | 0.512546 |
