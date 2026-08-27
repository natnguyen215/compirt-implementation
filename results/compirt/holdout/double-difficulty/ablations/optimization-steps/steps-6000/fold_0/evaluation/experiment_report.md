# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.713728 |
| log_loss | 0.490477 |
| ece | 0.0117137 |
| brier | 0.159407 |
| accuracy | 0.775901 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0106509 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.147079 |
| probability_p10 | 0.567338 |
| probability_p50 | 0.812558 |
| probability_p90 | 0.91948 |
| mean_predictive_variance | 0.153715 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0975055 |
| joint_tossup_event_log_loss | 6.50634 |
| buzz_position_mae | 0.14499 |
| buzz_position_median_absolute_error | 0.125846 |
| buzz_position_bias | -0.0233491 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.371382 |
| first_buzzer_mean_reciprocal_rank | 0.581251 |
| first_buzzer_log_loss | 1.63583 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.713728 |
| neg_average_precision | 0.447956 |
| neg_precision | 0.584041 |
| neg_recall | 0.157654 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.183597 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0121959 |
| no_buzz_calibration_error | -0.0010737 |
| no_buzz_brier | 0.0130309 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0233491 | -0.0469521 |
| Q1 (0-.2) | 197 | 0.376914 | 0.37449 |
| Q2 (.2-.4) | 985 | 0.224656 | 0.219138 |
| Q3 (.4-.6) | 2251 | 0.0766921 | 0.0738575 |
| Q4 (.6-.8) | 2866 | -0.0529338 | -0.0531123 |
| Q5 (.8-1) | 2996 | -0.178069 | -0.172748 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0117137 | 0.159407 | 0.713728 | 0.490477 |
| tossup_correctness | tier | fall | 2933 | 0.0142347 | 0.148418 | 0.711434 | 0.463386 |
| tossup_correctness | tier | nationals | 1584 | 0.0375772 | 0.176118 | 0.706438 | 0.533354 |
| tossup_correctness | tier | regionals | 1886 | 0.0283934 | 0.170798 | 0.709475 | 0.516414 |
| tossup_correctness | tier | winter | 2892 | 0.0178425 | 0.153971 | 0.720442 | 0.477553 |
| tossup_correctness | category | Current Events | 124 | 0.0648894 | 0.168393 | 0.681929 | 0.520267 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0253091 | 0.160577 | 0.709222 | 0.496302 |
| tossup_correctness | category | Geography | 197 | 0.0873116 | 0.169323 | 0.790093 | 0.512102 |
| tossup_correctness | category | History | 1491 | 0.0183761 | 0.149257 | 0.720508 | 0.46389 |
| tossup_correctness | category | Literature | 1472 | 0.0279343 | 0.13705 | 0.731985 | 0.435881 |
| tossup_correctness | category | Mythology | 332 | 0.0339976 | 0.141551 | 0.695998 | 0.448372 |
| tossup_correctness | category | Other Academic | 69 | 0.0786791 | 0.174102 | 0.692308 | 0.522383 |
| tossup_correctness | category | Philosophy | 324 | 0.0189717 | 0.149774 | 0.684704 | 0.467813 |
| tossup_correctness | category | Popular Culture | 102 | 0.066987 | 0.148678 | 0.43737 | 0.484466 |
| tossup_correctness | category | Religion | 372 | 0.0438365 | 0.183494 | 0.716084 | 0.543716 |
| tossup_correctness | category | Science | 1487 | 0.026829 | 0.170191 | 0.684897 | 0.518104 |
| tossup_correctness | category | Social Science | 336 | 0.0464328 | 0.178261 | 0.729619 | 0.536784 |
| tossup_correctness | category | Unknown | 1886 | 0.0283934 | 0.170798 | 0.709475 | 0.516414 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.0607005 | 0.170749 | 0.682891 | 0.526151 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.033217 | 0.171594 | 0.720418 | 0.517346 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0244188 | 0.161987 | 0.694436 | 0.49818 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0119978 | 0.153586 | 0.700217 | 0.477389 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0239593 | 0.158284 | 0.736824 | 0.486031 |
