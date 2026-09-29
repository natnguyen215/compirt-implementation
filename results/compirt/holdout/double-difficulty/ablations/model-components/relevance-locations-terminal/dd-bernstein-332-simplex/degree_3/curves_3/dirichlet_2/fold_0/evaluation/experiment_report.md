# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.71083 |
| log_loss | 0.505064 |
| ece | 0.0650813 |
| brier | 0.165056 |
| accuracy | 0.769123 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00387305 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.165526 |
| probability_p10 | 0.464448 |
| probability_p50 | 0.727856 |
| probability_p90 | 0.89504 |
| mean_predictive_variance | 0.182534 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.108224 |
| joint_tossup_event_log_loss | 6.75648 |
| buzz_position_mae | 0.180273 |
| buzz_position_median_absolute_error | 0.160656 |
| buzz_position_bias | -0.0980988 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.343303 |
| first_buzzer_mean_reciprocal_rank | 0.557551 |
| first_buzzer_log_loss | 1.68872 |
| first_buzzer_events | 9295 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.71083 |
| neg_average_precision | 0.443013 |
| neg_precision | 0.515126 |
| neg_recall | 0.280935 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0939205 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0809122 |
| no_buzz_calibration_error | 0.0676426 |
| no_buzz_brier | 0.0246731 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9295 | -0.0980988 | -0.111806 |
| Q1 (0-.2) | 197 | 0.336035 | 0.329561 |
| Q2 (.2-.4) | 985 | 0.175903 | 0.168272 |
| Q3 (.4-.6) | 2251 | 0.0206755 | 0.0189077 |
| Q4 (.6-.8) | 2866 | -0.124323 | -0.123632 |
| Q5 (.8-1) | 2996 | -0.280882 | -0.276099 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.0650813 | 0.165056 | 0.71083 | 0.505064 |
| tossup_correctness | tier | fall | 2933 | 0.070622 | 0.156721 | 0.698184 | 0.485795 |
| tossup_correctness | tier | nationals | 1584 | 0.0661985 | 0.18412 | 0.695228 | 0.549322 |
| tossup_correctness | tier | regionals | 1886 | 0.0719302 | 0.175155 | 0.706233 | 0.527847 |
| tossup_correctness | tier | winter | 2892 | 0.0569849 | 0.156482 | 0.727194 | 0.485506 |
| tossup_correctness | category | Current Events | 124 | 0.121481 | 0.177074 | 0.700659 | 0.53224 |
| tossup_correctness | category | Fine Arts | 1103 | 0.0596052 | 0.162869 | 0.714531 | 0.502939 |
| tossup_correctness | category | Geography | 197 | 0.111985 | 0.177975 | 0.771911 | 0.540881 |
| tossup_correctness | category | History | 1491 | 0.0807639 | 0.155669 | 0.723897 | 0.481298 |
| tossup_correctness | category | Literature | 1472 | 0.0575856 | 0.143113 | 0.726785 | 0.451677 |
| tossup_correctness | category | Mythology | 332 | 0.103262 | 0.156256 | 0.638053 | 0.493972 |
| tossup_correctness | category | Other Academic | 69 | 0.15251 | 0.182055 | 0.683258 | 0.543063 |
| tossup_correctness | category | Philosophy | 324 | 0.0849711 | 0.161771 | 0.655836 | 0.494033 |
| tossup_correctness | category | Popular Culture | 102 | 0.130246 | 0.152143 | 0.480277 | 0.489084 |
| tossup_correctness | category | Religion | 372 | 0.0555482 | 0.186932 | 0.709035 | 0.552077 |
| tossup_correctness | category | Science | 1487 | 0.0708774 | 0.177384 | 0.682247 | 0.534713 |
| tossup_correctness | category | Social Science | 336 | 0.0707191 | 0.174845 | 0.74661 | 0.527844 |
| tossup_correctness | category | Unknown | 1886 | 0.0719302 | 0.175155 | 0.706233 | 0.527847 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.121273 | 0.177492 | 0.716976 | 0.54286 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.0595006 | 0.176991 | 0.714549 | 0.531799 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.065231 | 0.167626 | 0.691298 | 0.512765 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.0718231 | 0.158607 | 0.707122 | 0.489107 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.0593176 | 0.164553 | 0.725311 | 0.503266 |
