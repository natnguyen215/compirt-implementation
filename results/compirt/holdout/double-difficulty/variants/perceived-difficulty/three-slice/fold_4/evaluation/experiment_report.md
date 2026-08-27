# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.608341 |
| log_loss | 0.707005 |
| ece | 0.266491 |
| brier | 0.252211 |
| accuracy | 0.589752 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.183603 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.168339 |
| probability_p10 | 0.260836 |
| probability_p50 | 0.529282 |
| probability_p90 | 0.711663 |
| mean_predictive_variance | 0.221615 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0942462 |
| joint_tossup_event_log_loss | 6.83365 |
| buzz_position_mae | 0.137579 |
| buzz_position_median_absolute_error | 0.114038 |
| buzz_position_bias | 0.000685034 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.371953 |
| first_buzzer_mean_reciprocal_rank | 0.578874 |
| first_buzzer_log_loss | 1.65152 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.608341 |
| neg_average_precision | 0.303221 |
| neg_precision | 0.289043 |
| neg_recall | 0.554974 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.137581 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0503501 |
| no_buzz_calibration_error | 0.038623 |
| no_buzz_brier | 0.018078 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | 0.000685034 | -0.0217262 |
| Q1 (0-.2) | 179 | 0.391992 | 0.395202 |
| Q2 (.2-.4) | 957 | 0.240748 | 0.236333 |
| Q3 (.4-.6) | 2203 | 0.0970568 | 0.0947411 |
| Q4 (.6-.8) | 2978 | -0.0244558 | -0.0216653 |
| Q5 (.8-1) | 2953 | -0.147375 | -0.135603 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.266491 | 0.252211 | 0.608341 | 0.707005 |
| tossup_correctness | tier | fall | 2876 | 0.298529 | 0.259212 | 0.618606 | 0.724884 |
| tossup_correctness | tier | nationals | 1579 | 0.192271 | 0.234076 | 0.605238 | 0.6614 |
| tossup_correctness | tier | regionals | 1990 | 0.251322 | 0.244686 | 0.624603 | 0.68948 |
| tossup_correctness | tier | winter | 2825 | 0.286045 | 0.26052 | 0.600731 | 0.726639 |
| tossup_correctness | category | Current Events | 123 | 0.287182 | 0.252775 | 0.671313 | 0.705112 |
| tossup_correctness | category | Fine Arts | 1093 | 0.257702 | 0.249098 | 0.618812 | 0.701428 |
| tossup_correctness | category | Geography | 191 | 0.242536 | 0.291132 | 0.527478 | 0.795713 |
| tossup_correctness | category | History | 1469 | 0.260609 | 0.254275 | 0.60815 | 0.709847 |
| tossup_correctness | category | Literature | 1436 | 0.280524 | 0.238001 | 0.600583 | 0.676469 |
| tossup_correctness | category | Mythology | 325 | 0.341984 | 0.278783 | 0.448333 | 0.763489 |
| tossup_correctness | category | Other Academic | 67 | 0.315261 | 0.269353 | 0.618598 | 0.747598 |
| tossup_correctness | category | Philosophy | 322 | 0.251514 | 0.222485 | 0.678868 | 0.638561 |
| tossup_correctness | category | Popular Culture | 100 | 0.432063 | 0.308454 | 0.531154 | 0.840779 |
| tossup_correctness | category | Religion | 365 | 0.224077 | 0.247507 | 0.634188 | 0.695726 |
| tossup_correctness | category | Science | 1456 | 0.277923 | 0.268082 | 0.582896 | 0.744964 |
| tossup_correctness | category | Social Science | 333 | 0.238568 | 0.255261 | 0.598537 | 0.708104 |
| tossup_correctness | category | Unknown | 1990 | 0.251322 | 0.244686 | 0.624603 | 0.68948 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.348357 | 0.306445 | 0.616086 | 0.825926 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.307153 | 0.281803 | 0.612012 | 0.773728 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.293512 | 0.266351 | 0.63021 | 0.742416 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.277693 | 0.251285 | 0.602895 | 0.704648 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.216897 | 0.229717 | 0.603014 | 0.654132 |
