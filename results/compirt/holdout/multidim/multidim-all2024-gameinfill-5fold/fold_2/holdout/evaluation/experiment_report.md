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
| auc | 0.886487 |
| log_loss | 0.425455 |
| ece | 0.0195432 |
| brier | 0.135467 |
| part_accuracy | 0.805591 |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.286224 |
| part_accuracy_macro_team | 0.809463 |
| part_accuracy_macro_bonus | 0.805242 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.327566 |
| probability_p10 | 0.0839819 |
| probability_p50 | 0.471457 |
| probability_p90 | 0.930889 |
| mean_predictive_variance | 0.1427 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.507619 |
| ranked_probability_score | 0.116623 |
| bonus_total_score_log_loss | 1.02168 |
| ppb_mae | 2.35346 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.794816 |
| match_winner_brier | 0.138166 |
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
| bonus_part_correctness | aggregate | all | 25791 | 0.0195432 | 0.135467 | 0.886487 | 0.425455 |
| bonus_part_correctness | tier | fall | 7995 | 0.0269922 | 0.132035 | 0.890759 | 0.413856 |
| bonus_part_correctness | tier | nationals | 4095 | 0.0196262 | 0.141057 | 0.872265 | 0.442747 |
| bonus_part_correctness | tier | regionals | 5580 | 0.0294731 | 0.136546 | 0.884124 | 0.428856 |
| bonus_part_correctness | tier | winter | 8121 | 0.0189134 | 0.135285 | 0.885404 | 0.425818 |
| bonus_part_correctness | category | Current Events | 216 | 0.0700572 | 0.124529 | 0.893069 | 0.406085 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.0341634 | 0.147129 | 0.869944 | 0.454153 |
| bonus_part_correctness | category | Geography | 501 | 0.0545255 | 0.131949 | 0.890944 | 0.417567 |
| bonus_part_correctness | category | History | 4068 | 0.0264657 | 0.133228 | 0.890231 | 0.418974 |
| bonus_part_correctness | category | Literature | 4065 | 0.0271057 | 0.128854 | 0.89443 | 0.409849 |
| bonus_part_correctness | category | Mythology | 945 | 0.0332554 | 0.153014 | 0.850804 | 0.468861 |
| bonus_part_correctness | category | Other Academic | 219 | 0.0878748 | 0.157921 | 0.862863 | 0.476279 |
| bonus_part_correctness | category | Philosophy | 963 | 0.0239977 | 0.142393 | 0.874073 | 0.443703 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.0581824 | 0.153039 | 0.850051 | 0.463452 |
| bonus_part_correctness | category | Religion | 1008 | 0.0402483 | 0.136428 | 0.887559 | 0.424793 |
| bonus_part_correctness | category | Science | 4059 | 0.0300634 | 0.132544 | 0.891021 | 0.419025 |
| bonus_part_correctness | category | Social Science | 909 | 0.0457099 | 0.110299 | 0.918987 | 0.359257 |
| bonus_part_correctness | category | Unknown | 5580 | 0.0294731 | 0.136546 | 0.884124 | 0.428856 |
