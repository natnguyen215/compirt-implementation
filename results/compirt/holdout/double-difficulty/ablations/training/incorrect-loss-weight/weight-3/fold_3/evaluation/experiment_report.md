# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.705391 |
| log_loss | 0.587886 |
| ece | 0.187252 |
| brier | 0.201189 |
| accuracy | 0.688546 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0814978 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.215229 |
| probability_p10 | 0.276253 |
| probability_p50 | 0.605816 |
| probability_p90 | 0.851748 |
| mean_predictive_variance | 0.196822 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.101221 |
| joint_tossup_event_log_loss | 6.68204 |
| buzz_position_mae | 0.151899 |
| buzz_position_median_absolute_error | 0.135361 |
| buzz_position_bias | -0.0490756 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.348678 |
| first_buzzer_mean_reciprocal_rank | 0.566351 |
| first_buzzer_log_loss | 1.67099 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.705391 |
| neg_average_precision | 0.444574 |
| neg_precision | 0.38254 |
| neg_recall | 0.577107 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.183477 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0152012 |
| no_buzz_calibration_error | 1.68492e-05 |
| no_buzz_brier | 0.0136857 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0490756 | -0.069508 |
| Q1 (0-.2) | 192 | 0.387421 | 0.394103 |
| Q2 (.2-.4) | 889 | 0.207216 | 0.207518 |
| Q3 (.4-.6) | 2210 | 0.0554792 | 0.0528267 |
| Q4 (.6-.8) | 2869 | -0.0799981 | -0.077213 |
| Q5 (.8-1) | 2920 | -0.204555 | -0.201452 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.187252 | 0.201189 | 0.705391 | 0.587886 |
| tossup_correctness | tier | fall | 2817 | 0.179398 | 0.195608 | 0.698596 | 0.575936 |
| tossup_correctness | tier | nationals | 1542 | 0.190383 | 0.21035 | 0.722327 | 0.60849 |
| tossup_correctness | tier | regionals | 1934 | 0.181333 | 0.202855 | 0.707143 | 0.591154 |
| tossup_correctness | tier | winter | 2787 | 0.199806 | 0.200605 | 0.695505 | 0.586296 |
| tossup_correctness | category | Current Events | 125 | 0.166055 | 0.208487 | 0.734951 | 0.598016 |
| tossup_correctness | category | Fine Arts | 1072 | 0.18857 | 0.197846 | 0.719192 | 0.579028 |
| tossup_correctness | category | Geography | 185 | 0.21329 | 0.217327 | 0.764196 | 0.62664 |
| tossup_correctness | category | History | 1443 | 0.197041 | 0.202433 | 0.732392 | 0.591032 |
| tossup_correctness | category | Literature | 1411 | 0.174549 | 0.18562 | 0.656084 | 0.553746 |
| tossup_correctness | category | Mythology | 320 | 0.183985 | 0.192521 | 0.661775 | 0.572856 |
| tossup_correctness | category | Other Academic | 64 | 0.202636 | 0.220351 | 0.636719 | 0.639543 |
| tossup_correctness | category | Philosophy | 312 | 0.199172 | 0.194941 | 0.668903 | 0.567997 |
| tossup_correctness | category | Popular Culture | 104 | 0.198534 | 0.166774 | 0.59517 | 0.51843 |
| tossup_correctness | category | Religion | 358 | 0.194497 | 0.218969 | 0.712912 | 0.630284 |
| tossup_correctness | category | Science | 1431 | 0.199105 | 0.210969 | 0.691471 | 0.608689 |
| tossup_correctness | category | Social Science | 321 | 0.19829 | 0.211636 | 0.721808 | 0.613915 |
| tossup_correctness | category | Unknown | 1934 | 0.181333 | 0.202855 | 0.707143 | 0.591154 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.184266 | 0.215952 | 0.739321 | 0.628411 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.175166 | 0.200685 | 0.737329 | 0.585346 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.165622 | 0.203815 | 0.683259 | 0.596377 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.183474 | 0.194999 | 0.68812 | 0.572077 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.21121 | 0.204467 | 0.725001 | 0.595101 |
