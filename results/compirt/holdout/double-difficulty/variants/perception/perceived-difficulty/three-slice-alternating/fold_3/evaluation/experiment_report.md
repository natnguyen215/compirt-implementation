# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.595645 |
| log_loss | 0.725946 |
| ece | 0.281336 |
| brier | 0.261761 |
| accuracy | 0.551872 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.218172 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.157809 |
| probability_p10 | 0.261556 |
| probability_p50 | 0.506865 |
| probability_p90 | 0.680934 |
| mean_predictive_variance | 0.224969 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0938729 |
| joint_tossup_event_log_loss | 6.82032 |
| buzz_position_mae | 0.138127 |
| buzz_position_median_absolute_error | 0.114049 |
| buzz_position_bias | -0.00854359 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.363877 |
| first_buzzer_mean_reciprocal_rank | 0.57439 |
| first_buzzer_log_loss | 1.65974 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.595645 |
| neg_average_precision | 0.302109 |
| neg_precision | 0.27555 |
| neg_recall | 0.582375 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.135005 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0477485 |
| no_buzz_calibration_error | 0.0325642 |
| no_buzz_brier | 0.0182999 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.00854359 | -0.0288137 |
| Q1 (0-.2) | 192 | 0.39768 | 0.398845 |
| Q2 (.2-.4) | 889 | 0.228426 | 0.228332 |
| Q3 (.4-.6) | 2210 | 0.0838749 | 0.0781095 |
| Q4 (.6-.8) | 2869 | -0.0343615 | -0.0307443 |
| Q5 (.8-1) | 2920 | -0.15198 | -0.142026 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.281336 | 0.261761 | 0.595645 | 0.725946 |
| tossup_correctness | tier | fall | 2817 | 0.312989 | 0.272516 | 0.601537 | 0.749855 |
| tossup_correctness | tier | nationals | 1542 | 0.211451 | 0.245229 | 0.565291 | 0.685143 |
| tossup_correctness | tier | regionals | 1934 | 0.25376 | 0.250442 | 0.619546 | 0.703075 |
| tossup_correctness | tier | winter | 2787 | 0.307144 | 0.267892 | 0.606339 | 0.740228 |
| tossup_correctness | category | Current Events | 125 | 0.231506 | 0.27087 | 0.56941 | 0.748008 |
| tossup_correctness | category | Fine Arts | 1072 | 0.284369 | 0.266359 | 0.577319 | 0.735387 |
| tossup_correctness | category | Geography | 185 | 0.260483 | 0.291719 | 0.540699 | 0.791995 |
| tossup_correctness | category | History | 1443 | 0.293998 | 0.268558 | 0.604987 | 0.740914 |
| tossup_correctness | category | Literature | 1411 | 0.294882 | 0.251716 | 0.563976 | 0.702434 |
| tossup_correctness | category | Mythology | 320 | 0.314624 | 0.272306 | 0.567526 | 0.745732 |
| tossup_correctness | category | Other Academic | 64 | 0.258009 | 0.251536 | 0.589844 | 0.69839 |
| tossup_correctness | category | Philosophy | 312 | 0.28799 | 0.238886 | 0.63929 | 0.67295 |
| tossup_correctness | category | Popular Culture | 104 | 0.458003 | 0.366001 | 0.520597 | 0.984551 |
| tossup_correctness | category | Religion | 358 | 0.263789 | 0.265453 | 0.620016 | 0.731973 |
| tossup_correctness | category | Science | 1431 | 0.285198 | 0.266817 | 0.586225 | 0.736293 |
| tossup_correctness | category | Social Science | 321 | 0.262874 | 0.260717 | 0.608378 | 0.722281 |
| tossup_correctness | category | Unknown | 1934 | 0.25376 | 0.250442 | 0.619546 | 0.703075 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.308474 | 0.28317 | 0.712301 | 0.773043 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.314667 | 0.292807 | 0.613199 | 0.795855 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.29975 | 0.273315 | 0.614929 | 0.752579 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.293894 | 0.260127 | 0.588591 | 0.72241 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.243129 | 0.243763 | 0.569783 | 0.684884 |
