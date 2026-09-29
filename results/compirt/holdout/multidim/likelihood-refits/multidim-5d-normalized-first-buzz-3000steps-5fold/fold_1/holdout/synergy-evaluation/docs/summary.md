# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/likelihood-refits/multidim-5d-normalized-first-buzz-3000steps-5fold/fold_1/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/multidim/likelihood-refits/multidim-5d-normalized-first-buzz-3000steps-5fold/fold_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 299882 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.5184 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.895076 |
| log_loss | 0.412245 |
| ece | 0.0298494 |
| brier | 0.131336 |
| part_accuracy | 0.813658 |
| part_all_correct_accuracy | 0.519002 |
| accuracy_lift_over_all_correct | 0.294656 |
| part_accuracy_macro_team | 0.814874 |
| part_accuracy_macro_bonus | 0.811703 |
| probability_std | 0.339638 |
| probability_p10 | 0.0634943 |
| probability_p50 | 0.457715 |
| probability_p90 | 0.94688 |
| mean_predictive_variance | 0.134528 |
| exact_acc | 0.526128 |
| ranked_probability_score | 0.111419 |
| bonus_total_score_log_loss | 0.98312 |
| ppb_mae | 1.96136 |
| ranked_probability_score_responses | 8420 |
| bonus_total_score_log_loss_responses | 8420 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.625979 |
| log_loss | 0.8228 |
| ece | 0.220128 |
| brier | 0.261728 |
| accuracy | 0.624546 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.137578 |
| probability_std | 0.294482 |
| probability_p10 | 0.104613 |
| probability_p50 | 0.621022 |
| probability_p90 | 0.913919 |
| mean_predictive_variance | 0.15945 |
| integrated_brier_score | 0.0950998 |
| joint_tossup_event_log_loss | 6.8183 |
| buzz_position_mae | 0.145866 |
| buzz_position_median_absolute_error | 0.125066 |
| buzz_position_bias | -0.044044 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.39041 |
| first_buzzer_mean_reciprocal_rank | 0.59654 |
| first_buzzer_log_loss | 1.63251 |
| first_buzzer_events | 9093 |
| first_buzzer_player_replay_accuracy | 0.00857803 |
| first_buzzer_team_replay_accuracy | 0.0103376 |
| tossup_scorer_player_replay_accuracy | 0.094697 |
| tossup_scorer_team_replay_accuracy | 0.0963203 |
| tossup_game_winner_accuracy | 0.144124 |
| tossup_model_official_winner_accuracy | 0.144105 |
| tossup_game_margin_mae | 54.1017 |
| tossup_game_zero_margin_mae | 55.2922 |
| tournament_player_ppg_spearman | 0.258775 |
| tournament_player_ppg_mae | 22.7774 |
| tournament_player_ppg_top10_overlap | 0.327586 |
| tournament_player_ppg_top10_random_overlap | 0.269705 |
| tournament_player_ppg_top10_adjusted_overlap | 0.0642114 |
| neg_auroc | 0.625979 |
| neg_average_precision | 0.323381 |
| neg_precision | 0.324544 |
| neg_recall | 0.534905 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0936372 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.062934 |
| no_buzz_calibration_error | 0.047025 |
| no_buzz_brier | 0.0237566 |
| full_pmf_max_mass_error | 6.66134e-16 |
| tossup_outcome_schema_version | 3 |
| tossup_outcome_events | 9240 |
| tossup_replay_seed | 42 |
| tossup_model_official_winner_games | 458 |
| first_buzzer_player_replay_accuracy_events | 9093 |
| first_buzzer_team_replay_accuracy_events | 9093 |
| tossup_scorer_player_replay_accuracy_events | 9240 |
| tossup_scorer_team_replay_accuracy_events | 9240 |
| tossup_game_winner_accuracy_games | 451 |
| tossup_game_margin_mae_games | 462 |
| tournament_player_ppg_tournaments | 29 |
| tossup_replay_incomplete_games | 0 |

## Tossup Game Replay

