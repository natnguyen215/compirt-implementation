# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.625956 |
| log_loss | 0.641588 |
| ece | 0.210128 |
| brier | 0.223462 |
| accuracy | 0.652535 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.12082 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.177477 |
| probability_p10 | 0.305499 |
| probability_p50 | 0.589006 |
| probability_p90 | 0.772815 |
| mean_predictive_variance | 0.214504 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0944982 |
| joint_tossup_event_log_loss | 6.72765 |
| buzz_position_mae | 0.138241 |
| buzz_position_median_absolute_error | 0.115044 |
| buzz_position_bias | 0.00368988 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.373894 |
| first_buzzer_mean_reciprocal_rank | 0.578967 |
| first_buzzer_log_loss | 1.65008 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.625956 |
| neg_average_precision | 0.317472 |
| neg_precision | 0.316152 |
| neg_recall | 0.458353 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.143305 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0474794 |
| no_buzz_calibration_error | 0.0357523 |
| no_buzz_brier | 0.0168542 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | 0.00368988 | -0.0184542 |
| Q1 (0-.2) | 179 | 0.393358 | 0.390777 |
| Q2 (.2-.4) | 957 | 0.247121 | 0.242367 |
| Q3 (.4-.6) | 2203 | 0.101742 | 0.0968268 |
| Q4 (.6-.8) | 2978 | -0.0208029 | -0.0193526 |
| Q5 (.8-1) | 2953 | -0.14727 | -0.136027 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.210128 | 0.223462 | 0.625956 | 0.641588 |
| tossup_correctness | tier | fall | 2876 | 0.211821 | 0.21378 | 0.637052 | 0.621107 |
| tossup_correctness | tier | nationals | 1579 | 0.147987 | 0.216468 | 0.619515 | 0.622886 |
| tossup_correctness | tier | regionals | 1990 | 0.208993 | 0.221407 | 0.64333 | 0.634504 |
| tossup_correctness | tier | winter | 2825 | 0.243938 | 0.238676 | 0.611035 | 0.677884 |
| tossup_correctness | category | Current Events | 123 | 0.237041 | 0.230217 | 0.669112 | 0.658491 |
| tossup_correctness | category | Fine Arts | 1093 | 0.191516 | 0.219657 | 0.620194 | 0.635035 |
| tossup_correctness | category | Geography | 191 | 0.213061 | 0.263222 | 0.594633 | 0.732089 |
| tossup_correctness | category | History | 1469 | 0.191241 | 0.220316 | 0.629914 | 0.634426 |
| tossup_correctness | category | Literature | 1436 | 0.194694 | 0.197602 | 0.6091 | 0.585264 |
| tossup_correctness | category | Mythology | 325 | 0.25723 | 0.226172 | 0.512666 | 0.648122 |
| tossup_correctness | category | Other Academic | 67 | 0.25544 | 0.243865 | 0.622642 | 0.695515 |
| tossup_correctness | category | Philosophy | 322 | 0.181987 | 0.189436 | 0.699376 | 0.562865 |
| tossup_correctness | category | Popular Culture | 100 | 0.371186 | 0.269372 | 0.53524 | 0.756286 |
| tossup_correctness | category | Religion | 365 | 0.154465 | 0.222143 | 0.64574 | 0.637598 |
| tossup_correctness | category | Science | 1456 | 0.260148 | 0.25405 | 0.598499 | 0.710524 |
| tossup_correctness | category | Social Science | 333 | 0.188045 | 0.228389 | 0.628212 | 0.649181 |
| tossup_correctness | category | Unknown | 1990 | 0.208993 | 0.221407 | 0.64333 | 0.634504 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.295674 | 0.26309 | 0.68209 | 0.730269 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.254851 | 0.254395 | 0.610397 | 0.710766 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.238345 | 0.236258 | 0.644597 | 0.674301 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.215628 | 0.217311 | 0.629767 | 0.627916 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.163877 | 0.207692 | 0.617502 | 0.603177 |
