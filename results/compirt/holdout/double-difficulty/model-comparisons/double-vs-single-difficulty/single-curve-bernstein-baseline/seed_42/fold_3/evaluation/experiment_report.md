# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.636382 |
| log_loss | 0.702133 |
| ece | 0.18366 |
| brier | 0.230074 |
| accuracy | 0.668282 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.101762 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.287892 |
| probability_p10 | 0.166087 |
| probability_p50 | 0.706749 |
| probability_p90 | 0.952088 |
| mean_predictive_variance | 0.150025 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0944123 |
| joint_tossup_event_log_loss | 6.66882 |
| buzz_position_mae | 0.136551 |
| buzz_position_median_absolute_error | 0.111917 |
| buzz_position_bias | 0.00302697 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.40815 |
| first_buzzer_mean_reciprocal_rank | 0.608509 |
| first_buzzer_log_loss | 1.58571 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.636382 |
| neg_average_precision | 0.339372 |
| neg_precision | 0.337553 |
| neg_recall | 0.45977 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.134814 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.059425 |
| no_buzz_calibration_error | 0.0442406 |
| no_buzz_brier | 0.0236257 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | 0.00302697 | -0.0160386 |
| Q1 (0-.2) | 192 | 0.394105 | 0.402555 |
| Q2 (.2-.4) | 889 | 0.227206 | 0.226051 |
| Q3 (.4-.6) | 2210 | 0.0957256 | 0.0932913 |
| Q4 (.6-.8) | 2869 | -0.0210302 | -0.0149583 |
| Q5 (.8-1) | 2920 | -0.137461 | -0.128048 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.18366 | 0.230074 | 0.636382 | 0.702133 |
| tossup_correctness | tier | fall | 2817 | 0.174613 | 0.219209 | 0.642659 | 0.653254 |
| tossup_correctness | tier | nationals | 1542 | 0.168891 | 0.244905 | 0.617114 | 0.752167 |
| tossup_correctness | tier | regionals | 1934 | 0.190273 | 0.23305 | 0.63607 | 0.728723 |
| tossup_correctness | tier | winter | 2787 | 0.196385 | 0.230785 | 0.646951 | 0.705405 |
| tossup_correctness | category | Current Events | 125 | 0.190177 | 0.249833 | 0.599816 | 0.719625 |
| tossup_correctness | category | Fine Arts | 1072 | 0.185801 | 0.245513 | 0.606336 | 0.715763 |
| tossup_correctness | category | Geography | 185 | 0.128373 | 0.23208 | 0.67007 | 0.686033 |
| tossup_correctness | category | History | 1443 | 0.168474 | 0.222947 | 0.651121 | 0.674274 |
| tossup_correctness | category | Literature | 1411 | 0.192653 | 0.220686 | 0.621693 | 0.693997 |
| tossup_correctness | category | Mythology | 320 | 0.280385 | 0.272749 | 0.568241 | 0.800944 |
| tossup_correctness | category | Other Academic | 64 | 0.215237 | 0.249937 | 0.558594 | 0.719391 |
| tossup_correctness | category | Philosophy | 312 | 0.207254 | 0.224614 | 0.673161 | 0.696017 |
| tossup_correctness | category | Popular Culture | 104 | 0.310173 | 0.292069 | 0.535511 | 0.860132 |
| tossup_correctness | category | Religion | 358 | 0.182281 | 0.228286 | 0.694349 | 0.688224 |
| tossup_correctness | category | Science | 1431 | 0.155157 | 0.214264 | 0.650851 | 0.663577 |
| tossup_correctness | category | Social Science | 321 | 0.18828 | 0.236236 | 0.645219 | 0.700094 |
| tossup_correctness | category | Unknown | 1934 | 0.190273 | 0.23305 | 0.63607 | 0.728723 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.433076 | 0.392297 | 0.688497 | 1.26725 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.328145 | 0.310479 | 0.687945 | 0.927346 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.232569 | 0.257181 | 0.649506 | 0.766547 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.159223 | 0.212666 | 0.63966 | 0.641941 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.113959 | 0.191515 | 0.62844 | 0.606798 |
