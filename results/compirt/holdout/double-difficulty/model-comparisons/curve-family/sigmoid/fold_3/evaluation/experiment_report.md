# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.662451 |
| log_loss | 0.545967 |
| ece | 0.106769 |
| brier | 0.182832 |
| accuracy | 0.728304 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0417401 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.177724 |
| probability_p10 | 0.415175 |
| probability_p50 | 0.681217 |
| probability_p90 | 0.894823 |
| mean_predictive_variance | 0.190962 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.103799 |
| joint_tossup_event_log_loss | 6.66126 |
| buzz_position_mae | 0.158056 |
| buzz_position_median_absolute_error | 0.1398 |
| buzz_position_bias | -0.0667759 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.328304 |
| first_buzzer_mean_reciprocal_rank | 0.545185 |
| first_buzzer_log_loss | 1.72297 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.662451 |
| neg_average_precision | 0.371564 |
| neg_precision | 0.391776 |
| neg_recall | 0.328544 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.153706 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.00619646 |
| no_buzz_calibration_error | -0.00898792 |
| no_buzz_brier | 0.0140235 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0667759 | -0.0867161 |
| Q1 (0-.2) | 192 | 0.366521 | 0.368055 |
| Q2 (.2-.4) | 889 | 0.192808 | 0.189695 |
| Q3 (.4-.6) | 2210 | 0.036659 | 0.0328262 |
| Q4 (.6-.8) | 2869 | -0.0966642 | -0.095575 |
| Q5 (.8-1) | 2920 | -0.223216 | -0.216608 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.106769 | 0.182832 | 0.662451 | 0.545967 |
| tossup_correctness | tier | fall | 2817 | 0.0937297 | 0.171975 | 0.674439 | 0.521535 |
| tossup_correctness | tier | nationals | 1542 | 0.0991912 | 0.191277 | 0.663049 | 0.567365 |
| tossup_correctness | tier | regionals | 1934 | 0.121419 | 0.19396 | 0.650525 | 0.571654 |
| tossup_correctness | tier | winter | 2787 | 0.116031 | 0.181412 | 0.655721 | 0.540998 |
| tossup_correctness | category | Current Events | 125 | 0.0758941 | 0.193104 | 0.69441 | 0.563519 |
| tossup_correctness | category | Fine Arts | 1072 | 0.107762 | 0.178845 | 0.679324 | 0.536911 |
| tossup_correctness | category | Geography | 185 | 0.112849 | 0.199313 | 0.702378 | 0.577374 |
| tossup_correctness | category | History | 1443 | 0.105538 | 0.181416 | 0.679791 | 0.541628 |
| tossup_correctness | category | Literature | 1411 | 0.112615 | 0.169763 | 0.611285 | 0.520435 |
| tossup_correctness | category | Mythology | 320 | 0.0877188 | 0.161465 | 0.678955 | 0.493377 |
| tossup_correctness | category | Other Academic | 64 | 0.130823 | 0.185937 | 0.615885 | 0.555489 |
| tossup_correctness | category | Philosophy | 312 | 0.144014 | 0.175721 | 0.632839 | 0.527267 |
| tossup_correctness | category | Popular Culture | 104 | 0.0770505 | 0.136312 | 0.59304 | 0.441283 |
| tossup_correctness | category | Religion | 358 | 0.11276 | 0.202413 | 0.661028 | 0.589982 |
| tossup_correctness | category | Science | 1431 | 0.100168 | 0.186203 | 0.65131 | 0.552247 |
| tossup_correctness | category | Social Science | 321 | 0.106724 | 0.185224 | 0.696908 | 0.553785 |
| tossup_correctness | category | Unknown | 1934 | 0.121419 | 0.19396 | 0.650525 | 0.571654 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0434045 | 0.181632 | 0.736619 | 0.539285 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0226849 | 0.165031 | 0.743334 | 0.500877 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0635924 | 0.171313 | 0.680867 | 0.524497 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.116397 | 0.174503 | 0.666192 | 0.526025 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.182891 | 0.205233 | 0.644577 | 0.595977 |
