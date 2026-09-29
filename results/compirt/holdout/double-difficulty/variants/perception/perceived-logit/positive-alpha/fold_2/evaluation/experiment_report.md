# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.603269 |
| log_loss | 0.78927 |
| ece | 0.344049 |
| brier | 0.295362 |
| accuracy | 0.371935 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.392244 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0973596 |
| probability_p10 | 0.293939 |
| probability_p50 | 0.42174 |
| probability_p90 | 0.544244 |
| mean_predictive_variance | 0.234142 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0955014 |
| joint_tossup_event_log_loss | 6.7806 |
| buzz_position_mae | 0.139242 |
| buzz_position_median_absolute_error | 0.115755 |
| buzz_position_bias | -0.00521591 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.383169 |
| first_buzzer_mean_reciprocal_rank | 0.592995 |
| first_buzzer_log_loss | 1.60134 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.603269 |
| neg_average_precision | 0.321043 |
| neg_precision | 0.254762 |
| neg_recall | 0.863949 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.129382 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0510545 |
| no_buzz_calibration_error | 0.0379415 |
| no_buzz_brier | 0.0197651 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.00521591 | -0.0265017 |
| Q1 (0-.2) | 183 | 0.395355 | 0.402311 |
| Q2 (.2-.4) | 955 | 0.231947 | 0.227682 |
| Q3 (.4-.6) | 2239 | 0.0878748 | 0.0831802 |
| Q4 (.6-.8) | 2875 | -0.0290798 | -0.0284059 |
| Q5 (.8-1) | 3005 | -0.151511 | -0.143712 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.344049 | 0.295362 | 0.603269 | 0.78927 |
| tossup_correctness | tier | fall | 2798 | 0.366697 | 0.29795 | 0.622021 | 0.793939 |
| tossup_correctness | tier | nationals | 1545 | 0.299993 | 0.290459 | 0.576122 | 0.779753 |
| tossup_correctness | tier | regionals | 2039 | 0.33116 | 0.287865 | 0.60889 | 0.77422 |
| tossup_correctness | tier | winter | 2875 | 0.355182 | 0.300796 | 0.602077 | 0.800514 |
| tossup_correctness | category | Current Events | 129 | 0.270243 | 0.288317 | 0.583829 | 0.7739 |
| tossup_correctness | category | Fine Arts | 1074 | 0.371257 | 0.311567 | 0.574745 | 0.823954 |
| tossup_correctness | category | Geography | 180 | 0.220135 | 0.287059 | 0.512861 | 0.771872 |
| tossup_correctness | category | History | 1454 | 0.335523 | 0.290168 | 0.61986 | 0.777689 |
| tossup_correctness | category | Literature | 1435 | 0.380791 | 0.301486 | 0.560537 | 0.802788 |
| tossup_correctness | category | Mythology | 324 | 0.390351 | 0.312151 | 0.608804 | 0.823266 |
| tossup_correctness | category | Other Academic | 71 | 0.353338 | 0.308975 | 0.546841 | 0.816627 |
| tossup_correctness | category | Philosophy | 310 | 0.355102 | 0.298536 | 0.648133 | 0.795306 |
| tossup_correctness | category | Popular Culture | 108 | 0.506385 | 0.35943 | 0.550347 | 0.925693 |
| tossup_correctness | category | Religion | 361 | 0.338196 | 0.297963 | 0.63148 | 0.794553 |
| tossup_correctness | category | Science | 1445 | 0.324722 | 0.287543 | 0.631083 | 0.772215 |
| tossup_correctness | category | Social Science | 327 | 0.300154 | 0.280385 | 0.635291 | 0.756141 |
| tossup_correctness | category | Unknown | 2039 | 0.33116 | 0.287865 | 0.60889 | 0.77422 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.440742 | 0.370955 | 0.681633 | 0.962235 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.38341 | 0.337404 | 0.630403 | 0.882442 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.365157 | 0.312204 | 0.631761 | 0.825148 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.361753 | 0.296165 | 0.603031 | 0.789535 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.292985 | 0.264081 | 0.585897 | 0.722141 |
