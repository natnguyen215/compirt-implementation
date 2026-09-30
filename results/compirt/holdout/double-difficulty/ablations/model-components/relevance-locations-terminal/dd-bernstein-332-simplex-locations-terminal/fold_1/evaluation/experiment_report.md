# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.709354 |
| log_loss | 0.497356 |
| ece | 0.0158633 |
| brier | 0.161796 |
| accuracy | 0.773342 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0112174 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.143637 |
| probability_p10 | 0.574783 |
| probability_p50 | 0.812538 |
| probability_p90 | 0.920443 |
| mean_predictive_variance | 0.153529 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100668 |
| joint_tossup_event_log_loss | 6.60058 |
| buzz_position_mae | 0.151074 |
| buzz_position_median_absolute_error | 0.133607 |
| buzz_position_bias | -0.0475397 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.351479 |
| first_buzzer_mean_reciprocal_rank | 0.564805 |
| first_buzzer_log_loss | 1.67763 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.709354 |
| neg_average_precision | 0.445715 |
| neg_precision | 0.595149 |
| neg_recall | 0.14748 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.190544 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0149294 |
| no_buzz_calibration_error | -0.000979641 |
| no_buzz_brier | 0.0154922 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0475397 | -0.0685082 |
| Q1 (0-.2) | 167 | 0.372885 | 0.377776 |
| Q2 (.2-.4) | 912 | 0.212708 | 0.214937 |
| Q3 (.4-.6) | 2115 | 0.062951 | 0.059694 |
| Q4 (.6-.8) | 2844 | -0.0688863 | -0.0701171 |
| Q5 (.8-1) | 3055 | -0.204834 | -0.201868 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0158633 | 0.161796 | 0.709354 | 0.497356 |
| tossup_correctness | tier | fall | 2842 | 0.0133547 | 0.149024 | 0.729304 | 0.463707 |
| tossup_correctness | tier | nationals | 1564 | 0.0461838 | 0.179767 | 0.713781 | 0.540469 |
| tossup_correctness | tier | regionals | 1937 | 0.0227995 | 0.167633 | 0.686238 | 0.513301 |
| tossup_correctness | tier | winter | 2750 | 0.0187113 | 0.160662 | 0.699462 | 0.49638 |
| tossup_correctness | category | Current Events | 126 | 0.0680989 | 0.160134 | 0.719517 | 0.491915 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0241176 | 0.151362 | 0.750857 | 0.468332 |
| tossup_correctness | category | Geography | 185 | 0.0755367 | 0.16233 | 0.796373 | 0.495358 |
| tossup_correctness | category | History | 1440 | 0.0293542 | 0.167925 | 0.707533 | 0.511356 |
| tossup_correctness | category | Literature | 1422 | 0.0142181 | 0.14224 | 0.678024 | 0.45134 |
| tossup_correctness | category | Mythology | 318 | 0.0323433 | 0.152076 | 0.664447 | 0.482555 |
| tossup_correctness | category | Other Academic | 66 | 0.173253 | 0.176041 | 0.805151 | 0.520361 |
| tossup_correctness | category | Philosophy | 311 | 0.0927118 | 0.169767 | 0.724192 | 0.509559 |
| tossup_correctness | category | Popular Culture | 102 | 0.0500011 | 0.107785 | 0.52037 | 0.37793 |
| tossup_correctness | category | Religion | 358 | 0.032533 | 0.180104 | 0.714144 | 0.541442 |
| tossup_correctness | category | Science | 1433 | 0.0353074 | 0.174348 | 0.695014 | 0.528616 |
| tossup_correctness | category | Social Science | 324 | 0.0562862 | 0.160548 | 0.776226 | 0.489719 |
| tossup_correctness | category | Unknown | 1937 | 0.0227995 | 0.167633 | 0.686238 | 0.513301 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.0771567 | 0.203809 | 0.618172 | 0.603778 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0233649 | 0.172825 | 0.722042 | 0.521383 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0280159 | 0.163885 | 0.714156 | 0.502459 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0171101 | 0.155662 | 0.693222 | 0.484155 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0117173 | 0.16047 | 0.717758 | 0.493123 |
