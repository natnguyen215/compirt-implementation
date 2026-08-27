# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.714402 |
| log_loss | 0.522372 |
| ece | 0.0853859 |
| brier | 0.170982 |
| accuracy | 0.753722 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0196332 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.230819 |
| probability_p10 | 0.342184 |
| probability_p50 | 0.761333 |
| probability_p90 | 0.939467 |
| mean_predictive_variance | 0.158058 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.098332 |
| joint_tossup_event_log_loss | 6.48549 |
| buzz_position_mae | 0.148397 |
| buzz_position_median_absolute_error | 0.130176 |
| buzz_position_bias | -0.050299 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.388026 |
| first_buzzer_mean_reciprocal_rank | 0.597181 |
| first_buzzer_log_loss | 1.58603 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.714402 |
| neg_average_precision | 0.427265 |
| neg_precision | 0.450164 |
| neg_recall | 0.391242 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.167102 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.00877221 |
| no_buzz_calibration_error | -0.00295487 |
| no_buzz_brier | 0.0104981 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.050299 | -0.0698183 |
| Q1 (0-.2) | 179 | 0.350535 | 0.347113 |
| Q2 (.2-.4) | 957 | 0.195084 | 0.186772 |
| Q3 (.4-.6) | 2203 | 0.0468287 | 0.0415346 |
| Q4 (.6-.8) | 2978 | -0.0785768 | -0.0795724 |
| Q5 (.8-1) | 2953 | -0.198061 | -0.190439 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0853859 | 0.170982 | 0.714402 | 0.522372 |
| tossup_correctness | tier | fall | 2876 | 0.0771572 | 0.158551 | 0.717394 | 0.487879 |
| tossup_correctness | tier | nationals | 1579 | 0.0841548 | 0.189862 | 0.698695 | 0.56438 |
| tossup_correctness | tier | regionals | 1990 | 0.0982952 | 0.173243 | 0.73608 | 0.534553 |
| tossup_correctness | tier | winter | 2825 | 0.0892145 | 0.171493 | 0.697927 | 0.525427 |
| tossup_correctness | category | Current Events | 123 | 0.132904 | 0.190797 | 0.692957 | 0.561635 |
| tossup_correctness | category | Fine Arts | 1093 | 0.074547 | 0.163572 | 0.717598 | 0.503052 |
| tossup_correctness | category | Geography | 191 | 0.106991 | 0.178731 | 0.739728 | 0.53721 |
| tossup_correctness | category | History | 1469 | 0.0637704 | 0.176959 | 0.716507 | 0.528885 |
| tossup_correctness | category | Literature | 1436 | 0.106393 | 0.162848 | 0.686132 | 0.507492 |
| tossup_correctness | category | Mythology | 325 | 0.111937 | 0.14227 | 0.669171 | 0.451933 |
| tossup_correctness | category | Other Academic | 67 | 0.179695 | 0.205753 | 0.61186 | 0.609096 |
| tossup_correctness | category | Philosophy | 322 | 0.0759806 | 0.163016 | 0.718795 | 0.491814 |
| tossup_correctness | category | Popular Culture | 100 | 0.0765251 | 0.115263 | 0.599591 | 0.384918 |
| tossup_correctness | category | Religion | 365 | 0.0718651 | 0.195527 | 0.677543 | 0.576557 |
| tossup_correctness | category | Science | 1456 | 0.0856723 | 0.176943 | 0.698906 | 0.538738 |
| tossup_correctness | category | Social Science | 333 | 0.0760729 | 0.171247 | 0.755784 | 0.516579 |
| tossup_correctness | category | Unknown | 1990 | 0.0982952 | 0.173243 | 0.73608 | 0.534553 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.149374 | 0.196405 | 0.697512 | 0.594855 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.0926451 | 0.179972 | 0.711304 | 0.547228 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0718799 | 0.170611 | 0.714016 | 0.51999 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0809255 | 0.162111 | 0.712858 | 0.499174 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0948516 | 0.175752 | 0.717014 | 0.535093 |
