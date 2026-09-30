# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_2/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_2/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 334467 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.54923 |
| log_loss | 0.611278 |
| ece | 0.11219 |
| brier | 0.190244 |
| accuracy | 0.768612 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.00143172 |
| probability_std | 0.0892334 |
| probability_p10 | 0.758203 |
| probability_p50 | 0.898993 |
| probability_p90 | 0.95549 |
| mean_predictive_variance | 0.102056 |
| integrated_brier_score | 0.174767 |
| joint_tossup_event_log_loss | 7.78696 |
| buzz_position_mae | 0.342725 |
| buzz_position_median_absolute_error | 0.346285 |
| buzz_position_bias | -0.330231 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.339868 |
| first_buzzer_mean_reciprocal_rank | 0.555336 |
| first_buzzer_log_loss | 1.69024 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.637445 |
| tossup_scorer_player_top1_accuracy | 0.261171 |
| tossup_scorer_team_top1_accuracy | 0.429176 |
| tossup_game_winner_accuracy | 0.734513 |
| tossup_game_margin_mae | 45.1292 |
| tournament_player_ppg_spearman | 0.625199 |
| tournament_player_ppg_mae | 10.2573 |
| tournament_player_ppg_top10_overlap | 0.6 |
| neg_auroc | 0.54923 |
| neg_average_precision | 0.26542 |
| neg_precision | 0.372549 |
| neg_recall | 0.00909962 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0282279 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.231074 |
| no_buzz_calibration_error | 0.215889 |
| no_buzz_brier | 0.0701174 |
| full_pmf_max_mass_error | 1.11022e-15 |
| tossup_outcome_events | 9220 |
| first_buzzer_team_top1_accuracy_events | 9080 |
| tossup_scorer_player_top1_accuracy_events | 9220 |
| tossup_scorer_team_top1_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 452 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.54923 | 0.611278 | 0.11219 | 0.190244 | 0.768612 | 0.770044 | -0.00143172 | 0.0892334 | 0.758203 | 0.898993 | 0.95549 | 0.102056 |
| tossup_correctness | tier | fall | 2817 | 0.551123 | 0.574273 | 0.0983673 | 0.181141 | 0.778488 | 0.781683 | -0.00319489 | 0.0884207 | 0.753182 | 0.890172 | 0.94532 | 0.109989 |
| tossup_correctness | tier | nationals | 1542 | 0.593679 | 0.659952 | 0.138915 | 0.211099 | 0.732166 | 0.73476 | -0.00259403 | 0.107682 | 0.701089 | 0.893006 | 0.960889 | 0.108353 |
| tossup_correctness | tier | regionals | 1934 | 0.537398 | 0.648873 | 0.12388 | 0.200066 | 0.756463 | 0.75698 | -0.000517063 | 0.0929187 | 0.736708 | 0.900772 | 0.958387 | 0.100661 |
| tossup_correctness | tier | winter | 2787 | 0.52132 | 0.595662 | 0.109694 | 0.181089 | 0.787226 | 0.786868 | 0.000358809 | 0.0715047 | 0.807627 | 0.907046 | 0.959899 | 0.0915216 |
| tossup_correctness | category | Current Events | 125 | 0.639435 | 0.664046 | 0.161798 | 0.223514 | 0.704 | 0.704 | 0 | 0.0868437 | 0.72642 | 0.883098 | 0.92927 | 0.118186 |
| tossup_correctness | category | Fine Arts | 1072 | 0.566977 | 0.611168 | 0.123597 | 0.191002 | 0.770522 | 0.770522 | 0 | 0.0815643 | 0.779146 | 0.908815 | 0.960465 | 0.0953533 |
| tossup_correctness | category | Geography | 185 | 0.630769 | 0.687633 | 0.174858 | 0.225298 | 0.718919 | 0.702703 | 0.0162162 | 0.0962906 | 0.773958 | 0.888965 | 0.945899 | 0.10729 |
| tossup_correctness | category | History | 1443 | 0.568958 | 0.605399 | 0.113725 | 0.191946 | 0.761608 | 0.765073 | -0.003465 | 0.0901326 | 0.757061 | 0.89479 | 0.948531 | 0.106159 |
| tossup_correctness | category | Literature | 1411 | 0.513991 | 0.546733 | 0.0923014 | 0.163664 | 0.811481 | 0.81219 | -0.000708717 | 0.0879805 | 0.785291 | 0.904855 | 0.959952 | 0.096745 |
| tossup_correctness | category | Mythology | 320 | 0.537461 | 0.564175 | 0.0883021 | 0.171371 | 0.790625 | 0.79375 | -0.003125 | 0.0904288 | 0.774564 | 0.906405 | 0.954723 | 0.0995128 |
| tossup_correctness | category | Other Academic | 64 | 0.546875 | 0.658862 | 0.15626 | 0.208578 | 0.75 | 0.75 | 0 | 0.0988137 | 0.700687 | 0.887616 | 0.959225 | 0.11143 |
| tossup_correctness | category | Philosophy | 312 | 0.490516 | 0.566592 | 0.112999 | 0.169367 | 0.801282 | 0.801282 | 0 | 0.0799919 | 0.797154 | 0.907257 | 0.962102 | 0.0946209 |
| tossup_correctness | category | Popular Culture | 104 | 0.541193 | 0.463703 | 0.0775037 | 0.136956 | 0.836538 | 0.846154 | -0.00961538 | 0.0865586 | 0.778382 | 0.90447 | 0.950596 | 0.102329 |
| tossup_correctness | category | Religion | 358 | 0.551138 | 0.71287 | 0.162339 | 0.225687 | 0.72067 | 0.726257 | -0.00558659 | 0.0901408 | 0.763048 | 0.908803 | 0.956496 | 0.0992961 |
| tossup_correctness | category | Science | 1431 | 0.561503 | 0.602454 | 0.104386 | 0.190527 | 0.763103 | 0.765199 | -0.00209644 | 0.0890803 | 0.743408 | 0.887615 | 0.950123 | 0.110456 |
| tossup_correctness | category | Social Science | 321 | 0.500153 | 0.685472 | 0.157991 | 0.216485 | 0.738318 | 0.744548 | -0.00623053 | 0.084974 | 0.765395 | 0.902186 | 0.950769 | 0.10189 |
| tossup_correctness | category | Unknown | 1934 | 0.537398 | 0.648873 | 0.12388 | 0.200066 | 0.756463 | 0.75698 | -0.000517063 | 0.0929187 | 0.736708 | 0.900772 | 0.958387 | 0.100661 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.499743 | 0.727421 | 0.156524 | 0.238533 | 0.697917 | 0.697917 | 0 | 0.085115 | 0.732748 | 0.871176 | 0.929048 | 0.12351 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.553095 | 0.648067 | 0.120977 | 0.21012 | 0.728909 | 0.733408 | -0.00449944 | 0.0935304 | 0.728838 | 0.870085 | 0.939209 | 0.121711 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.5037 | 0.636643 | 0.116235 | 0.200247 | 0.757014 | 0.759276 | -0.00226244 | 0.0869629 | 0.756525 | 0.8877 | 0.945447 | 0.109681 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.558863 | 0.567688 | 0.0970577 | 0.175577 | 0.787731 | 0.789125 | -0.00139421 | 0.0871938 | 0.769183 | 0.899746 | 0.954493 | 0.100888 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.564844 | 0.616072 | 0.121838 | 0.187857 | 0.775342 | 0.775342 | 0 | 0.0882966 | 0.784687 | 0.917296 | 0.964136 | 0.0900382 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1133 | -1.48224 | 0.590056 | -2.81132 | -2.28292 | -1.83594 | -1.55456 | -1.20413 | -0.47543 | 2.04162 |
| player | beta | 1133 | -2.97033 | 1.02789 | -6.69945 | -5.20007 | -3.44844 | -2.75698 | -2.20403 | -1.74346 | -1.39739 |
| player | theta_1 | 1133 | 0.918218 | 0.875558 | -2.21656 | -0.581239 | 0.404439 | 0.954217 | 1.5079 | 2.25356 | 3.63807 |
| player | theta_2 | 1133 | 0.92844 | 0.869101 | -2.20845 | -0.550941 | 0.387459 | 0.990323 | 1.5505 | 2.19866 | 3.92402 |
| player | theta_norm | 1133 | 1.65587 | 0.695866 | 0.0784945 | 0.502967 | 1.12016 | 1.68613 | 2.18414 | 2.70529 | 3.92508 |
| tossup | start_difficulty_d1 | 1240 | -1.21657 | 0.486293 | -2.29841 | -1.95182 | -1.59763 | -1.26589 | -0.856939 | -0.343916 | -0.148412 |
| tossup | start_difficulty_d2 | 1240 | -1.13397 | 0.408096 | -2.07392 | -1.74728 | -1.45819 | -1.15758 | -0.826988 | -0.439137 | -0.0642965 |
| tossup | end_difficulty_d1 | 1240 | -1.76206 | 0.425716 | -3.02767 | -2.49156 | -2.07073 | -1.74649 | -1.43777 | -1.09432 | -0.869739 |
| tossup | end_difficulty_d2 | 1240 | -1.70673 | 0.35264 | -2.85398 | -2.32165 | -1.9619 | -1.66349 | -1.4502 | -1.18072 | -0.957309 |
| tossup | total_drop_d1 | 1240 | 0.545492 | 0.188651 | 0.202611 | 0.265183 | 0.384669 | 0.544076 | 0.711789 | 0.835167 | 1.02025 |
| tossup | total_drop_d2 | 1240 | 0.572759 | 0.179588 | 0.207951 | 0.291961 | 0.43919 | 0.563878 | 0.71833 | 0.868102 | 1.07922 |
| tossup | drop_share_1_d1 | 1240 | 0.33103 | 0.03594 | 0.175848 | 0.27245 | 0.309955 | 0.329614 | 0.351372 | 0.392121 | 0.465066 |
| tossup | drop_share_2_d1 | 1240 | 0.312678 | 0.019908 | 0.246821 | 0.277729 | 0.298776 | 0.315046 | 0.327464 | 0.341251 | 0.376201 |
| tossup | drop_share_3_d1 | 1240 | 0.356293 | 0.0416368 | 0.243981 | 0.298171 | 0.330559 | 0.350494 | 0.374718 | 0.438297 | 0.559272 |
| tossup | drop_share_1_d2 | 1240 | 0.326753 | 0.0325261 | 0.195533 | 0.266175 | 0.310845 | 0.327444 | 0.345525 | 0.376529 | 0.452603 |
| tossup | drop_share_2_d2 | 1240 | 0.314424 | 0.01998 | 0.248078 | 0.277931 | 0.301761 | 0.316844 | 0.329321 | 0.343461 | 0.355436 |
| tossup | drop_share_3_d2 | 1240 | 0.358823 | 0.0410217 | 0.247598 | 0.305677 | 0.332805 | 0.351422 | 0.375883 | 0.443833 | 0.521022 |
| tossup | r_1 | 1240 | 0.536183 | 0.278201 | 0.031198 | 0.069192 | 0.305035 | 0.553681 | 0.783547 | 0.92821 | 0.968371 |
| tossup | r_2 | 1240 | 0.463817 | 0.278201 | 0.0316287 | 0.07179 | 0.216453 | 0.446319 | 0.694965 | 0.930808 | 0.968802 |
| tossup | r_norm | 1240 | 0.806483 | 0.0829147 | 0.707107 | 0.707744 | 0.724837 | 0.792963 | 0.880781 | 0.948122 | 0.969304 |
