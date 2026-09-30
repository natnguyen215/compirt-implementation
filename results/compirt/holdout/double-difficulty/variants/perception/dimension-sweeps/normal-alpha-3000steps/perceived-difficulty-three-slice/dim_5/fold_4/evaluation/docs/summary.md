# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_5/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_5/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 320051 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.672564 |
| log_loss | 0.501102 |
| ece | 0.0170649 |
| brier | 0.162478 |
| accuracy | 0.779935 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00658037 |
| probability_std | 0.120247 |
| probability_p10 | 0.599298 |
| probability_p50 | 0.783532 |
| probability_p90 | 0.900842 |
| mean_predictive_variance | 0.165778 |
| integrated_brier_score | 0.0998792 |
| joint_tossup_event_log_loss | 6.85205 |
| buzz_position_mae | 0.15864 |
| buzz_position_median_absolute_error | 0.146058 |
| buzz_position_bias | -0.0634396 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.371197 |
| first_buzzer_mean_reciprocal_rank | 0.577652 |
| first_buzzer_log_loss | 1.65003 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.645847 |
| tossup_scorer_player_top1_accuracy | 0.326759 |
| tossup_scorer_team_top1_accuracy | 0.51194 |
| tossup_game_winner_accuracy | 0.814004 |
| tossup_game_margin_mae | 33.9986 |
| tournament_player_ppg_spearman | 0.699923 |
| tournament_player_ppg_mae | 9.05372 |
| tournament_player_ppg_top10_overlap | 0.675862 |
| neg_auroc | 0.672564 |
| neg_average_precision | 0.393682 |
| neg_precision | 0.601329 |
| neg_recall | 0.0861495 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0553365 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0912841 |
| no_buzz_calibration_error | 0.079557 |
| no_buzz_brier | 0.0247176 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.672564 | 0.501102 | 0.0170649 | 0.162478 | 0.779935 | 0.773355 | 0.00658037 | 0.120247 | 0.599298 | 0.783532 | 0.900842 | 0.165778 |
| tossup_correctness | tier | fall | 2876 | 0.673788 | 0.476818 | 0.0163133 | 0.152799 | 0.796592 | 0.793115 | 0.00347705 | 0.115105 | 0.618464 | 0.803627 | 0.901785 | 0.159074 |
| tossup_correctness | tier | nationals | 1579 | 0.671718 | 0.548633 | 0.0320425 | 0.182913 | 0.739709 | 0.729576 | 0.010133 | 0.123135 | 0.528929 | 0.716182 | 0.849853 | 0.194696 |
| tossup_correctness | tier | regionals | 1990 | 0.700799 | 0.504194 | 0.0442875 | 0.164186 | 0.774874 | 0.765829 | 0.00904523 | 0.111084 | 0.570923 | 0.742166 | 0.849017 | 0.187012 |
| tossup_correctness | tier | winter | 2825 | 0.663052 | 0.497081 | 0.0308561 | 0.159707 | 0.789027 | 0.783009 | 0.0060177 | 0.104358 | 0.672782 | 0.832939 | 0.927716 | 0.141481 |
| tossup_correctness | category | Current Events | 123 | 0.739178 | 0.493747 | 0.0770168 | 0.159235 | 0.788618 | 0.764228 | 0.0243902 | 0.123339 | 0.523985 | 0.719967 | 0.845218 | 0.192356 |
| tossup_correctness | category | Fine Arts | 1093 | 0.683332 | 0.499887 | 0.0183834 | 0.162666 | 0.781336 | 0.769442 | 0.0118939 | 0.112727 | 0.624652 | 0.792827 | 0.90219 | 0.161144 |
| tossup_correctness | category | Geography | 191 | 0.764381 | 0.519868 | 0.0494018 | 0.17033 | 0.753927 | 0.691099 | 0.0628272 | 0.165255 | 0.458691 | 0.77506 | 0.88904 | 0.17632 |
| tossup_correctness | category | History | 1469 | 0.675356 | 0.518399 | 0.0209011 | 0.170021 | 0.764466 | 0.758339 | 0.00612662 | 0.121299 | 0.603469 | 0.800143 | 0.90593 | 0.160852 |
| tossup_correctness | category | Literature | 1436 | 0.620054 | 0.470173 | 0.0341074 | 0.14768 | 0.81337 | 0.81546 | -0.00208914 | 0.108654 | 0.653265 | 0.830639 | 0.926721 | 0.144554 |
| tossup_correctness | category | Mythology | 325 | 0.636611 | 0.446196 | 0.0895777 | 0.138809 | 0.830769 | 0.843077 | -0.0123077 | 0.115437 | 0.59569 | 0.772965 | 0.888826 | 0.171356 |
| tossup_correctness | category | Other Academic | 67 | 0.642857 | 0.525642 | 0.118827 | 0.171973 | 0.761194 | 0.791045 | -0.0298507 | 0.124824 | 0.533472 | 0.696664 | 0.856469 | 0.195888 |
| tossup_correctness | category | Philosophy | 322 | 0.625136 | 0.505959 | 0.0421739 | 0.164831 | 0.78882 | 0.785714 | 0.00310559 | 0.11131 | 0.637523 | 0.809579 | 0.912295 | 0.155111 |
| tossup_correctness | category | Popular Culture | 100 | 0.518897 | 0.41343 | 0.121836 | 0.123577 | 0.88 | 0.89 | -0.01 | 0.102832 | 0.624111 | 0.797012 | 0.881802 | 0.167514 |
| tossup_correctness | category | Religion | 365 | 0.660966 | 0.565313 | 0.0589338 | 0.190971 | 0.715068 | 0.723288 | -0.00821918 | 0.12369 | 0.586999 | 0.785484 | 0.905415 | 0.166999 |
| tossup_correctness | category | Science | 1456 | 0.679113 | 0.501865 | 0.0165737 | 0.162762 | 0.775412 | 0.76717 | 0.00824176 | 0.119066 | 0.610734 | 0.798387 | 0.906703 | 0.159064 |
| tossup_correctness | category | Social Science | 333 | 0.699177 | 0.532215 | 0.0281693 | 0.177007 | 0.747748 | 0.72973 | 0.018018 | 0.12937 | 0.54919 | 0.753343 | 0.885612 | 0.177786 |
| tossup_correctness | category | Unknown | 1990 | 0.700799 | 0.504194 | 0.0442875 | 0.164186 | 0.774874 | 0.765829 | 0.00904523 | 0.111084 | 0.570923 | 0.742166 | 0.849017 | 0.187012 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.600663 | 0.557041 | 0.0968966 | 0.184802 | 0.765363 | 0.748603 | 0.0167598 | 0.125145 | 0.519066 | 0.717058 | 0.82008 | 0.198274 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.630465 | 0.539876 | 0.041851 | 0.178551 | 0.757576 | 0.754441 | 0.0031348 | 0.121364 | 0.539853 | 0.732566 | 0.864892 | 0.187816 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.654165 | 0.515721 | 0.0280591 | 0.168215 | 0.776668 | 0.766682 | 0.00998638 | 0.119606 | 0.583128 | 0.769516 | 0.884875 | 0.173362 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.691164 | 0.476596 | 0.0188885 | 0.152443 | 0.796844 | 0.787441 | 0.00940228 | 0.115378 | 0.62424 | 0.79529 | 0.904667 | 0.160931 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.685998 | 0.498954 | 0.0231169 | 0.161756 | 0.773451 | 0.771758 | 0.00169319 | 0.117889 | 0.618036 | 0.804291 | 0.918329 | 0.155896 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | -1.28352 | 1.28253 | -4.46782 | -3.55339 | -2.5388 | -0.510096 | -0.276322 | -0.0795126 | 0.511901 |
| player | theta_2 | 1196 | -2.37046 | 0.821179 | -4.87415 | -3.65375 | -2.91974 | -2.40135 | -1.92101 | -0.735068 | -0.00169994 |
| player | theta_3 | 1196 | -0.528414 | 0.381213 | -1.98983 | -1.23989 | -0.748296 | -0.45653 | -0.26042 | -0.00457804 | 0.740398 |
| player | theta_4 | 1196 | -0.872289 | 0.535254 | -3.11663 | -1.84138 | -1.18655 | -0.807093 | -0.488065 | -0.142421 | 0.722504 |
| player | theta_5 | 1196 | -0.643115 | 0.523191 | -2.72198 | -1.6382 | -0.86812 | -0.545339 | -0.315477 | 0.0466318 | 1.16771 |
| player | theta_norm | 1196 | 3.32965 | 0.810209 | 1.53441 | 2.13109 | 2.71368 | 3.27397 | 3.89812 | 4.72137 | 6.1436 |
| tossup | start_difficulty_d1 | 1240 | -1.83354 | 1.47133 | -4.15309 | -3.57243 | -3.16869 | -2.6189 | -0.218025 | 0.113193 | 0.439056 |
| tossup | start_difficulty_d2 | 1240 | -2.25509 | 1.54591 | -5.12377 | -4.27329 | -3.61006 | -2.66267 | -0.519506 | -0.0176049 | 0.211351 |
| tossup | start_difficulty_d3 | 1240 | -0.380578 | 0.61531 | -3.38513 | -1.83852 | -0.489929 | -0.170139 | -0.00541569 | 0.159387 | 0.678938 |
| tossup | start_difficulty_d4 | 1240 | -0.635889 | 0.805685 | -3.43695 | -2.32925 | -1.05454 | -0.413831 | -0.0455904 | 0.297589 | 0.894328 |
| tossup | start_difficulty_d5 | 1240 | -0.472188 | 0.697654 | -2.8508 | -2.00234 | -0.740449 | -0.242684 | 0.0127527 | 0.291795 | 1.40557 |
| tossup | end_difficulty_d1 | 1240 | -2.94024 | 1.6174 | -6.81007 | -5.11983 | -4.35009 | -3.57462 | -1.20678 | -0.828928 | -0.476602 |
| tossup | end_difficulty_d2 | 1240 | -3.34721 | 1.65933 | -8.55241 | -5.66833 | -4.71177 | -3.68093 | -1.5633 | -0.984788 | -0.699372 |
| tossup | end_difficulty_d3 | 1240 | -1.39329 | 0.698724 | -4.74006 | -3.03308 | -1.51409 | -1.16419 | -0.977833 | -0.772704 | -0.16229 |
| tossup | end_difficulty_d4 | 1240 | -1.66621 | 0.904516 | -5.48332 | -3.50508 | -2.13854 | -1.41348 | -1.02205 | -0.622398 | 0.0467859 |
| tossup | end_difficulty_d5 | 1240 | -1.50792 | 0.839826 | -4.56814 | -3.37732 | -1.78919 | -1.23107 | -0.943716 | -0.630075 | 0.607033 |
| tossup | total_drop_d1 | 1240 | 1.1067 | 0.305116 | 0.57356 | 0.815717 | 0.952854 | 1.01529 | 1.17017 | 1.64411 | 3.6459 |
| tossup | total_drop_d2 | 1240 | 1.09212 | 0.432083 | 0.375808 | 0.661566 | 0.911205 | 1.00859 | 1.14817 | 1.77568 | 5.81354 |
| tossup | total_drop_d3 | 1240 | 1.01271 | 0.11163 | 0.790546 | 0.905098 | 0.958095 | 0.992732 | 1.03561 | 1.17955 | 1.95333 |
| tossup | total_drop_d4 | 1240 | 1.03032 | 0.141093 | 0.785599 | 0.887679 | 0.946444 | 0.999062 | 1.07342 | 1.26443 | 2.30511 |
| tossup | total_drop_d5 | 1240 | 1.03574 | 0.160003 | 0.798534 | 0.895663 | 0.947363 | 0.988594 | 1.06122 | 1.36477 | 2.28912 |
| tossup | drop_share_1_d1 | 1240 | 0.349731 | 0.0450262 | 0.256784 | 0.298353 | 0.310541 | 0.336493 | 0.385791 | 0.425042 | 0.520681 |
| tossup | drop_share_2_d1 | 1240 | 0.340224 | 0.0148923 | 0.289789 | 0.313919 | 0.331346 | 0.34147 | 0.349594 | 0.363259 | 0.404487 |
| tossup | drop_share_3_d1 | 1240 | 0.310045 | 0.0405318 | 0.162718 | 0.237128 | 0.280237 | 0.32376 | 0.3435 | 0.357923 | 0.397042 |
| tossup | drop_share_1_d2 | 1240 | 0.34916 | 0.0530213 | 0.219732 | 0.294359 | 0.312398 | 0.333481 | 0.374054 | 0.450809 | 0.619619 |
| tossup | drop_share_2_d2 | 1240 | 0.337336 | 0.022568 | 0.238293 | 0.300003 | 0.324488 | 0.34033 | 0.349896 | 0.366532 | 0.500173 |
| tossup | drop_share_3_d2 | 1240 | 0.313504 | 0.0462853 | 0.131171 | 0.22075 | 0.290928 | 0.326332 | 0.34388 | 0.365307 | 0.458568 |
| tossup | drop_share_1_d3 | 1240 | 0.312856 | 0.0125641 | 0.282766 | 0.29464 | 0.304646 | 0.31207 | 0.3191 | 0.335044 | 0.382002 |
| tossup | drop_share_2_d3 | 1240 | 0.347015 | 0.00920486 | 0.318466 | 0.332562 | 0.340802 | 0.347165 | 0.353126 | 0.362286 | 0.378488 |
| tossup | drop_share_3_d3 | 1240 | 0.340129 | 0.0136152 | 0.278566 | 0.314952 | 0.332621 | 0.341588 | 0.349065 | 0.35862 | 0.392969 |
| tossup | drop_share_1_d4 | 1240 | 0.315938 | 0.0165752 | 0.281253 | 0.294651 | 0.304898 | 0.31355 | 0.322997 | 0.346278 | 0.409536 |
| tossup | drop_share_2_d4 | 1240 | 0.346567 | 0.0100873 | 0.313903 | 0.330277 | 0.340101 | 0.346436 | 0.353147 | 0.362466 | 0.41384 |
| tossup | drop_share_3_d4 | 1240 | 0.337495 | 0.016486 | 0.255813 | 0.306852 | 0.329511 | 0.339467 | 0.348106 | 0.360429 | 0.375593 |
| tossup | drop_share_1_d5 | 1240 | 0.315758 | 0.0155232 | 0.265749 | 0.294815 | 0.305444 | 0.313117 | 0.324479 | 0.344746 | 0.382273 |
| tossup | drop_share_2_d5 | 1240 | 0.346835 | 0.00925899 | 0.319557 | 0.331319 | 0.340345 | 0.346851 | 0.353163 | 0.362205 | 0.374627 |
| tossup | drop_share_3_d5 | 1240 | 0.337408 | 0.0168504 | 0.263312 | 0.305103 | 0.328593 | 0.339583 | 0.348774 | 0.360904 | 0.382255 |
| tossup | r_1 | 1240 | 0.343405 | 0.280029 | 0.0142081 | 0.0248325 | 0.0404409 | 0.455122 | 0.605961 | 0.713788 | 0.825464 |
| tossup | r_2 | 1240 | 0.412697 | 0.296885 | 0.0340481 | 0.0488945 | 0.101467 | 0.33455 | 0.708956 | 0.830834 | 0.924629 |
| tossup | r_3 | 1240 | 0.069738 | 0.049031 | 0.00625279 | 0.020536 | 0.0387595 | 0.0555315 | 0.0830045 | 0.180351 | 0.319842 |
| tossup | r_4 | 1240 | 0.0913891 | 0.0565671 | 0.0199657 | 0.0359139 | 0.0496184 | 0.0711737 | 0.118606 | 0.218469 | 0.305184 |
| tossup | r_5 | 1240 | 0.0827713 | 0.0584702 | 0.011202 | 0.0263578 | 0.0411703 | 0.0640931 | 0.100933 | 0.20692 | 0.32026 |
| tossup | r_norm | 1240 | 0.690875 | 0.080295 | 0.513387 | 0.573066 | 0.630158 | 0.681841 | 0.746048 | 0.835572 | 0.925406 |
