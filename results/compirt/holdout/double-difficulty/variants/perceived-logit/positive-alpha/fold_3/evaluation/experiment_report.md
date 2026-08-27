# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.611064 |
| log_loss | 0.782683 |
| ece | 0.346736 |
| brier | 0.292505 |
| accuracy | 0.377974 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.39207 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0940351 |
| probability_p10 | 0.300311 |
| probability_p50 | 0.424666 |
| probability_p90 | 0.543286 |
| mean_predictive_variance | 0.235293 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0927016 |
| joint_tossup_event_log_loss | 6.70808 |
| buzz_position_mae | 0.136521 |
| buzz_position_median_absolute_error | 0.11352 |
| buzz_position_bias | -0.0110053 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.400551 |
| first_buzzer_mean_reciprocal_rank | 0.604022 |
| first_buzzer_log_loss | 1.57989 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.611064 |
| neg_average_precision | 0.330054 |
| neg_precision | 0.250491 |
| neg_recall | 0.855843 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.125075 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0489808 |
| no_buzz_calibration_error | 0.0337964 |
| no_buzz_brier | 0.0185553 |
| full_pmf_max_mass_error | 1.11022e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0110053 | -0.032086 |
| Q1 (0-.2) | 192 | 0.390439 | 0.397055 |
| Q2 (.2-.4) | 889 | 0.220465 | 0.220804 |
| Q3 (.4-.6) | 2210 | 0.0776924 | 0.074616 |
| Q4 (.6-.8) | 2869 | -0.0375275 | -0.0317632 |
| Q5 (.8-1) | 2920 | -0.148945 | -0.140234 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.346736 | 0.292505 | 0.611064 | 0.782683 |
| tossup_correctness | tier | fall | 2817 | 0.352948 | 0.289941 | 0.613665 | 0.776198 |
| tossup_correctness | tier | nationals | 1542 | 0.312591 | 0.292123 | 0.576756 | 0.783452 |
| tossup_correctness | tier | regionals | 1934 | 0.330877 | 0.288135 | 0.61192 | 0.77416 |
| tossup_correctness | tier | winter | 2787 | 0.370511 | 0.29834 | 0.632009 | 0.794727 |
| tossup_correctness | category | Current Events | 125 | 0.284528 | 0.281415 | 0.593366 | 0.757468 |
| tossup_correctness | category | Fine Arts | 1072 | 0.35401 | 0.300802 | 0.573614 | 0.799434 |
| tossup_correctness | category | Geography | 185 | 0.287594 | 0.283369 | 0.595804 | 0.762561 |
| tossup_correctness | category | History | 1443 | 0.342077 | 0.288791 | 0.632292 | 0.774286 |
| tossup_correctness | category | Literature | 1411 | 0.378739 | 0.295144 | 0.598528 | 0.789271 |
| tossup_correctness | category | Mythology | 320 | 0.392017 | 0.319288 | 0.554462 | 0.83947 |
| tossup_correctness | category | Other Academic | 64 | 0.354941 | 0.30414 | 0.583333 | 0.805874 |
| tossup_correctness | category | Philosophy | 312 | 0.382672 | 0.298535 | 0.625871 | 0.795495 |
| tossup_correctness | category | Popular Culture | 104 | 0.454593 | 0.343066 | 0.544744 | 0.891278 |
| tossup_correctness | category | Religion | 358 | 0.319077 | 0.288294 | 0.649686 | 0.773108 |
| tossup_correctness | category | Science | 1431 | 0.336566 | 0.285855 | 0.630914 | 0.768176 |
| tossup_correctness | category | Social Science | 321 | 0.324892 | 0.288881 | 0.620778 | 0.774781 |
| tossup_correctness | category | Unknown | 1934 | 0.330877 | 0.288135 | 0.61192 | 0.77416 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.386643 | 0.343219 | 0.699177 | 0.898676 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.383763 | 0.332213 | 0.65285 | 0.869315 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.367386 | 0.310954 | 0.630182 | 0.821598 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.359499 | 0.292006 | 0.606746 | 0.780728 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.304669 | 0.263608 | 0.596207 | 0.721149 |
