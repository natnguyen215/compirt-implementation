# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.625247 |
| log_loss | 0.819321 |
| ece | 0.220132 |
| brier | 0.261846 |
| accuracy | 0.619423 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.144755 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.291752 |
| probability_p10 | 0.102781 |
| probability_p50 | 0.618182 |
| probability_p90 | 0.908259 |
| mean_predictive_variance | 0.161437 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0958602 |
| joint_tossup_event_log_loss | 6.77617 |
| buzz_position_mae | 0.145638 |
| buzz_position_median_absolute_error | 0.125505 |
| buzz_position_bias | -0.0385668 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.395809 |
| first_buzzer_mean_reciprocal_rank | 0.603629 |
| first_buzzer_log_loss | 1.59788 |
| first_buzzer_events | 9257 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9257 | -0.0385668 | -0.0545037 |
| Q1 (0-.2) | 183 | 0.357299 | 0.361656 |
| Q2 (.2-.4) | 955 | 0.193865 | 0.188781 |
| Q3 (.4-.6) | 2239 | 0.0599358 | 0.0573158 |
| Q4 (.6-.8) | 2875 | -0.0595719 | -0.0587014 |
| Q5 (.8-1) | 3005 | -0.189839 | -0.180961 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.894051 |
| log_loss | 0.414519 |
| ece | 0.0328488 |
| brier | 0.132156 |
| part_accuracy | 0.81195 |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.292583 |
| part_accuracy_macro_team | 0.81624 |
| part_accuracy_macro_bonus | 0.808329 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.340723 |
| probability_p10 | 0.0608722 |
| probability_p50 | 0.453559 |
| probability_p90 | 0.946469 |
| mean_predictive_variance | 0.133726 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.523787 |
| ranked_probability_score | 0.112259 |
| bonus_total_score_log_loss | 0.992657 |
| ppb_mae | 1.87625 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.801296 |
| match_winner_brier | 0.138423 |
| match_games | 463 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.220132 | 0.261846 | 0.625247 | 0.819321 |
| tossup_correctness | tier | fall | 2798 | 0.241171 | 0.261778 | 0.642351 | 0.830272 |
| tossup_correctness | tier | nationals | 1545 | 0.193128 | 0.258927 | 0.610675 | 0.773007 |
| tossup_correctness | tier | regionals | 2039 | 0.219741 | 0.263018 | 0.620758 | 0.841413 |
| tossup_correctness | tier | winter | 2875 | 0.223858 | 0.262649 | 0.627366 | 0.817884 |
| tossup_correctness | category | Current Events | 129 | 0.267636 | 0.29321 | 0.585992 | 0.881871 |
| tossup_correctness | category | Fine Arts | 1074 | 0.264942 | 0.285786 | 0.605496 | 0.887447 |
| tossup_correctness | category | Geography | 180 | 0.191961 | 0.280547 | 0.596553 | 0.817306 |
| tossup_correctness | category | History | 1454 | 0.206793 | 0.25038 | 0.640517 | 0.777552 |
| tossup_correctness | category | Literature | 1435 | 0.232295 | 0.254632 | 0.59648 | 0.808058 |
| tossup_correctness | category | Mythology | 324 | 0.259688 | 0.271505 | 0.629073 | 0.898282 |
| tossup_correctness | category | Other Academic | 71 | 0.24038 | 0.26699 | 0.591503 | 0.782372 |
| tossup_correctness | category | Philosophy | 310 | 0.229949 | 0.251752 | 0.686441 | 0.75461 |
| tossup_correctness | category | Popular Culture | 108 | 0.423695 | 0.332172 | 0.543403 | 1.00951 |
| tossup_correctness | category | Religion | 361 | 0.242481 | 0.267367 | 0.645723 | 0.800278 |
| tossup_correctness | category | Science | 1445 | 0.192507 | 0.252998 | 0.63693 | 0.794157 |
| tossup_correctness | category | Social Science | 327 | 0.174831 | 0.244529 | 0.66605 | 0.729945 |
| tossup_correctness | category | Unknown | 2039 | 0.219741 | 0.263018 | 0.620758 | 0.841413 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.499743 | 0.431551 | 0.706821 | 1.38879 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.379497 | 0.356423 | 0.658179 | 1.11473 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.269225 | 0.281213 | 0.657119 | 0.880983 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.200398 | 0.241095 | 0.630184 | 0.750392 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.149768 | 0.226877 | 0.598003 | 0.710762 |
| bonus_part_correctness | aggregate | all | 25791 | 0.0328488 | 0.132156 | 0.894051 | 0.414519 |
| bonus_part_correctness | tier | fall | 7995 | 0.0279125 | 0.126857 | 0.898406 | 0.398571 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0592254 | 0.139729 | 0.885145 | 0.435192 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0413799 | 0.136046 | 0.887965 | 0.426762 |
| bonus_part_correctness | tier | winter | 8121 | 0.0218748 | 0.13088 | 0.894557 | 0.411384 |
| bonus_part_correctness | category | Current Events | 216 | 0.0609379 | 0.127763 | 0.89393 | 0.406968 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0405187 | 0.142818 | 0.879731 | 0.440237 |
| bonus_part_correctness | category | Geography | 501 | 0.028209 | 0.130332 | 0.893093 | 0.40811 |
| bonus_part_correctness | category | History | 4068 | 0.0365377 | 0.130549 | 0.896934 | 0.408876 |
| bonus_part_correctness | category | Literature | 4065 | 0.025896 | 0.123663 | 0.904492 | 0.39294 |
| bonus_part_correctness | category | Mythology | 945 | 0.03616 | 0.14877 | 0.861576 | 0.454375 |
| bonus_part_correctness | category | Other Academic | 219 | 0.068308 | 0.15576 | 0.865199 | 0.473258 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0334547 | 0.130277 | 0.897773 | 0.408382 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.050781 | 0.159902 | 0.840432 | 0.485779 |
| bonus_part_correctness | category | Religion | 1008 | 0.0425996 | 0.129408 | 0.90089 | 0.404088 |
| bonus_part_correctness | category | Science | 4059 | 0.0364681 | 0.128902 | 0.898539 | 0.407531 |
| bonus_part_correctness | category | Social Science | 909 | 0.0331132 | 0.108469 | 0.922267 | 0.353537 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0413799 | 0.136046 | 0.887965 | 0.426762 |
