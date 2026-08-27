# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.720876 |
| log_loss | 0.483489 |
| ece | 0.00911076 |
| brier | 0.156722 |
| accuracy | 0.780197 |
| all_correct_accuracy | 0.768775 |
| accuracy_lift_over_all_correct | 0.011422 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.147204 |
| probability_p10 | 0.571028 |
| probability_p50 | 0.813341 |
| probability_p90 | 0.924493 |
| mean_predictive_variance | 0.152304 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0891957 |
| joint_tossup_event_log_loss | 5.53521 |
| buzz_position_mae | 0.158637 |
| buzz_position_median_absolute_error | 0.142493 |
| buzz_position_bias | -0.0476798 |
| survival_events | 31247 |
| joint_tossup_event_log_loss_events | 31247 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.329407 |
| first_buzzer_mean_reciprocal_rank | 0.545582 |
| first_buzzer_log_loss | 1.7244 |
| first_buzzer_events | 25127 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.720876 |
| neg_average_precision | 0.44919 |
| neg_precision | 0.595476 |
| neg_recall | 0.154045 |
| full_pmf_events | 31247 |
| full_pmf_final_decile_mass | 0.14344 |
| no_buzz_observed_rate | 0.195859 |
| no_buzz_predicted_rate | 0.206194 |
| no_buzz_calibration_error | 0.0103356 |
| no_buzz_brier | 0.0399789 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 25127 | -0.0476798 | -0.0678468 |
| Q1 (0-.2) | 567 | 0.376134 | 0.382769 |
| Q2 (.2-.4) | 2566 | 0.225634 | 0.223767 |
| Q3 (.4-.6) | 5810 | 0.0713881 | 0.0689364 |
| Q4 (.6-.8) | 8074 | -0.0733367 | -0.073952 |
| Q5 (.8-1) | 8110 | -0.223544 | -0.221181 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 25127 | 0.00911076 | 0.156722 | 0.720876 | 0.483489 |
| tossup_correctness | tier | bowl | 715 | 0.0359464 | 0.150972 | 0.723258 | 0.469105 |
| tossup_correctness | tier | fall | 8478 | 0.017257 | 0.140201 | 0.734917 | 0.441935 |
| tossup_correctness | tier | nationals | 4789 | 0.032011 | 0.171991 | 0.717325 | 0.521344 |
| tossup_correctness | tier | open | 476 | 0.104037 | 0.207091 | 0.682403 | 0.623547 |
| tossup_correctness | tier | regionals | 4845 | 0.0198011 | 0.166687 | 0.711312 | 0.507544 |
| tossup_correctness | tier | winter | 5824 | 0.0112782 | 0.156515 | 0.716038 | 0.483158 |
| tossup_correctness | category | Current Events | 407 | 0.0323416 | 0.145582 | 0.748171 | 0.451998 |
| tossup_correctness | category | Fine Arts | 3464 | 0.0112122 | 0.155556 | 0.733802 | 0.48059 |
| tossup_correctness | category | Geography | 517 | 0.0544865 | 0.170979 | 0.710565 | 0.517385 |
| tossup_correctness | category | History | 4671 | 0.016245 | 0.157369 | 0.71501 | 0.484421 |
| tossup_correctness | category | Literature | 4592 | 0.0183087 | 0.128963 | 0.743652 | 0.414322 |
| tossup_correctness | category | Mythology | 1025 | 0.0403765 | 0.128743 | 0.689176 | 0.418349 |
| tossup_correctness | category | Other Academic | 228 | 0.08491 | 0.153156 | 0.71829 | 0.47723 |
| tossup_correctness | category | Philosophy | 1052 | 0.0348971 | 0.158257 | 0.707375 | 0.486579 |
| tossup_correctness | category | Popular Culture | 353 | 0.0203085 | 0.147449 | 0.638211 | 0.466982 |
| tossup_correctness | category | Religion | 1138 | 0.0167199 | 0.164657 | 0.716346 | 0.501192 |
| tossup_correctness | category | Science | 4649 | 0.0295699 | 0.180154 | 0.696441 | 0.541688 |
| tossup_correctness | category | Social Science | 1040 | 0.0258639 | 0.173382 | 0.711681 | 0.525426 |
| tossup_correctness | category | Unknown | 1991 | 0.0293352 | 0.167525 | 0.712975 | 0.511128 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 567 | 0.0318762 | 0.15802 | 0.745853 | 0.48406 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 2566 | 0.0122107 | 0.163506 | 0.719859 | 0.500359 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 5810 | 0.015792 | 0.160351 | 0.710811 | 0.492522 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 8074 | 0.0113438 | 0.148443 | 0.715997 | 0.463592 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 8110 | 0.0128649 | 0.160127 | 0.728601 | 0.491447 |
