# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_5/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-difficulty-three-slice/dim_5/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 320054 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.668694 |
| log_loss | 0.512167 |
| ece | 0.00936119 |
| brier | 0.167292 |
| accuracy | 0.769016 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | 0.00376547 |
| probability_std | 0.122659 |
| probability_p10 | 0.590897 |
| probability_p50 | 0.785591 |
| probability_p90 | 0.900958 |
| mean_predictive_variance | 0.165548 |
| integrated_brier_score | 0.102136 |
| joint_tossup_event_log_loss | 6.88698 |
| buzz_position_mae | 0.161865 |
| buzz_position_median_absolute_error | 0.148575 |
| buzz_position_bias | -0.0667709 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.363421 |
| first_buzzer_mean_reciprocal_rank | 0.573108 |
| first_buzzer_log_loss | 1.66011 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.649597 |
| tossup_scorer_player_top1_accuracy | 0.328344 |
| tossup_scorer_team_top1_accuracy | 0.491614 |
| tossup_game_winner_accuracy | 0.803965 |
| tossup_game_margin_mae | 34.2422 |
| tournament_player_ppg_spearman | 0.692889 |
| tournament_player_ppg_mae | 8.91262 |
| tournament_player_ppg_top10_overlap | 0.655172 |
| neg_auroc | 0.668694 |
| neg_average_precision | 0.387987 |
| neg_precision | 0.55132 |
| neg_recall | 0.0861595 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0551915 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.0924397 |
| no_buzz_calibration_error | 0.07917 |
| no_buzz_brier | 0.026009 |
| full_pmf_max_mass_error | 1.44329e-15 |
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
| tossup_correctness | aggregate | all | 9295 | 0.668694 | 0.512167 | 0.00936119 | 0.167292 | 0.769016 | 0.76525 | 0.00376547 | 0.122659 | 0.590897 | 0.785591 | 0.900958 | 0.165548 |
| tossup_correctness | tier | fall | 2933 | 0.665752 | 0.48246 | 0.0191555 | 0.154578 | 0.795431 | 0.791681 | 0.00375043 | 0.119607 | 0.60528 | 0.79935 | 0.900461 | 0.161235 |
| tossup_correctness | tier | nationals | 1584 | 0.665265 | 0.559177 | 0.0474742 | 0.1879 | 0.731061 | 0.724747 | 0.00631313 | 0.122805 | 0.502444 | 0.690727 | 0.827188 | 0.203425 |
| tossup_correctness | tier | regionals | 1886 | 0.652169 | 0.538715 | 0.0209145 | 0.179019 | 0.747084 | 0.746023 | 0.00106045 | 0.106509 | 0.618952 | 0.779043 | 0.891607 | 0.167849 |
| tossup_correctness | tier | winter | 2892 | 0.681835 | 0.499235 | 0.0263911 | 0.161252 | 0.777317 | 0.773167 | 0.00414938 | 0.112966 | 0.649028 | 0.82296 | 0.919386 | 0.147676 |
| tossup_correctness | category | Current Events | 124 | 0.70274 | 0.518656 | 0.0804361 | 0.169147 | 0.782258 | 0.75 | 0.0322581 | 0.125189 | 0.508009 | 0.720978 | 0.851902 | 0.196554 |
| tossup_correctness | category | Fine Arts | 1103 | 0.640145 | 0.531694 | 0.0273325 | 0.174544 | 0.757933 | 0.759746 | -0.00181324 | 0.124828 | 0.588681 | 0.7839 | 0.903818 | 0.165106 |
| tossup_correctness | category | Geography | 197 | 0.737646 | 0.559198 | 0.0531298 | 0.189764 | 0.685279 | 0.670051 | 0.0152284 | 0.159208 | 0.469089 | 0.690995 | 0.878706 | 0.190718 |
| tossup_correctness | category | History | 1491 | 0.705491 | 0.479662 | 0.0477892 | 0.154132 | 0.78672 | 0.787391 | -0.000670691 | 0.124883 | 0.558886 | 0.763757 | 0.88399 | 0.176333 |
| tossup_correctness | category | Literature | 1472 | 0.639291 | 0.476255 | 0.0240663 | 0.150331 | 0.807745 | 0.804348 | 0.00339674 | 0.11182 | 0.643696 | 0.825599 | 0.91972 | 0.146987 |
| tossup_correctness | category | Mythology | 332 | 0.677121 | 0.463629 | 0.0620543 | 0.147678 | 0.801205 | 0.813253 | -0.0120482 | 0.111285 | 0.586559 | 0.766201 | 0.882167 | 0.174515 |
| tossup_correctness | category | Other Academic | 69 | 0.536199 | 0.571039 | 0.102173 | 0.191178 | 0.768116 | 0.753623 | 0.0144928 | 0.0971335 | 0.539125 | 0.711449 | 0.826725 | 0.200931 |
| tossup_correctness | category | Philosophy | 324 | 0.684526 | 0.46874 | 0.0325454 | 0.14879 | 0.802469 | 0.799383 | 0.00308642 | 0.123102 | 0.588381 | 0.787472 | 0.903041 | 0.162971 |
| tossup_correctness | category | Popular Culture | 102 | 0.413149 | 0.507599 | 0.1093 | 0.160341 | 0.823529 | 0.833333 | -0.00980392 | 0.0967024 | 0.656883 | 0.780355 | 0.880449 | 0.167407 |
| tossup_correctness | category | Religion | 372 | 0.679994 | 0.56191 | 0.0508129 | 0.19098 | 0.725806 | 0.709677 | 0.016129 | 0.134609 | 0.538935 | 0.754528 | 0.886678 | 0.178663 |
| tossup_correctness | category | Science | 1487 | 0.686368 | 0.51974 | 0.0310768 | 0.170615 | 0.765299 | 0.752522 | 0.0127774 | 0.125043 | 0.60504 | 0.814149 | 0.918049 | 0.153936 |
| tossup_correctness | category | Social Science | 336 | 0.692373 | 0.56121 | 0.0467262 | 0.190003 | 0.708333 | 0.702381 | 0.00595238 | 0.127838 | 0.5475 | 0.737132 | 0.862297 | 0.184003 |
| tossup_correctness | category | Unknown | 1886 | 0.652169 | 0.538715 | 0.0209145 | 0.179019 | 0.747084 | 0.746023 | 0.00106045 | 0.106509 | 0.618952 | 0.779043 | 0.891607 | 0.167849 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.640451 | 0.561526 | 0.0749513 | 0.186467 | 0.751269 | 0.736041 | 0.0152284 | 0.1242 | 0.530171 | 0.696195 | 0.827529 | 0.200423 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.655691 | 0.54777 | 0.0254048 | 0.181695 | 0.747208 | 0.735025 | 0.0121827 | 0.127012 | 0.546538 | 0.740377 | 0.866368 | 0.18523 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.679919 | 0.503346 | 0.0185906 | 0.163534 | 0.77299 | 0.769436 | 0.00355398 | 0.118436 | 0.582268 | 0.778235 | 0.88731 | 0.170804 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.66823 | 0.490973 | 0.0145339 | 0.158707 | 0.783671 | 0.78402 | -0.000348918 | 0.120224 | 0.603319 | 0.798358 | 0.905044 | 0.160629 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.670701 | 0.52412 | 0.0258349 | 0.172333 | 0.760347 | 0.756008 | 0.00433912 | 0.120777 | 0.608 | 0.801222 | 0.913846 | 0.157541 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1186 | -1.1551 | 1.15803 | -4.46132 | -3.3568 | -2.23069 | -0.487739 | -0.279583 | -0.114712 | 0.280573 |
| player | theta_2 | 1186 | -2.54923 | 0.748336 | -5.16882 | -3.73801 | -3.03742 | -2.55561 | -2.15029 | -1.00606 | -0.120963 |
| player | theta_3 | 1186 | -0.689043 | 0.490567 | -2.42879 | -1.58468 | -1.02571 | -0.57319 | -0.302388 | -0.0601139 | 0.333883 |
| player | theta_4 | 1186 | -0.717272 | 0.390569 | -2.29298 | -1.39035 | -0.944436 | -0.689054 | -0.470208 | -0.145404 | 0.926159 |
| player | theta_5 | 1186 | -0.51382 | 0.432633 | -2.55618 | -1.4529 | -0.684967 | -0.414064 | -0.243604 | 0.0140129 | 0.546848 |
| player | theta_norm | 1186 | 3.30684 | 0.794218 | 1.53748 | 2.11555 | 2.71851 | 3.23887 | 3.81521 | 4.74931 | 5.9156 |
| tossup | start_difficulty_d1 | 1240 | -1.54713 | 1.33797 | -4.08569 | -3.42682 | -2.88046 | -1.51459 | -0.181801 | 0.146207 | 0.494126 |
| tossup | start_difficulty_d2 | 1240 | -2.58693 | 1.49487 | -5.22894 | -4.22442 | -3.67606 | -3.2494 | -0.718324 | -0.072723 | 0.305284 |
| tossup | start_difficulty_d3 | 1240 | -0.562015 | 0.792131 | -3.76232 | -2.2681 | -0.835336 | -0.242942 | -0.0309024 | 0.15022 | 0.404768 |
| tossup | start_difficulty_d4 | 1240 | -0.479323 | 0.724494 | -3.19262 | -2.29816 | -0.676102 | -0.234508 | -0.0197683 | 0.227083 | 0.762874 |
| tossup | start_difficulty_d5 | 1240 | -0.354598 | 0.524323 | -2.44843 | -1.41772 | -0.638036 | -0.234585 | 0.0120714 | 0.292105 | 1.14913 |
| tossup | end_difficulty_d1 | 1240 | -2.63321 | 1.48238 | -6.17406 | -4.96157 | -3.95968 | -2.55371 | -1.17205 | -0.793593 | -0.40643 |
| tossup | end_difficulty_d2 | 1240 | -3.71965 | 1.65636 | -9.62783 | -5.81436 | -4.8636 | -4.24196 | -1.80378 | -1.04014 | -0.651347 |
| tossup | end_difficulty_d3 | 1240 | -1.57863 | 0.872294 | -4.98645 | -3.51085 | -1.84204 | -1.25029 | -1.005 | -0.790766 | -0.471479 |
| tossup | end_difficulty_d4 | 1240 | -1.50127 | 0.834013 | -5.30251 | -3.56817 | -1.73361 | -1.23527 | -0.988378 | -0.696503 | -0.0885698 |
| tossup | end_difficulty_d5 | 1240 | -1.37229 | 0.614216 | -3.99255 | -2.62921 | -1.68948 | -1.22053 | -0.935285 | -0.601266 | 0.331306 |
| tossup | total_drop_d1 | 1240 | 1.08608 | 0.266781 | 0.606246 | 0.852506 | 0.952774 | 1.00816 | 1.11627 | 1.59874 | 3.34985 |
| tossup | total_drop_d2 | 1240 | 1.13271 | 0.502133 | 0.389872 | 0.651971 | 0.896741 | 1.0176 | 1.19745 | 2.00155 | 5.94331 |
| tossup | total_drop_d3 | 1240 | 1.01662 | 0.130382 | 0.803405 | 0.897839 | 0.953892 | 0.991934 | 1.03919 | 1.22485 | 2.43485 |
| tossup | total_drop_d4 | 1240 | 1.02195 | 0.134989 | 0.813587 | 0.895715 | 0.950627 | 0.991287 | 1.04765 | 1.2503 | 2.39939 |
| tossup | total_drop_d5 | 1240 | 1.01769 | 0.102218 | 0.817825 | 0.896892 | 0.954525 | 0.993779 | 1.0585 | 1.22577 | 1.83667 |
| tossup | drop_share_1_d1 | 1240 | 0.340997 | 0.0392041 | 0.259116 | 0.297652 | 0.309593 | 0.326884 | 0.369501 | 0.41364 | 0.496796 |
| tossup | drop_share_2_d1 | 1240 | 0.342222 | 0.0129389 | 0.290367 | 0.319348 | 0.334299 | 0.342861 | 0.350239 | 0.362367 | 0.404749 |
| tossup | drop_share_3_d1 | 1240 | 0.316781 | 0.0362357 | 0.166693 | 0.247739 | 0.291997 | 0.329363 | 0.344778 | 0.357947 | 0.385027 |
| tossup | drop_share_1_d2 | 1240 | 0.360546 | 0.0585973 | 0.1811 | 0.29452 | 0.315604 | 0.349674 | 0.395057 | 0.466586 | 0.661077 |
| tossup | drop_share_2_d2 | 1240 | 0.334507 | 0.0241881 | 0.221178 | 0.29697 | 0.320571 | 0.335958 | 0.348366 | 0.365138 | 0.530921 |
| tossup | drop_share_3_d2 | 1240 | 0.304947 | 0.0506 | 0.113508 | 0.206992 | 0.273559 | 0.316268 | 0.341102 | 0.365347 | 0.46472 |
| tossup | drop_share_1_d3 | 1240 | 0.314796 | 0.0136868 | 0.281301 | 0.295503 | 0.305479 | 0.313071 | 0.321197 | 0.340879 | 0.379166 |
| tossup | drop_share_2_d3 | 1240 | 0.34653 | 0.00945105 | 0.318375 | 0.331438 | 0.33999 | 0.346597 | 0.352698 | 0.362547 | 0.379622 |
| tossup | drop_share_3_d3 | 1240 | 0.338674 | 0.0143868 | 0.279768 | 0.312697 | 0.330983 | 0.340341 | 0.348561 | 0.358384 | 0.386137 |
| tossup | drop_share_1_d4 | 1240 | 0.31398 | 0.0156547 | 0.280056 | 0.294366 | 0.30435 | 0.311425 | 0.319548 | 0.344551 | 0.399305 |
| tossup | drop_share_2_d4 | 1240 | 0.346737 | 0.00956528 | 0.314792 | 0.331118 | 0.340453 | 0.346582 | 0.353265 | 0.362109 | 0.375402 |
| tossup | drop_share_3_d4 | 1240 | 0.339284 | 0.0159196 | 0.25954 | 0.307854 | 0.331948 | 0.341902 | 0.349209 | 0.360402 | 0.376208 |
| tossup | drop_share_1_d5 | 1240 | 0.312848 | 0.0124555 | 0.274433 | 0.293863 | 0.303941 | 0.31215 | 0.320239 | 0.335055 | 0.359384 |
| tossup | drop_share_2_d5 | 1240 | 0.346681 | 0.00904265 | 0.322219 | 0.331571 | 0.340317 | 0.346804 | 0.352805 | 0.361612 | 0.378677 |
| tossup | drop_share_3_d5 | 1240 | 0.340472 | 0.013095 | 0.29304 | 0.317387 | 0.332491 | 0.341589 | 0.349647 | 0.360605 | 0.374791 |
| tossup | r_1 | 1240 | 0.263104 | 0.249292 | 0.0138368 | 0.0258487 | 0.0397285 | 0.157902 | 0.525043 | 0.688545 | 0.803999 |
| tossup | r_2 | 1240 | 0.498591 | 0.28212 | 0.041021 | 0.0576325 | 0.120223 | 0.604027 | 0.718925 | 0.835551 | 0.934831 |
| tossup | r_3 | 1240 | 0.0854398 | 0.0641595 | 0.0087297 | 0.0250196 | 0.0421001 | 0.0613939 | 0.104321 | 0.231517 | 0.360775 |
| tossup | r_4 | 1240 | 0.0786529 | 0.049401 | 0.0178442 | 0.0335417 | 0.047955 | 0.0636137 | 0.0867919 | 0.20063 | 0.304759 |
| tossup | r_5 | 1240 | 0.0742125 | 0.0471865 | 0.0104117 | 0.026707 | 0.0415027 | 0.0606388 | 0.0889229 | 0.172509 | 0.314765 |
| tossup | r_norm | 1240 | 0.693547 | 0.0787887 | 0.53212 | 0.582513 | 0.634486 | 0.682508 | 0.746899 | 0.841437 | 0.935563 |
