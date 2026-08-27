# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.707079 |
| log_loss | 0.534907 |
| ece | 0.0795498 |
| brier | 0.176374 |
| accuracy | 0.744302 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.0198768 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.23119 |
| probability_p10 | 0.336122 |
| probability_p50 | 0.756847 |
| probability_p90 | 0.938325 |
| mean_predictive_variance | 0.159179 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0994914 |
| joint_tossup_event_log_loss | 6.49073 |
| buzz_position_mae | 0.149506 |
| buzz_position_median_absolute_error | 0.130601 |
| buzz_position_bias | -0.0476609 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.396673 |
| first_buzzer_mean_reciprocal_rank | 0.602998 |
| first_buzzer_log_loss | 1.56561 |
| first_buzzer_events | 9257 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.707079 |
| neg_average_precision | 0.427285 |
| neg_precision | 0.450324 |
| neg_recall | 0.382043 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.17381 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.00863803 |
| no_buzz_calibration_error | -0.00447498 |
| no_buzz_brier | 0.012296 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0476609 | -0.067841 |
| Q1 (0-.2) | 183 | 0.363698 | 0.371609 |
| Q2 (.2-.4) | 955 | 0.195565 | 0.191585 |
| Q3 (.4-.6) | 2239 | 0.0484704 | 0.0424426 |
| Q4 (.6-.8) | 2875 | -0.0749787 | -0.0776944 |
| Q5 (.8-1) | 3005 | -0.195501 | -0.193992 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.0795498 | 0.176374 | 0.707079 | 0.534907 |
| tossup_correctness | tier | fall | 2798 | 0.0725584 | 0.161877 | 0.724441 | 0.498259 |
| tossup_correctness | tier | nationals | 1545 | 0.0726851 | 0.1949 | 0.697693 | 0.577496 |
| tossup_correctness | tier | regionals | 2039 | 0.0952913 | 0.182979 | 0.696429 | 0.553357 |
| tossup_correctness | tier | winter | 2875 | 0.0890069 | 0.175845 | 0.698615 | 0.534602 |
| tossup_correctness | category | Current Events | 129 | 0.0703211 | 0.203558 | 0.689562 | 0.588463 |
| tossup_correctness | category | Fine Arts | 1074 | 0.0928036 | 0.174991 | 0.689968 | 0.529779 |
| tossup_correctness | category | Geography | 180 | 0.0737833 | 0.189365 | 0.755582 | 0.553451 |
| tossup_correctness | category | History | 1454 | 0.0896112 | 0.184154 | 0.691862 | 0.559035 |
| tossup_correctness | category | Literature | 1435 | 0.0733164 | 0.155545 | 0.724407 | 0.484435 |
| tossup_correctness | category | Mythology | 324 | 0.0679328 | 0.159706 | 0.681282 | 0.493542 |
| tossup_correctness | category | Other Academic | 71 | 0.110256 | 0.175842 | 0.683007 | 0.537922 |
| tossup_correctness | category | Philosophy | 310 | 0.103565 | 0.162711 | 0.759963 | 0.491599 |
| tossup_correctness | category | Popular Culture | 108 | 0.100557 | 0.116538 | 0.473958 | 0.401371 |
| tossup_correctness | category | Religion | 361 | 0.092514 | 0.184977 | 0.706066 | 0.55165 |
| tossup_correctness | category | Science | 1445 | 0.077382 | 0.18488 | 0.703859 | 0.553644 |
| tossup_correctness | category | Social Science | 327 | 0.0910721 | 0.180944 | 0.733996 | 0.54379 |
| tossup_correctness | category | Unknown | 2039 | 0.0952913 | 0.182979 | 0.696429 | 0.553357 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.148376 | 0.184967 | 0.751721 | 0.557042 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.0750786 | 0.179359 | 0.719334 | 0.543216 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.065601 | 0.175608 | 0.712714 | 0.529885 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.0746734 | 0.169493 | 0.695031 | 0.515295 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.10246 | 0.182058 | 0.707784 | 0.553424 |
