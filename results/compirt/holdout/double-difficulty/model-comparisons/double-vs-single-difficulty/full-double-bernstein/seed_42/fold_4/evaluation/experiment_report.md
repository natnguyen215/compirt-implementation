# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.714741 |
| log_loss | 0.522345 |
| ece | 0.0984182 |
| brier | 0.171432 |
| accuracy | 0.74617 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0271845 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.228048 |
| probability_p10 | 0.349881 |
| probability_p50 | 0.734261 |
| probability_p90 | 0.950594 |
| mean_predictive_variance | 0.162829 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0971966 |
| joint_tossup_event_log_loss | 6.51992 |
| buzz_position_mae | 0.138555 |
| buzz_position_median_absolute_error | 0.11412 |
| buzz_position_bias | 0.0222672 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.389105 |
| first_buzzer_mean_reciprocal_rank | 0.597272 |
| first_buzzer_log_loss | 1.59417 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.714741 |
| neg_average_precision | 0.435123 |
| neg_precision | 0.436428 |
| neg_recall | 0.411709 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.153575 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0682136 |
| no_buzz_calibration_error | 0.0564866 |
| no_buzz_brier | 0.0231924 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | 0.0222672 | 0.00185807 |
| Q1 (0-.2) | 179 | 0.4106 | 0.424201 |
| Q2 (.2-.4) | 957 | 0.264657 | 0.264873 |
| Q3 (.4-.6) | 2203 | 0.120812 | 0.122541 |
| Q4 (.6-.8) | 2978 | -0.000381681 | 0.00357844 |
| Q5 (.8-1) | 2953 | -0.130501 | -0.122995 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0984182 | 0.171432 | 0.714741 | 0.522345 |
| tossup_correctness | tier | fall | 2876 | 0.0873034 | 0.160014 | 0.719568 | 0.492733 |
| tossup_correctness | tier | nationals | 1579 | 0.104499 | 0.193712 | 0.705396 | 0.578385 |
| tossup_correctness | tier | regionals | 1990 | 0.111275 | 0.172026 | 0.733054 | 0.522031 |
| tossup_correctness | tier | winter | 2825 | 0.0991591 | 0.170185 | 0.695271 | 0.521391 |
| tossup_correctness | category | Current Events | 123 | 0.121773 | 0.163041 | 0.776963 | 0.484287 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0928714 | 0.168179 | 0.717825 | 0.518603 |
| tossup_correctness | category | Geography | 191 | 0.122412 | 0.178807 | 0.767334 | 0.54636 |
| tossup_correctness | category | History | 1469 | 0.0789253 | 0.177282 | 0.714519 | 0.533769 |
| tossup_correctness | category | Literature | 1436 | 0.0836174 | 0.157494 | 0.689287 | 0.488019 |
| tossup_correctness | category | Mythology | 325 | 0.125263 | 0.161426 | 0.633033 | 0.506063 |
| tossup_correctness | category | Other Academic | 67 | 0.168216 | 0.20392 | 0.661725 | 0.610309 |
| tossup_correctness | category | Philosophy | 322 | 0.101546 | 0.173192 | 0.680701 | 0.518172 |
| tossup_correctness | category | Popular Culture | 100 | 0.127538 | 0.149787 | 0.550562 | 0.45954 |
| tossup_correctness | category | Religion | 365 | 0.0956529 | 0.192055 | 0.692994 | 0.571798 |
| tossup_correctness | category | Science | 1456 | 0.107324 | 0.175535 | 0.709697 | 0.536927 |
| tossup_correctness | category | Social Science | 333 | 0.12021 | 0.179222 | 0.746091 | 0.537546 |
| tossup_correctness | category | Unknown | 1990 | 0.111275 | 0.172026 | 0.733054 | 0.522031 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.259178 | 0.239583 | 0.730348 | 0.676435 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.182713 | 0.207214 | 0.718283 | 0.603129 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.121539 | 0.179637 | 0.721899 | 0.539549 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0913057 | 0.159997 | 0.718943 | 0.495209 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0618298 | 0.161117 | 0.71454 | 0.501356 |
