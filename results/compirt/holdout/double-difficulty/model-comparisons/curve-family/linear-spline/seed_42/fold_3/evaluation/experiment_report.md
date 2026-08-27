# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.724893 |
| log_loss | 0.557806 |
| ece | 0.115058 |
| brier | 0.17754 |
| accuracy | 0.740749 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.0292952 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.272645 |
| probability_p10 | 0.261433 |
| probability_p50 | 0.770203 |
| probability_p90 | 0.983287 |
| mean_predictive_variance | 0.138676 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0911437 |
| joint_tossup_event_log_loss | 6.4042 |
| buzz_position_mae | 0.134339 |
| buzz_position_median_absolute_error | 0.109435 |
| buzz_position_bias | -0.0020722 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.403084 |
| first_buzzer_mean_reciprocal_rank | 0.605362 |
| first_buzzer_log_loss | 1.5812 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.724893 |
| neg_average_precision | 0.448407 |
| neg_precision | 0.440572 |
| neg_recall | 0.472222 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.171366 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0465598 |
| no_buzz_calibration_error | 0.0313754 |
| no_buzz_brier | 0.0178544 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0020722 | -0.0217922 |
| Q1 (0-.2) | 192 | 0.396174 | 0.39547 |
| Q2 (.2-.4) | 889 | 0.226691 | 0.225004 |
| Q3 (.4-.6) | 2210 | 0.0920678 | 0.0849341 |
| Q4 (.6-.8) | 2869 | -0.029197 | -0.0273435 |
| Q5 (.8-1) | 2920 | -0.142504 | -0.13432 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.115058 | 0.17754 | 0.724893 | 0.557806 |
| tossup_correctness | tier | fall | 2817 | 0.108892 | 0.169616 | 0.71341 | 0.554361 |
| tossup_correctness | tier | nationals | 1542 | 0.101076 | 0.186004 | 0.735078 | 0.559579 |
| tossup_correctness | tier | regionals | 1934 | 0.120832 | 0.183675 | 0.733912 | 0.559746 |
| tossup_correctness | tier | winter | 2787 | 0.12502 | 0.176608 | 0.718102 | 0.558959 |
| tossup_correctness | category | Current Events | 125 | 0.0706425 | 0.169803 | 0.792383 | 0.507796 |
| tossup_correctness | category | Fine Arts | 1072 | 0.124921 | 0.178767 | 0.719473 | 0.574434 |
| tossup_correctness | category | Geography | 185 | 0.139217 | 0.191469 | 0.766713 | 0.58423 |
| tossup_correctness | category | History | 1443 | 0.10931 | 0.17627 | 0.734909 | 0.549815 |
| tossup_correctness | category | Literature | 1411 | 0.125721 | 0.168284 | 0.689097 | 0.544959 |
| tossup_correctness | category | Mythology | 320 | 0.112467 | 0.158852 | 0.718921 | 0.519127 |
| tossup_correctness | category | Other Academic | 64 | 0.127684 | 0.200443 | 0.652344 | 0.609745 |
| tossup_correctness | category | Philosophy | 312 | 0.129597 | 0.17825 | 0.69729 | 0.549483 |
| tossup_correctness | category | Popular Culture | 104 | 0.141553 | 0.168933 | 0.654119 | 0.59097 |
| tossup_correctness | category | Religion | 358 | 0.105125 | 0.191545 | 0.729631 | 0.597796 |
| tossup_correctness | category | Science | 1431 | 0.109025 | 0.179673 | 0.717871 | 0.565551 |
| tossup_correctness | category | Social Science | 321 | 0.117273 | 0.168885 | 0.747678 | 0.533636 |
| tossup_correctness | category | Unknown | 1934 | 0.120832 | 0.183675 | 0.733912 | 0.559746 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.129497 | 0.188054 | 0.786413 | 0.588304 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.10676 | 0.173567 | 0.774287 | 0.53834 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.120444 | 0.180899 | 0.712124 | 0.576531 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0934607 | 0.164321 | 0.721833 | 0.524637 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.135055 | 0.188503 | 0.713708 | 0.580144 |
