# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_4/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_4/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 336832 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.539079 |
| log_loss | 0.596175 |
| ece | 0.0962202 |
| brier | 0.187444 |
| accuracy | 0.769163 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | -0.000881057 |
| probability_std | 0.101623 |
| probability_p10 | 0.700639 |
| probability_p50 | 0.882233 |
| probability_p90 | 0.947665 |
| mean_predictive_variance | 0.11601 |
| integrated_brier_score | 0.175777 |
| joint_tossup_event_log_loss | 7.72459 |
| buzz_position_mae | 0.342079 |
| buzz_position_median_absolute_error | 0.344064 |
| buzz_position_bias | -0.329265 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.368833 |
| first_buzzer_mean_reciprocal_rank | 0.579789 |
| first_buzzer_log_loss | 1.6394 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.635242 |
| tossup_scorer_player_top1_accuracy | 0.263666 |
| tossup_scorer_team_top1_accuracy | 0.419089 |
| tossup_game_winner_accuracy | 0.699115 |
| tossup_game_margin_mae | 46.681 |
| tournament_player_ppg_spearman | 0.601576 |
| tournament_player_ppg_mae | 10.486 |
| tournament_player_ppg_top10_overlap | 0.593103 |
| neg_auroc | 0.539079 |
| neg_average_precision | 0.271709 |
| neg_precision | 0.439394 |
| neg_recall | 0.0138889 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0288114 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.231462 |
| no_buzz_calibration_error | 0.216278 |
| no_buzz_brier | 0.07077 |
| full_pmf_max_mass_error | 1.44329e-15 |
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
| tossup_correctness | aggregate | all | 9080 | 0.539079 | 0.596175 | 0.0962202 | 0.187444 | 0.769163 | 0.770044 | -0.000881057 | 0.101623 | 0.700639 | 0.882233 | 0.947665 | 0.11601 |
| tossup_correctness | tier | fall | 2817 | 0.52839 | 0.571958 | 0.0912015 | 0.180738 | 0.779198 | 0.781683 | -0.00248491 | 0.0898284 | 0.722762 | 0.876802 | 0.938039 | 0.118713 |
| tossup_correctness | tier | nationals | 1542 | 0.592086 | 0.607189 | 0.0833278 | 0.198862 | 0.732815 | 0.73476 | -0.00194553 | 0.128809 | 0.613348 | 0.837094 | 0.93878 | 0.142562 |
| tossup_correctness | tier | regionals | 1934 | 0.531331 | 0.629518 | 0.109681 | 0.197628 | 0.75698 | 0.75698 | 0 | 0.106148 | 0.680839 | 0.884237 | 0.952545 | 0.116352 |
| tossup_correctness | tier | winter | 2787 | 0.505031 | 0.591419 | 0.109761 | 0.180838 | 0.787585 | 0.786868 | 0.000717618 | 0.0787929 | 0.782998 | 0.90222 | 0.954349 | 0.09835 |
| tossup_correctness | category | Current Events | 125 | 0.623157 | 0.653269 | 0.151016 | 0.221636 | 0.696 | 0.704 | -0.008 | 0.111177 | 0.645577 | 0.856904 | 0.91743 | 0.134137 |
| tossup_correctness | category | Fine Arts | 1072 | 0.538812 | 0.607174 | 0.114876 | 0.190584 | 0.771455 | 0.770522 | 0.000932836 | 0.0929599 | 0.726039 | 0.900362 | 0.950831 | 0.105691 |
| tossup_correctness | category | Geography | 185 | 0.584895 | 0.681679 | 0.144259 | 0.221721 | 0.713514 | 0.702703 | 0.0108108 | 0.100578 | 0.7051 | 0.876161 | 0.933147 | 0.119502 |
| tossup_correctness | category | History | 1443 | 0.56328 | 0.583194 | 0.0795932 | 0.185881 | 0.765073 | 0.765073 | 0 | 0.105275 | 0.673424 | 0.865423 | 0.941281 | 0.125735 |
| tossup_correctness | category | Literature | 1411 | 0.496628 | 0.53727 | 0.0835873 | 0.161708 | 0.810064 | 0.81219 | -0.00212615 | 0.0953645 | 0.73669 | 0.893055 | 0.952996 | 0.108159 |
| tossup_correctness | category | Mythology | 320 | 0.532093 | 0.556411 | 0.0884982 | 0.17235 | 0.790625 | 0.79375 | -0.003125 | 0.0955609 | 0.741726 | 0.899962 | 0.945135 | 0.107659 |
| tossup_correctness | category | Other Academic | 64 | 0.596354 | 0.607419 | 0.155874 | 0.201397 | 0.734375 | 0.75 | -0.015625 | 0.122827 | 0.619535 | 0.858374 | 0.945659 | 0.130971 |
| tossup_correctness | category | Philosophy | 312 | 0.463935 | 0.578534 | 0.121801 | 0.174281 | 0.801282 | 0.801282 | 0 | 0.0918466 | 0.740223 | 0.901241 | 0.954486 | 0.103064 |
| tossup_correctness | category | Popular Culture | 104 | 0.509943 | 0.466765 | 0.0680842 | 0.137822 | 0.836538 | 0.846154 | -0.00961538 | 0.0768128 | 0.761732 | 0.891941 | 0.940162 | 0.108094 |
| tossup_correctness | category | Religion | 358 | 0.538383 | 0.690598 | 0.151065 | 0.219632 | 0.726257 | 0.726257 | 0 | 0.104292 | 0.711351 | 0.899119 | 0.948794 | 0.108815 |
| tossup_correctness | category | Science | 1431 | 0.563739 | 0.578421 | 0.0844328 | 0.185665 | 0.7645 | 0.765199 | -0.000698812 | 0.101573 | 0.696633 | 0.860631 | 0.938567 | 0.126979 |
| tossup_correctness | category | Social Science | 321 | 0.502296 | 0.674623 | 0.154556 | 0.215846 | 0.735202 | 0.744548 | -0.00934579 | 0.0966685 | 0.724825 | 0.890246 | 0.942478 | 0.109749 |
| tossup_correctness | category | Unknown | 1934 | 0.531331 | 0.629518 | 0.109681 | 0.197628 | 0.75698 | 0.75698 | 0 | 0.106148 | 0.680839 | 0.884237 | 0.952545 | 0.116352 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.493181 | 0.702019 | 0.137148 | 0.231239 | 0.697917 | 0.697917 | 0 | 0.0977786 | 0.664321 | 0.832423 | 0.921117 | 0.142329 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.517136 | 0.640083 | 0.108421 | 0.209073 | 0.728909 | 0.733408 | -0.00449944 | 0.104177 | 0.671606 | 0.844686 | 0.926808 | 0.13772 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.499659 | 0.621461 | 0.1044 | 0.197933 | 0.756109 | 0.759276 | -0.00316742 | 0.0995009 | 0.698096 | 0.868843 | 0.937368 | 0.124712 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.546532 | 0.55458 | 0.0847748 | 0.173129 | 0.790171 | 0.789125 | 0.00104566 | 0.0979624 | 0.707462 | 0.883621 | 0.944324 | 0.115396 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.557402 | 0.597578 | 0.102501 | 0.184105 | 0.775342 | 0.775342 | 0 | 0.101594 | 0.710758 | 0.907307 | 0.95803 | 0.101687 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1133 | -1.33546 | 0.758404 | -3.20087 | -2.35404 | -1.78381 | -1.41204 | -1.00244 | -0.0413837 | 2.30013 |
| player | beta | 1133 | -3.469 | 1.13047 | -6.88456 | -5.88098 | -4.01381 | -3.23831 | -2.60351 | -2.09095 | -1.70455 |
| player | theta_1 | 1133 | 0.840827 | 0.936755 | -2.32319 | -0.944324 | 0.261122 | 1.00773 | 1.51424 | 2.14766 | 3.19564 |
| player | theta_2 | 1133 | 0.820789 | 0.991525 | -3.07581 | -0.878363 | 0.205601 | 0.90338 | 1.48083 | 2.34241 | 3.7887 |
| player | theta_3 | 1133 | 0.822096 | 0.956558 | -2.37509 | -1.03271 | 0.279447 | 0.975508 | 1.4908 | 2.13276 | 3.69029 |
| player | theta_4 | 1133 | 0.756988 | 0.769727 | -1.81266 | -0.691839 | 0.297804 | 0.806392 | 1.28017 | 1.90934 | 3.69163 |
| player | theta_norm | 1133 | 2.35651 | 0.664777 | 0.395127 | 1.21621 | 1.93788 | 2.36356 | 2.77754 | 3.40712 | 5.26085 |
| tossup | start_difficulty_d1 | 1240 | -0.875446 | 0.387664 | -2.08081 | -1.65879 | -1.12232 | -0.795537 | -0.582847 | -0.371125 | -0.166145 |
| tossup | start_difficulty_d2 | 1240 | -0.882715 | 0.43424 | -2.04795 | -1.68351 | -1.18859 | -0.831887 | -0.537835 | -0.263294 | -0.0326683 |
| tossup | start_difficulty_d3 | 1240 | -0.877919 | 0.511957 | -2.36362 | -1.86044 | -1.23139 | -0.739188 | -0.441909 | -0.266747 | -0.0812631 |
| tossup | start_difficulty_d4 | 1240 | -0.793381 | 0.322871 | -2.01308 | -1.40766 | -0.991415 | -0.770688 | -0.552226 | -0.319091 | -0.112648 |
| tossup | end_difficulty_d1 | 1240 | -1.61639 | 0.304537 | -2.61616 | -2.17123 | -1.81161 | -1.5818 | -1.37868 | -1.17902 | -1.00205 |
| tossup | end_difficulty_d2 | 1240 | -1.62663 | 0.370302 | -2.79832 | -2.26187 | -1.90103 | -1.58515 | -1.33024 | -1.09084 | -0.837823 |
| tossup | end_difficulty_d3 | 1240 | -1.62364 | 0.436314 | -3.15932 | -2.44001 | -1.91513 | -1.52277 | -1.26487 | -1.09558 | -0.887372 |
| tossup | end_difficulty_d4 | 1240 | -1.56647 | 0.293758 | -2.48709 | -2.09797 | -1.76006 | -1.54878 | -1.34781 | -1.12623 | -0.881279 |
| tossup | total_drop_d1 | 1240 | 0.740945 | 0.194423 | 0.239444 | 0.363172 | 0.618923 | 0.772694 | 0.888476 | 1.00281 | 1.18042 |
| tossup | total_drop_d2 | 1240 | 0.743912 | 0.177079 | 0.256925 | 0.392253 | 0.644521 | 0.76733 | 0.865056 | 0.991843 | 1.26149 |
| tossup | total_drop_d3 | 1240 | 0.745723 | 0.190297 | 0.247402 | 0.364677 | 0.646402 | 0.788965 | 0.877812 | 0.994012 | 1.26005 |
| tossup | total_drop_d4 | 1240 | 0.773084 | 0.160685 | 0.292116 | 0.451431 | 0.693241 | 0.792325 | 0.880573 | 1.00045 | 1.2128 |
| tossup | drop_share_1_d1 | 1240 | 0.319552 | 0.0216872 | 0.226212 | 0.286267 | 0.307764 | 0.319023 | 0.330095 | 0.354296 | 0.431724 |
| tossup | drop_share_2_d1 | 1240 | 0.327138 | 0.0183432 | 0.253253 | 0.289441 | 0.31843 | 0.330339 | 0.339876 | 0.350885 | 0.367532 |
| tossup | drop_share_3_d1 | 1240 | 0.35331 | 0.0279762 | 0.273228 | 0.319728 | 0.336527 | 0.348404 | 0.363834 | 0.410739 | 0.491784 |
| tossup | drop_share_1_d2 | 1240 | 0.318733 | 0.0211828 | 0.232209 | 0.285899 | 0.307228 | 0.318375 | 0.330471 | 0.354262 | 0.402937 |
| tossup | drop_share_2_d2 | 1240 | 0.327701 | 0.0173102 | 0.249169 | 0.292609 | 0.318758 | 0.330604 | 0.339441 | 0.350886 | 0.364799 |
| tossup | drop_share_3_d2 | 1240 | 0.353566 | 0.0264569 | 0.277148 | 0.319753 | 0.33674 | 0.349907 | 0.364001 | 0.403907 | 0.497922 |
| tossup | drop_share_1_d3 | 1240 | 0.321786 | 0.0246579 | 0.217214 | 0.291113 | 0.306063 | 0.318297 | 0.332445 | 0.37 | 0.443955 |
| tossup | drop_share_2_d3 | 1240 | 0.329032 | 0.0162773 | 0.271815 | 0.296298 | 0.321305 | 0.33154 | 0.340212 | 0.351207 | 0.36709 |
| tossup | drop_share_3_d3 | 1240 | 0.349181 | 0.024758 | 0.26118 | 0.31225 | 0.335814 | 0.34776 | 0.361067 | 0.39113 | 0.478366 |
| tossup | drop_share_1_d4 | 1240 | 0.318343 | 0.0201774 | 0.209878 | 0.287536 | 0.307563 | 0.318678 | 0.329616 | 0.349322 | 0.423987 |
| tossup | drop_share_2_d4 | 1240 | 0.330357 | 0.0149432 | 0.266581 | 0.302079 | 0.322905 | 0.332214 | 0.34053 | 0.351098 | 0.363095 |
| tossup | drop_share_3_d4 | 1240 | 0.3513 | 0.0252506 | 0.265294 | 0.319465 | 0.336296 | 0.347447 | 0.360494 | 0.400522 | 0.491695 |
| tossup | r_1 | 1240 | 0.246426 | 0.206838 | 0.0352147 | 0.0656764 | 0.111745 | 0.161816 | 0.294939 | 0.754092 | 0.888004 |
| tossup | r_2 | 1240 | 0.269858 | 0.211099 | 0.0320587 | 0.0558641 | 0.10459 | 0.18995 | 0.406601 | 0.707778 | 0.880181 |
| tossup | r_3 | 1240 | 0.271772 | 0.204344 | 0.033614 | 0.0600903 | 0.109172 | 0.194577 | 0.402492 | 0.701026 | 0.837733 |
| tossup | r_4 | 1240 | 0.211944 | 0.145941 | 0.0360227 | 0.0571534 | 0.108235 | 0.175059 | 0.268454 | 0.529129 | 0.831874 |
| tossup | r_norm | 1240 | 0.627466 | 0.09435 | 0.500448 | 0.512334 | 0.550913 | 0.603967 | 0.693088 | 0.811324 | 0.890379 |
