# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_6/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_6/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 320179 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.666496 |
| log_loss | 0.51462 |
| ece | 0.0202235 |
| brier | 0.167686 |
| accuracy | 0.768478 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00322754 |
| probability_std | 0.128116 |
| probability_p10 | 0.581201 |
| probability_p50 | 0.781225 |
| probability_p90 | 0.90523 |
| mean_predictive_variance | 0.166276 |
| integrated_brier_score | 0.104496 |
| joint_tossup_event_log_loss | 7.05442 |
| buzz_position_mae | 0.163158 |
| buzz_position_median_absolute_error | 0.148803 |
| buzz_position_bias | -0.0658499 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.344917 |
| first_buzzer_mean_reciprocal_rank | 0.558554 |
| first_buzzer_log_loss | 1.71877 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.640667 |
| tossup_scorer_player_top1_accuracy | 0.322187 |
| tossup_scorer_team_top1_accuracy | 0.489384 |
| tossup_game_winner_accuracy | 0.795154 |
| tossup_game_margin_mae | 35.5767 |
| tournament_player_ppg_spearman | 0.684889 |
| tournament_player_ppg_mae | 9.2972 |
| tournament_player_ppg_top10_overlap | 0.668966 |
| neg_auroc | 0.666496 |
| neg_average_precision | 0.389992 |
| neg_precision | 0.5375 |
| neg_recall | 0.0985335 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0563588 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.093564 |
| no_buzz_calibration_error | 0.0802944 |
| no_buzz_brier | 0.026434 |
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
| tossup_correctness | aggregate | all | 9295 | 0.666496 | 0.51462 | 0.0202235 | 0.167686 | 0.768478 | 0.76525 | 0.00322754 | 0.128116 | 0.581201 | 0.781225 | 0.90523 | 0.166276 |
| tossup_correctness | tier | fall | 2933 | 0.661002 | 0.485828 | 0.0251796 | 0.155712 | 0.792704 | 0.791681 | 0.00102284 | 0.123129 | 0.600182 | 0.797062 | 0.903223 | 0.161166 |
| tossup_correctness | tier | nationals | 1584 | 0.675706 | 0.554193 | 0.0476841 | 0.185562 | 0.732323 | 0.724747 | 0.00757576 | 0.127348 | 0.498623 | 0.693326 | 0.837016 | 0.201926 |
| tossup_correctness | tier | regionals | 1886 | 0.647176 | 0.541378 | 0.0175814 | 0.179628 | 0.751326 | 0.746023 | 0.00530223 | 0.118859 | 0.594601 | 0.767885 | 0.889748 | 0.172539 |
| tossup_correctness | tier | winter | 2892 | 0.675194 | 0.504695 | 0.025826 | 0.162251 | 0.774896 | 0.773167 | 0.00172891 | 0.118827 | 0.637762 | 0.822534 | 0.925316 | 0.147848 |
| tossup_correctness | category | Current Events | 124 | 0.694762 | 0.521951 | 0.0910704 | 0.170488 | 0.790323 | 0.75 | 0.0403226 | 0.12626 | 0.518272 | 0.703723 | 0.834653 | 0.199355 |
| tossup_correctness | category | Fine Arts | 1103 | 0.637713 | 0.533958 | 0.0285626 | 0.174646 | 0.759746 | 0.759746 | 0 | 0.124983 | 0.601973 | 0.790735 | 0.91111 | 0.161754 |
| tossup_correctness | category | Geography | 197 | 0.737995 | 0.556813 | 0.0444569 | 0.188946 | 0.71066 | 0.670051 | 0.0406091 | 0.148473 | 0.470443 | 0.679427 | 0.86555 | 0.196323 |
| tossup_correctness | category | History | 1491 | 0.694197 | 0.484092 | 0.0488128 | 0.155502 | 0.78605 | 0.787391 | -0.00134138 | 0.122678 | 0.565711 | 0.761771 | 0.881589 | 0.177865 |
| tossup_correctness | category | Literature | 1472 | 0.641742 | 0.481923 | 0.0361115 | 0.150283 | 0.807065 | 0.804348 | 0.00271739 | 0.106154 | 0.677991 | 0.851553 | 0.940962 | 0.130763 |
| tossup_correctness | category | Mythology | 332 | 0.67264 | 0.465243 | 0.0627407 | 0.147925 | 0.804217 | 0.813253 | -0.00903614 | 0.111781 | 0.590211 | 0.764299 | 0.884687 | 0.174749 |
| tossup_correctness | category | Other Academic | 69 | 0.504525 | 0.588085 | 0.138788 | 0.19703 | 0.753623 | 0.753623 | 0 | 0.0972103 | 0.554049 | 0.697378 | 0.820167 | 0.205114 |
| tossup_correctness | category | Philosophy | 324 | 0.675854 | 0.472508 | 0.0301783 | 0.150711 | 0.805556 | 0.799383 | 0.00617284 | 0.118745 | 0.61447 | 0.805032 | 0.911934 | 0.158053 |
| tossup_correctness | category | Popular Culture | 102 | 0.490657 | 0.516624 | 0.128135 | 0.167281 | 0.784314 | 0.833333 | -0.0490196 | 0.117073 | 0.584084 | 0.741432 | 0.856035 | 0.185858 |
| tossup_correctness | category | Religion | 372 | 0.672559 | 0.566524 | 0.0622416 | 0.1928 | 0.693548 | 0.709677 | -0.016129 | 0.133202 | 0.55327 | 0.755358 | 0.883828 | 0.180048 |
| tossup_correctness | category | Science | 1487 | 0.68726 | 0.516152 | 0.00966742 | 0.169433 | 0.762609 | 0.752522 | 0.0100874 | 0.13891 | 0.545243 | 0.784426 | 0.901865 | 0.167294 |
| tossup_correctness | category | Social Science | 336 | 0.686017 | 0.561662 | 0.0567527 | 0.189083 | 0.708333 | 0.702381 | 0.00595238 | 0.130549 | 0.533756 | 0.73646 | 0.860618 | 0.186184 |
| tossup_correctness | category | Unknown | 1886 | 0.647176 | 0.541378 | 0.0175814 | 0.179628 | 0.751326 | 0.746023 | 0.00530223 | 0.118859 | 0.594601 | 0.767885 | 0.889748 | 0.172539 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.602785 | 0.576279 | 0.0678945 | 0.192823 | 0.741117 | 0.736041 | 0.00507614 | 0.129113 | 0.520309 | 0.681707 | 0.834748 | 0.202128 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.66111 | 0.548842 | 0.0289204 | 0.182616 | 0.729949 | 0.735025 | -0.00507614 | 0.131754 | 0.525428 | 0.735133 | 0.869926 | 0.186722 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.679607 | 0.504357 | 0.0233492 | 0.164031 | 0.774767 | 0.769436 | 0.00533096 | 0.121483 | 0.581077 | 0.772168 | 0.888569 | 0.172035 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.665447 | 0.493535 | 0.0232054 | 0.159099 | 0.783671 | 0.78402 | -0.000348918 | 0.123708 | 0.597371 | 0.79517 | 0.908764 | 0.160944 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.665651 | 0.527195 | 0.0234622 | 0.172087 | 0.763685 | 0.756008 | 0.0076769 | 0.129865 | 0.591562 | 0.796773 | 0.922584 | 0.15797 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | -0.671536 | 1.06033 | -4.706 | -3.274 | -0.484224 | -0.244893 | -0.132529 | 0.0352894 | 0.354195 |
| player | theta_2 | 1186 | -0.975768 | 1.23538 | -4.6803 | -3.44195 | -2.01256 | -0.26004 | -0.153376 | -0.0336313 | 0.324791 |
| player | theta_3 | 1186 | -0.269488 | 0.326728 | -1.75283 | -0.829219 | -0.429704 | -0.24411 | -0.113022 | 0.241372 | 1.21627 |
| player | theta_4 | 1186 | -2.1803 | 1.14281 | -5.3412 | -3.70827 | -3.01211 | -2.43974 | -1.57733 | -0.159323 | 0.83128 |
| player | theta_5 | 1186 | -0.301034 | 0.400777 | -1.76923 | -0.949409 | -0.510342 | -0.295169 | -0.117966 | 0.380259 | 1.59824 |
| player | theta_6 | 1186 | -0.252941 | 0.311325 | -1.37866 | -0.741927 | -0.415909 | -0.23686 | -0.114814 | 0.267432 | 1.63507 |
| player | theta_norm | 1186 | 3.15684 | 0.858017 | 1.38127 | 1.95291 | 2.5215 | 3.05995 | 3.67461 | 4.7117 | 6.06483 |
| tossup | start_difficulty_d1 | 1240 | -0.972996 | 1.44521 | -4.39607 | -3.58261 | -2.66518 | -0.138141 | 0.0345433 | 0.219547 | 0.427767 |
| tossup | start_difficulty_d2 | 1240 | -0.99674 | 1.53878 | -4.85 | -3.92207 | -2.64004 | -0.151087 | 0.0152771 | 0.161365 | 0.395097 |
| tossup | start_difficulty_d3 | 1240 | -0.00360775 | 0.202528 | -1.39453 | -0.39284 | -0.0786833 | 0.0341057 | 0.119609 | 0.232928 | 0.471932 |
| tossup | start_difficulty_d4 | 1240 | -1.77807 | 1.88371 | -5.8558 | -4.49543 | -3.69787 | -0.61264 | -0.0378355 | 0.223173 | 0.837514 |
| tossup | start_difficulty_d5 | 1240 | -0.0656294 | 0.447525 | -1.87499 | -1.12263 | -0.171612 | 0.055719 | 0.203862 | 0.411766 | 0.781011 |
| tossup | start_difficulty_d6 | 1240 | -0.00722172 | 0.256086 | -1.58931 | -0.444708 | -0.103833 | 0.0279028 | 0.142491 | 0.307046 | 0.612284 |
| tossup | end_difficulty_d1 | 1240 | -2.06255 | 1.63745 | -7.77814 | -5.27283 | -3.58373 | -1.15128 | -0.943986 | -0.752268 | -0.463197 |
| tossup | end_difficulty_d2 | 1240 | -2.07343 | 1.72312 | -9.35401 | -5.44861 | -3.54927 | -1.15115 | -0.962554 | -0.797716 | -0.478961 |
| tossup | end_difficulty_d3 | 1240 | -0.998992 | 0.239429 | -2.65767 | -1.44719 | -1.08709 | -0.954391 | -0.851871 | -0.7198 | -0.431524 |
| tossup | end_difficulty_d4 | 1240 | -2.85026 | 2.01034 | -11.2611 | -6.01169 | -4.75785 | -1.71895 | -1.02479 | -0.721014 | -0.0288304 |
| tossup | end_difficulty_d5 | 1240 | -1.07907 | 0.54516 | -3.33002 | -2.35359 | -1.18849 | -0.928065 | -0.748481 | -0.502421 | -0.118129 |
| tossup | end_difficulty_d6 | 1240 | -1.00549 | 0.303204 | -2.82115 | -1.51046 | -1.12157 | -0.962206 | -0.823673 | -0.640218 | -0.277639 |
| tossup | total_drop_d1 | 1240 | 1.08956 | 0.336652 | 0.607888 | 0.882684 | 0.961808 | 1.00238 | 1.05905 | 1.66716 | 4.08513 |
| tossup | total_drop_d2 | 1240 | 1.07669 | 0.380737 | 0.483521 | 0.830694 | 0.957961 | 0.995137 | 1.04542 | 1.60727 | 5.45917 |
| tossup | total_drop_d3 | 1240 | 0.995384 | 0.0519921 | 0.873712 | 0.925106 | 0.960956 | 0.989783 | 1.02188 | 1.08208 | 1.44961 |
| tossup | total_drop_d4 | 1240 | 1.07219 | 0.426027 | 0.391289 | 0.672417 | 0.921129 | 0.996791 | 1.09113 | 1.73934 | 7.63788 |
| tossup | total_drop_d5 | 1240 | 1.01344 | 0.107809 | 0.855001 | 0.901825 | 0.949431 | 0.989377 | 1.03717 | 1.23207 | 1.61555 |
| tossup | total_drop_d6 | 1240 | 0.998263 | 0.0609531 | 0.851224 | 0.914923 | 0.962621 | 0.990883 | 1.02674 | 1.09277 | 1.57041 |
| tossup | drop_share_1_d1 | 1240 | 0.328575 | 0.042421 | 0.254604 | 0.289652 | 0.301611 | 0.311603 | 0.339309 | 0.417204 | 0.517391 |
| tossup | drop_share_2_d1 | 1240 | 0.344311 | 0.0144463 | 0.286694 | 0.319235 | 0.335906 | 0.344986 | 0.353464 | 0.365796 | 0.424901 |
| tossup | drop_share_3_d1 | 1240 | 0.327114 | 0.0384726 | 0.160758 | 0.24267 | 0.320669 | 0.341643 | 0.351292 | 0.3634 | 0.38813 |
| tossup | drop_share_1_d2 | 1240 | 0.328988 | 0.0467355 | 0.23411 | 0.290809 | 0.302921 | 0.311537 | 0.331573 | 0.425338 | 0.663451 |
| tossup | drop_share_2_d2 | 1240 | 0.342708 | 0.0165472 | 0.225588 | 0.316118 | 0.334964 | 0.344091 | 0.352687 | 0.363955 | 0.469607 |
| tossup | drop_share_3_d2 | 1240 | 0.328304 | 0.0390086 | 0.110079 | 0.239333 | 0.326045 | 0.341279 | 0.351185 | 0.362608 | 0.420338 |
| tossup | drop_share_1_d3 | 1240 | 0.306326 | 0.0106787 | 0.272973 | 0.288801 | 0.299278 | 0.306121 | 0.313464 | 0.323957 | 0.353315 |
| tossup | drop_share_2_d3 | 1240 | 0.347174 | 0.0106106 | 0.308326 | 0.329962 | 0.340144 | 0.347222 | 0.354077 | 0.364407 | 0.381633 |
| tossup | drop_share_3_d3 | 1240 | 0.346501 | 0.0115746 | 0.302515 | 0.327275 | 0.338894 | 0.346449 | 0.354397 | 0.365463 | 0.382875 |
| tossup | drop_share_1_d4 | 1240 | 0.339031 | 0.058424 | 0.159805 | 0.287746 | 0.302705 | 0.316381 | 0.363004 | 0.460702 | 0.649994 |
| tossup | drop_share_2_d4 | 1240 | 0.338974 | 0.0247112 | 0.226488 | 0.29861 | 0.32593 | 0.341512 | 0.352914 | 0.370485 | 0.532809 |
| tossup | drop_share_3_d4 | 1240 | 0.321995 | 0.0495776 | 0.122701 | 0.214293 | 0.305577 | 0.337782 | 0.351407 | 0.3715 | 0.47312 |
| tossup | drop_share_1_d5 | 1240 | 0.307051 | 0.0133715 | 0.273599 | 0.28809 | 0.298333 | 0.305875 | 0.314033 | 0.331075 | 0.373121 |
| tossup | drop_share_2_d5 | 1240 | 0.347746 | 0.0109324 | 0.307679 | 0.329956 | 0.340113 | 0.347742 | 0.355571 | 0.36553 | 0.387455 |
| tossup | drop_share_3_d5 | 1240 | 0.345203 | 0.0140814 | 0.272621 | 0.319972 | 0.337691 | 0.346156 | 0.354587 | 0.365995 | 0.382489 |
| tossup | drop_share_1_d6 | 1240 | 0.306359 | 0.0113784 | 0.273148 | 0.288009 | 0.298509 | 0.306183 | 0.31368 | 0.325119 | 0.354331 |
| tossup | drop_share_2_d6 | 1240 | 0.346883 | 0.0106687 | 0.312835 | 0.329831 | 0.339539 | 0.346586 | 0.354405 | 0.364039 | 0.380262 |
| tossup | drop_share_3_d6 | 1240 | 0.346757 | 0.0114035 | 0.296914 | 0.327903 | 0.339988 | 0.346679 | 0.354497 | 0.364998 | 0.386929 |
| tossup | r_1 | 1240 | 0.210229 | 0.267575 | 0.0101492 | 0.0213591 | 0.0322086 | 0.0442847 | 0.556926 | 0.689337 | 0.784861 |
| tossup | r_2 | 1240 | 0.222637 | 0.290772 | 0.0113781 | 0.0235452 | 0.0351144 | 0.0598926 | 0.587651 | 0.770291 | 0.884702 |
| tossup | r_3 | 1240 | 0.0514127 | 0.0307077 | 0.0089541 | 0.0199281 | 0.0311601 | 0.0436255 | 0.0616581 | 0.112459 | 0.261589 |
| tossup | r_4 | 1240 | 0.390147 | 0.352839 | 0.0242288 | 0.0408686 | 0.0647042 | 0.126279 | 0.769603 | 0.871205 | 0.950544 |
| tossup | r_5 | 1240 | 0.0653021 | 0.037638 | 0.0094816 | 0.0245317 | 0.0410547 | 0.0565206 | 0.0760579 | 0.149436 | 0.251369 |
| tossup | r_6 | 1240 | 0.0602724 | 0.0310133 | 0.0094928 | 0.0240135 | 0.0394595 | 0.055147 | 0.0736423 | 0.112309 | 0.282148 |
| tossup | r_norm | 1240 | 0.72985 | 0.0870358 | 0.517823 | 0.59829 | 0.659207 | 0.726846 | 0.792554 | 0.877556 | 0.950803 |
