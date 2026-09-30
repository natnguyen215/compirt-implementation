# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_3/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_3/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 334844 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.547051 |
| log_loss | 0.612538 |
| ece | 0.107105 |
| brier | 0.192045 |
| accuracy | 0.764497 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.000753093 |
| probability_std | 0.0901657 |
| probability_p10 | 0.745281 |
| probability_p50 | 0.89438 |
| probability_p90 | 0.952616 |
| mean_predictive_variance | 0.106108 |
| integrated_brier_score | 0.172722 |
| joint_tossup_event_log_loss | 7.771 |
| buzz_position_mae | 0.338888 |
| buzz_position_median_absolute_error | 0.341908 |
| buzz_position_bias | -0.326054 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.356105 |
| first_buzzer_mean_reciprocal_rank | 0.570113 |
| first_buzzer_log_loss | 1.65542 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.626358 |
| tossup_scorer_player_top1_accuracy | 0.267304 |
| tossup_scorer_team_top1_accuracy | 0.400318 |
| tossup_game_winner_accuracy | 0.729075 |
| tossup_game_margin_mae | 42.9344 |
| tournament_player_ppg_spearman | 0.596718 |
| tournament_player_ppg_mae | 10.0456 |
| tournament_player_ppg_top10_overlap | 0.6 |
| neg_auroc | 0.547051 |
| neg_average_precision | 0.275811 |
| neg_precision | 0.405405 |
| neg_recall | 0.00687443 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.028613 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.240581 |
| no_buzz_calibration_error | 0.227311 |
| no_buzz_brier | 0.0741429 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9420 |
| first_buzzer_team_top1_accuracy_events | 9295 |
| tossup_scorer_player_top1_accuracy_events | 9420 |
| tossup_scorer_team_top1_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 454 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.547051 | 0.612538 | 0.107105 | 0.192045 | 0.764497 | 0.76525 | -0.000753093 | 0.0901657 | 0.745281 | 0.89438 | 0.952616 | 0.106108 |
| tossup_correctness | tier | fall | 2933 | 0.557074 | 0.545971 | 0.0783577 | 0.171045 | 0.790999 | 0.791681 | -0.000681896 | 0.0773935 | 0.76305 | 0.884845 | 0.943852 | 0.109933 |
| tossup_correctness | tier | nationals | 1584 | 0.561381 | 0.674914 | 0.126314 | 0.215825 | 0.722854 | 0.724747 | -0.00189394 | 0.121516 | 0.646531 | 0.885194 | 0.95413 | 0.11911 |
| tossup_correctness | tier | regionals | 1886 | 0.524667 | 0.657384 | 0.121272 | 0.208109 | 0.744433 | 0.746023 | -0.00159067 | 0.0979095 | 0.716616 | 0.885165 | 0.954606 | 0.112686 |
| tossup_correctness | tier | winter | 2892 | 0.542906 | 0.616637 | 0.121321 | 0.189842 | 0.773513 | 0.773167 | 0.000345781 | 0.0678232 | 0.810411 | 0.910251 | 0.956927 | 0.0908178 |
| tossup_correctness | category | Current Events | 124 | 0.492196 | 0.618458 | 0.100439 | 0.198038 | 0.758065 | 0.75 | 0.00806452 | 0.0940268 | 0.72856 | 0.864626 | 0.923092 | 0.12744 |
| tossup_correctness | category | Fine Arts | 1103 | 0.513996 | 0.655973 | 0.134798 | 0.202962 | 0.760653 | 0.759746 | 0.000906618 | 0.0813963 | 0.770653 | 0.909038 | 0.956248 | 0.0954638 |
| tossup_correctness | category | Geography | 197 | 0.638578 | 0.759723 | 0.202249 | 0.253401 | 0.670051 | 0.670051 | 0 | 0.0793687 | 0.774948 | 0.89441 | 0.951993 | 0.105094 |
| tossup_correctness | category | History | 1491 | 0.533787 | 0.571176 | 0.08691 | 0.17712 | 0.782696 | 0.787391 | -0.00469484 | 0.0934689 | 0.734225 | 0.880721 | 0.948661 | 0.113219 |
| tossup_correctness | category | Literature | 1472 | 0.54046 | 0.543389 | 0.0931504 | 0.164469 | 0.805027 | 0.804348 | 0.000679348 | 0.0812839 | 0.78112 | 0.908384 | 0.956897 | 0.0944999 |
| tossup_correctness | category | Mythology | 332 | 0.622282 | 0.502123 | 0.0891613 | 0.156163 | 0.816265 | 0.813253 | 0.00301205 | 0.0736944 | 0.81608 | 0.907498 | 0.951871 | 0.0944564 |
| tossup_correctness | category | Other Academic | 69 | 0.461538 | 0.657872 | 0.163291 | 0.199046 | 0.753623 | 0.753623 | 0 | 0.085907 | 0.806285 | 0.903257 | 0.943262 | 0.0996377 |
| tossup_correctness | category | Philosophy | 324 | 0.571429 | 0.537634 | 0.0858017 | 0.164325 | 0.799383 | 0.799383 | 0 | 0.0810358 | 0.770913 | 0.908185 | 0.954921 | 0.0965436 |
| tossup_correctness | category | Popular Culture | 102 | 0.428374 | 0.5123 | 0.119671 | 0.153173 | 0.833333 | 0.833333 | 0 | 0.0706 | 0.770886 | 0.895626 | 0.939022 | 0.103838 |
| tossup_correctness | category | Religion | 372 | 0.629489 | 0.687878 | 0.162198 | 0.223991 | 0.706989 | 0.709677 | -0.00268817 | 0.10281 | 0.709421 | 0.898017 | 0.951462 | 0.10411 |
| tossup_correctness | category | Science | 1487 | 0.579307 | 0.605444 | 0.103403 | 0.193526 | 0.752522 | 0.752522 | 0 | 0.0901845 | 0.734681 | 0.877733 | 0.9454 | 0.115781 |
| tossup_correctness | category | Social Science | 336 | 0.529068 | 0.766648 | 0.194965 | 0.245516 | 0.702381 | 0.702381 | 0 | 0.0835078 | 0.786254 | 0.901062 | 0.954565 | 0.0983048 |
| tossup_correctness | category | Unknown | 1886 | 0.524667 | 0.657384 | 0.121272 | 0.208109 | 0.744433 | 0.746023 | -0.00159067 | 0.0979095 | 0.716616 | 0.885165 | 0.954606 | 0.112686 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.55756 | 0.618022 | 0.109617 | 0.205717 | 0.730964 | 0.736041 | -0.00507614 | 0.101369 | 0.701489 | 0.836142 | 0.923959 | 0.138702 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.523666 | 0.652279 | 0.117352 | 0.209688 | 0.73401 | 0.735025 | -0.00101523 | 0.0909061 | 0.724722 | 0.869131 | 0.936915 | 0.121728 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.565023 | 0.583591 | 0.0933381 | 0.185598 | 0.767659 | 0.769436 | -0.00177699 | 0.0864069 | 0.749013 | 0.882516 | 0.942664 | 0.112791 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.551209 | 0.572433 | 0.0943329 | 0.17821 | 0.783671 | 0.78402 | -0.000348918 | 0.0867795 | 0.756795 | 0.894688 | 0.950063 | 0.105525 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.541452 | 0.659224 | 0.133051 | 0.203424 | 0.756008 | 0.756008 | 0 | 0.0916633 | 0.751881 | 0.913138 | 0.960462 | 0.0943663 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1186 | -1.42202 | 0.664794 | -2.99133 | -2.3369 | -1.81607 | -1.48787 | -1.10837 | -0.325954 | 2.11104 |
| player | beta | 1186 | -3.19459 | 1.05966 | -6.90758 | -5.37307 | -3.72238 | -2.94181 | -2.41661 | -1.88128 | -1.45814 |
| player | theta_1 | 1186 | 0.902679 | 0.88813 | -2.49583 | -0.706343 | 0.352593 | 0.992968 | 1.53698 | 2.20885 | 3.22733 |
| player | theta_2 | 1186 | 0.889221 | 0.938623 | -2.83552 | -0.741677 | 0.260769 | 0.992005 | 1.57991 | 2.23259 | 3.35544 |
| player | theta_3 | 1186 | 0.870401 | 0.852098 | -2.0526 | -0.713747 | 0.358849 | 0.972934 | 1.45786 | 2.10043 | 3.22031 |
| player | theta_norm | 1186 | 2.08582 | 0.637719 | 0.159337 | 0.96797 | 1.6776 | 2.13929 | 2.53595 | 3.03155 | 4.41937 |
| tossup | start_difficulty_d1 | 1240 | -1.02345 | 0.459079 | -2.25498 | -1.79079 | -1.40751 | -0.979333 | -0.650135 | -0.348171 | -0.0810142 |
| tossup | start_difficulty_d2 | 1240 | -0.981205 | 0.434 | -2.09944 | -1.70629 | -1.3331 | -0.955063 | -0.617016 | -0.34616 | -0.162758 |
| tossup | start_difficulty_d3 | 1240 | -0.954025 | 0.432617 | -2.09625 | -1.72496 | -1.28628 | -0.898888 | -0.596352 | -0.345696 | -0.159265 |
| tossup | end_difficulty_d1 | 1240 | -1.67531 | 0.360559 | -2.72811 | -2.29333 | -1.93314 | -1.65182 | -1.39029 | -1.14354 | -0.924826 |
| tossup | end_difficulty_d2 | 1240 | -1.65455 | 0.362266 | -2.77477 | -2.24942 | -1.94303 | -1.6216 | -1.35331 | -1.13024 | -0.969438 |
| tossup | end_difficulty_d3 | 1240 | -1.64028 | 0.38416 | -2.94518 | -2.37596 | -1.87984 | -1.57442 | -1.34229 | -1.13309 | -0.927732 |
| tossup | total_drop_d1 | 1240 | 0.651864 | 0.206348 | 0.202886 | 0.299511 | 0.476402 | 0.691191 | 0.81994 | 0.93 | 1.14024 |
| tossup | total_drop_d2 | 1240 | 0.673349 | 0.177696 | 0.236549 | 0.342041 | 0.549664 | 0.703019 | 0.807847 | 0.925453 | 1.12644 |
| tossup | total_drop_d3 | 1240 | 0.686256 | 0.162073 | 0.255568 | 0.376993 | 0.586059 | 0.716093 | 0.803555 | 0.908112 | 1.18662 |
| tossup | drop_share_1_d1 | 1240 | 0.326646 | 0.029541 | 0.209356 | 0.286924 | 0.309212 | 0.324064 | 0.339772 | 0.382457 | 0.464973 |
| tossup | drop_share_2_d1 | 1240 | 0.321092 | 0.0188628 | 0.253441 | 0.286261 | 0.308608 | 0.324136 | 0.33563 | 0.346534 | 0.365799 |
| tossup | drop_share_3_d1 | 1240 | 0.352262 | 0.0315224 | 0.244255 | 0.306391 | 0.333452 | 0.348147 | 0.366396 | 0.408878 | 0.509242 |
| tossup | drop_share_1_d2 | 1240 | 0.321571 | 0.0246661 | 0.214965 | 0.282465 | 0.308948 | 0.321875 | 0.334206 | 0.362865 | 0.435294 |
| tossup | drop_share_2_d2 | 1240 | 0.322919 | 0.0184739 | 0.251767 | 0.287296 | 0.31282 | 0.326533 | 0.335774 | 0.346493 | 0.366592 |
| tossup | drop_share_3_d2 | 1240 | 0.355511 | 0.0316109 | 0.262061 | 0.317345 | 0.336255 | 0.349002 | 0.368728 | 0.419501 | 0.506786 |
| tossup | drop_share_1_d3 | 1240 | 0.322819 | 0.0256858 | 0.198353 | 0.282206 | 0.309297 | 0.321859 | 0.336683 | 0.364035 | 0.417912 |
| tossup | drop_share_2_d3 | 1240 | 0.32427 | 0.0168249 | 0.255113 | 0.291769 | 0.31523 | 0.327431 | 0.336078 | 0.345711 | 0.363026 |
| tossup | drop_share_3_d3 | 1240 | 0.35291 | 0.031581 | 0.256079 | 0.312479 | 0.334463 | 0.348149 | 0.364973 | 0.41407 | 0.51424 |
| tossup | r_1 | 1240 | 0.355641 | 0.254935 | 0.0263012 | 0.0692193 | 0.1367 | 0.262973 | 0.575813 | 0.81777 | 0.90811 |
| tossup | r_2 | 1240 | 0.3335 | 0.246738 | 0.0320894 | 0.0687554 | 0.128793 | 0.244938 | 0.519838 | 0.810065 | 0.939407 |
| tossup | r_3 | 1240 | 0.310859 | 0.222697 | 0.0266029 | 0.0649596 | 0.126851 | 0.231431 | 0.471121 | 0.745919 | 0.904417 |
| tossup | r_norm | 1240 | 0.708761 | 0.0855769 | 0.577355 | 0.590991 | 0.63619 | 0.695579 | 0.777887 | 0.85835 | 0.9404 |
