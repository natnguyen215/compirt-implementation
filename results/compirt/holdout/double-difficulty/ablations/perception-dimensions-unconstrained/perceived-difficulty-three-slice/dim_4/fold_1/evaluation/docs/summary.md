# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_4/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_4/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 324839 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.627578 |
| log_loss | 0.533894 |
| ece | 0.0308369 |
| brier | 0.17474 |
| accuracy | 0.762785 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.000659848 |
| probability_std | 0.118471 |
| probability_p10 | 0.599659 |
| probability_p50 | 0.784401 |
| probability_p90 | 0.903517 |
| mean_predictive_variance | 0.165421 |
| integrated_brier_score | 0.102553 |
| joint_tossup_event_log_loss | 6.90317 |
| buzz_position_mae | 0.163734 |
| buzz_position_median_absolute_error | 0.149169 |
| buzz_position_bias | -0.0735155 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.356428 |
| first_buzzer_mean_reciprocal_rank | 0.566348 |
| first_buzzer_log_loss | 1.67132 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.643572 |
| tossup_scorer_player_top1_accuracy | 0.321753 |
| tossup_scorer_team_top1_accuracy | 0.486364 |
| tossup_game_winner_accuracy | 0.779279 |
| tossup_game_margin_mae | 35.4344 |
| tournament_player_ppg_spearman | 0.652266 |
| tournament_player_ppg_mae | 9.13518 |
| tournament_player_ppg_top10_overlap | 0.665517 |
| neg_auroc | 0.627578 |
| neg_average_precision | 0.353803 |
| neg_precision | 0.511278 |
| neg_recall | 0.0628756 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0562188 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0922294 |
| no_buzz_calibration_error | 0.0763203 |
| no_buzz_brier | 0.0270267 |
| full_pmf_max_mass_error | 1.55431e-15 |
| tossup_outcome_events | 9240 |
| first_buzzer_team_top1_accuracy_events | 9093 |
| tossup_scorer_player_top1_accuracy_events | 9240 |
| tossup_scorer_team_top1_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 444 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.627578 | 0.533894 | 0.0308369 | 0.17474 | 0.762785 | 0.762125 | 0.000659848 | 0.118471 | 0.599659 | 0.784401 | 0.903517 | 0.165421 |
| tossup_correctness | tier | fall | 2842 | 0.626553 | 0.505302 | 0.0319144 | 0.162766 | 0.782899 | 0.785362 | -0.00246305 | 0.112263 | 0.62168 | 0.802065 | 0.907754 | 0.158205 |
| tossup_correctness | tier | nationals | 1564 | 0.635268 | 0.57562 | 0.0265247 | 0.193996 | 0.719949 | 0.718031 | 0.00191816 | 0.120951 | 0.532332 | 0.710015 | 0.850955 | 0.194774 |
| tossup_correctness | tier | regionals | 1937 | 0.614131 | 0.540238 | 0.0236993 | 0.178523 | 0.757873 | 0.758389 | -0.000516262 | 0.10762 | 0.59642 | 0.762815 | 0.87201 | 0.177538 |
| tossup_correctness | tier | winter | 2750 | 0.623747 | 0.535245 | 0.0434107 | 0.1735 | 0.769818 | 0.765818 | 0.004 | 0.113769 | 0.643119 | 0.822757 | 0.92483 | 0.147649 |
| tossup_correctness | category | Current Events | 126 | 0.611091 | 0.549694 | 0.113007 | 0.18242 | 0.738095 | 0.769841 | -0.031746 | 0.112759 | 0.517412 | 0.67945 | 0.815943 | 0.206168 |
| tossup_correctness | category | Fine Arts | 1071 | 0.635035 | 0.525629 | 0.0374912 | 0.171209 | 0.770308 | 0.766573 | 0.00373483 | 0.111076 | 0.629709 | 0.800458 | 0.91003 | 0.157553 |
| tossup_correctness | category | Geography | 185 | 0.712763 | 0.547858 | 0.0548782 | 0.18414 | 0.708108 | 0.697297 | 0.0108108 | 0.156254 | 0.481646 | 0.747115 | 0.882557 | 0.180546 |
| tossup_correctness | category | History | 1440 | 0.630992 | 0.540469 | 0.0328962 | 0.178832 | 0.755556 | 0.754167 | 0.00138889 | 0.125828 | 0.565157 | 0.765007 | 0.890498 | 0.174116 |
| tossup_correctness | category | Literature | 1422 | 0.575655 | 0.488866 | 0.0518001 | 0.151894 | 0.815049 | 0.814346 | 0.000703235 | 0.0964222 | 0.693642 | 0.852779 | 0.935314 | 0.130702 |
| tossup_correctness | category | Mythology | 318 | 0.68294 | 0.497736 | 0.0818727 | 0.159392 | 0.779874 | 0.789308 | -0.00943396 | 0.113732 | 0.571431 | 0.737137 | 0.86598 | 0.185354 |
| tossup_correctness | category | Other Academic | 66 | 0.548712 | 0.611204 | 0.106662 | 0.208626 | 0.742424 | 0.712121 | 0.030303 | 0.114133 | 0.52303 | 0.699795 | 0.831591 | 0.201796 |
| tossup_correctness | category | Philosophy | 311 | 0.639622 | 0.553329 | 0.078209 | 0.183409 | 0.73955 | 0.745981 | -0.00643087 | 0.11441 | 0.643512 | 0.812676 | 0.912669 | 0.154414 |
| tossup_correctness | category | Popular Culture | 102 | 0.619444 | 0.409901 | 0.122666 | 0.123888 | 0.862745 | 0.882353 | -0.0196078 | 0.122057 | 0.598324 | 0.78336 | 0.889232 | 0.167664 |
| tossup_correctness | category | Religion | 358 | 0.628403 | 0.594044 | 0.077263 | 0.201819 | 0.706704 | 0.712291 | -0.00558659 | 0.126253 | 0.600797 | 0.776771 | 0.902863 | 0.167129 |
| tossup_correctness | category | Science | 1433 | 0.644963 | 0.55133 | 0.0308876 | 0.182031 | 0.743196 | 0.738311 | 0.00488486 | 0.114183 | 0.598448 | 0.780758 | 0.89684 | 0.16806 |
| tossup_correctness | category | Social Science | 324 | 0.594743 | 0.574118 | 0.0599831 | 0.191216 | 0.737654 | 0.731481 | 0.00617284 | 0.115429 | 0.584224 | 0.755024 | 0.884706 | 0.177559 |
| tossup_correctness | category | Unknown | 1937 | 0.614131 | 0.540238 | 0.0236993 | 0.178523 | 0.757873 | 0.758389 | -0.000516262 | 0.10762 | 0.59642 | 0.762815 | 0.87201 | 0.177538 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.597164 | 0.601946 | 0.0897193 | 0.204241 | 0.694611 | 0.712575 | -0.0179641 | 0.119983 | 0.506827 | 0.706835 | 0.841641 | 0.198543 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.634958 | 0.567096 | 0.0539424 | 0.189162 | 0.735746 | 0.729167 | 0.00657895 | 0.122531 | 0.534795 | 0.720705 | 0.852968 | 0.193307 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.629159 | 0.537737 | 0.0389294 | 0.177257 | 0.755083 | 0.755083 | 0 | 0.115144 | 0.583507 | 0.763719 | 0.880512 | 0.176836 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.617986 | 0.515318 | 0.0324657 | 0.167128 | 0.778129 | 0.780942 | -0.00281294 | 0.112091 | 0.617244 | 0.79221 | 0.902768 | 0.162156 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.635355 | 0.534896 | 0.0342911 | 0.174167 | 0.76563 | 0.762029 | 0.00360065 | 0.114112 | 0.634902 | 0.81643 | 0.925254 | 0.150422 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | -1.95831 | 1.11214 | -4.48503 | -3.48978 | -2.75394 | -2.2403 | -0.714995 | -0.149138 | 0.32972 |
| player | theta_2 | 1167 | -1.49958 | 0.554374 | -3.5912 | -2.51278 | -1.83469 | -1.45335 | -1.1177 | -0.678073 | -0.15312 |
| player | theta_3 | 1167 | -1.01624 | 0.848346 | -3.64092 | -2.63395 | -1.6088 | -0.766564 | -0.327739 | -0.0438076 | 0.659403 |
| player | theta_4 | 1167 | -1.67154 | 1.07339 | -4.56668 | -3.34313 | -2.49798 | -1.81219 | -0.561741 | -0.139977 | 0.237761 |
| player | theta_norm | 1167 | 3.54547 | 0.868272 | 1.54101 | 2.27369 | 2.88441 | 3.49549 | 4.10683 | 5.08063 | 6.25819 |
| tossup | start_difficulty_d1 | 1220 | -2.37067 | 1.31418 | -4.48779 | -3.8304 | -3.27777 | -2.89526 | -1.66278 | -0.0206221 | 0.306854 |
| tossup | start_difficulty_d2 | 1220 | -1.32347 | 0.985702 | -4.18139 | -3.03212 | -2.02235 | -1.25434 | -0.466382 | 0.0652548 | 0.591546 |
| tossup | start_difficulty_d3 | 1220 | -1.02858 | 0.957569 | -3.72379 | -2.82189 | -1.7726 | -0.851489 | -0.204872 | 0.18965 | 0.889022 |
| tossup | start_difficulty_d4 | 1220 | -1.52882 | 1.47899 | -4.71466 | -4.03309 | -2.97892 | -0.922311 | -0.200342 | 0.0575771 | 0.436992 |
| tossup | end_difficulty_d1 | 1220 | -3.47339 | 1.43668 | -7.10782 | -5.29903 | -4.45859 | -3.94204 | -2.62125 | -0.982628 | -0.631473 |
| tossup | end_difficulty_d2 | 1220 | -2.39738 | 1.13349 | -9.44379 | -4.38095 | -3.14038 | -2.26484 | -1.44086 | -0.858821 | -0.269127 |
| tossup | end_difficulty_d3 | 1220 | -2.07669 | 1.07704 | -7.39716 | -3.97322 | -2.87262 | -1.87459 | -1.17971 | -0.729022 | 0.0315323 |
| tossup | end_difficulty_d4 | 1220 | -2.56857 | 1.53548 | -7.18557 | -5.19528 | -4.00152 | -1.95909 | -1.20422 | -0.90815 | -0.442193 |
| tossup | total_drop_d1 | 1220 | 1.10272 | 0.351312 | 0.534407 | 0.704273 | 0.919871 | 1.0141 | 1.2035 | 1.73846 | 3.76022 |
| tossup | total_drop_d2 | 1220 | 1.0739 | 0.295066 | 0.74818 | 0.857289 | 0.943293 | 1.01002 | 1.11985 | 1.47967 | 7.09371 |
| tossup | total_drop_d3 | 1220 | 1.04811 | 0.190367 | 0.766139 | 0.894229 | 0.957575 | 1.01137 | 1.08727 | 1.29218 | 4.34143 |
| tossup | total_drop_d4 | 1220 | 1.03974 | 0.212205 | 0.379297 | 0.771928 | 0.95206 | 1.00772 | 1.07883 | 1.38119 | 2.73317 |
| tossup | drop_share_1_d1 | 1220 | 0.354944 | 0.0462871 | 0.238734 | 0.295196 | 0.316624 | 0.353155 | 0.38586 | 0.429284 | 0.671752 |
| tossup | drop_share_2_d1 | 1220 | 0.336498 | 0.0177225 | 0.22344 | 0.308486 | 0.326053 | 0.336683 | 0.34676 | 0.362553 | 0.437724 |
| tossup | drop_share_3_d1 | 1220 | 0.308558 | 0.0429536 | 0.104808 | 0.23577 | 0.280228 | 0.311033 | 0.342038 | 0.365227 | 0.447856 |
| tossup | drop_share_1_d2 | 1220 | 0.330655 | 0.0250905 | 0.272871 | 0.298406 | 0.312663 | 0.325852 | 0.344905 | 0.377786 | 0.478558 |
| tossup | drop_share_2_d2 | 1220 | 0.344164 | 0.0110292 | 0.304614 | 0.325469 | 0.336797 | 0.344502 | 0.35158 | 0.361763 | 0.376333 |
| tossup | drop_share_3_d2 | 1220 | 0.32518 | 0.0257933 | 0.204233 | 0.277232 | 0.310273 | 0.328916 | 0.343165 | 0.360716 | 0.396075 |
| tossup | drop_share_1_d3 | 1220 | 0.326827 | 0.0245885 | 0.279094 | 0.296083 | 0.310164 | 0.322199 | 0.339094 | 0.374823 | 0.490213 |
| tossup | drop_share_2_d3 | 1220 | 0.345458 | 0.00999391 | 0.305931 | 0.329106 | 0.33887 | 0.345751 | 0.352117 | 0.36092 | 0.382067 |
| tossup | drop_share_3_d3 | 1220 | 0.327715 | 0.0236171 | 0.203857 | 0.282054 | 0.315415 | 0.331955 | 0.344557 | 0.358675 | 0.379958 |
| tossup | drop_share_1_d4 | 1220 | 0.335325 | 0.0406269 | 0.225283 | 0.297545 | 0.308184 | 0.321573 | 0.351178 | 0.421739 | 0.59836 |
| tossup | drop_share_2_d4 | 1220 | 0.341082 | 0.0168304 | 0.251412 | 0.310528 | 0.33359 | 0.343508 | 0.350638 | 0.360904 | 0.488404 |
| tossup | drop_share_3_d4 | 1220 | 0.323593 | 0.0342545 | 0.139286 | 0.252704 | 0.309348 | 0.33378 | 0.345032 | 0.359279 | 0.438303 |
| tossup | r_1 | 1220 | 0.452994 | 0.254675 | 0.0149103 | 0.0285944 | 0.227126 | 0.532685 | 0.6502 | 0.759671 | 0.880977 |
| tossup | r_2 | 1220 | 0.139463 | 0.0879907 | 0.0270833 | 0.0430101 | 0.0648047 | 0.116551 | 0.197281 | 0.302704 | 0.456032 |
| tossup | r_3 | 1220 | 0.136079 | 0.118514 | 0.012609 | 0.0252402 | 0.0477298 | 0.0997148 | 0.187594 | 0.40846 | 0.677251 |
| tossup | r_4 | 1220 | 0.271463 | 0.284185 | 0.0166366 | 0.0318315 | 0.0548188 | 0.128009 | 0.388177 | 0.804622 | 0.90543 |
| tossup | r_norm | 1220 | 0.691332 | 0.0787435 | 0.516459 | 0.569572 | 0.628056 | 0.685011 | 0.755707 | 0.821406 | 0.907574 |
