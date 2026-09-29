# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_4/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_4/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 336425 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.556231 |
| log_loss | 0.605389 |
| ece | 0.10073 |
| brier | 0.191975 |
| accuracy | 0.760585 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.00153965 |
| probability_std | 0.100519 |
| probability_p10 | 0.706637 |
| probability_p50 | 0.885456 |
| probability_p90 | 0.948361 |
| mean_predictive_variance | 0.114501 |
| integrated_brier_score | 0.17535 |
| joint_tossup_event_log_loss | 7.75042 |
| buzz_position_mae | 0.343933 |
| buzz_position_median_absolute_error | 0.350895 |
| buzz_position_bias | -0.331951 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.358188 |
| first_buzzer_mean_reciprocal_rank | 0.569498 |
| first_buzzer_log_loss | 1.65903 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.624546 |
| tossup_scorer_player_top1_accuracy | 0.272944 |
| tossup_scorer_team_top1_accuracy | 0.394481 |
| tossup_game_winner_accuracy | 0.711712 |
| tossup_game_margin_mae | 43.0516 |
| tournament_player_ppg_spearman | 0.585007 |
| tournament_player_ppg_mae | 10.3058 |
| tournament_player_ppg_top10_overlap | 0.596552 |
| neg_auroc | 0.556231 |
| neg_average_precision | 0.282643 |
| neg_precision | 0.36 |
| neg_recall | 0.00832178 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.029436 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.236224 |
| no_buzz_calibration_error | 0.220315 |
| no_buzz_brier | 0.0727984 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| tossup_correctness | aggregate | all | 9093 | 0.556231 | 0.605389 | 0.10073 | 0.191975 | 0.760585 | 0.762125 | -0.00153965 | 0.100519 | 0.706637 | 0.885456 | 0.948361 | 0.114501 |
| tossup_correctness | tier | fall | 2842 | 0.55759 | 0.554165 | 0.0827507 | 0.175318 | 0.784659 | 0.785362 | -0.00070373 | 0.0850024 | 0.746773 | 0.883785 | 0.939133 | 0.11315 |
| tossup_correctness | tier | nationals | 1564 | 0.562724 | 0.648769 | 0.10346 | 0.214608 | 0.711637 | 0.718031 | -0.00639386 | 0.127245 | 0.613991 | 0.831788 | 0.941758 | 0.143166 |
| tossup_correctness | tier | regionals | 1937 | 0.541004 | 0.621406 | 0.104109 | 0.195709 | 0.757873 | 0.758389 | -0.000516262 | 0.104749 | 0.695239 | 0.882385 | 0.950467 | 0.11604 |
| tossup_correctness | tier | winter | 2750 | 0.544885 | 0.622374 | 0.117653 | 0.193686 | 0.765455 | 0.765818 | -0.000363636 | 0.0816172 | 0.773431 | 0.904204 | 0.955421 | 0.0985116 |
| tossup_correctness | category | Current Events | 126 | 0.507999 | 0.598138 | 0.109264 | 0.191578 | 0.769841 | 0.769841 | 0 | 0.10167 | 0.68842 | 0.865616 | 0.922412 | 0.128232 |
| tossup_correctness | category | Fine Arts | 1071 | 0.572146 | 0.600683 | 0.111959 | 0.190604 | 0.766573 | 0.766573 | 0 | 0.0914416 | 0.72673 | 0.896114 | 0.949401 | 0.106829 |
| tossup_correctness | category | Geography | 185 | 0.522702 | 0.751685 | 0.175277 | 0.243569 | 0.702703 | 0.697297 | 0.00540541 | 0.109581 | 0.705456 | 0.888188 | 0.947691 | 0.112875 |
| tossup_correctness | category | History | 1440 | 0.545351 | 0.616686 | 0.103967 | 0.197893 | 0.752778 | 0.754167 | -0.00138889 | 0.103553 | 0.681027 | 0.872177 | 0.943066 | 0.122211 |
| tossup_correctness | category | Literature | 1422 | 0.533203 | 0.518516 | 0.064423 | 0.156975 | 0.81294 | 0.814346 | -0.00140647 | 0.0912748 | 0.74281 | 0.895812 | 0.954642 | 0.1062 |
| tossup_correctness | category | Mythology | 318 | 0.600642 | 0.541768 | 0.0937044 | 0.170654 | 0.786164 | 0.789308 | -0.00314465 | 0.0945395 | 0.741135 | 0.899158 | 0.940813 | 0.106394 |
| tossup_correctness | category | Other Academic | 66 | 0.455767 | 0.76328 | 0.21743 | 0.245524 | 0.712121 | 0.712121 | 0 | 0.11316 | 0.672886 | 0.889072 | 0.951853 | 0.120246 |
| tossup_correctness | category | Philosophy | 311 | 0.600338 | 0.639271 | 0.137486 | 0.201252 | 0.73955 | 0.745981 | -0.00643087 | 0.100438 | 0.734163 | 0.911352 | 0.956685 | 0.0991166 |
| tossup_correctness | category | Popular Culture | 102 | 0.609259 | 0.368986 | 0.0295907 | 0.107015 | 0.872549 | 0.882353 | -0.00980392 | 0.0763014 | 0.800294 | 0.885353 | 0.941791 | 0.107415 |
| tossup_correctness | category | Religion | 358 | 0.582105 | 0.701546 | 0.160067 | 0.229025 | 0.703911 | 0.712291 | -0.00837989 | 0.110421 | 0.683811 | 0.892318 | 0.945488 | 0.111948 |
| tossup_correctness | category | Science | 1433 | 0.563624 | 0.626631 | 0.105342 | 0.202883 | 0.736916 | 0.738311 | -0.00139567 | 0.102007 | 0.694667 | 0.867499 | 0.941573 | 0.124235 |
| tossup_correctness | category | Social Science | 324 | 0.588341 | 0.64754 | 0.140955 | 0.210853 | 0.728395 | 0.731481 | -0.00308642 | 0.0943793 | 0.726622 | 0.893394 | 0.942167 | 0.111979 |
| tossup_correctness | category | Unknown | 1937 | 0.541004 | 0.621406 | 0.104109 | 0.195709 | 0.757873 | 0.758389 | -0.000516262 | 0.104749 | 0.695239 | 0.882385 | 0.950467 | 0.11604 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.52451 | 0.672553 | 0.138018 | 0.223465 | 0.694611 | 0.712575 | -0.0179641 | 0.1076 | 0.661897 | 0.840757 | 0.922398 | 0.140577 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.545079 | 0.64027 | 0.10613 | 0.210435 | 0.720395 | 0.729167 | -0.00877193 | 0.103413 | 0.672896 | 0.852907 | 0.925929 | 0.1342 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.540691 | 0.609578 | 0.0994035 | 0.196364 | 0.756028 | 0.755083 | 0.000945626 | 0.0980877 | 0.705267 | 0.868759 | 0.936729 | 0.122463 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.560804 | 0.567792 | 0.0907109 | 0.178907 | 0.780239 | 0.780942 | -0.000703235 | 0.0959174 | 0.71329 | 0.887506 | 0.945725 | 0.112904 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.559189 | 0.623406 | 0.113078 | 0.193868 | 0.761047 | 0.762029 | -0.000981997 | 0.101669 | 0.714097 | 0.905619 | 0.957456 | 0.103171 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1167 | -1.3342 | 0.768335 | -3.22737 | -2.38464 | -1.79266 | -1.42969 | -0.994567 | -0.00754712 | 2.18506 |
| player | beta | 1167 | -3.45567 | 1.14308 | -6.99888 | -5.86474 | -4.01059 | -3.17982 | -2.59534 | -2.07174 | -1.69752 |
| player | theta_1 | 1167 | 0.849102 | 0.927587 | -2.02093 | -0.879614 | 0.190201 | 1.04607 | 1.53188 | 2.13629 | 3.1645 |
| player | theta_2 | 1167 | 0.842468 | 0.965659 | -2.53553 | -0.91071 | 0.310152 | 0.913545 | 1.48245 | 2.30764 | 3.83013 |
| player | theta_3 | 1167 | 0.818222 | 0.947638 | -2.72395 | -0.953411 | 0.249106 | 0.952846 | 1.48958 | 2.17436 | 3.09184 |
| player | theta_4 | 1167 | 0.768667 | 0.795167 | -1.92593 | -0.734859 | 0.288657 | 0.853422 | 1.30545 | 1.93521 | 3.88599 |
| player | theta_norm | 1167 | 2.36372 | 0.651645 | 0.377109 | 1.26934 | 1.9549 | 2.38972 | 2.77325 | 3.38695 | 5.01571 |
| tossup | start_difficulty_d1 | 1220 | -0.888292 | 0.40481 | -2.08579 | -1.68436 | -1.15169 | -0.813967 | -0.567724 | -0.355611 | -0.00320702 |
| tossup | start_difficulty_d2 | 1220 | -0.898192 | 0.444003 | -2.24997 | -1.7023 | -1.19562 | -0.870514 | -0.563471 | -0.23551 | 0.00537892 |
| tossup | start_difficulty_d3 | 1220 | -0.854944 | 0.483864 | -2.39033 | -1.80908 | -1.16347 | -0.738296 | -0.458395 | -0.272417 | 0.0341287 |
| tossup | start_difficulty_d4 | 1220 | -0.799626 | 0.321356 | -1.9491 | -1.37393 | -0.991689 | -0.778819 | -0.569573 | -0.320434 | 0.0115155 |
| tossup | end_difficulty_d1 | 1220 | -1.62511 | 0.325928 | -2.80029 | -2.21816 | -1.85045 | -1.59501 | -1.36481 | -1.15919 | -0.977634 |
| tossup | end_difficulty_d2 | 1220 | -1.63861 | 0.384131 | -2.72555 | -2.29308 | -1.9263 | -1.60681 | -1.3317 | -1.09017 | -0.754714 |
| tossup | end_difficulty_d3 | 1220 | -1.60461 | 0.409789 | -2.84787 | -2.38854 | -1.88916 | -1.51129 | -1.26955 | -1.09409 | -0.843204 |
| tossup | end_difficulty_d4 | 1220 | -1.56829 | 0.291974 | -2.47363 | -2.06876 | -1.76521 | -1.55 | -1.35499 | -1.11904 | -0.898479 |
| tossup | total_drop_d1 | 1220 | 0.736813 | 0.194903 | 0.242587 | 0.356219 | 0.608731 | 0.768065 | 0.881238 | 1.01393 | 1.18 |
| tossup | total_drop_d2 | 1220 | 0.740414 | 0.175395 | 0.243179 | 0.391828 | 0.639054 | 0.763877 | 0.865139 | 0.997765 | 1.25405 |
| tossup | total_drop_d3 | 1220 | 0.749662 | 0.185613 | 0.255493 | 0.364849 | 0.657637 | 0.79224 | 0.874888 | 0.991252 | 1.21186 |
| tossup | total_drop_d4 | 1220 | 0.768663 | 0.164053 | 0.280199 | 0.433431 | 0.684746 | 0.789974 | 0.87837 | 0.998907 | 1.22145 |
| tossup | drop_share_1_d1 | 1220 | 0.319671 | 0.0216037 | 0.235139 | 0.28622 | 0.30787 | 0.319449 | 0.330931 | 0.354728 | 0.417405 |
| tossup | drop_share_2_d1 | 1220 | 0.326873 | 0.018425 | 0.254778 | 0.289079 | 0.317656 | 0.330647 | 0.339595 | 0.350729 | 0.367639 |
| tossup | drop_share_3_d1 | 1220 | 0.353455 | 0.0277611 | 0.273787 | 0.31779 | 0.336757 | 0.348408 | 0.363857 | 0.407513 | 0.484065 |
| tossup | drop_share_1_d2 | 1220 | 0.318994 | 0.0216896 | 0.215957 | 0.286286 | 0.306967 | 0.318894 | 0.330515 | 0.35559 | 0.417774 |
| tossup | drop_share_2_d2 | 1220 | 0.327388 | 0.0173052 | 0.250276 | 0.292324 | 0.318542 | 0.330312 | 0.339195 | 0.350562 | 0.363167 |
| tossup | drop_share_3_d2 | 1220 | 0.353618 | 0.0270288 | 0.26843 | 0.318987 | 0.337272 | 0.349643 | 0.363239 | 0.407576 | 0.496682 |
| tossup | drop_share_1_d3 | 1220 | 0.321463 | 0.0243819 | 0.221174 | 0.289588 | 0.306227 | 0.317806 | 0.332741 | 0.367033 | 0.441706 |
| tossup | drop_share_2_d3 | 1220 | 0.329391 | 0.0160203 | 0.268665 | 0.297602 | 0.321217 | 0.331897 | 0.340484 | 0.351169 | 0.364529 |
| tossup | drop_share_3_d3 | 1220 | 0.349146 | 0.0241437 | 0.261479 | 0.313964 | 0.335662 | 0.348316 | 0.361929 | 0.388741 | 0.467943 |
| tossup | drop_share_1_d4 | 1220 | 0.318614 | 0.0206216 | 0.20516 | 0.287743 | 0.307607 | 0.319135 | 0.330493 | 0.350232 | 0.430577 |
| tossup | drop_share_2_d4 | 1220 | 0.329946 | 0.0152601 | 0.264601 | 0.300012 | 0.322116 | 0.331892 | 0.340253 | 0.350943 | 0.364867 |
| tossup | drop_share_3_d4 | 1220 | 0.35144 | 0.0257504 | 0.279054 | 0.320071 | 0.336456 | 0.347588 | 0.360815 | 0.401277 | 0.510479 |
| tossup | r_1 | 1220 | 0.247885 | 0.201524 | 0.0319228 | 0.0641193 | 0.11844 | 0.16807 | 0.296419 | 0.752761 | 0.87512 |
| tossup | r_2 | 1220 | 0.2746 | 0.212138 | 0.0316993 | 0.0580093 | 0.103089 | 0.196415 | 0.411496 | 0.698746 | 0.898704 |
| tossup | r_3 | 1220 | 0.261619 | 0.192739 | 0.0278161 | 0.055203 | 0.110902 | 0.191191 | 0.37685 | 0.662533 | 0.846038 |
| tossup | r_4 | 1220 | 0.215895 | 0.149361 | 0.0321098 | 0.0592676 | 0.111851 | 0.175953 | 0.265879 | 0.55331 | 0.838384 |
| tossup | r_norm | 1220 | 0.622945 | 0.0938427 | 0.50011 | 0.512849 | 0.544204 | 0.59821 | 0.678833 | 0.810596 | 0.900658 |
