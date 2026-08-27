# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.601715 |
| log_loss | 0.784413 |
| ece | 0.338711 |
| brier | 0.293014 |
| accuracy | 0.384142 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.377983 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.09832 |
| probability_p10 | 0.296978 |
| probability_p50 | 0.422684 |
| probability_p90 | 0.548682 |
| mean_predictive_variance | 0.23447 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0926069 |
| joint_tossup_event_log_loss | 6.73927 |
| buzz_position_mae | 0.136742 |
| buzz_position_median_absolute_error | 0.115431 |
| buzz_position_bias | -0.00951106 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.39173 |
| first_buzzer_mean_reciprocal_rank | 0.597909 |
| first_buzzer_log_loss | 1.60232 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.601715 |
| neg_average_precision | 0.315142 |
| neg_precision | 0.259415 |
| neg_recall | 0.856681 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.128574 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.052657 |
| no_buzz_calibration_error | 0.0367479 |
| no_buzz_brier | 0.0221619 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.00951106 | -0.0328838 |
| Q1 (0-.2) | 167 | 0.3793 | 0.399692 |
| Q2 (.2-.4) | 912 | 0.228289 | 0.22539 |
| Q3 (.4-.6) | 2115 | 0.0872403 | 0.0865722 |
| Q4 (.6-.8) | 2844 | -0.028488 | -0.027482 |
| Q5 (.8-1) | 3055 | -0.151071 | -0.142858 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.338711 | 0.293014 | 0.601715 | 0.784413 |
| tossup_correctness | tier | fall | 2842 | 0.361529 | 0.294376 | 0.621834 | 0.786397 |
| tossup_correctness | tier | nationals | 1564 | 0.287608 | 0.285214 | 0.571176 | 0.76904 |
| tossup_correctness | tier | regionals | 1937 | 0.325175 | 0.285695 | 0.607735 | 0.769401 |
| tossup_correctness | tier | winter | 2750 | 0.353901 | 0.301199 | 0.604809 | 0.801681 |
| tossup_correctness | category | Current Events | 126 | 0.370566 | 0.311091 | 0.596872 | 0.823926 |
| tossup_correctness | category | Fine Arts | 1071 | 0.355501 | 0.300165 | 0.616234 | 0.799196 |
| tossup_correctness | category | Geography | 185 | 0.309534 | 0.302165 | 0.563953 | 0.804512 |
| tossup_correctness | category | History | 1440 | 0.32686 | 0.288118 | 0.608089 | 0.773332 |
| tossup_correctness | category | Literature | 1422 | 0.378888 | 0.298126 | 0.565316 | 0.796614 |
| tossup_correctness | category | Mythology | 318 | 0.384004 | 0.314007 | 0.562883 | 0.827442 |
| tossup_correctness | category | Other Academic | 66 | 0.325287 | 0.283181 | 0.723404 | 0.761184 |
| tossup_correctness | category | Philosophy | 311 | 0.330401 | 0.286759 | 0.659374 | 0.771797 |
| tossup_correctness | category | Popular Culture | 102 | 0.501296 | 0.370116 | 0.386111 | 0.948906 |
| tossup_correctness | category | Religion | 358 | 0.293467 | 0.283438 | 0.614544 | 0.76412 |
| tossup_correctness | category | Science | 1433 | 0.317897 | 0.289499 | 0.605497 | 0.776353 |
| tossup_correctness | category | Social Science | 324 | 0.314278 | 0.289467 | 0.606528 | 0.775061 |
| tossup_correctness | category | Unknown | 1937 | 0.325175 | 0.285695 | 0.607735 | 0.769401 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.407059 | 0.361176 | 0.594188 | 0.936589 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.382435 | 0.340376 | 0.5946 | 0.889628 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.36687 | 0.313732 | 0.628016 | 0.828285 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.354528 | 0.293894 | 0.608043 | 0.785054 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.28826 | 0.259988 | 0.604741 | 0.713716 |
