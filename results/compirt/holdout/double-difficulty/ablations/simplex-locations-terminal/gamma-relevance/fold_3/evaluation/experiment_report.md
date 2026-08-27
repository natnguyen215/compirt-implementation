# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.714609 |
| log_loss | 0.495748 |
| ece | 0.0426126 |
| brier | 0.158427 |
| accuracy | 0.782048 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0120044 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.186289 |
| probability_p10 | 0.484836 |
| probability_p50 | 0.786782 |
| probability_p90 | 0.952541 |
| mean_predictive_variance | 0.154282 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0927023 |
| joint_tossup_event_log_loss | 6.36831 |
| buzz_position_mae | 0.134332 |
| buzz_position_median_absolute_error | 0.107694 |
| buzz_position_bias | 0.00336961 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.396366 |
| first_buzzer_mean_reciprocal_rank | 0.599602 |
| first_buzzer_log_loss | 1.58445 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.714609 |
| neg_average_precision | 0.458699 |
| neg_precision | 0.554014 |
| neg_recall | 0.26772 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.186064 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.00881237 |
| no_buzz_calibration_error | -0.00637201 |
| no_buzz_brier | 0.0131426 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | 0.00336961 | -0.0188906 |
| Q1 (0-.2) | 192 | 0.408249 | 0.418555 |
| Q2 (.2-.4) | 889 | 0.233605 | 0.231888 |
| Q3 (.4-.6) | 2210 | 0.0900708 | 0.0843764 |
| Q4 (.6-.8) | 2869 | -0.0256504 | -0.0245692 |
| Q5 (.8-1) | 2920 | -0.130455 | -0.120297 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0426126 | 0.158427 | 0.714609 | 0.495748 |
| tossup_correctness | tier | fall | 2817 | 0.045712 | 0.154196 | 0.708421 | 0.491571 |
| tossup_correctness | tier | nationals | 1542 | 0.0405911 | 0.17332 | 0.722223 | 0.52669 |
| tossup_correctness | tier | regionals | 1934 | 0.0470585 | 0.164925 | 0.708007 | 0.510417 |
| tossup_correctness | tier | winter | 2787 | 0.053582 | 0.149954 | 0.712706 | 0.472671 |
| tossup_correctness | category | Current Events | 125 | 0.0566927 | 0.17061 | 0.758907 | 0.507797 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0410436 | 0.154742 | 0.730462 | 0.486397 |
| tossup_correctness | category | Geography | 185 | 0.0856686 | 0.16852 | 0.765315 | 0.509559 |
| tossup_correctness | category | History | 1443 | 0.043816 | 0.160104 | 0.724843 | 0.49585 |
| tossup_correctness | category | Literature | 1411 | 0.0468546 | 0.146257 | 0.675314 | 0.470216 |
| tossup_correctness | category | Mythology | 320 | 0.0591356 | 0.155136 | 0.665772 | 0.51358 |
| tossup_correctness | category | Other Academic | 64 | 0.089348 | 0.181884 | 0.64974 | 0.586662 |
| tossup_correctness | category | Philosophy | 312 | 0.072749 | 0.147936 | 0.699355 | 0.460196 |
| tossup_correctness | category | Popular Culture | 104 | 0.0500205 | 0.128196 | 0.617188 | 0.433638 |
| tossup_correctness | category | Religion | 358 | 0.0667471 | 0.171546 | 0.730887 | 0.51748 |
| tossup_correctness | category | Science | 1431 | 0.0513969 | 0.1602 | 0.71264 | 0.500523 |
| tossup_correctness | category | Social Science | 321 | 0.065893 | 0.163034 | 0.744515 | 0.510975 |
| tossup_correctness | category | Unknown | 1934 | 0.0470585 | 0.164925 | 0.708007 | 0.510417 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0745776 | 0.185034 | 0.738806 | 0.54821 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0350871 | 0.160451 | 0.760413 | 0.490717 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.050657 | 0.168753 | 0.692656 | 0.528681 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0410109 | 0.152839 | 0.693169 | 0.484497 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0492018 | 0.153736 | 0.730549 | 0.47996 |
