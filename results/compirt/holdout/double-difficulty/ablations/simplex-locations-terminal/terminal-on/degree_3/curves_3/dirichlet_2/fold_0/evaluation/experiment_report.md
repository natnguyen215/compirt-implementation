# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.711118 |
| log_loss | 0.504833 |
| ece | 0.0683354 |
| brier | 0.165118 |
| accuracy | 0.770629 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00537924 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.163428 |
| probability_p10 | 0.466919 |
| probability_p50 | 0.723877 |
| probability_p90 | 0.890267 |
| mean_predictive_variance | 0.184308 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.110131 |
| joint_tossup_event_log_loss | 6.72412 |
| buzz_position_mae | 0.166572 |
| buzz_position_median_absolute_error | 0.14879 |
| buzz_position_bias | -0.0746779 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.335772 |
| first_buzzer_mean_reciprocal_rank | 0.554564 |
| first_buzzer_log_loss | 1.69245 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.711118 |
| neg_average_precision | 0.446318 |
| neg_precision | 0.520973 |
| neg_recall | 0.284601 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.175714 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0130871 |
| no_buzz_calibration_error | -0.000182562 |
| no_buzz_brier | 0.0125715 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0746779 | -0.0940039 |
| Q1 (0-.2) | 197 | 0.347026 | 0.337401 |
| Q2 (.2-.4) | 985 | 0.187591 | 0.180231 |
| Q3 (.4-.6) | 2251 | 0.0370831 | 0.0321112 |
| Q4 (.6-.8) | 2866 | -0.103951 | -0.104157 |
| Q5 (.8-1) | 2996 | -0.244601 | -0.245693 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0683354 | 0.165118 | 0.711118 | 0.504833 |
| tossup_correctness | tier | fall | 2933 | 0.0728006 | 0.154791 | 0.707969 | 0.480449 |
| tossup_correctness | tier | nationals | 1584 | 0.0724617 | 0.183642 | 0.698654 | 0.54849 |
| tossup_correctness | tier | regionals | 1886 | 0.0759884 | 0.176107 | 0.70557 | 0.530219 |
| tossup_correctness | tier | winter | 2892 | 0.058829 | 0.158278 | 0.716061 | 0.489097 |
| tossup_correctness | category | Current Events | 124 | 0.0904884 | 0.17574 | 0.692334 | 0.529932 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0543674 | 0.165584 | 0.70023 | 0.508163 |
| tossup_correctness | category | Geography | 197 | 0.11461 | 0.181139 | 0.762587 | 0.545948 |
| tossup_correctness | category | History | 1491 | 0.0859121 | 0.156733 | 0.722177 | 0.482781 |
| tossup_correctness | category | Literature | 1472 | 0.0654036 | 0.14299 | 0.724495 | 0.453864 |
| tossup_correctness | category | Mythology | 332 | 0.101378 | 0.150883 | 0.681004 | 0.475346 |
| tossup_correctness | category | Other Academic | 69 | 0.088179 | 0.179351 | 0.69457 | 0.535184 |
| tossup_correctness | category | Philosophy | 324 | 0.0897272 | 0.157931 | 0.678052 | 0.487226 |
| tossup_correctness | category | Popular Culture | 102 | 0.165357 | 0.154676 | 0.473356 | 0.501274 |
| tossup_correctness | category | Religion | 372 | 0.0683239 | 0.189389 | 0.703458 | 0.558436 |
| tossup_correctness | category | Science | 1487 | 0.0633338 | 0.174966 | 0.686507 | 0.526672 |
| tossup_correctness | category | Social Science | 336 | 0.0660696 | 0.173526 | 0.756059 | 0.524158 |
| tossup_correctness | category | Unknown | 1886 | 0.0759884 | 0.176107 | 0.70557 | 0.530219 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.127836 | 0.177618 | 0.712467 | 0.538965 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0575105 | 0.177255 | 0.711368 | 0.53115 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0712905 | 0.168946 | 0.686468 | 0.514921 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0764812 | 0.15852 | 0.705841 | 0.49005 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0667981 | 0.16374 | 0.732293 | 0.5005 |
