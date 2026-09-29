# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_5/fold_2/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_5/fold_2`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 316003 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.669172 |
| log_loss | 0.514849 |
| ece | 0.0216361 |
| brier | 0.167851 |
| accuracy | 0.768067 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | 0.00388895 |
| probability_std | 0.134102 |
| probability_p10 | 0.564757 |
| probability_p50 | 0.777581 |
| probability_p90 | 0.903704 |
| mean_predictive_variance | 0.168079 |
| integrated_brier_score | 0.10161 |
| joint_tossup_event_log_loss | 6.88173 |
| buzz_position_mae | 0.159646 |
| buzz_position_median_absolute_error | 0.1438 |
| buzz_position_bias | -0.0644362 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.349465 |
| first_buzzer_mean_reciprocal_rank | 0.561376 |
| first_buzzer_log_loss | 1.67771 |
| first_buzzer_events | 9257 |
| first_buzzer_team_top1_accuracy | 0.653776 |
| tossup_scorer_player_top1_accuracy | 0.321855 |
| tossup_scorer_team_top1_accuracy | 0.501812 |
| tossup_game_winner_accuracy | 0.773913 |
| tossup_game_margin_mae | 36.7571 |
| tournament_player_ppg_spearman | 0.699729 |
| tournament_player_ppg_mae | 8.94786 |
| tournament_player_ppg_top10_overlap | 0.662069 |
| neg_auroc | 0.669172 |
| neg_average_precision | 0.396782 |
| neg_precision | 0.536145 |
| neg_recall | 0.122309 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.056255 |
| no_buzz_observed_rate | 0.013113 |
| no_buzz_predicted_rate | 0.0905395 |
| no_buzz_calibration_error | 0.0774265 |
| no_buzz_brier | 0.025101 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| tossup_correctness | aggregate | all | 9257 | 0.669172 | 0.514849 | 0.0216361 | 0.167851 | 0.768067 | 0.764178 | 0.00388895 | 0.134102 | 0.564757 | 0.777581 | 0.903704 | 0.168079 |
| tossup_correctness | tier | fall | 2798 | 0.679337 | 0.486919 | 0.0271852 | 0.156409 | 0.787706 | 0.785204 | 0.00250179 | 0.122891 | 0.594563 | 0.792538 | 0.902038 | 0.16316 |
| tossup_correctness | tier | nationals | 1545 | 0.690919 | 0.54964 | 0.050293 | 0.18463 | 0.723625 | 0.721036 | 0.002589 | 0.131293 | 0.497317 | 0.68767 | 0.840076 | 0.201902 |
| tossup_correctness | tier | regionals | 2039 | 0.635066 | 0.533563 | 0.0433312 | 0.17422 | 0.763119 | 0.762138 | 0.000980873 | 0.132998 | 0.576905 | 0.7887 | 0.913175 | 0.162102 |
| tossup_correctness | tier | winter | 2875 | 0.665799 | 0.510062 | 0.0215639 | 0.165453 | 0.776348 | 0.768348 | 0.008 | 0.13243 | 0.593536 | 0.799235 | 0.914621 | 0.158929 |
| tossup_correctness | category | Current Events | 129 | 0.667117 | 0.601676 | 0.0493459 | 0.20744 | 0.666667 | 0.666667 | 0 | 0.125545 | 0.527426 | 0.700053 | 0.839843 | 0.198189 |
| tossup_correctness | category | Fine Arts | 1074 | 0.646838 | 0.512787 | 0.0374485 | 0.167301 | 0.771881 | 0.776536 | -0.00465549 | 0.133765 | 0.551757 | 0.772418 | 0.897033 | 0.171131 |
| tossup_correctness | category | Geography | 180 | 0.729991 | 0.590431 | 0.0733428 | 0.201285 | 0.722222 | 0.616667 | 0.105556 | 0.159583 | 0.408501 | 0.674333 | 0.841802 | 0.200952 |
| tossup_correctness | category | History | 1454 | 0.673476 | 0.517436 | 0.0143624 | 0.169961 | 0.762724 | 0.757909 | 0.00481431 | 0.126337 | 0.5718 | 0.770038 | 0.888053 | 0.173704 |
| tossup_correctness | category | Literature | 1435 | 0.650672 | 0.465869 | 0.0303799 | 0.144849 | 0.811847 | 0.810453 | 0.00139373 | 0.115618 | 0.649076 | 0.842618 | 0.934758 | 0.137418 |
| tossup_correctness | category | Mythology | 324 | 0.654451 | 0.488934 | 0.0474602 | 0.15795 | 0.790123 | 0.79321 | -0.00308642 | 0.125785 | 0.587459 | 0.772064 | 0.889557 | 0.171834 |
| tossup_correctness | category | Other Academic | 71 | 0.375817 | 0.60166 | 0.128638 | 0.202069 | 0.732394 | 0.760563 | -0.028169 | 0.0860875 | 0.62909 | 0.725696 | 0.828582 | 0.194309 |
| tossup_correctness | category | Philosophy | 310 | 0.658326 | 0.520167 | 0.0209232 | 0.172152 | 0.758065 | 0.76129 | -0.00322581 | 0.117306 | 0.602914 | 0.783986 | 0.910782 | 0.164485 |
| tossup_correctness | category | Popular Culture | 108 | 0.557292 | 0.437054 | 0.161612 | 0.132934 | 0.851852 | 0.888889 | -0.037037 | 0.112716 | 0.588659 | 0.755758 | 0.848673 | 0.18564 |
| tossup_correctness | category | Religion | 361 | 0.680709 | 0.529995 | 0.0557068 | 0.175127 | 0.764543 | 0.742382 | 0.0221607 | 0.13328 | 0.520679 | 0.734686 | 0.865656 | 0.186946 |
| tossup_correctness | category | Science | 1445 | 0.707405 | 0.515779 | 0.0253062 | 0.170193 | 0.749481 | 0.746021 | 0.00346021 | 0.138644 | 0.521475 | 0.752 | 0.885208 | 0.179604 |
| tossup_correctness | category | Social Science | 327 | 0.712026 | 0.539157 | 0.0462474 | 0.178932 | 0.737003 | 0.718654 | 0.0183486 | 0.133214 | 0.516261 | 0.722018 | 0.85686 | 0.191328 |
| tossup_correctness | category | Unknown | 2039 | 0.635066 | 0.533563 | 0.0433312 | 0.17422 | 0.763119 | 0.762138 | 0.000980873 | 0.132998 | 0.576905 | 0.7887 | 0.913175 | 0.162102 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.603098 | 0.57974 | 0.107344 | 0.195506 | 0.715847 | 0.743169 | -0.0273224 | 0.139745 | 0.485518 | 0.677687 | 0.825921 | 0.203248 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.680546 | 0.545285 | 0.0277173 | 0.181689 | 0.741361 | 0.728796 | 0.0125654 | 0.134427 | 0.516168 | 0.729586 | 0.857873 | 0.190086 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.683885 | 0.517921 | 0.020057 | 0.170113 | 0.761947 | 0.752568 | 0.00937919 | 0.130634 | 0.555346 | 0.764466 | 0.888433 | 0.1755 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.673778 | 0.487088 | 0.0217843 | 0.156529 | 0.789217 | 0.786087 | 0.00313043 | 0.129316 | 0.586202 | 0.793933 | 0.90897 | 0.161822 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.65179 | 0.525495 | 0.0277104 | 0.170916 | 0.76406 | 0.764393 | -0.000332779 | 0.133909 | 0.581165 | 0.793987 | 0.919165 | 0.159401 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1197 | -0.666882 | 1.05384 | -4.51558 | -3.28959 | -0.465331 | -0.24912 | -0.145913 | 0.0493239 | 0.754934 |
| player | theta_2 | 1197 | -2.63862 | 0.836292 | -5.54885 | -3.89221 | -3.18228 | -2.6869 | -2.16874 | -0.767465 | 0.315568 |
| player | theta_3 | 1197 | -0.281007 | 0.380757 | -1.84691 | -0.878333 | -0.468083 | -0.266718 | -0.118913 | 0.306212 | 2.21456 |
| player | theta_4 | 1197 | -0.248507 | 0.258799 | -1.10355 | -0.677625 | -0.394717 | -0.241246 | -0.114828 | 0.166858 | 0.753229 |
| player | theta_5 | 1197 | -0.270341 | 0.468585 | -2.02188 | -1.02858 | -0.515665 | -0.271564 | -0.0707857 | 0.545629 | 1.68272 |
| player | theta_norm | 1197 | 3.04344 | 0.773616 | 1.26196 | 1.94973 | 2.48472 | 2.96941 | 3.51201 | 4.4396 | 5.85608 |
| tossup | start_difficulty_d1 | 1240 | -0.935761 | 1.41247 | -4.12777 | -3.48899 | -2.63634 | -0.131959 | 0.0510797 | 0.244467 | 0.510727 |
| tossup | start_difficulty_d2 | 1240 | -2.63885 | 1.64192 | -5.99988 | -4.5298 | -3.79256 | -3.32658 | -0.393027 | 0.0109346 | 0.433106 |
| tossup | start_difficulty_d3 | 1240 | -0.0135973 | 0.468558 | -2.10073 | -0.974999 | -0.137992 | 0.034209 | 0.194422 | 0.541093 | 2.31193 |
| tossup | start_difficulty_d4 | 1240 | -0.00765505 | 0.338637 | -2.19654 | -0.522598 | -0.0941029 | 0.0453557 | 0.159312 | 0.392276 | 1.0342 |
| tossup | start_difficulty_d5 | 1240 | -0.0526 | 0.419441 | -1.79083 | -0.940957 | -0.205336 | 0.0491648 | 0.21185 | 0.479588 | 0.752993 |
| tossup | end_difficulty_d1 | 1240 | -2.02316 | 1.60627 | -8.10545 | -5.09516 | -3.53505 | -1.14023 | -0.928686 | -0.71623 | -0.432659 |
| tossup | end_difficulty_d2 | 1240 | -3.81287 | 1.87959 | -9.85661 | -6.35902 | -5.01105 | -4.3513 | -1.44915 | -0.953455 | -0.396328 |
| tossup | end_difficulty_d3 | 1240 | -1.01806 | 0.572193 | -3.60523 | -2.16838 | -1.15282 | -0.952125 | -0.758754 | -0.359283 | 1.64052 |
| tossup | end_difficulty_d4 | 1240 | -1.00684 | 0.415146 | -4.1294 | -1.59917 | -1.10925 | -0.943934 | -0.804331 | -0.549093 | 0.185817 |
| tossup | end_difficulty_d5 | 1240 | -1.06254 | 0.512883 | -3.25596 | -2.14686 | -1.25155 | -0.932502 | -0.7388 | -0.436883 | -0.085543 |
| tossup | total_drop_d1 | 1240 | 1.08739 | 0.335688 | 0.594529 | 0.878309 | 0.960288 | 1.00162 | 1.05568 | 1.64564 | 4.35503 |
| tossup | total_drop_d2 | 1240 | 1.17402 | 0.646566 | 0.39446 | 0.638237 | 0.878235 | 1.01214 | 1.18807 | 2.29543 | 6.17604 |
| tossup | total_drop_d3 | 1240 | 1.00446 | 0.117982 | 0.671412 | 0.884388 | 0.947761 | 0.985 | 1.03087 | 1.18397 | 1.95406 |
| tossup | total_drop_d4 | 1240 | 0.999181 | 0.0897296 | 0.80733 | 0.904394 | 0.953788 | 0.987396 | 1.02401 | 1.10202 | 2.31878 |
| tossup | total_drop_d5 | 1240 | 1.00994 | 0.105725 | 0.795249 | 0.895059 | 0.946391 | 0.98623 | 1.0424 | 1.20822 | 1.89699 |
| tossup | drop_share_1_d1 | 1240 | 0.327931 | 0.0404404 | 0.257611 | 0.290517 | 0.301804 | 0.311886 | 0.340829 | 0.408921 | 0.544775 |
| tossup | drop_share_2_d1 | 1240 | 0.344359 | 0.0137152 | 0.260684 | 0.320386 | 0.336299 | 0.345271 | 0.353078 | 0.363911 | 0.411392 |
| tossup | drop_share_3_d1 | 1240 | 0.32771 | 0.0370174 | 0.179342 | 0.248245 | 0.318214 | 0.341025 | 0.351175 | 0.364452 | 0.404298 |
| tossup | drop_share_1_d2 | 1240 | 0.358754 | 0.0655971 | 0.187015 | 0.286943 | 0.310529 | 0.343892 | 0.393047 | 0.489417 | 0.681303 |
| tossup | drop_share_2_d2 | 1240 | 0.335408 | 0.0260938 | 0.215682 | 0.294973 | 0.321048 | 0.335929 | 0.349039 | 0.372239 | 0.478433 |
| tossup | drop_share_3_d2 | 1240 | 0.305838 | 0.0570326 | 0.103015 | 0.197149 | 0.271229 | 0.322293 | 0.346333 | 0.376788 | 0.476901 |
| tossup | drop_share_1_d3 | 1240 | 0.306054 | 0.0127345 | 0.269524 | 0.28552 | 0.297497 | 0.306058 | 0.313737 | 0.327166 | 0.366141 |
| tossup | drop_share_2_d3 | 1240 | 0.346983 | 0.0112362 | 0.308092 | 0.32945 | 0.338979 | 0.346753 | 0.354703 | 0.366023 | 0.387482 |
| tossup | drop_share_3_d3 | 1240 | 0.346962 | 0.0136573 | 0.28939 | 0.325017 | 0.33922 | 0.347359 | 0.35529 | 0.368483 | 0.393236 |
| tossup | drop_share_1_d4 | 1240 | 0.306436 | 0.0123046 | 0.2738 | 0.289207 | 0.298331 | 0.305708 | 0.313138 | 0.326293 | 0.388956 |
| tossup | drop_share_2_d4 | 1240 | 0.347415 | 0.010391 | 0.316222 | 0.330181 | 0.340772 | 0.347104 | 0.353985 | 0.365088 | 0.384376 |
| tossup | drop_share_3_d4 | 1240 | 0.346149 | 0.0127405 | 0.263005 | 0.325905 | 0.338667 | 0.346664 | 0.354267 | 0.364787 | 0.38089 |
| tossup | drop_share_1_d5 | 1240 | 0.30684 | 0.0127106 | 0.268593 | 0.287951 | 0.298474 | 0.30537 | 0.314394 | 0.328722 | 0.381378 |
| tossup | drop_share_2_d5 | 1240 | 0.347351 | 0.0112147 | 0.310254 | 0.329708 | 0.339377 | 0.347208 | 0.35535 | 0.366109 | 0.393518 |
| tossup | drop_share_3_d5 | 1240 | 0.345809 | 0.0134673 | 0.274415 | 0.322295 | 0.338506 | 0.34664 | 0.3554 | 0.365048 | 0.381028 |
| tossup | r_1 | 1240 | 0.22289 | 0.285435 | 0.0104645 | 0.0230416 | 0.0333181 | 0.0455092 | 0.591793 | 0.735384 | 0.836511 |
| tossup | r_2 | 1240 | 0.577694 | 0.318242 | 0.0411392 | 0.0661287 | 0.130369 | 0.737104 | 0.817966 | 0.886855 | 0.95482 |
| tossup | r_3 | 1240 | 0.0638323 | 0.0398183 | 0.0107533 | 0.0238711 | 0.0380061 | 0.0518786 | 0.0754759 | 0.15398 | 0.266091 |
| tossup | r_4 | 1240 | 0.0633015 | 0.0307944 | 0.0117119 | 0.0273963 | 0.0429794 | 0.0558395 | 0.0767716 | 0.119979 | 0.2497 |
| tossup | r_5 | 1240 | 0.0722819 | 0.0470847 | 0.0118629 | 0.0256773 | 0.0414378 | 0.0580437 | 0.0860353 | 0.171433 | 0.299776 |
| tossup | r_norm | 1240 | 0.759912 | 0.0812831 | 0.545756 | 0.628688 | 0.695303 | 0.761789 | 0.824328 | 0.88867 | 0.955088 |
