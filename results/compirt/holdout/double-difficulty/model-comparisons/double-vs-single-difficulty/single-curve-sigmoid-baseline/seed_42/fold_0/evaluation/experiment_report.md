# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.635505 |
| log_loss | 0.810881 |
| ece | 0.2202 |
| brier | 0.258354 |
| accuracy | 0.629048 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.136202 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.294526 |
| probability_p10 | 0.105318 |
| probability_p50 | 0.618551 |
| probability_p90 | 0.912996 |
| mean_predictive_variance | 0.159632 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0949991 |
| joint_tossup_event_log_loss | 6.80596 |
| buzz_position_mae | 0.144891 |
| buzz_position_median_absolute_error | 0.125541 |
| buzz_position_bias | -0.0396223 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.403012 |
| first_buzzer_mean_reciprocal_rank | 0.606287 |
| first_buzzer_log_loss | 1.60606 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.635505 |
| neg_average_precision | 0.332506 |
| neg_precision | 0.326194 |
| neg_recall | 0.544455 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0905991 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0601738 |
| no_buzz_calibration_error | 0.0469041 |
| no_buzz_brier | 0.0219085 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0396223 | -0.0542022 |
| Q1 (0-.2) | 197 | 0.335764 | 0.336534 |
| Q2 (.2-.4) | 985 | 0.191336 | 0.182842 |
| Q3 (.4-.6) | 2251 | 0.0579354 | 0.0534872 |
| Q4 (.6-.8) | 2866 | -0.0633063 | -0.0570088 |
| Q5 (.8-1) | 2996 | -0.19088 | -0.184151 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.2202 | 0.258354 | 0.635505 | 0.810881 |
| tossup_correctness | tier | fall | 2933 | 0.245867 | 0.254492 | 0.65027 | 0.813888 |
| tossup_correctness | tier | nationals | 1584 | 0.170769 | 0.253904 | 0.615128 | 0.775491 |
| tossup_correctness | tier | regionals | 1886 | 0.221472 | 0.264839 | 0.636829 | 0.833398 |
| tossup_correctness | tier | winter | 2892 | 0.228037 | 0.260478 | 0.642593 | 0.81253 |
| tossup_correctness | category | Current Events | 124 | 0.25541 | 0.276418 | 0.585848 | 0.859769 |
| tossup_correctness | category | Fine Arts | 1103 | 0.221664 | 0.2455 | 0.662633 | 0.767861 |
| tossup_correctness | category | Geography | 197 | 0.259775 | 0.301809 | 0.617016 | 0.944348 |
| tossup_correctness | category | History | 1491 | 0.218934 | 0.242874 | 0.661738 | 0.776949 |
| tossup_correctness | category | Literature | 1472 | 0.22354 | 0.252568 | 0.606507 | 0.799238 |
| tossup_correctness | category | Mythology | 332 | 0.301502 | 0.27616 | 0.614755 | 0.858441 |
| tossup_correctness | category | Other Academic | 69 | 0.272001 | 0.279432 | 0.559955 | 0.813486 |
| tossup_correctness | category | Philosophy | 324 | 0.22533 | 0.256679 | 0.582655 | 0.761078 |
| tossup_correctness | category | Popular Culture | 102 | 0.409027 | 0.38005 | 0.451903 | 1.21457 |
| tossup_correctness | category | Religion | 372 | 0.187521 | 0.274346 | 0.616898 | 0.850329 |
| tossup_correctness | category | Science | 1487 | 0.208323 | 0.253728 | 0.64027 | 0.792392 |
| tossup_correctness | category | Social Science | 336 | 0.221706 | 0.271553 | 0.639153 | 0.847092 |
| tossup_correctness | category | Unknown | 1886 | 0.221472 | 0.264839 | 0.636829 | 0.833398 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.488326 | 0.422674 | 0.678647 | 1.33165 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.388638 | 0.356641 | 0.663613 | 1.13198 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.274445 | 0.28383 | 0.64447 | 0.876196 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.192393 | 0.234196 | 0.643927 | 0.726805 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.140035 | 0.219204 | 0.630967 | 0.702424 |
