# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.598231 |
| log_loss | 0.638274 |
| ece | 0.199603 |
| brier | 0.223357 |
| accuracy | 0.64751 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.116668 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.149097 |
| probability_p10 | 0.348333 |
| probability_p50 | 0.585101 |
| probability_p90 | 0.744333 |
| mean_predictive_variance | 0.2236 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0956429 |
| joint_tossup_event_log_loss | 6.63045 |
| buzz_position_mae | 0.13762 |
| buzz_position_median_absolute_error | 0.113412 |
| buzz_position_bias | 0.00516905 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.393216 |
| first_buzzer_mean_reciprocal_rank | 0.599262 |
| first_buzzer_log_loss | 1.58717 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.598231 |
| neg_average_precision | 0.311021 |
| neg_precision | 0.31237 |
| neg_recall | 0.411819 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.140748 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0484989 |
| no_buzz_calibration_error | 0.0353859 |
| no_buzz_brier | 0.0195912 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | 0.00516905 | -0.0160746 |
| Q1 (0-.2) | 183 | 0.402892 | 0.403539 |
| Q2 (.2-.4) | 955 | 0.238426 | 0.229624 |
| Q3 (.4-.6) | 2239 | 0.0961397 | 0.0915206 |
| Q4 (.6-.8) | 2875 | -0.0188754 | -0.0162587 |
| Q5 (.8-1) | 3005 | -0.137959 | -0.131149 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.199603 | 0.223357 | 0.598231 | 0.638274 |
| tossup_correctness | tier | fall | 2798 | 0.235812 | 0.226623 | 0.613022 | 0.644918 |
| tossup_correctness | tier | nationals | 1545 | 0.135011 | 0.221262 | 0.583892 | 0.633365 |
| tossup_correctness | tier | regionals | 2039 | 0.188153 | 0.220981 | 0.603588 | 0.633804 |
| tossup_correctness | tier | winter | 2875 | 0.207196 | 0.222989 | 0.600893 | 0.637615 |
| tossup_correctness | category | Current Events | 129 | 0.147732 | 0.242453 | 0.589778 | 0.679605 |
| tossup_correctness | category | Fine Arts | 1074 | 0.210149 | 0.227197 | 0.569469 | 0.646382 |
| tossup_correctness | category | Geography | 180 | 0.126458 | 0.257893 | 0.518214 | 0.71303 |
| tossup_correctness | category | History | 1454 | 0.193328 | 0.223076 | 0.589875 | 0.637305 |
| tossup_correctness | category | Literature | 1435 | 0.206348 | 0.20214 | 0.596647 | 0.591988 |
| tossup_correctness | category | Mythology | 324 | 0.239977 | 0.225695 | 0.595737 | 0.642429 |
| tossup_correctness | category | Other Academic | 71 | 0.22804 | 0.238811 | 0.456427 | 0.670329 |
| tossup_correctness | category | Philosophy | 310 | 0.188458 | 0.211104 | 0.6112 | 0.611323 |
| tossup_correctness | category | Popular Culture | 108 | 0.402559 | 0.282318 | 0.469618 | 0.767222 |
| tossup_correctness | category | Religion | 361 | 0.19573 | 0.228346 | 0.605481 | 0.648188 |
| tossup_correctness | category | Science | 1445 | 0.216162 | 0.236378 | 0.608301 | 0.667045 |
| tossup_correctness | category | Social Science | 327 | 0.167369 | 0.216797 | 0.651804 | 0.623284 |
| tossup_correctness | category | Unknown | 2039 | 0.188153 | 0.220981 | 0.603588 | 0.633804 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.251158 | 0.245084 | 0.665676 | 0.688049 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.209771 | 0.23675 | 0.620324 | 0.667751 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.202595 | 0.227052 | 0.618688 | 0.646718 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.217603 | 0.21996 | 0.598771 | 0.630677 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.175151 | 0.218274 | 0.568493 | 0.626851 |
