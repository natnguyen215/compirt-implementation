# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.723369 |
| log_loss | 0.495823 |
| ece | 0.0752971 |
| brier | 0.161267 |
| accuracy | 0.772708 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.000647249 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.200553 |
| probability_p10 | 0.422205 |
| probability_p50 | 0.743712 |
| probability_p90 | 0.943933 |
| mean_predictive_variance | 0.166021 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0941867 |
| joint_tossup_event_log_loss | 6.43976 |
| buzz_position_mae | 0.136256 |
| buzz_position_median_absolute_error | 0.110936 |
| buzz_position_bias | 0.00863933 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.375189 |
| first_buzzer_mean_reciprocal_rank | 0.585905 |
| first_buzzer_log_loss | 1.62303 |
| first_buzzer_events | 9270 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.723369 |
| neg_average_precision | 0.454311 |
| neg_precision | 0.498 |
| neg_recall | 0.355545 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.187437 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.00910445 |
| no_buzz_calibration_error | -0.00262262 |
| no_buzz_brier | 0.0104271 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | 0.00863933 | -0.0134958 |
| Q1 (0-.2) | 179 | 0.396542 | 0.40016 |
| Q2 (.2-.4) | 957 | 0.246248 | 0.237867 |
| Q3 (.4-.6) | 2203 | 0.100945 | 0.0965451 |
| Q4 (.6-.8) | 2978 | -0.0196852 | -0.0195858 |
| Q5 (.8-1) | 2953 | -0.132175 | -0.119631 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.0752971 | 0.161267 | 0.723369 | 0.495823 |
| tossup_correctness | tier | fall | 2876 | 0.0650605 | 0.152479 | 0.719146 | 0.471682 |
| tossup_correctness | tier | nationals | 1579 | 0.0812689 | 0.182537 | 0.715577 | 0.549194 |
| tossup_correctness | tier | regionals | 1990 | 0.0808398 | 0.161194 | 0.744218 | 0.494531 |
| tossup_correctness | tier | winter | 2825 | 0.0786411 | 0.158375 | 0.710275 | 0.491477 |
| tossup_correctness | category | Current Events | 123 | 0.108114 | 0.167664 | 0.739545 | 0.496691 |
| tossup_correctness | category | Fine Arts | 1093 | 0.0639444 | 0.159781 | 0.719184 | 0.496284 |
| tossup_correctness | category | Geography | 191 | 0.0762601 | 0.165082 | 0.782486 | 0.510345 |
| tossup_correctness | category | History | 1469 | 0.0645858 | 0.170301 | 0.712117 | 0.516036 |
| tossup_correctness | category | Literature | 1436 | 0.0757591 | 0.14582 | 0.709141 | 0.459472 |
| tossup_correctness | category | Mythology | 325 | 0.108375 | 0.142115 | 0.676542 | 0.451299 |
| tossup_correctness | category | Other Academic | 67 | 0.191596 | 0.185708 | 0.673854 | 0.562955 |
| tossup_correctness | category | Philosophy | 322 | 0.0851638 | 0.166813 | 0.682076 | 0.502656 |
| tossup_correctness | category | Popular Culture | 100 | 0.103286 | 0.118051 | 0.602656 | 0.391236 |
| tossup_correctness | category | Religion | 365 | 0.075107 | 0.191378 | 0.681143 | 0.568624 |
| tossup_correctness | category | Science | 1456 | 0.0824235 | 0.163909 | 0.721349 | 0.502531 |
| tossup_correctness | category | Social Science | 333 | 0.0791432 | 0.165604 | 0.764198 | 0.506581 |
| tossup_correctness | category | Unknown | 1990 | 0.0808398 | 0.161194 | 0.744218 | 0.494531 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.189224 | 0.19739 | 0.746269 | 0.572041 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.119997 | 0.180304 | 0.722019 | 0.535574 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.077484 | 0.165921 | 0.723282 | 0.506618 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.0663009 | 0.154273 | 0.715196 | 0.480714 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.0621419 | 0.156488 | 0.732595 | 0.485503 |
