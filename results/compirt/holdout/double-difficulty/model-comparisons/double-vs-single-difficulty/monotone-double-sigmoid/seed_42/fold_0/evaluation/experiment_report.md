# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.676567 |
| log_loss | 0.545948 |
| ece | 0.0759116 |
| brier | 0.179696 |
| accuracy | 0.739968 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0252824 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.202612 |
| probability_p10 | 0.420933 |
| probability_p50 | 0.744017 |
| probability_p90 | 0.930356 |
| mean_predictive_variance | 0.167638 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0937225 |
| joint_tossup_event_log_loss | 6.51586 |
| buzz_position_mae | 0.139386 |
| buzz_position_median_absolute_error | 0.118601 |
| buzz_position_bias | -0.0132276 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.397956 |
| first_buzzer_mean_reciprocal_rank | 0.602723 |
| first_buzzer_log_loss | 1.58848 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.676567 |
| neg_average_precision | 0.374013 |
| neg_precision | 0.419795 |
| neg_recall | 0.281852 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.106743 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.060445 |
| no_buzz_calibration_error | 0.0471754 |
| no_buzz_brier | 0.0225722 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0132276 | -0.0310039 |
| Q1 (0-.2) | 197 | 0.367571 | 0.370922 |
| Q2 (.2-.4) | 985 | 0.217476 | 0.212408 |
| Q3 (.4-.6) | 2251 | 0.0805321 | 0.0768494 |
| Q4 (.6-.8) | 2866 | -0.0364769 | -0.0325047 |
| Q5 (.8-1) | 2996 | -0.16232 | -0.154584 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0759116 | 0.179696 | 0.676567 | 0.545948 |
| tossup_correctness | tier | fall | 2933 | 0.0991128 | 0.172664 | 0.67867 | 0.532007 |
| tossup_correctness | tier | nationals | 1584 | 0.041073 | 0.190647 | 0.659448 | 0.567416 |
| tossup_correctness | tier | regionals | 1886 | 0.0698483 | 0.186132 | 0.674833 | 0.557427 |
| tossup_correctness | tier | winter | 2892 | 0.0796081 | 0.176634 | 0.68771 | 0.540841 |
| tossup_correctness | category | Current Events | 124 | 0.130735 | 0.189425 | 0.669788 | 0.583806 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0813719 | 0.184947 | 0.667519 | 0.56328 |
| tossup_correctness | category | Geography | 197 | 0.150608 | 0.201637 | 0.732051 | 0.621752 |
| tossup_correctness | category | History | 1491 | 0.0725818 | 0.163854 | 0.710287 | 0.50466 |
| tossup_correctness | category | Literature | 1472 | 0.0826181 | 0.16538 | 0.657567 | 0.514163 |
| tossup_correctness | category | Mythology | 332 | 0.127807 | 0.175973 | 0.629092 | 0.543703 |
| tossup_correctness | category | Other Academic | 69 | 0.121558 | 0.169333 | 0.729638 | 0.509834 |
| tossup_correctness | category | Philosophy | 324 | 0.0672991 | 0.163928 | 0.662905 | 0.497424 |
| tossup_correctness | category | Popular Culture | 102 | 0.201305 | 0.221734 | 0.539792 | 0.662575 |
| tossup_correctness | category | Religion | 372 | 0.0707777 | 0.209621 | 0.646465 | 0.614053 |
| tossup_correctness | category | Science | 1487 | 0.0817019 | 0.18578 | 0.66706 | 0.558005 |
| tossup_correctness | category | Social Science | 336 | 0.075456 | 0.191102 | 0.697119 | 0.580912 |
| tossup_correctness | category | Unknown | 1886 | 0.0698483 | 0.186132 | 0.674833 | 0.557427 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.184145 | 0.201759 | 0.722944 | 0.604112 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.105809 | 0.189653 | 0.714242 | 0.567394 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0932325 | 0.180234 | 0.668272 | 0.547289 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0717732 | 0.171535 | 0.670838 | 0.525727 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0559384 | 0.182376 | 0.673121 | 0.553408 |
