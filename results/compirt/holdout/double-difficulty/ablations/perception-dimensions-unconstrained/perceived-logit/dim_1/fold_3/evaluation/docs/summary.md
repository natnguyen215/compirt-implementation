# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_1/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_1/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 332450 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.571495 |
| log_loss | 0.608163 |
| ece | 0.118313 |
| brier | 0.18968 |
| accuracy | 0.768282 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.00176211 |
| probability_std | 0.0827163 |
| probability_p10 | 0.785957 |
| probability_p50 | 0.903852 |
| probability_p90 | 0.959173 |
| mean_predictive_variance | 0.0968376 |
| integrated_brier_score | 0.173837 |
| joint_tossup_event_log_loss | 7.81712 |
| buzz_position_mae | 0.340234 |
| buzz_position_median_absolute_error | 0.34349 |
| buzz_position_bias | -0.327481 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.309141 |
| first_buzzer_mean_reciprocal_rank | 0.530768 |
| first_buzzer_log_loss | 1.75074 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.629185 |
| tossup_scorer_player_top1_accuracy | 0.253145 |
| tossup_scorer_team_top1_accuracy | 0.438395 |
| tossup_game_winner_accuracy | 0.74115 |
| tossup_game_margin_mae | 43.9429 |
| tournament_player_ppg_spearman | 0.647056 |
| tournament_player_ppg_mae | 10.1204 |
| tournament_player_ppg_top10_overlap | 0.613793 |
| neg_auroc | 0.571495 |
| neg_average_precision | 0.277999 |
| neg_precision | 0.3 |
| neg_recall | 0.00574713 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0288705 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.224385 |
| no_buzz_calibration_error | 0.209201 |
| no_buzz_brier | 0.0664356 |
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
| tossup_correctness | aggregate | all | 9080 | 0.571495 | 0.608163 | 0.118313 | 0.18968 | 0.768282 | 0.770044 | -0.00176211 | 0.0827163 | 0.785957 | 0.903852 | 0.959173 | 0.0968376 |
| tossup_correctness | tier | fall | 2817 | 0.574489 | 0.57067 | 0.09869 | 0.179504 | 0.778488 | 0.781683 | -0.00319489 | 0.0827088 | 0.768228 | 0.894272 | 0.951576 | 0.104882 |
| tossup_correctness | tier | nationals | 1542 | 0.619152 | 0.660817 | 0.151006 | 0.212328 | 0.733463 | 0.73476 | -0.00129702 | 0.0926817 | 0.760756 | 0.902342 | 0.959213 | 0.100079 |
| tossup_correctness | tier | regionals | 1934 | 0.557102 | 0.647393 | 0.129257 | 0.200629 | 0.754395 | 0.75698 | -0.00258532 | 0.0936881 | 0.785873 | 0.905931 | 0.962594 | 0.0953722 |
| tossup_correctness | tier | winter | 2787 | 0.547349 | 0.589703 | 0.112463 | 0.179836 | 0.786868 | 0.786868 | 0 | 0.0646036 | 0.817389 | 0.91118 | 0.962782 | 0.0879296 |
| tossup_correctness | category | Current Events | 125 | 0.625614 | 0.679129 | 0.160454 | 0.225912 | 0.704 | 0.704 | 0 | 0.0767595 | 0.767903 | 0.888621 | 0.935036 | 0.111281 |
| tossup_correctness | category | Fine Arts | 1072 | 0.575405 | 0.613564 | 0.127457 | 0.191179 | 0.770522 | 0.770522 | 0 | 0.0709348 | 0.800109 | 0.911701 | 0.959895 | 0.0914814 |
| tossup_correctness | category | Geography | 185 | 0.627972 | 0.692877 | 0.169473 | 0.225709 | 0.713514 | 0.702703 | 0.0108108 | 0.0896338 | 0.78254 | 0.893887 | 0.953094 | 0.103451 |
| tossup_correctness | category | History | 1443 | 0.582497 | 0.601678 | 0.114797 | 0.191079 | 0.762301 | 0.765073 | -0.002772 | 0.0845964 | 0.773078 | 0.895892 | 0.952154 | 0.103929 |
| tossup_correctness | category | Literature | 1411 | 0.563779 | 0.538393 | 0.0953594 | 0.161262 | 0.810773 | 0.81219 | -0.00141743 | 0.0754371 | 0.810303 | 0.920595 | 0.966433 | 0.0846273 |
| tossup_correctness | category | Mythology | 320 | 0.53257 | 0.566352 | 0.0945843 | 0.17229 | 0.7875 | 0.79375 | -0.00625 | 0.0837677 | 0.788175 | 0.90727 | 0.953901 | 0.0978881 |
| tossup_correctness | category | Other Academic | 64 | 0.567708 | 0.64785 | 0.177195 | 0.208583 | 0.75 | 0.75 | 0 | 0.0804968 | 0.770078 | 0.893532 | 0.959089 | 0.103697 |
| tossup_correctness | category | Philosophy | 312 | 0.493742 | 0.570172 | 0.104933 | 0.169628 | 0.801282 | 0.801282 | 0 | 0.073149 | 0.81147 | 0.904812 | 0.965352 | 0.0929397 |
| tossup_correctness | category | Popular Culture | 104 | 0.606534 | 0.438298 | 0.07747 | 0.132175 | 0.846154 | 0.846154 | 0 | 0.0680145 | 0.788632 | 0.9022 | 0.960329 | 0.0964818 |
| tossup_correctness | category | Religion | 358 | 0.557732 | 0.715002 | 0.170785 | 0.225739 | 0.72067 | 0.726257 | -0.00558659 | 0.0880252 | 0.768963 | 0.906541 | 0.956229 | 0.099288 |
| tossup_correctness | category | Science | 1431 | 0.587427 | 0.596889 | 0.114709 | 0.189807 | 0.765199 | 0.765199 | 0 | 0.0780178 | 0.781179 | 0.893009 | 0.950764 | 0.104287 |
| tossup_correctness | category | Social Science | 321 | 0.530207 | 0.669972 | 0.150113 | 0.213366 | 0.735202 | 0.744548 | -0.00934579 | 0.0794721 | 0.783617 | 0.896956 | 0.948319 | 0.101458 |
| tossup_correctness | category | Unknown | 1934 | 0.557102 | 0.647393 | 0.129257 | 0.200629 | 0.754395 | 0.75698 | -0.00258532 | 0.0936881 | 0.785873 | 0.905931 | 0.962594 | 0.0953722 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.518013 | 0.736882 | 0.181635 | 0.240546 | 0.703125 | 0.697917 | 0.00520833 | 0.0768 | 0.758439 | 0.885329 | 0.934956 | 0.113424 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.576907 | 0.648006 | 0.133272 | 0.209846 | 0.728909 | 0.733408 | -0.00449944 | 0.0872521 | 0.749238 | 0.878401 | 0.944231 | 0.113639 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.534552 | 0.634273 | 0.121777 | 0.199181 | 0.755656 | 0.759276 | -0.00361991 | 0.0807499 | 0.782728 | 0.893431 | 0.952123 | 0.102975 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.577152 | 0.567631 | 0.104535 | 0.175603 | 0.788428 | 0.789125 | -0.000697107 | 0.0821041 | 0.792936 | 0.905621 | 0.958201 | 0.0952167 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.588682 | 0.607631 | 0.122434 | 0.186837 | 0.774315 | 0.775342 | -0.0010274 | 0.0813207 | 0.80696 | 0.917558 | 0.966031 | 0.0875789 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1133 | -1.57444 | 0.518792 | -2.63636 | -2.26448 | -1.89568 | -1.63702 | -1.36042 | -0.753828 | 2.36369 |
| player | beta | 1133 | -2.66141 | 0.970578 | -6.31533 | -4.63548 | -3.11114 | -2.45604 | -1.97267 | -1.48065 | -1.08188 |
| player | theta_1 | 1133 | 0.890303 | 0.761561 | -2.03043 | -0.278228 | 0.381053 | 0.897424 | 1.4183 | 2.19868 | 2.52656 |
| player | theta_norm | 1133 | 0.983852 | 0.635999 | 5.63026e-06 | 0.0948747 | 0.441143 | 0.922309 | 1.44327 | 2.19868 | 2.52656 |
| tossup | start_difficulty_d1 | 1240 | -1.53459 | 0.265959 | -2.21851 | -1.94513 | -1.72472 | -1.54829 | -1.3655 | -1.05915 | -0.651585 |
| tossup | end_difficulty_d1 | 1240 | -1.89248 | 0.331014 | -2.8526 | -2.44315 | -2.12017 | -1.89661 | -1.65925 | -1.33852 | -1.04142 |
| tossup | total_drop_d1 | 1240 | 0.357897 | 0.115989 | 0.166983 | 0.213872 | 0.262241 | 0.341792 | 0.426944 | 0.557226 | 1.12755 |
| tossup | drop_share_1_d1 | 1240 | 0.340273 | 0.0509429 | 0.171027 | 0.248772 | 0.310136 | 0.345751 | 0.374273 | 0.413694 | 0.489175 |
| tossup | drop_share_2_d1 | 1240 | 0.293452 | 0.0206686 | 0.219368 | 0.255859 | 0.28084 | 0.295183 | 0.308103 | 0.323902 | 0.359128 |
| tossup | drop_share_3_d1 | 1240 | 0.366274 | 0.0616912 | 0.234795 | 0.282438 | 0.321232 | 0.356416 | 0.399996 | 0.487095 | 0.577212 |
| tossup | r_1 | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| tossup | r_norm | 1240 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
