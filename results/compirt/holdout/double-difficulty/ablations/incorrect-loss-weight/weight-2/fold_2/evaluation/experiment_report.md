# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.711698 |
| log_loss | 0.528724 |
| ece | 0.112461 |
| brier | 0.175539 |
| accuracy | 0.746894 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0172842 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.190221 |
| probability_p10 | 0.373701 |
| probability_p50 | 0.684575 |
| probability_p90 | 0.876791 |
| mean_predictive_variance | 0.190798 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.102507 |
| joint_tossup_event_log_loss | 6.65697 |
| buzz_position_mae | 0.15226 |
| buzz_position_median_absolute_error | 0.13432 |
| buzz_position_bias | -0.0431706 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.356163 |
| first_buzzer_mean_reciprocal_rank | 0.569805 |
| first_buzzer_log_loss | 1.66183 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.711698 |
| neg_average_precision | 0.448483 |
| neg_precision | 0.460278 |
| neg_recall | 0.424645 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.190025 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0136924 |
| no_buzz_calibration_error | 0.000579347 |
| no_buzz_brier | 0.0128455 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0431706 | -0.0637841 |
| Q1 (0-.2) | 183 | 0.386766 | 0.401449 |
| Q2 (.2-.4) | 955 | 0.217021 | 0.215424 |
| Q3 (.4-.6) | 2239 | 0.0625296 | 0.0586545 |
| Q4 (.6-.8) | 2875 | -0.0687557 | -0.0691767 |
| Q5 (.8-1) | 3005 | -0.206321 | -0.205647 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.112461 | 0.175539 | 0.711698 | 0.528724 |
| tossup_correctness | tier | fall | 2798 | 0.12093 | 0.162987 | 0.738972 | 0.498895 |
| tossup_correctness | tier | nationals | 1545 | 0.0943851 | 0.187852 | 0.711929 | 0.5573 |
| tossup_correctness | tier | regionals | 2039 | 0.115906 | 0.178866 | 0.704109 | 0.535684 |
| tossup_correctness | tier | winter | 2875 | 0.111488 | 0.178777 | 0.686612 | 0.537463 |
| tossup_correctness | category | Current Events | 129 | 0.0889071 | 0.202742 | 0.698756 | 0.58585 |
| tossup_correctness | category | Fine Arts | 1074 | 0.135615 | 0.176256 | 0.706585 | 0.530492 |
| tossup_correctness | category | Geography | 180 | 0.0922674 | 0.190159 | 0.751926 | 0.558928 |
| tossup_correctness | category | History | 1454 | 0.105011 | 0.180501 | 0.697665 | 0.539661 |
| tossup_correctness | category | Literature | 1435 | 0.113518 | 0.149717 | 0.725678 | 0.471048 |
| tossup_correctness | category | Mythology | 324 | 0.0962979 | 0.165101 | 0.673152 | 0.508249 |
| tossup_correctness | category | Other Academic | 71 | 0.167933 | 0.197373 | 0.602397 | 0.588902 |
| tossup_correctness | category | Philosophy | 310 | 0.110868 | 0.172333 | 0.726638 | 0.51919 |
| tossup_correctness | category | Popular Culture | 108 | 0.148997 | 0.135407 | 0.460937 | 0.445053 |
| tossup_correctness | category | Religion | 361 | 0.147457 | 0.203886 | 0.669917 | 0.592669 |
| tossup_correctness | category | Science | 1445 | 0.106215 | 0.181389 | 0.716283 | 0.541187 |
| tossup_correctness | category | Social Science | 327 | 0.11353 | 0.189659 | 0.735014 | 0.563068 |
| tossup_correctness | category | Unknown | 2039 | 0.115906 | 0.178866 | 0.704109 | 0.535684 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.132046 | 0.202855 | 0.659887 | 0.588584 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0960306 | 0.182784 | 0.72223 | 0.546025 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.0980676 | 0.172629 | 0.726664 | 0.522059 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.111185 | 0.167189 | 0.705955 | 0.508592 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.128702 | 0.181729 | 0.703807 | 0.543808 |
