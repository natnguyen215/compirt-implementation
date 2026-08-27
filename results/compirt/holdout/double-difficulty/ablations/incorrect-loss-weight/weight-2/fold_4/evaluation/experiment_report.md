# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.721968 |
| log_loss | 0.517113 |
| ece | 0.119682 |
| brier | 0.170865 |
| accuracy | 0.753398 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0199569 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.189061 |
| probability_p10 | 0.379166 |
| probability_p50 | 0.685702 |
| probability_p90 | 0.875487 |
| mean_predictive_variance | 0.190641 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10125 |
| joint_tossup_event_log_loss | 6.64564 |
| buzz_position_mae | 0.150678 |
| buzz_position_median_absolute_error | 0.133454 |
| buzz_position_bias | -0.043339 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.349946 |
| first_buzzer_mean_reciprocal_rank | 0.561904 |
| first_buzzer_log_loss | 1.68465 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.721968 |
| neg_average_precision | 0.451556 |
| neg_precision | 0.451494 |
| neg_recall | 0.409805 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.185394 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0134811 |
| no_buzz_calibration_error | 0.00175403 |
| no_buzz_brier | 0.0110436 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.043339 | -0.0644287 |
| Q1 (0-.2) | 179 | 0.377678 | 0.382679 |
| Q2 (.2-.4) | 957 | 0.217642 | 0.210903 |
| Q3 (.4-.6) | 2203 | 0.0648038 | 0.0602101 |
| Q4 (.6-.8) | 2978 | -0.0713941 | -0.072532 |
| Q5 (.8-1) | 2953 | -0.205822 | -0.201565 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.119682 | 0.170865 | 0.721968 | 0.517113 |
| tossup_correctness | tier | fall | 2876 | 0.119125 | 0.162444 | 0.723498 | 0.496419 |
| tossup_correctness | tier | nationals | 1579 | 0.0977313 | 0.184342 | 0.714896 | 0.54949 |
| tossup_correctness | tier | regionals | 1990 | 0.12831 | 0.173354 | 0.734949 | 0.522796 |
| tossup_correctness | tier | winter | 2825 | 0.126536 | 0.170152 | 0.711404 | 0.516079 |
| tossup_correctness | category | Current Events | 123 | 0.15134 | 0.178321 | 0.746882 | 0.526816 |
| tossup_correctness | category | Fine Arts | 1093 | 0.105072 | 0.163324 | 0.736533 | 0.500488 |
| tossup_correctness | category | Geography | 191 | 0.128393 | 0.178145 | 0.789676 | 0.535152 |
| tossup_correctness | category | History | 1469 | 0.10509 | 0.177995 | 0.712881 | 0.532389 |
| tossup_correctness | category | Literature | 1436 | 0.112486 | 0.153515 | 0.701273 | 0.477534 |
| tossup_correctness | category | Mythology | 325 | 0.151516 | 0.152807 | 0.687205 | 0.476414 |
| tossup_correctness | category | Other Academic | 67 | 0.18709 | 0.190598 | 0.708895 | 0.563427 |
| tossup_correctness | category | Philosophy | 322 | 0.121624 | 0.178494 | 0.672681 | 0.532371 |
| tossup_correctness | category | Popular Culture | 100 | 0.143023 | 0.129521 | 0.545455 | 0.425326 |
| tossup_correctness | category | Religion | 365 | 0.101808 | 0.200953 | 0.656616 | 0.586321 |
| tossup_correctness | category | Science | 1456 | 0.133098 | 0.175601 | 0.725717 | 0.529046 |
| tossup_correctness | category | Social Science | 333 | 0.131255 | 0.182184 | 0.740375 | 0.54224 |
| tossup_correctness | category | Unknown | 1990 | 0.12831 | 0.173354 | 0.734949 | 0.522796 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.152358 | 0.183758 | 0.747927 | 0.545678 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.121522 | 0.183041 | 0.699817 | 0.545657 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.110767 | 0.171755 | 0.723225 | 0.518634 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.116506 | 0.164911 | 0.710356 | 0.503717 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.127216 | 0.171479 | 0.735359 | 0.518505 |
