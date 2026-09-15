# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_6/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_6/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 327174 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.649895 |
| log_loss | 0.523926 |
| ece | 0.0207402 |
| brier | 0.171035 |
| accuracy | 0.767513 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00538876 |
| probability_std | 0.120583 |
| probability_p10 | 0.601576 |
| probability_p50 | 0.792496 |
| probability_p90 | 0.907259 |
| mean_predictive_variance | 0.162421 |
| integrated_brier_score | 0.100087 |
| joint_tossup_event_log_loss | 6.86462 |
| buzz_position_mae | 0.160045 |
| buzz_position_median_absolute_error | 0.145933 |
| buzz_position_bias | -0.068749 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.361157 |
| first_buzzer_mean_reciprocal_rank | 0.571563 |
| first_buzzer_log_loss | 1.65395 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.641372 |
| tossup_scorer_player_top1_accuracy | 0.329221 |
| tossup_scorer_team_top1_accuracy | 0.495779 |
| tossup_game_winner_accuracy | 0.759009 |
| tossup_game_margin_mae | 34.0762 |
| tournament_player_ppg_spearman | 0.679536 |
| tournament_player_ppg_mae | 8.81131 |
| tournament_player_ppg_top10_overlap | 0.662069 |
| neg_auroc | 0.649895 |
| neg_average_precision | 0.383428 |
| neg_precision | 0.589744 |
| neg_recall | 0.0744337 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.056742 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0964695 |
| no_buzz_calibration_error | 0.0805604 |
| no_buzz_brier | 0.0284135 |
| full_pmf_max_mass_error | 1.33227e-15 |
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
| tossup_correctness | aggregate | all | 9093 | 0.649895 | 0.523926 | 0.0207402 | 0.171035 | 0.767513 | 0.762125 | 0.00538876 | 0.120583 | 0.601576 | 0.792496 | 0.907259 | 0.162421 |
| tossup_correctness | tier | fall | 2842 | 0.670373 | 0.489516 | 0.0226634 | 0.157365 | 0.78677 | 0.785362 | 0.00140746 | 0.0983723 | 0.67197 | 0.827687 | 0.915414 | 0.14555 |
| tossup_correctness | tier | nationals | 1564 | 0.661049 | 0.568081 | 0.0491084 | 0.190862 | 0.730179 | 0.718031 | 0.0121483 | 0.118429 | 0.512392 | 0.678656 | 0.814479 | 0.207125 |
| tossup_correctness | tier | regionals | 1937 | 0.619418 | 0.536489 | 0.0217693 | 0.176407 | 0.761487 | 0.758389 | 0.00309757 | 0.105326 | 0.618019 | 0.779294 | 0.878962 | 0.170982 |
| tossup_correctness | tier | winter | 2750 | 0.64554 | 0.525525 | 0.0341866 | 0.170103 | 0.773091 | 0.765818 | 0.00727273 | 0.120002 | 0.621059 | 0.822669 | 0.923256 | 0.148403 |
| tossup_correctness | category | Current Events | 126 | 0.65695 | 0.523458 | 0.0649617 | 0.172394 | 0.753968 | 0.769841 | -0.015873 | 0.107168 | 0.556037 | 0.712748 | 0.837496 | 0.195805 |
| tossup_correctness | category | Fine Arts | 1071 | 0.655596 | 0.515192 | 0.042347 | 0.167693 | 0.78338 | 0.766573 | 0.0168067 | 0.127281 | 0.591687 | 0.786385 | 0.909936 | 0.163081 |
| tossup_correctness | category | Geography | 185 | 0.711656 | 0.547217 | 0.0411896 | 0.182993 | 0.740541 | 0.697297 | 0.0432432 | 0.150634 | 0.478373 | 0.730318 | 0.877477 | 0.186128 |
| tossup_correctness | category | History | 1440 | 0.67587 | 0.520393 | 0.0141723 | 0.170903 | 0.761111 | 0.754167 | 0.00694444 | 0.122532 | 0.569483 | 0.775767 | 0.88969 | 0.171884 |
| tossup_correctness | category | Literature | 1422 | 0.594193 | 0.484408 | 0.0559433 | 0.151507 | 0.81294 | 0.814346 | -0.00140647 | 0.112624 | 0.650571 | 0.844209 | 0.933903 | 0.138127 |
| tossup_correctness | category | Mythology | 318 | 0.694952 | 0.48697 | 0.0561031 | 0.155554 | 0.783019 | 0.789308 | -0.00628931 | 0.120154 | 0.576763 | 0.765484 | 0.882639 | 0.176277 |
| tossup_correctness | category | Other Academic | 66 | 0.590146 | 0.593076 | 0.041056 | 0.201432 | 0.69697 | 0.712121 | -0.0151515 | 0.108958 | 0.543876 | 0.712668 | 0.82771 | 0.203222 |
| tossup_correctness | category | Philosophy | 311 | 0.682344 | 0.53306 | 0.0521488 | 0.176873 | 0.73955 | 0.745981 | -0.00643087 | 0.122949 | 0.617119 | 0.805973 | 0.91518 | 0.156116 |
| tossup_correctness | category | Popular Culture | 102 | 0.627778 | 0.390307 | 0.117296 | 0.114283 | 0.862745 | 0.882353 | -0.0196078 | 0.0924838 | 0.664095 | 0.784999 | 0.8827 | 0.16382 |
| tossup_correctness | category | Religion | 358 | 0.672911 | 0.567323 | 0.0434803 | 0.191541 | 0.712291 | 0.712291 | 0 | 0.123075 | 0.57791 | 0.765408 | 0.893273 | 0.172249 |
| tossup_correctness | category | Science | 1433 | 0.670047 | 0.548688 | 0.0549451 | 0.181144 | 0.746685 | 0.738311 | 0.00837404 | 0.119143 | 0.620025 | 0.822445 | 0.917203 | 0.149806 |
| tossup_correctness | category | Social Science | 324 | 0.646006 | 0.551727 | 0.0627961 | 0.182804 | 0.75 | 0.731481 | 0.0185185 | 0.119328 | 0.579055 | 0.768245 | 0.881934 | 0.175755 |
| tossup_correctness | category | Unknown | 1937 | 0.619418 | 0.536489 | 0.0217693 | 0.176407 | 0.761487 | 0.758389 | 0.00309757 | 0.105326 | 0.618019 | 0.779294 | 0.878962 | 0.170982 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.647234 | 0.575981 | 0.0487704 | 0.193557 | 0.730539 | 0.712575 | 0.0179641 | 0.115623 | 0.541033 | 0.727954 | 0.846049 | 0.191411 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.669203 | 0.549595 | 0.0263851 | 0.182921 | 0.741228 | 0.729167 | 0.0120614 | 0.124194 | 0.550883 | 0.750235 | 0.869835 | 0.183757 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.657814 | 0.526037 | 0.0107547 | 0.172911 | 0.760284 | 0.755083 | 0.00520095 | 0.116872 | 0.597591 | 0.785702 | 0.889108 | 0.168918 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.633687 | 0.508897 | 0.0236236 | 0.164561 | 0.783052 | 0.780942 | 0.0021097 | 0.115176 | 0.616464 | 0.805776 | 0.908015 | 0.158062 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.650505 | 0.525947 | 0.0305752 | 0.170984 | 0.767921 | 0.762029 | 0.00589198 | 0.122373 | 0.613476 | 0.807465 | 0.922962 | 0.154028 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1167 | -0.832967 | 1.01095 | -4.68474 | -3.26055 | -0.738409 | -0.428577 | -0.272323 | -0.0766445 | 0.389715 |
| player | theta_2 | 1167 | -1.22609 | 1.10833 | -4.8657 | -3.32203 | -2.13607 | -0.750354 | -0.342185 | -0.121791 | 0.586241 |
| player | theta_3 | 1167 | -1.37255 | 1.06592 | -4.45306 | -3.25773 | -2.29615 | -0.878881 | -0.494866 | -0.200992 | 0.81786 |
| player | theta_4 | 1167 | -1.89348 | 0.953002 | -4.90788 | -3.47865 | -2.58202 | -1.93662 | -1.07711 | -0.536799 | 0.138741 |
| player | theta_5 | 1167 | -0.780827 | 0.464465 | -2.32633 | -1.56077 | -1.08931 | -0.756891 | -0.446172 | -0.109199 | 0.793648 |
| player | theta_6 | 1167 | -0.540197 | 0.422675 | -2.80059 | -1.32913 | -0.740075 | -0.439882 | -0.267809 | -0.0512536 | 0.598389 |
| player | theta_norm | 1167 | 3.52069 | 0.926515 | 1.56278 | 2.21976 | 2.7977 | 3.41599 | 4.1523 | 5.20369 | 6.54213 |
| tossup | start_difficulty_d1 | 1220 | -1.15586 | 1.36368 | -3.92446 | -3.49308 | -2.77328 | -0.3684 | -0.104457 | 0.107125 | 0.46272 |
| tossup | start_difficulty_d2 | 1220 | -1.26236 | 1.35201 | -4.65428 | -3.7522 | -2.43572 | -0.621588 | -0.185401 | 0.0492673 | 0.347845 |
| tossup | start_difficulty_d3 | 1220 | -1.05548 | 1.49774 | -5.05174 | -4.11426 | -1.6116 | -0.256068 | -0.0543242 | 0.123634 | 0.489328 |
| tossup | start_difficulty_d4 | 1220 | -1.7342 | 1.43503 | -5.07065 | -4.26167 | -3.09797 | -1.26255 | -0.526853 | -0.0173496 | 0.335996 |
| tossup | start_difficulty_d5 | 1220 | -0.549519 | 0.805911 | -4.00138 | -2.3492 | -0.810628 | -0.253176 | -0.0157815 | 0.188696 | 0.697788 |
| tossup | start_difficulty_d6 | 1220 | -0.34713 | 0.490241 | -2.30431 | -1.40535 | -0.531723 | -0.213226 | -0.013559 | 0.196818 | 0.77148 |
| tossup | end_difficulty_d1 | 1220 | -2.2293 | 1.51167 | -6.76331 | -4.95579 | -3.79338 | -1.37384 | -1.08576 | -0.854551 | -0.492644 |
| tossup | end_difficulty_d2 | 1220 | -2.32683 | 1.46497 | -7.21164 | -5.04161 | -3.55192 | -1.64847 | -1.16525 | -0.898124 | -0.497635 |
| tossup | end_difficulty_d3 | 1220 | -2.0814 | 1.55621 | -7.40526 | -5.23701 | -2.73768 | -1.27921 | -1.03565 | -0.821949 | -0.395172 |
| tossup | end_difficulty_d4 | 1220 | -2.78687 | 1.51249 | -7.65353 | -5.4703 | -4.11763 | -2.35213 | -1.52106 | -0.958681 | -0.556553 |
| tossup | end_difficulty_d5 | 1220 | -1.57734 | 0.906741 | -5.32016 | -3.66108 | -1.84291 | -1.25081 | -0.980547 | -0.74476 | -0.192656 |
| tossup | end_difficulty_d6 | 1220 | -1.36124 | 0.583064 | -4.00044 | -2.59397 | -1.56115 | -1.20481 | -0.983251 | -0.73256 | -0.110784 |
| tossup | total_drop_d1 | 1220 | 1.07343 | 0.251864 | 0.634563 | 0.90066 | 0.963951 | 1.00273 | 1.0635 | 1.53379 | 3.13 |
| tossup | total_drop_d2 | 1220 | 1.06448 | 0.237461 | 0.564488 | 0.859749 | 0.959569 | 1.00767 | 1.08106 | 1.48462 | 3.37067 |
| tossup | total_drop_d3 | 1220 | 1.02592 | 0.225272 | 0.550593 | 0.756637 | 0.950684 | 0.996218 | 1.05297 | 1.3767 | 3.41007 |
| tossup | total_drop_d4 | 1220 | 1.05267 | 0.24473 | 0.377866 | 0.773989 | 0.939849 | 1.00324 | 1.11456 | 1.45306 | 3.32126 |
| tossup | total_drop_d5 | 1220 | 1.02783 | 0.145884 | 0.840763 | 0.898346 | 0.945597 | 0.992333 | 1.05332 | 1.31596 | 2.62735 |
| tossup | total_drop_d6 | 1220 | 1.01411 | 0.111928 | 0.83545 | 0.906672 | 0.95591 | 0.990277 | 1.03993 | 1.2009 | 2.03441 |
| tossup | drop_share_1_d1 | 1220 | 0.332857 | 0.0415916 | 0.268428 | 0.295321 | 0.305485 | 0.31479 | 0.353502 | 0.421847 | 0.509392 |
| tossup | drop_share_2_d1 | 1220 | 0.343291 | 0.0133972 | 0.292784 | 0.31894 | 0.336115 | 0.343833 | 0.351924 | 0.363091 | 0.441817 |
| tossup | drop_share_3_d1 | 1220 | 0.323852 | 0.0368671 | 0.173083 | 0.243112 | 0.311108 | 0.338126 | 0.348005 | 0.359013 | 0.384648 |
| tossup | drop_share_1_d2 | 1220 | 0.333711 | 0.0401772 | 0.267624 | 0.296671 | 0.308587 | 0.319185 | 0.343751 | 0.423495 | 0.5337 |
| tossup | drop_share_2_d2 | 1220 | 0.342565 | 0.0141768 | 0.27737 | 0.317356 | 0.335831 | 0.343945 | 0.352027 | 0.361624 | 0.395003 |
| tossup | drop_share_3_d2 | 1220 | 0.323725 | 0.0340375 | 0.177426 | 0.249924 | 0.314434 | 0.335466 | 0.344833 | 0.358047 | 0.400796 |
| tossup | drop_share_1_d3 | 1220 | 0.324562 | 0.0405335 | 0.234034 | 0.292869 | 0.304041 | 0.311955 | 0.325165 | 0.411635 | 0.709046 |
| tossup | drop_share_2_d3 | 1220 | 0.342681 | 0.0175937 | 0.201157 | 0.309737 | 0.336063 | 0.345224 | 0.352918 | 0.364442 | 0.415382 |
| tossup | drop_share_3_d3 | 1220 | 0.332757 | 0.0343753 | 0.0897965 | 0.264017 | 0.328808 | 0.341407 | 0.350708 | 0.364138 | 0.429776 |
| tossup | drop_share_1_d4 | 1220 | 0.340355 | 0.0457176 | 0.228154 | 0.298937 | 0.313174 | 0.326385 | 0.349216 | 0.443161 | 0.660764 |
| tossup | drop_share_2_d4 | 1220 | 0.339771 | 0.0189399 | 0.210041 | 0.305846 | 0.331183 | 0.342141 | 0.350674 | 0.362381 | 0.503655 |
| tossup | drop_share_3_d4 | 1220 | 0.319874 | 0.0376699 | 0.129195 | 0.239531 | 0.309801 | 0.33029 | 0.341548 | 0.358741 | 0.446585 |
| tossup | drop_share_1_d5 | 1220 | 0.315141 | 0.0161692 | 0.278748 | 0.295102 | 0.30519 | 0.312249 | 0.32102 | 0.349979 | 0.392343 |
| tossup | drop_share_2_d5 | 1220 | 0.346374 | 0.0101953 | 0.315995 | 0.329608 | 0.339149 | 0.346671 | 0.35377 | 0.361814 | 0.38145 |
| tossup | drop_share_3_d5 | 1220 | 0.338485 | 0.0170855 | 0.241194 | 0.305318 | 0.331056 | 0.340521 | 0.349374 | 0.362999 | 0.382732 |
| tossup | drop_share_1_d6 | 1220 | 0.312323 | 0.0114321 | 0.279351 | 0.294946 | 0.304874 | 0.311189 | 0.31887 | 0.332085 | 0.36236 |
| tossup | drop_share_2_d6 | 1220 | 0.346896 | 0.00935128 | 0.314516 | 0.33191 | 0.340508 | 0.347208 | 0.353024 | 0.362436 | 0.374852 |
| tossup | drop_share_3_d6 | 1220 | 0.34078 | 0.01284 | 0.28293 | 0.319782 | 0.333515 | 0.34171 | 0.349359 | 0.359537 | 0.374708 |
| tossup | r_1 | 1220 | 0.196071 | 0.236992 | 0.0118654 | 0.0215257 | 0.0338391 | 0.0474001 | 0.483476 | 0.623071 | 0.743629 |
| tossup | r_2 | 1220 | 0.200328 | 0.231387 | 0.0158989 | 0.0256575 | 0.0404867 | 0.0728458 | 0.274122 | 0.67099 | 0.832662 |
| tossup | r_3 | 1220 | 0.186599 | 0.248156 | 0.0139665 | 0.0269041 | 0.0403067 | 0.0594208 | 0.138814 | 0.720748 | 0.853763 |
| tossup | r_4 | 1220 | 0.275365 | 0.272349 | 0.0294721 | 0.045663 | 0.0751431 | 0.139119 | 0.391446 | 0.791334 | 0.919718 |
| tossup | r_5 | 1220 | 0.0769414 | 0.0526528 | 0.0172155 | 0.0295795 | 0.0440544 | 0.0586122 | 0.084748 | 0.208504 | 0.296983 |
| tossup | r_6 | 1220 | 0.0646952 | 0.0393585 | 0.0107869 | 0.0225561 | 0.0374044 | 0.0551498 | 0.0775937 | 0.150715 | 0.2642 |
| tossup | r_norm | 1220 | 0.665093 | 0.0809913 | 0.478979 | 0.547895 | 0.601705 | 0.656226 | 0.722759 | 0.809537 | 0.920441 |
