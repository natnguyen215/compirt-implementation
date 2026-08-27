# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.712285 |
| log_loss | 0.494645 |
| ece | 0.0151722 |
| brier | 0.161128 |
| accuracy | 0.772352 |
| all_correct_accuracy | 0.763618 |
| accuracy_lift_over_all_correct | 0.00873432 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.14613 |
| probability_p10 | 0.568586 |
| probability_p50 | 0.812105 |
| probability_p90 | 0.923539 |
| mean_predictive_variance | 0.153258 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0913905 |
| joint_tossup_event_log_loss | 5.54749 |
| buzz_position_mae | 0.159171 |
| buzz_position_median_absolute_error | 0.140524 |
| buzz_position_bias | -0.0476632 |
| survival_events | 31333 |
| joint_tossup_event_log_loss_events | 31333 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.340877 |
| first_buzzer_mean_reciprocal_rank | 0.555611 |
| first_buzzer_log_loss | 1.6997 |
| first_buzzer_events | 25188 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.712285 |
| neg_average_precision | 0.439569 |
| neg_precision | 0.574224 |
| neg_recall | 0.142929 |
| full_pmf_events | 31333 |
| full_pmf_final_decile_mass | 0.141589 |
| no_buzz_observed_rate | 0.196119 |
| no_buzz_predicted_rate | 0.206603 |
| no_buzz_calibration_error | 0.0104838 |
| no_buzz_brier | 0.047622 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 25188 | -0.0476632 | -0.0663396 |
| Q1 (0-.2) | 528 | 0.387799 | 0.396341 |
| Q2 (.2-.4) | 2660 | 0.226066 | 0.224594 |
| Q3 (.4-.6) | 5812 | 0.0706487 | 0.0679071 |
| Q4 (.6-.8) | 8053 | -0.0722408 | -0.0734652 |
| Q5 (.8-1) | 8135 | -0.225628 | -0.223341 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 25188 | 0.0151722 | 0.161128 | 0.712285 | 0.494645 |
| tossup_correctness | tier | bowl | 656 | 0.0307953 | 0.15754 | 0.746038 | 0.481487 |
| tossup_correctness | tier | fall | 8504 | 0.00953064 | 0.148177 | 0.726193 | 0.462434 |
| tossup_correctness | tier | nationals | 4792 | 0.0310289 | 0.170728 | 0.723332 | 0.517773 |
| tossup_correctness | tier | open | 496 | 0.117541 | 0.214716 | 0.6157 | 0.629369 |
| tossup_correctness | tier | regionals | 4947 | 0.0163695 | 0.167072 | 0.70484 | 0.509491 |
| tossup_correctness | tier | winter | 5793 | 0.0191062 | 0.162941 | 0.692653 | 0.500073 |
| tossup_correctness | category | Current Events | 403 | 0.0686795 | 0.176951 | 0.744636 | 0.529559 |
| tossup_correctness | category | Fine Arts | 3459 | 0.0178621 | 0.158451 | 0.715968 | 0.488277 |
| tossup_correctness | category | Geography | 523 | 0.0352758 | 0.175169 | 0.708937 | 0.528615 |
| tossup_correctness | category | History | 4665 | 0.0174208 | 0.163359 | 0.705011 | 0.500048 |
| tossup_correctness | category | Literature | 4596 | 0.00797403 | 0.137215 | 0.725855 | 0.437548 |
| tossup_correctness | category | Mythology | 1024 | 0.0161075 | 0.149065 | 0.695339 | 0.467331 |
| tossup_correctness | category | Other Academic | 224 | 0.0825386 | 0.185239 | 0.692667 | 0.543378 |
| tossup_correctness | category | Philosophy | 1052 | 0.0363457 | 0.164585 | 0.67839 | 0.502279 |
| tossup_correctness | category | Popular Culture | 364 | 0.0395294 | 0.148921 | 0.676227 | 0.469154 |
| tossup_correctness | category | Religion | 1136 | 0.0232734 | 0.174729 | 0.691993 | 0.529047 |
| tossup_correctness | category | Science | 4642 | 0.022908 | 0.174558 | 0.705474 | 0.525539 |
| tossup_correctness | category | Social Science | 1040 | 0.0475124 | 0.178672 | 0.711218 | 0.538137 |
| tossup_correctness | category | Unknown | 2060 | 0.0246871 | 0.164408 | 0.70269 | 0.503369 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 528 | 0.0339579 | 0.159348 | 0.731478 | 0.489543 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 2660 | 0.02522 | 0.173273 | 0.707782 | 0.522109 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 5812 | 0.0250823 | 0.166155 | 0.718205 | 0.506006 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 8053 | 0.013346 | 0.152978 | 0.69962 | 0.475838 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 8135 | 0.014733 | 0.161749 | 0.717501 | 0.496495 |
