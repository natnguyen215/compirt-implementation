# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.629115 |
| log_loss | 0.63125 |
| ece | 0.192637 |
| brier | 0.218613 |
| accuracy | 0.66638 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0988704 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.170399 |
| probability_p10 | 0.329714 |
| probability_p50 | 0.596104 |
| probability_p90 | 0.7744 |
| mean_predictive_variance | 0.215689 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.098032 |
| joint_tossup_event_log_loss | 6.8354 |
| buzz_position_mae | 0.142068 |
| buzz_position_median_absolute_error | 0.116013 |
| buzz_position_bias | -0.00234295 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.368908 |
| first_buzzer_mean_reciprocal_rank | 0.579109 |
| first_buzzer_log_loss | 1.68521 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.629115 |
| neg_average_precision | 0.324649 |
| neg_precision | 0.33723 |
| neg_recall | 0.436297 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.143843 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0490115 |
| no_buzz_calibration_error | 0.0357418 |
| no_buzz_brier | 0.0185262 |
| full_pmf_max_mass_error | 1.55431e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.00234295 | -0.0207314 |
| Q1 (0-.2) | 197 | 0.386788 | 0.400747 |
| Q2 (.2-.4) | 985 | 0.231998 | 0.225281 |
| Q3 (.4-.6) | 2251 | 0.0893017 | 0.0876107 |
| Q4 (.6-.8) | 2866 | -0.0300561 | -0.0235704 |
| Q5 (.8-1) | 2996 | -0.14732 | -0.135122 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.192637 | 0.218613 | 0.629115 | 0.63125 |
| tossup_correctness | tier | fall | 2933 | 0.217319 | 0.21682 | 0.629788 | 0.628551 |
| tossup_correctness | tier | nationals | 1584 | 0.124993 | 0.211455 | 0.622818 | 0.612601 |
| tossup_correctness | tier | regionals | 1886 | 0.183125 | 0.219893 | 0.647748 | 0.631175 |
| tossup_correctness | tier | winter | 2892 | 0.212395 | 0.223518 | 0.628027 | 0.644249 |
| tossup_correctness | category | Current Events | 124 | 0.231798 | 0.243464 | 0.594173 | 0.69291 |
| tossup_correctness | category | Fine Arts | 1103 | 0.183334 | 0.218187 | 0.618409 | 0.631545 |
| tossup_correctness | category | Geography | 197 | 0.172065 | 0.244832 | 0.635315 | 0.684776 |
| tossup_correctness | category | History | 1491 | 0.192038 | 0.200049 | 0.659653 | 0.589749 |
| tossup_correctness | category | Literature | 1472 | 0.192671 | 0.206232 | 0.579192 | 0.605686 |
| tossup_correctness | category | Mythology | 332 | 0.223579 | 0.21572 | 0.589307 | 0.627724 |
| tossup_correctness | category | Other Academic | 69 | 0.196135 | 0.224053 | 0.570136 | 0.640456 |
| tossup_correctness | category | Philosophy | 324 | 0.176629 | 0.19895 | 0.604633 | 0.587647 |
| tossup_correctness | category | Popular Culture | 102 | 0.35902 | 0.297646 | 0.524567 | 0.815367 |
| tossup_correctness | category | Religion | 372 | 0.131963 | 0.224002 | 0.641309 | 0.644345 |
| tossup_correctness | category | Science | 1487 | 0.223215 | 0.239464 | 0.611323 | 0.677079 |
| tossup_correctness | category | Social Science | 336 | 0.159562 | 0.223383 | 0.667881 | 0.643144 |
| tossup_correctness | category | Unknown | 1886 | 0.183125 | 0.219893 | 0.647748 | 0.631175 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.264338 | 0.255374 | 0.659814 | 0.714617 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.231629 | 0.249841 | 0.616565 | 0.700236 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.216922 | 0.227846 | 0.62092 | 0.652514 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.203587 | 0.212908 | 0.638098 | 0.618836 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.146886 | 0.204451 | 0.6319 | 0.598986 |
