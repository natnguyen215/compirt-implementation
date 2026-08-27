# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.716044 |
| log_loss | 0.489612 |
| ece | 0.013727 |
| brier | 0.158877 |
| accuracy | 0.777945 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.012695 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.141948 |
| probability_p10 | 0.575835 |
| probability_p50 | 0.817341 |
| probability_p90 | 0.919423 |
| mean_predictive_variance | 0.152357 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101839 |
| joint_tossup_event_log_loss | 6.62695 |
| buzz_position_mae | 0.152336 |
| buzz_position_median_absolute_error | 0.135878 |
| buzz_position_bias | -0.0435555 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.344379 |
| first_buzzer_mean_reciprocal_rank | 0.561379 |
| first_buzzer_log_loss | 1.67439 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.716044 |
| neg_average_precision | 0.452002 |
| neg_precision | 0.612595 |
| neg_recall | 0.147113 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.18796 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0163264 |
| no_buzz_calibration_error | 0.00305676 |
| no_buzz_brier | 0.0129631 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0435555 | -0.0644456 |
| Q1 (0-.2) | 197 | 0.367397 | 0.356333 |
| Q2 (.2-.4) | 985 | 0.213363 | 0.207174 |
| Q3 (.4-.6) | 2251 | 0.0622632 | 0.0583189 |
| Q4 (.6-.8) | 2866 | -0.0731045 | -0.071 |
| Q5 (.8-1) | 2996 | -0.206284 | -0.204383 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.013727 | 0.158877 | 0.716044 | 0.489612 |
| tossup_correctness | tier | fall | 2933 | 0.00860498 | 0.147552 | 0.715771 | 0.461503 |
| tossup_correctness | tier | nationals | 1584 | 0.0415272 | 0.17641 | 0.709657 | 0.534056 |
| tossup_correctness | tier | regionals | 1886 | 0.0255329 | 0.169302 | 0.717228 | 0.511655 |
| tossup_correctness | tier | winter | 2892 | 0.0138395 | 0.153961 | 0.714661 | 0.479401 |
| tossup_correctness | category | Current Events | 124 | 0.0798045 | 0.174207 | 0.654873 | 0.53424 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0298562 | 0.164062 | 0.700216 | 0.505648 |
| tossup_correctness | category | Geography | 197 | 0.0657063 | 0.171289 | 0.776923 | 0.51985 |
| tossup_correctness | category | History | 1491 | 0.0171337 | 0.148111 | 0.723811 | 0.461911 |
| tossup_correctness | category | Literature | 1472 | 0.0230966 | 0.136776 | 0.728222 | 0.436458 |
| tossup_correctness | category | Mythology | 332 | 0.0149949 | 0.141351 | 0.677897 | 0.451197 |
| tossup_correctness | category | Other Academic | 69 | 0.0739716 | 0.165108 | 0.707014 | 0.504401 |
| tossup_correctness | category | Philosophy | 324 | 0.0168848 | 0.148682 | 0.690288 | 0.464656 |
| tossup_correctness | category | Popular Culture | 102 | 0.0522305 | 0.145179 | 0.483737 | 0.474702 |
| tossup_correctness | category | Religion | 372 | 0.0573779 | 0.184601 | 0.716786 | 0.54532 |
| tossup_correctness | category | Science | 1487 | 0.0260927 | 0.168388 | 0.691201 | 0.514441 |
| tossup_correctness | category | Social Science | 336 | 0.0696516 | 0.174455 | 0.74661 | 0.526778 |
| tossup_correctness | category | Unknown | 1886 | 0.0255329 | 0.169302 | 0.717228 | 0.511655 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0636375 | 0.164286 | 0.703316 | 0.512923 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0343811 | 0.172921 | 0.713432 | 0.522518 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0200962 | 0.160685 | 0.702525 | 0.494507 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0117263 | 0.152156 | 0.708129 | 0.473661 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0141873 | 0.158975 | 0.732662 | 0.488841 |
