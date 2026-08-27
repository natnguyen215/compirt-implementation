# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.709588 |
| log_loss | 0.506994 |
| ece | 0.0636272 |
| brier | 0.165554 |
| accuracy | 0.767074 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00494886 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.166516 |
| probability_p10 | 0.463908 |
| probability_p50 | 0.725952 |
| probability_p90 | 0.898097 |
| mean_predictive_variance | 0.181581 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.106916 |
| joint_tossup_event_log_loss | 6.73337 |
| buzz_position_mae | 0.177669 |
| buzz_position_median_absolute_error | 0.160718 |
| buzz_position_bias | -0.10181 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.333223 |
| first_buzzer_mean_reciprocal_rank | 0.550355 |
| first_buzzer_log_loss | 1.70571 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.709588 |
| neg_average_precision | 0.45574 |
| neg_precision | 0.518828 |
| neg_recall | 0.286639 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0963825 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0794862 |
| no_buzz_calibration_error | 0.0635771 |
| no_buzz_brier | 0.0254892 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.10181 | -0.116074 |
| Q1 (0-.2) | 167 | 0.333407 | 0.339603 |
| Q2 (.2-.4) | 912 | 0.175086 | 0.17744 |
| Q3 (.4-.6) | 2115 | 0.0181404 | 0.0149492 |
| Q4 (.6-.8) | 2844 | -0.118404 | -0.118326 |
| Q5 (.8-1) | 3055 | -0.275857 | -0.269214 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0636272 | 0.165554 | 0.709588 | 0.506994 |
| tossup_correctness | tier | fall | 2842 | 0.0557528 | 0.15179 | 0.727585 | 0.472962 |
| tossup_correctness | tier | nationals | 1564 | 0.0639047 | 0.181873 | 0.712454 | 0.544278 |
| tossup_correctness | tier | regionals | 1937 | 0.0804483 | 0.173812 | 0.688835 | 0.527932 |
| tossup_correctness | tier | winter | 2750 | 0.0642588 | 0.164679 | 0.696573 | 0.506214 |
| tossup_correctness | category | Current Events | 126 | 0.130475 | 0.17319 | 0.723782 | 0.518652 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0677422 | 0.155469 | 0.747727 | 0.481803 |
| tossup_correctness | category | Geography | 185 | 0.120493 | 0.170212 | 0.793605 | 0.528731 |
| tossup_correctness | category | History | 1440 | 0.0542771 | 0.165699 | 0.716445 | 0.505554 |
| tossup_correctness | category | Literature | 1422 | 0.0756598 | 0.150371 | 0.672908 | 0.471422 |
| tossup_correctness | category | Mythology | 318 | 0.0736082 | 0.156431 | 0.671463 | 0.491174 |
| tossup_correctness | category | Other Academic | 66 | 0.13242 | 0.159239 | 0.824188 | 0.49081 |
| tossup_correctness | category | Philosophy | 311 | 0.0327446 | 0.168639 | 0.736087 | 0.505179 |
| tossup_correctness | category | Popular Culture | 102 | 0.11774 | 0.123999 | 0.493519 | 0.424876 |
| tossup_correctness | category | Religion | 358 | 0.0815027 | 0.187436 | 0.700438 | 0.55729 |
| tossup_correctness | category | Science | 1433 | 0.0485343 | 0.175484 | 0.694381 | 0.530678 |
| tossup_correctness | category | Social Science | 324 | 0.0705848 | 0.162137 | 0.764732 | 0.496769 |
| tossup_correctness | category | Unknown | 1937 | 0.0804483 | 0.173812 | 0.688835 | 0.527932 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.107483 | 0.188292 | 0.702031 | 0.555246 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0646807 | 0.177288 | 0.723126 | 0.531948 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0521372 | 0.16641 | 0.715077 | 0.509026 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0718599 | 0.161645 | 0.692574 | 0.498337 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0671288 | 0.163854 | 0.713645 | 0.503561 |
