# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.710281 |
| log_loss | 0.486178 |
| ece | 0.00762232 |
| brier | 0.157184 |
| accuracy | 0.783921 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0138767 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.140514 |
| probability_p10 | 0.583649 |
| probability_p50 | 0.812982 |
| probability_p90 | 0.918282 |
| mean_predictive_variance | 0.153208 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101498 |
| joint_tossup_event_log_loss | 6.59262 |
| buzz_position_mae | 0.152274 |
| buzz_position_median_absolute_error | 0.135428 |
| buzz_position_bias | -0.0492869 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.349009 |
| first_buzzer_mean_reciprocal_rank | 0.565576 |
| first_buzzer_log_loss | 1.67554 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.710281 |
| neg_average_precision | 0.447726 |
| neg_precision | 0.635193 |
| neg_recall | 0.141762 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.184146 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0152375 |
| no_buzz_calibration_error | 5.30907e-05 |
| no_buzz_brier | 0.0136983 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0492869 | -0.0710662 |
| Q1 (0-.2) | 192 | 0.387311 | 0.395531 |
| Q2 (.2-.4) | 889 | 0.208727 | 0.207582 |
| Q3 (.4-.6) | 2210 | 0.0556448 | 0.0540912 |
| Q4 (.6-.8) | 2869 | -0.0800651 | -0.0784863 |
| Q5 (.8-1) | 2920 | -0.205724 | -0.202375 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.00762232 | 0.157184 | 0.710281 | 0.486178 |
| tossup_correctness | tier | fall | 2817 | 0.0130997 | 0.153219 | 0.702997 | 0.477813 |
| tossup_correctness | tier | nationals | 1542 | 0.0356965 | 0.170846 | 0.725097 | 0.515939 |
| tossup_correctness | tier | regionals | 1934 | 0.0204373 | 0.162391 | 0.717364 | 0.497858 |
| tossup_correctness | tier | winter | 2787 | 0.01735 | 0.150021 | 0.698932 | 0.470061 |
| tossup_correctness | category | Current Events | 125 | 0.0702981 | 0.180697 | 0.743243 | 0.533937 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0261915 | 0.152491 | 0.725639 | 0.474523 |
| tossup_correctness | category | Geography | 185 | 0.0533878 | 0.160681 | 0.778601 | 0.490822 |
| tossup_correctness | category | History | 1443 | 0.024369 | 0.159004 | 0.727529 | 0.485888 |
| tossup_correctness | category | Literature | 1411 | 0.0265522 | 0.144491 | 0.658286 | 0.459504 |
| tossup_correctness | category | Mythology | 320 | 0.0286143 | 0.151752 | 0.664639 | 0.482644 |
| tossup_correctness | category | Other Academic | 64 | 0.167553 | 0.191623 | 0.638021 | 0.569185 |
| tossup_correctness | category | Philosophy | 312 | 0.0392921 | 0.149199 | 0.65729 | 0.468988 |
| tossup_correctness | category | Popular Culture | 104 | 0.0311901 | 0.125583 | 0.603693 | 0.421699 |
| tossup_correctness | category | Religion | 358 | 0.0434374 | 0.179173 | 0.715071 | 0.533889 |
| tossup_correctness | category | Science | 1431 | 0.0183851 | 0.1594 | 0.699853 | 0.492699 |
| tossup_correctness | category | Social Science | 321 | 0.0271297 | 0.160084 | 0.734003 | 0.494296 |
| tossup_correctness | category | Unknown | 1934 | 0.0204373 | 0.162391 | 0.717364 | 0.497858 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0777722 | 0.184578 | 0.747813 | 0.54453 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0318761 | 0.163556 | 0.751786 | 0.498225 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0247893 | 0.167404 | 0.685679 | 0.513203 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0158954 | 0.15146 | 0.692588 | 0.472925 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0128237 | 0.151333 | 0.727461 | 0.471241 |
