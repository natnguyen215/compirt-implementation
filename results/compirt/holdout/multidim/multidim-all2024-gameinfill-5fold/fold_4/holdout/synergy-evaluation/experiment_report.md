# CompIRT Experiment Report

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.635744 |
| log_loss | 0.832833 |
| ece | 0.226928 |
| brier | 0.261801 |
| accuracy | 0.623517 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.149838 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.297878 |
| probability_p10 | 0.0894543 |
| probability_p50 | 0.613305 |
| probability_p90 | 0.913538 |
| mean_predictive_variance | 0.158042 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.0950408 |
| joint_tossup_event_log_loss | 6.82337 |
| buzz_position_mae | 0.145527 |
| buzz_position_median_absolute_error | 0.127177 |
| buzz_position_bias | -0.040406 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.395146 |
| first_buzzer_mean_reciprocal_rank | 0.601402 |
| first_buzzer_log_loss | 1.62485 |
| first_buzzer_events | 9270 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9270 | -0.040406 | -0.0536425 |
| Q1 (0-.2) | 179 | 0.339922 | 0.336356 |
| Q2 (.2-.4) | 957 | 0.195917 | 0.1872 |
| Q3 (.4-.6) | 2203 | 0.05941 | 0.0543767 |
| Q4 (.6-.8) | 2978 | -0.0622029 | -0.0572055 |
| Q5 (.8-1) | 2953 | -0.19253 | -0.184963 |

## Stage 2: Bonus Metrics

### Part-Level Correctness

| metric | value |
| --- | --- |
| auc | 0.897278 |
| log_loss | 0.409088 |
| ece | 0.034084 |
| brier | 0.130176 |
| part_accuracy | 0.816052 |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.290497 |
| part_accuracy_macro_team | 0.822032 |
| part_accuracy_macro_bonus | 0.808825 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.340047 |
| probability_p10 | 0.0635756 |
| probability_p50 | 0.460282 |
| probability_p90 | 0.949424 |
| mean_predictive_variance | 0.134295 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.529344 |
| ranked_probability_score | 0.113478 |
| bonus_total_score_log_loss | 1.00004 |
| ppb_mae | 1.85769 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.806034 |
| match_winner_brier | 0.139216 |
| match_games | 464 |
| match_simulations_per_game | 500 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.226928 | 0.261801 | 0.635744 | 0.832833 |
| tossup_correctness | tier | fall | 2876 | 0.245352 | 0.259173 | 0.639197 | 0.825186 |
| tossup_correctness | tier | nationals | 1579 | 0.176365 | 0.252036 | 0.636819 | 0.773812 |
| tossup_correctness | tier | regionals | 1990 | 0.223428 | 0.263734 | 0.639241 | 0.85357 |
| tossup_correctness | tier | winter | 2825 | 0.244468 | 0.268572 | 0.635319 | 0.858998 |
| tossup_correctness | category | Current Events | 123 | 0.257172 | 0.261576 | 0.665811 | 0.782202 |
| tossup_correctness | category | Fine Arts | 1093 | 0.229514 | 0.267973 | 0.640885 | 0.858877 |
| tossup_correctness | category | Geography | 191 | 0.239772 | 0.305957 | 0.563559 | 0.912076 |
| tossup_correctness | category | History | 1469 | 0.196921 | 0.24319 | 0.658989 | 0.754552 |
| tossup_correctness | category | Literature | 1436 | 0.253441 | 0.259368 | 0.624775 | 0.848689 |
| tossup_correctness | category | Mythology | 325 | 0.334144 | 0.307822 | 0.520896 | 1.00186 |
| tossup_correctness | category | Other Academic | 67 | 0.283644 | 0.280805 | 0.644205 | 0.87095 |
| tossup_correctness | category | Philosophy | 322 | 0.237351 | 0.256981 | 0.666609 | 0.78454 |
| tossup_correctness | category | Popular Culture | 100 | 0.366562 | 0.299323 | 0.53524 | 0.938479 |
| tossup_correctness | category | Religion | 365 | 0.223183 | 0.249822 | 0.665092 | 0.768807 |
| tossup_correctness | category | Science | 1456 | 0.221476 | 0.262784 | 0.615223 | 0.838068 |
| tossup_correctness | category | Social Science | 333 | 0.215664 | 0.250818 | 0.679012 | 0.763249 |
| tossup_correctness | category | Unknown | 1990 | 0.223428 | 0.263734 | 0.639241 | 0.85357 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.508553 | 0.443521 | 0.706302 | 1.42672 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.411394 | 0.372858 | 0.65773 | 1.19019 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.291934 | 0.288219 | 0.66316 | 0.92448 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.195902 | 0.235429 | 0.649067 | 0.731584 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.145586 | 0.221681 | 0.620591 | 0.714756 |
| bonus_part_correctness | aggregate | all | 25866 | 0.034084 | 0.130176 | 0.897278 | 0.409088 |
| bonus_part_correctness | tier | fall | 8259 | 0.0296231 | 0.129306 | 0.893838 | 0.405634 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0564176 | 0.139743 | 0.882817 | 0.439142 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0465689 | 0.12929 | 0.900912 | 0.407211 |
| bonus_part_correctness | tier | winter | 7983 | 0.018981 | 0.126688 | 0.901263 | 0.398257 |
| bonus_part_correctness | category | Current Events | 258 | 0.0722877 | 0.150187 | 0.869233 | 0.468759 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0290987 | 0.130413 | 0.895083 | 0.411628 |
| bonus_part_correctness | category | Geography | 450 | 0.0307382 | 0.125753 | 0.898287 | 0.394768 |
| bonus_part_correctness | category | History | 4116 | 0.0345718 | 0.13066 | 0.895686 | 0.410118 |
| bonus_part_correctness | category | Literature | 4092 | 0.0323443 | 0.12749 | 0.901004 | 0.400755 |
| bonus_part_correctness | category | Mythology | 951 | 0.067167 | 0.140351 | 0.8764 | 0.434444 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0476716 | 0.128722 | 0.90144 | 0.402226 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0264822 | 0.12962 | 0.896568 | 0.405955 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0543912 | 0.142994 | 0.870975 | 0.434318 |
| bonus_part_correctness | category | Religion | 1029 | 0.0290368 | 0.127638 | 0.900615 | 0.40134 |
| bonus_part_correctness | category | Science | 4089 | 0.0288 | 0.132814 | 0.891812 | 0.417536 |
| bonus_part_correctness | category | Social Science | 891 | 0.0378993 | 0.118041 | 0.912704 | 0.3756 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0465689 | 0.12929 | 0.900912 | 0.407211 |
