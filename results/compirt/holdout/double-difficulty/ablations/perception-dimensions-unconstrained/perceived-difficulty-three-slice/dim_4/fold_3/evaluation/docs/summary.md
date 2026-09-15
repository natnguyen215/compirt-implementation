# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_4/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_4/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 321861 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.646764 |
| log_loss | 0.516335 |
| ece | 0.0267581 |
| brier | 0.167746 |
| accuracy | 0.773458 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.0034141 |
| probability_std | 0.122199 |
| probability_p10 | 0.599261 |
| probability_p50 | 0.784884 |
| probability_p90 | 0.906032 |
| mean_predictive_variance | 0.164432 |
| integrated_brier_score | 0.102719 |
| joint_tossup_event_log_loss | 6.85154 |
| buzz_position_mae | 0.163021 |
| buzz_position_median_absolute_error | 0.147837 |
| buzz_position_bias | -0.0744458 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.368833 |
| first_buzzer_mean_reciprocal_rank | 0.576325 |
| first_buzzer_log_loss | 1.65723 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.657159 |
| tossup_scorer_player_top1_accuracy | 0.327223 |
| tossup_scorer_team_top1_accuracy | 0.504121 |
| tossup_game_winner_accuracy | 0.800885 |
| tossup_game_margin_mae | 35.1611 |
| tournament_player_ppg_spearman | 0.707553 |
| tournament_player_ppg_mae | 8.74282 |
| tournament_player_ppg_top10_overlap | 0.672414 |
| neg_auroc | 0.646764 |
| neg_average_precision | 0.37248 |
| neg_precision | 0.551495 |
| neg_recall | 0.0795019 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0540512 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0869659 |
| no_buzz_calibration_error | 0.0717815 |
| no_buzz_brier | 0.0244936 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| tossup_correctness | aggregate | all | 9080 | 0.646764 | 0.516335 | 0.0267581 | 0.167746 | 0.773458 | 0.770044 | 0.0034141 | 0.122199 | 0.599261 | 0.784884 | 0.906032 | 0.164432 |
| tossup_correctness | tier | fall | 2817 | 0.612967 | 0.514797 | 0.0412555 | 0.165723 | 0.784523 | 0.781683 | 0.0028399 | 0.114044 | 0.630598 | 0.807519 | 0.912682 | 0.154939 |
| tossup_correctness | tier | nationals | 1542 | 0.702134 | 0.538812 | 0.0587404 | 0.179486 | 0.737354 | 0.73476 | 0.00259403 | 0.123694 | 0.50753 | 0.688997 | 0.826317 | 0.203098 |
| tossup_correctness | tier | regionals | 1934 | 0.651735 | 0.526902 | 0.0172162 | 0.173557 | 0.758014 | 0.75698 | 0.00103413 | 0.105237 | 0.614225 | 0.77432 | 0.880483 | 0.17231 |
| tossup_correctness | tier | winter | 2787 | 0.640892 | 0.498118 | 0.028719 | 0.159263 | 0.792967 | 0.786868 | 0.00609975 | 0.116185 | 0.645502 | 0.822614 | 0.924366 | 0.147168 |
| tossup_correctness | category | Current Events | 125 | 0.639435 | 0.578031 | 0.0821946 | 0.195791 | 0.72 | 0.704 | 0.016 | 0.106644 | 0.56506 | 0.716726 | 0.825484 | 0.196521 |
| tossup_correctness | category | Fine Arts | 1072 | 0.640106 | 0.518394 | 0.0357723 | 0.168769 | 0.774254 | 0.770522 | 0.00373134 | 0.120497 | 0.614288 | 0.807813 | 0.913718 | 0.155649 |
| tossup_correctness | category | Geography | 185 | 0.763357 | 0.518039 | 0.0486441 | 0.172088 | 0.740541 | 0.702703 | 0.0378378 | 0.148388 | 0.48047 | 0.732944 | 0.872256 | 0.184779 |
| tossup_correctness | category | History | 1443 | 0.686763 | 0.504336 | 0.0216282 | 0.164179 | 0.775468 | 0.765073 | 0.010395 | 0.123179 | 0.585783 | 0.768189 | 0.895919 | 0.172076 |
| tossup_correctness | category | Literature | 1411 | 0.575478 | 0.491494 | 0.0489114 | 0.152662 | 0.811481 | 0.81219 | -0.000708717 | 0.10078 | 0.698994 | 0.852949 | 0.9394 | 0.129768 |
| tossup_correctness | category | Mythology | 320 | 0.596099 | 0.516316 | 0.0851647 | 0.165815 | 0.775 | 0.79375 | -0.01875 | 0.119381 | 0.561667 | 0.763362 | 0.866535 | 0.180567 |
| tossup_correctness | category | Other Academic | 64 | 0.561198 | 0.565485 | 0.0951229 | 0.188036 | 0.765625 | 0.75 | 0.015625 | 0.0999375 | 0.582543 | 0.700822 | 0.823327 | 0.199997 |
| tossup_correctness | category | Philosophy | 312 | 0.574774 | 0.505927 | 0.0481226 | 0.160656 | 0.798077 | 0.801282 | -0.00320513 | 0.116037 | 0.626795 | 0.808436 | 0.916773 | 0.153695 |
| tossup_correctness | category | Popular Culture | 104 | 0.524858 | 0.459376 | 0.114221 | 0.143639 | 0.836538 | 0.846154 | -0.00961538 | 0.110986 | 0.647418 | 0.778443 | 0.923465 | 0.160066 |
| tossup_correctness | category | Religion | 358 | 0.626413 | 0.579148 | 0.0586519 | 0.193816 | 0.723464 | 0.726257 | -0.0027933 | 0.133724 | 0.579381 | 0.774221 | 0.909674 | 0.164883 |
| tossup_correctness | category | Science | 1431 | 0.664558 | 0.513782 | 0.0350365 | 0.167614 | 0.772886 | 0.765199 | 0.00768693 | 0.133007 | 0.558297 | 0.761136 | 0.886016 | 0.175268 |
| tossup_correctness | category | Social Science | 321 | 0.651393 | 0.544018 | 0.0267075 | 0.182331 | 0.741433 | 0.744548 | -0.00311526 | 0.117593 | 0.575212 | 0.753121 | 0.878244 | 0.179957 |
| tossup_correctness | category | Unknown | 1934 | 0.651735 | 0.526902 | 0.0172162 | 0.173557 | 0.758014 | 0.75698 | 0.00103413 | 0.105237 | 0.614225 | 0.77432 | 0.880483 | 0.17231 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.706511 | 0.566378 | 0.0542209 | 0.191905 | 0.692708 | 0.697917 | -0.00520833 | 0.121511 | 0.508985 | 0.682456 | 0.814773 | 0.206757 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.653665 | 0.553237 | 0.0392155 | 0.184749 | 0.735658 | 0.733408 | 0.00224972 | 0.129291 | 0.525126 | 0.725074 | 0.851972 | 0.19058 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.62256 | 0.539239 | 0.0305376 | 0.177016 | 0.757919 | 0.759276 | -0.00135747 | 0.119546 | 0.590045 | 0.771883 | 0.885765 | 0.17256 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.638687 | 0.495034 | 0.0300927 | 0.158648 | 0.794005 | 0.789125 | 0.00487975 | 0.11302 | 0.622373 | 0.795253 | 0.907564 | 0.160011 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.658541 | 0.505402 | 0.0348169 | 0.162904 | 0.781849 | 0.775342 | 0.00650685 | 0.120301 | 0.621756 | 0.811172 | 0.923103 | 0.151881 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | -1.92025 | 1.09311 | -5.10102 | -3.50733 | -2.71634 | -2.13235 | -0.983931 | -0.147144 | 0.613247 |
| player | theta_2 | 1133 | -1.491 | 0.909625 | -4.65928 | -3.24466 | -2.14747 | -1.26532 | -0.767158 | -0.383625 | 0.577463 |
| player | theta_3 | 1133 | -0.804779 | 0.679769 | -3.88057 | -2.25106 | -1.07846 | -0.644222 | -0.343933 | -0.0250055 | 0.735469 |
| player | theta_4 | 1133 | -1.55547 | 1.09631 | -4.91884 | -3.34104 | -2.48226 | -1.39521 | -0.554424 | -0.0972105 | 0.712046 |
| player | theta_norm | 1133 | 3.44419 | 0.89382 | 1.53156 | 2.08729 | 2.75323 | 3.39664 | 4.07178 | 4.98902 | 6.08391 |
| tossup | start_difficulty_d1 | 1240 | -2.16057 | 1.32849 | -4.80895 | -3.89703 | -3.18872 | -2.61577 | -0.759693 | 0.00235628 | 0.360431 |
| tossup | start_difficulty_d2 | 1240 | -1.51069 | 1.18653 | -4.13763 | -3.52902 | -2.49682 | -1.29431 | -0.494123 | 0.0821294 | 0.746985 |
| tossup | start_difficulty_d3 | 1240 | -0.730101 | 0.783167 | -3.06519 | -2.20108 | -1.28323 | -0.52408 | -0.110894 | 0.247694 | 0.948821 |
| tossup | start_difficulty_d4 | 1240 | -1.30304 | 1.46614 | -4.88651 | -4.08404 | -2.39018 | -0.588379 | -0.180016 | 0.0892952 | 0.388693 |
| tossup | end_difficulty_d1 | 1240 | -3.23112 | 1.42341 | -7.42403 | -5.19622 | -4.32122 | -3.6017 | -1.78119 | -0.938553 | -0.569684 |
| tossup | end_difficulty_d2 | 1240 | -2.59686 | 1.3289 | -7.06582 | -4.83144 | -3.69422 | -2.35722 | -1.47984 | -0.838836 | -0.100255 |
| tossup | end_difficulty_d3 | 1240 | -1.774 | 0.909408 | -4.74713 | -3.5442 | -2.36828 | -1.52918 | -1.06824 | -0.640506 | 0.168488 |
| tossup | end_difficulty_d4 | 1240 | -2.32781 | 1.51684 | -6.70395 | -5.24963 | -3.42535 | -1.61353 | -1.16482 | -0.860747 | -0.509853 |
| tossup | total_drop_d1 | 1240 | 1.07055 | 0.30509 | 0.489734 | 0.70191 | 0.934615 | 1.01061 | 1.14088 | 1.53949 | 3.93192 |
| tossup | total_drop_d2 | 1240 | 1.08618 | 0.278472 | 0.64694 | 0.847423 | 0.936528 | 1.01291 | 1.14073 | 1.54944 | 3.52645 |
| tossup | total_drop_d3 | 1240 | 1.0439 | 0.150948 | 0.780333 | 0.891643 | 0.951505 | 1.00167 | 1.08879 | 1.34492 | 2.04462 |
| tossup | total_drop_d4 | 1240 | 1.02477 | 0.199489 | 0.368268 | 0.750059 | 0.952473 | 0.997951 | 1.06572 | 1.33248 | 2.46922 |
| tossup | drop_share_1_d1 | 1240 | 0.348244 | 0.0441289 | 0.209451 | 0.295364 | 0.315246 | 0.341647 | 0.3753 | 0.425253 | 0.587222 |
| tossup | drop_share_2_d1 | 1240 | 0.338704 | 0.0188007 | 0.261473 | 0.308495 | 0.328885 | 0.339512 | 0.34822 | 0.365345 | 0.512847 |
| tossup | drop_share_3_d1 | 1240 | 0.313052 | 0.0416475 | 0.146898 | 0.239077 | 0.2867 | 0.320652 | 0.342412 | 0.366128 | 0.466009 |
| tossup | drop_share_1_d2 | 1240 | 0.337244 | 0.034231 | 0.269055 | 0.299203 | 0.312895 | 0.327819 | 0.354037 | 0.40156 | 0.559727 |
| tossup | drop_share_2_d2 | 1240 | 0.342519 | 0.0130559 | 0.287839 | 0.319002 | 0.335185 | 0.343103 | 0.351417 | 0.362337 | 0.380193 |
| tossup | drop_share_3_d2 | 1240 | 0.320237 | 0.0311012 | 0.152434 | 0.260429 | 0.303291 | 0.327276 | 0.342864 | 0.359586 | 0.394921 |
| tossup | drop_share_1_d3 | 1240 | 0.319966 | 0.0175667 | 0.273771 | 0.294894 | 0.308052 | 0.316922 | 0.330634 | 0.353432 | 0.384037 |
| tossup | drop_share_2_d3 | 1240 | 0.34687 | 0.00921136 | 0.32243 | 0.332017 | 0.340586 | 0.346587 | 0.353101 | 0.361774 | 0.382412 |
| tossup | drop_share_3_d3 | 1240 | 0.333164 | 0.0183376 | 0.277657 | 0.297953 | 0.322297 | 0.335437 | 0.346286 | 0.35955 | 0.37932 |
| tossup | drop_share_1_d4 | 1240 | 0.331072 | 0.0413574 | 0.230943 | 0.297079 | 0.30726 | 0.317441 | 0.334789 | 0.420257 | 0.574982 |
| tossup | drop_share_2_d4 | 1240 | 0.341948 | 0.0164576 | 0.259557 | 0.309862 | 0.335031 | 0.344598 | 0.351581 | 0.361876 | 0.465318 |
| tossup | drop_share_3_d4 | 1240 | 0.326979 | 0.0343728 | 0.144916 | 0.249456 | 0.321164 | 0.336472 | 0.345885 | 0.35984 | 0.433267 |
| tossup | r_1 | 1240 | 0.406104 | 0.284643 | 0.0157616 | 0.0287054 | 0.105978 | 0.440579 | 0.665548 | 0.820518 | 0.912421 |
| tossup | r_2 | 1240 | 0.230085 | 0.215056 | 0.0245204 | 0.0398465 | 0.0690656 | 0.123333 | 0.364704 | 0.679466 | 0.803921 |
| tossup | r_3 | 1240 | 0.10844 | 0.0862123 | 0.0120034 | 0.0256071 | 0.0442648 | 0.0760076 | 0.146541 | 0.303833 | 0.427813 |
| tossup | r_4 | 1240 | 0.25537 | 0.302602 | 0.0172036 | 0.0342349 | 0.0567414 | 0.09264 | 0.257943 | 0.831203 | 0.9199 |
| tossup | r_norm | 1240 | 0.716334 | 0.0882782 | 0.506982 | 0.584261 | 0.641023 | 0.71656 | 0.787735 | 0.859088 | 0.921097 |
