# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-10000-20260913-195429/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-10000-20260913-195429/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 277683 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.712223 |
| log_loss | 0.491092 |
| ece | 0.0112871 |
| brier | 0.159591 |
| accuracy | 0.777622 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.0123722 |
| probability_std | 0.148969 |
| probability_p10 | 0.562611 |
| probability_p50 | 0.810044 |
| probability_p90 | 0.920742 |
| mean_predictive_variance | 0.154274 |
| integrated_brier_score | 0.095789 |
| joint_tossup_event_log_loss | 6.44735 |
| buzz_position_mae | 0.142788 |
| buzz_position_median_absolute_error | 0.122743 |
| buzz_position_bias | -0.0147595 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.379236 |
| first_buzzer_mean_reciprocal_rank | 0.58675 |
| first_buzzer_log_loss | 1.62148 |
| first_buzzer_events | 9295 |
| first_buzzer_player_replay_accuracy | 0.217751 |
| first_buzzer_team_replay_accuracy | 0.473158 |
| tossup_scorer_player_replay_accuracy | 0.23758 |
| tossup_scorer_team_replay_accuracy | 0.446921 |
| tossup_game_winner_accuracy | 0.678492 |
| tossup_model_official_winner_accuracy | 0.709402 |
| tossup_game_margin_mae | 49.5966 |
| tossup_game_zero_margin_mae | 54.8195 |
| tournament_player_ppg_spearman | 0.595601 |
| tournament_player_ppg_mae | 12.411 |
| tournament_player_ppg_top10_overlap | 0.610345 |
| tournament_player_ppg_top10_random_overlap | 0.282327 |
| tournament_player_ppg_top10_adjusted_overlap | 0.455188 |
| neg_auroc | 0.712223 |
| neg_average_precision | 0.44716 |
| neg_precision | 0.594417 |
| neg_recall | 0.165903 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.174105 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0227762 |
| no_buzz_calibration_error | 0.00950653 |
| no_buzz_brier | 0.0143201 |
| full_pmf_max_mass_error | 6.66134e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9420 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 468 |
| first_buzzer_player_replay_accuracy_events | 9295 |
| first_buzzer_team_replay_accuracy_events | 9295 |
| tossup_scorer_player_replay_accuracy_events | 9420 |
| tossup_scorer_team_replay_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 451 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.678492 |
| tossup_game_margin_mae | 49.5966 |
| tossup_game_zero_margin_mae | 54.8195 |
| tossup_game_margin_mae_games | 471 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 451 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.712223 | 0.491092 | 0.0112871 | 0.159591 | 0.777622 | 0.76525 | 0.0123722 | 0.148969 | 0.562611 | 0.810044 | 0.920742 | 0.154274 |
| tossup_correctness | tier | fall | 2933 | 0.712337 | 0.462657 | 0.0161002 | 0.148101 | 0.799182 | 0.791681 | 0.00750085 | 0.145903 | 0.564092 | 0.815772 | 0.923279 | 0.152495 |
| tossup_correctness | tier | nationals | 1584 | 0.699581 | 0.53867 | 0.0348592 | 0.178016 | 0.75 | 0.724747 | 0.0252525 | 0.16335 | 0.51699 | 0.806422 | 0.917707 | 0.157269 |
| tossup_correctness | tier | regionals | 1886 | 0.709153 | 0.515167 | 0.0256069 | 0.170229 | 0.756628 | 0.746023 | 0.0106045 | 0.144577 | 0.566572 | 0.796725 | 0.915873 | 0.159492 |
| tossup_correctness | tier | winter | 2892 | 0.7188 | 0.478169 | 0.0157628 | 0.154213 | 0.784578 | 0.773167 | 0.0114108 | 0.145818 | 0.581428 | 0.815569 | 0.922909 | 0.151034 |
| tossup_correctness | category | Current Events | 124 | 0.688172 | 0.516067 | 0.082566 | 0.16711 | 0.790323 | 0.75 | 0.0403226 | 0.161619 | 0.501097 | 0.755158 | 0.920008 | 0.169496 |
| tossup_correctness | category | Fine Arts | 1103 | 0.708677 | 0.496802 | 0.0193591 | 0.160851 | 0.780598 | 0.759746 | 0.0208522 | 0.152366 | 0.576169 | 0.81881 | 0.922753 | 0.151769 |
| tossup_correctness | category | Geography | 197 | 0.793124 | 0.511202 | 0.0668304 | 0.1691 | 0.751269 | 0.670051 | 0.0812183 | 0.217296 | 0.379376 | 0.742369 | 0.911651 | 0.167698 |
| tossup_correctness | category | History | 1491 | 0.716569 | 0.465592 | 0.0178042 | 0.149787 | 0.791415 | 0.787391 | 0.00402414 | 0.139446 | 0.574729 | 0.809757 | 0.919049 | 0.15505 |
| tossup_correctness | category | Literature | 1472 | 0.729478 | 0.436176 | 0.0283998 | 0.137028 | 0.816576 | 0.804348 | 0.0122283 | 0.127249 | 0.632104 | 0.844699 | 0.929445 | 0.138144 |
| tossup_correctness | category | Mythology | 332 | 0.692234 | 0.450939 | 0.0316411 | 0.142566 | 0.810241 | 0.813253 | -0.00301205 | 0.120338 | 0.636022 | 0.827268 | 0.915763 | 0.147073 |
| tossup_correctness | category | Other Academic | 69 | 0.704751 | 0.513179 | 0.160739 | 0.171398 | 0.73913 | 0.753623 | -0.0144928 | 0.118371 | 0.621869 | 0.79359 | 0.894168 | 0.162255 |
| tossup_correctness | category | Philosophy | 324 | 0.676626 | 0.470753 | 0.0387035 | 0.150427 | 0.799383 | 0.799383 | 0 | 0.12993 | 0.600024 | 0.818808 | 0.920411 | 0.152052 |
| tossup_correctness | category | Popular Culture | 102 | 0.440138 | 0.488305 | 0.0695989 | 0.14948 | 0.823529 | 0.833333 | -0.00980392 | 0.0834127 | 0.723089 | 0.845696 | 0.916445 | 0.133374 |
| tossup_correctness | category | Religion | 372 | 0.713033 | 0.548079 | 0.0383207 | 0.185265 | 0.717742 | 0.709677 | 0.00806452 | 0.155392 | 0.518156 | 0.767966 | 0.908576 | 0.169712 |
| tossup_correctness | category | Science | 1487 | 0.682612 | 0.519737 | 0.0319652 | 0.170903 | 0.761937 | 0.752522 | 0.00941493 | 0.159447 | 0.52091 | 0.7997 | 0.919565 | 0.158878 |
| tossup_correctness | category | Social Science | 336 | 0.728517 | 0.535666 | 0.0315527 | 0.177552 | 0.741071 | 0.702381 | 0.0386905 | 0.183496 | 0.4541 | 0.786278 | 0.917677 | 0.163429 |
| tossup_correctness | category | Unknown | 1886 | 0.709153 | 0.515167 | 0.0256069 | 0.170229 | 0.756628 | 0.746023 | 0.0106045 | 0.144577 | 0.566572 | 0.796725 | 0.915873 | 0.159492 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.692971 | 0.51953 | 0.0736454 | 0.168644 | 0.771574 | 0.736041 | 0.035533 | 0.150781 | 0.513024 | 0.756823 | 0.883874 | 0.175974 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.719613 | 0.518147 | 0.0278059 | 0.171758 | 0.754315 | 0.735025 | 0.0192893 | 0.149976 | 0.539901 | 0.791978 | 0.913052 | 0.161835 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.693233 | 0.49909 | 0.0207973 | 0.162115 | 0.770324 | 0.769436 | 0.000888494 | 0.145204 | 0.579934 | 0.811711 | 0.922619 | 0.152014 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.698653 | 0.478147 | 0.0132908 | 0.154029 | 0.7903 | 0.78402 | 0.00628053 | 0.142542 | 0.588945 | 0.82343 | 0.92625 | 0.148625 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.734383 | 0.4867 | 0.0128142 | 0.158419 | 0.779039 | 0.756008 | 0.0230307 | 0.155498 | 0.528496 | 0.804571 | 0.915993 | 0.157462 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 1.27439 | 0.795892 | -0.979318 | -0.0253267 | 0.735314 | 1.25745 | 1.78476 | 2.68721 | 3.37416 |
| player | theta_1 | 1186 | -0.541364 | 0.92988 | -2.92618 | -1.94377 | -1.13766 | -0.637179 | -0.00137674 | 1.08886 | 3.81531 |
| player | theta_2 | 1186 | -0.497492 | 0.830564 | -3.03722 | -1.76215 | -1.02685 | -0.575312 | 0.00543065 | 1.02017 | 2.5529 |
| player | theta_3 | 1186 | -0.578674 | 0.927427 | -3.24248 | -1.92071 | -1.17238 | -0.696362 | -0.0550675 | 1.15264 | 2.98401 |
| player | theta_norm | 1186 | 1.7008 | 0.629017 | 0.256927 | 0.758379 | 1.26073 | 1.63321 | 2.09291 | 2.82701 | 5.01354 |
| tossup | start_difficulty_d1 | 1240 | -1.11499 | 0.541738 | -2.82428 | -1.82771 | -1.46972 | -1.16485 | -0.816824 | -0.216769 | 2.13171 |
| tossup | start_difficulty_d2 | 1240 | -1.11989 | 0.488535 | -2.68931 | -1.84211 | -1.43472 | -1.16936 | -0.837436 | -0.239341 | 0.882884 |
| tossup | start_difficulty_d3 | 1240 | -1.12402 | 0.501964 | -3.01696 | -1.90193 | -1.4402 | -1.13961 | -0.809442 | -0.350073 | 1.3494 |
| tossup | end_difficulty_d1 | 1240 | -2.11157 | 0.627977 | -4.01554 | -2.97269 | -2.51348 | -2.16229 | -1.75433 | -1.05163 | 1.40531 |
| tossup | end_difficulty_d2 | 1240 | -2.11553 | 0.573773 | -3.93312 | -2.96478 | -2.48481 | -2.15785 | -1.78366 | -1.0772 | 0.21076 |
| tossup | end_difficulty_d3 | 1240 | -2.11933 | 0.590227 | -4.32386 | -3.04815 | -2.49682 | -2.13867 | -1.74046 | -1.19365 | 0.683013 |
| tossup | total_drop_d1 | 1240 | 0.996584 | 0.109986 | 0.59672 | 0.81281 | 0.92913 | 0.998792 | 1.06306 | 1.17404 | 1.59872 |
| tossup | total_drop_d2 | 1240 | 0.995639 | 0.101648 | 0.642908 | 0.820475 | 0.930497 | 0.999351 | 1.06355 | 1.16193 | 1.43563 |
| tossup | total_drop_d3 | 1240 | 0.995308 | 0.106353 | 0.603342 | 0.827174 | 0.927457 | 0.993269 | 1.06317 | 1.1598 | 1.55235 |
| tossup | drop_share_1_d1 | 1240 | 0.304261 | 0.0153687 | 0.213296 | 0.280417 | 0.295535 | 0.304891 | 0.313797 | 0.327865 | 0.356072 |
| tossup | drop_share_2_d1 | 1240 | 0.346736 | 0.0117532 | 0.307759 | 0.328314 | 0.338724 | 0.346714 | 0.354513 | 0.365892 | 0.428339 |
| tossup | drop_share_3_d1 | 1240 | 0.349003 | 0.0162351 | 0.299389 | 0.324603 | 0.33863 | 0.347923 | 0.358512 | 0.376134 | 0.450692 |
| tossup | drop_share_1_d2 | 1240 | 0.304784 | 0.014463 | 0.241317 | 0.280143 | 0.295832 | 0.305241 | 0.313998 | 0.327264 | 0.34991 |
| tossup | drop_share_2_d2 | 1240 | 0.347139 | 0.0116067 | 0.314852 | 0.328179 | 0.339108 | 0.347102 | 0.355081 | 0.366272 | 0.382135 |
| tossup | drop_share_3_d2 | 1240 | 0.348077 | 0.0153675 | 0.302509 | 0.324188 | 0.337662 | 0.346901 | 0.357498 | 0.375185 | 0.412023 |
| tossup | drop_share_1_d3 | 1240 | 0.304618 | 0.0145462 | 0.23744 | 0.280951 | 0.295472 | 0.304998 | 0.314393 | 0.328382 | 0.359585 |
| tossup | drop_share_2_d3 | 1240 | 0.347109 | 0.0113748 | 0.311911 | 0.327647 | 0.339582 | 0.347102 | 0.35521 | 0.365312 | 0.382688 |
| tossup | drop_share_3_d3 | 1240 | 0.348273 | 0.0152825 | 0.294697 | 0.323008 | 0.338781 | 0.347647 | 0.357403 | 0.373432 | 0.412615 |
| tossup | r_1 | 1240 | 0.319742 | 0.165743 | 0.047347 | 0.108088 | 0.188223 | 0.286405 | 0.429492 | 0.630324 | 0.875291 |
| tossup | r_2 | 1240 | 0.332202 | 0.167496 | 0.0586126 | 0.118617 | 0.202077 | 0.295739 | 0.429624 | 0.676548 | 0.839197 |
| tossup | r_3 | 1240 | 0.348056 | 0.171041 | 0.0571739 | 0.115353 | 0.211414 | 0.318516 | 0.4642 | 0.662354 | 0.872597 |
| tossup | r_norm | 1240 | 0.644275 | 0.0579736 | 0.577424 | 0.581339 | 0.599937 | 0.627064 | 0.672035 | 0.763109 | 0.879737 |
| tossup_hazard | hazard_start_difficulty_d1 | 1240 | 7.47486 | 0.520442 | 3.72417 | 6.63542 | 7.30556 | 7.46758 | 7.68282 | 8.38477 | 9.25554 |
| tossup_hazard | hazard_start_difficulty_d2 | 1240 | 7.48429 | 0.509168 | 4.45948 | 6.59666 | 7.34967 | 7.49027 | 7.67882 | 8.29916 | 9.68704 |
| tossup_hazard | hazard_start_difficulty_d3 | 1240 | 7.54094 | 0.503385 | 4.55487 | 6.74574 | 7.35637 | 7.50852 | 7.7452 | 8.42501 | 9.72334 |
| tossup_hazard | hazard_end_difficulty_d1 | 1240 | 4.08298 | 3.41328 | -11.4546 | -2.7144 | 1.88251 | 6.24292 | 6.45829 | 6.73909 | 7.54614 |
| tossup_hazard | hazard_end_difficulty_d2 | 1240 | 4.5078 | 3.45919 | -11.568 | -3.00371 | 2.80073 | 6.36361 | 6.53004 | 6.85813 | 7.76317 |
| tossup_hazard | hazard_end_difficulty_d3 | 1240 | 4.57081 | 3.34279 | -11.894 | -2.43785 | 3.04876 | 6.36274 | 6.54414 | 6.95225 | 7.81493 |
| tossup_hazard | hazard_total_drop_d1 | 1240 | 3.39188 | 3.51294 | 0.849925 | 0.952134 | 1.01027 | 1.07565 | 5.65538 | 10.5688 | 19.3512 |
| tossup_hazard | hazard_total_drop_d2 | 1240 | 2.97648 | 3.52291 | 0.847067 | 0.945049 | 0.996176 | 1.04262 | 4.55005 | 10.778 | 19.8307 |
| tossup_hazard | hazard_total_drop_d3 | 1240 | 2.97013 | 3.42424 | 0.852656 | 0.935451 | 0.992743 | 1.04445 | 4.73787 | 10.2581 | 19.9106 |
| tossup_hazard | hazard_drop_share_1_d1 | 1240 | 0.260259 | 0.0879563 | 0.0517762 | 0.0956588 | 0.203556 | 0.29132 | 0.305642 | 0.3323 | 0.715527 |
| tossup_hazard | hazard_drop_share_2_d1 | 1240 | 0.33409 | 0.0795573 | 0.0624401 | 0.17017 | 0.328195 | 0.345738 | 0.357404 | 0.45484 | 0.722041 |
| tossup_hazard | hazard_drop_share_3_d1 | 1240 | 0.405652 | 0.131108 | 0.103741 | 0.280302 | 0.342472 | 0.356998 | 0.40846 | 0.713484 | 0.885784 |
| tossup_hazard | hazard_drop_share_1_d2 | 1240 | 0.271544 | 0.0819219 | 0.0389532 | 0.10203 | 0.266598 | 0.294773 | 0.307221 | 0.33018 | 0.728135 |
| tossup_hazard | hazard_drop_share_2_d2 | 1240 | 0.337716 | 0.0716851 | 0.0675987 | 0.180084 | 0.334991 | 0.346582 | 0.3576 | 0.441066 | 0.655706 |
| tossup_hazard | hazard_drop_share_3_d2 | 1240 | 0.39074 | 0.121951 | 0.0807901 | 0.263866 | 0.342589 | 0.354813 | 0.377046 | 0.692825 | 0.893448 |
| tossup_hazard | hazard_drop_share_1_d3 | 1240 | 0.265662 | 0.0810121 | 0.0411133 | 0.0988368 | 0.2575 | 0.29319 | 0.306283 | 0.326359 | 0.724029 |
| tossup_hazard | hazard_drop_share_2_d3 | 1240 | 0.338132 | 0.0725679 | 0.0710188 | 0.184987 | 0.332554 | 0.346028 | 0.357371 | 0.444812 | 0.727915 |
| tossup_hazard | hazard_drop_share_3_d3 | 1240 | 0.396207 | 0.121069 | 0.0877105 | 0.291297 | 0.343121 | 0.357088 | 0.388094 | 0.70078 | 0.886782 |
| tossup_hazard | hazard_r_1 | 1240 | 0.361071 | 0.294553 | 0.0137004 | 0.038614 | 0.097436 | 0.241779 | 0.600911 | 0.886747 | 0.947166 |
| tossup_hazard | hazard_r_2 | 1240 | 0.305618 | 0.2701 | 0.0130538 | 0.0313125 | 0.0751805 | 0.181932 | 0.518696 | 0.826644 | 0.929736 |
| tossup_hazard | hazard_r_3 | 1240 | 0.333311 | 0.271795 | 0.0126697 | 0.0342598 | 0.0857575 | 0.252538 | 0.545596 | 0.852959 | 0.973246 |
