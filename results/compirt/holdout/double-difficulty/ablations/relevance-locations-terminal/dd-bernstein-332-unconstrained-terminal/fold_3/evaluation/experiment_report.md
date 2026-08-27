# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.717387 |
| log_loss | 0.501655 |
| ece | 0.0727024 |
| brier | 0.161978 |
| accuracy | 0.767952 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.00209251 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.199597 |
| probability_p10 | 0.429178 |
| probability_p50 | 0.754429 |
| probability_p90 | 0.946708 |
| mean_predictive_variance | 0.163374 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0933879 |
| joint_tossup_event_log_loss | 6.40115 |
| buzz_position_mae | 0.135681 |
| buzz_position_median_absolute_error | 0.110142 |
| buzz_position_bias | 0.00163841 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.382489 |
| first_buzzer_mean_reciprocal_rank | 0.58858 |
| first_buzzer_log_loss | 1.60768 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.717387 |
| neg_average_precision | 0.461728 |
| neg_precision | 0.493426 |
| neg_recall | 0.341475 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.184789 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.00841332 |
| no_buzz_calibration_error | -0.00677107 |
| no_buzz_brier | 0.0129876 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | 0.00163841 | -0.0208595 |
| Q1 (0-.2) | 192 | 0.412259 | 0.422662 |
| Q2 (.2-.4) | 889 | 0.234005 | 0.235135 |
| Q3 (.4-.6) | 2210 | 0.0887174 | 0.0820209 |
| Q4 (.6-.8) | 2869 | -0.0278293 | -0.0277617 |
| Q5 (.8-1) | 2920 | -0.133058 | -0.123335 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0727024 | 0.161978 | 0.717387 | 0.501655 |
| tossup_correctness | tier | fall | 2817 | 0.0662703 | 0.156402 | 0.709516 | 0.49423 |
| tossup_correctness | tier | nationals | 1542 | 0.0753067 | 0.179789 | 0.71945 | 0.538459 |
| tossup_correctness | tier | regionals | 1934 | 0.0775064 | 0.169084 | 0.711964 | 0.516213 |
| tossup_correctness | tier | winter | 2787 | 0.075851 | 0.152829 | 0.718144 | 0.478696 |
| tossup_correctness | category | Current Events | 125 | 0.110441 | 0.18289 | 0.711302 | 0.539745 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0693394 | 0.159555 | 0.723607 | 0.496982 |
| tossup_correctness | category | Geography | 185 | 0.0989653 | 0.16948 | 0.775804 | 0.50897 |
| tossup_correctness | category | History | 1443 | 0.0690632 | 0.161168 | 0.736461 | 0.495083 |
| tossup_correctness | category | Literature | 1411 | 0.0707045 | 0.150484 | 0.674573 | 0.478603 |
| tossup_correctness | category | Mythology | 320 | 0.0812725 | 0.162621 | 0.65408 | 0.531616 |
| tossup_correctness | category | Other Academic | 64 | 0.137261 | 0.185003 | 0.644531 | 0.567765 |
| tossup_correctness | category | Philosophy | 312 | 0.0882745 | 0.154162 | 0.697355 | 0.474538 |
| tossup_correctness | category | Popular Culture | 104 | 0.0563734 | 0.135241 | 0.598722 | 0.447918 |
| tossup_correctness | category | Religion | 358 | 0.0682337 | 0.170739 | 0.748783 | 0.514131 |
| tossup_correctness | category | Science | 1431 | 0.0722492 | 0.163746 | 0.720053 | 0.506751 |
| tossup_correctness | category | Social Science | 321 | 0.0988213 | 0.162342 | 0.753087 | 0.505467 |
| tossup_correctness | category | Unknown | 1934 | 0.0775064 | 0.169084 | 0.711964 | 0.516213 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.137661 | 0.199165 | 0.733016 | 0.583598 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0705318 | 0.167462 | 0.759054 | 0.504371 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0787942 | 0.171477 | 0.697876 | 0.530643 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0679227 | 0.156068 | 0.698274 | 0.488295 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0719628 | 0.156482 | 0.730962 | 0.486629 |
