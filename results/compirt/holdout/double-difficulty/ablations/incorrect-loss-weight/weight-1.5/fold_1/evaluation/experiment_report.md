# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.709817 |
| log_loss | 0.50685 |
| ece | 0.0595295 |
| brier | 0.165882 |
| accuracy | 0.765754 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00362917 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.175148 |
| probability_p10 | 0.451131 |
| probability_p50 | 0.744316 |
| probability_p90 | 0.89757 |
| mean_predictive_variance | 0.176985 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.100796 |
| joint_tossup_event_log_loss | 6.61288 |
| buzz_position_mae | 0.151258 |
| buzz_position_median_absolute_error | 0.133607 |
| buzz_position_bias | -0.0478597 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.34961 |
| first_buzzer_mean_reciprocal_rank | 0.563586 |
| first_buzzer_log_loss | 1.67955 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.709817 |
| neg_average_precision | 0.445967 |
| neg_precision | 0.513274 |
| neg_recall | 0.294961 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.190406 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.015123 |
| no_buzz_calibration_error | -0.000786131 |
| no_buzz_brier | 0.0154591 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.0478597 | -0.0686818 |
| Q1 (0-.2) | 167 | 0.373827 | 0.375464 |
| Q2 (.2-.4) | 912 | 0.212714 | 0.214111 |
| Q3 (.4-.6) | 2115 | 0.0625471 | 0.0599493 |
| Q4 (.6-.8) | 2844 | -0.0691461 | -0.070583 |
| Q5 (.8-1) | 3055 | -0.205318 | -0.202762 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0595295 | 0.165882 | 0.709817 | 0.50685 |
| tossup_correctness | tier | fall | 2842 | 0.0619696 | 0.15387 | 0.727957 | 0.476501 |
| tossup_correctness | tier | nationals | 1564 | 0.0398234 | 0.178317 | 0.715156 | 0.536636 |
| tossup_correctness | tier | regionals | 1937 | 0.0621666 | 0.172268 | 0.686865 | 0.523434 |
| tossup_correctness | tier | winter | 2750 | 0.0677087 | 0.166726 | 0.70003 | 0.509594 |
| tossup_correctness | category | Current Events | 126 | 0.119414 | 0.170507 | 0.719517 | 0.517 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0673684 | 0.156217 | 0.749452 | 0.481502 |
| tossup_correctness | category | Geography | 185 | 0.114087 | 0.170946 | 0.792774 | 0.520991 |
| tossup_correctness | category | History | 1440 | 0.0489481 | 0.1703 | 0.707458 | 0.515799 |
| tossup_correctness | category | Literature | 1422 | 0.0734285 | 0.149356 | 0.6782 | 0.468112 |
| tossup_correctness | category | Mythology | 318 | 0.0864328 | 0.157364 | 0.665814 | 0.493664 |
| tossup_correctness | category | Other Academic | 66 | 0.162526 | 0.164343 | 0.81299 | 0.500371 |
| tossup_correctness | category | Philosophy | 311 | 0.0531433 | 0.168955 | 0.721846 | 0.508549 |
| tossup_correctness | category | Popular Culture | 102 | 0.105753 | 0.117931 | 0.533333 | 0.404488 |
| tossup_correctness | category | Religion | 358 | 0.062373 | 0.182428 | 0.714182 | 0.54697 |
| tossup_correctness | category | Science | 1433 | 0.0483852 | 0.176969 | 0.696106 | 0.532861 |
| tossup_correctness | category | Social Science | 324 | 0.0744144 | 0.161362 | 0.778214 | 0.495206 |
| tossup_correctness | category | Unknown | 1937 | 0.0621666 | 0.172268 | 0.686865 | 0.523434 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.09184 | 0.208042 | 0.619048 | 0.611954 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.0554502 | 0.176552 | 0.723235 | 0.529628 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0464387 | 0.165651 | 0.712891 | 0.506749 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0611699 | 0.160139 | 0.693008 | 0.49449 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0688355 | 0.165898 | 0.720289 | 0.505882 |
