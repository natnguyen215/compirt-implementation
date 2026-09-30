# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.708553 |
| log_loss | 0.517602 |
| ece | 0.0738198 |
| brier | 0.168164 |
| accuracy | 0.761465 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.000659848 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.200427 |
| probability_p10 | 0.425335 |
| probability_p50 | 0.741152 |
| probability_p90 | 0.946136 |
| mean_predictive_variance | 0.16594 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0939638 |
| joint_tossup_event_log_loss | 6.51687 |
| buzz_position_mae | 0.138731 |
| buzz_position_median_absolute_error | 0.115824 |
| buzz_position_bias | -0.00575687 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.375234 |
| first_buzzer_mean_reciprocal_rank | 0.583231 |
| first_buzzer_log_loss | 1.63383 |
| first_buzzer_events | 9093 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.708553 |
| neg_average_precision | 0.450125 |
| neg_precision | 0.497984 |
| neg_recall | 0.34258 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.131315 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0611049 |
| no_buzz_calibration_error | 0.0451958 |
| no_buzz_brier | 0.0239801 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9093 | -0.00575687 | -0.0256511 |
| Q1 (0-.2) | 167 | 0.40002 | 0.415131 |
| Q2 (.2-.4) | 912 | 0.236465 | 0.236982 |
| Q3 (.4-.6) | 2115 | 0.0951255 | 0.0944028 |
| Q4 (.6-.8) | 2844 | -0.0240308 | -0.0209688 |
| Q5 (.8-1) | 3055 | -0.153078 | -0.145604 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.0738198 | 0.168164 | 0.708553 | 0.517602 |
| tossup_correctness | tier | fall | 2842 | 0.0595026 | 0.154337 | 0.725961 | 0.480402 |
| tossup_correctness | tier | nationals | 1564 | 0.0835654 | 0.188593 | 0.70169 | 0.568796 |
| tossup_correctness | tier | regionals | 1937 | 0.0805996 | 0.175641 | 0.684172 | 0.542102 |
| tossup_correctness | tier | winter | 2750 | 0.0791304 | 0.165567 | 0.706539 | 0.509675 |
| tossup_correctness | category | Current Events | 126 | 0.12061 | 0.171365 | 0.730892 | 0.514591 |
| tossup_correctness | category | Fine Arts | 1071 | 0.0660322 | 0.156653 | 0.74742 | 0.482499 |
| tossup_correctness | category | Geography | 185 | 0.107342 | 0.166245 | 0.8134 | 0.514796 |
| tossup_correctness | category | History | 1440 | 0.069284 | 0.167594 | 0.719504 | 0.516912 |
| tossup_correctness | category | Literature | 1422 | 0.0871775 | 0.156694 | 0.658518 | 0.49159 |
| tossup_correctness | category | Mythology | 318 | 0.0805301 | 0.165719 | 0.644883 | 0.521739 |
| tossup_correctness | category | Other Academic | 66 | 0.129069 | 0.147693 | 0.836506 | 0.454677 |
| tossup_correctness | category | Philosophy | 311 | 0.0352708 | 0.167268 | 0.737451 | 0.498859 |
| tossup_correctness | category | Popular Culture | 102 | 0.124716 | 0.123433 | 0.534259 | 0.41794 |
| tossup_correctness | category | Religion | 358 | 0.0739543 | 0.189822 | 0.708129 | 0.572223 |
| tossup_correctness | category | Science | 1433 | 0.0732391 | 0.180041 | 0.697532 | 0.544047 |
| tossup_correctness | category | Social Science | 324 | 0.0683061 | 0.159273 | 0.76929 | 0.48799 |
| tossup_correctness | category | Unknown | 1937 | 0.0805996 | 0.175641 | 0.684172 | 0.542102 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.190497 | 0.220907 | 0.648985 | 0.656549 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.112349 | 0.190245 | 0.714085 | 0.561922 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.0780254 | 0.170601 | 0.712492 | 0.524751 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.0760396 | 0.16326 | 0.697449 | 0.505092 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.0510913 | 0.161566 | 0.717411 | 0.503474 |
