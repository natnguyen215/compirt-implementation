# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_5/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_5/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 317209 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.660993 |
| log_loss | 0.521095 |
| ece | 0.0243588 |
| brier | 0.169868 |
| accuracy | 0.769493 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00736831 |
| probability_std | 0.131215 |
| probability_p10 | 0.568785 |
| probability_p50 | 0.777911 |
| probability_p90 | 0.905257 |
| mean_predictive_variance | 0.167145 |
| integrated_brier_score | 0.100994 |
| joint_tossup_event_log_loss | 6.88409 |
| buzz_position_mae | 0.161706 |
| buzz_position_median_absolute_error | 0.148941 |
| buzz_position_bias | -0.0706284 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.336083 |
| first_buzzer_mean_reciprocal_rank | 0.552232 |
| first_buzzer_log_loss | 1.69588 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.639283 |
| tossup_scorer_player_top1_accuracy | 0.320563 |
| tossup_scorer_team_top1_accuracy | 0.49632 |
| tossup_game_winner_accuracy | 0.772523 |
| tossup_game_margin_mae | 34.6393 |
| tournament_player_ppg_spearman | 0.665417 |
| tournament_player_ppg_mae | 9.06091 |
| tournament_player_ppg_top10_overlap | 0.658621 |
| neg_auroc | 0.660993 |
| neg_average_precision | 0.393437 |
| neg_precision | 0.578824 |
| neg_recall | 0.113731 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0559355 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0908255 |
| no_buzz_calibration_error | 0.0749164 |
| no_buzz_brier | 0.0265576 |
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
| tossup_correctness | aggregate | all | 9093 | 0.660993 | 0.521095 | 0.0243588 | 0.169868 | 0.769493 | 0.762125 | 0.00736831 | 0.131215 | 0.568785 | 0.777911 | 0.905257 | 0.167145 |
| tossup_correctness | tier | fall | 2842 | 0.686361 | 0.48099 | 0.0145304 | 0.154781 | 0.793807 | 0.785362 | 0.00844476 | 0.122273 | 0.599869 | 0.80185 | 0.910584 | 0.158879 |
| tossup_correctness | tier | nationals | 1564 | 0.665391 | 0.564173 | 0.0312644 | 0.188201 | 0.732097 | 0.718031 | 0.0140665 | 0.138756 | 0.512065 | 0.719663 | 0.870199 | 0.189165 |
| tossup_correctness | tier | regionals | 1937 | 0.629314 | 0.536966 | 0.0353697 | 0.177142 | 0.762003 | 0.758389 | 0.00361384 | 0.121124 | 0.555854 | 0.747856 | 0.869046 | 0.183431 |
| tossup_correctness | tier | winter | 2750 | 0.649232 | 0.526863 | 0.0286635 | 0.169911 | 0.770909 | 0.765818 | 0.00509091 | 0.129659 | 0.601409 | 0.811021 | 0.929096 | 0.151694 |
| tossup_correctness | category | Current Events | 126 | 0.713473 | 0.516056 | 0.102551 | 0.166859 | 0.777778 | 0.769841 | 0.00793651 | 0.123187 | 0.510124 | 0.689671 | 0.839332 | 0.201378 |
| tossup_correctness | category | Fine Arts | 1071 | 0.670899 | 0.511094 | 0.0262634 | 0.16656 | 0.776844 | 0.766573 | 0.0102708 | 0.132183 | 0.584865 | 0.789848 | 0.913389 | 0.162854 |
| tossup_correctness | category | Geography | 185 | 0.742248 | 0.533673 | 0.0563856 | 0.177775 | 0.756757 | 0.697297 | 0.0594595 | 0.159887 | 0.445551 | 0.698617 | 0.850097 | 0.19686 |
| tossup_correctness | category | History | 1440 | 0.677532 | 0.519079 | 0.0139521 | 0.170707 | 0.765972 | 0.754167 | 0.0118056 | 0.125953 | 0.566539 | 0.772895 | 0.890036 | 0.171488 |
| tossup_correctness | category | Literature | 1422 | 0.59927 | 0.490748 | 0.0485498 | 0.1507 | 0.811533 | 0.814346 | -0.00281294 | 0.112466 | 0.671736 | 0.854948 | 0.950605 | 0.127233 |
| tossup_correctness | category | Mythology | 318 | 0.711839 | 0.476484 | 0.0496259 | 0.152815 | 0.789308 | 0.789308 | 0 | 0.119317 | 0.5802 | 0.766135 | 0.885218 | 0.174225 |
| tossup_correctness | category | Other Academic | 66 | 0.675252 | 0.555038 | 0.0760738 | 0.185981 | 0.772727 | 0.712121 | 0.0606061 | 0.12209 | 0.524878 | 0.729029 | 0.858168 | 0.193605 |
| tossup_correctness | category | Philosophy | 311 | 0.684199 | 0.530293 | 0.0534098 | 0.175717 | 0.749196 | 0.745981 | 0.00321543 | 0.115067 | 0.646221 | 0.817044 | 0.914209 | 0.153064 |
| tossup_correctness | category | Popular Culture | 102 | 0.622222 | 0.415623 | 0.137096 | 0.124358 | 0.862745 | 0.882353 | -0.0196078 | 0.117618 | 0.616642 | 0.76136 | 0.877627 | 0.176015 |
| tossup_correctness | category | Religion | 358 | 0.678508 | 0.563945 | 0.0480872 | 0.189418 | 0.726257 | 0.712291 | 0.0139665 | 0.128628 | 0.54818 | 0.765584 | 0.886381 | 0.176282 |
| tossup_correctness | category | Science | 1433 | 0.672348 | 0.538432 | 0.0204995 | 0.178615 | 0.74529 | 0.738311 | 0.00697837 | 0.138124 | 0.539565 | 0.773294 | 0.896294 | 0.171308 |
| tossup_correctness | category | Social Science | 324 | 0.68951 | 0.533422 | 0.0298179 | 0.176256 | 0.75 | 0.731481 | 0.0185185 | 0.120079 | 0.562849 | 0.75902 | 0.86794 | 0.17944 |
| tossup_correctness | category | Unknown | 1937 | 0.629314 | 0.536966 | 0.0353697 | 0.177142 | 0.762003 | 0.758389 | 0.00361384 | 0.121124 | 0.555854 | 0.747856 | 0.869046 | 0.183431 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.605917 | 0.59049 | 0.0699811 | 0.199953 | 0.712575 | 0.712575 | 0 | 0.121136 | 0.531335 | 0.702323 | 0.837223 | 0.199241 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.677788 | 0.545774 | 0.0408008 | 0.180743 | 0.751096 | 0.729167 | 0.0219298 | 0.136748 | 0.496736 | 0.723722 | 0.856879 | 0.191539 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.669699 | 0.521935 | 0.0206309 | 0.171603 | 0.76643 | 0.755083 | 0.0113475 | 0.126359 | 0.566538 | 0.764521 | 0.886617 | 0.17492 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.654552 | 0.50314 | 0.0264095 | 0.163003 | 0.779887 | 0.780942 | -0.00105485 | 0.125375 | 0.588748 | 0.788415 | 0.904932 | 0.163333 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.657385 | 0.526068 | 0.0263288 | 0.170167 | 0.77054 | 0.762029 | 0.00851064 | 0.131723 | 0.588334 | 0.800092 | 0.926293 | 0.156276 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | -1.25363 | 1.39594 | -4.88331 | -3.7442 | -2.64653 | -0.317619 | -0.158216 | -0.00926701 | 0.521679 |
| player | theta_2 | 1167 | -2.1351 | 1.17021 | -5.21032 | -3.67927 | -2.96778 | -2.41284 | -1.15119 | -0.14939 | 1.7446 |
| player | theta_3 | 1167 | -0.243744 | 0.317595 | -1.71528 | -0.700465 | -0.413802 | -0.24942 | -0.112836 | 0.308721 | 1.39969 |
| player | theta_4 | 1167 | -0.26597 | 0.399563 | -1.73695 | -0.915684 | -0.484651 | -0.254998 | -0.0860907 | 0.431188 | 1.96573 |
| player | theta_5 | 1167 | -0.251258 | 0.297289 | -1.87383 | -0.75728 | -0.389156 | -0.23265 | -0.108979 | 0.196785 | 1.23991 |
| player | theta_norm | 1167 | 3.06425 | 0.773428 | 1.3635 | 1.97362 | 2.49366 | 2.97812 | 3.56042 | 4.43997 | 5.88891 |
| tossup | start_difficulty_d1 | 1220 | -1.79628 | 1.64462 | -4.6368 | -3.87938 | -3.32798 | -2.59796 | -0.0396071 | 0.173819 | 0.494783 |
| tossup | start_difficulty_d2 | 1220 | -1.79379 | 1.89301 | -5.91779 | -4.47311 | -3.70683 | -0.722778 | 0.0140994 | 0.247074 | 1.28976 |
| tossup | start_difficulty_d3 | 1220 | -0.0148783 | 0.345713 | -1.93524 | -0.695545 | -0.106433 | 0.0469742 | 0.177497 | 0.383378 | 0.772455 |
| tossup | start_difficulty_d4 | 1220 | -0.0383516 | 0.397777 | -1.9029 | -0.896172 | -0.166042 | 0.0494615 | 0.211132 | 0.41873 | 0.832322 |
| tossup | start_difficulty_d5 | 1220 | -0.0168602 | 0.38144 | -2.09749 | -0.8243 | -0.121592 | 0.0532485 | 0.19398 | 0.413885 | 0.807617 |
| tossup | end_difficulty_d1 | 1220 | -2.93454 | 1.84674 | -9.45213 | -5.58194 | -4.56571 | -3.45108 | -1.0334 | -0.787122 | -0.463199 |
| tossup | end_difficulty_d2 | 1220 | -2.86286 | 2.02538 | -10.099 | -5.99722 | -4.72017 | -1.85628 | -0.974839 | -0.68558 | 0.512763 |
| tossup | end_difficulty_d3 | 1220 | -1.01691 | 0.424693 | -3.29423 | -1.78775 | -1.12877 | -0.938529 | -0.784712 | -0.544737 | -0.135324 |
| tossup | end_difficulty_d4 | 1220 | -1.04455 | 0.481073 | -3.30702 | -2.0421 | -1.1974 | -0.930309 | -0.74776 | -0.490739 | 0.0250918 |
| tossup | end_difficulty_d5 | 1220 | -1.01827 | 0.47042 | -3.55 | -1.95038 | -1.13332 | -0.927388 | -0.757435 | -0.508813 | -0.0913205 |
| tossup | total_drop_d1 | 1220 | 1.13826 | 0.441068 | 0.534496 | 0.764131 | 0.947752 | 1.00524 | 1.16626 | 1.99333 | 6.50854 |
| tossup | total_drop_d2 | 1220 | 1.06907 | 0.432375 | 0.371808 | 0.652254 | 0.916413 | 0.986661 | 1.07608 | 1.85538 | 6.27062 |
| tossup | total_drop_d3 | 1220 | 1.00203 | 0.0942579 | 0.821525 | 0.905347 | 0.952532 | 0.984859 | 1.0285 | 1.12997 | 2.08225 |
| tossup | total_drop_d4 | 1220 | 1.0062 | 0.0944799 | 0.80723 | 0.894429 | 0.948314 | 0.988374 | 1.03633 | 1.18274 | 1.62658 |
| tossup | total_drop_d5 | 1220 | 1.00141 | 0.0993916 | 0.829728 | 0.89434 | 0.947519 | 0.983972 | 1.02931 | 1.16133 | 1.81495 |
| tossup | drop_share_1_d1 | 1220 | 0.346714 | 0.0499721 | 0.231603 | 0.292554 | 0.30579 | 0.327383 | 0.382947 | 0.43451 | 0.577511 |
| tossup | drop_share_2_d1 | 1220 | 0.341221 | 0.017347 | 0.274992 | 0.312006 | 0.331367 | 0.341757 | 0.351891 | 0.364037 | 0.472855 |
| tossup | drop_share_3_d1 | 1220 | 0.312065 | 0.0451809 | 0.147497 | 0.230865 | 0.277713 | 0.329225 | 0.347068 | 0.362805 | 0.423232 |
| tossup | drop_share_1_d2 | 1220 | 0.337605 | 0.0585199 | 0.194259 | 0.284938 | 0.303002 | 0.315484 | 0.361339 | 0.452154 | 0.716651 |
| tossup | drop_share_2_d2 | 1220 | 0.339208 | 0.0241295 | 0.185476 | 0.299168 | 0.327871 | 0.341496 | 0.351753 | 0.371093 | 0.523148 |
| tossup | drop_share_3_d2 | 1220 | 0.323188 | 0.0499677 | 0.0978723 | 0.21793 | 0.306252 | 0.339547 | 0.352271 | 0.375829 | 0.470264 |
| tossup | drop_share_1_d3 | 1220 | 0.305909 | 0.0118399 | 0.271159 | 0.28692 | 0.298076 | 0.30551 | 0.313094 | 0.325181 | 0.374932 |
| tossup | drop_share_2_d3 | 1220 | 0.347118 | 0.0112071 | 0.307656 | 0.329522 | 0.339383 | 0.346915 | 0.354525 | 0.365535 | 0.391223 |
| tossup | drop_share_3_d3 | 1220 | 0.346973 | 0.0128073 | 0.298285 | 0.32527 | 0.339729 | 0.34751 | 0.355057 | 0.367616 | 0.384599 |
| tossup | drop_share_1_d4 | 1220 | 0.306637 | 0.0118242 | 0.27519 | 0.288708 | 0.298491 | 0.305882 | 0.314051 | 0.326622 | 0.372848 |
| tossup | drop_share_2_d4 | 1220 | 0.347602 | 0.0105109 | 0.320167 | 0.330122 | 0.340563 | 0.347213 | 0.354397 | 0.364948 | 0.385122 |
| tossup | drop_share_3_d4 | 1220 | 0.345762 | 0.012844 | 0.286523 | 0.323286 | 0.338095 | 0.346262 | 0.35486 | 0.365073 | 0.380473 |
| tossup | drop_share_1_d5 | 1220 | 0.306732 | 0.0126021 | 0.270035 | 0.287476 | 0.298555 | 0.305437 | 0.314047 | 0.327931 | 0.362434 |
| tossup | drop_share_2_d5 | 1220 | 0.346948 | 0.0112012 | 0.311119 | 0.328971 | 0.339089 | 0.346826 | 0.354904 | 0.364905 | 0.385484 |
| tossup | drop_share_3_d5 | 1220 | 0.34632 | 0.0133757 | 0.27575 | 0.324841 | 0.338305 | 0.347015 | 0.355568 | 0.366036 | 0.387298 |
| tossup | r_1 | 1220 | 0.398866 | 0.336016 | 0.0100664 | 0.0235794 | 0.0369226 | 0.579273 | 0.714673 | 0.807829 | 0.883087 |
| tossup | r_2 | 1220 | 0.405918 | 0.361535 | 0.0266971 | 0.039881 | 0.0638484 | 0.148766 | 0.790383 | 0.891487 | 0.962588 |
| tossup | r_3 | 1220 | 0.0599385 | 0.0333689 | 0.00868401 | 0.0228595 | 0.0398277 | 0.0538037 | 0.0710254 | 0.119395 | 0.259305 |
| tossup | r_4 | 1220 | 0.0702416 | 0.042986 | 0.00898229 | 0.0261854 | 0.0413642 | 0.0586007 | 0.0845552 | 0.164917 | 0.26624 |
| tossup | r_5 | 1220 | 0.065036 | 0.0340427 | 0.00967904 | 0.0271901 | 0.0439254 | 0.0578445 | 0.0759402 | 0.132748 | 0.263932 |
| tossup | r_norm | 1220 | 0.760099 | 0.0800307 | 0.54784 | 0.631425 | 0.701688 | 0.757259 | 0.818043 | 0.89324 | 0.962771 |
