# CompIRT Experiment Report

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.700393 |
| log_loss | 0.573395 |
| ece | 0.130664 |
| brier | 0.191409 |
| accuracy | 0.716847 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | -0.0504237 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.252523 |
| probability_p10 | 0.245086 |
| probability_p50 | 0.704809 |
| probability_p90 | 0.926538 |
| mean_predictive_variance | 0.165552 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0867061 |
| joint_tossup_event_log_loss | 6.11618 |
| buzz_position_mae | 0.134574 |
| buzz_position_median_absolute_error | 0.11554 |
| buzz_position_bias | -0.0302251 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.477647 |
| first_buzzer_mean_reciprocal_rank | 0.667782 |
| first_buzzer_log_loss | 1.36117 |
| first_buzzer_events | 47914 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 47914 | -0.0302251 | -0.0463086 |
| Q1 (0-.2) | 943 | 0.338508 | 0.341074 |
| Q2 (.2-.4) | 4869 | 0.194123 | 0.188057 |
| Q3 (.4-.6) | 11467 | 0.064071 | 0.0601305 |
| Q4 (.6-.8) | 15035 | -0.050435 | -0.0494119 |
| Q5 (.8-1) | 15600 | -0.172373 | -0.16577 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.924131 |
| log_loss | 0.358455 |
| ece | 0.0366069 |
| brier | 0.111821 |
| part_accuracy | 0.843295 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.322806 |
| part_accuracy_macro_team | 0.845959 |
| part_accuracy_macro_game | 0.843711 |
| part_accuracy_macro_bonus | 0.851473 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.338338 |
| probability_p10 | 0.0757429 |
| probability_p50 | 0.474651 |
| probability_p90 | 0.95255 |
| mean_predictive_variance | 0.135477 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.590217 |
| ranked_probability_score | 0.102047 |
| bonus_total_score_log_loss | 0.900859 |
| ppb_mae | 1.97857 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.806144 |
| match_winner_brier | 0.130001 |
| match_games | 2409 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.130664 | 0.191409 | 0.700393 | 0.573395 |
| tossup_correctness | tier | fall | 14760 | 0.138184 | 0.183068 | 0.709766 | 0.550494 |
| tossup_correctness | tier | nationals | 7940 | 0.103321 | 0.200601 | 0.681576 | 0.59896 |
| tossup_correctness | tier | regionals | 10202 | 0.130243 | 0.195191 | 0.696916 | 0.587214 |
| tossup_correctness | tier | winter | 15012 | 0.146072 | 0.192178 | 0.710562 | 0.573 |
| tossup_correctness | category | Current Events | 640 | 0.149833 | 0.216164 | 0.667885 | 0.632752 |
| tossup_correctness | category | Fine Arts | 5640 | 0.130906 | 0.191796 | 0.706464 | 0.570029 |
| tossup_correctness | category | Geography | 972 | 0.126616 | 0.221443 | 0.695818 | 0.636075 |
| tossup_correctness | category | History | 7599 | 0.120783 | 0.180789 | 0.723043 | 0.546216 |
| tossup_correctness | category | Literature | 7469 | 0.140158 | 0.18603 | 0.673561 | 0.563151 |
| tossup_correctness | category | Mythology | 1692 | 0.191896 | 0.198416 | 0.667496 | 0.594701 |
| tossup_correctness | category | Other Academic | 357 | 0.169638 | 0.206225 | 0.689315 | 0.605896 |
| tossup_correctness | category | Philosophy | 1649 | 0.138835 | 0.186425 | 0.716186 | 0.554077 |
| tossup_correctness | category | Popular Culture | 538 | 0.283555 | 0.235957 | 0.591044 | 0.682558 |
| tossup_correctness | category | Religion | 1889 | 0.120802 | 0.198482 | 0.71006 | 0.58871 |
| tossup_correctness | category | Science | 7556 | 0.110863 | 0.188518 | 0.704125 | 0.564972 |
| tossup_correctness | category | Social Science | 1711 | 0.120958 | 0.19764 | 0.707738 | 0.586451 |
| tossup_correctness | category | Unknown | 10202 | 0.130243 | 0.195191 | 0.696916 | 0.587214 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.371424 | 0.322584 | 0.731444 | 0.924429 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.286839 | 0.262255 | 0.735459 | 0.753998 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.195524 | 0.210457 | 0.723392 | 0.617188 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.119634 | 0.171053 | 0.722738 | 0.516647 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.0504597 | 0.166985 | 0.695734 | 0.518309 |
| bonus_part_correctness | aggregate | all | 133461 | 0.0366069 | 0.111821 | 0.924131 | 0.358455 |
| bonus_part_correctness | tier | fall | 42336 | 0.0311541 | 0.116451 | 0.915573 | 0.368531 |
| bonus_part_correctness | tier | nationals | 21051 | 0.0495933 | 0.10326 | 0.934951 | 0.338462 |
| bonus_part_correctness | tier | regionals | 27762 | 0.041087 | 0.108465 | 0.927954 | 0.351064 |
| bonus_part_correctness | tier | winter | 42312 | 0.0337189 | 0.113648 | 0.920502 | 0.36317 |
| bonus_part_correctness | category | Current Events | 1281 | 0.0462475 | 0.101987 | 0.935333 | 0.336004 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.034454 | 0.119582 | 0.913117 | 0.38018 |
| bonus_part_correctness | category | Geography | 2427 | 0.0456503 | 0.113131 | 0.921213 | 0.360222 |
| bonus_part_correctness | category | History | 21273 | 0.035141 | 0.112033 | 0.923957 | 0.357818 |
| bonus_part_correctness | category | Literature | 21312 | 0.0417541 | 0.108892 | 0.927422 | 0.35099 |
| bonus_part_correctness | category | Mythology | 4923 | 0.0344285 | 0.124042 | 0.903117 | 0.387528 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.0493893 | 0.0931521 | 0.947289 | 0.307169 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.0419946 | 0.120071 | 0.912372 | 0.382422 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.0354932 | 0.117988 | 0.912098 | 0.370849 |
| bonus_part_correctness | category | Religion | 5280 | 0.0334325 | 0.109983 | 0.927186 | 0.352081 |
| bonus_part_correctness | category | Science | 21183 | 0.0343895 | 0.11201 | 0.923494 | 0.358848 |
| bonus_part_correctness | category | Social Science | 4698 | 0.0339186 | 0.103008 | 0.933918 | 0.331609 |
| bonus_part_correctness | category | Unknown | 27762 | 0.041087 | 0.108465 | 0.927954 | 0.351064 |
