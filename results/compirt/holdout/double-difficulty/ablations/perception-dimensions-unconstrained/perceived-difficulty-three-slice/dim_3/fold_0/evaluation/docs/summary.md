# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_3/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_3/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 313790 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.645403 |
| log_loss | 0.524217 |
| ece | 0.0305484 |
| brier | 0.171254 |
| accuracy | 0.765573 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.000322754 |
| probability_std | 0.129949 |
| probability_p10 | 0.578939 |
| probability_p50 | 0.784193 |
| probability_p90 | 0.907571 |
| mean_predictive_variance | 0.165348 |
| integrated_brier_score | 0.101902 |
| joint_tossup_event_log_loss | 6.91346 |
| buzz_position_mae | 0.160675 |
| buzz_position_median_absolute_error | 0.148198 |
| buzz_position_bias | -0.0649778 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.343948 |
| first_buzzer_mean_reciprocal_rank | 0.559674 |
| first_buzzer_log_loss | 1.68403 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.639376 |
| tossup_scorer_player_top1_accuracy | 0.312527 |
| tossup_scorer_team_top1_accuracy | 0.478238 |
| tossup_game_winner_accuracy | 0.799559 |
| tossup_game_margin_mae | 34.281 |
| tournament_player_ppg_spearman | 0.67555 |
| tournament_player_ppg_mae | 8.9986 |
| tournament_player_ppg_top10_overlap | 0.651724 |
| neg_auroc | 0.645403 |
| neg_average_precision | 0.366429 |
| neg_precision | 0.50348 |
| neg_recall | 0.09945 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0563015 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0917439 |
| no_buzz_calibration_error | 0.0784743 |
| no_buzz_brier | 0.025582 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9420 |
| first_buzzer_team_top1_accuracy_events | 9295 |
| tossup_scorer_player_top1_accuracy_events | 9420 |
| tossup_scorer_team_top1_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 454 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.645403 | 0.524217 | 0.0305484 | 0.171254 | 0.765573 | 0.76525 | 0.000322754 | 0.129949 | 0.578939 | 0.784193 | 0.907571 | 0.165348 |
| tossup_correctness | tier | fall | 2933 | 0.615337 | 0.505796 | 0.0345359 | 0.161458 | 0.790658 | 0.791681 | -0.00102284 | 0.114615 | 0.634905 | 0.818704 | 0.923683 | 0.148261 |
| tossup_correctness | tier | nationals | 1584 | 0.656485 | 0.564487 | 0.0603829 | 0.190276 | 0.726641 | 0.724747 | 0.00189394 | 0.134292 | 0.482507 | 0.683794 | 0.837871 | 0.202487 |
| tossup_correctness | tier | regionals | 1886 | 0.634117 | 0.548372 | 0.0262221 | 0.18241 | 0.742842 | 0.746023 | -0.00318134 | 0.125047 | 0.58356 | 0.776943 | 0.896314 | 0.16881 |
| tossup_correctness | tier | winter | 2892 | 0.663456 | 0.505091 | 0.02139 | 0.163494 | 0.776279 | 0.773167 | 0.00311203 | 0.12234 | 0.608941 | 0.798766 | 0.908528 | 0.160078 |
| tossup_correctness | category | Current Events | 124 | 0.691988 | 0.526674 | 0.077617 | 0.174593 | 0.758065 | 0.75 | 0.00806452 | 0.116974 | 0.539698 | 0.708166 | 0.844228 | 0.194789 |
| tossup_correctness | category | Fine Arts | 1103 | 0.60983 | 0.545747 | 0.0530057 | 0.178917 | 0.760653 | 0.759746 | 0.000906618 | 0.123629 | 0.605462 | 0.79651 | 0.915748 | 0.159793 |
| tossup_correctness | category | Geography | 197 | 0.723077 | 0.567659 | 0.0560393 | 0.193823 | 0.685279 | 0.670051 | 0.0152284 | 0.150463 | 0.488655 | 0.725253 | 0.861785 | 0.189258 |
| tossup_correctness | category | History | 1491 | 0.677712 | 0.498628 | 0.0779664 | 0.160771 | 0.78605 | 0.787391 | -0.00134138 | 0.126363 | 0.528871 | 0.732225 | 0.859756 | 0.189405 |
| tossup_correctness | category | Literature | 1472 | 0.616497 | 0.489357 | 0.0392865 | 0.153538 | 0.805027 | 0.804348 | 0.000679348 | 0.106928 | 0.671854 | 0.848669 | 0.936038 | 0.134257 |
| tossup_correctness | category | Mythology | 332 | 0.653345 | 0.47633 | 0.0778614 | 0.152588 | 0.792169 | 0.813253 | -0.0210843 | 0.123987 | 0.567571 | 0.758844 | 0.875857 | 0.178512 |
| tossup_correctness | category | Other Academic | 69 | 0.520362 | 0.577732 | 0.143483 | 0.194201 | 0.782609 | 0.753623 | 0.0289855 | 0.10979 | 0.511747 | 0.672142 | 0.8188 | 0.209775 |
| tossup_correctness | category | Philosophy | 324 | 0.678586 | 0.470207 | 0.0355905 | 0.14985 | 0.799383 | 0.799383 | 0 | 0.121937 | 0.608963 | 0.798135 | 0.910171 | 0.157508 |
| tossup_correctness | category | Popular Culture | 102 | 0.492042 | 0.542654 | 0.145205 | 0.179398 | 0.745098 | 0.833333 | -0.0882353 | 0.140401 | 0.524969 | 0.732805 | 0.875055 | 0.187135 |
| tossup_correctness | category | Religion | 372 | 0.666316 | 0.572844 | 0.0408484 | 0.194 | 0.712366 | 0.709677 | 0.00268817 | 0.141481 | 0.534278 | 0.765297 | 0.886814 | 0.176171 |
| tossup_correctness | category | Science | 1487 | 0.671681 | 0.527104 | 0.0339646 | 0.172329 | 0.763282 | 0.752522 | 0.0107599 | 0.130226 | 0.599916 | 0.81373 | 0.918034 | 0.154241 |
| tossup_correctness | category | Social Science | 336 | 0.662542 | 0.57405 | 0.0340306 | 0.195098 | 0.708333 | 0.702381 | 0.00595238 | 0.122484 | 0.56891 | 0.744505 | 0.863273 | 0.184717 |
| tossup_correctness | category | Unknown | 1886 | 0.634117 | 0.548372 | 0.0262221 | 0.18241 | 0.742842 | 0.746023 | -0.00318134 | 0.125047 | 0.58356 | 0.776943 | 0.896314 | 0.16881 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.634218 | 0.572612 | 0.0822155 | 0.190642 | 0.725888 | 0.736041 | -0.0101523 | 0.130575 | 0.511598 | 0.707286 | 0.829617 | 0.200151 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.611741 | 0.571995 | 0.0528334 | 0.191348 | 0.73198 | 0.735025 | -0.00304569 | 0.134318 | 0.51983 | 0.737431 | 0.866734 | 0.186196 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.645937 | 0.518694 | 0.0272197 | 0.169317 | 0.76988 | 0.769436 | 0.000444247 | 0.125243 | 0.574745 | 0.772607 | 0.886739 | 0.172915 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.653584 | 0.497141 | 0.0282587 | 0.160403 | 0.783671 | 0.78402 | -0.000348918 | 0.125637 | 0.593177 | 0.796998 | 0.908673 | 0.160651 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.652058 | 0.535377 | 0.0301613 | 0.175208 | 0.758678 | 0.756008 | 0.00267023 | 0.129318 | 0.598105 | 0.803906 | 0.924119 | 0.155014 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | -2.3357 | 0.723999 | -4.9253 | -3.54637 | -2.83522 | -2.30227 | -1.81546 | -1.18315 | -0.399688 |
| player | theta_2 | 1186 | -1.34526 | 0.98238 | -4.77633 | -3.13154 | -2.15021 | -1.06399 | -0.536606 | -0.132186 | 1.14887 |
| player | theta_3 | 1186 | -1.00305 | 0.922708 | -4.16944 | -3.12775 | -1.21755 | -0.701264 | -0.389655 | -0.0843016 | 0.3903 |
| player | theta_norm | 1186 | 3.1703 | 0.748095 | 1.4667 | 2.0779 | 2.61401 | 3.10833 | 3.63421 | 4.47689 | 5.47296 |
| tossup | start_difficulty_d1 | 1240 | -2.44665 | 1.12348 | -5.23499 | -3.93353 | -3.34599 | -2.72237 | -1.50736 | -0.423409 | 0.41095 |
| tossup | start_difficulty_d2 | 1240 | -1.0541 | 1.39642 | -4.66728 | -3.91573 | -1.76656 | -0.399315 | -0.0603719 | 0.249203 | 1.00876 |
| tossup | start_difficulty_d3 | 1240 | -1.24466 | 1.16192 | -3.67133 | -3.07336 | -2.4244 | -0.966008 | -0.242648 | 0.248838 | 1.70231 |
| tossup | end_difficulty_d1 | 1240 | -3.56246 | 1.27903 | -8.23502 | -5.51915 | -4.45558 | -3.7095 | -2.56149 | -1.40266 | -0.472898 |
| tossup | end_difficulty_d2 | 1240 | -2.08501 | 1.47165 | -7.72192 | -5.01486 | -3.05225 | -1.42036 | -1.02454 | -0.668285 | 0.219363 |
| tossup | end_difficulty_d3 | 1240 | -2.29856 | 1.29152 | -5.79047 | -4.48509 | -3.44975 | -2.00002 | -1.20647 | -0.67202 | 0.92369 |
| tossup | total_drop_d1 | 1240 | 1.11581 | 0.437035 | 0.368604 | 0.685164 | 0.890476 | 1.01112 | 1.20829 | 1.93827 | 4.92256 |
| tossup | total_drop_d2 | 1240 | 1.03092 | 0.251405 | 0.498676 | 0.741137 | 0.926004 | 0.989035 | 1.07296 | 1.42932 | 3.68464 |
| tossup | total_drop_d3 | 1240 | 1.0539 | 0.220215 | 0.634609 | 0.848783 | 0.934193 | 0.995146 | 1.10208 | 1.45386 | 3.55507 |
| tossup | drop_share_1_d1 | 1240 | 0.356801 | 0.0487953 | 0.18497 | 0.300528 | 0.323088 | 0.345977 | 0.382898 | 0.451086 | 0.61852 |
| tossup | drop_share_2_d1 | 1240 | 0.337526 | 0.0202885 | 0.241136 | 0.306257 | 0.325826 | 0.337755 | 0.349725 | 0.365889 | 0.535066 |
| tossup | drop_share_3_d1 | 1240 | 0.305674 | 0.0438886 | 0.140344 | 0.226466 | 0.28067 | 0.313803 | 0.336268 | 0.362396 | 0.469161 |
| tossup | drop_share_1_d2 | 1240 | 0.324132 | 0.0372878 | 0.222347 | 0.291275 | 0.30585 | 0.314737 | 0.328336 | 0.399735 | 0.702323 |
| tossup | drop_share_2_d2 | 1240 | 0.343602 | 0.0164657 | 0.196716 | 0.310571 | 0.337658 | 0.345914 | 0.352992 | 0.363381 | 0.410452 |
| tossup | drop_share_3_d2 | 1240 | 0.332266 | 0.0325846 | 0.100962 | 0.267875 | 0.323653 | 0.338528 | 0.348717 | 0.367594 | 0.455472 |
| tossup | drop_share_1_d3 | 1240 | 0.332048 | 0.0323959 | 0.244398 | 0.29536 | 0.309841 | 0.321642 | 0.348881 | 0.401143 | 0.467046 |
| tossup | drop_share_2_d3 | 1240 | 0.343685 | 0.0118854 | 0.304268 | 0.323483 | 0.336427 | 0.344093 | 0.350868 | 0.361569 | 0.399191 |
| tossup | drop_share_3_d3 | 1240 | 0.324268 | 0.0309852 | 0.196529 | 0.261617 | 0.308078 | 0.332434 | 0.346006 | 0.360981 | 0.40566 |
| tossup | r_1 | 1240 | 0.516454 | 0.312452 | 0.0373309 | 0.0756768 | 0.206679 | 0.611409 | 0.825364 | 0.90253 | 0.96793 |
| tossup | r_2 | 1240 | 0.22052 | 0.250624 | 0.014677 | 0.0330483 | 0.0565575 | 0.0973553 | 0.228057 | 0.758916 | 0.886261 |
| tossup | r_3 | 1240 | 0.263026 | 0.275884 | 0.0129273 | 0.0309276 | 0.0602131 | 0.112321 | 0.555515 | 0.781132 | 0.912116 |
| tossup | r_norm | 1240 | 0.784305 | 0.0759355 | 0.595605 | 0.664868 | 0.722913 | 0.783547 | 0.844519 | 0.906976 | 0.968197 |
