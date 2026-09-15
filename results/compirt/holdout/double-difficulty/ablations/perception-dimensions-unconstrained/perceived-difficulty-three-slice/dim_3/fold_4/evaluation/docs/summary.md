# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_3/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_3/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 316476 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.634959 |
| log_loss | 0.520132 |
| ece | 0.0367107 |
| brier | 0.169207 |
| accuracy | 0.771197 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0021575 |
| probability_std | 0.132128 |
| probability_p10 | 0.57673 |
| probability_p50 | 0.788293 |
| probability_p90 | 0.911199 |
| mean_predictive_variance | 0.163357 |
| integrated_brier_score | 0.101723 |
| joint_tossup_event_log_loss | 6.90892 |
| buzz_position_mae | 0.160406 |
| buzz_position_median_absolute_error | 0.145959 |
| buzz_position_bias | -0.0667397 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.361273 |
| first_buzzer_mean_reciprocal_rank | 0.569721 |
| first_buzzer_log_loss | 1.67062 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.645739 |
| tossup_scorer_player_top1_accuracy | 0.316951 |
| tossup_scorer_team_top1_accuracy | 0.490832 |
| tossup_game_winner_accuracy | 0.814004 |
| tossup_game_margin_mae | 33.7777 |
| tournament_player_ppg_spearman | 0.686855 |
| tournament_player_ppg_mae | 9.19128 |
| tournament_player_ppg_top10_overlap | 0.686207 |
| neg_auroc | 0.634959 |
| neg_average_precision | 0.348932 |
| neg_precision | 0.477064 |
| neg_recall | 0.0990005 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0553962 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0900601 |
| no_buzz_calibration_error | 0.0783331 |
| no_buzz_brier | 0.0244289 |
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
| tossup_correctness | aggregate | all | 9270 | 0.634959 | 0.520132 | 0.0367107 | 0.169207 | 0.771197 | 0.773355 | -0.0021575 | 0.132128 | 0.57673 | 0.788293 | 0.911199 | 0.163357 |
| tossup_correctness | tier | fall | 2876 | 0.584777 | 0.515709 | 0.0496586 | 0.164642 | 0.790682 | 0.793115 | -0.00243394 | 0.109447 | 0.656371 | 0.83346 | 0.927056 | 0.142216 |
| tossup_correctness | tier | nationals | 1579 | 0.656522 | 0.562828 | 0.0633532 | 0.189292 | 0.722609 | 0.729576 | -0.00696643 | 0.13557 | 0.482142 | 0.684173 | 0.832338 | 0.203427 |
| tossup_correctness | tier | regionals | 1990 | 0.647207 | 0.522533 | 0.02227 | 0.171157 | 0.764824 | 0.765829 | -0.00100503 | 0.129347 | 0.580911 | 0.790985 | 0.905331 | 0.163637 |
| tossup_correctness | tier | winter | 2825 | 0.656097 | 0.499077 | 0.0244841 | 0.161255 | 0.783009 | 0.783009 | 0 | 0.125489 | 0.595355 | 0.791084 | 0.909728 | 0.162286 |
| tossup_correctness | category | Current Events | 123 | 0.588775 | 0.565368 | 0.134452 | 0.189428 | 0.731707 | 0.764228 | -0.0325203 | 0.135587 | 0.473735 | 0.679739 | 0.843379 | 0.204563 |
| tossup_correctness | category | Fine Arts | 1093 | 0.61985 | 0.527796 | 0.0358497 | 0.17162 | 0.773102 | 0.769442 | 0.00365965 | 0.120123 | 0.626278 | 0.80998 | 0.916808 | 0.153468 |
| tossup_correctness | category | Geography | 191 | 0.741911 | 0.540476 | 0.0336118 | 0.180306 | 0.732984 | 0.691099 | 0.0418848 | 0.146426 | 0.485681 | 0.730905 | 0.866789 | 0.188021 |
| tossup_correctness | category | History | 1469 | 0.656844 | 0.531042 | 0.0474814 | 0.17574 | 0.748809 | 0.758339 | -0.00953029 | 0.134409 | 0.522242 | 0.734654 | 0.871757 | 0.18587 |
| tossup_correctness | category | Literature | 1436 | 0.58352 | 0.491593 | 0.059614 | 0.153159 | 0.808496 | 0.81546 | -0.00696379 | 0.11617 | 0.652698 | 0.851217 | 0.943052 | 0.133074 |
| tossup_correctness | category | Mythology | 325 | 0.609417 | 0.469194 | 0.1116 | 0.148957 | 0.806154 | 0.843077 | -0.0369231 | 0.127537 | 0.559221 | 0.755813 | 0.88562 | 0.17931 |
| tossup_correctness | category | Other Academic | 67 | 0.607817 | 0.568946 | 0.16276 | 0.188037 | 0.746269 | 0.791045 | -0.0447761 | 0.127199 | 0.491696 | 0.670311 | 0.803809 | 0.209522 |
| tossup_correctness | category | Philosophy | 322 | 0.625823 | 0.508033 | 0.0383246 | 0.163979 | 0.78882 | 0.785714 | 0.00310559 | 0.11971 | 0.612923 | 0.804426 | 0.913337 | 0.154963 |
| tossup_correctness | category | Popular Culture | 100 | 0.543412 | 0.441977 | 0.172943 | 0.134154 | 0.87 | 0.89 | -0.02 | 0.117727 | 0.563951 | 0.744495 | 0.871466 | 0.182996 |
| tossup_correctness | category | Religion | 365 | 0.634788 | 0.57903 | 0.0453322 | 0.195968 | 0.712329 | 0.723288 | -0.0109589 | 0.137157 | 0.564923 | 0.771499 | 0.898517 | 0.171154 |
| tossup_correctness | category | Science | 1456 | 0.637995 | 0.516663 | 0.0424524 | 0.167591 | 0.778846 | 0.76717 | 0.0116758 | 0.124233 | 0.605466 | 0.79992 | 0.909363 | 0.158823 |
| tossup_correctness | category | Social Science | 333 | 0.659305 | 0.552846 | 0.0207971 | 0.18548 | 0.732733 | 0.72973 | 0.003003 | 0.130072 | 0.525015 | 0.74553 | 0.864159 | 0.184688 |
| tossup_correctness | category | Unknown | 1990 | 0.647207 | 0.522533 | 0.02227 | 0.171157 | 0.764824 | 0.765829 | -0.00100503 | 0.129347 | 0.580911 | 0.790985 | 0.905331 | 0.163637 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.618076 | 0.56335 | 0.101354 | 0.187324 | 0.765363 | 0.748603 | 0.0167598 | 0.139108 | 0.484764 | 0.702642 | 0.829184 | 0.200498 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.596806 | 0.56121 | 0.0606958 | 0.187825 | 0.735632 | 0.754441 | -0.0188088 | 0.134954 | 0.510266 | 0.736188 | 0.857138 | 0.187853 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.621248 | 0.532137 | 0.0424476 | 0.174783 | 0.760781 | 0.766682 | -0.00590104 | 0.127942 | 0.559998 | 0.762615 | 0.88459 | 0.175672 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.644511 | 0.495918 | 0.0332438 | 0.15956 | 0.790799 | 0.787441 | 0.00335796 | 0.124478 | 0.606683 | 0.803466 | 0.911752 | 0.157972 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.647332 | 0.519661 | 0.0306737 | 0.167644 | 0.77108 | 0.771758 | -0.000677277 | 0.131404 | 0.594094 | 0.819112 | 0.929096 | 0.14941 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | -2.3364 | 0.711148 | -4.48459 | -3.5432 | -2.83616 | -2.29662 | -1.79753 | -1.28074 | -0.61852 |
| player | theta_2 | 1196 | -1.35583 | 0.837826 | -4.42805 | -2.79691 | -2.02743 | -1.22891 | -0.656618 | -0.23845 | 0.546848 |
| player | theta_3 | 1196 | -1.41196 | 0.976274 | -4.3333 | -3.19968 | -2.06824 | -1.36336 | -0.5293 | -0.136447 | 0.4352 |
| player | theta_norm | 1196 | 3.29476 | 0.771181 | 1.43533 | 2.12937 | 2.76343 | 3.23371 | 3.77649 | 4.65619 | 6.09251 |
| tossup | start_difficulty_d1 | 1240 | -2.42085 | 1.15946 | -5.03202 | -3.91158 | -3.35671 | -2.75946 | -1.40871 | -0.402422 | 0.310799 |
| tossup | start_difficulty_d2 | 1240 | -1.05699 | 1.25699 | -4.45852 | -3.51022 | -1.93571 | -0.529231 | -0.104826 | 0.26389 | 1.77304 |
| tossup | start_difficulty_d3 | 1240 | -1.6092 | 1.29113 | -4.79362 | -3.45154 | -2.75056 | -1.54417 | -0.360959 | 0.228267 | 1.34446 |
| tossup | end_difficulty_d1 | 1240 | -3.52217 | 1.29305 | -8.01872 | -5.40731 | -4.4676 | -3.69671 | -2.4444 | -1.36946 | -0.589431 |
| tossup | end_difficulty_d2 | 1240 | -2.09288 | 1.34368 | -8.84924 | -4.58139 | -3.1626 | -1.55133 | -1.06238 | -0.644454 | 0.958461 |
| tossup | end_difficulty_d3 | 1240 | -2.68071 | 1.43716 | -8.45799 | -4.96948 | -3.79616 | -2.60831 | -1.35244 | -0.687146 | 0.484217 |
| tossup | total_drop_d1 | 1240 | 1.10132 | 0.41311 | 0.356539 | 0.678695 | 0.891805 | 1.01538 | 1.18423 | 1.76219 | 5.12509 |
| tossup | total_drop_d2 | 1240 | 1.03589 | 0.250023 | 0.554955 | 0.783922 | 0.924923 | 0.987237 | 1.07842 | 1.42125 | 5.37181 |
| tossup | total_drop_d3 | 1240 | 1.07151 | 0.298704 | 0.590951 | 0.790079 | 0.928518 | 1.00556 | 1.10605 | 1.56592 | 4.62015 |
| tossup | drop_share_1_d1 | 1240 | 0.355845 | 0.0486403 | 0.225293 | 0.298534 | 0.321463 | 0.343431 | 0.383649 | 0.449859 | 0.587856 |
| tossup | drop_share_2_d1 | 1240 | 0.337272 | 0.0197447 | 0.2592 | 0.306084 | 0.325636 | 0.33774 | 0.348968 | 0.365123 | 0.509789 |
| tossup | drop_share_3_d1 | 1240 | 0.306883 | 0.0438144 | 0.144258 | 0.226573 | 0.28055 | 0.315572 | 0.336479 | 0.365123 | 0.449197 |
| tossup | drop_share_1_d2 | 1240 | 0.324486 | 0.0297585 | 0.239309 | 0.293405 | 0.306901 | 0.317237 | 0.332189 | 0.388964 | 0.556743 |
| tossup | drop_share_2_d2 | 1240 | 0.344119 | 0.0137552 | 0.267974 | 0.316006 | 0.337858 | 0.345736 | 0.353059 | 0.362926 | 0.4102 |
| tossup | drop_share_3_d2 | 1240 | 0.331396 | 0.027159 | 0.175282 | 0.277644 | 0.321101 | 0.336069 | 0.347302 | 0.364694 | 0.419353 |
| tossup | drop_share_1_d3 | 1240 | 0.339955 | 0.0407309 | 0.24014 | 0.294926 | 0.311146 | 0.328024 | 0.362966 | 0.414121 | 0.587662 |
| tossup | drop_share_2_d3 | 1240 | 0.341193 | 0.0144299 | 0.253499 | 0.316397 | 0.33275 | 0.341954 | 0.350036 | 0.362221 | 0.417609 |
| tossup | drop_share_3_d3 | 1240 | 0.318852 | 0.0373781 | 0.149581 | 0.246274 | 0.298592 | 0.328858 | 0.344259 | 0.36336 | 0.428789 |
| tossup | r_1 | 1240 | 0.507705 | 0.3163 | 0.0376981 | 0.0725032 | 0.192592 | 0.599922 | 0.823018 | 0.898009 | 0.963864 |
| tossup | r_2 | 1240 | 0.17942 | 0.169263 | 0.018568 | 0.035737 | 0.0613295 | 0.101526 | 0.243426 | 0.551174 | 0.812147 |
| tossup | r_3 | 1240 | 0.312875 | 0.276106 | 0.0154564 | 0.0345581 | 0.0781666 | 0.163372 | 0.584898 | 0.80016 | 0.900795 |
| tossup | r_norm | 1240 | 0.763879 | 0.0954327 | 0.578139 | 0.590411 | 0.696965 | 0.773815 | 0.841415 | 0.901906 | 0.96421 |
