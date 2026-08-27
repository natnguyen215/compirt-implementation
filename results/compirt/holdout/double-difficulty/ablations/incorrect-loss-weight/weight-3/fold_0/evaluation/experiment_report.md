# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.711536 |
| log_loss | 0.586409 |
| ece | 0.183534 |
| brier | 0.200428 |
| accuracy | 0.696181 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0690694 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.2133 |
| probability_p10 | 0.272008 |
| probability_p50 | 0.605793 |
| probability_p90 | 0.84962 |
| mean_predictive_variance | 0.197826 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102031 |
| joint_tossup_event_log_loss | 6.71197 |
| buzz_position_mae | 0.152367 |
| buzz_position_median_absolute_error | 0.13577 |
| buzz_position_bias | -0.0425474 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.353201 |
| first_buzzer_mean_reciprocal_rank | 0.567101 |
| first_buzzer_log_loss | 1.66616 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.711536 |
| neg_average_precision | 0.440017 |
| neg_precision | 0.398546 |
| neg_recall | 0.57791 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.188025 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.015834 |
| no_buzz_calibration_error | 0.00256435 |
| no_buzz_brier | 0.0130475 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0425474 | -0.0642834 |
| Q1 (0-.2) | 197 | 0.370271 | 0.371738 |
| Q2 (.2-.4) | 985 | 0.213951 | 0.209153 |
| Q3 (.4-.6) | 2251 | 0.0626959 | 0.0585794 |
| Q4 (.6-.8) | 2866 | -0.0723389 | -0.0727173 |
| Q5 (.8-1) | 2996 | -0.204595 | -0.20214 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.183534 | 0.200428 | 0.711536 | 0.586409 |
| tossup_correctness | tier | fall | 2933 | 0.190498 | 0.193806 | 0.707401 | 0.570275 |
| tossup_correctness | tier | nationals | 1584 | 0.167889 | 0.210422 | 0.706894 | 0.610462 |
| tossup_correctness | tier | regionals | 1886 | 0.185358 | 0.210348 | 0.705842 | 0.609288 |
| tossup_correctness | tier | winter | 2892 | 0.183869 | 0.195202 | 0.71652 | 0.574678 |
| tossup_correctness | category | Current Events | 124 | 0.213371 | 0.229912 | 0.673951 | 0.652933 |
| tossup_correctness | category | Fine Arts | 1103 | 0.170641 | 0.197199 | 0.709213 | 0.579968 |
| tossup_correctness | category | Geography | 197 | 0.182742 | 0.205916 | 0.788811 | 0.61164 |
| tossup_correctness | category | History | 1491 | 0.19998 | 0.19731 | 0.717765 | 0.577463 |
| tossup_correctness | category | Literature | 1472 | 0.165625 | 0.17048 | 0.723988 | 0.518875 |
| tossup_correctness | category | Mythology | 332 | 0.193068 | 0.185982 | 0.688949 | 0.554016 |
| tossup_correctness | category | Other Academic | 69 | 0.212718 | 0.22021 | 0.664027 | 0.629123 |
| tossup_correctness | category | Philosophy | 324 | 0.210048 | 0.203085 | 0.688209 | 0.589027 |
| tossup_correctness | category | Popular Culture | 102 | 0.200925 | 0.190239 | 0.466436 | 0.574082 |
| tossup_correctness | category | Religion | 372 | 0.18512 | 0.221786 | 0.707421 | 0.631355 |
| tossup_correctness | category | Science | 1487 | 0.187892 | 0.214507 | 0.688535 | 0.617432 |
| tossup_correctness | category | Social Science | 336 | 0.16362 | 0.211084 | 0.726737 | 0.612751 |
| tossup_correctness | category | Unknown | 1886 | 0.185358 | 0.210348 | 0.705842 | 0.609288 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.245646 | 0.225187 | 0.688462 | 0.648845 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.166982 | 0.207671 | 0.704976 | 0.601307 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.179838 | 0.200452 | 0.698157 | 0.588237 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.182221 | 0.194101 | 0.70065 | 0.571007 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.19273 | 0.202455 | 0.733053 | 0.590767 |
