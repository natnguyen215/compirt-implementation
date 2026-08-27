# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.646538 |
| log_loss | 0.854499 |
| ece | 0.223605 |
| brier | 0.261554 |
| accuracy | 0.634642 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.130608 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.314815 |
| probability_p10 | 0.088806 |
| probability_p50 | 0.615585 |
| probability_p90 | 0.960005 |
| mean_predictive_variance | 0.146382 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.122073 |
| joint_tossup_event_log_loss | 8.26786 |
| buzz_position_mae | 0.151264 |
| buzz_position_median_absolute_error | 0.121667 |
| buzz_position_bias | 0.0440534 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.324045 |
| first_buzzer_mean_reciprocal_rank | 0.531007 |
| first_buzzer_log_loss | 2.52282 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.646538 |
| neg_average_precision | 0.321827 |
| neg_precision | 0.337003 |
| neg_recall | 0.57516 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.160717 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.196093 |
| no_buzz_calibration_error | 0.182823 |
| no_buzz_brier | 0.110904 |
| full_pmf_max_mass_error | 8.27105e-12 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | 0.0440534 | 0.0284145 |
| Q1 (0-.2) | 197 | 0.43695 | 0.445873 |
| Q2 (.2-.4) | 985 | 0.286376 | 0.278429 |
| Q3 (.4-.6) | 2251 | 0.143738 | 0.138101 |
| Q4 (.6-.8) | 2866 | 0.0198527 | 0.0251013 |
| Q5 (.8-1) | 2996 | -0.113196 | -0.103616 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.223605 | 0.261554 | 0.646538 | 0.854499 |
| tossup_correctness | tier | fall | 2933 | 0.155339 | 0.200397 | 0.679973 | 0.687468 |
| tossup_correctness | tier | nationals | 1584 | 0.353055 | 0.348164 | 0.672652 | 1.08081 |
| tossup_correctness | tier | regionals | 1886 | 0.284992 | 0.314796 | 0.587908 | 1.06715 |
| tossup_correctness | tier | winter | 2892 | 0.187469 | 0.241417 | 0.639555 | 0.761263 |
| tossup_correctness | category | Current Events | 124 | 0.230553 | 0.258306 | 0.654873 | 0.906469 |
| tossup_correctness | category | Fine Arts | 1103 | 0.205282 | 0.246056 | 0.648732 | 0.788811 |
| tossup_correctness | category | Geography | 197 | 0.204617 | 0.226434 | 0.764336 | 0.765315 |
| tossup_correctness | category | History | 1491 | 0.227142 | 0.258161 | 0.655719 | 0.837868 |
| tossup_correctness | category | Literature | 1472 | 0.200629 | 0.234529 | 0.643226 | 0.751567 |
| tossup_correctness | category | Mythology | 332 | 0.22229 | 0.252296 | 0.573716 | 0.804686 |
| tossup_correctness | category | Other Academic | 69 | 0.288717 | 0.291058 | 0.644796 | 0.924893 |
| tossup_correctness | category | Philosophy | 324 | 0.236575 | 0.2513 | 0.655658 | 0.781877 |
| tossup_correctness | category | Popular Culture | 102 | 0.21015 | 0.187689 | 0.350865 | 0.633046 |
| tossup_correctness | category | Religion | 372 | 0.201997 | 0.264901 | 0.656881 | 0.841364 |
| tossup_correctness | category | Science | 1487 | 0.211803 | 0.251114 | 0.675666 | 0.813518 |
| tossup_correctness | category | Social Science | 336 | 0.197452 | 0.246706 | 0.694492 | 0.802281 |
| tossup_correctness | category | Unknown | 1886 | 0.284992 | 0.314796 | 0.587908 | 1.06715 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.412246 | 0.374259 | 0.611936 | 1.3862 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.270029 | 0.299181 | 0.643017 | 1.02617 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.251501 | 0.279273 | 0.623592 | 0.928294 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.223984 | 0.253421 | 0.646936 | 0.819479 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.179981 | 0.236239 | 0.668255 | 0.741154 |
