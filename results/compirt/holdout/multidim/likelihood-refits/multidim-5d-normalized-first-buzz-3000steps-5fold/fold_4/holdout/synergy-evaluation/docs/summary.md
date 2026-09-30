# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/likelihood-refits/multidim-5d-normalized-first-buzz-3000steps-5fold/fold_4/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/likelihood-refits/multidim-5d-normalized-first-buzz-3000steps-5fold/fold_4`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 298485 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.545512 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.897276 |
| log_loss | 0.409278 |
| ece | 0.0346524 |
| brier | 0.130243 |
| part_accuracy | 0.816052 |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.290497 |
| part_accuracy_macro_team | 0.82204 |
| part_accuracy_macro_bonus | 0.808883 |
| probability_std | 0.339839 |
| probability_p10 | 0.0633799 |
| probability_p50 | 0.459827 |
| probability_p90 | 0.948638 |
| mean_predictive_variance | 0.134427 |
| exact_acc | 0.529344 |
| ranked_probability_score | 0.113508 |
| bonus_total_score_log_loss | 1.00018 |
| ppb_mae | 1.86663 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.635893 |
| log_loss | 0.830145 |
| ece | 0.227098 |
| brier | 0.261324 |
| accuracy | 0.623732 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.149622 |
| probability_std | 0.29671 |
| probability_p10 | 0.0900234 |
| probability_p50 | 0.614423 |
| probability_p90 | 0.912391 |
| mean_predictive_variance | 0.158759 |
| integrated_brier_score | 0.0949591 |
| joint_tossup_event_log_loss | 6.84133 |
| buzz_position_mae | 0.145611 |
| buzz_position_median_absolute_error | 0.127451 |
| buzz_position_bias | -0.0399681 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.396764 |
| first_buzzer_mean_reciprocal_rank | 0.602402 |
| first_buzzer_log_loss | 1.62221 |
| first_buzzer_events | 9270 |
| first_buzzer_player_replay_accuracy | 0.0111111 |
| first_buzzer_team_replay_accuracy | 0.0132686 |
| tossup_scorer_player_replay_accuracy | 0.0902985 |
| tossup_scorer_team_replay_accuracy | 0.0924307 |
| tossup_game_winner_accuracy | 0.189956 |
| tossup_model_official_winner_accuracy | 0.185345 |
| tossup_game_margin_mae | 56.3006 |
| tossup_game_zero_margin_mae | 58.0704 |
| tournament_player_ppg_spearman | 0.266308 |
| tournament_player_ppg_mae | 23.4198 |
| tournament_player_ppg_top10_overlap | 0.365517 |
| tournament_player_ppg_top10_random_overlap | 0.291672 |
| tournament_player_ppg_top10_adjusted_overlap | 0.101004 |
| neg_auroc | 0.635893 |
| neg_average_precision | 0.323135 |
| neg_precision | 0.310156 |
| neg_recall | 0.539267 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0916629 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0601436 |
| no_buzz_calibration_error | 0.0484165 |
| no_buzz_brier | 0.0204414 |
| full_pmf_max_mass_error | 5.55112e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9380 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 464 |
| first_buzzer_player_replay_accuracy_events | 9270 |
| first_buzzer_team_replay_accuracy_events | 9270 |
| tossup_scorer_player_replay_accuracy_events | 9380 |
| tossup_scorer_team_replay_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 458 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.189956 |
| tossup_game_margin_mae | 56.3006 |
| tossup_game_zero_margin_mae | 58.0704 |
| tossup_game_margin_mae_games | 469 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 458 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.635893 | 0.830145 | 0.227098 | 0.261324 | 0.623732 | 0.773355 | -0.149622 | 0.29671 | 0.0900234 | 0.614423 | 0.912391 | 0.158759 |
| tossup_correctness | tier | fall | 2876 | 0.638322 | 0.823975 | 0.245605 | 0.259197 | 0.623435 | 0.793115 | -0.16968 | 0.29278 | 0.0876064 | 0.612941 | 0.907387 | 0.161165 |
| tossup_correctness | tier | nationals | 1579 | 0.636498 | 0.771146 | 0.177722 | 0.251569 | 0.634579 | 0.729576 | -0.0949968 | 0.29328 | 0.118539 | 0.646973 | 0.927832 | 0.157233 |
| tossup_correctness | tier | regionals | 1990 | 0.640723 | 0.848624 | 0.22459 | 0.262551 | 0.628141 | 0.765829 | -0.137688 | 0.302333 | 0.0841341 | 0.609036 | 0.913444 | 0.155645 |
| tossup_correctness | tier | winter | 2825 | 0.63586 | 0.856387 | 0.243996 | 0.268077 | 0.614867 | 0.783009 | -0.168142 | 0.297728 | 0.0853012 | 0.597209 | 0.906322 | 0.159357 |
| tossup_correctness | category | Current Events | 123 | 0.667645 | 0.776349 | 0.253499 | 0.260632 | 0.601626 | 0.764228 | -0.162602 | 0.28983 | 0.0885109 | 0.602032 | 0.869499 | 0.165384 |
| tossup_correctness | category | Fine Arts | 1093 | 0.640007 | 0.857336 | 0.22937 | 0.267921 | 0.614822 | 0.769442 | -0.15462 | 0.303967 | 0.0791606 | 0.609126 | 0.912264 | 0.155477 |
| tossup_correctness | category | Geography | 191 | 0.560478 | 0.91163 | 0.237757 | 0.305748 | 0.513089 | 0.691099 | -0.17801 | 0.273773 | 0.0890288 | 0.539353 | 0.854178 | 0.174872 |
| tossup_correctness | category | History | 1469 | 0.659372 | 0.751064 | 0.195896 | 0.242437 | 0.646018 | 0.758339 | -0.112321 | 0.289159 | 0.111397 | 0.628834 | 0.912468 | 0.160862 |
| tossup_correctness | category | Literature | 1436 | 0.624997 | 0.845715 | 0.254943 | 0.258952 | 0.638579 | 0.81546 | -0.17688 | 0.306726 | 0.0873449 | 0.659481 | 0.933855 | 0.149687 |
| tossup_correctness | category | Mythology | 325 | 0.521254 | 1.00138 | 0.333942 | 0.308036 | 0.56 | 0.843077 | -0.283077 | 0.289949 | 0.0777036 | 0.581451 | 0.879786 | 0.165056 |
| tossup_correctness | category | Other Academic | 67 | 0.641509 | 0.865913 | 0.283299 | 0.279599 | 0.61194 | 0.791045 | -0.179104 | 0.276853 | 0.0799013 | 0.558572 | 0.848992 | 0.173292 |
| tossup_correctness | category | Philosophy | 322 | 0.667182 | 0.781778 | 0.238238 | 0.256194 | 0.630435 | 0.785714 | -0.15528 | 0.302718 | 0.0854092 | 0.613224 | 0.919846 | 0.155303 |
| tossup_correctness | category | Popular Culture | 100 | 0.53524 | 0.937218 | 0.368248 | 0.299688 | 0.59 | 0.89 | -0.3 | 0.267012 | 0.0861032 | 0.585605 | 0.834579 | 0.178231 |
| tossup_correctness | category | Religion | 365 | 0.664004 | 0.769051 | 0.224732 | 0.249838 | 0.657534 | 0.723288 | -0.0657534 | 0.292935 | 0.102377 | 0.597209 | 0.904787 | 0.16252 |
| tossup_correctness | category | Science | 1456 | 0.614552 | 0.837349 | 0.222223 | 0.262942 | 0.616071 | 0.76717 | -0.151099 | 0.286366 | 0.106073 | 0.629001 | 0.904566 | 0.164168 |
| tossup_correctness | category | Social Science | 333 | 0.678921 | 0.761083 | 0.215325 | 0.250346 | 0.600601 | 0.72973 | -0.129129 | 0.287153 | 0.0843812 | 0.535217 | 0.9058 | 0.166954 |
| tossup_correctness | category | Unknown | 1990 | 0.640723 | 0.848624 | 0.22459 | 0.262551 | 0.628141 | 0.765829 | -0.137688 | 0.302333 | 0.0841341 | 0.609036 | 0.913444 | 0.155645 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.708789 | 1.41367 | 0.502606 | 0.439818 | 0.329609 | 0.748603 | -0.418994 | 0.219456 | 0.0138355 | 0.186119 | 0.577019 | 0.138023 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.65707 | 1.18375 | 0.410041 | 0.371785 | 0.464995 | 0.754441 | -0.289446 | 0.264175 | 0.0268244 | 0.293932 | 0.736724 | 0.156 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.662663 | 0.922224 | 0.290928 | 0.287622 | 0.577394 | 0.766682 | -0.189287 | 0.288344 | 0.0553687 | 0.489552 | 0.85876 | 0.166321 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.648595 | 0.73023 | 0.195396 | 0.235018 | 0.655809 | 0.787441 | -0.131632 | 0.27873 | 0.146828 | 0.658849 | 0.913901 | 0.163487 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.6213 | 0.712246 | 0.148461 | 0.221616 | 0.695225 | 0.771758 | -0.0765323 | 0.268225 | 0.217855 | 0.749088 | 0.941046 | 0.150501 |
| bonus_part_correctness | aggregate | all | 25866 | 0.897276 | 0.409278 | 0.0346524 | 0.130243 | 0.816052 | 0.525555 | 0.290497 | 0.339839 | 0.0633799 | 0.459827 | 0.948638 | 0.134427 |
| bonus_part_correctness | tier | fall | 8259 | 0.893913 | 0.40572 | 0.030264 | 0.129325 | 0.816564 | 0.601283 | 0.21528 | 0.33117 | 0.102922 | 0.625138 | 0.959249 | 0.135283 |
| bonus_part_correctness | tier | nationals | 4167 | 0.882746 | 0.439549 | 0.0571466 | 0.139884 | 0.804896 | 0.438445 | 0.366451 | 0.322147 | 0.0439986 | 0.271859 | 0.888235 | 0.132131 |
| bonus_part_correctness | tier | regionals | 5457 | 0.90086 | 0.407646 | 0.0472323 | 0.129445 | 0.817665 | 0.493861 | 0.323804 | 0.333321 | 0.0549887 | 0.37103 | 0.931121 | 0.136048 |
| bonus_part_correctness | tier | winter | 7983 | 0.901296 | 0.398273 | 0.0190393 | 0.126705 | 0.820243 | 0.514343 | 0.3059 | 0.3411 | 0.0653944 | 0.466031 | 0.953557 | 0.133631 |
| bonus_part_correctness | category | Current Events | 258 | 0.869173 | 0.468169 | 0.0692231 | 0.150046 | 0.802326 | 0.515504 | 0.286822 | 0.360791 | 0.0513778 | 0.436833 | 0.944576 | 0.119305 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.895167 | 0.411686 | 0.0294123 | 0.130447 | 0.821333 | 0.508 | 0.313333 | 0.334098 | 0.0682673 | 0.433441 | 0.94441 | 0.137992 |
| bonus_part_correctness | category | Geography | 450 | 0.898266 | 0.394425 | 0.0268258 | 0.125741 | 0.808889 | 0.582222 | 0.226667 | 0.339435 | 0.0790044 | 0.649246 | 0.968559 | 0.127961 |
| bonus_part_correctness | category | History | 4116 | 0.895639 | 0.410319 | 0.0350731 | 0.130714 | 0.812682 | 0.562196 | 0.250486 | 0.341492 | 0.0681504 | 0.547993 | 0.954103 | 0.132647 |
| bonus_part_correctness | category | Literature | 4092 | 0.90106 | 0.400782 | 0.0328087 | 0.127495 | 0.818426 | 0.522727 | 0.295699 | 0.343323 | 0.0633736 | 0.43996 | 0.952635 | 0.132028 |
| bonus_part_correctness | category | Mythology | 951 | 0.87643 | 0.434871 | 0.067792 | 0.140558 | 0.793901 | 0.647739 | 0.146162 | 0.312364 | 0.121618 | 0.629988 | 0.954072 | 0.146037 |
| bonus_part_correctness | category | Other Academic | 276 | 0.900754 | 0.403282 | 0.0523371 | 0.129173 | 0.822464 | 0.532609 | 0.289855 | 0.351972 | 0.0525727 | 0.522415 | 0.947125 | 0.126096 |
| bonus_part_correctness | category | Philosophy | 957 | 0.896839 | 0.405637 | 0.0238509 | 0.129505 | 0.814002 | 0.474399 | 0.339603 | 0.32923 | 0.0666557 | 0.399736 | 0.942378 | 0.140271 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.870928 | 0.435203 | 0.0618641 | 0.143212 | 0.8 | 0.616667 | 0.183333 | 0.31454 | 0.141821 | 0.64231 | 0.962032 | 0.142993 |
| bonus_part_correctness | category | Religion | 1029 | 0.90094 | 0.400651 | 0.0328601 | 0.127308 | 0.821186 | 0.501458 | 0.319728 | 0.342652 | 0.0562988 | 0.457942 | 0.945646 | 0.132148 |
| bonus_part_correctness | category | Science | 4089 | 0.891714 | 0.417803 | 0.0293005 | 0.1329 | 0.812424 | 0.533382 | 0.279041 | 0.340154 | 0.0675156 | 0.485836 | 0.954002 | 0.134279 |
| bonus_part_correctness | category | Social Science | 891 | 0.912441 | 0.376376 | 0.0369966 | 0.118367 | 0.840629 | 0.480359 | 0.360269 | 0.351171 | 0.0485584 | 0.340947 | 0.953405 | 0.123707 |
| bonus_part_correctness | category | Unknown | 5457 | 0.90086 | 0.407646 | 0.0472323 | 0.129445 | 0.817665 | 0.493861 | 0.323804 | 0.333321 | 0.0549887 | 0.37103 | 0.931121 | 0.136048 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.891193 | 0.897276 | 0.00608297 | synergy |
| log_loss | 0.418663 | 0.409278 | -0.0093858 | synergy |
| ece | 0.02631 | 0.0346524 | 0.00834242 | no-synergy |
| brier | 0.133331 | 0.130243 | -0.0030877 | synergy |
| accuracy_lift_over_all_correct | 0.284814 | 0.290497 | 0.00568314 | synergy |
| part_accuracy | 0.810369 | 0.816052 | 0.00568314 | synergy |
| part_accuracy_macro_team | 0.814372 | 0.82204 | 0.00766887 | synergy |
| part_accuracy_macro_bonus | 0.801633 | 0.808883 | 0.00724938 | synergy |
| exact_acc | 0.515658 | 0.529344 | 0.0136859 | synergy |
| ranked_probability_score | 0.117406 | 0.113508 | -0.00389834 | synergy |
| bonus_total_score_log_loss | 1.02344 | 1.00018 | -0.023266 | synergy |
| ppb_mae | 2.31844 | 1.86663 | -0.451812 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 4.5662 | 1.19106 | 0.768505 | 2.02235 | 3.9518 | 4.79085 | 5.41824 | 6.0907 | 7.05385 |
| player | theta_1 | 1196 | 0.00115001 | 0.746401 | -2.25264 | -1.40931 | -0.44783 | 0.137217 | 0.539817 | 1.02017 | 1.86272 |
| player | theta_2 | 1196 | -0.0652172 | 0.737443 | -2.37915 | -1.49523 | -0.46031 | 0.0601399 | 0.42725 | 1.023 | 1.72784 |
| player | theta_3 | 1196 | 0.0950213 | 0.733042 | -2.32968 | -1.36556 | -0.287123 | 0.23002 | 0.591539 | 1.10005 | 1.99804 |
| player | theta_4 | 1196 | 0.0639936 | 0.751216 | -2.01844 | -1.34961 | -0.394348 | 0.156929 | 0.595043 | 1.16041 | 2.26252 |
| player | theta_5 | 1196 | 0.044462 | 0.756177 | -2.62502 | -1.42779 | -0.343117 | 0.196112 | 0.583732 | 1.05099 | 1.78021 |
| player | theta_norm | 1196 | 1.55932 | 0.600225 | 0.366597 | 0.716385 | 1.10933 | 1.47413 | 1.92511 | 2.71621 | 3.62874 |
| tossup | beta_1 | 1240 | 0.757813 | 0.512562 | -0.151586 | 0.224514 | 0.411946 | 0.571713 | 0.976351 | 1.86017 | 2.62804 |
| tossup | beta_2 | 1240 | 0.820179 | 0.590286 | -1.32106 | 0.19901 | 0.405511 | 0.609495 | 1.16675 | 2.03017 | 2.87593 |
| tossup | beta_3 | 1240 | 0.757296 | 0.52548 | -1.12572 | 0.236529 | 0.421183 | 0.588615 | 0.919769 | 1.87236 | 3.24593 |
| tossup | beta_4 | 1240 | 0.748749 | 0.543926 | -0.503453 | 0.212359 | 0.390116 | 0.564174 | 0.92961 | 1.95517 | 3.06764 |
| tossup | beta_5 | 1240 | 0.796764 | 0.562741 | -1.97436 | 0.217989 | 0.397541 | 0.604456 | 1.10067 | 1.96093 | 2.85445 |
| tossup | gamma_1 | 1240 | 11.8692 | 57.6874 | 1.24529 | 3.28587 | 4.51074 | 5.16793 | 6.1761 | 26.4036 | 1733.8 |
| tossup | gamma_2 | 1240 | 13.5269 | 86.0242 | 0.694364 | 3.3924 | 4.53852 | 5.19386 | 6.33923 | 21.7925 | 2026.6 |
| tossup | gamma_3 | 1240 | 11.8967 | 52.3561 | 0.656231 | 3.08082 | 4.40887 | 5.07554 | 5.94918 | 22.3747 | 891.689 |
| tossup | gamma_4 | 1240 | 11.9938 | 71.0269 | 1.16765 | 3.43739 | 4.5258 | 5.14928 | 6.00213 | 18.9885 | 2085.14 |
| tossup | gamma_5 | 1240 | 13.2824 | 66.1238 | 0.355212 | 3.19163 | 4.50697 | 5.15846 | 6.17715 | 22.7251 | 1368.02 |
| tossup | mu_1 | 1240 | 0.500131 | 0.100375 | 0.204176 | 0.38357 | 0.445079 | 0.478026 | 0.518551 | 0.71504 | 0.963668 |
| tossup | mu_2 | 1240 | 0.514684 | 0.120061 | 0.197078 | 0.387285 | 0.443107 | 0.47957 | 0.556144 | 0.7843 | 0.977009 |
| tossup | mu_3 | 1240 | 0.510677 | 0.110015 | 0.14913 | 0.395286 | 0.451642 | 0.482777 | 0.530519 | 0.748449 | 0.984902 |
| tossup | mu_4 | 1240 | 0.504925 | 0.107031 | 0.130901 | 0.397286 | 0.448571 | 0.47775 | 0.519006 | 0.730734 | 0.985675 |
| tossup | mu_5 | 1240 | 0.510999 | 0.109999 | 0.134285 | 0.385283 | 0.449346 | 0.483882 | 0.543037 | 0.73739 | 0.967776 |
| tossup | r_1 | 1240 | 1.02309 | 0.768453 | 0.0914744 | 0.223421 | 0.456076 | 0.77938 | 1.40155 | 2.59829 | 4.52013 |
| tossup | r_2 | 1240 | 1.26863 | 1.01794 | 0.10319 | 0.223125 | 0.501765 | 0.930874 | 1.78265 | 3.35693 | 5.57309 |
| tossup | r_3 | 1240 | 1.05909 | 0.90714 | 0.0824889 | 0.223798 | 0.439329 | 0.754369 | 1.3815 | 3.09544 | 6.6541 |
| tossup | r_4 | 1240 | 1.05718 | 0.921455 | 0.0738243 | 0.216798 | 0.423043 | 0.716761 | 1.29847 | 3.12594 | 5.43784 |
| tossup | r_5 | 1240 | 1.09237 | 0.789425 | 0.0906332 | 0.223219 | 0.469552 | 0.85877 | 1.54066 | 2.76279 | 3.98714 |
| tossup | r_norm | 1240 | 3.05972 | 0.803791 | 1.04944 | 1.91552 | 2.49034 | 2.94397 | 3.54348 | 4.49835 | 6.88956 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
