# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.60348 |
| log_loss | 0.700408 |
| ece | 0.260539 |
| brier | 0.250141 |
| accuracy | 0.585022 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.185022 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.162868 |
| probability_p10 | 0.274874 |
| probability_p50 | 0.528582 |
| probability_p90 | 0.709369 |
| mean_predictive_variance | 0.223384 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0932968 |
| joint_tossup_event_log_loss | 6.76029 |
| buzz_position_mae | 0.137383 |
| buzz_position_median_absolute_error | 0.113291 |
| buzz_position_bias | -0.00791133 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.378304 |
| first_buzzer_mean_reciprocal_rank | 0.585863 |
| first_buzzer_log_loss | 1.6254 |
| first_buzzer_events | 9080 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.60348 |
| neg_average_precision | 0.308289 |
| neg_precision | 0.287126 |
| neg_recall | 0.542625 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.132838 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0495152 |
| no_buzz_calibration_error | 0.0343308 |
| no_buzz_brier | 0.0187992 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.00791133 | -0.0285773 |
| Q1 (0-.2) | 192 | 0.397795 | 0.398309 |
| Q2 (.2-.4) | 889 | 0.226966 | 0.229271 |
| Q3 (.4-.6) | 2210 | 0.0840134 | 0.0787057 |
| Q4 (.6-.8) | 2869 | -0.032932 | -0.0292772 |
| Q5 (.8-1) | 2920 | -0.151086 | -0.14317 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.260539 | 0.250141 | 0.60348 | 0.700408 |
| tossup_correctness | tier | fall | 2817 | 0.286714 | 0.257893 | 0.603815 | 0.717802 |
| tossup_correctness | tier | nationals | 1542 | 0.198953 | 0.238509 | 0.580034 | 0.67046 |
| tossup_correctness | tier | regionals | 1934 | 0.243279 | 0.243743 | 0.631829 | 0.688496 |
| tossup_correctness | tier | winter | 2787 | 0.280133 | 0.253182 | 0.605402 | 0.707663 |
| tossup_correctness | category | Current Events | 125 | 0.203499 | 0.256449 | 0.603194 | 0.717674 |
| tossup_correctness | category | Fine Arts | 1072 | 0.259219 | 0.252585 | 0.582885 | 0.70507 |
| tossup_correctness | category | Geography | 185 | 0.238721 | 0.281061 | 0.550909 | 0.76775 |
| tossup_correctness | category | History | 1443 | 0.268948 | 0.256727 | 0.597166 | 0.713673 |
| tossup_correctness | category | Literature | 1411 | 0.280841 | 0.244083 | 0.56989 | 0.686034 |
| tossup_correctness | category | Mythology | 320 | 0.28345 | 0.25267 | 0.583035 | 0.702983 |
| tossup_correctness | category | Other Academic | 64 | 0.226175 | 0.230139 | 0.628906 | 0.65241 |
| tossup_correctness | category | Philosophy | 312 | 0.26545 | 0.228519 | 0.623871 | 0.650541 |
| tossup_correctness | category | Popular Culture | 104 | 0.435654 | 0.345721 | 0.522727 | 0.934896 |
| tossup_correctness | category | Religion | 358 | 0.241714 | 0.254543 | 0.623469 | 0.707888 |
| tossup_correctness | category | Science | 1431 | 0.256518 | 0.24971 | 0.606167 | 0.699605 |
| tossup_correctness | category | Social Science | 321 | 0.240334 | 0.245814 | 0.624094 | 0.689363 |
| tossup_correctness | category | Unknown | 1934 | 0.243279 | 0.243743 | 0.631829 | 0.688496 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.280613 | 0.266297 | 0.712172 | 0.737322 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.287191 | 0.276017 | 0.619412 | 0.757724 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.274787 | 0.25927 | 0.618743 | 0.72178 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.271991 | 0.248849 | 0.590686 | 0.697817 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.22908 | 0.235562 | 0.586467 | 0.666901 |
