# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_6/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_6/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 335408 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.554777 |
| log_loss | 0.577715 |
| ece | 0.0823619 |
| brier | 0.185956 |
| accuracy | 0.765465 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.000215169 |
| probability_std | 0.112354 |
| probability_p10 | 0.655483 |
| probability_p50 | 0.854881 |
| probability_p90 | 0.933144 |
| mean_predictive_variance | 0.134532 |
| integrated_brier_score | 0.170339 |
| joint_tossup_event_log_loss | 7.68296 |
| buzz_position_mae | 0.328052 |
| buzz_position_median_absolute_error | 0.326762 |
| buzz_position_bias | -0.313279 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.340075 |
| first_buzzer_mean_reciprocal_rank | 0.557232 |
| first_buzzer_log_loss | 1.68468 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.621087 |
| tossup_scorer_player_top1_accuracy | 0.266561 |
| tossup_scorer_team_top1_accuracy | 0.386943 |
| tossup_game_winner_accuracy | 0.711454 |
| tossup_game_margin_mae | 43.6788 |
| tournament_player_ppg_spearman | 0.568674 |
| tournament_player_ppg_mae | 10.4629 |
| tournament_player_ppg_top10_overlap | 0.610345 |
| neg_auroc | 0.554777 |
| neg_average_precision | 0.288943 |
| neg_precision | 0.508475 |
| neg_recall | 0.0274977 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0330132 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.223426 |
| no_buzz_calibration_error | 0.210156 |
| no_buzz_brier | 0.0654855 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| tossup_correctness | aggregate | all | 9295 | 0.554777 | 0.577715 | 0.0823619 | 0.185956 | 0.765465 | 0.76525 | 0.000215169 | 0.112354 | 0.655483 | 0.854881 | 0.933144 | 0.134532 |
| tossup_correctness | tier | fall | 2933 | 0.558541 | 0.532676 | 0.0675787 | 0.168963 | 0.792363 | 0.791681 | 0.000681896 | 0.0907872 | 0.709424 | 0.867223 | 0.930456 | 0.12486 |
| tossup_correctness | tier | nationals | 1584 | 0.58354 | 0.599335 | 0.0714159 | 0.200776 | 0.726641 | 0.724747 | 0.00189394 | 0.133132 | 0.550552 | 0.739313 | 0.901517 | 0.179572 |
| tossup_correctness | tier | regionals | 1886 | 0.521602 | 0.617556 | 0.109288 | 0.201452 | 0.743372 | 0.746023 | -0.00265111 | 0.118141 | 0.626353 | 0.82414 | 0.92996 | 0.147825 |
| tossup_correctness | tier | winter | 2892 | 0.538278 | 0.585569 | 0.0926479 | 0.184966 | 0.773859 | 0.773167 | 0.000691563 | 0.0781785 | 0.755398 | 0.886708 | 0.941539 | 0.111004 |
| tossup_correctness | category | Current Events | 124 | 0.551162 | 0.583692 | 0.115262 | 0.19457 | 0.75 | 0.75 | 0 | 0.122936 | 0.578813 | 0.817063 | 0.901892 | 0.156377 |
| tossup_correctness | category | Fine Arts | 1103 | 0.513703 | 0.619094 | 0.117519 | 0.197388 | 0.760653 | 0.759746 | 0.000906618 | 0.10875 | 0.671573 | 0.880567 | 0.939836 | 0.122786 |
| tossup_correctness | category | Geography | 197 | 0.64662 | 0.691365 | 0.157461 | 0.238152 | 0.670051 | 0.670051 | 0 | 0.100036 | 0.69516 | 0.851634 | 0.92737 | 0.132904 |
| tossup_correctness | category | History | 1491 | 0.558889 | 0.537882 | 0.0618907 | 0.172023 | 0.78605 | 0.787391 | -0.00134138 | 0.105889 | 0.661602 | 0.8467 | 0.925097 | 0.138058 |
| tossup_correctness | category | Literature | 1472 | 0.557798 | 0.520478 | 0.0791304 | 0.161622 | 0.806386 | 0.804348 | 0.00203804 | 0.10521 | 0.688994 | 0.884539 | 0.943948 | 0.117862 |
| tossup_correctness | category | Mythology | 332 | 0.557646 | 0.501933 | 0.0901832 | 0.157543 | 0.816265 | 0.813253 | 0.00301205 | 0.0946289 | 0.706426 | 0.881514 | 0.934248 | 0.120412 |
| tossup_correctness | category | Other Academic | 69 | 0.489819 | 0.612382 | 0.149169 | 0.196591 | 0.782609 | 0.753623 | 0.0289855 | 0.125102 | 0.600427 | 0.830448 | 0.913791 | 0.152289 |
| tossup_correctness | category | Philosophy | 324 | 0.596495 | 0.503446 | 0.0719318 | 0.157603 | 0.799383 | 0.799383 | 0 | 0.109042 | 0.658515 | 0.871286 | 0.935857 | 0.128463 |
| tossup_correctness | category | Popular Culture | 102 | 0.33564 | 0.518969 | 0.107673 | 0.157171 | 0.833333 | 0.833333 | 0 | 0.080364 | 0.70576 | 0.862369 | 0.91936 | 0.127648 |
| tossup_correctness | category | Religion | 372 | 0.61318 | 0.640997 | 0.116067 | 0.212599 | 0.715054 | 0.709677 | 0.00537634 | 0.125898 | 0.63214 | 0.869102 | 0.934575 | 0.13094 |
| tossup_correctness | category | Science | 1487 | 0.591374 | 0.570506 | 0.0576233 | 0.185633 | 0.752522 | 0.752522 | 0 | 0.113585 | 0.64653 | 0.832151 | 0.923924 | 0.144262 |
| tossup_correctness | category | Social Science | 336 | 0.539153 | 0.69597 | 0.136949 | 0.229991 | 0.702381 | 0.702381 | 0 | 0.107306 | 0.665911 | 0.872668 | 0.93028 | 0.127925 |
| tossup_correctness | category | Unknown | 1886 | 0.521602 | 0.617556 | 0.109288 | 0.201452 | 0.743372 | 0.746023 | -0.00265111 | 0.118141 | 0.626353 | 0.82414 | 0.92996 | 0.147825 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.524801 | 0.61175 | 0.0978635 | 0.205404 | 0.725888 | 0.736041 | -0.0101523 | 0.118824 | 0.585696 | 0.784941 | 0.900067 | 0.168174 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.536007 | 0.614326 | 0.0888966 | 0.202896 | 0.736041 | 0.735025 | 0.00101523 | 0.108797 | 0.638983 | 0.830047 | 0.909917 | 0.14944 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.574383 | 0.553041 | 0.0634442 | 0.179464 | 0.769436 | 0.769436 | 0 | 0.104792 | 0.665267 | 0.845278 | 0.920155 | 0.139018 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.559786 | 0.545105 | 0.076899 | 0.173985 | 0.785415 | 0.78402 | 0.00139567 | 0.10896 | 0.662683 | 0.860222 | 0.930285 | 0.132839 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.546599 | 0.613173 | 0.104207 | 0.195437 | 0.755674 | 0.756008 | -0.000333778 | 0.119038 | 0.646671 | 0.87557 | 0.943726 | 0.125669 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1186 | -1.06853 | 1.01356 | -3.44815 | -2.41791 | -1.69576 | -1.2551 | -0.635034 | 1.19418 | 2.20991 |
| player | beta | 1186 | -4.0929 | 1.29278 | -7.32379 | -6.59313 | -4.90452 | -3.77162 | -3.06477 | -2.48221 | -1.93829 |
| player | theta_1 | 1186 | 0.64576 | 0.790064 | -2.2319 | -0.902338 | 0.214161 | 0.819555 | 1.19059 | 1.69132 | 2.71697 |
| player | theta_2 | 1186 | 0.688693 | 0.964862 | -2.46539 | -1.06603 | 0.0503047 | 0.908837 | 1.43233 | 1.92302 | 3.10758 |
| player | theta_3 | 1186 | 0.662001 | 0.807564 | -2.21741 | -0.885638 | 0.198897 | 0.782555 | 1.19783 | 1.7983 | 2.73511 |
| player | theta_4 | 1186 | 0.645665 | 0.781017 | -1.83642 | -0.865461 | 0.174651 | 0.770907 | 1.19626 | 1.72945 | 2.41442 |
| player | theta_5 | 1186 | 0.576285 | 0.6065 | -1.73173 | -0.665989 | 0.311896 | 0.680435 | 0.940862 | 1.37898 | 2.45707 |
| player | theta_6 | 1186 | 0.585287 | 0.608304 | -1.85107 | -0.680258 | 0.322159 | 0.705562 | 0.967093 | 1.34064 | 2.26674 |
| player | theta_norm | 1186 | 2.32236 | 0.761854 | 0.198711 | 0.917521 | 1.84324 | 2.4094 | 2.81953 | 3.4577 | 4.8368 |
| tossup | start_difficulty_d1 | 1240 | -0.709276 | 0.394074 | -1.9754 | -1.43574 | -0.953595 | -0.683336 | -0.434748 | -0.0909464 | 0.357323 |
| tossup | start_difficulty_d2 | 1240 | -0.723544 | 0.397532 | -1.92571 | -1.42617 | -0.995067 | -0.70887 | -0.396068 | -0.137332 | 0.306001 |
| tossup | start_difficulty_d3 | 1240 | -0.719451 | 0.445033 | -2.21775 | -1.60694 | -0.993253 | -0.647852 | -0.399489 | -0.100878 | 0.315621 |
| tossup | start_difficulty_d4 | 1240 | -0.695834 | 0.395216 | -2.01711 | -1.37922 | -0.963185 | -0.674917 | -0.392384 | -0.0866627 | 0.277062 |
| tossup | start_difficulty_d5 | 1240 | -0.653172 | 0.340325 | -1.69959 | -1.19056 | -0.916991 | -0.655447 | -0.393958 | -0.076134 | 0.427434 |
| tossup | start_difficulty_d6 | 1240 | -0.659454 | 0.355496 | -1.8299 | -1.2424 | -0.902204 | -0.654368 | -0.391767 | -0.075611 | 0.339794 |
| tossup | end_difficulty_d1 | 1240 | -1.60475 | 0.354835 | -2.73305 | -2.2026 | -1.8378 | -1.56734 | -1.37243 | -1.01194 | -0.351035 |
| tossup | end_difficulty_d2 | 1240 | -1.59596 | 0.328156 | -2.61767 | -2.13436 | -1.82104 | -1.58838 | -1.38119 | -1.06258 | -0.308213 |
| tossup | end_difficulty_d3 | 1240 | -1.60883 | 0.387053 | -2.91631 | -2.32213 | -1.82945 | -1.56498 | -1.3582 | -1.04098 | -0.410381 |
| tossup | end_difficulty_d4 | 1240 | -1.59652 | 0.358135 | -2.72786 | -2.20709 | -1.84368 | -1.58372 | -1.34422 | -1.00651 | -0.49704 |
| tossup | end_difficulty_d5 | 1240 | -1.56681 | 0.324356 | -2.48803 | -2.06957 | -1.7964 | -1.55562 | -1.35112 | -1.0086 | -0.281432 |
| tossup | end_difficulty_d6 | 1240 | -1.57078 | 0.335953 | -2.57331 | -2.13527 | -1.79224 | -1.54749 | -1.35487 | -1.01975 | -0.393136 |
| tossup | total_drop_d1 | 1240 | 0.895471 | 0.19037 | 0.328752 | 0.572304 | 0.773353 | 0.882571 | 1.02552 | 1.20363 | 1.69385 |
| tossup | total_drop_d2 | 1240 | 0.872416 | 0.206627 | 0.279675 | 0.474754 | 0.75672 | 0.887081 | 1.0262 | 1.16757 | 1.48807 |
| tossup | total_drop_d3 | 1240 | 0.889375 | 0.199106 | 0.343619 | 0.536552 | 0.768432 | 0.888869 | 1.02748 | 1.20614 | 1.5247 |
| tossup | total_drop_d4 | 1240 | 0.900684 | 0.189706 | 0.348135 | 0.569248 | 0.780094 | 0.895069 | 1.02918 | 1.20894 | 1.50106 |
| tossup | total_drop_d5 | 1240 | 0.913637 | 0.161955 | 0.468643 | 0.685469 | 0.788528 | 0.890579 | 1.02575 | 1.20116 | 1.41646 |
| tossup | total_drop_d6 | 1240 | 0.911328 | 0.162089 | 0.474781 | 0.684095 | 0.784125 | 0.890321 | 1.02343 | 1.20248 | 1.41404 |
| tossup | drop_share_1_d1 | 1240 | 0.311935 | 0.017746 | 0.235197 | 0.285177 | 0.300333 | 0.31126 | 0.323135 | 0.341175 | 0.384729 |
| tossup | drop_share_2_d1 | 1240 | 0.336782 | 0.0142397 | 0.280721 | 0.311549 | 0.328468 | 0.33753 | 0.345909 | 0.359275 | 0.380837 |
| tossup | drop_share_3_d1 | 1240 | 0.351284 | 0.0187716 | 0.295304 | 0.324289 | 0.339149 | 0.350071 | 0.361051 | 0.383035 | 0.437768 |
| tossup | drop_share_1_d2 | 1240 | 0.31293 | 0.0185816 | 0.245704 | 0.285347 | 0.300479 | 0.312246 | 0.323982 | 0.344231 | 0.418468 |
| tossup | drop_share_2_d2 | 1240 | 0.335452 | 0.0162841 | 0.261728 | 0.304813 | 0.326464 | 0.337272 | 0.346648 | 0.358198 | 0.381351 |
| tossup | drop_share_3_d2 | 1240 | 0.351618 | 0.0213852 | 0.268362 | 0.321878 | 0.337941 | 0.348999 | 0.36175 | 0.391391 | 0.468823 |
| tossup | drop_share_1_d3 | 1240 | 0.313048 | 0.0203733 | 0.243412 | 0.284125 | 0.300531 | 0.310835 | 0.323111 | 0.351327 | 0.417018 |
| tossup | drop_share_2_d3 | 1240 | 0.336544 | 0.0147907 | 0.269121 | 0.310831 | 0.32728 | 0.337775 | 0.346615 | 0.359432 | 0.377885 |
| tossup | drop_share_3_d3 | 1240 | 0.350408 | 0.0198039 | 0.2649 | 0.31984 | 0.338509 | 0.350035 | 0.360539 | 0.381759 | 0.443291 |
| tossup | drop_share_1_d4 | 1240 | 0.312138 | 0.0183061 | 0.230673 | 0.283689 | 0.299903 | 0.311663 | 0.323155 | 0.342905 | 0.377316 |
| tossup | drop_share_2_d4 | 1240 | 0.336716 | 0.0143022 | 0.2777 | 0.311588 | 0.328584 | 0.338035 | 0.346 | 0.358179 | 0.376785 |
| tossup | drop_share_3_d4 | 1240 | 0.351146 | 0.0195206 | 0.293442 | 0.324289 | 0.339023 | 0.349669 | 0.360471 | 0.384153 | 0.464256 |
| tossup | drop_share_1_d5 | 1240 | 0.311501 | 0.0164187 | 0.251636 | 0.284951 | 0.300114 | 0.311179 | 0.322223 | 0.338523 | 0.366573 |
| tossup | drop_share_2_d5 | 1240 | 0.338 | 0.0128275 | 0.297201 | 0.316841 | 0.329371 | 0.338177 | 0.346808 | 0.359103 | 0.373861 |
| tossup | drop_share_3_d5 | 1240 | 0.350498 | 0.016741 | 0.297141 | 0.323447 | 0.338494 | 0.35051 | 0.361158 | 0.377518 | 0.413189 |
| tossup | drop_share_1_d6 | 1240 | 0.312217 | 0.0168573 | 0.251249 | 0.285114 | 0.301268 | 0.311528 | 0.323025 | 0.340442 | 0.382906 |
| tossup | drop_share_2_d6 | 1240 | 0.337961 | 0.0129004 | 0.293165 | 0.316808 | 0.329526 | 0.338089 | 0.346596 | 0.358751 | 0.384776 |
| tossup | drop_share_3_d6 | 1240 | 0.349822 | 0.0169157 | 0.294483 | 0.32286 | 0.338751 | 0.349323 | 0.36048 | 0.378738 | 0.431685 |
| tossup | r_1 | 1240 | 0.156778 | 0.0902795 | 0.0435585 | 0.0669445 | 0.114231 | 0.144895 | 0.165932 | 0.335998 | 0.700711 |
| tossup | r_2 | 1240 | 0.188558 | 0.149142 | 0.0385433 | 0.0651981 | 0.102334 | 0.12736 | 0.199902 | 0.56892 | 0.767652 |
| tossup | r_3 | 1240 | 0.171021 | 0.10211 | 0.0331548 | 0.0617432 | 0.11702 | 0.150136 | 0.179314 | 0.41276 | 0.719512 |
| tossup | r_4 | 1240 | 0.169265 | 0.0915012 | 0.0367871 | 0.0665934 | 0.118702 | 0.164066 | 0.187829 | 0.333922 | 0.771819 |
| tossup | r_5 | 1240 | 0.156669 | 0.0458672 | 0.0458866 | 0.0747754 | 0.121608 | 0.164086 | 0.189183 | 0.223839 | 0.340894 |
| tossup | r_6 | 1240 | 0.157709 | 0.0454125 | 0.041744 | 0.0732245 | 0.125129 | 0.173304 | 0.189916 | 0.20554 | 0.400786 |
| tossup | r_norm | 1240 | 0.463667 | 0.0760442 | 0.408637 | 0.410148 | 0.414157 | 0.424006 | 0.487388 | 0.63814 | 0.778857 |
