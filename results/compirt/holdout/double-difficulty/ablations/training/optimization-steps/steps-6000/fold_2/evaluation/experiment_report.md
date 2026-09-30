# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.712137 |
| log_loss | 0.492209 |
| ece | 0.0108435 |
| brier | 0.159937 |
| accuracy | 0.774333 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0101545 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.145929 |
| probability_p10 | 0.570384 |
| probability_p50 | 0.808235 |
| probability_p90 | 0.9194 |
| mean_predictive_variance | 0.155168 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0976811 |
| joint_tossup_event_log_loss | 6.51699 |
| buzz_position_mae | 0.144253 |
| buzz_position_median_absolute_error | 0.124853 |
| buzz_position_bias | -0.0234385 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.364265 |
| first_buzzer_mean_reciprocal_rank | 0.576904 |
| first_buzzer_log_loss | 1.63857 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.712137 |
| neg_average_precision | 0.449958 |
| neg_precision | 0.585455 |
| neg_recall | 0.147503 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.184448 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0102631 |
| no_buzz_calibration_error | -0.00284987 |
| no_buzz_brier | 0.0127642 |
| full_pmf_max_mass_error | 1.22125e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0234385 | -0.0449814 |
| Q1 (0-.2) | 183 | 0.399615 | 0.414085 |
| Q2 (.2-.4) | 955 | 0.227792 | 0.228501 |
| Q3 (.4-.6) | 2239 | 0.0768182 | 0.0733292 |
| Q4 (.6-.8) | 2875 | -0.0497948 | -0.0498613 |
| Q5 (.8-1) | 3005 | -0.178528 | -0.173786 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0108435 | 0.159937 | 0.712137 | 0.492209 |
| tossup_correctness | tier | fall | 2798 | 0.0149222 | 0.146737 | 0.735716 | 0.458598 |
| tossup_correctness | tier | nationals | 1545 | 0.0417094 | 0.177899 | 0.713684 | 0.53536 |
| tossup_correctness | tier | regionals | 2039 | 0.0194549 | 0.162652 | 0.700601 | 0.499911 |
| tossup_correctness | tier | winter | 2875 | 0.0187172 | 0.161205 | 0.695145 | 0.496268 |
| tossup_correctness | category | Current Events | 129 | 0.116987 | 0.208988 | 0.683072 | 0.61066 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0359678 | 0.152118 | 0.716057 | 0.474061 |
| tossup_correctness | category | Geography | 180 | 0.0921079 | 0.191196 | 0.756887 | 0.565035 |
| tossup_correctness | category | History | 1454 | 0.0227862 | 0.167524 | 0.689722 | 0.512374 |
| tossup_correctness | category | Literature | 1435 | 0.0159465 | 0.135459 | 0.725981 | 0.432945 |
| tossup_correctness | category | Mythology | 324 | 0.0433767 | 0.150551 | 0.702073 | 0.469611 |
| tossup_correctness | category | Other Academic | 71 | 0.114596 | 0.175815 | 0.62963 | 0.541317 |
| tossup_correctness | category | Philosophy | 310 | 0.019133 | 0.160151 | 0.723431 | 0.489635 |
| tossup_correctness | category | Popular Culture | 108 | 0.0847612 | 0.107398 | 0.524306 | 0.373568 |
| tossup_correctness | category | Religion | 361 | 0.0423371 | 0.176091 | 0.681753 | 0.531193 |
| tossup_correctness | category | Science | 1445 | 0.0333157 | 0.168363 | 0.716295 | 0.509889 |
| tossup_correctness | category | Social Science | 327 | 0.0445975 | 0.173734 | 0.746577 | 0.519566 |
| tossup_correctness | category | Unknown | 2039 | 0.0194549 | 0.162652 | 0.700601 | 0.499911 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.10883 | 0.18075 | 0.66724 | 0.538856 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0266116 | 0.173065 | 0.720049 | 0.52362 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0201833 | 0.161892 | 0.724007 | 0.496147 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0130377 | 0.15205 | 0.70519 | 0.472421 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0208771 | 0.160585 | 0.707039 | 0.495382 |
