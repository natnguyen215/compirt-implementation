# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold/fold_0/holdout/evaluation`
Result root: `results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold/fold_0`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 298145 |
| pyramidal | calibrate_correctness | False |
| compositional | tournament | all tournaments |
| compositional | dimensions | 5 |
| compositional | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.143376 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.886726 |
| log_loss | 0.424619 |
| ece | 0.0172196 |
| brier | 0.135103 |
| part_accuracy | 0.809784 |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.291347 |
| part_accuracy_macro_team | 0.812382 |
| part_accuracy_macro_bonus | 0.805734 |
| probability_std | 0.327012 |
| probability_p10 | 0.0860023 |
| probability_p50 | 0.477924 |
| probability_p90 | 0.932653 |
| mean_predictive_variance | 0.143048 |
| exact_acc | 0.513479 |
| ranked_probability_score | 0.11738 |
| bonus_total_score_log_loss | 1.02644 |
| ppb_mae | 2.3728 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.635505 |
| log_loss | 0.810881 |
| ece | 0.2202 |
| brier | 0.258354 |
| accuracy | 0.629048 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.136202 |
| probability_std | 0.294526 |
| probability_p10 | 0.105318 |
| probability_p50 | 0.618551 |
| probability_p90 | 0.912996 |
| mean_predictive_variance | 0.159632 |
| integrated_brier_score | 0.0949991 |
| joint_tossup_event_log_loss | 6.78108 |
| buzz_position_mae | 0.144891 |
| buzz_position_median_absolute_error | 0.125541 |
| buzz_position_bias | -0.0396224 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.403012 |
| first_buzzer_mean_reciprocal_rank | 0.606287 |
| first_buzzer_log_loss | 1.60606 |
| first_buzzer_events | 9295 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.777778 |
| match_winner_brier | 0.150752 |
| match_games | 468 |
| match_simulations_per_game | 500 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.635505 | 0.810881 | 0.2202 | 0.258354 | 0.629048 | 0.76525 | -0.136202 | 0.294526 | 0.105318 | 0.618551 | 0.912996 | 0.159632 |
| tossup_correctness | tier | fall | 2933 | 0.65027 | 0.813888 | 0.245867 | 0.254492 | 0.638936 | 0.791681 | -0.152745 | 0.292487 | 0.104706 | 0.608433 | 0.904799 | 0.161392 |
| tossup_correctness | tier | nationals | 1584 | 0.615128 | 0.775491 | 0.170769 | 0.253904 | 0.635732 | 0.724747 | -0.0890152 | 0.288518 | 0.137545 | 0.677655 | 0.924436 | 0.156355 |
| tossup_correctness | tier | regionals | 1886 | 0.636829 | 0.833398 | 0.221472 | 0.264839 | 0.610286 | 0.746023 | -0.135737 | 0.30041 | 0.089881 | 0.596906 | 0.921302 | 0.157461 |
| tossup_correctness | tier | winter | 2892 | 0.642593 | 0.81253 | 0.228037 | 0.260478 | 0.627593 | 0.773167 | -0.145574 | 0.293968 | 0.0985424 | 0.604039 | 0.907292 | 0.161058 |
| tossup_correctness | category | Current Events | 124 | 0.585848 | 0.859769 | 0.25541 | 0.276418 | 0.58871 | 0.75 | -0.16129 | 0.283605 | 0.113821 | 0.588914 | 0.895815 | 0.167796 |
| tossup_correctness | category | Fine Arts | 1103 | 0.662633 | 0.767861 | 0.221664 | 0.2455 | 0.650045 | 0.759746 | -0.109701 | 0.287783 | 0.10929 | 0.611077 | 0.898633 | 0.163769 |
| tossup_correctness | category | Geography | 197 | 0.617016 | 0.944348 | 0.259775 | 0.301809 | 0.588832 | 0.670051 | -0.0812183 | 0.296046 | 0.0522312 | 0.493654 | 0.84817 | 0.160207 |
| tossup_correctness | category | History | 1491 | 0.661738 | 0.776949 | 0.218934 | 0.242874 | 0.66063 | 0.787391 | -0.126761 | 0.29071 | 0.117283 | 0.63396 | 0.909697 | 0.160361 |
| tossup_correctness | category | Literature | 1472 | 0.606507 | 0.799238 | 0.22354 | 0.252568 | 0.64606 | 0.804348 | -0.158288 | 0.298153 | 0.116083 | 0.685362 | 0.931645 | 0.150559 |
| tossup_correctness | category | Mythology | 332 | 0.614755 | 0.858441 | 0.301502 | 0.27616 | 0.60241 | 0.813253 | -0.210843 | 0.272262 | 0.111348 | 0.569331 | 0.862205 | 0.175475 |
| tossup_correctness | category | Other Academic | 69 | 0.559955 | 0.813486 | 0.272001 | 0.279432 | 0.565217 | 0.753623 | -0.188406 | 0.271269 | 0.150434 | 0.628432 | 0.83927 | 0.174825 |
| tossup_correctness | category | Philosophy | 324 | 0.582655 | 0.761078 | 0.22533 | 0.256679 | 0.608025 | 0.799383 | -0.191358 | 0.27715 | 0.179194 | 0.662461 | 0.921818 | 0.164022 |
| tossup_correctness | category | Popular Culture | 102 | 0.451903 | 1.21457 | 0.409027 | 0.38005 | 0.5 | 0.833333 | -0.333333 | 0.295142 | 0.0620145 | 0.475184 | 0.831278 | 0.160831 |
| tossup_correctness | category | Religion | 372 | 0.616898 | 0.850329 | 0.187521 | 0.274346 | 0.594086 | 0.709677 | -0.115591 | 0.292387 | 0.0967362 | 0.579182 | 0.898772 | 0.16305 |
| tossup_correctness | category | Science | 1487 | 0.64027 | 0.792392 | 0.208323 | 0.253728 | 0.628783 | 0.752522 | -0.123739 | 0.29322 | 0.111436 | 0.628113 | 0.918213 | 0.159625 |
| tossup_correctness | category | Social Science | 336 | 0.639153 | 0.847092 | 0.221706 | 0.271553 | 0.627976 | 0.702381 | -0.0744048 | 0.292712 | 0.0682451 | 0.554223 | 0.873779 | 0.164281 |
| tossup_correctness | category | Unknown | 1886 | 0.636829 | 0.833398 | 0.221472 | 0.264839 | 0.610286 | 0.746023 | -0.135737 | 0.30041 | 0.089881 | 0.596906 | 0.921302 | 0.157461 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.678647 | 1.33165 | 0.488326 | 0.422674 | 0.385787 | 0.736041 | -0.350254 | 0.221896 | 0.025171 | 0.187215 | 0.610372 | 0.141826 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.663613 | 1.13198 | 0.388638 | 0.356641 | 0.488325 | 0.735025 | -0.246701 | 0.265144 | 0.0328675 | 0.293404 | 0.742184 | 0.156764 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.64447 | 0.876196 | 0.274445 | 0.28383 | 0.589516 | 0.769436 | -0.17992 | 0.286135 | 0.0857553 | 0.51737 | 0.871313 | 0.168102 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.643927 | 0.726805 | 0.192393 | 0.234196 | 0.6612 | 0.78402 | -0.122819 | 0.277207 | 0.159982 | 0.656597 | 0.921947 | 0.163414 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.630967 | 0.702424 | 0.140035 | 0.219204 | 0.690254 | 0.756008 | -0.0657543 | 0.268425 | 0.213669 | 0.746477 | 0.936805 | 0.151765 |
| bonus_part_correctness | aggregate | all | 25818 | 0.886726 | 0.424619 | 0.0172196 | 0.135103 | 0.809784 | 0.518437 | 0.291347 | 0.327012 | 0.0860023 | 0.477924 | 0.932653 | 0.143048 |
| bonus_part_correctness | tier | fall | 8415 | 0.881615 | 0.425659 | 0.0267429 | 0.136635 | 0.804278 | 0.600475 | 0.203803 | 0.318357 | 0.121026 | 0.625083 | 0.941971 | 0.143102 |
| bonus_part_correctness | tier | nationals | 4179 | 0.872771 | 0.44046 | 0.0163185 | 0.139551 | 0.804738 | 0.413975 | 0.390763 | 0.310746 | 0.0741973 | 0.339616 | 0.880307 | 0.147716 |
| bonus_part_correctness | tier | regionals | 5070 | 0.88748 | 0.42042 | 0.0216155 | 0.132744 | 0.816371 | 0.477318 | 0.339053 | 0.323009 | 0.081073 | 0.409212 | 0.921848 | 0.144705 |
| bonus_part_correctness | tier | winter | 8154 | 0.890301 | 0.418038 | 0.0193138 | 0.132708 | 0.813956 | 0.512877 | 0.301079 | 0.332251 | 0.0774314 | 0.448637 | 0.937117 | 0.139568 |
| bonus_part_correctness | category | Current Events | 258 | 0.926683 | 0.357564 | 0.0650224 | 0.107254 | 0.868217 | 0.496124 | 0.372093 | 0.332832 | 0.0713001 | 0.480581 | 0.914067 | 0.138861 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.872819 | 0.448048 | 0.0223973 | 0.144373 | 0.79187 | 0.506667 | 0.285203 | 0.318194 | 0.0884048 | 0.466737 | 0.923428 | 0.148655 |
| bonus_part_correctness | category | Geography | 453 | 0.868744 | 0.444052 | 0.0320079 | 0.140907 | 0.803532 | 0.600442 | 0.203091 | 0.319445 | 0.102407 | 0.674243 | 0.939943 | 0.141591 |
| bonus_part_correctness | category | History | 4176 | 0.881576 | 0.432409 | 0.0231413 | 0.138565 | 0.799569 | 0.55364 | 0.245929 | 0.328523 | 0.0828847 | 0.555477 | 0.938529 | 0.14099 |
| bonus_part_correctness | category | Literature | 4197 | 0.90227 | 0.396838 | 0.0300197 | 0.12429 | 0.830832 | 0.508458 | 0.322373 | 0.329049 | 0.0915048 | 0.458511 | 0.934489 | 0.141724 |
| bonus_part_correctness | category | Mythology | 951 | 0.864974 | 0.448488 | 0.0453766 | 0.147392 | 0.781283 | 0.608833 | 0.17245 | 0.304859 | 0.163359 | 0.638143 | 0.941458 | 0.148885 |
| bonus_part_correctness | category | Other Academic | 258 | 0.922149 | 0.367856 | 0.0745119 | 0.114036 | 0.852713 | 0.55814 | 0.294574 | 0.33594 | 0.0672212 | 0.548555 | 0.933855 | 0.136883 |
| bonus_part_correctness | category | Philosophy | 969 | 0.873827 | 0.445532 | 0.0252718 | 0.143137 | 0.793602 | 0.493292 | 0.30031 | 0.312666 | 0.0915258 | 0.430575 | 0.918397 | 0.151817 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.855504 | 0.458984 | 0.0527293 | 0.152958 | 0.762376 | 0.620462 | 0.141914 | 0.306959 | 0.129464 | 0.629033 | 0.9451 | 0.148333 |
| bonus_part_correctness | category | Religion | 1041 | 0.881403 | 0.432907 | 0.0343187 | 0.137557 | 0.804995 | 0.509126 | 0.295869 | 0.333153 | 0.0663237 | 0.469121 | 0.92359 | 0.138995 |
| bonus_part_correctness | category | Science | 4152 | 0.886611 | 0.424128 | 0.0190899 | 0.13487 | 0.809489 | 0.529383 | 0.280106 | 0.330123 | 0.0880345 | 0.489557 | 0.936696 | 0.14086 |
| bonus_part_correctness | category | Social Science | 915 | 0.887588 | 0.42078 | 0.0375711 | 0.132802 | 0.827322 | 0.485246 | 0.342077 | 0.342418 | 0.0616471 | 0.370744 | 0.935176 | 0.131553 |
| bonus_part_correctness | category | Unknown | 5070 | 0.88748 | 0.42042 | 0.0216155 | 0.132744 | 0.816371 | 0.477318 | 0.339053 | 0.323009 | 0.081073 | 0.409212 | 0.921848 | 0.144705 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.886726 | 0.893518 | 0.00679198 | synergy |
| log_loss | 0.424619 | 0.413527 | -0.0110921 | synergy |
| ece | 0.0172196 | 0.0236442 | 0.00642459 | no-synergy |
| brier | 0.135103 | 0.131992 | -0.00311115 | synergy |
| accuracy_lift_over_all_correct | 0.291347 | 0.292432 | 0.00108451 | synergy |
| part_accuracy | 0.809784 | 0.810868 | 0.00108451 | synergy |
| part_accuracy_macro_team | 0.812382 | 0.812641 | 0.000259131 | synergy |
| part_accuracy_macro_bonus | 0.805734 | 0.807966 | 0.00223257 | synergy |
| exact_acc | 0.513479 | 0.514292 | 0.000813386 | synergy |
| ranked_probability_score | 0.11738 | 0.113116 | -0.0042646 | synergy |
| bonus_total_score_log_loss | 1.02644 | 0.996424 | -0.030016 | synergy |
| ppb_mae | 2.3728 | 1.81822 | -0.554581 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1186 | 4.56826 | 1.18785 | 0.864323 | 1.85412 | 4.03512 | 4.77996 | 5.36932 | 6.13107 | 7.11739 |
| player | theta_1 | 1186 | 0.0152751 | 0.752727 | -2.79704 | -1.41438 | -0.412719 | 0.129306 | 0.564763 | 1.03815 | 1.61486 |
| player | theta_2 | 1186 | -0.0580386 | 0.741524 | -2.67328 | -1.4689 | -0.499774 | 0.0297633 | 0.433653 | 1.04623 | 1.75381 |
| player | theta_3 | 1186 | 0.0755989 | 0.716959 | -2.37609 | -1.27982 | -0.340728 | 0.162175 | 0.577538 | 1.14839 | 1.6694 |
| player | theta_4 | 1186 | 0.0935186 | 0.727058 | -2.69764 | -1.35658 | -0.286392 | 0.226629 | 0.572716 | 1.09786 | 2.01783 |
| player | theta_5 | 1186 | 0.0347722 | 0.766565 | -2.93369 | -1.42968 | -0.390066 | 0.193693 | 0.576572 | 1.04844 | 1.88207 |
| player | theta_norm | 1186 | 1.5562 | 0.584996 | 0.361274 | 0.770285 | 1.13865 | 1.46469 | 1.86637 | 2.73562 | 3.45035 |
| tossup | beta_1 | 1240 | 0.760832 | 0.509103 | -1.1198 | 0.214056 | 0.405661 | 0.598872 | 1.00413 | 1.77438 | 2.9123 |
| tossup | beta_2 | 1240 | 0.826338 | 0.579091 | -1.76105 | 0.195392 | 0.412848 | 0.614017 | 1.1811 | 1.99614 | 3.15324 |
| tossup | beta_3 | 1240 | 0.744395 | 0.514565 | -0.28796 | 0.234736 | 0.412738 | 0.569368 | 0.875734 | 1.94395 | 2.85756 |
| tossup | beta_4 | 1240 | 0.769353 | 0.543015 | -1.3212 | 0.224574 | 0.41287 | 0.578067 | 0.952683 | 1.95817 | 2.94585 |
| tossup | beta_5 | 1240 | 0.807082 | 0.560208 | -0.210934 | 0.208999 | 0.411188 | 0.607027 | 1.1124 | 2.01313 | 2.7654 |
| tossup | gamma_1 | 1240 | 12.854 | 69.4723 | 0.365531 | 3.31685 | 4.52143 | 5.17531 | 6.23733 | 21.4946 | 1770.5 |
| tossup | gamma_2 | 1240 | 14.7265 | 81.0941 | 0.464669 | 3.34936 | 4.54521 | 5.16076 | 6.30237 | 24.1556 | 1720.01 |
| tossup | gamma_3 | 1240 | 10.9223 | 34.2147 | 1.49964 | 3.37506 | 4.55784 | 5.14194 | 6.06934 | 27.4517 | 598.251 |
| tossup | gamma_4 | 1240 | 13.536 | 76.7392 | 0.607472 | 3.22821 | 4.48536 | 5.10118 | 5.93574 | 21.1848 | 1478.5 |
| tossup | gamma_5 | 1240 | 13.8683 | 83.3381 | 0.846828 | 3.18468 | 4.48581 | 5.1712 | 6.33288 | 20.9821 | 1589.3 |
| tossup | mu_1 | 1240 | 0.501009 | 0.0983044 | 0.108214 | 0.390303 | 0.446639 | 0.47982 | 0.528273 | 0.715723 | 0.942812 |
| tossup | mu_2 | 1240 | 0.520093 | 0.123497 | 0.188005 | 0.390662 | 0.442277 | 0.47934 | 0.570697 | 0.786387 | 0.975906 |
| tossup | mu_3 | 1240 | 0.500871 | 0.103892 | 0.135798 | 0.392094 | 0.449164 | 0.476936 | 0.516623 | 0.74378 | 0.940125 |
| tossup | mu_4 | 1240 | 0.506785 | 0.110382 | 0.182948 | 0.380452 | 0.449013 | 0.482061 | 0.530572 | 0.752013 | 0.989487 |
| tossup | mu_5 | 1240 | 0.512199 | 0.110463 | 0.170474 | 0.385785 | 0.450216 | 0.485497 | 0.540906 | 0.742651 | 0.989729 |
| tossup | r_1 | 1240 | 1.04847 | 0.775211 | 0.0576672 | 0.224586 | 0.44863 | 0.815804 | 1.45764 | 2.58107 | 4.29514 |
| tossup | r_2 | 1240 | 1.2897 | 1.04727 | 0.0593185 | 0.225821 | 0.509509 | 0.89659 | 1.85168 | 3.44253 | 6.05852 |
| tossup | r_3 | 1240 | 0.98565 | 0.814206 | 0.0954514 | 0.208962 | 0.416801 | 0.705336 | 1.2328 | 2.81206 | 4.62666 |
| tossup | r_4 | 1240 | 1.0635 | 0.828683 | 0.0922437 | 0.217263 | 0.446343 | 0.806479 | 1.50646 | 2.85806 | 5.63083 |
| tossup | r_5 | 1240 | 1.13481 | 0.84271 | 0.0696721 | 0.209892 | 0.50233 | 0.905316 | 1.57284 | 2.74824 | 6.98424 |
| tossup | r_norm | 1240 | 3.05065 | 0.775539 | 0.796569 | 1.94115 | 2.49671 | 2.96674 | 3.53638 | 4.39916 | 7.15092 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
