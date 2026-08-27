# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.656504 |
| log_loss | 0.82548 |
| ece | 0.229057 |
| brier | 0.257064 |
| accuracy | 0.638436 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.131608 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.316524 |
| probability_p10 | 0.095359 |
| probability_p50 | 0.60999 |
| probability_p90 | 0.968381 |
| mean_predictive_variance | 0.144988 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.119232 |
| joint_tossup_event_log_loss | 8.01229 |
| buzz_position_mae | 0.150259 |
| buzz_position_median_absolute_error | 0.119618 |
| buzz_position_bias | 0.0410777 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.327203 |
| first_buzzer_mean_reciprocal_rank | 0.530956 |
| first_buzzer_log_loss | 2.34628 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.656504 |
| neg_average_precision | 0.327548 |
| neg_precision | 0.337149 |
| neg_recall | 0.592433 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.167099 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.18554 |
| no_buzz_calibration_error | 0.170356 |
| no_buzz_brier | 0.0968644 |
| full_pmf_max_mass_error | 1.189e-11 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | 0.0410777 | 0.0233445 |
| Q1 (0-.2) | 192 | 0.462802 | 0.471083 |
| Q2 (.2-.4) | 889 | 0.286239 | 0.279934 |
| Q3 (.4-.6) | 2210 | 0.141014 | 0.137353 |
| Q4 (.6-.8) | 2869 | 0.0186021 | 0.0199531 |
| Q5 (.8-1) | 2920 | -0.114845 | -0.107142 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.229057 | 0.257064 | 0.656504 | 0.82548 |
| tossup_correctness | tier | fall | 2817 | 0.148773 | 0.19703 | 0.685601 | 0.652934 |
| tossup_correctness | tier | nationals | 1542 | 0.377623 | 0.354008 | 0.701582 | 1.10389 |
| tossup_correctness | tier | regionals | 1934 | 0.268808 | 0.293309 | 0.627574 | 0.93921 |
| tossup_correctness | tier | winter | 2787 | 0.204197 | 0.238955 | 0.63677 | 0.766923 |
| tossup_correctness | category | Current Events | 125 | 0.201502 | 0.265864 | 0.664005 | 0.794465 |
| tossup_correctness | category | Fine Arts | 1072 | 0.211228 | 0.246417 | 0.65659 | 0.765368 |
| tossup_correctness | category | Geography | 185 | 0.186779 | 0.21472 | 0.776783 | 0.687942 |
| tossup_correctness | category | History | 1443 | 0.221237 | 0.251146 | 0.681595 | 0.822567 |
| tossup_correctness | category | Literature | 1411 | 0.220195 | 0.24109 | 0.614719 | 0.762643 |
| tossup_correctness | category | Mythology | 320 | 0.229564 | 0.260532 | 0.588583 | 0.918635 |
| tossup_correctness | category | Other Academic | 64 | 0.267215 | 0.268625 | 0.595052 | 0.815955 |
| tossup_correctness | category | Philosophy | 312 | 0.25486 | 0.274644 | 0.618129 | 0.836502 |
| tossup_correctness | category | Popular Culture | 104 | 0.16567 | 0.190863 | 0.591619 | 0.702007 |
| tossup_correctness | category | Religion | 358 | 0.223147 | 0.249964 | 0.706515 | 0.791217 |
| tossup_correctness | category | Science | 1431 | 0.229347 | 0.247468 | 0.674407 | 0.803867 |
| tossup_correctness | category | Social Science | 321 | 0.209238 | 0.241335 | 0.687621 | 0.79455 |
| tossup_correctness | category | Unknown | 1934 | 0.268808 | 0.293309 | 0.627574 | 0.93921 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.368954 | 0.379101 | 0.590968 | 1.38968 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.26567 | 0.281499 | 0.688909 | 0.949859 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.245134 | 0.274129 | 0.637805 | 0.889796 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.225357 | 0.249644 | 0.646399 | 0.792162 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.200433 | 0.235975 | 0.664402 | 0.734573 |
