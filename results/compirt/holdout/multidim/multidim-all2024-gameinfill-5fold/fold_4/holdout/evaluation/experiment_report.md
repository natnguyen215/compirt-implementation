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
| auc | 0.891115 |
| log_loss | 0.418661 |
| ece | 0.0260805 |
| brier | 0.133346 |
| part_accuracy | 0.810137 |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.284582 |
| part_accuracy_macro_team | 0.814245 |
| part_accuracy_macro_bonus | 0.801593 |

### Part Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.327596 |
| probability_p10 | 0.0853943 |
| probability_p50 | 0.467923 |
| probability_p90 | 0.933284 |
| mean_predictive_variance | 0.142681 |

### Bonus-Level Score (0/10/20/30 totals and PPB)

| metric | value |
| --- | --- |
| exact_acc | 0.514498 |
| ranked_probability_score | 0.117458 |
| bonus_total_score_log_loss | 1.02381 |
| ppb_mae | 2.32011 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.799569 |
| match_winner_brier | 0.142561 |
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
| bonus_part_correctness | aggregate | all | 25866 | 0.0260805 | 0.133346 | 0.891115 | 0.418661 |
| bonus_part_correctness | tier | fall | 8259 | 0.0315298 | 0.133278 | 0.887172 | 0.417843 |
| bonus_part_correctness | tier | nationals | 4167 | 0.0228154 | 0.142042 | 0.873063 | 0.444235 |
| bonus_part_correctness | tier | regionals | 5457 | 0.0272306 | 0.13288 | 0.890994 | 0.418644 |
| bonus_part_correctness | tier | winter | 7983 | 0.0245893 | 0.129197 | 0.897761 | 0.406169 |
| bonus_part_correctness | category | Current Events | 258 | 0.0693102 | 0.145038 | 0.87988 | 0.450476 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.0274748 | 0.137436 | 0.883999 | 0.43053 |
| bonus_part_correctness | category | Geography | 450 | 0.03933 | 0.130659 | 0.889069 | 0.413326 |
| bonus_part_correctness | category | History | 4116 | 0.0329765 | 0.132167 | 0.893265 | 0.413693 |
| bonus_part_correctness | category | Literature | 4092 | 0.0253779 | 0.131497 | 0.89186 | 0.414889 |
| bonus_part_correctness | category | Mythology | 951 | 0.0676894 | 0.141333 | 0.875795 | 0.436094 |
| bonus_part_correctness | category | Other Academic | 276 | 0.0423818 | 0.117876 | 0.915151 | 0.376029 |
| bonus_part_correctness | category | Philosophy | 957 | 0.0352995 | 0.140791 | 0.879963 | 0.436387 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.0677009 | 0.132113 | 0.891845 | 0.410377 |
| bonus_part_correctness | category | Religion | 1029 | 0.050888 | 0.125818 | 0.903569 | 0.397608 |
| bonus_part_correctness | category | Science | 4089 | 0.0230869 | 0.135926 | 0.886109 | 0.425942 |
| bonus_part_correctness | category | Social Science | 891 | 0.037177 | 0.119891 | 0.908571 | 0.381792 |
| bonus_part_correctness | category | Unknown | 5457 | 0.0272306 | 0.13288 | 0.890994 | 0.418644 |
