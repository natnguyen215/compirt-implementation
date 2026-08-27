# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.71054 |
| log_loss | 0.486601 |
| ece | 0.0133902 |
| brier | 0.157025 |
| accuracy | 0.781167 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0111233 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.144454 |
| probability_p10 | 0.577565 |
| probability_p50 | 0.817032 |
| probability_p90 | 0.924654 |
| mean_predictive_variance | 0.151096 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.1001 |
| joint_tossup_event_log_loss | 6.52985 |
| buzz_position_mae | 0.15055 |
| buzz_position_median_absolute_error | 0.133204 |
| buzz_position_bias | -0.049908 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.380837 |
| first_buzzer_mean_reciprocal_rank | 0.587207 |
| first_buzzer_log_loss | 1.63214 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.71054 |
| neg_average_precision | 0.44744 |
| neg_precision | 0.6 |
| neg_recall | 0.145115 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.180798 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.014322 |
| no_buzz_calibration_error | -0.000862424 |
| no_buzz_brier | 0.0133439 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.049908 | -0.0717627 |
| Q1 (0-.2) | 192 | 0.379441 | 0.38131 |
| Q2 (.2-.4) | 889 | 0.206533 | 0.210672 |
| Q3 (.4-.6) | 2210 | 0.0517844 | 0.0480431 |
| Q4 (.6-.8) | 2869 | -0.0797684 | -0.0788574 |
| Q5 (.8-1) | 2920 | -0.20384 | -0.199458 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0133902 | 0.157025 | 0.71054 | 0.486601 |
| tossup_correctness | tier | fall | 2817 | 0.0219641 | 0.15256 | 0.704172 | 0.476939 |
| tossup_correctness | tier | nationals | 1542 | 0.0304481 | 0.170367 | 0.72901 | 0.514858 |
| tossup_correctness | tier | regionals | 1934 | 0.0233463 | 0.163726 | 0.711427 | 0.501557 |
| tossup_correctness | tier | winter | 2787 | 0.0181315 | 0.149507 | 0.700007 | 0.470354 |
| tossup_correctness | category | Current Events | 125 | 0.0716732 | 0.179001 | 0.754607 | 0.528886 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0315582 | 0.15213 | 0.725447 | 0.474651 |
| tossup_correctness | category | Geography | 185 | 0.0631664 | 0.162044 | 0.780559 | 0.494847 |
| tossup_correctness | category | History | 1443 | 0.0254187 | 0.15762 | 0.731414 | 0.484279 |
| tossup_correctness | category | Literature | 1411 | 0.02635 | 0.142077 | 0.674563 | 0.453153 |
| tossup_correctness | category | Mythology | 320 | 0.0411155 | 0.152241 | 0.661954 | 0.482838 |
| tossup_correctness | category | Other Academic | 64 | 0.0964512 | 0.18016 | 0.688802 | 0.536067 |
| tossup_correctness | category | Philosophy | 312 | 0.0244473 | 0.148421 | 0.669935 | 0.466794 |
| tossup_correctness | category | Popular Culture | 104 | 0.0366774 | 0.125052 | 0.633523 | 0.418058 |
| tossup_correctness | category | Religion | 358 | 0.0341098 | 0.178483 | 0.716091 | 0.533518 |
| tossup_correctness | category | Science | 1431 | 0.0283771 | 0.161501 | 0.686016 | 0.500416 |
| tossup_correctness | category | Social Science | 321 | 0.047991 | 0.159581 | 0.739259 | 0.494081 |
| tossup_correctness | category | Unknown | 1934 | 0.0233463 | 0.163726 | 0.711427 | 0.501557 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0539229 | 0.188703 | 0.71912 | 0.555161 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.02883 | 0.166226 | 0.740422 | 0.505202 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0288086 | 0.166192 | 0.692157 | 0.510895 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0173171 | 0.150361 | 0.693383 | 0.471772 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0159289 | 0.151751 | 0.727005 | 0.472612 |
