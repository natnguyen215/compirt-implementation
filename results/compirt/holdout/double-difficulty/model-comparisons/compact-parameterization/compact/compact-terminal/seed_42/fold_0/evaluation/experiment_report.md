# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.711796 |
| log_loss | 0.527693 |
| ece | 0.0772385 |
| brier | 0.173512 |
| accuracy | 0.752232 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.0130178 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.232061 |
| probability_p10 | 0.341679 |
| probability_p50 | 0.764407 |
| probability_p90 | 0.941542 |
| mean_predictive_variance | 0.156674 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0990541 |
| joint_tossup_event_log_loss | 6.46783 |
| buzz_position_mae | 0.149467 |
| buzz_position_median_absolute_error | 0.130812 |
| buzz_position_bias | -0.0490806 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.400108 |
| first_buzzer_mean_reciprocal_rank | 0.606797 |
| first_buzzer_log_loss | 1.55805 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.711796 |
| neg_average_precision | 0.43706 |
| neg_precision | 0.466593 |
| neg_recall | 0.387259 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.169002 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.00928608 |
| no_buzz_calibration_error | -0.00398356 |
| no_buzz_brier | 0.012487 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0490806 | -0.0694632 |
| Q1 (0-.2) | 197 | 0.348808 | 0.353464 |
| Q2 (.2-.4) | 985 | 0.190955 | 0.184058 |
| Q3 (.4-.6) | 2251 | 0.0458978 | 0.0398426 |
| Q4 (.6-.8) | 2866 | -0.0793903 | -0.0790895 |
| Q5 (.8-1) | 2996 | -0.196527 | -0.190909 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0772385 | 0.173512 | 0.711796 | 0.527693 |
| tossup_correctness | tier | fall | 2933 | 0.076833 | 0.162321 | 0.708948 | 0.496953 |
| tossup_correctness | tier | nationals | 1584 | 0.0812063 | 0.188708 | 0.704055 | 0.563057 |
| tossup_correctness | tier | regionals | 1886 | 0.0798244 | 0.185137 | 0.706612 | 0.559836 |
| tossup_correctness | tier | winter | 2892 | 0.0756758 | 0.168957 | 0.716133 | 0.518538 |
| tossup_correctness | category | Current Events | 124 | 0.112545 | 0.189613 | 0.676032 | 0.565953 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0636811 | 0.166866 | 0.714315 | 0.512617 |
| tossup_correctness | category | Geography | 197 | 0.0999932 | 0.190404 | 0.755128 | 0.576837 |
| tossup_correctness | category | History | 1491 | 0.0896049 | 0.16373 | 0.734626 | 0.501716 |
| tossup_correctness | category | Literature | 1472 | 0.0783645 | 0.156426 | 0.713715 | 0.487237 |
| tossup_correctness | category | Mythology | 332 | 0.103505 | 0.160313 | 0.658901 | 0.496032 |
| tossup_correctness | category | Other Academic | 69 | 0.100981 | 0.17514 | 0.702489 | 0.527965 |
| tossup_correctness | category | Philosophy | 324 | 0.0998628 | 0.158472 | 0.703416 | 0.477184 |
| tossup_correctness | category | Popular Culture | 102 | 0.127726 | 0.150961 | 0.435294 | 0.496726 |
| tossup_correctness | category | Religion | 372 | 0.0687482 | 0.2016 | 0.677504 | 0.587253 |
| tossup_correctness | category | Science | 1487 | 0.0916514 | 0.187572 | 0.688969 | 0.558638 |
| tossup_correctness | category | Social Science | 336 | 0.0707238 | 0.173225 | 0.756907 | 0.53278 |
| tossup_correctness | category | Unknown | 1886 | 0.0798244 | 0.185137 | 0.706612 | 0.559836 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.118683 | 0.182988 | 0.70756 | 0.549007 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.066059 | 0.180067 | 0.717205 | 0.537808 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.0791054 | 0.175434 | 0.693839 | 0.532295 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.081804 | 0.168592 | 0.702786 | 0.51649 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.083248 | 0.173996 | 0.72967 | 0.530225 |
