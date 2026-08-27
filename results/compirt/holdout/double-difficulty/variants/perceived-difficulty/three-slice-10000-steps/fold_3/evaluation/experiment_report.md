# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.625209 |
| log_loss | 0.634528 |
| ece | 0.203605 |
| brier | 0.220693 |
| accuracy | 0.654626 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.115419 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.169737 |
| probability_p10 | 0.319444 |
| probability_p50 | 0.590609 |
| probability_p90 | 0.76998 |
| mean_predictive_variance | 0.216775 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0933127 |
| joint_tossup_event_log_loss | 6.66622 |
| buzz_position_mae | 0.137081 |
| buzz_position_median_absolute_error | 0.113652 |
| buzz_position_bias | -0.0037748 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.375 |
| first_buzzer_mean_reciprocal_rank | 0.581981 |
| first_buzzer_log_loss | 1.64024 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.625209 |
| neg_average_precision | 0.322367 |
| neg_precision | 0.320425 |
| neg_recall | 0.447797 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.141288 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.047807 |
| no_buzz_calibration_error | 0.0326226 |
| no_buzz_brier | 0.0181346 |
| full_pmf_max_mass_error | 1.44329e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0037748 | -0.0246783 |
| Q1 (0-.2) | 192 | 0.405996 | 0.405703 |
| Q2 (.2-.4) | 889 | 0.23308 | 0.230996 |
| Q3 (.4-.6) | 2210 | 0.0890708 | 0.0833316 |
| Q4 (.6-.8) | 2869 | -0.029293 | -0.0256632 |
| Q5 (.8-1) | 2920 | -0.148027 | -0.137505 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.203605 | 0.220693 | 0.625209 | 0.634528 |
| tossup_correctness | tier | fall | 2817 | 0.206236 | 0.2148 | 0.626998 | 0.62137 |
| tossup_correctness | tier | nationals | 1542 | 0.144254 | 0.2143 | 0.608728 | 0.617192 |
| tossup_correctness | tier | regionals | 1934 | 0.196368 | 0.216296 | 0.662406 | 0.623659 |
| tossup_correctness | tier | winter | 2787 | 0.238807 | 0.233236 | 0.61182 | 0.664962 |
| tossup_correctness | category | Current Events | 125 | 0.117267 | 0.227027 | 0.626229 | 0.649303 |
| tossup_correctness | category | Fine Arts | 1072 | 0.203883 | 0.225876 | 0.602025 | 0.645144 |
| tossup_correctness | category | Geography | 185 | 0.18842 | 0.247223 | 0.612168 | 0.692719 |
| tossup_correctness | category | History | 1443 | 0.191877 | 0.216808 | 0.631156 | 0.627245 |
| tossup_correctness | category | Literature | 1411 | 0.224828 | 0.214381 | 0.577833 | 0.619744 |
| tossup_correctness | category | Mythology | 320 | 0.206059 | 0.215478 | 0.588046 | 0.623015 |
| tossup_correctness | category | Other Academic | 64 | 0.157725 | 0.202504 | 0.647135 | 0.592655 |
| tossup_correctness | category | Philosophy | 312 | 0.207655 | 0.205922 | 0.599484 | 0.601316 |
| tossup_correctness | category | Popular Culture | 104 | 0.380644 | 0.306061 | 0.537642 | 0.843881 |
| tossup_correctness | category | Religion | 358 | 0.170086 | 0.222339 | 0.63854 | 0.640058 |
| tossup_correctness | category | Science | 1431 | 0.217043 | 0.228873 | 0.623084 | 0.652313 |
| tossup_correctness | category | Social Science | 321 | 0.183871 | 0.214535 | 0.667925 | 0.621825 |
| tossup_correctness | category | Unknown | 1934 | 0.196368 | 0.216296 | 0.662406 | 0.623659 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.226072 | 0.239615 | 0.706639 | 0.67818 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.230126 | 0.2421 | 0.645524 | 0.682048 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.21858 | 0.230494 | 0.632799 | 0.658219 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.213733 | 0.219272 | 0.607196 | 0.631554 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.172769 | 0.206909 | 0.620753 | 0.602181 |
