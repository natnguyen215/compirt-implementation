# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.596692 |
| log_loss | 0.737962 |
| ece | 0.290837 |
| brier | 0.266584 |
| accuracy | 0.548759 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.224595 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.162858 |
| probability_p10 | 0.243696 |
| probability_p50 | 0.502624 |
| probability_p90 | 0.683413 |
| mean_predictive_variance | 0.223172 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0950349 |
| joint_tossup_event_log_loss | 6.86197 |
| buzz_position_mae | 0.138928 |
| buzz_position_median_absolute_error | 0.116082 |
| buzz_position_bias | -0.000730965 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.364078 |
| first_buzzer_mean_reciprocal_rank | 0.573353 |
| first_buzzer_log_loss | 1.65445 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.596692 |
| neg_average_precision | 0.302474 |
| neg_precision | 0.272807 |
| neg_recall | 0.594955 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.136672 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0497325 |
| no_buzz_calibration_error | 0.0380055 |
| no_buzz_brier | 0.0180489 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.000730965 | -0.0228434 |
| Q1 (0-.2) | 179 | 0.395281 | 0.398878 |
| Q2 (.2-.4) | 957 | 0.241022 | 0.235724 |
| Q3 (.4-.6) | 2203 | 0.0966123 | 0.0955861 |
| Q4 (.6-.8) | 2978 | -0.0257728 | -0.0236128 |
| Q5 (.8-1) | 2953 | -0.150449 | -0.139686 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.290837 | 0.266584 | 0.596692 | 0.737962 |
| tossup_correctness | tier | fall | 2876 | 0.330159 | 0.278377 | 0.611907 | 0.766134 |
| tossup_correctness | tier | nationals | 1579 | 0.204312 | 0.23899 | 0.599611 | 0.671959 |
| tossup_correctness | tier | regionals | 1990 | 0.270914 | 0.256627 | 0.611198 | 0.716354 |
| tossup_correctness | tier | winter | 2825 | 0.313203 | 0.277015 | 0.590431 | 0.761396 |
| tossup_correctness | category | Current Events | 123 | 0.310065 | 0.267274 | 0.66361 | 0.737751 |
| tossup_correctness | category | Fine Arts | 1093 | 0.287253 | 0.267131 | 0.59822 | 0.739956 |
| tossup_correctness | category | Geography | 191 | 0.255989 | 0.298863 | 0.515408 | 0.812265 |
| tossup_correctness | category | History | 1469 | 0.280228 | 0.263587 | 0.611007 | 0.730116 |
| tossup_correctness | category | Literature | 1436 | 0.30659 | 0.253998 | 0.59495 | 0.711371 |
| tossup_correctness | category | Mythology | 325 | 0.371423 | 0.300735 | 0.445327 | 0.811089 |
| tossup_correctness | category | Other Academic | 67 | 0.325529 | 0.281724 | 0.587601 | 0.769163 |
| tossup_correctness | category | Philosophy | 322 | 0.27815 | 0.234435 | 0.686888 | 0.665222 |
| tossup_correctness | category | Popular Culture | 100 | 0.472465 | 0.33498 | 0.547497 | 0.897748 |
| tossup_correctness | category | Religion | 365 | 0.24977 | 0.263036 | 0.615924 | 0.730122 |
| tossup_correctness | category | Science | 1456 | 0.309121 | 0.287222 | 0.556257 | 0.783609 |
| tossup_correctness | category | Social Science | 333 | 0.254725 | 0.260835 | 0.609488 | 0.721006 |
| tossup_correctness | category | Unknown | 1990 | 0.270914 | 0.256627 | 0.611198 | 0.716354 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.371558 | 0.323971 | 0.612106 | 0.865443 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.335634 | 0.30206 | 0.593646 | 0.818671 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.32089 | 0.28285 | 0.623027 | 0.777175 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.301845 | 0.265087 | 0.594534 | 0.734055 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.237906 | 0.240983 | 0.586609 | 0.678766 |
