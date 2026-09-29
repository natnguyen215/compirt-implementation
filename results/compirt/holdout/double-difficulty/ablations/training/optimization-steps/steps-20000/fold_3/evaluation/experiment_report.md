# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.711538 |
| log_loss | 0.485456 |
| ece | 0.0105123 |
| brier | 0.15696 |
| accuracy | 0.785683 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0156388 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.147952 |
| probability_p10 | 0.567305 |
| probability_p50 | 0.808361 |
| probability_p90 | 0.919445 |
| mean_predictive_variance | 0.154412 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0940272 |
| joint_tossup_event_log_loss | 6.42511 |
| buzz_position_mae | 0.138579 |
| buzz_position_median_absolute_error | 0.116518 |
| buzz_position_bias | -0.00852571 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.360793 |
| first_buzzer_mean_reciprocal_rank | 0.575579 |
| first_buzzer_log_loss | 1.63938 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.711538 |
| neg_average_precision | 0.448262 |
| neg_precision | 0.629562 |
| neg_recall | 0.16523 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.176998 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0108346 |
| no_buzz_calibration_error | -0.00434977 |
| no_buzz_brier | 0.0138674 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.00852571 | -0.0312584 |
| Q1 (0-.2) | 192 | 0.41296 | 0.416003 |
| Q2 (.2-.4) | 889 | 0.236241 | 0.234395 |
| Q3 (.4-.6) | 2210 | 0.0873947 | 0.0825825 |
| Q4 (.6-.8) | 2869 | -0.0378132 | -0.0356112 |
| Q5 (.8-1) | 2920 | -0.154581 | -0.145524 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0105123 | 0.15696 | 0.711538 | 0.485456 |
| tossup_correctness | tier | fall | 2817 | 0.013158 | 0.153143 | 0.703872 | 0.477309 |
| tossup_correctness | tier | nationals | 1542 | 0.0284923 | 0.169362 | 0.727782 | 0.512471 |
| tossup_correctness | tier | regionals | 1934 | 0.0156405 | 0.162159 | 0.715745 | 0.497565 |
| tossup_correctness | tier | winter | 2787 | 0.0284693 | 0.150348 | 0.702478 | 0.47034 |
| tossup_correctness | category | Current Events | 125 | 0.0664972 | 0.175636 | 0.765663 | 0.519994 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0208971 | 0.152276 | 0.729724 | 0.473498 |
| tossup_correctness | category | Geography | 185 | 0.05214 | 0.158893 | 0.783636 | 0.486493 |
| tossup_correctness | category | History | 1443 | 0.0342637 | 0.159891 | 0.724747 | 0.48769 |
| tossup_correctness | category | Literature | 1411 | 0.0260067 | 0.144467 | 0.664316 | 0.458578 |
| tossup_correctness | category | Mythology | 320 | 0.0360522 | 0.151625 | 0.661895 | 0.482047 |
| tossup_correctness | category | Other Academic | 64 | 0.130062 | 0.183751 | 0.66276 | 0.547835 |
| tossup_correctness | category | Philosophy | 312 | 0.0395023 | 0.148165 | 0.660194 | 0.466742 |
| tossup_correctness | category | Popular Culture | 104 | 0.0567299 | 0.123959 | 0.639205 | 0.413877 |
| tossup_correctness | category | Religion | 358 | 0.0404961 | 0.179685 | 0.707221 | 0.537891 |
| tossup_correctness | category | Science | 1431 | 0.024228 | 0.158297 | 0.70402 | 0.489529 |
| tossup_correctness | category | Social Science | 321 | 0.0346313 | 0.162533 | 0.723798 | 0.502194 |
| tossup_correctness | category | Unknown | 1934 | 0.0156405 | 0.162159 | 0.715745 | 0.497565 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0695305 | 0.184109 | 0.741379 | 0.542835 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0210719 | 0.163749 | 0.748783 | 0.498655 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0270515 | 0.16801 | 0.685851 | 0.515145 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.01918 | 0.149822 | 0.699939 | 0.468256 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0154338 | 0.151757 | 0.725792 | 0.472094 |
