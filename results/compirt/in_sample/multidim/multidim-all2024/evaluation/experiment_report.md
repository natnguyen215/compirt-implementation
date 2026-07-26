# CompIRT Experiment Report

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.700325 |
| log_loss | 0.57645 |
| ece | 0.128749 |
| brier | 0.192849 |
| accuracy | 0.715302 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | -0.0519681 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.256321 |
| probability_p10 | 0.237035 |
| probability_p50 | 0.709465 |
| probability_p90 | 0.92861 |
| mean_predictive_variance | 0.163477 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.085288 |
| joint_tossup_event_log_loss | 6.10421 |
| buzz_position_mae | 0.134659 |
| buzz_position_median_absolute_error | 0.115784 |
| buzz_position_bias | -0.0398828 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.47938 |
| first_buzzer_mean_reciprocal_rank | 0.670549 |
| first_buzzer_log_loss | 1.34399 |
| first_buzzer_events | 47914 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 47914 | -0.0398828 | -0.0543883 |
| Q1 (0-.2) | 943 | 0.325893 | 0.324078 |
| Q2 (.2-.4) | 4869 | 0.179411 | 0.172551 |
| Q3 (.4-.6) | 11467 | 0.0524886 | 0.0480506 |
| Q4 (.6-.8) | 15035 | -0.0592733 | -0.0568894 |
| Q5 (.8-1) | 15600 | -0.179649 | -0.173408 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.927123 |
| log_loss | 0.355133 |
| ece | 0.0417817 |
| brier | 0.110096 |
| part_accuracy | 0.845678 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.325189 |
| part_accuracy_macro_team | 0.848976 |
| part_accuracy_macro_bonus | 0.853912 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.336235 |
| probability_p10 | 0.0777476 |
| probability_p50 | 0.471455 |
| probability_p90 | 0.945791 |
| mean_predictive_variance | 0.136928 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.596534 |
| ranked_probability_score | 0.100243 |
| bonus_total_score_log_loss | 0.889913 |
| ppb_mae | 1.83683 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.803238 |
| match_winner_brier | 0.130041 |
| match_games | 2409 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.128749 | 0.192849 | 0.700325 | 0.57645 |
| tossup_correctness | tier | fall | 14760 | 0.143458 | 0.186969 | 0.70572 | 0.561576 |
| tossup_correctness | tier | nationals | 7940 | 0.0904968 | 0.197388 | 0.691216 | 0.58643 |
| tossup_correctness | tier | regionals | 10202 | 0.123581 | 0.194809 | 0.701128 | 0.583724 |
| tossup_correctness | tier | winter | 15012 | 0.145523 | 0.194897 | 0.706701 | 0.580852 |
| tossup_correctness | category | Current Events | 640 | 0.135781 | 0.213773 | 0.668661 | 0.621403 |
| tossup_correctness | category | Fine Arts | 5640 | 0.136787 | 0.194849 | 0.703603 | 0.578562 |
| tossup_correctness | category | Geography | 972 | 0.125307 | 0.232341 | 0.659361 | 0.660724 |
| tossup_correctness | category | History | 7599 | 0.114515 | 0.183856 | 0.715954 | 0.553338 |
| tossup_correctness | category | Literature | 7469 | 0.145958 | 0.187592 | 0.677603 | 0.568442 |
| tossup_correctness | category | Mythology | 1692 | 0.209866 | 0.213939 | 0.652222 | 0.631835 |
| tossup_correctness | category | Other Academic | 357 | 0.154439 | 0.197862 | 0.703448 | 0.586898 |
| tossup_correctness | category | Philosophy | 1649 | 0.13629 | 0.183984 | 0.726333 | 0.547089 |
| tossup_correctness | category | Popular Culture | 538 | 0.308739 | 0.252309 | 0.60545 | 0.737916 |
| tossup_correctness | category | Religion | 1889 | 0.117903 | 0.197633 | 0.715781 | 0.58688 |
| tossup_correctness | category | Science | 7556 | 0.105061 | 0.187062 | 0.705795 | 0.560853 |
| tossup_correctness | category | Social Science | 1711 | 0.108324 | 0.19541 | 0.723514 | 0.576966 |
| tossup_correctness | category | Unknown | 10202 | 0.123581 | 0.194809 | 0.701128 | 0.583724 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.383773 | 0.327888 | 0.744768 | 0.949603 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.296392 | 0.271254 | 0.728459 | 0.783167 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.185283 | 0.210047 | 0.717273 | 0.617892 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.107127 | 0.172145 | 0.711255 | 0.520188 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.0529966 | 0.167527 | 0.705167 | 0.513135 |
| bonus_part_correctness | aggregate | all | 133461 | 0.0417817 | 0.110096 | 0.927123 | 0.355133 |
| bonus_part_correctness | tier | fall | 42336 | 0.0365563 | 0.114663 | 0.918816 | 0.365041 |
| bonus_part_correctness | tier | nationals | 21051 | 0.0535738 | 0.103536 | 0.935883 | 0.340517 |
| bonus_part_correctness | tier | regionals | 27762 | 0.0480624 | 0.10603 | 0.931857 | 0.345915 |
| bonus_part_correctness | tier | winter | 42312 | 0.0381357 | 0.111457 | 0.924052 | 0.358539 |
| bonus_part_correctness | category | Current Events | 1281 | 0.0495865 | 0.103294 | 0.936379 | 0.338875 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.0386058 | 0.117456 | 0.916734 | 0.375407 |
| bonus_part_correctness | category | Geography | 2427 | 0.0439074 | 0.112283 | 0.922829 | 0.360213 |
| bonus_part_correctness | category | History | 21273 | 0.0408308 | 0.11031 | 0.926954 | 0.354596 |
| bonus_part_correctness | category | Literature | 21312 | 0.0444277 | 0.107454 | 0.929622 | 0.348629 |
| bonus_part_correctness | category | Mythology | 4923 | 0.0393234 | 0.123247 | 0.905508 | 0.386825 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.0498589 | 0.0923895 | 0.947495 | 0.308297 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.0435745 | 0.119582 | 0.914495 | 0.381583 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.0411077 | 0.122089 | 0.907387 | 0.381363 |
| bonus_part_correctness | category | Religion | 5280 | 0.041302 | 0.108263 | 0.92939 | 0.348663 |
| bonus_part_correctness | category | Science | 21183 | 0.0402561 | 0.109884 | 0.927244 | 0.35436 |
| bonus_part_correctness | category | Social Science | 4698 | 0.0431219 | 0.101567 | 0.936352 | 0.329912 |
| bonus_part_correctness | category | Unknown | 27762 | 0.0480624 | 0.10603 | 0.931857 | 0.345915 |
