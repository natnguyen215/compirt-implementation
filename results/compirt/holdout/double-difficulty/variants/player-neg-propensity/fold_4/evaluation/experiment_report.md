# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.725361 |
| log_loss | 0.475326 |
| ece | 0.00785134 |
| brier | 0.153464 |
| accuracy | 0.788134 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.0147789 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.14347 |
| probability_p10 | 0.573311 |
| probability_p50 | 0.814524 |
| probability_p90 | 0.92135 |
| mean_predictive_variance | 0.152788 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100276 |
| joint_tossup_event_log_loss | 6.55952 |
| buzz_position_mae | 0.149853 |
| buzz_position_median_absolute_error | 0.132632 |
| buzz_position_bias | -0.0430568 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.365912 |
| first_buzzer_mean_reciprocal_rank | 0.575961 |
| first_buzzer_log_loss | 1.65173 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.725361 |
| neg_average_precision | 0.453999 |
| neg_precision | 0.631985 |
| neg_recall | 0.156116 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.18397 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0133675 |
| no_buzz_calibration_error | 0.00164044 |
| no_buzz_brier | 0.010975 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.0430568 | -0.064362 |
| Q1 (0-.2) | 179 | 0.372804 | 0.375898 |
| Q2 (.2-.4) | 957 | 0.216276 | 0.210209 |
| Q3 (.4-.6) | 2203 | 0.0635964 | 0.0614196 |
| Q4 (.6-.8) | 2978 | -0.0712374 | -0.0725596 |
| Q5 (.8-1) | 2953 | -0.203455 | -0.200793 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.00785134 | 0.153464 | 0.725361 | 0.475326 |
| tossup_correctness | tier | fall | 2876 | 0.0107658 | 0.144148 | 0.726162 | 0.45224 |
| tossup_correctness | tier | nationals | 1579 | 0.0361552 | 0.173888 | 0.717213 | 0.525598 |
| tossup_correctness | tier | regionals | 1990 | 0.0230068 | 0.154848 | 0.740379 | 0.477427 |
| tossup_correctness | tier | winter | 2825 | 0.0101481 | 0.150557 | 0.716159 | 0.469249 |
| tossup_correctness | category | Current Events | 123 | 0.0858421 | 0.149306 | 0.775495 | 0.46213 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0229456 | 0.150119 | 0.736529 | 0.468938 |
| tossup_correctness | category | Geography | 191 | 0.0664703 | 0.157495 | 0.796867 | 0.486792 |
| tossup_correctness | category | History | 1469 | 0.0326786 | 0.166156 | 0.713993 | 0.503582 |
| tossup_correctness | category | Literature | 1436 | 0.0140159 | 0.134859 | 0.721045 | 0.429967 |
| tossup_correctness | category | Mythology | 325 | 0.0378161 | 0.128989 | 0.663733 | 0.418943 |
| tossup_correctness | category | Other Academic | 67 | 0.0909482 | 0.156324 | 0.679245 | 0.487183 |
| tossup_correctness | category | Philosophy | 322 | 0.0325422 | 0.160796 | 0.672681 | 0.493192 |
| tossup_correctness | category | Popular Culture | 100 | 0.0538906 | 0.105612 | 0.538304 | 0.367313 |
| tossup_correctness | category | Religion | 365 | 0.0474591 | 0.187629 | 0.657853 | 0.561861 |
| tossup_correctness | category | Science | 1456 | 0.0112624 | 0.1563 | 0.72129 | 0.482706 |
| tossup_correctness | category | Social Science | 333 | 0.0430608 | 0.160378 | 0.749977 | 0.493673 |
| tossup_correctness | category | Unknown | 1990 | 0.0230068 | 0.154848 | 0.740379 | 0.477427 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.048895 | 0.161228 | 0.739303 | 0.491825 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.00957524 | 0.164758 | 0.704603 | 0.50305 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.0254437 | 0.157382 | 0.72404 | 0.484227 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0097449 | 0.148129 | 0.715876 | 0.463549 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.00966988 | 0.15179 | 0.738782 | 0.470576 |
