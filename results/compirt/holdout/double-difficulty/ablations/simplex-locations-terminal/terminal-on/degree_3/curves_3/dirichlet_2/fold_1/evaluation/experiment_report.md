# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.712897 |
| log_loss | 0.506502 |
| ece | 0.0683872 |
| brier | 0.165227 |
| accuracy | 0.768393 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00626856 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.165405 |
| probability_p10 | 0.464632 |
| probability_p50 | 0.724465 |
| probability_p90 | 0.894359 |
| mean_predictive_variance | 0.183244 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.109369 |
| joint_tossup_event_log_loss | 6.71536 |
| buzz_position_mae | 0.166176 |
| buzz_position_median_absolute_error | 0.150058 |
| buzz_position_bias | -0.0802368 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.324865 |
| first_buzzer_mean_reciprocal_rank | 0.541873 |
| first_buzzer_log_loss | 1.72113 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.712897 |
| neg_average_precision | 0.460498 |
| neg_precision | 0.523573 |
| neg_recall | 0.292649 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.176796 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0120081 |
| no_buzz_calibration_error | -0.00390101 |
| no_buzz_brier | 0.0148396 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0802368 | -0.0993482 |
| Q1 (0-.2) | 167 | 0.349413 | 0.359099 |
| Q2 (.2-.4) | 912 | 0.191887 | 0.190866 |
| Q3 (.4-.6) | 2115 | 0.0346452 | 0.0316926 |
| Q4 (.6-.8) | 2844 | -0.101926 | -0.103748 |
| Q5 (.8-1) | 3055 | -0.244302 | -0.241513 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0683872 | 0.165227 | 0.712897 | 0.506502 |
| tossup_correctness | tier | fall | 2842 | 0.0590309 | 0.15199 | 0.728216 | 0.472829 |
| tossup_correctness | tier | nationals | 1564 | 0.0687069 | 0.181744 | 0.715552 | 0.54511 |
| tossup_correctness | tier | regionals | 1937 | 0.0818161 | 0.172665 | 0.694469 | 0.525126 |
| tossup_correctness | tier | winter | 2750 | 0.07111 | 0.164276 | 0.701647 | 0.506227 |
| tossup_correctness | category | Current Events | 126 | 0.119823 | 0.170989 | 0.727693 | 0.517963 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0738882 | 0.157245 | 0.738582 | 0.486659 |
| tossup_correctness | category | Geography | 185 | 0.118064 | 0.170127 | 0.79222 | 0.524708 |
| tossup_correctness | category | History | 1440 | 0.0523436 | 0.166502 | 0.71657 | 0.508441 |
| tossup_correctness | category | Literature | 1422 | 0.0797499 | 0.147072 | 0.697791 | 0.462426 |
| tossup_correctness | category | Mythology | 318 | 0.0646192 | 0.152164 | 0.704406 | 0.477015 |
| tossup_correctness | category | Other Academic | 66 | 0.104194 | 0.167441 | 0.802912 | 0.510113 |
| tossup_correctness | category | Philosophy | 311 | 0.0451585 | 0.169432 | 0.721519 | 0.511393 |
| tossup_correctness | category | Popular Culture | 102 | 0.140554 | 0.128768 | 0.426852 | 0.43626 |
| tossup_correctness | category | Religion | 358 | 0.0741005 | 0.185481 | 0.700438 | 0.555014 |
| tossup_correctness | category | Science | 1433 | 0.0573474 | 0.176352 | 0.695841 | 0.533265 |
| tossup_correctness | category | Social Science | 324 | 0.0741581 | 0.164355 | 0.757408 | 0.504389 |
| tossup_correctness | category | Unknown | 1937 | 0.0818161 | 0.172665 | 0.694469 | 0.525126 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0929508 | 0.198101 | 0.66159 | 0.580394 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0695901 | 0.177941 | 0.719686 | 0.534076 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0506218 | 0.163741 | 0.725177 | 0.502608 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.077217 | 0.161284 | 0.69259 | 0.498609 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.076003 | 0.164335 | 0.719628 | 0.504276 |
