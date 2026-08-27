# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.719254 |
| log_loss | 0.574721 |
| ece | 0.123041 |
| brier | 0.185057 |
| accuracy | 0.731112 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0310129 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.27825 |
| probability_p10 | 0.244053 |
| probability_p50 | 0.750029 |
| probability_p90 | 0.981382 |
| mean_predictive_variance | 0.141038 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0924424 |
| joint_tossup_event_log_loss | 6.48355 |
| buzz_position_mae | 0.135752 |
| buzz_position_median_absolute_error | 0.111105 |
| buzz_position_bias | 0.000864922 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.393599 |
| first_buzzer_mean_reciprocal_rank | 0.598844 |
| first_buzzer_log_loss | 1.6016 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.719254 |
| neg_average_precision | 0.455225 |
| neg_precision | 0.442355 |
| neg_recall | 0.500231 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.180583 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0482587 |
| no_buzz_calibration_error | 0.0323496 |
| no_buzz_brier | 0.0199084 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | 0.000864922 | -0.0206261 |
| Q1 (0-.2) | 167 | 0.399635 | 0.414733 |
| Q2 (.2-.4) | 912 | 0.237184 | 0.231327 |
| Q3 (.4-.6) | 2115 | 0.100419 | 0.0947978 |
| Q4 (.6-.8) | 2844 | -0.0180996 | -0.0188641 |
| Q5 (.8-1) | 3055 | -0.142749 | -0.131969 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.123041 | 0.185057 | 0.719254 | 0.574721 |
| tossup_correctness | tier | fall | 2842 | 0.105658 | 0.170188 | 0.729206 | 0.533588 |
| tossup_correctness | tier | nationals | 1564 | 0.131621 | 0.202709 | 0.711564 | 0.606587 |
| tossup_correctness | tier | regionals | 1937 | 0.138278 | 0.187915 | 0.722433 | 0.581071 |
| tossup_correctness | tier | winter | 2750 | 0.133478 | 0.188372 | 0.706544 | 0.594636 |
| tossup_correctness | category | Current Events | 126 | 0.195319 | 0.203466 | 0.720583 | 0.61083 |
| tossup_correctness | category | Fine Arts | 1071 | 0.131925 | 0.185823 | 0.7179 | 0.578705 |
| tossup_correctness | category | Geography | 185 | 0.169366 | 0.194951 | 0.794297 | 0.615097 |
| tossup_correctness | category | History | 1440 | 0.110908 | 0.181253 | 0.728873 | 0.565534 |
| tossup_correctness | category | Literature | 1422 | 0.12021 | 0.170687 | 0.694899 | 0.541292 |
| tossup_correctness | category | Mythology | 318 | 0.123355 | 0.183181 | 0.686686 | 0.572465 |
| tossup_correctness | category | Other Academic | 66 | 0.113339 | 0.166947 | 0.788354 | 0.514868 |
| tossup_correctness | category | Philosophy | 311 | 0.114947 | 0.19059 | 0.718518 | 0.576117 |
| tossup_correctness | category | Popular Culture | 102 | 0.144286 | 0.133701 | 0.646296 | 0.463182 |
| tossup_correctness | category | Religion | 358 | 0.123161 | 0.202354 | 0.724729 | 0.601937 |
| tossup_correctness | category | Science | 1433 | 0.120706 | 0.193606 | 0.710107 | 0.596146 |
| tossup_correctness | category | Social Science | 324 | 0.13569 | 0.192078 | 0.714778 | 0.597403 |
| tossup_correctness | category | Unknown | 1937 | 0.138278 | 0.187915 | 0.722433 | 0.581071 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.170457 | 0.217635 | 0.704832 | 0.69131 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.1499 | 0.195499 | 0.746729 | 0.611036 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.103399 | 0.17834 | 0.731437 | 0.558242 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.115074 | 0.177424 | 0.703499 | 0.556144 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.139056 | 0.191917 | 0.714659 | 0.58621 |
