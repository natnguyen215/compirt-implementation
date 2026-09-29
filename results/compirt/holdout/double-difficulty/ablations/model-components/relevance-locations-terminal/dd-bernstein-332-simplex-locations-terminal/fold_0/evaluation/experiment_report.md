# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.716142 |
| log_loss | 0.48962 |
| ece | 0.0133403 |
| brier | 0.159161 |
| accuracy | 0.776439 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0111888 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.139301 |
| probability_p10 | 0.58301 |
| probability_p50 | 0.815306 |
| probability_p90 | 0.916788 |
| mean_predictive_variance | 0.1538 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102139 |
| joint_tossup_event_log_loss | 6.62402 |
| buzz_position_mae | 0.152571 |
| buzz_position_median_absolute_error | 0.135821 |
| buzz_position_bias | -0.0425869 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.354492 |
| first_buzzer_mean_reciprocal_rank | 0.567756 |
| first_buzzer_log_loss | 1.66891 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.716142 |
| neg_average_precision | 0.448805 |
| neg_precision | 0.602767 |
| neg_recall | 0.13978 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.188776 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0159887 |
| no_buzz_calibration_error | 0.00271904 |
| no_buzz_brier | 0.0131148 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0425869 | -0.0647335 |
| Q1 (0-.2) | 197 | 0.367599 | 0.371464 |
| Q2 (.2-.4) | 985 | 0.214186 | 0.206115 |
| Q3 (.4-.6) | 2251 | 0.0637293 | 0.0614807 |
| Q4 (.6-.8) | 2866 | -0.0718866 | -0.0738042 |
| Q5 (.8-1) | 2996 | -0.205829 | -0.202576 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0133403 | 0.159161 | 0.716142 | 0.48962 |
| tossup_correctness | tier | fall | 2933 | 0.0112251 | 0.147846 | 0.712571 | 0.462227 |
| tossup_correctness | tier | nationals | 1584 | 0.0414397 | 0.175851 | 0.711483 | 0.531811 |
| tossup_correctness | tier | regionals | 1886 | 0.0271974 | 0.170457 | 0.711517 | 0.515254 |
| tossup_correctness | tier | winter | 2892 | 0.0141196 | 0.15413 | 0.721437 | 0.477577 |
| tossup_correctness | category | Current Events | 124 | 0.103316 | 0.169467 | 0.676032 | 0.52432 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0212368 | 0.161489 | 0.709997 | 0.497223 |
| tossup_correctness | category | Geography | 197 | 0.0760247 | 0.171724 | 0.787179 | 0.520246 |
| tossup_correctness | category | History | 1491 | 0.021979 | 0.148166 | 0.727094 | 0.461459 |
| tossup_correctness | category | Literature | 1472 | 0.0300489 | 0.137627 | 0.730607 | 0.43733 |
| tossup_correctness | category | Mythology | 332 | 0.0139834 | 0.140843 | 0.693608 | 0.447439 |
| tossup_correctness | category | Other Academic | 69 | 0.060565 | 0.166727 | 0.70362 | 0.506584 |
| tossup_correctness | category | Philosophy | 324 | 0.0293709 | 0.147901 | 0.692664 | 0.463162 |
| tossup_correctness | category | Popular Culture | 102 | 0.0526914 | 0.148114 | 0.431834 | 0.483678 |
| tossup_correctness | category | Religion | 372 | 0.0491465 | 0.183004 | 0.718996 | 0.541918 |
| tossup_correctness | category | Science | 1487 | 0.0272721 | 0.169422 | 0.688799 | 0.515349 |
| tossup_correctness | category | Social Science | 336 | 0.0506844 | 0.179035 | 0.729788 | 0.537812 |
| tossup_correctness | category | Unknown | 1886 | 0.0271974 | 0.170457 | 0.711517 | 0.515254 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.069003 | 0.167566 | 0.691379 | 0.523192 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.027369 | 0.172452 | 0.717047 | 0.519918 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0195998 | 0.161179 | 0.70037 | 0.495315 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0144652 | 0.152648 | 0.70366 | 0.475045 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0236665 | 0.158955 | 0.737426 | 0.487116 |
