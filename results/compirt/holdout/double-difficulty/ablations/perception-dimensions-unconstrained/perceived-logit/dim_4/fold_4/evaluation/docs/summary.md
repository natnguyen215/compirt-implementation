# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_4/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_4/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 335328 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.54316 |
| log_loss | 0.586609 |
| ece | 0.0914102 |
| brier | 0.184478 |
| accuracy | 0.774002 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.000647249 |
| probability_std | 0.0992816 |
| probability_p10 | 0.710682 |
| probability_p50 | 0.881654 |
| probability_p90 | 0.947451 |
| mean_predictive_variance | 0.115846 |
| integrated_brier_score | 0.173594 |
| joint_tossup_event_log_loss | 7.74645 |
| buzz_position_mae | 0.338566 |
| buzz_position_median_absolute_error | 0.341214 |
| buzz_position_bias | -0.32602 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.362567 |
| first_buzzer_mean_reciprocal_rank | 0.572675 |
| first_buzzer_log_loss | 1.65518 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.622977 |
| tossup_scorer_player_top1_accuracy | 0.262473 |
| tossup_scorer_team_top1_accuracy | 0.410874 |
| tossup_game_winner_accuracy | 0.715536 |
| tossup_game_margin_mae | 45.1475 |
| tournament_player_ppg_spearman | 0.606689 |
| tournament_player_ppg_mae | 10.6016 |
| tournament_player_ppg_top10_overlap | 0.606897 |
| neg_auroc | 0.54316 |
| neg_average_precision | 0.270853 |
| neg_precision | 0.548387 |
| neg_recall | 0.0161828 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0292503 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.235993 |
| no_buzz_calibration_error | 0.224266 |
| no_buzz_brier | 0.0723853 |
| full_pmf_max_mass_error | 1.44329e-15 |
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
| tossup_correctness | aggregate | all | 9270 | 0.54316 | 0.586609 | 0.0914102 | 0.184478 | 0.774002 | 0.773355 | 0.000647249 | 0.0992816 | 0.710682 | 0.881654 | 0.947451 | 0.115846 |
| tossup_correctness | tier | fall | 2876 | 0.528287 | 0.552649 | 0.0844034 | 0.171828 | 0.792768 | 0.793115 | -0.000347705 | 0.080875 | 0.751071 | 0.885039 | 0.94286 | 0.111589 |
| tossup_correctness | tier | nationals | 1579 | 0.570129 | 0.630534 | 0.0931723 | 0.205427 | 0.730842 | 0.729576 | 0.00126662 | 0.125549 | 0.615161 | 0.840916 | 0.94381 | 0.138727 |
| tossup_correctness | tier | regionals | 1990 | 0.525037 | 0.607291 | 0.106647 | 0.191548 | 0.767839 | 0.765829 | 0.00201005 | 0.110664 | 0.673092 | 0.873598 | 0.948461 | 0.122899 |
| tossup_correctness | tier | winter | 2825 | 0.540118 | 0.582063 | 0.102698 | 0.180668 | 0.783363 | 0.783009 | 0.000353982 | 0.0800525 | 0.761394 | 0.898137 | 0.951677 | 0.102425 |
| tossup_correctness | category | Current Events | 123 | 0.608951 | 0.56519 | 0.100529 | 0.183661 | 0.764228 | 0.764228 | 0 | 0.120373 | 0.660689 | 0.867416 | 0.94598 | 0.127536 |
| tossup_correctness | category | Fine Arts | 1093 | 0.539923 | 0.607532 | 0.110755 | 0.189553 | 0.769442 | 0.769442 | 0 | 0.0864493 | 0.76405 | 0.899878 | 0.951246 | 0.102685 |
| tossup_correctness | category | Geography | 191 | 0.674756 | 0.657304 | 0.159817 | 0.222372 | 0.685864 | 0.691099 | -0.0052356 | 0.0960906 | 0.716271 | 0.877682 | 0.936543 | 0.121949 |
| tossup_correctness | category | History | 1469 | 0.547221 | 0.601896 | 0.0985008 | 0.192511 | 0.760381 | 0.758339 | 0.00204221 | 0.0967193 | 0.695982 | 0.870013 | 0.940866 | 0.123192 |
| tossup_correctness | category | Literature | 1436 | 0.514345 | 0.527574 | 0.0856073 | 0.158817 | 0.81546 | 0.81546 | 0 | 0.0905385 | 0.742959 | 0.899194 | 0.954181 | 0.104742 |
| tossup_correctness | category | Mythology | 325 | 0.569987 | 0.446301 | 0.0571496 | 0.13406 | 0.84 | 0.843077 | -0.00307692 | 0.08525 | 0.775089 | 0.900593 | 0.944926 | 0.102412 |
| tossup_correctness | category | Other Academic | 67 | 0.551213 | 0.538916 | 0.107933 | 0.168791 | 0.80597 | 0.791045 | 0.0149254 | 0.0946071 | 0.749601 | 0.864359 | 0.939896 | 0.12001 |
| tossup_correctness | category | Philosophy | 322 | 0.496935 | 0.606809 | 0.121775 | 0.186106 | 0.785714 | 0.785714 | 0 | 0.0950077 | 0.737361 | 0.912397 | 0.951998 | 0.10015 |
| tossup_correctness | category | Popular Culture | 100 | 0.544433 | 0.369765 | 0.0329827 | 0.105231 | 0.89 | 0.89 | 0 | 0.0806838 | 0.767601 | 0.878163 | 0.941573 | 0.11211 |
| tossup_correctness | category | Religion | 365 | 0.562406 | 0.684616 | 0.14865 | 0.219803 | 0.723288 | 0.723288 | 0 | 0.0961924 | 0.74376 | 0.898121 | 0.945027 | 0.105253 |
| tossup_correctness | category | Science | 1456 | 0.559239 | 0.576862 | 0.0813924 | 0.184132 | 0.76717 | 0.76717 | 0 | 0.0987157 | 0.703266 | 0.861009 | 0.939417 | 0.12715 |
| tossup_correctness | category | Social Science | 333 | 0.517375 | 0.676154 | 0.144365 | 0.216748 | 0.72973 | 0.72973 | 0 | 0.100124 | 0.718985 | 0.882025 | 0.940121 | 0.115323 |
| tossup_correctness | category | Unknown | 1990 | 0.525037 | 0.607291 | 0.106647 | 0.191548 | 0.767839 | 0.765829 | 0.00201005 | 0.110664 | 0.673092 | 0.873598 | 0.948461 | 0.122899 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.543118 | 0.586358 | 0.0833317 | 0.187963 | 0.765363 | 0.748603 | 0.0167598 | 0.0975254 | 0.707137 | 0.831034 | 0.919455 | 0.139819 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.480044 | 0.6252 | 0.0990478 | 0.200291 | 0.752351 | 0.754441 | -0.00208986 | 0.104385 | 0.687461 | 0.849239 | 0.929806 | 0.134002 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.532876 | 0.589292 | 0.0914385 | 0.188592 | 0.763504 | 0.766682 | -0.00317749 | 0.0933768 | 0.716654 | 0.866008 | 0.935269 | 0.123692 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.561708 | 0.551667 | 0.0795907 | 0.172639 | 0.790128 | 0.787441 | 0.00268637 | 0.0958845 | 0.716797 | 0.885373 | 0.945462 | 0.113914 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.547771 | 0.607355 | 0.1084 | 0.188013 | 0.773112 | 0.771758 | 0.00135455 | 0.102074 | 0.712384 | 0.903497 | 0.956732 | 0.104605 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1196 | -1.34824 | 0.754869 | -3.20556 | -2.36792 | -1.80524 | -1.43233 | -1.00993 | -0.0479839 | 2.18875 |
| player | beta | 1196 | -3.44094 | 1.11493 | -6.85663 | -5.75573 | -4.01197 | -3.18588 | -2.59922 | -2.09654 | -1.73516 |
| player | theta_1 | 1196 | 0.848337 | 0.964954 | -2.05896 | -0.923321 | 0.208505 | 1.01429 | 1.56578 | 2.19208 | 3.60468 |
| player | theta_2 | 1196 | 0.82007 | 0.931567 | -2.65238 | -0.873842 | 0.32995 | 0.935839 | 1.43711 | 2.1784 | 3.52767 |
| player | theta_3 | 1196 | 0.836018 | 0.957789 | -2.54738 | -1.03477 | 0.285082 | 1.00477 | 1.52002 | 2.17058 | 2.9829 |
| player | theta_4 | 1196 | 0.779329 | 0.771618 | -2.23044 | -0.592582 | 0.326657 | 0.837878 | 1.31108 | 1.9494 | 3.57228 |
| player | theta_norm | 1196 | 2.36299 | 0.651191 | 0.509133 | 1.23063 | 1.94127 | 2.40265 | 2.76672 | 3.39359 | 5.24335 |
| tossup | start_difficulty_d1 | 1240 | -0.884332 | 0.385024 | -1.97522 | -1.64819 | -1.12469 | -0.798892 | -0.595075 | -0.38051 | -0.0861409 |
| tossup | start_difficulty_d2 | 1240 | -0.886299 | 0.426164 | -2.15725 | -1.65415 | -1.17792 | -0.84139 | -0.56019 | -0.260382 | -0.0763031 |
| tossup | start_difficulty_d3 | 1240 | -0.881709 | 0.502914 | -2.33367 | -1.87695 | -1.22288 | -0.750361 | -0.458603 | -0.293541 | -0.0153721 |
| tossup | start_difficulty_d4 | 1240 | -0.804451 | 0.332407 | -1.91144 | -1.39691 | -1.02358 | -0.79061 | -0.542191 | -0.31468 | -0.0603178 |
| tossup | end_difficulty_d1 | 1240 | -1.62115 | 0.303587 | -2.74334 | -2.17771 | -1.8208 | -1.58746 | -1.38922 | -1.18876 | -1.00495 |
| tossup | end_difficulty_d2 | 1240 | -1.63052 | 0.364968 | -2.76091 | -2.25309 | -1.91277 | -1.60166 | -1.33664 | -1.07498 | -0.912527 |
| tossup | end_difficulty_d3 | 1240 | -1.62636 | 0.428775 | -2.89525 | -2.42762 | -1.93304 | -1.52856 | -1.26278 | -1.09903 | -0.950423 |
| tossup | end_difficulty_d4 | 1240 | -1.57477 | 0.30805 | -2.61884 | -2.12013 | -1.78032 | -1.5598 | -1.34116 | -1.11661 | -0.876998 |
| tossup | total_drop_d1 | 1240 | 0.736818 | 0.194615 | 0.232651 | 0.360297 | 0.618592 | 0.764471 | 0.88295 | 1.01149 | 1.19508 |
| tossup | total_drop_d2 | 1240 | 0.744216 | 0.176369 | 0.247392 | 0.399438 | 0.648169 | 0.769725 | 0.86507 | 1.00047 | 1.2088 |
| tossup | total_drop_d3 | 1240 | 0.744653 | 0.189921 | 0.260111 | 0.358564 | 0.637622 | 0.784445 | 0.873993 | 0.999351 | 1.38457 |
| tossup | total_drop_d4 | 1240 | 0.770319 | 0.160064 | 0.288051 | 0.420493 | 0.702521 | 0.788497 | 0.86941 | 1.00497 | 1.26955 |
| tossup | drop_share_1_d1 | 1240 | 0.320029 | 0.0226639 | 0.21413 | 0.285369 | 0.308184 | 0.319507 | 0.331072 | 0.356426 | 0.429735 |
| tossup | drop_share_2_d1 | 1240 | 0.326823 | 0.0183568 | 0.248718 | 0.288641 | 0.317543 | 0.33038 | 0.33952 | 0.350543 | 0.368077 |
| tossup | drop_share_3_d1 | 1240 | 0.353148 | 0.028607 | 0.262595 | 0.318293 | 0.336247 | 0.348016 | 0.36394 | 0.411074 | 0.51528 |
| tossup | drop_share_1_d2 | 1240 | 0.319798 | 0.0215235 | 0.216496 | 0.287515 | 0.307488 | 0.318673 | 0.331788 | 0.355041 | 0.41269 |
| tossup | drop_share_2_d2 | 1240 | 0.327822 | 0.0167807 | 0.244701 | 0.295166 | 0.319067 | 0.330459 | 0.339315 | 0.350342 | 0.364844 |
| tossup | drop_share_3_d2 | 1240 | 0.35238 | 0.0256226 | 0.266552 | 0.31892 | 0.33657 | 0.348654 | 0.36308 | 0.40069 | 0.478638 |
| tossup | drop_share_1_d3 | 1240 | 0.32233 | 0.0246915 | 0.231149 | 0.290235 | 0.306819 | 0.318565 | 0.33394 | 0.368824 | 0.448212 |
| tossup | drop_share_2_d3 | 1240 | 0.328891 | 0.0160553 | 0.272824 | 0.296437 | 0.32081 | 0.331404 | 0.339977 | 0.351133 | 0.366367 |
| tossup | drop_share_3_d3 | 1240 | 0.348779 | 0.0245744 | 0.257551 | 0.311148 | 0.334592 | 0.348013 | 0.361318 | 0.390722 | 0.451152 |
| tossup | drop_share_1_d4 | 1240 | 0.318325 | 0.0206944 | 0.206687 | 0.287319 | 0.308063 | 0.319038 | 0.330037 | 0.348777 | 0.413363 |
| tossup | drop_share_2_d4 | 1240 | 0.330042 | 0.0154139 | 0.26064 | 0.300625 | 0.323307 | 0.332191 | 0.340201 | 0.350799 | 0.363476 |
| tossup | drop_share_3_d4 | 1240 | 0.351633 | 0.0269116 | 0.273096 | 0.320183 | 0.336277 | 0.347345 | 0.35981 | 0.407247 | 0.506706 |
| tossup | r_1 | 1240 | 0.254881 | 0.213383 | 0.031997 | 0.0647312 | 0.108944 | 0.164649 | 0.315251 | 0.761363 | 0.874965 |
| tossup | r_2 | 1240 | 0.260567 | 0.202021 | 0.0368272 | 0.0586568 | 0.103851 | 0.185396 | 0.378264 | 0.687585 | 0.876384 |
| tossup | r_3 | 1240 | 0.269466 | 0.202719 | 0.0315619 | 0.0589043 | 0.11208 | 0.191996 | 0.385074 | 0.707918 | 0.855613 |
| tossup | r_4 | 1240 | 0.215087 | 0.147543 | 0.0338504 | 0.0583252 | 0.109513 | 0.179727 | 0.273386 | 0.522554 | 0.861126 |
| tossup | r_norm | 1240 | 0.625777 | 0.0960887 | 0.501427 | 0.51323 | 0.544535 | 0.599678 | 0.691327 | 0.809075 | 0.879335 |
