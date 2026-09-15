# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_2/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_2/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 2 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 332904 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.550922 |
| log_loss | 0.620449 |
| ece | 0.11605 |
| brier | 0.194082 |
| accuracy | 0.764178 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0 |
| probability_std | 0.0883224 |
| probability_p10 | 0.753773 |
| probability_p50 | 0.89884 |
| probability_p90 | 0.956099 |
| mean_predictive_variance | 0.102682 |
| integrated_brier_score | 0.173534 |
| joint_tossup_event_log_loss | 7.78943 |
| buzz_position_mae | 0.340517 |
| buzz_position_median_absolute_error | 0.343783 |
| buzz_position_bias | -0.327752 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.340499 |
| first_buzzer_mean_reciprocal_rank | 0.558183 |
| first_buzzer_log_loss | 1.67303 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.63876 |
| tossup_scorer_player_top1_accuracy | 0.266738 |
| tossup_scorer_team_top1_accuracy | 0.417804 |
| tossup_game_winner_accuracy | 0.719565 |
| tossup_game_margin_mae | 45.5193 |
| tournament_player_ppg_spearman | 0.639253 |
| tournament_player_ppg_mae | 9.89492 |
| tournament_player_ppg_top10_overlap | 0.6 |
| neg_auroc | 0.550922 |
| neg_average_precision | 0.274118 |
| neg_precision | 0.5 |
| neg_recall | 0.0032066 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0287908 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.235452 |
| no_buzz_calibration_error | 0.222339 |
| no_buzz_brier | 0.0713256 |
| full_pmf_max_mass_error | 1.55431e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9257 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 460 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.550922 | 0.620449 | 0.11605 | 0.194082 | 0.764178 | 0.764178 | 0 | 0.0883224 | 0.753773 | 0.89884 | 0.956099 | 0.102682 |
| tossup_correctness | tier | fall | 2798 | 0.550391 | 0.568305 | 0.0967083 | 0.17791 | 0.785561 | 0.785204 | 0.000357398 | 0.0744639 | 0.783676 | 0.890064 | 0.946783 | 0.104735 |
| tossup_correctness | tier | nationals | 1545 | 0.569122 | 0.698721 | 0.141986 | 0.221816 | 0.720388 | 0.721036 | -0.000647249 | 0.102783 | 0.699837 | 0.896808 | 0.962398 | 0.108153 |
| tossup_correctness | tier | regionals | 2039 | 0.552465 | 0.623828 | 0.112299 | 0.194694 | 0.762629 | 0.762138 | 0.000490436 | 0.106242 | 0.69489 | 0.900557 | 0.959802 | 0.106125 |
| tossup_correctness | tier | winter | 2875 | 0.543847 | 0.626736 | 0.126464 | 0.194482 | 0.768 | 0.768348 | -0.000347826 | 0.0758597 | 0.781213 | 0.907061 | 0.958433 | 0.0953035 |
| tossup_correctness | category | Current Events | 129 | 0.555976 | 0.778345 | 0.195695 | 0.258519 | 0.666667 | 0.666667 | 0 | 0.0853871 | 0.76077 | 0.890179 | 0.936722 | 0.112726 |
| tossup_correctness | category | Fine Arts | 1074 | 0.553652 | 0.603402 | 0.114539 | 0.186608 | 0.776536 | 0.776536 | 0 | 0.0770737 | 0.791184 | 0.91026 | 0.957594 | 0.0943927 |
| tossup_correctness | category | Geography | 180 | 0.589241 | 0.902741 | 0.26589 | 0.302735 | 0.611111 | 0.616667 | -0.00555556 | 0.0834838 | 0.760309 | 0.897654 | 0.949233 | 0.104761 |
| tossup_correctness | category | History | 1454 | 0.563908 | 0.618783 | 0.121643 | 0.197265 | 0.756534 | 0.757909 | -0.00137552 | 0.0848824 | 0.753799 | 0.893327 | 0.947631 | 0.106813 |
| tossup_correctness | category | Literature | 1435 | 0.509291 | 0.552837 | 0.0921942 | 0.164781 | 0.810453 | 0.810453 | 0 | 0.0766521 | 0.788659 | 0.909622 | 0.963497 | 0.0927856 |
| tossup_correctness | category | Mythology | 324 | 0.584471 | 0.546942 | 0.115968 | 0.170167 | 0.79321 | 0.79321 | 0 | 0.090079 | 0.754972 | 0.906119 | 0.952042 | 0.0994289 |
| tossup_correctness | category | Other Academic | 71 | 0.385621 | 0.740414 | 0.198511 | 0.22111 | 0.760563 | 0.760563 | 0 | 0.0852003 | 0.768201 | 0.917901 | 0.953905 | 0.0920292 |
| tossup_correctness | category | Philosophy | 310 | 0.509047 | 0.662754 | 0.156009 | 0.203584 | 0.76129 | 0.76129 | 0 | 0.0781726 | 0.788812 | 0.912142 | 0.958341 | 0.0915819 |
| tossup_correctness | category | Popular Culture | 108 | 0.634549 | 0.34004 | 0.0563794 | 0.0976169 | 0.888889 | 0.888889 | 0 | 0.0662595 | 0.792008 | 0.889437 | 0.948038 | 0.103475 |
| tossup_correctness | category | Religion | 361 | 0.537875 | 0.669688 | 0.137376 | 0.209128 | 0.742382 | 0.742382 | 0 | 0.0808026 | 0.769234 | 0.902756 | 0.952117 | 0.0992547 |
| tossup_correctness | category | Science | 1445 | 0.552335 | 0.637023 | 0.118207 | 0.203224 | 0.747405 | 0.746021 | 0.00138408 | 0.0848552 | 0.74141 | 0.877784 | 0.949888 | 0.113135 |
| tossup_correctness | category | Social Science | 327 | 0.566605 | 0.713486 | 0.161066 | 0.227681 | 0.718654 | 0.718654 | 0 | 0.0835799 | 0.766657 | 0.898946 | 0.950728 | 0.101791 |
| tossup_correctness | category | Unknown | 2039 | 0.552465 | 0.623828 | 0.112299 | 0.194694 | 0.762629 | 0.762138 | 0.000490436 | 0.106242 | 0.69489 | 0.900557 | 0.959802 | 0.106125 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.449937 | 0.677121 | 0.135426 | 0.2153 | 0.737705 | 0.743169 | -0.00546448 | 0.0922791 | 0.740577 | 0.859844 | 0.935551 | 0.120895 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.550598 | 0.65962 | 0.135327 | 0.215871 | 0.727749 | 0.728796 | -0.00104712 | 0.0846757 | 0.751066 | 0.872074 | 0.937105 | 0.116556 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.545808 | 0.631329 | 0.116717 | 0.200056 | 0.753461 | 0.752568 | 0.000893256 | 0.0884671 | 0.74768 | 0.884412 | 0.947605 | 0.110655 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.55165 | 0.575344 | 0.0967178 | 0.177827 | 0.786087 | 0.786087 | 0 | 0.0882764 | 0.754937 | 0.902991 | 0.955622 | 0.101029 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.554882 | 0.639595 | 0.127501 | 0.196965 | 0.764393 | 0.764393 | 0 | 0.0867685 | 0.761886 | 0.914667 | 0.962978 | 0.0928045 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1197 | -1.48331 | 0.572442 | -2.76306 | -2.25491 | -1.82302 | -1.53672 | -1.22551 | -0.478578 | 1.76671 |
| player | beta | 1197 | -2.9438 | 1.02252 | -6.5662 | -5.04299 | -3.42279 | -2.71119 | -2.2127 | -1.70465 | -1.38257 |
| player | theta_1 | 1197 | 0.953676 | 0.883473 | -1.78666 | -0.542028 | 0.393489 | 0.992794 | 1.55972 | 2.35125 | 3.5349 |
| player | theta_2 | 1197 | 0.904097 | 0.869752 | -2.2765 | -0.626787 | 0.351449 | 0.948968 | 1.53884 | 2.20536 | 3.69449 |
| player | theta_norm | 1197 | 1.67677 | 0.671871 | 0.0591051 | 0.576923 | 1.1595 | 1.69855 | 2.18138 | 2.69719 | 3.71155 |
| tossup | start_difficulty_d1 | 1240 | -1.25308 | 0.503587 | -2.36242 | -1.93938 | -1.64293 | -1.34892 | -0.906594 | -0.307277 | -0.1407 |
| tossup | start_difficulty_d2 | 1240 | -1.09791 | 0.416095 | -2.06561 | -1.76824 | -1.43156 | -1.06421 | -0.774286 | -0.434249 | -0.133783 |
| tossup | end_difficulty_d1 | 1240 | -1.77949 | 0.443946 | -3.1479 | -2.5056 | -2.10104 | -1.80724 | -1.40463 | -1.09645 | -0.900259 |
| tossup | end_difficulty_d2 | 1240 | -1.68599 | 0.350388 | -2.82116 | -2.29769 | -1.93606 | -1.63357 | -1.42783 | -1.16782 | -0.972479 |
| tossup | total_drop_d1 | 1240 | 0.526413 | 0.183989 | 0.209227 | 0.26164 | 0.368081 | 0.519877 | 0.675313 | 0.830367 | 0.998495 |
| tossup | total_drop_d2 | 1240 | 0.588079 | 0.176015 | 0.216917 | 0.290992 | 0.450863 | 0.596244 | 0.732227 | 0.853399 | 0.99279 |
| tossup | drop_share_1_d1 | 1240 | 0.331926 | 0.0369608 | 0.176146 | 0.272582 | 0.310148 | 0.331602 | 0.354554 | 0.391263 | 0.466857 |
| tossup | drop_share_2_d1 | 1240 | 0.311085 | 0.0202638 | 0.242398 | 0.276093 | 0.298089 | 0.312961 | 0.326292 | 0.340817 | 0.373348 |
| tossup | drop_share_3_d1 | 1240 | 0.356989 | 0.0432188 | 0.233149 | 0.297362 | 0.329893 | 0.350392 | 0.376599 | 0.441473 | 0.556701 |
| tossup | drop_share_1_d2 | 1240 | 0.327253 | 0.0323346 | 0.19883 | 0.271021 | 0.310635 | 0.327179 | 0.345829 | 0.378204 | 0.447236 |
| tossup | drop_share_2_d2 | 1240 | 0.315837 | 0.0196764 | 0.252725 | 0.277649 | 0.304208 | 0.318681 | 0.331149 | 0.342455 | 0.359539 |
| tossup | drop_share_3_d2 | 1240 | 0.35691 | 0.040351 | 0.255248 | 0.304503 | 0.331868 | 0.348788 | 0.372491 | 0.441636 | 0.517439 |
| tossup | r_1 | 1240 | 0.581643 | 0.278994 | 0.0311024 | 0.0682399 | 0.387464 | 0.658759 | 0.815292 | 0.923435 | 0.968222 |
| tossup | r_2 | 1240 | 0.418357 | 0.278994 | 0.0317779 | 0.076565 | 0.184708 | 0.341241 | 0.612536 | 0.93176 | 0.968898 |
| tossup | r_norm | 1240 | 0.813854 | 0.0807976 | 0.707107 | 0.708072 | 0.73442 | 0.808514 | 0.886217 | 0.945381 | 0.969397 |
