# CompIRT Tossup Evaluation Report

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Stage 1: Tossup Metrics

### Buzz Correctness (scored on actual first buzzes)

| metric | value |
| --- | --- |
| auc | 0.652626 |
| log_loss | 0.512577 |
| ece | 0.0195255 |
| brier | 0.166337 |
| accuracy | 0.776542 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0064978 |

### Correctness Probability Sharpness

| metric | value |
| --- | --- |
| probability_std | 0.11425 |
| probability_p10 | 0.616472 |
| probability_p50 | 0.7937 |
| probability_p90 | 0.905258 |
| mean_predictive_variance | 0.161891 |

### Buzz Timing (survival replay over all lineup rows)

The survival replay reconstructs each event's probability that someone has buzzed by each relative question position. `integrated_brier_score` measures probability error over that curve (lower is better). `survival_events` is the number of events reconstructed and scored.

| metric | value |
| --- | --- |
| integrated_brier_score | 0.10302 |
| joint_tossup_event_log_loss | 6.89023 |
| buzz_position_mae | 0.161344 |
| buzz_position_median_absolute_error | 0.146133 |
| buzz_position_bias | -0.0692506 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |

### First-Buzzer Identity (who buzzes first)

These metrics use events with an observed buzz and a complete fitted roster. `first_buzzer_top1_accuracy` is the fraction where the model's highest-probability player was the observed first buzzer. `first_buzzer_mean_reciprocal_rank` averages `1 / rank` for the observed buzzer, so ranks 1, 2, and 3 receive 1, 1/2, and 1/3 credit. `first_buzzer_log_loss` averages the negative log probability assigned to the observed buzzer (lower is better), conditional on someone buzzing. `first_buzzer_events` is the shared denominator.

| metric | value |
| --- | --- |
| first_buzzer_top1_accuracy | 0.355066 |
| first_buzzer_mean_reciprocal_rank | 0.566932 |
| first_buzzer_log_loss | 1.67771 |
| first_buzzer_events | 9080 |

### Tossup Ownership, Games, and Tournament PPG (+10/-5 phase 0)

These deterministic Stage-1 metrics use +10 for a correct initial buzz, -5 for an incorrect initial buzz, and zero for no buzz. Bonuses, powers, and bouncebacks are excluded. Game-winner accuracy omits observed tossup-score ties; tournament ranking metrics are macro-averaged.

| metric | value |
| --- | --- |
| first_buzzer_team_top1_accuracy | 0.659361 |
| tossup_scorer_player_top1_accuracy | 0.319848 |
| tossup_scorer_team_top1_accuracy | 0.50705 |
| tossup_game_winner_accuracy | 0.807522 |
| tossup_game_margin_mae | 35.245 |
| tournament_player_ppg_spearman | 0.690548 |
| tournament_player_ppg_mae | 8.94971 |
| tournament_player_ppg_top10_overlap | 0.665517 |

### Other Metrics

| metric | value |
| --- | --- |
| neg_auroc | 0.652626 |
| neg_average_precision | 0.383268 |
| neg_precision | 0.631111 |
| neg_recall | 0.0680077 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0554887 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0953226 |
| no_buzz_calibration_error | 0.0801382 |
| no_buzz_brier | 0.0277423 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9220 |
| first_buzzer_team_top1_accuracy_events | 9080 |
| tossup_scorer_player_top1_accuracy_events | 9220 |
| tossup_scorer_team_top1_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 452 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |

### Buzz-Position Bias

Signed error is predicted minus observed position, so positive rows are predicted too late. Opposite-signed errors early and late in the question can cancel in the overall row; read the bands. Bands bin by observed position, which conditions on the noisy outcome, so band values are upper bounds on structural timing bias.

| band | events | mean_signed_error | median_signed_error |
| --- | --- | --- | --- |
| overall | 9080 | -0.0692506 | -0.0834954 |
| Q1 (0-.2) | 192 | 0.368754 | 0.364218 |
| Q2 (.2-.4) | 889 | 0.200641 | 0.201892 |
| Q3 (.4-.6) | 2210 | 0.0459257 | 0.0488546 |
| Q4 (.6-.8) | 2869 | -0.093074 | -0.0852748 |
| Q5 (.8-1) | 2920 | -0.243984 | -0.241391 |

## Calibration By Stratum

Strata are fixed bands, not equal-count quantiles; read each row against its `observations` count. Sharpness columns stay in `csvs/prediction_diagnostics_by_stratum.csv`.

| scenario | stratum | value | observations | ece | brier | auc | log_loss |
| --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.0195255 | 0.166337 | 0.652626 | 0.512577 |
| tossup_correctness | tier | fall | 2817 | 0.0245284 | 0.16228 | 0.638088 | 0.5045 |
| tossup_correctness | tier | nationals | 1542 | 0.065411 | 0.180365 | 0.701552 | 0.542648 |
| tossup_correctness | tier | regionals | 1934 | 0.0208517 | 0.172814 | 0.658288 | 0.524327 |
| tossup_correctness | tier | winter | 2787 | 0.0226885 | 0.158183 | 0.642844 | 0.495948 |
| tossup_correctness | category | Current Events | 125 | 0.0436669 | 0.194203 | 0.654484 | 0.573403 |
| tossup_correctness | category | Fine Arts | 1072 | 0.0265321 | 0.166335 | 0.653898 | 0.511025 |
| tossup_correctness | category | Geography | 185 | 0.055134 | 0.173752 | 0.761818 | 0.521928 |
| tossup_correctness | category | History | 1443 | 0.0222033 | 0.163259 | 0.685945 | 0.502075 |
| tossup_correctness | category | Literature | 1411 | 0.0552668 | 0.153131 | 0.575162 | 0.491875 |
| tossup_correctness | category | Mythology | 320 | 0.0769425 | 0.161239 | 0.593414 | 0.508686 |
| tossup_correctness | category | Other Academic | 64 | 0.117785 | 0.183274 | 0.597656 | 0.55382 |
| tossup_correctness | category | Philosophy | 312 | 0.0709045 | 0.160003 | 0.57271 | 0.5055 |
| tossup_correctness | category | Popular Culture | 104 | 0.0784542 | 0.139332 | 0.507812 | 0.456852 |
| tossup_correctness | category | Religion | 358 | 0.0452742 | 0.190059 | 0.643603 | 0.568056 |
| tossup_correctness | category | Science | 1431 | 0.0369057 | 0.165669 | 0.671092 | 0.508518 |
| tossup_correctness | category | Social Science | 321 | 0.0170955 | 0.177227 | 0.677212 | 0.532903 |
| tossup_correctness | category | Unknown | 1934 | 0.0208517 | 0.172814 | 0.658288 | 0.524327 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.0494112 | 0.19181 | 0.701621 | 0.566282 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.0181279 | 0.179929 | 0.670478 | 0.542029 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.0204053 | 0.175037 | 0.629707 | 0.534272 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.0188875 | 0.157839 | 0.644194 | 0.492626 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.0306094 | 0.16229 | 0.662096 | 0.50326 |
