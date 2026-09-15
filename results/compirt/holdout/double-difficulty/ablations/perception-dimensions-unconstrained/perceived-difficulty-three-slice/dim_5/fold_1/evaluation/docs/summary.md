# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_5/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_5/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 323573 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.661967 |
| log_loss | 0.517769 |
| ece | 0.0187105 |
| brier | 0.169071 |
| accuracy | 0.770373 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.0082481 |
| probability_std | 0.1215 |
| probability_p10 | 0.593702 |
| probability_p50 | 0.786196 |
| probability_p90 | 0.901357 |
| mean_predictive_variance | 0.165618 |
| integrated_brier_score | 0.100992 |
| joint_tossup_event_log_loss | 6.86758 |
| buzz_position_mae | 0.161574 |
| buzz_position_median_absolute_error | 0.146567 |
| buzz_position_bias | -0.0712194 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.356318 |
| first_buzzer_mean_reciprocal_rank | 0.567789 |
| first_buzzer_log_loss | 1.66401 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.644452 |
| tossup_scorer_player_top1_accuracy | 0.329004 |
| tossup_scorer_team_top1_accuracy | 0.492965 |
| tossup_game_winner_accuracy | 0.774775 |
| tossup_game_margin_mae | 33.8929 |
| tournament_player_ppg_spearman | 0.675474 |
| tournament_player_ppg_mae | 8.87493 |
| tournament_player_ppg_top10_overlap | 0.686207 |
| neg_auroc | 0.661967 |
| neg_average_precision | 0.397308 |
| neg_precision | 0.619048 |
| neg_recall | 0.0901526 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0561156 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0953444 |
| no_buzz_calibration_error | 0.0794353 |
| no_buzz_brier | 0.0282811 |
| full_pmf_max_mass_error | 1.44329e-15 |
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
| tossup_correctness | aggregate | all | 9093 | 0.661967 | 0.517769 | 0.0187105 | 0.169071 | 0.770373 | 0.762125 | 0.0082481 | 0.1215 | 0.593702 | 0.786196 | 0.901357 | 0.165618 |
| tossup_correctness | tier | fall | 2842 | 0.704137 | 0.474988 | 0.0164905 | 0.152686 | 0.789585 | 0.785362 | 0.00422238 | 0.10999 | 0.62743 | 0.805328 | 0.902127 | 0.158187 |
| tossup_correctness | tier | nationals | 1564 | 0.660403 | 0.565714 | 0.0453353 | 0.189554 | 0.734655 | 0.718031 | 0.016624 | 0.126298 | 0.50766 | 0.696683 | 0.834757 | 0.200154 |
| tossup_correctness | tier | regionals | 1937 | 0.635514 | 0.531732 | 0.0254317 | 0.175162 | 0.764068 | 0.758389 | 0.00567888 | 0.111775 | 0.598134 | 0.762622 | 0.879332 | 0.175956 |
| tossup_correctness | tier | winter | 2750 | 0.642472 | 0.52488 | 0.0405067 | 0.170064 | 0.775273 | 0.765818 | 0.00945455 | 0.113565 | 0.638513 | 0.826363 | 0.921332 | 0.146374 |
| tossup_correctness | category | Current Events | 126 | 0.710985 | 0.508989 | 0.0906988 | 0.165639 | 0.777778 | 0.769841 | 0.00793651 | 0.106884 | 0.54993 | 0.712826 | 0.837587 | 0.197673 |
| tossup_correctness | category | Fine Arts | 1071 | 0.680711 | 0.504505 | 0.0302762 | 0.163914 | 0.784314 | 0.766573 | 0.0177404 | 0.127146 | 0.58523 | 0.77628 | 0.901932 | 0.168819 |
| tossup_correctness | category | Geography | 185 | 0.759275 | 0.520083 | 0.062492 | 0.171188 | 0.740541 | 0.697297 | 0.0432432 | 0.161896 | 0.475469 | 0.746057 | 0.883287 | 0.181007 |
| tossup_correctness | category | History | 1440 | 0.681272 | 0.519074 | 0.0295274 | 0.170605 | 0.767361 | 0.754167 | 0.0131944 | 0.125616 | 0.58958 | 0.804261 | 0.908027 | 0.159398 |
| tossup_correctness | category | Literature | 1422 | 0.606087 | 0.478378 | 0.041713 | 0.150137 | 0.80872 | 0.814346 | -0.00562588 | 0.109314 | 0.645346 | 0.815338 | 0.917524 | 0.151288 |
| tossup_correctness | category | Mythology | 318 | 0.702147 | 0.476466 | 0.0744342 | 0.151504 | 0.811321 | 0.789308 | 0.0220126 | 0.118472 | 0.5747 | 0.763702 | 0.89042 | 0.176724 |
| tossup_correctness | category | Other Academic | 66 | 0.600224 | 0.59358 | 0.0701543 | 0.201811 | 0.681818 | 0.712121 | -0.030303 | 0.112665 | 0.539039 | 0.725173 | 0.848172 | 0.196923 |
| tossup_correctness | category | Philosophy | 311 | 0.677433 | 0.531781 | 0.0519013 | 0.176631 | 0.73955 | 0.745981 | -0.00643087 | 0.118223 | 0.62118 | 0.802987 | 0.903548 | 0.158697 |
| tossup_correctness | category | Popular Culture | 102 | 0.634259 | 0.396133 | 0.1165 | 0.116565 | 0.882353 | 0.882353 | 0 | 0.101485 | 0.639776 | 0.781852 | 0.879649 | 0.169023 |
| tossup_correctness | category | Religion | 358 | 0.660956 | 0.573612 | 0.0577991 | 0.193394 | 0.72067 | 0.712291 | 0.00837989 | 0.126294 | 0.572681 | 0.775333 | 0.893823 | 0.170738 |
| tossup_correctness | category | Science | 1433 | 0.678813 | 0.539205 | 0.0385331 | 0.178202 | 0.743196 | 0.738311 | 0.00488486 | 0.12094 | 0.599572 | 0.80157 | 0.910195 | 0.159038 |
| tossup_correctness | category | Social Science | 324 | 0.670838 | 0.540752 | 0.0981122 | 0.178695 | 0.768519 | 0.731481 | 0.037037 | 0.128595 | 0.552048 | 0.764914 | 0.88982 | 0.174257 |
| tossup_correctness | category | Unknown | 1937 | 0.635514 | 0.531732 | 0.0254317 | 0.175162 | 0.764068 | 0.758389 | 0.00567888 | 0.111775 | 0.598134 | 0.762622 | 0.879332 | 0.175956 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.636029 | 0.574732 | 0.0567097 | 0.193694 | 0.742515 | 0.712575 | 0.0299401 | 0.104969 | 0.565226 | 0.718331 | 0.828586 | 0.19889 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.671225 | 0.547755 | 0.0369303 | 0.182179 | 0.747807 | 0.729167 | 0.0186404 | 0.127585 | 0.53042 | 0.735936 | 0.861009 | 0.188727 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.671749 | 0.519221 | 0.0198303 | 0.170194 | 0.767849 | 0.755083 | 0.012766 | 0.118183 | 0.590377 | 0.779495 | 0.886638 | 0.170698 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.645235 | 0.50477 | 0.0210037 | 0.163231 | 0.781997 | 0.780942 | 0.00105485 | 0.117281 | 0.610667 | 0.797368 | 0.903786 | 0.161593 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.666294 | 0.5168 | 0.0217652 | 0.168471 | 0.769558 | 0.762029 | 0.00752864 | 0.120832 | 0.61265 | 0.801576 | 0.917322 | 0.15713 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | -1.29813 | 1.21052 | -4.48452 | -3.44476 | -2.44615 | -0.557137 | -0.324326 | -0.125934 | 0.258166 |
| player | theta_2 | 1167 | -2.48042 | 0.746572 | -4.7825 | -3.63198 | -2.96619 | -2.47043 | -2.12034 | -0.986017 | -0.00546994 |
| player | theta_3 | 1167 | -0.859794 | 0.599531 | -3.39691 | -1.88521 | -1.34502 | -0.773045 | -0.329934 | -0.117826 | 0.225193 |
| player | theta_4 | 1167 | -0.874556 | 0.491202 | -2.85944 | -1.7424 | -1.13096 | -0.822624 | -0.569805 | -0.140903 | 0.937628 |
| player | theta_5 | 1167 | -0.527193 | 0.369742 | -2.10542 | -1.23129 | -0.726676 | -0.4719 | -0.280839 | -0.0134256 | 0.625398 |
| player | theta_norm | 1167 | 3.43148 | 0.776485 | 1.68127 | 2.2974 | 2.83645 | 3.34498 | 3.95302 | 4.81182 | 6.12693 |
| tossup | start_difficulty_d1 | 1220 | -1.71406 | 1.37556 | -4.43374 | -3.49576 | -3.00401 | -2.1054 | -0.247283 | 0.141697 | 0.433757 |
| tossup | start_difficulty_d2 | 1220 | -2.45865 | 1.4759 | -4.99538 | -4.2088 | -3.59871 | -3.05144 | -0.75084 | -0.0462142 | 0.366685 |
| tossup | start_difficulty_d3 | 1220 | -0.735181 | 1.02292 | -4.71575 | -2.9602 | -1.12148 | -0.27538 | -0.0529475 | 0.139071 | 0.553171 |
| tossup | start_difficulty_d4 | 1220 | -0.660861 | 0.820226 | -3.45754 | -2.45273 | -1.05203 | -0.410037 | -0.0502326 | 0.230928 | 0.725986 |
| tossup | start_difficulty_d5 | 1220 | -0.319739 | 0.537218 | -2.74091 | -1.44158 | -0.469134 | -0.177685 | 0.00155079 | 0.217765 | 0.889988 |
| tossup | end_difficulty_d1 | 1220 | -2.81002 | 1.52624 | -7.68903 | -5.05913 | -4.11263 | -3.09813 | -1.24063 | -0.814441 | -0.479871 |
| tossup | end_difficulty_d2 | 1220 | -3.56828 | 1.61415 | -9.75061 | -5.6615 | -4.77983 | -4.02556 | -1.85989 | -1.0073 | -0.548731 |
| tossup | end_difficulty_d3 | 1220 | -1.75583 | 1.09198 | -5.96771 | -4.11493 | -2.21006 | -1.27773 | -1.02937 | -0.796464 | -0.307304 |
| tossup | end_difficulty_d4 | 1220 | -1.69028 | 0.910443 | -5.24896 | -3.58892 | -2.09603 | -1.40999 | -1.01949 | -0.688972 | -0.145838 |
| tossup | end_difficulty_d5 | 1220 | -1.34101 | 0.659833 | -5.38624 | -2.64286 | -1.49881 | -1.17213 | -0.959277 | -0.706278 | 0.0484623 |
| tossup | total_drop_d1 | 1220 | 1.09597 | 0.304275 | 0.601552 | 0.824939 | 0.950064 | 1.00748 | 1.13758 | 1.65174 | 4.18704 |
| tossup | total_drop_d2 | 1220 | 1.10964 | 0.453348 | 0.385233 | 0.67744 | 0.912283 | 1.01858 | 1.17898 | 1.7643 | 6.37151 |
| tossup | total_drop_d3 | 1220 | 1.02065 | 0.149075 | 0.741659 | 0.883399 | 0.952 | 0.992538 | 1.04054 | 1.27948 | 2.80991 |
| tossup | total_drop_d4 | 1220 | 1.02942 | 0.125775 | 0.79019 | 0.894396 | 0.950582 | 0.999745 | 1.0742 | 1.26405 | 1.99601 |
| tossup | total_drop_d5 | 1220 | 1.02127 | 0.147197 | 0.841526 | 0.90687 | 0.955454 | 0.99309 | 1.04068 | 1.2094 | 2.97079 |
| tossup | drop_share_1_d1 | 1220 | 0.345532 | 0.0423664 | 0.249353 | 0.298588 | 0.311435 | 0.331976 | 0.376168 | 0.42215 | 0.560177 |
| tossup | drop_share_2_d1 | 1220 | 0.34112 | 0.0143543 | 0.28542 | 0.316268 | 0.333054 | 0.34205 | 0.349782 | 0.361843 | 0.427656 |
| tossup | drop_share_3_d1 | 1220 | 0.313347 | 0.0386935 | 0.154403 | 0.238179 | 0.288013 | 0.326631 | 0.343605 | 0.3571 | 0.405079 |
| tossup | drop_share_1_d2 | 1220 | 0.356662 | 0.0535199 | 0.219284 | 0.296187 | 0.316233 | 0.344688 | 0.387805 | 0.45142 | 0.697603 |
| tossup | drop_share_2_d2 | 1220 | 0.335424 | 0.022218 | 0.19153 | 0.299955 | 0.322428 | 0.336834 | 0.348839 | 0.365794 | 0.478472 |
| tossup | drop_share_3_d2 | 1220 | 0.307914 | 0.046499 | 0.110867 | 0.22196 | 0.280781 | 0.319108 | 0.340784 | 0.36296 | 0.450113 |
| tossup | drop_share_1_d3 | 1220 | 0.317193 | 0.0166604 | 0.26325 | 0.295617 | 0.306848 | 0.314421 | 0.323967 | 0.350121 | 0.406511 |
| tossup | drop_share_2_d3 | 1220 | 0.345827 | 0.0104486 | 0.311128 | 0.327484 | 0.339107 | 0.346578 | 0.352804 | 0.362553 | 0.38181 |
| tossup | drop_share_3_d3 | 1220 | 0.33698 | 0.0164616 | 0.276175 | 0.30535 | 0.328448 | 0.339166 | 0.347538 | 0.359657 | 0.39884 |
| tossup | drop_share_1_d4 | 1220 | 0.315907 | 0.0161503 | 0.27911 | 0.294762 | 0.305515 | 0.313227 | 0.322635 | 0.347207 | 0.404899 |
| tossup | drop_share_2_d4 | 1220 | 0.346487 | 0.00980427 | 0.314351 | 0.330167 | 0.340024 | 0.346212 | 0.353113 | 0.362725 | 0.377093 |
| tossup | drop_share_3_d4 | 1220 | 0.337606 | 0.0159985 | 0.251289 | 0.307209 | 0.33006 | 0.339372 | 0.348343 | 0.359346 | 0.377506 |
| tossup | drop_share_1_d5 | 1220 | 0.312735 | 0.0136055 | 0.274034 | 0.29434 | 0.304601 | 0.311177 | 0.318828 | 0.333353 | 0.386245 |
| tossup | drop_share_2_d5 | 1220 | 0.346799 | 0.00905616 | 0.320451 | 0.331642 | 0.340601 | 0.346929 | 0.352821 | 0.361681 | 0.375365 |
| tossup | drop_share_3_d5 | 1220 | 0.340466 | 0.0145634 | 0.248221 | 0.316995 | 0.333631 | 0.342058 | 0.349329 | 0.360099 | 0.374829 |
| tossup | r_1 | 1220 | 0.3011 | 0.262076 | 0.0146973 | 0.025013 | 0.0401883 | 0.277544 | 0.561512 | 0.701795 | 0.813747 |
| tossup | r_2 | 1220 | 0.442435 | 0.26746 | 0.0406497 | 0.0575134 | 0.122654 | 0.497716 | 0.6743 | 0.806932 | 0.915488 |
| tossup | r_3 | 1220 | 0.10038 | 0.0866389 | 0.00762032 | 0.0241263 | 0.0414005 | 0.0637971 | 0.132379 | 0.282229 | 0.482033 |
| tossup | r_4 | 1220 | 0.0903477 | 0.057837 | 0.0181475 | 0.0339428 | 0.0473534 | 0.0696368 | 0.116055 | 0.2169 | 0.311306 |
| tossup | r_5 | 1220 | 0.0657376 | 0.040554 | 0.00962701 | 0.0242695 | 0.0378011 | 0.0546174 | 0.0791155 | 0.156669 | 0.258703 |
| tossup | r_norm | 1220 | 0.675017 | 0.0769192 | 0.518097 | 0.567169 | 0.616127 | 0.66454 | 0.723269 | 0.815777 | 0.917121 |
