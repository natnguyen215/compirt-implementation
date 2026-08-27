# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.716674 |
| log_loss | 0.490778 |
| ece | 0.0132066 |
| brier | 0.159601 |
| accuracy | 0.775629 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0114508 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.142124 |
| probability_p10 | 0.574596 |
| probability_p50 | 0.81342 |
| probability_p90 | 0.919344 |
| mean_predictive_variance | 0.153724 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102436 |
| joint_tossup_event_log_loss | 6.62835 |
| buzz_position_mae | 0.152216 |
| buzz_position_median_absolute_error | 0.135748 |
| buzz_position_bias | -0.0438917 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.353678 |
| first_buzzer_mean_reciprocal_rank | 0.567303 |
| first_buzzer_log_loss | 1.66646 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.716674 |
| neg_average_precision | 0.448821 |
| neg_precision | 0.603113 |
| neg_recall | 0.142006 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.190438 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0139698 |
| no_buzz_calibration_error | 0.000856746 |
| no_buzz_brier | 0.0127075 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0438917 | -0.0641727 |
| Q1 (0-.2) | 183 | 0.385918 | 0.387183 |
| Q2 (.2-.4) | 955 | 0.216096 | 0.216062 |
| Q3 (.4-.6) | 2239 | 0.0617455 | 0.0571654 |
| Q4 (.6-.8) | 2875 | -0.0692557 | -0.0696524 |
| Q5 (.8-1) | 3005 | -0.207134 | -0.207088 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0132066 | 0.159601 | 0.716674 | 0.490778 |
| tossup_correctness | tier | fall | 2798 | 0.00773537 | 0.147076 | 0.736434 | 0.458731 |
| tossup_correctness | tier | nationals | 1545 | 0.0421658 | 0.177929 | 0.716183 | 0.534697 |
| tossup_correctness | tier | regionals | 2039 | 0.0115793 | 0.162701 | 0.70358 | 0.499375 |
| tossup_correctness | tier | winter | 2875 | 0.017744 | 0.159742 | 0.704404 | 0.492266 |
| tossup_correctness | category | Current Events | 129 | 0.0961145 | 0.209036 | 0.6947 | 0.606242 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0296212 | 0.15245 | 0.713697 | 0.474454 |
| tossup_correctness | category | Geography | 180 | 0.0920089 | 0.191932 | 0.751404 | 0.569711 |
| tossup_correctness | category | History | 1454 | 0.0205583 | 0.165555 | 0.698665 | 0.507321 |
| tossup_correctness | category | Literature | 1435 | 0.0157053 | 0.134411 | 0.732433 | 0.429827 |
| tossup_correctness | category | Mythology | 324 | 0.0371451 | 0.154256 | 0.663511 | 0.483202 |
| tossup_correctness | category | Other Academic | 71 | 0.068656 | 0.178291 | 0.630719 | 0.540807 |
| tossup_correctness | category | Philosophy | 310 | 0.0444289 | 0.16072 | 0.742442 | 0.485528 |
| tossup_correctness | category | Popular Culture | 108 | 0.0720082 | 0.105754 | 0.546875 | 0.366113 |
| tossup_correctness | category | Religion | 361 | 0.053577 | 0.173802 | 0.689015 | 0.525112 |
| tossup_correctness | category | Science | 1445 | 0.0368877 | 0.166871 | 0.732037 | 0.505018 |
| tossup_correctness | category | Social Science | 327 | 0.0403352 | 0.180687 | 0.717946 | 0.537653 |
| tossup_correctness | category | Unknown | 2039 | 0.0115793 | 0.162701 | 0.70358 | 0.499375 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.0407332 | 0.17857 | 0.666145 | 0.537097 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.031617 | 0.172726 | 0.724465 | 0.522433 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0251256 | 0.161033 | 0.731098 | 0.494506 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0186253 | 0.15155 | 0.711536 | 0.469678 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0184135 | 0.160911 | 0.708767 | 0.495305 |
