# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.716571 |
| log_loss | 0.503987 |
| ece | 0.0688554 |
| brier | 0.164678 |
| accuracy | 0.76958 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00540132 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.163248 |
| probability_p10 | 0.462495 |
| probability_p50 | 0.72212 |
| probability_p90 | 0.88793 |
| mean_predictive_variance | 0.184995 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.111083 |
| joint_tossup_event_log_loss | 6.73722 |
| buzz_position_mae | 0.166672 |
| buzz_position_median_absolute_error | 0.14987 |
| buzz_position_bias | -0.0763337 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.337366 |
| first_buzzer_mean_reciprocal_rank | 0.553538 |
| first_buzzer_log_loss | 1.69545 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.716571 |
| neg_average_precision | 0.454191 |
| neg_precision | 0.520358 |
| neg_recall | 0.292716 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.178157 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0112522 |
| no_buzz_calibration_error | -0.00186081 |
| no_buzz_brier | 0.0125598 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0763337 | -0.0947668 |
| Q1 (0-.2) | 183 | 0.358523 | 0.375086 |
| Q2 (.2-.4) | 955 | 0.190757 | 0.195607 |
| Q3 (.4-.6) | 2239 | 0.0353096 | 0.0305609 |
| Q4 (.6-.8) | 2875 | -0.101673 | -0.102642 |
| Q5 (.8-1) | 3005 | -0.24664 | -0.246279 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0688554 | 0.164678 | 0.716571 | 0.503987 |
| tossup_correctness | tier | fall | 2798 | 0.0670626 | 0.151164 | 0.734859 | 0.472954 |
| tossup_correctness | tier | nationals | 1545 | 0.0725559 | 0.182789 | 0.715007 | 0.545513 |
| tossup_correctness | tier | regionals | 2039 | 0.0872814 | 0.169245 | 0.70965 | 0.514148 |
| tossup_correctness | tier | winter | 2875 | 0.060283 | 0.164857 | 0.697528 | 0.504666 |
| tossup_correctness | category | Current Events | 129 | 0.0853696 | 0.195238 | 0.704164 | 0.568902 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0866583 | 0.163175 | 0.708608 | 0.500769 |
| tossup_correctness | category | Geography | 180 | 0.0581709 | 0.180185 | 0.775428 | 0.535278 |
| tossup_correctness | category | History | 1454 | 0.0610506 | 0.169055 | 0.703295 | 0.514034 |
| tossup_correctness | category | Literature | 1435 | 0.0750658 | 0.14132 | 0.727084 | 0.451704 |
| tossup_correctness | category | Mythology | 324 | 0.0586672 | 0.156121 | 0.68134 | 0.486845 |
| tossup_correctness | category | Other Academic | 71 | 0.103385 | 0.186603 | 0.62963 | 0.562554 |
| tossup_correctness | category | Philosophy | 310 | 0.0681785 | 0.163111 | 0.736372 | 0.496446 |
| tossup_correctness | category | Popular Culture | 108 | 0.172598 | 0.123772 | 0.506076 | 0.423894 |
| tossup_correctness | category | Religion | 361 | 0.097621 | 0.181496 | 0.712045 | 0.54208 |
| tossup_correctness | category | Science | 1445 | 0.0526602 | 0.169418 | 0.722877 | 0.513556 |
| tossup_correctness | category | Social Science | 327 | 0.0814345 | 0.182783 | 0.715264 | 0.546652 |
| tossup_correctness | category | Unknown | 2039 | 0.0872814 | 0.169245 | 0.70965 | 0.514148 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.114924 | 0.187809 | 0.68664 | 0.55659 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0605833 | 0.176168 | 0.718668 | 0.531467 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0577605 | 0.165478 | 0.726157 | 0.503368 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.071607 | 0.158152 | 0.705041 | 0.488792 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0789457 | 0.165264 | 0.71831 | 0.507049 |
