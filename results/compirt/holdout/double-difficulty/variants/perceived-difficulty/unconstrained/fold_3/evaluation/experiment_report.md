# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.661646 |
| log_loss | 0.512578 |
| ece | 0.0365519 |
| brier | 0.167061 |
| accuracy | 0.773128 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0030837 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.133809 |
| probability_p10 | 0.552824 |
| probability_p50 | 0.763338 |
| probability_p90 | 0.89244 |
| mean_predictive_variance | 0.174842 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.1673 |
| joint_tossup_event_log_loss | 7.57409 |
| buzz_position_mae | 0.325361 |
| buzz_position_median_absolute_error | 0.326363 |
| buzz_position_bias | -0.310058 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.350551 |
| first_buzzer_mean_reciprocal_rank | 0.563427 |
| first_buzzer_log_loss | 1.68418 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.661646 |
| neg_average_precision | 0.385052 |
| neg_precision | 0.526119 |
| neg_recall | 0.135057 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0328142 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.216943 |
| no_buzz_calibration_error | 0.201758 |
| no_buzz_brier | 0.0644995 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.310058 | -0.326088 |
| Q1 (0-.2) | 192 | 0.188706 | 0.185272 |
| Q2 (.2-.4) | 889 | 0.019583 | 0.0157281 |
| Q3 (.4-.6) | 2210 | -0.158284 | -0.159673 |
| Q4 (.6-.8) | 2869 | -0.337563 | -0.33699 |
| Q5 (.8-1) | 2920 | -0.531057 | -0.535449 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0365519 | 0.167061 | 0.661646 | 0.512578 |
| tossup_correctness | tier | fall | 2817 | 0.0129398 | 0.16033 | 0.656333 | 0.496659 |
| tossup_correctness | tier | nationals | 1542 | 0.121175 | 0.188049 | 0.712709 | 0.560192 |
| tossup_correctness | tier | regionals | 1934 | 0.0458959 | 0.174668 | 0.659698 | 0.529057 |
| tossup_correctness | tier | winter | 2787 | 0.0269388 | 0.156974 | 0.656868 | 0.49089 |
| tossup_correctness | category | Current Events | 125 | 0.0855678 | 0.204609 | 0.627764 | 0.595293 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0443253 | 0.167395 | 0.65146 | 0.511621 |
| tossup_correctness | category | Geography | 185 | 0.0682339 | 0.177609 | 0.738601 | 0.532598 |
| tossup_correctness | category | History | 1443 | 0.0304581 | 0.163577 | 0.693758 | 0.501463 |
| tossup_correctness | category | Literature | 1411 | 0.0508812 | 0.151328 | 0.597738 | 0.483651 |
| tossup_correctness | category | Mythology | 320 | 0.0612082 | 0.161874 | 0.614591 | 0.504876 |
| tossup_correctness | category | Other Academic | 64 | 0.143355 | 0.190936 | 0.601562 | 0.569351 |
| tossup_correctness | category | Philosophy | 312 | 0.0649785 | 0.163213 | 0.571935 | 0.506853 |
| tossup_correctness | category | Popular Culture | 104 | 0.133547 | 0.144847 | 0.53267 | 0.47131 |
| tossup_correctness | category | Religion | 358 | 0.0306623 | 0.18279 | 0.673587 | 0.547153 |
| tossup_correctness | category | Science | 1431 | 0.0373631 | 0.167415 | 0.676201 | 0.511329 |
| tossup_correctness | category | Social Science | 321 | 0.03819 | 0.176459 | 0.692979 | 0.532164 |
| tossup_correctness | category | Unknown | 1934 | 0.0458959 | 0.174668 | 0.659698 | 0.529057 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0504225 | 0.190252 | 0.708312 | 0.559755 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0233729 | 0.179862 | 0.679273 | 0.539956 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0344822 | 0.174793 | 0.64429 | 0.531148 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0549523 | 0.160106 | 0.652331 | 0.496966 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0451952 | 0.16262 | 0.669866 | 0.502427 |
