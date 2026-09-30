# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.71243 |
| log_loss | 0.498979 |
| ece | 0.0683664 |
| brier | 0.162119 |
| accuracy | 0.779075 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00903084 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.166224 |
| probability_p10 | 0.469766 |
| probability_p50 | 0.730716 |
| probability_p90 | 0.899906 |
| mean_predictive_variance | 0.18048 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.108581 |
| joint_tossup_event_log_loss | 6.73213 |
| buzz_position_mae | 0.179699 |
| buzz_position_median_absolute_error | 0.159901 |
| buzz_position_bias | -0.10347 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.345044 |
| first_buzzer_mean_reciprocal_rank | 0.558902 |
| first_buzzer_log_loss | 1.69503 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.71243 |
| neg_average_precision | 0.449944 |
| neg_precision | 0.535902 |
| neg_recall | 0.293103 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0919765 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0754861 |
| no_buzz_calibration_error | 0.0603017 |
| no_buzz_brier | 0.0222073 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.10347 | -0.116152 |
| Q1 (0-.2) | 192 | 0.344352 | 0.350479 |
| Q2 (.2-.4) | 889 | 0.172517 | 0.166542 |
| Q3 (.4-.6) | 2210 | 0.0146373 | 0.0113384 |
| Q4 (.6-.8) | 2869 | -0.129583 | -0.128154 |
| Q5 (.8-1) | 2920 | -0.280672 | -0.275361 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0683664 | 0.162119 | 0.71243 | 0.498979 |
| tossup_correctness | tier | fall | 2817 | 0.0575775 | 0.155713 | 0.70549 | 0.485931 |
| tossup_correctness | tier | nationals | 1542 | 0.0820832 | 0.178456 | 0.718207 | 0.536033 |
| tossup_correctness | tier | regionals | 1934 | 0.0714914 | 0.170103 | 0.704483 | 0.516558 |
| tossup_correctness | tier | winter | 2787 | 0.0720986 | 0.154016 | 0.712911 | 0.479466 |
| tossup_correctness | category | Current Events | 125 | 0.07365 | 0.171947 | 0.76812 | 0.515616 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0609461 | 0.155348 | 0.734946 | 0.484166 |
| tossup_correctness | category | Geography | 185 | 0.100456 | 0.16213 | 0.805594 | 0.496297 |
| tossup_correctness | category | History | 1443 | 0.0735887 | 0.160738 | 0.738687 | 0.493817 |
| tossup_correctness | category | Literature | 1411 | 0.0714299 | 0.152513 | 0.651085 | 0.478265 |
| tossup_correctness | category | Mythology | 320 | 0.0882602 | 0.161884 | 0.644834 | 0.506788 |
| tossup_correctness | category | Other Academic | 64 | 0.0941389 | 0.179076 | 0.657552 | 0.541399 |
| tossup_correctness | category | Philosophy | 312 | 0.0855802 | 0.157007 | 0.661935 | 0.489422 |
| tossup_correctness | category | Popular Culture | 104 | 0.0458609 | 0.132953 | 0.615767 | 0.432595 |
| tossup_correctness | category | Religion | 358 | 0.0810914 | 0.178063 | 0.72916 | 0.533864 |
| tossup_correctness | category | Science | 1431 | 0.0687666 | 0.164426 | 0.706477 | 0.503616 |
| tossup_correctness | category | Social Science | 321 | 0.0843783 | 0.164447 | 0.757883 | 0.506829 |
| tossup_correctness | category | Unknown | 1934 | 0.0714914 | 0.170103 | 0.704483 | 0.516558 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0889322 | 0.187062 | 0.734817 | 0.554661 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0551222 | 0.166291 | 0.749443 | 0.505893 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.063179 | 0.168476 | 0.701751 | 0.516011 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0731961 | 0.156099 | 0.697937 | 0.485202 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0745689 | 0.160314 | 0.715384 | 0.493857 |
