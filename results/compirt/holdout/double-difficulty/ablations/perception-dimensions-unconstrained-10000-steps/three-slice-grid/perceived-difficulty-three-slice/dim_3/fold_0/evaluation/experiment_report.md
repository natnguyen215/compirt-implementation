# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.654189 |
| log_loss | 0.522409 |
| ece | 0.0295586 |
| brier | 0.170602 |
| accuracy | 0.763959 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.00129102 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.136436 |
| probability_p10 | 0.56103 |
| probability_p50 | 0.778376 |
| probability_p90 | 0.909699 |
| mean_predictive_variance | 0.167238 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.105474 |
| joint_tossup_event_log_loss | 7.00849 |
| buzz_position_mae | 0.163605 |
| buzz_position_median_absolute_error | 0.148395 |
| buzz_position_bias | -0.0669745 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.341689 |
| first_buzzer_mean_reciprocal_rank | 0.555851 |
| first_buzzer_log_loss | 1.72134 |
| first_buzzer_events | 9295 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.637655 |
| tossup_scorer_player_top1_accuracy | 0.312739 |
| tossup_scorer_team_top1_accuracy | 0.478662 |
| tossup_game_winner_accuracy | 0.795154 |
| tossup_game_margin_mae | 35.0713 |
| tournament_player_ppg_spearman | 0.693886 |
| tournament_player_ppg_mae | 9.36101 |
| tournament_player_ppg_top10_overlap | 0.637931 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.654189 |
| neg_average_precision | 0.37258 |
| neg_precision | 0.487755 |
| neg_recall | 0.109533 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0568494 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0901596 |
| no_buzz_calibration_error | 0.0768899 |
| no_buzz_brier | 0.0251231 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| overall | 9295 | -0.0669745 | -0.0802273 |
| Q1 (0-.2) | 197 | 0.356693 | 0.364533 |
| Q2 (.2-.4) | 985 | 0.200848 | 0.198207 |
| Q3 (.4-.6) | 2251 | 0.0485163 | 0.052509 |
| Q4 (.6-.8) | 2866 | -0.0931408 | -0.0832492 |
| Q5 (.8-1) | 2996 | -0.244626 | -0.238219 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0295586 | 0.170602 | 0.654189 | 0.522409 |
| tossup_correctness | tier | fall | 2933 | 0.0298021 | 0.157979 | 0.646763 | 0.493863 |
| tossup_correctness | tier | nationals | 1584 | 0.0494824 | 0.191471 | 0.650924 | 0.566711 |
| tossup_correctness | tier | regionals | 1886 | 0.025417 | 0.182274 | 0.638577 | 0.548156 |
| tossup_correctness | tier | winter | 2892 | 0.024753 | 0.16436 | 0.658718 | 0.510304 |
| tossup_correctness | category | Current Events | 124 | 0.0649795 | 0.171967 | 0.703087 | 0.521274 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0485868 | 0.178141 | 0.613158 | 0.544426 |
| tossup_correctness | category | Geography | 197 | 0.0721867 | 0.195145 | 0.711772 | 0.570476 |
| tossup_correctness | category | History | 1491 | 0.0681515 | 0.158685 | 0.684158 | 0.493092 |
| tossup_correctness | category | Literature | 1472 | 0.0363675 | 0.153019 | 0.627487 | 0.491971 |
| tossup_correctness | category | Mythology | 332 | 0.0761055 | 0.148604 | 0.692533 | 0.46514 |
| tossup_correctness | category | Other Academic | 69 | 0.128524 | 0.192 | 0.571267 | 0.572842 |
| tossup_correctness | category | Philosophy | 324 | 0.0352024 | 0.150276 | 0.678824 | 0.470369 |
| tossup_correctness | category | Popular Culture | 102 | 0.141108 | 0.170209 | 0.492042 | 0.52241 |
| tossup_correctness | category | Religion | 372 | 0.0511526 | 0.195758 | 0.666807 | 0.575307 |
| tossup_correctness | category | Science | 1487 | 0.0213515 | 0.172782 | 0.675149 | 0.52366 |
| tossup_correctness | category | Social Science | 336 | 0.0234128 | 0.194902 | 0.665636 | 0.573597 |
| tossup_correctness | category | Unknown | 1886 | 0.025417 | 0.182274 | 0.638577 | 0.548156 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0898989 | 0.199142 | 0.60252 | 0.590977 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0412096 | 0.18768 | 0.636132 | 0.561785 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0339941 | 0.168782 | 0.657578 | 0.516339 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0264417 | 0.160536 | 0.660704 | 0.496963 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0278693 | 0.174106 | 0.656853 | 0.533857 |
