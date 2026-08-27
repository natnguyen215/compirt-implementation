# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.715073 |
| log_loss | 0.491436 |
| ece | 0.0125304 |
| brier | 0.159932 |
| accuracy | 0.774333 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.0101545 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.139528 |
| probability_p10 | 0.583954 |
| probability_p50 | 0.811001 |
| probability_p90 | 0.917105 |
| mean_predictive_variance | 0.154806 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102703 |
| joint_tossup_event_log_loss | 6.63341 |
| buzz_position_mae | 0.152461 |
| buzz_position_median_absolute_error | 0.134024 |
| buzz_position_bias | -0.0435125 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.350654 |
| first_buzzer_mean_reciprocal_rank | 0.565318 |
| first_buzzer_log_loss | 1.66911 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.715073 |
| neg_average_precision | 0.448449 |
| neg_precision | 0.597917 |
| neg_recall | 0.13147 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.190914 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0139609 |
| no_buzz_calibration_error | 0.000847844 |
| no_buzz_brier | 0.0128568 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0435125 | -0.063379 |
| Q1 (0-.2) | 183 | 0.387718 | 0.399664 |
| Q2 (.2-.4) | 955 | 0.21645 | 0.214873 |
| Q3 (.4-.6) | 2239 | 0.0635378 | 0.0589 |
| Q4 (.6-.8) | 2875 | -0.0693908 | -0.0694878 |
| Q5 (.8-1) | 3005 | -0.207394 | -0.207246 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0125304 | 0.159932 | 0.715073 | 0.491436 |
| tossup_correctness | tier | fall | 2798 | 0.0211386 | 0.146374 | 0.741338 | 0.456664 |
| tossup_correctness | tier | nationals | 1545 | 0.0464944 | 0.178467 | 0.713963 | 0.536228 |
| tossup_correctness | tier | regionals | 2039 | 0.0142396 | 0.162055 | 0.708368 | 0.496899 |
| tossup_correctness | tier | winter | 2875 | 0.0193926 | 0.16166 | 0.692259 | 0.497331 |
| tossup_correctness | category | Current Events | 129 | 0.0964187 | 0.208678 | 0.692537 | 0.606658 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0225313 | 0.152583 | 0.710961 | 0.475248 |
| tossup_correctness | category | Geography | 180 | 0.0783357 | 0.190503 | 0.754276 | 0.563922 |
| tossup_correctness | category | History | 1454 | 0.0227611 | 0.166509 | 0.695997 | 0.508625 |
| tossup_correctness | category | Literature | 1435 | 0.027451 | 0.135396 | 0.729092 | 0.432391 |
| tossup_correctness | category | Mythology | 324 | 0.0327682 | 0.152321 | 0.684535 | 0.47585 |
| tossup_correctness | category | Other Academic | 71 | 0.0987533 | 0.177605 | 0.592593 | 0.548252 |
| tossup_correctness | category | Philosophy | 310 | 0.0297229 | 0.160801 | 0.726466 | 0.490118 |
| tossup_correctness | category | Popular Culture | 108 | 0.111045 | 0.106227 | 0.499132 | 0.372308 |
| tossup_correctness | category | Religion | 361 | 0.0214046 | 0.177601 | 0.68095 | 0.533175 |
| tossup_correctness | category | Science | 1445 | 0.0290266 | 0.168365 | 0.722508 | 0.508838 |
| tossup_correctness | category | Social Science | 327 | 0.0545658 | 0.177039 | 0.735245 | 0.528592 |
| tossup_correctness | category | Unknown | 2039 | 0.0142396 | 0.162055 | 0.708368 | 0.496899 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.064625 | 0.181439 | 0.659105 | 0.539586 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0278894 | 0.173319 | 0.72304 | 0.522694 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0260164 | 0.161577 | 0.730679 | 0.494696 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.015676 | 0.151748 | 0.710054 | 0.471073 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.0186438 | 0.160972 | 0.705718 | 0.495623 |
