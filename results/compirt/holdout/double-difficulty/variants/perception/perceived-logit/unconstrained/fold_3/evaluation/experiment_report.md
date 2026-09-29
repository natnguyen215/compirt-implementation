# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.546423 |
| log_loss | 0.603306 |
| ece | 0.103786 |
| brier | 0.188603 |
| accuracy | 0.769163 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.000881057 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.0972724 |
| probability_p10 | 0.722096 |
| probability_p50 | 0.893828 |
| probability_p90 | 0.953147 |
| mean_predictive_variance | 0.108212 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.176747 |
| joint_tossup_event_log_loss | 7.77171 |
| buzz_position_mae | 0.342914 |
| buzz_position_median_absolute_error | 0.344309 |
| buzz_position_bias | -0.330095 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.347907 |
| first_buzzer_mean_reciprocal_rank | 0.562802 |
| first_buzzer_log_loss | 1.6774 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.546423 |
| neg_average_precision | 0.271995 |
| neg_precision | 0.425926 |
| neg_recall | 0.0110153 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0284681 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.230545 |
| no_buzz_calibration_error | 0.21536 |
| no_buzz_brier | 0.0703191 |
| full_pmf_max_mass_error | 1.11022e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.330095 | -0.344309 |
| Q1 (0-.2) | 192 | 0.171319 | 0.171101 |
| Q2 (.2-.4) | 889 | 0.00323609 | -0.000166832 |
| Q3 (.4-.6) | 2210 | -0.176406 | -0.176523 |
| Q4 (.6-.8) | 2869 | -0.357814 | -0.357385 |
| Q5 (.8-1) | 2920 | -0.553634 | -0.556709 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.103786 | 0.188603 | 0.546423 | 0.603306 |
| tossup_correctness | tier | fall | 2817 | 0.0950134 | 0.180301 | 0.549521 | 0.571625 |
| tossup_correctness | tier | nationals | 1542 | 0.102047 | 0.201693 | 0.600013 | 0.622359 |
| tossup_correctness | tier | regionals | 1934 | 0.126248 | 0.200985 | 0.531553 | 0.647321 |
| tossup_correctness | tier | winter | 2787 | 0.106435 | 0.181161 | 0.510514 | 0.594243 |
| tossup_correctness | category | Current Events | 125 | 0.141257 | 0.220517 | 0.616093 | 0.653665 |
| tossup_correctness | category | Fine Arts | 1072 | 0.12537 | 0.191116 | 0.557459 | 0.610037 |
| tossup_correctness | category | Geography | 185 | 0.151941 | 0.220703 | 0.601259 | 0.675963 |
| tossup_correctness | category | History | 1443 | 0.0857753 | 0.187979 | 0.557306 | 0.592842 |
| tossup_correctness | category | Literature | 1411 | 0.0828903 | 0.161926 | 0.511067 | 0.541007 |
| tossup_correctness | category | Mythology | 320 | 0.090219 | 0.171806 | 0.52917 | 0.557734 |
| tossup_correctness | category | Other Academic | 64 | 0.17918 | 0.207091 | 0.589844 | 0.62879 |
| tossup_correctness | category | Philosophy | 312 | 0.111716 | 0.168296 | 0.522258 | 0.556271 |
| tossup_correctness | category | Popular Culture | 104 | 0.0639107 | 0.137973 | 0.536222 | 0.455017 |
| tossup_correctness | category | Religion | 358 | 0.165729 | 0.222271 | 0.540424 | 0.701235 |
| tossup_correctness | category | Science | 1431 | 0.0919131 | 0.186823 | 0.575212 | 0.587004 |
| tossup_correctness | category | Social Science | 321 | 0.147338 | 0.214347 | 0.508368 | 0.672618 |
| tossup_correctness | category | Unknown | 1934 | 0.126248 | 0.200985 | 0.531553 | 0.647321 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.178072 | 0.233505 | 0.501287 | 0.709805 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.105149 | 0.209025 | 0.537603 | 0.644684 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.107697 | 0.198275 | 0.502793 | 0.628736 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0920796 | 0.174136 | 0.557785 | 0.56039 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.1136 | 0.186329 | 0.565002 | 0.606626 |
