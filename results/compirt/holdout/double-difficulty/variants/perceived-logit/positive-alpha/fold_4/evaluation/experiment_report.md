# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.605149 |
| log_loss | 0.794659 |
| ece | 0.355254 |
| brier | 0.297911 |
| accuracy | 0.365696 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.407659 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0960255 |
| probability_p10 | 0.292812 |
| probability_p50 | 0.418688 |
| probability_p90 | 0.541562 |
| mean_predictive_variance | 0.234072 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0937598 |
| joint_tossup_event_log_loss | 6.79526 |
| buzz_position_mae | 0.137279 |
| buzz_position_median_absolute_error | 0.114722 |
| buzz_position_bias | -0.00343356 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.38986 |
| first_buzzer_mean_reciprocal_rank | 0.59549 |
| first_buzzer_log_loss | 1.62179 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.605149 |
| neg_average_precision | 0.310607 |
| neg_precision | 0.247629 |
| neg_recall | 0.882437 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.127087 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0492566 |
| no_buzz_calibration_error | 0.0375295 |
| no_buzz_brier | 0.0180395 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.00343356 | -0.024536 |
| Q1 (0-.2) | 179 | 0.388277 | 0.391446 |
| Q2 (.2-.4) | 957 | 0.231602 | 0.223389 |
| Q3 (.4-.6) | 2203 | 0.0905604 | 0.0869985 |
| Q4 (.6-.8) | 2978 | -0.0279743 | -0.0228559 |
| Q5 (.8-1) | 2953 | -0.14872 | -0.13824 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.355254 | 0.297911 | 0.605149 | 0.794659 |
| tossup_correctness | tier | fall | 2876 | 0.37131 | 0.297783 | 0.616419 | 0.793521 |
| tossup_correctness | tier | nationals | 1579 | 0.306021 | 0.287867 | 0.593644 | 0.775068 |
| tossup_correctness | tier | regionals | 1990 | 0.343994 | 0.293659 | 0.609794 | 0.786235 |
| tossup_correctness | tier | winter | 2825 | 0.37436 | 0.306652 | 0.604256 | 0.812702 |
| tossup_correctness | category | Current Events | 123 | 0.351467 | 0.291686 | 0.66471 | 0.780916 |
| tossup_correctness | category | Fine Arts | 1093 | 0.35984 | 0.302865 | 0.605463 | 0.80532 |
| tossup_correctness | category | Geography | 191 | 0.289663 | 0.297992 | 0.537108 | 0.794817 |
| tossup_correctness | category | History | 1469 | 0.33554 | 0.28803 | 0.633087 | 0.773254 |
| tossup_correctness | category | Literature | 1436 | 0.388465 | 0.303064 | 0.57542 | 0.806617 |
| tossup_correctness | category | Mythology | 325 | 0.439954 | 0.33323 | 0.492772 | 0.867287 |
| tossup_correctness | category | Other Academic | 67 | 0.406673 | 0.328079 | 0.591644 | 0.859658 |
| tossup_correctness | category | Philosophy | 322 | 0.366508 | 0.292677 | 0.66048 | 0.783272 |
| tossup_correctness | category | Popular Culture | 100 | 0.487237 | 0.343191 | 0.529111 | 0.891595 |
| tossup_correctness | category | Religion | 365 | 0.310335 | 0.284543 | 0.662091 | 0.765546 |
| tossup_correctness | category | Science | 1456 | 0.349677 | 0.299691 | 0.583128 | 0.79778 |
| tossup_correctness | category | Social Science | 333 | 0.320366 | 0.288473 | 0.646776 | 0.774059 |
| tossup_correctness | category | Unknown | 1990 | 0.343994 | 0.293659 | 0.609794 | 0.786235 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.448458 | 0.383889 | 0.602322 | 0.98917 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.408464 | 0.344462 | 0.629003 | 0.896977 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.384336 | 0.320697 | 0.628718 | 0.843575 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.366093 | 0.296039 | 0.625229 | 0.789041 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.299753 | 0.262502 | 0.598104 | 0.718883 |
