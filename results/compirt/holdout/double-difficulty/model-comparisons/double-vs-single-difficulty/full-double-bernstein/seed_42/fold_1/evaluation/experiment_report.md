# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.707992 |
| log_loss | 0.535206 |
| ece | 0.0922799 |
| brier | 0.174462 |
| accuracy | 0.748708 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.0134169 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.229044 |
| probability_p10 | 0.349052 |
| probability_p50 | 0.740116 |
| probability_p90 | 0.953133 |
| mean_predictive_variance | 0.16119 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0959197 |
| joint_tossup_event_log_loss | 6.53026 |
| buzz_position_mae | 0.137009 |
| buzz_position_median_absolute_error | 0.112179 |
| buzz_position_bias | 0.0171412 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.386671 |
| first_buzzer_mean_reciprocal_rank | 0.594193 |
| first_buzzer_log_loss | 1.60697 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.707992 |
| neg_average_precision | 0.451668 |
| neg_precision | 0.468196 |
| neg_recall | 0.415164 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.156363 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0713633 |
| no_buzz_calibration_error | 0.0554542 |
| no_buzz_brier | 0.0279845 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | 0.0171412 | -0.00381886 |
| Q1 (0-.2) | 167 | 0.409832 | 0.440724 |
| Q2 (.2-.4) | 912 | 0.256405 | 0.261273 |
| Q3 (.4-.6) | 2115 | 0.118332 | 0.119486 |
| Q4 (.6-.8) | 2844 | 0.000710429 | 0.00378016 |
| Q5 (.8-1) | 3055 | -0.130511 | -0.12458 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0922799 | 0.174462 | 0.707992 | 0.535206 |
| tossup_correctness | tier | fall | 2842 | 0.081732 | 0.159673 | 0.723374 | 0.495418 |
| tossup_correctness | tier | nationals | 1564 | 0.104342 | 0.196672 | 0.697911 | 0.590685 |
| tossup_correctness | tier | regionals | 1937 | 0.101655 | 0.181356 | 0.692962 | 0.559552 |
| tossup_correctness | tier | winter | 2750 | 0.092824 | 0.172259 | 0.704135 | 0.527625 |
| tossup_correctness | category | Current Events | 126 | 0.141599 | 0.194344 | 0.701386 | 0.566215 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0856095 | 0.161037 | 0.747786 | 0.493572 |
| tossup_correctness | category | Geography | 185 | 0.12457 | 0.175492 | 0.800526 | 0.540128 |
| tossup_correctness | category | History | 1440 | 0.0909054 | 0.169807 | 0.727136 | 0.525307 |
| tossup_correctness | category | Literature | 1422 | 0.0975685 | 0.165807 | 0.65758 | 0.512573 |
| tossup_correctness | category | Mythology | 318 | 0.116417 | 0.175063 | 0.625141 | 0.543315 |
| tossup_correctness | category | Other Academic | 66 | 0.0714809 | 0.137252 | 0.855543 | 0.427236 |
| tossup_correctness | category | Philosophy | 311 | 0.0683275 | 0.168002 | 0.747763 | 0.506398 |
| tossup_correctness | category | Popular Culture | 102 | 0.174176 | 0.151212 | 0.457407 | 0.508116 |
| tossup_correctness | category | Religion | 358 | 0.0741137 | 0.190992 | 0.717419 | 0.581009 |
| tossup_correctness | category | Science | 1433 | 0.0957821 | 0.188513 | 0.688847 | 0.567978 |
| tossup_correctness | category | Social Science | 324 | 0.0910079 | 0.168088 | 0.749988 | 0.510405 |
| tossup_correctness | category | Unknown | 1937 | 0.101655 | 0.181356 | 0.692962 | 0.559552 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.226653 | 0.240128 | 0.687325 | 0.689353 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.170809 | 0.209436 | 0.723607 | 0.613955 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.112319 | 0.179654 | 0.712549 | 0.549358 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0903135 | 0.168217 | 0.700191 | 0.517312 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0503253 | 0.162651 | 0.716153 | 0.510132 |
