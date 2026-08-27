# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.607153 |
| log_loss | 0.633846 |
| ece | 0.199908 |
| brier | 0.221247 |
| accuracy | 0.653039 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.112211 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.147883 |
| probability_p10 | 0.355818 |
| probability_p50 | 0.582117 |
| probability_p90 | 0.745891 |
| mean_predictive_variance | 0.223861 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0942424 |
| joint_tossup_event_log_loss | 6.64241 |
| buzz_position_mae | 0.136366 |
| buzz_position_median_absolute_error | 0.111625 |
| buzz_position_bias | 0.00448255 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.398924 |
| first_buzzer_mean_reciprocal_rank | 0.602392 |
| first_buzzer_log_loss | 1.59517 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.607153 |
| neg_average_precision | 0.31516 |
| neg_precision | 0.319613 |
| neg_recall | 0.423465 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.138782 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.047259 |
| no_buzz_calibration_error | 0.0339894 |
| no_buzz_brier | 0.0193613 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | 0.00448255 | -0.0187066 |
| Q1 (0-.2) | 197 | 0.37889 | 0.38165 |
| Q2 (.2-.4) | 985 | 0.231533 | 0.229257 |
| Q3 (.4-.6) | 2251 | 0.0933391 | 0.0891406 |
| Q4 (.6-.8) | 2866 | -0.0234047 | -0.021605 |
| Q5 (.8-1) | 2996 | -0.134868 | -0.125489 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.199908 | 0.221247 | 0.607153 | 0.633846 |
| tossup_correctness | tier | fall | 2933 | 0.236652 | 0.222436 | 0.620011 | 0.636276 |
| tossup_correctness | tier | nationals | 1584 | 0.126629 | 0.218816 | 0.580293 | 0.628381 |
| tossup_correctness | tier | regionals | 1886 | 0.183926 | 0.221349 | 0.623963 | 0.634498 |
| tossup_correctness | tier | winter | 2892 | 0.213319 | 0.221305 | 0.614102 | 0.633949 |
| tossup_correctness | category | Current Events | 124 | 0.240626 | 0.24632 | 0.591398 | 0.690699 |
| tossup_correctness | category | Fine Arts | 1103 | 0.181991 | 0.215227 | 0.617886 | 0.620777 |
| tossup_correctness | category | Geography | 197 | 0.175077 | 0.259519 | 0.529487 | 0.714892 |
| tossup_correctness | category | History | 1491 | 0.226046 | 0.216072 | 0.626891 | 0.622606 |
| tossup_correctness | category | Literature | 1472 | 0.187743 | 0.199779 | 0.59475 | 0.586983 |
| tossup_correctness | category | Mythology | 332 | 0.261594 | 0.229975 | 0.555018 | 0.653253 |
| tossup_correctness | category | Other Academic | 69 | 0.22183 | 0.219401 | 0.61991 | 0.630911 |
| tossup_correctness | category | Philosophy | 324 | 0.197295 | 0.209118 | 0.550639 | 0.606413 |
| tossup_correctness | category | Popular Culture | 102 | 0.361091 | 0.292471 | 0.483045 | 0.785987 |
| tossup_correctness | category | Religion | 372 | 0.156128 | 0.233389 | 0.585543 | 0.659238 |
| tossup_correctness | category | Science | 1487 | 0.217704 | 0.235017 | 0.599218 | 0.663919 |
| tossup_correctness | category | Social Science | 336 | 0.173444 | 0.233196 | 0.602839 | 0.660258 |
| tossup_correctness | category | Unknown | 1886 | 0.183926 | 0.221349 | 0.623963 | 0.634498 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.230705 | 0.24247 | 0.637666 | 0.682059 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.216224 | 0.240867 | 0.609333 | 0.675937 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.213807 | 0.225814 | 0.599061 | 0.643841 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.214196 | 0.21661 | 0.616111 | 0.623607 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.168776 | 0.214405 | 0.599867 | 0.619123 |
