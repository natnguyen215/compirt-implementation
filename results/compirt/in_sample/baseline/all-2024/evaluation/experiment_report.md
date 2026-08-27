# CompIRT Experiment Report

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.701385 |
| log_loss | 0.579618 |
| ece | 0.149084 |
| brier | 0.195886 |
| accuracy | 0.705952 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | -0.0613182 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.239614 |
| probability_p10 | 0.249051 |
| probability_p50 | 0.668611 |
| probability_p90 | 0.895095 |
| mean_predictive_variance | 0.178617 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0904948 |
| joint_tossup_event_log_loss | 6.26439 |
| buzz_position_mae | 0.139008 |
| buzz_position_median_absolute_error | 0.121411 |
| buzz_position_bias | -0.0595034 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.489544 |
| first_buzzer_mean_reciprocal_rank | 0.677112 |
| first_buzzer_log_loss | 1.34911 |
| first_buzzer_events | 47914 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.701385 |
| neg_average_precision | 0.42674 |
| neg_precision | 0.395579 |
| neg_recall | 0.499058 |
| full_pmf_events | 48612 |
| full_pmf_final_decile_mass | 0.0763893 |
| no_buzz_observed_rate | 0.0143586 |
| no_buzz_predicted_rate | 0.0808153 |
| no_buzz_calibration_error | 0.0664567 |
| no_buzz_brier | 0.0242857 |
| full_pmf_max_mass_error | 1.33227e-15 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 47914 | -0.0595034 | -0.0753921 |
| Q1 (0-.2) | 943 | 0.297163 | 0.289975 |
| Q2 (.2-.4) | 4869 | 0.155425 | 0.143338 |
| Q3 (.4-.6) | 11467 | 0.0262745 | 0.0202977 |
| Q4 (.6-.8) | 15035 | -0.081436 | -0.0812315 |
| Q5 (.8-1) | 15600 | -0.19006 | -0.182401 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.932678 |
| log_loss | 0.342423 |
| ece | 0.0411874 |
| brier | 0.105804 |
| part_accuracy | 0.852594 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.332105 |
| part_accuracy_macro_team | 0.855296 |
| part_accuracy_macro_bonus | 0.860211 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.342499 |
| probability_p10 | 0.0750338 |
| probability_p50 | 0.475163 |
| probability_p90 | 0.954589 |
| mean_predictive_variance | 0.13266 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.612404 |
| ranked_probability_score | 0.0960612 |
| bonus_total_score_log_loss | 0.859128 |
| ppb_mae | 1.57744 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Match Winner Simulation

Match simulation was unavailable or skipped.

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.149084 | 0.195886 | 0.701385 | 0.579618 |
| tossup_correctness | tier | fall | 14760 | 0.160056 | 0.189981 | 0.70418 | 0.566194 |
| tossup_correctness | tier | nationals | 7940 | 0.104199 | 0.199512 | 0.691545 | 0.585303 |
| tossup_correctness | tier | regionals | 10202 | 0.143029 | 0.195613 | 0.706801 | 0.578042 |
| tossup_correctness | tier | winter | 15012 | 0.166151 | 0.199959 | 0.702001 | 0.59088 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.34074 | 0.296556 | 0.735664 | 0.833925 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.300675 | 0.269245 | 0.730458 | 0.765358 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.202564 | 0.213353 | 0.72231 | 0.623558 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.120945 | 0.173267 | 0.712233 | 0.522379 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.0780034 | 0.175864 | 0.69312 | 0.529139 |
| bonus_part_correctness | aggregate | all | 133461 | 0.0411874 | 0.105804 | 0.932678 | 0.342423 |
| bonus_part_correctness | tier | fall | 42336 | 0.0358022 | 0.109981 | 0.925312 | 0.350685 |
| bonus_part_correctness | tier | nationals | 21051 | 0.0563385 | 0.101884 | 0.937889 | 0.336467 |
| bonus_part_correctness | tier | regionals | 27762 | 0.0487845 | 0.0999127 | 0.939895 | 0.328267 |
| bonus_part_correctness | tier | winter | 42312 | 0.0353003 | 0.107442 | 0.929241 | 0.346407 |
| bonus_part_correctness | category | Current Events | 1281 | 0.0437089 | 0.10238 | 0.93713 | 0.336148 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.0394138 | 0.116206 | 0.918681 | 0.370725 |
| bonus_part_correctness | category | Geography | 2427 | 0.0486974 | 0.107171 | 0.929586 | 0.345408 |
| bonus_part_correctness | category | History | 21273 | 0.0400855 | 0.10563 | 0.932779 | 0.341124 |
| bonus_part_correctness | category | Literature | 21312 | 0.0421659 | 0.101767 | 0.936354 | 0.332222 |
| bonus_part_correctness | category | Mythology | 4923 | 0.0379333 | 0.116681 | 0.915637 | 0.368413 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.0439798 | 0.09427 | 0.946271 | 0.31266 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.0450896 | 0.114741 | 0.920578 | 0.366426 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.0359335 | 0.119966 | 0.910336 | 0.373796 |
| bonus_part_correctness | category | Religion | 5280 | 0.0376049 | 0.105787 | 0.932732 | 0.340589 |
| bonus_part_correctness | category | Science | 21183 | 0.0418371 | 0.10643 | 0.931927 | 0.3439 |
| bonus_part_correctness | category | Social Science | 4698 | 0.0449639 | 0.100386 | 0.938587 | 0.325345 |
| bonus_part_correctness | category | Unknown | 27762 | 0.0487845 | 0.0999127 | 0.939895 | 0.328267 |
