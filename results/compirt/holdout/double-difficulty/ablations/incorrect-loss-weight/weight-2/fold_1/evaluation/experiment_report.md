# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.709228 |
| log_loss | 0.532209 |
| ece | 0.10994 |
| brier | 0.176749 |
| accuracy | 0.745958 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0161663 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.194779 |
| probability_p10 | 0.365932 |
| probability_p50 | 0.688474 |
| probability_p90 | 0.880393 |
| mean_predictive_variance | 0.188487 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100931 |
| joint_tossup_event_log_loss | 6.64259 |
| buzz_position_mae | 0.151387 |
| buzz_position_median_absolute_error | 0.13403 |
| buzz_position_bias | -0.0480406 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.351039 |
| first_buzzer_mean_reciprocal_rank | 0.562887 |
| first_buzzer_log_loss | 1.68294 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.709228 |
| neg_average_precision | 0.445145 |
| neg_precision | 0.462671 |
| neg_recall | 0.421174 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.190501 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0151147 |
| no_buzz_calibration_error | -0.000794359 |
| no_buzz_brier | 0.0154285 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0480406 | -0.0685815 |
| Q1 (0-.2) | 167 | 0.373886 | 0.378778 |
| Q2 (.2-.4) | 912 | 0.213176 | 0.213309 |
| Q3 (.4-.6) | 2115 | 0.0621387 | 0.059024 |
| Q4 (.6-.8) | 2844 | -0.0692873 | -0.0711113 |
| Q5 (.8-1) | 3055 | -0.205584 | -0.202701 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.10994 | 0.176749 | 0.709228 | 0.532209 |
| tossup_correctness | tier | fall | 2842 | 0.109479 | 0.164218 | 0.726047 | 0.501713 |
| tossup_correctness | tier | nationals | 1564 | 0.0940044 | 0.186841 | 0.714956 | 0.556395 |
| tossup_correctness | tier | regionals | 1937 | 0.113824 | 0.183829 | 0.68628 | 0.550017 |
| tossup_correctness | tier | winter | 2750 | 0.119137 | 0.178972 | 0.699964 | 0.537429 |
| tossup_correctness | category | Current Events | 126 | 0.172255 | 0.188069 | 0.71454 | 0.556187 |
| tossup_correctness | category | Fine Arts | 1071 | 0.118301 | 0.168013 | 0.745462 | 0.509881 |
| tossup_correctness | category | Geography | 185 | 0.160833 | 0.186388 | 0.789037 | 0.560805 |
| tossup_correctness | category | History | 1440 | 0.0956915 | 0.179552 | 0.707024 | 0.537209 |
| tossup_correctness | category | Literature | 1422 | 0.118506 | 0.161149 | 0.677939 | 0.4961 |
| tossup_correctness | category | Mythology | 318 | 0.132596 | 0.168372 | 0.666052 | 0.517681 |
| tossup_correctness | category | Other Academic | 66 | 0.130767 | 0.16451 | 0.81411 | 0.507052 |
| tossup_correctness | category | Philosophy | 311 | 0.0937828 | 0.176558 | 0.720864 | 0.527313 |
| tossup_correctness | category | Popular Culture | 102 | 0.156356 | 0.132091 | 0.535185 | 0.438028 |
| tossup_correctness | category | Religion | 358 | 0.112204 | 0.193023 | 0.715553 | 0.571591 |
| tossup_correctness | category | Science | 1433 | 0.100152 | 0.187096 | 0.696257 | 0.55526 |
| tossup_correctness | category | Social Science | 324 | 0.113674 | 0.170613 | 0.779281 | 0.518431 |
| tossup_correctness | category | Unknown | 1937 | 0.113824 | 0.183829 | 0.68628 | 0.550017 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.130441 | 0.218041 | 0.619573 | 0.63498 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.108051 | 0.187033 | 0.723065 | 0.553881 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0970417 | 0.1747 | 0.711127 | 0.528005 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.109749 | 0.17098 | 0.692603 | 0.519505 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.12227 | 0.178211 | 0.720568 | 0.534859 |
