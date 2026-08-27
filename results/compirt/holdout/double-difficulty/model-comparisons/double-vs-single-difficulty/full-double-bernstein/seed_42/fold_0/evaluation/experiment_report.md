# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.7012 |
| log_loss | 0.534406 |
| ece | 0.0911489 |
| brier | 0.176486 |
| accuracy | 0.738999 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0262507 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.225645 |
| probability_p10 | 0.357266 |
| probability_p50 | 0.733844 |
| probability_p90 | 0.94907 |
| mean_predictive_variance | 0.163017 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0964519 |
| joint_tossup_event_log_loss | 6.52424 |
| buzz_position_mae | 0.13736 |
| buzz_position_median_absolute_error | 0.112736 |
| buzz_position_bias | 0.0220451 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.398171 |
| first_buzzer_mean_reciprocal_rank | 0.600895 |
| first_buzzer_log_loss | 1.59122 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.7012 |
| neg_average_precision | 0.431299 |
| neg_precision | 0.437436 |
| neg_recall | 0.390926 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.154434 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0690883 |
| no_buzz_calibration_error | 0.0558187 |
| no_buzz_brier | 0.0254653 |
| full_pmf_max_mass_error | 1.66533e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | 0.0220451 | 0.000280407 |
| Q1 (0-.2) | 197 | 0.404747 | 0.404997 |
| Q2 (.2-.4) | 985 | 0.25387 | 0.253579 |
| Q3 (.4-.6) | 2251 | 0.117485 | 0.116924 |
| Q4 (.6-.8) | 2866 | -0.00318827 | -0.000240402 |
| Q5 (.8-1) | 2996 | -0.126906 | -0.119859 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0911489 | 0.176486 | 0.7012 | 0.534406 |
| tossup_correctness | tier | fall | 2933 | 0.105435 | 0.169364 | 0.687903 | 0.52055 |
| tossup_correctness | tier | nationals | 1584 | 0.102615 | 0.196337 | 0.694071 | 0.578951 |
| tossup_correctness | tier | regionals | 1886 | 0.0857999 | 0.186655 | 0.698847 | 0.556131 |
| tossup_correctness | tier | winter | 2892 | 0.077639 | 0.166202 | 0.710853 | 0.509893 |
| tossup_correctness | category | Current Events | 124 | 0.161523 | 0.191833 | 0.681929 | 0.581074 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0838293 | 0.174282 | 0.697366 | 0.534813 |
| tossup_correctness | category | Geography | 197 | 0.12068 | 0.18162 | 0.786131 | 0.561974 |
| tossup_correctness | category | History | 1491 | 0.101083 | 0.168661 | 0.718824 | 0.510831 |
| tossup_correctness | category | Literature | 1472 | 0.082135 | 0.158749 | 0.679435 | 0.496398 |
| tossup_correctness | category | Mythology | 332 | 0.119988 | 0.167509 | 0.639486 | 0.517922 |
| tossup_correctness | category | Other Academic | 69 | 0.124171 | 0.179839 | 0.713801 | 0.526397 |
| tossup_correctness | category | Philosophy | 324 | 0.105409 | 0.167768 | 0.689932 | 0.499201 |
| tossup_correctness | category | Popular Culture | 102 | 0.16239 | 0.169486 | 0.440138 | 0.56536 |
| tossup_correctness | category | Religion | 372 | 0.093934 | 0.203735 | 0.676803 | 0.59569 |
| tossup_correctness | category | Science | 1487 | 0.10236 | 0.184868 | 0.69546 | 0.551277 |
| tossup_correctness | category | Social Science | 336 | 0.0934661 | 0.18183 | 0.741441 | 0.54884 |
| tossup_correctness | category | Unknown | 1886 | 0.0857999 | 0.186655 | 0.698847 | 0.556131 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.259335 | 0.222781 | 0.730371 | 0.638998 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.146628 | 0.203401 | 0.705256 | 0.591329 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.116904 | 0.184625 | 0.691312 | 0.555322 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0931035 | 0.168933 | 0.693662 | 0.517947 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0487767 | 0.165701 | 0.72366 | 0.508844 |
