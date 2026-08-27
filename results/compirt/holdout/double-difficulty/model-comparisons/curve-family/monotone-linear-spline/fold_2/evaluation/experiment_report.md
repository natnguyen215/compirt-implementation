# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.656293 |
| log_loss | 0.84151 |
| ece | 0.224694 |
| brier | 0.258213 |
| accuracy | 0.635303 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.128875 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.311491 |
| probability_p10 | 0.0958291 |
| probability_p50 | 0.60076 |
| probability_p90 | 0.96047 |
| mean_predictive_variance | 0.149115 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.121379 |
| joint_tossup_event_log_loss | 8.25545 |
| buzz_position_mae | 0.152308 |
| buzz_position_median_absolute_error | 0.122274 |
| buzz_position_bias | 0.0324704 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.33445 |
| first_buzzer_mean_reciprocal_rank | 0.536049 |
| first_buzzer_log_loss | 2.50595 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.656293 |
| neg_average_precision | 0.326935 |
| neg_precision | 0.342571 |
| neg_recall | 0.594595 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.157479 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.201463 |
| no_buzz_calibration_error | 0.18835 |
| no_buzz_brier | 0.109018 |
| full_pmf_max_mass_error | 8.08609e-12 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | 0.0324704 | 0.0182685 |
| Q1 (0-.2) | 183 | 0.425886 | 0.427846 |
| Q2 (.2-.4) | 955 | 0.282373 | 0.277211 |
| Q3 (.4-.6) | 2239 | 0.133094 | 0.122912 |
| Q4 (.6-.8) | 2875 | 0.0130109 | 0.00842067 |
| Q5 (.8-1) | 3005 | -0.127264 | -0.114593 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.224694 | 0.258213 | 0.656293 | 0.84151 |
| tossup_correctness | tier | fall | 2798 | 0.151007 | 0.191674 | 0.704212 | 0.669918 |
| tossup_correctness | tier | nationals | 1545 | 0.361109 | 0.345075 | 0.692348 | 1.0801 |
| tossup_correctness | tier | regionals | 2039 | 0.274242 | 0.298498 | 0.614968 | 0.959542 |
| tossup_correctness | tier | winter | 2875 | 0.192149 | 0.247721 | 0.637596 | 0.79658 |
| tossup_correctness | category | Current Events | 129 | 0.18546 | 0.246521 | 0.679286 | 0.763365 |
| tossup_correctness | category | Fine Arts | 1074 | 0.231342 | 0.263102 | 0.639613 | 0.857981 |
| tossup_correctness | category | Geography | 180 | 0.134668 | 0.224873 | 0.733516 | 0.694301 |
| tossup_correctness | category | History | 1454 | 0.202977 | 0.238804 | 0.670016 | 0.775358 |
| tossup_correctness | category | Literature | 1435 | 0.219919 | 0.235459 | 0.659773 | 0.769415 |
| tossup_correctness | category | Mythology | 324 | 0.200744 | 0.243748 | 0.615483 | 0.874428 |
| tossup_correctness | category | Other Academic | 71 | 0.326118 | 0.343658 | 0.558824 | 1.09172 |
| tossup_correctness | category | Philosophy | 310 | 0.227593 | 0.264886 | 0.659757 | 0.820895 |
| tossup_correctness | category | Popular Culture | 108 | 0.170507 | 0.144185 | 0.611111 | 0.485548 |
| tossup_correctness | category | Religion | 361 | 0.264726 | 0.289821 | 0.635572 | 0.942842 |
| tossup_correctness | category | Science | 1445 | 0.20357 | 0.244801 | 0.687849 | 0.82223 |
| tossup_correctness | category | Social Science | 327 | 0.227373 | 0.251577 | 0.697132 | 0.797312 |
| tossup_correctness | category | Unknown | 2039 | 0.274242 | 0.298498 | 0.614968 | 0.959542 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.377027 | 0.343269 | 0.666693 | 1.1928 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.278115 | 0.299061 | 0.642968 | 1.04006 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.232729 | 0.270654 | 0.651438 | 0.903786 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.217965 | 0.246548 | 0.658684 | 0.797398 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.19889 | 0.241944 | 0.658683 | 0.75282 |
