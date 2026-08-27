# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.634748 |
| log_loss | 0.737194 |
| ece | 0.200899 |
| brier | 0.24066 |
| accuracy | 0.650701 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.122654 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.295351 |
| probability_p10 | 0.142136 |
| probability_p50 | 0.678015 |
| probability_p90 | 0.947848 |
| mean_predictive_variance | 0.150998 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0964541 |
| joint_tossup_event_log_loss | 6.77235 |
| buzz_position_mae | 0.138831 |
| buzz_position_median_absolute_error | 0.115054 |
| buzz_position_bias | 0.0106881 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.392017 |
| first_buzzer_mean_reciprocal_rank | 0.598197 |
| first_buzzer_log_loss | 1.6146 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.634748 |
| neg_average_precision | 0.333952 |
| neg_precision | 0.319581 |
| neg_recall | 0.479296 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.139122 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0607584 |
| no_buzz_calibration_error | 0.0490313 |
| no_buzz_brier | 0.0227494 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | 0.0106881 | -0.00945051 |
| Q1 (0-.2) | 179 | 0.390363 | 0.394285 |
| Q2 (.2-.4) | 957 | 0.24458 | 0.238771 |
| Q3 (.4-.6) | 2203 | 0.105445 | 0.105978 |
| Q4 (.6-.8) | 2978 | -0.0105832 | -0.00614879 |
| Q5 (.8-1) | 2953 | -0.137365 | -0.128811 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.200899 | 0.24066 | 0.634748 | 0.737194 |
| tossup_correctness | tier | fall | 2876 | 0.198662 | 0.22845 | 0.644395 | 0.693623 |
| tossup_correctness | tier | nationals | 1579 | 0.185443 | 0.2453 | 0.634254 | 0.757448 |
| tossup_correctness | tier | regionals | 1990 | 0.20639 | 0.245716 | 0.636888 | 0.754049 |
| tossup_correctness | tier | winter | 2825 | 0.216197 | 0.246934 | 0.629955 | 0.758357 |
| tossup_correctness | category | Current Events | 123 | 0.198756 | 0.223223 | 0.685987 | 0.636512 |
| tossup_correctness | category | Fine Arts | 1093 | 0.208349 | 0.243773 | 0.640635 | 0.734187 |
| tossup_correctness | category | Geography | 191 | 0.183109 | 0.270289 | 0.598613 | 0.800215 |
| tossup_correctness | category | History | 1469 | 0.172438 | 0.228321 | 0.651852 | 0.685312 |
| tossup_correctness | category | Literature | 1436 | 0.217504 | 0.241601 | 0.596217 | 0.793562 |
| tossup_correctness | category | Mythology | 325 | 0.295122 | 0.275756 | 0.54537 | 0.814738 |
| tossup_correctness | category | Other Academic | 67 | 0.292361 | 0.305643 | 0.598383 | 0.908135 |
| tossup_correctness | category | Philosophy | 322 | 0.216189 | 0.222244 | 0.693017 | 0.679566 |
| tossup_correctness | category | Popular Culture | 100 | 0.331768 | 0.264725 | 0.52094 | 0.795807 |
| tossup_correctness | category | Religion | 365 | 0.180104 | 0.22652 | 0.697645 | 0.675814 |
| tossup_correctness | category | Science | 1456 | 0.182103 | 0.236913 | 0.624576 | 0.723075 |
| tossup_correctness | category | Social Science | 333 | 0.183793 | 0.235181 | 0.672291 | 0.690237 |
| tossup_correctness | category | Unknown | 1990 | 0.20639 | 0.245716 | 0.636888 | 0.754049 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.511596 | 0.455223 | 0.682255 | 1.46694 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.376765 | 0.344733 | 0.663853 | 1.05986 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.261879 | 0.274275 | 0.654539 | 0.824561 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.174733 | 0.215218 | 0.661782 | 0.653204 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.11155 | 0.194506 | 0.633926 | 0.607914 |
