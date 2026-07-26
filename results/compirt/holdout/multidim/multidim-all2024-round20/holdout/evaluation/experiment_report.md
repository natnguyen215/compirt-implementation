# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.691036 |
| log_loss | 0.596193 |
| ece | 0.133886 |
| brier | 0.200237 |
| accuracy | 0.70701 |
| all_correct_accuracy | 0.754791 |
| accuracy_lift_over_all_correct | -0.0477816 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.249098 |
| probability_p10 | 0.235105 |
| probability_p50 | 0.68194 |
| probability_p90 | 0.910628 |
| mean_predictive_variance | 0.172049 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0809954 |
| joint_tossup_event_log_loss | 6.10918 |
| buzz_position_mae | 0.129597 |
| buzz_position_median_absolute_error | 0.109263 |
| buzz_position_bias | -0.0479821 |
| survival_events | 7740 |
| joint_tossup_event_log_loss_events | 7740 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.490024 |
| first_buzzer_mean_reciprocal_rank | 0.677516 |
| first_buzzer_log_loss | 1.35285 |
| first_buzzer_events | 7618 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 7618 | -0.0479821 | -0.0567994 |
| Q1 (0-.2) | 125 | 0.285846 | 0.268524 |
| Q2 (.2-.4) | 769 | 0.160893 | 0.155704 |
| Q3 (.4-.6) | 1822 | 0.0391632 | 0.0344518 |
| Q4 (.6-.8) | 2322 | -0.0574331 | -0.0536443 |
| Q5 (.8-1) | 2580 | -0.17945 | -0.174396 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.939166 |
| log_loss | 0.362611 |
| ece | 0.0919266 |
| brier | 0.108595 |
| part_accuracy | 0.86197 |
| part_all_correct_accuracy | 0.509829 |
| accuracy_lift_over_all_correct | 0.352141 |
| part_accuracy_macro_team | 0.869828 |
| part_accuracy_macro_game | 0.86287 |
| part_accuracy_macro_bonus | 0.896265 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.300408 |
| probability_p10 | 0.09226 |
| probability_p50 | 0.450159 |
| probability_p90 | 0.885743 |
| mean_predictive_variance | 0.159166 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.635526 |
| ranked_probability_score | 0.0993972 |
| bonus_total_score_log_loss | 0.892599 |
| ppb_mae | 2.45854 |
| ranked_probability_score_responses | 7054 |
| bonus_total_score_log_loss_responses | 7054 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.744792 |
| match_winner_brier | 0.163109 |
| match_games | 384 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 7618 | 0.133886 | 0.200237 | 0.691036 | 0.596193 |
| tossup_correctness | tier | fall | 2044 | 0.159288 | 0.204428 | 0.688582 | 0.604007 |
| tossup_correctness | tier | nationals | 1870 | 0.110468 | 0.217795 | 0.65859 | 0.643291 |
| tossup_correctness | tier | regionals | 1376 | 0.123589 | 0.181342 | 0.727185 | 0.546883 |
| tossup_correctness | tier | winter | 2328 | 0.162051 | 0.19362 | 0.71947 | 0.580645 |
| tossup_correctness | category | Current Events | 95 | 0.193034 | 0.219976 | 0.647715 | 0.630094 |
| tossup_correctness | category | Fine Arts | 936 | 0.165827 | 0.209083 | 0.685671 | 0.619078 |
| tossup_correctness | category | Geography | 182 | 0.128629 | 0.248373 | 0.639031 | 0.695349 |
| tossup_correctness | category | History | 1258 | 0.137405 | 0.214777 | 0.657603 | 0.636513 |
| tossup_correctness | category | Literature | 1229 | 0.131428 | 0.190012 | 0.692454 | 0.573148 |
| tossup_correctness | category | Mythology | 269 | 0.219128 | 0.202232 | 0.662831 | 0.601796 |
| tossup_correctness | category | Other Academic | 75 | 0.187369 | 0.232933 | 0.583686 | 0.694079 |
| tossup_correctness | category | Philosophy | 257 | 0.139065 | 0.208433 | 0.665344 | 0.619557 |
| tossup_correctness | category | Popular Culture | 73 | 0.329785 | 0.269316 | 0.640762 | 0.77683 |
| tossup_correctness | category | Religion | 314 | 0.120118 | 0.191399 | 0.725397 | 0.566584 |
| tossup_correctness | category | Science | 1252 | 0.109677 | 0.196341 | 0.703939 | 0.587487 |
| tossup_correctness | category | Social Science | 302 | 0.156256 | 0.196496 | 0.714956 | 0.57937 |
| tossup_correctness | category | Unknown | 1376 | 0.123589 | 0.181342 | 0.727185 | 0.546883 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 125 | 0.309199 | 0.286589 | 0.715366 | 0.802629 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 769 | 0.288615 | 0.262748 | 0.745946 | 0.753157 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 1822 | 0.204327 | 0.220032 | 0.697293 | 0.648229 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2322 | 0.109272 | 0.181753 | 0.714774 | 0.544207 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2580 | 0.0626942 | 0.180077 | 0.677748 | 0.549446 |
| bonus_part_correctness | aggregate | all | 21162 | 0.0919266 | 0.108595 | 0.939166 | 0.362611 |
| bonus_part_correctness | tier | fall | 5877 | 0.104208 | 0.114221 | 0.93431 | 0.37918 |
| bonus_part_correctness | tier | nationals | 4923 | 0.0477514 | 0.104302 | 0.93216 | 0.34115 |
| bonus_part_correctness | tier | regionals | 3873 | 0.106529 | 0.103952 | 0.946598 | 0.35406 |
| bonus_part_correctness | tier | winter | 6489 | 0.105602 | 0.109528 | 0.941453 | 0.368989 |
| bonus_part_correctness | category | Current Events | 189 | 0.13084 | 0.0955317 | 0.960826 | 0.335763 |
| bonus_part_correctness | category | Fine Arts | 2508 | 0.0890654 | 0.119106 | 0.926095 | 0.388283 |
| bonus_part_correctness | category | Geography | 363 | 0.113917 | 0.111844 | 0.939259 | 0.372776 |
| bonus_part_correctness | category | History | 3456 | 0.0911041 | 0.112292 | 0.936926 | 0.370735 |
| bonus_part_correctness | category | Literature | 3555 | 0.0931533 | 0.105644 | 0.941703 | 0.355291 |
| bonus_part_correctness | category | Mythology | 777 | 0.100736 | 0.116536 | 0.927652 | 0.387481 |
| bonus_part_correctness | category | Other Academic | 249 | 0.0880576 | 0.0857767 | 0.962186 | 0.294263 |
| bonus_part_correctness | category | Philosophy | 858 | 0.0795296 | 0.102158 | 0.943009 | 0.342949 |
| bonus_part_correctness | category | Popular Culture | 204 | 0.101544 | 0.100231 | 0.947079 | 0.332522 |
| bonus_part_correctness | category | Religion | 870 | 0.0945558 | 0.111604 | 0.934362 | 0.368565 |
| bonus_part_correctness | category | Science | 3468 | 0.0818349 | 0.108612 | 0.936325 | 0.36245 |
| bonus_part_correctness | category | Social Science | 792 | 0.0810286 | 0.101891 | 0.941204 | 0.342583 |
| bonus_part_correctness | category | Unknown | 3873 | 0.106529 | 0.103952 | 0.946598 | 0.35406 |
