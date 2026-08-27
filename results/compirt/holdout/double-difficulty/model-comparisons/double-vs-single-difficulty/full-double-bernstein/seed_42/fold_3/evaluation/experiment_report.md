# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.712452 |
| log_loss | 0.519931 |
| ece | 0.0891749 |
| brier | 0.16935 |
| accuracy | 0.754515 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0155286 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.223504 |
| probability_p10 | 0.36407 |
| probability_p50 | 0.744311 |
| probability_p90 | 0.95177 |
| mean_predictive_variance | 0.160864 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0951629 |
| joint_tossup_event_log_loss | 6.47142 |
| buzz_position_mae | 0.136304 |
| buzz_position_median_absolute_error | 0.112171 |
| buzz_position_bias | 0.0156808 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.403524 |
| first_buzzer_mean_reciprocal_rank | 0.604489 |
| first_buzzer_log_loss | 1.58395 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.712452 |
| neg_average_precision | 0.448355 |
| neg_precision | 0.460593 |
| neg_recall | 0.394636 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.149964 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0669894 |
| no_buzz_calibration_error | 0.051805 |
| no_buzz_brier | 0.0240363 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | 0.0156808 | -0.00446494 |
| Q1 (0-.2) | 192 | 0.422556 | 0.429221 |
| Q2 (.2-.4) | 889 | 0.251083 | 0.248046 |
| Q3 (.4-.6) | 2210 | 0.110636 | 0.107379 |
| Q4 (.6-.8) | 2869 | -0.00956047 | -0.00516852 |
| Q5 (.8-1) | 2920 | -0.129808 | -0.122361 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0891749 | 0.16935 | 0.712452 | 0.519931 |
| tossup_correctness | tier | fall | 2817 | 0.0884947 | 0.164236 | 0.69997 | 0.514151 |
| tossup_correctness | tier | nationals | 1542 | 0.0965755 | 0.186148 | 0.723762 | 0.556413 |
| tossup_correctness | tier | regionals | 1934 | 0.0990387 | 0.178729 | 0.700766 | 0.540333 |
| tossup_correctness | tier | winter | 2787 | 0.0835646 | 0.158717 | 0.717519 | 0.49143 |
| tossup_correctness | category | Current Events | 125 | 0.117807 | 0.170556 | 0.770577 | 0.516817 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0794118 | 0.165644 | 0.716367 | 0.510973 |
| tossup_correctness | category | Geography | 185 | 0.114498 | 0.175593 | 0.767972 | 0.529195 |
| tossup_correctness | category | History | 1443 | 0.0867248 | 0.169503 | 0.733776 | 0.514105 |
| tossup_correctness | category | Literature | 1411 | 0.0924147 | 0.160266 | 0.658988 | 0.503597 |
| tossup_correctness | category | Mythology | 320 | 0.0969692 | 0.163299 | 0.662849 | 0.532786 |
| tossup_correctness | category | Other Academic | 64 | 0.13614 | 0.193802 | 0.630208 | 0.592293 |
| tossup_correctness | category | Philosophy | 312 | 0.0942696 | 0.161831 | 0.702839 | 0.486116 |
| tossup_correctness | category | Popular Culture | 104 | 0.105466 | 0.148258 | 0.554688 | 0.487729 |
| tossup_correctness | category | Religion | 358 | 0.102399 | 0.179477 | 0.743721 | 0.535599 |
| tossup_correctness | category | Science | 1431 | 0.0938079 | 0.167845 | 0.723959 | 0.516541 |
| tossup_correctness | category | Social Science | 321 | 0.103237 | 0.171112 | 0.74329 | 0.534476 |
| tossup_correctness | category | Unknown | 1934 | 0.0990387 | 0.178729 | 0.700766 | 0.540333 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.215334 | 0.238119 | 0.721179 | 0.690489 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.129111 | 0.179037 | 0.770075 | 0.530546 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.110239 | 0.1823 | 0.696458 | 0.555621 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0879167 | 0.162297 | 0.698122 | 0.502586 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0602655 | 0.159009 | 0.718749 | 0.495514 |
