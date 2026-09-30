# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.611355 |
| log_loss | 0.786612 |
| ece | 0.344156 |
| brier | 0.294051 |
| accuracy | 0.379559 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.385691 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0965866 |
| probability_p10 | 0.295826 |
| probability_p50 | 0.420877 |
| probability_p90 | 0.545136 |
| mean_predictive_variance | 0.234445 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0942375 |
| joint_tossup_event_log_loss | 6.7712 |
| buzz_position_mae | 0.138316 |
| buzz_position_median_absolute_error | 0.116939 |
| buzz_position_bias | -0.00475391 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.39376 |
| first_buzzer_mean_reciprocal_rank | 0.599511 |
| first_buzzer_log_loss | 1.59468 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.611355 |
| neg_average_precision | 0.31809 |
| neg_precision | 0.25589 |
| neg_recall | 0.861137 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.127483 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0496625 |
| no_buzz_calibration_error | 0.0363929 |
| no_buzz_brier | 0.0197215 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.00475391 | -0.0268712 |
| Q1 (0-.2) | 197 | 0.378414 | 0.375312 |
| Q2 (.2-.4) | 985 | 0.227006 | 0.219275 |
| Q3 (.4-.6) | 2251 | 0.085738 | 0.0844915 |
| Q4 (.6-.8) | 2866 | -0.0315585 | -0.030742 |
| Q5 (.8-1) | 2996 | -0.148493 | -0.139296 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.344156 | 0.294051 | 0.611355 | 0.786612 |
| tossup_correctness | tier | fall | 2933 | 0.372467 | 0.299763 | 0.614801 | 0.798374 |
| tossup_correctness | tier | nationals | 1584 | 0.292944 | 0.284715 | 0.576529 | 0.767642 |
| tossup_correctness | tier | regionals | 1886 | 0.320987 | 0.286025 | 0.622397 | 0.769783 |
| tossup_correctness | tier | winter | 2892 | 0.35961 | 0.298604 | 0.631551 | 0.796048 |
| tossup_correctness | category | Current Events | 124 | 0.345234 | 0.292614 | 0.623656 | 0.782536 |
| tossup_correctness | category | Fine Arts | 1103 | 0.343913 | 0.29672 | 0.608578 | 0.791902 |
| tossup_correctness | category | Geography | 197 | 0.277861 | 0.297092 | 0.568182 | 0.793981 |
| tossup_correctness | category | History | 1491 | 0.362028 | 0.291043 | 0.655412 | 0.780154 |
| tossup_correctness | category | Literature | 1472 | 0.370971 | 0.297233 | 0.565928 | 0.794005 |
| tossup_correctness | category | Mythology | 332 | 0.413072 | 0.319602 | 0.594564 | 0.838786 |
| tossup_correctness | category | Other Academic | 69 | 0.357998 | 0.304184 | 0.606335 | 0.808212 |
| tossup_correctness | category | Philosophy | 324 | 0.369973 | 0.296046 | 0.601396 | 0.79083 |
| tossup_correctness | category | Popular Culture | 102 | 0.454698 | 0.354174 | 0.488581 | 0.915339 |
| tossup_correctness | category | Religion | 372 | 0.294494 | 0.287787 | 0.610655 | 0.774487 |
| tossup_correctness | category | Science | 1487 | 0.334198 | 0.293621 | 0.606126 | 0.785608 |
| tossup_correctness | category | Social Science | 336 | 0.299379 | 0.289821 | 0.62572 | 0.775887 |
| tossup_correctness | category | Unknown | 1886 | 0.320987 | 0.286025 | 0.622397 | 0.769783 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.423244 | 0.366684 | 0.614058 | 0.950286 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.388623 | 0.337519 | 0.630559 | 0.882585 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.379348 | 0.316679 | 0.607038 | 0.834536 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.358276 | 0.291776 | 0.63517 | 0.78056 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.284863 | 0.260159 | 0.613002 | 0.714079 |
