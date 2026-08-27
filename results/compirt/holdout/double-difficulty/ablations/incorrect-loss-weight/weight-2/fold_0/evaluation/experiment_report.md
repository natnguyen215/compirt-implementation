# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.714452 |
| log_loss | 0.525175 |
| ece | 0.109364 |
| brier | 0.174086 |
| accuracy | 0.748467 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0167832 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.189819 |
| probability_p10 | 0.374867 |
| probability_p50 | 0.69226 |
| probability_p90 | 0.875273 |
| mean_predictive_variance | 0.189668 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102004 |
| joint_tossup_event_log_loss | 6.65158 |
| buzz_position_mae | 0.15233 |
| buzz_position_median_absolute_error | 0.135818 |
| buzz_position_bias | -0.0426218 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.355245 |
| first_buzzer_mean_reciprocal_rank | 0.568737 |
| first_buzzer_log_loss | 1.66509 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.714452 |
| neg_average_precision | 0.444057 |
| neg_precision | 0.459877 |
| neg_recall | 0.409716 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.187897 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0159069 |
| no_buzz_calibration_error | 0.00263731 |
| no_buzz_brier | 0.0130831 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0426218 | -0.0640818 |
| Q1 (0-.2) | 197 | 0.370302 | 0.365122 |
| Q2 (.2-.4) | 985 | 0.214026 | 0.209236 |
| Q3 (.4-.6) | 2251 | 0.0630304 | 0.0597749 |
| Q4 (.6-.8) | 2866 | -0.0724232 | -0.072962 |
| Q5 (.8-1) | 2996 | -0.205024 | -0.202152 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.109364 | 0.174086 | 0.714452 | 0.525175 |
| tossup_correctness | tier | fall | 2933 | 0.12141 | 0.166533 | 0.712139 | 0.506808 |
| tossup_correctness | tier | nationals | 1584 | 0.0921213 | 0.185798 | 0.708861 | 0.553188 |
| tossup_correctness | tier | regionals | 1886 | 0.106789 | 0.183974 | 0.707555 | 0.547487 |
| tossup_correctness | tier | winter | 2892 | 0.109436 | 0.168884 | 0.719166 | 0.513908 |
| tossup_correctness | category | Current Events | 124 | 0.164272 | 0.195156 | 0.685397 | 0.57516 |
| tossup_correctness | category | Fine Arts | 1103 | 0.101892 | 0.173515 | 0.711298 | 0.524808 |
| tossup_correctness | category | Geography | 197 | 0.120645 | 0.182489 | 0.786713 | 0.551312 |
| tossup_correctness | category | History | 1491 | 0.126682 | 0.168535 | 0.721086 | 0.510967 |
| tossup_correctness | category | Literature | 1472 | 0.0966511 | 0.147991 | 0.726876 | 0.466047 |
| tossup_correctness | category | Mythology | 332 | 0.125772 | 0.157919 | 0.689964 | 0.489971 |
| tossup_correctness | category | Other Academic | 69 | 0.124995 | 0.184493 | 0.684389 | 0.550823 |
| tossup_correctness | category | Philosophy | 324 | 0.134906 | 0.170553 | 0.690882 | 0.515698 |
| tossup_correctness | category | Popular Culture | 102 | 0.139102 | 0.165036 | 0.456055 | 0.518386 |
| tossup_correctness | category | Religion | 372 | 0.103476 | 0.193311 | 0.715593 | 0.566454 |
| tossup_correctness | category | Science | 1487 | 0.113897 | 0.186821 | 0.690582 | 0.553136 |
| tossup_correctness | category | Social Science | 336 | 0.0934458 | 0.189057 | 0.726017 | 0.560722 |
| tossup_correctness | category | Unknown | 1886 | 0.106789 | 0.183974 | 0.707555 | 0.547487 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.169906 | 0.1916 | 0.690186 | 0.578052 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0946757 | 0.183264 | 0.713157 | 0.544848 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.105798 | 0.175188 | 0.700646 | 0.528863 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.109449 | 0.168194 | 0.702582 | 0.511569 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.116062 | 0.174725 | 0.735403 | 0.525474 |