| metric | value |
| --- | --- |
| tossup_game_winner_accuracy | 0.144124 |
| tossup_game_margin_mae | 54.1017 |
| tossup_game_zero_margin_mae | 55.2922 |
| tossup_game_margin_mae_games | 462 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 451 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.625979 | 0.8228 | 0.220128 | 0.261728 | 0.624546 | 0.762125 | -0.137578 | 0.294482 | 0.104613 | 0.621022 | 0.913919 | 0.15945 |
| tossup_correctness | tier | fall | 2842 | 0.63379 | 0.798823 | 0.224349 | 0.253586 | 0.63582 | 0.785362 | -0.149543 | 0.287745 | 0.127539 | 0.631909 | 0.904295 | 0.162581 |
| tossup_correctness | tier | nationals | 1564 | 0.609004 | 0.787131 | 0.190617 | 0.259688 | 0.618926 | 0.718031 | -0.0991049 | 0.29161 | 0.118866 | 0.650544 | 0.925499 | 0.157052 |
| tossup_correctness | tier | regionals | 1937 | 0.63013 | 0.796262 | 0.209003 | 0.254543 | 0.634486 | 0.758389 | -0.123903 | 0.297194 | 0.10576 | 0.650399 | 0.923627 | 0.155441 |
| tossup_correctness | tier | winter | 2750 | 0.631563 | 0.886557 | 0.248293 | 0.276365 | 0.609091 | 0.765818 | -0.156727 | 0.297999 | 0.0813907 | 0.566574 | 0.904831 | 0.160404 |
| tossup_correctness | category | Current Events | 126 | 0.564166 | 1.06312 | 0.320896 | 0.324802 | 0.52381 | 0.769841 | -0.246032 | 0.282661 | 0.07185 | 0.506238 | 0.844412 | 0.169109 |
| tossup_correctness | category | Fine Arts | 1071 | 0.631488 | 0.850555 | 0.243737 | 0.271934 | 0.618114 | 0.766573 | -0.148459 | 0.299538 | 0.0779034 | 0.585736 | 0.911155 | 0.158742 |
| tossup_correctness | category | Geography | 185 | 0.624446 | 0.887632 | 0.245248 | 0.296377 | 0.578378 | 0.697297 | -0.118919 | 0.279433 | 0.0694691 | 0.453756 | 0.831201 | 0.170079 |
| tossup_correctness | category | History | 1440 | 0.622351 | 0.796333 | 0.214433 | 0.257299 | 0.634028 | 0.754167 | -0.120139 | 0.29109 | 0.116849 | 0.638951 | 0.915235 | 0.160194 |
| tossup_correctness | category | Literature | 1422 | 0.609574 | 0.826545 | 0.229858 | 0.253307 | 0.639241 | 0.814346 | -0.175105 | 0.298074 | 0.126036 | 0.676799 | 0.935377 | 0.151719 |
| tossup_correctness | category | Mythology | 318 | 0.603675 | 0.824611 | 0.279061 | 0.274336 | 0.58805 | 0.789308 | -0.201258 | 0.276038 | 0.120639 | 0.591377 | 0.88662 | 0.172542 |
| tossup_correctness | category | Other Academic | 66 | 0.702128 | 0.759513 | 0.22359 | 0.239768 | 0.590909 | 0.712121 | -0.121212 | 0.279665 | 0.0356294 | 0.525259 | 0.861303 | 0.171639 |
| tossup_correctness | category | Philosophy | 311 | 0.665812 | 0.827546 | 0.212881 | 0.258296 | 0.633441 | 0.745981 | -0.11254 | 0.304315 | 0.0825089 | 0.609013 | 0.913814 | 0.155016 |
| tossup_correctness | category | Popular Culture | 102 | 0.469444 | 1.11893 | 0.40824 | 0.346726 | 0.5 | 0.882353 | -0.382353 | 0.269875 | 0.0652149 | 0.496065 | 0.787428 | 0.176498 |
| tossup_correctness | category | Religion | 358 | 0.650333 | 0.793658 | 0.182063 | 0.256556 | 0.625698 | 0.712291 | -0.0865922 | 0.289627 | 0.112857 | 0.607754 | 0.899237 | 0.164091 |
| tossup_correctness | category | Science | 1433 | 0.62307 | 0.822699 | 0.211001 | 0.260257 | 0.62596 | 0.738311 | -0.112352 | 0.289507 | 0.123809 | 0.615059 | 0.906315 | 0.162467 |
| tossup_correctness | category | Social Science | 324 | 0.62874 | 0.806404 | 0.228235 | 0.264138 | 0.611111 | 0.731481 | -0.12037 | 0.277865 | 0.102258 | 0.560686 | 0.880804 | 0.171649 |
| tossup_correctness | category | Unknown | 1937 | 0.63013 | 0.796262 | 0.209003 | 0.254543 | 0.634486 | 0.758389 | -0.123903 | 0.297194 | 0.10576 | 0.650399 | 0.923627 | 0.155441 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.643557 | 1.3385 | 0.45141 | 0.425248 | 0.377246 | 0.712575 | -0.335329 | 0.242229 | 0.0126627 | 0.191642 | 0.683115 | 0.136187 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.64107 | 1.18657 | 0.385622 | 0.364687 | 0.479167 | 0.729167 | -0.25 | 0.267998 | 0.0303708 | 0.299027 | 0.760418 | 0.155076 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.645203 | 0.879007 | 0.272011 | 0.284524 | 0.588652 | 0.755083 | -0.16643 | 0.28497 | 0.0790447 | 0.503859 | 0.861677 | 0.168642 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.628397 | 0.747503 | 0.202339 | 0.239558 | 0.656118 | 0.780942 | -0.124824 | 0.277573 | 0.16357 | 0.664759 | 0.917276 | 0.163365 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.622658 | 0.717199 | 0.141503 | 0.22691 | 0.676923 | 0.762029 | -0.0851064 | 0.269205 | 0.217295 | 0.745199 | 0.940216 | 0.15202 |
| bonus_part_correctness | aggregate | all | 25260 | 0.895076 | 0.412245 | 0.0298494 | 0.131336 | 0.813658 | 0.519002 | 0.294656 | 0.339638 | 0.0634943 | 0.457715 | 0.94688 | 0.134528 |
| bonus_part_correctness | tier | fall | 8160 | 0.891383 | 0.4091 | 0.0354803 | 0.130793 | 0.810417 | 0.608701 | 0.201716 | 0.328776 | 0.102825 | 0.620108 | 0.955253 | 0.136545 |
| bonus_part_correctness | tier | nationals | 4107 | 0.889819 | 0.419444 | 0.0445692 | 0.133375 | 0.81008 | 0.411493 | 0.398588 | 0.314426 | 0.0442276 | 0.25458 | 0.869206 | 0.134009 |
| bonus_part_correctness | tier | regionals | 5280 | 0.891971 | 0.417325 | 0.0293212 | 0.132793 | 0.815341 | 0.48125 | 0.334091 | 0.335332 | 0.0563213 | 0.389638 | 0.941921 | 0.135242 |
| bonus_part_correctness | tier | winter | 7713 | 0.895292 | 0.40826 | 0.0212011 | 0.129827 | 0.81784 | 0.507196 | 0.310644 | 0.343088 | 0.0620627 | 0.453176 | 0.950062 | 0.132183 |
| bonus_part_correctness | category | Current Events | 249 | 0.902247 | 0.401066 | 0.0533178 | 0.125669 | 0.835341 | 0.514056 | 0.321285 | 0.348102 | 0.0638883 | 0.447163 | 0.950579 | 0.128402 |
| bonus_part_correctness | category | Fine Arts | 2934 | 0.875343 | 0.446177 | 0.0341254 | 0.144441 | 0.794138 | 0.507157 | 0.28698 | 0.333238 | 0.0649411 | 0.425457 | 0.938044 | 0.13825 |
| bonus_part_correctness | category | Geography | 459 | 0.890282 | 0.415525 | 0.0548743 | 0.133649 | 0.810458 | 0.618736 | 0.191721 | 0.33112 | 0.0862058 | 0.639191 | 0.954415 | 0.136259 |
| bonus_part_correctness | category | History | 4017 | 0.898256 | 0.404329 | 0.0284378 | 0.128663 | 0.815285 | 0.552153 | 0.263132 | 0.340971 | 0.0693832 | 0.540732 | 0.948693 | 0.133177 |
| bonus_part_correctness | category | Literature | 4047 | 0.901258 | 0.399943 | 0.0230629 | 0.125683 | 0.827527 | 0.50556 | 0.321967 | 0.3404 | 0.0657161 | 0.439503 | 0.948777 | 0.133908 |
| bonus_part_correctness | category | Mythology | 924 | 0.871444 | 0.438701 | 0.0386834 | 0.143189 | 0.784632 | 0.619048 | 0.165584 | 0.320312 | 0.10927 | 0.642287 | 0.959872 | 0.140443 |
| bonus_part_correctness | category | Other Academic | 237 | 0.917487 | 0.368215 | 0.0505445 | 0.112991 | 0.831224 | 0.481013 | 0.350211 | 0.356257 | 0.0462871 | 0.451336 | 0.964994 | 0.122835 |
| bonus_part_correctness | category | Philosophy | 948 | 0.89806 | 0.408383 | 0.0478535 | 0.130059 | 0.816456 | 0.494726 | 0.32173 | 0.330373 | 0.059797 | 0.407503 | 0.937259 | 0.139314 |
| bonus_part_correctness | category | Popular Culture | 294 | 0.882155 | 0.422579 | 0.0956281 | 0.139755 | 0.792517 | 0.673469 | 0.119048 | 0.315487 | 0.104917 | 0.613926 | 0.956746 | 0.143246 |
| bonus_part_correctness | category | Religion | 984 | 0.900225 | 0.405137 | 0.0416084 | 0.128913 | 0.806911 | 0.513211 | 0.293699 | 0.34728 | 0.0550065 | 0.44613 | 0.948061 | 0.129137 |
| bonus_part_correctness | category | Science | 3990 | 0.896894 | 0.408656 | 0.0298779 | 0.130228 | 0.812531 | 0.52807 | 0.284461 | 0.340287 | 0.066305 | 0.472858 | 0.947806 | 0.134205 |
| bonus_part_correctness | category | Social Science | 897 | 0.916063 | 0.372558 | 0.0463201 | 0.116575 | 0.835006 | 0.490524 | 0.344482 | 0.350911 | 0.0481409 | 0.369419 | 0.948175 | 0.124258 |
| bonus_part_correctness | category | Unknown | 5280 | 0.891971 | 0.417325 | 0.0293212 | 0.132793 | 0.815341 | 0.48125 | 0.334091 | 0.335332 | 0.0563213 | 0.389638 | 0.941921 | 0.135242 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.88705 | 0.895076 | 0.00802578 | synergy |
| log_loss | 0.424268 | 0.412245 | -0.0120228 | synergy |
| ece | 0.017465 | 0.0298494 | 0.0123844 | no-synergy |
| brier | 0.135077 | 0.131336 | -0.00374053 | synergy |
| accuracy_lift_over_all_correct | 0.288599 | 0.294656 | 0.00605701 | synergy |
| part_accuracy | 0.807601 | 0.813658 | 0.00605701 | synergy |
| part_accuracy_macro_team | 0.811147 | 0.814874 | 0.00372705 | synergy |
| part_accuracy_macro_bonus | 0.804574 | 0.811703 | 0.0071289 | synergy |
| exact_acc | 0.516746 | 0.526128 | 0.00938242 | synergy |
| ranked_probability_score | 0.115834 | 0.111419 | -0.00441518 | synergy |
| bonus_total_score_log_loss | 1.01423 | 0.98312 | -0.0311109 | synergy |
| ppb_mae | 2.37194 | 1.96136 | -0.410583 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 4.59169 | 1.19643 | 0.967552 | 1.97451 | 4.02325 | 4.82806 | 5.43155 | 6.14128 | 7.1026 |
| player | theta_1 | 1167 | 0.0366061 | 0.735778 | -2.26402 | -1.41868 | -0.376034 | 0.177649 | 0.553005 | 1.03912 | 1.91004 |
| player | theta_2 | 1167 | 0.0717107 | 0.742675 | -2.58227 | -1.45168 | -0.300112 | 0.176493 | 0.570745 | 1.13146 | 1.94214 |
| player | theta_3 | 1167 | 0.0161106 | 0.718776 | -2.53843 | -1.27133 | -0.447039 | 0.0939332 | 0.549178 | 1.0764 | 1.64936 |
| player | theta_4 | 1167 | 0.0542037 | 0.737517 | -2.27846 | -1.36819 | -0.353985 | 0.18307 | 0.573944 | 1.08347 | 2.07244 |
| player | theta_5 | 1167 | -0.0144201 | 0.767054 | -2.81743 | -1.49388 | -0.446325 | 0.140864 | 0.530362 | 0.987638 | 1.83352 |
| player | theta_norm | 1167 | 1.5435 | 0.60608 | 0.453393 | 0.731564 | 1.10021 | 1.43747 | 1.89747 | 2.74748 | 3.82846 |
| tossup | beta_1 | 1220 | 0.759804 | 0.518866 | -1.29233 | 0.213521 | 0.394637 | 0.587683 | 0.996204 | 1.86785 | 2.62437 |
| tossup | beta_2 | 1220 | 0.861456 | 0.59736 | -1.41662 | 0.212103 | 0.427726 | 0.655509 | 1.22173 | 2.03281 | 2.9087 |
| tossup | beta_3 | 1220 | 0.733078 | 0.539094 | -1.19447 | 0.188894 | 0.390339 | 0.555194 | 0.890113 | 1.94743 | 3.2258 |
| tossup | beta_4 | 1220 | 0.748985 | 0.522509 | -0.934604 | 0.208122 | 0.414003 | 0.576236 | 0.916039 | 1.90375 | 2.78165 |
| tossup | beta_5 | 1220 | 0.797799 | 0.546745 | -1.04324 | 0.200791 | 0.40269 | 0.621094 | 1.07313 | 1.9071 | 3.09357 |
| tossup | gamma_1 | 1220 | 11.8372 | 58.2998 | 0.566705 | 3.34165 | 4.50774 | 5.16654 | 6.14022 | 26.7004 | 1736.64 |
| tossup | gamma_2 | 1220 | 13.5937 | 81.5353 | 0.576669 | 3.03587 | 4.41738 | 5.09667 | 6.15273 | 21.498 | 1966.4 |
| tossup | gamma_3 | 1220 | 12.3253 | 53.7252 | 0.889968 | 3.38147 | 4.52905 | 5.09234 | 5.87453 | 24.7878 | 1176.42 |
| tossup | gamma_4 | 1220 | 11.8748 | 76.7626 | 0.794698 | 3.17584 | 4.48546 | 5.10118 | 5.94029 | 19.3589 | 1540.41 |
| tossup | gamma_5 | 1220 | 13.3094 | 56.1215 | 0.56595 | 3.09556 | 4.45201 | 5.13555 | 6.48883 | 25.8412 | 1278.2 |
| tossup | mu_1 | 1220 | 0.501727 | 0.104801 | 0.121692 | 0.384724 | 0.446267 | 0.475921 | 0.529466 | 0.720643 | 0.983549 |
| tossup | mu_2 | 1220 | 0.527241 | 0.126466 | 0.183277 | 0.380561 | 0.447511 | 0.487439 | 0.588654 | 0.798875 | 0.98683 |
| tossup | mu_3 | 1220 | 0.500472 | 0.104221 | 0.175937 | 0.396309 | 0.446349 | 0.474345 | 0.517987 | 0.721227 | 0.957765 |
| tossup | mu_4 | 1220 | 0.501732 | 0.107197 | 0.145442 | 0.384413 | 0.447493 | 0.478651 | 0.522334 | 0.734877 | 0.957495 |
| tossup | mu_5 | 1220 | 0.511778 | 0.110419 | 0.156946 | 0.372781 | 0.447285 | 0.485286 | 0.555476 | 0.733643 | 0.948937 |
| tossup | r_1 | 1220 | 1.01942 | 0.756598 | 0.0885328 | 0.218253 | 0.430898 | 0.759433 | 1.45745 | 2.54528 | 4.08254 |
| tossup | r_2 | 1220 | 1.40533 | 1.09076 | 0.104975 | 0.240564 | 0.524896 | 1.06492 | 2.11447 | 3.55257 | 6.0739 |
| tossup | r_3 | 1220 | 0.97912 | 0.815729 | 0.105582 | 0.208368 | 0.412927 | 0.710987 | 1.24978 | 2.75964 | 5.56069 |
| tossup | r_4 | 1220 | 1.02236 | 0.840034 | 0.0605896 | 0.223554 | 0.418728 | 0.742549 | 1.32284 | 2.83342 | 5.36144 |
| tossup | r_5 | 1220 | 1.12767 | 0.786118 | 0.072092 | 0.210155 | 0.479614 | 0.904405 | 1.63974 | 2.63037 | 5.10975 |
| tossup | r_norm | 1220 | 3.06865 | 0.788531 | 1.37111 | 1.9419 | 2.50219 | 2.96995 | 3.53061 | 4.52078 | 6.20318 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
