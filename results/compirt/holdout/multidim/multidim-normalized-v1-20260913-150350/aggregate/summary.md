# Game-infill 5-fold aggregate

Folds: 5

## evaluation_tossup_metrics (5 folds)

| metric | mean | std | n_folds |
| --- | --- | --- | --- |
| auc | 0.632324 | 0.00612202 | 5 |
| log_loss | 0.808652 | 0.0258656 | 5 |
| ece | 0.21948 | 0.00611817 | 5 |
| brier | 0.258086 | 0.00588528 | 5 |
| accuracy | 0.627938 | 0.00898833 | 5 |
| all_correct_accuracy | 0.76699 | 0.00459462 | 5 |
| accuracy_lift_over_all_correct | -0.139052 | 0.0086009 | 5 |
| probability_std | 0.292924 | 0.00295864 | 5 |
| probability_p10 | 0.10474 | 0.0113583 | 5 |
| probability_p50 | 0.621767 | 0.00912602 | 5 |
| probability_p90 | 0.913459 | 0.00509164 | 5 |
| mean_predictive_variance | 0.160209 | 0.00128912 | 5 |
| neg_auroc | 0.632324 | 0.00612202 | 5 |
| neg_average_precision | 0.328698 | 0.00698849 | 5 |
| neg_precision | 0.320528 | 0.00771211 | 5 |
| neg_recall | 0.532496 | 0.0097522 | 5 |
| joint_tossup_event_log_loss | 6.7942 | 0.0467583 | 5 |
| joint_tossup_event_log_loss_events | 9328 | 91.214 | 5 |
| integrated_brier_score | 0.0950046 | 0.000515212 | 5 |
| survival_events | 9328 | 91.214 | 5 |
| survival_events_skipped | 0 | 0 | 5 |
| first_buzzer_top1_accuracy | 0.396492 | 0.00439159 | 5 |
| first_buzzer_mean_reciprocal_rank | 0.602187 | 0.00344543 | 5 |
| first_buzzer_log_loss | 1.60899 | 0.0178083 | 5 |
| first_buzzer_events | 9199 | 103.704 | 5 |
| full_pmf_events | 9328 | 91.214 | 5 |
| full_pmf_final_decile_mass | 0.0914237 | 0.00260852 | 5 |
| no_buzz_observed_rate | 0.0138406 | 0.0016887 | 5 |
| no_buzz_predicted_rate | 0.0616544 | 0.00189835 | 5 |
| no_buzz_calibration_error | 0.0478138 | 0.00247305 | 5 |
| no_buzz_brier | 0.0218596 | 0.00136454 | 5 |
| full_pmf_max_mass_error | 5.9952e-16 | 6.08094e-17 | 5 |
| first_buzzer_player_replay_accuracy | 0.0101019 | 0.00245887 | 5 |
| first_buzzer_team_replay_accuracy | 0.0120164 | 0.0026921 | 5 |
| tossup_scorer_player_replay_accuracy | 0.0925455 | 0.00203414 | 5 |
| tossup_scorer_team_replay_accuracy | 0.0943039 | 0.00193448 | 5 |
| tossup_game_winner_accuracy | 0.159336 | 0.0265976 | 5 |
| tossup_model_official_winner_accuracy | 0.159865 | 0.0246668 | 5 |
| tossup_game_margin_mae | 55.8249 | 1.77207 | 5 |
| tossup_game_zero_margin_mae | 57.1639 | 1.97181 | 5 |
| tournament_player_ppg_spearman | 0.243696 | 0.0226779 | 5 |
| tournament_player_ppg_mae | 23.1885 | 0.260508 | 5 |
| tournament_player_ppg_top10_overlap | 0.333793 | 0.0313585 | 5 |
| tournament_player_ppg_top10_random_overlap | 0.283194 | 0.00914581 | 5 |
| tournament_player_ppg_top10_adjusted_overlap | 0.0550105 | 0.0428847 | 5 |
| tossup_outcome_schema_version | 3 | 0 | 5 |
| tossup_outcome_events | 9324 | 88.7694 | 5 |
| tossup_replay_seed | 42 | 0 | 5 |
| tossup_model_official_winner_games | 461.8 | 4.49444 | 5 |
| first_buzzer_player_replay_accuracy_events | 9195.2 | 101.369 | 5 |
| first_buzzer_team_replay_accuracy_events | 9195.2 | 101.369 | 5 |
| tossup_scorer_player_replay_accuracy_events | 9324 | 88.7694 | 5 |
| tossup_scorer_team_replay_accuracy_events | 9324 | 88.7694 | 5 |
| tossup_game_winner_accuracy_games | 453 | 3.39116 | 5 |
| tossup_game_margin_mae_games | 466.2 | 4.43847 | 5 |
| tournament_player_ppg_tournaments | 29 | 0 | 5 |
| tossup_replay_incomplete_games | 0.2 | 0.447214 | 5 |
| buzz_position_mae | 0.145472 | 0.0003612 | 5 |
| buzz_position_median_absolute_error | 0.125727 | 0.0010054 | 5 |
| buzz_position_bias | -0.041668 | 0.00386975 | 5 |

## evaluation_bonus_metrics (5 folds)

| metric | mean | std | n_folds |
| --- | --- | --- | --- |
| auc | 0.888284 | 0.00197609 | 5 |
| log_loss | 0.422597 | 0.00284247 | 5 |
| ece | 0.0205824 | 0.00411055 | 5 |
| brier | 0.134579 | 0.000830891 | 5 |
| accuracy_lift_over_all_correct | 0.286863 | 0.00335181 | 5 |
| probability_std | 0.327147 | 0.000556568 | 5 |
| probability_p10 | 0.0853247 | 0.00069738 | 5 |
| probability_p50 | 0.472852 | 0.00422364 | 5 |
| probability_p90 | 0.931803 | 0.00154808 | 5 |
| mean_predictive_variance | 0.142969 | 0.000363732 | 5 |
| part_accuracy | 0.808473 | 0.00172754 | 5 |
| part_all_correct_accuracy | 0.521609 | 0.00367649 | 5 |
| part_accuracy_macro_team | 0.811805 | 0.00159224 | 5 |
| part_accuracy_macro_bonus | 0.804931 | 0.00210686 | 5 |
| exact_acc | 0.512861 | 0.00343793 | 5 |
| ranked_probability_score | 0.116922 | 0.000731264 | 5 |
| ranked_probability_score_responses | 8540 | 94.8077 | 5 |
| bonus_total_score_log_loss | 1.02136 | 0.00421506 | 5 |
| bonus_total_score_log_loss_responses | 8540 | 94.8077 | 5 |
| ppb_mae | 2.35021 | 0.0213764 | 5 |

## evaluation_game_metrics (5 folds)

| metric | mean | std | n_folds |
| --- | --- | --- | --- |
| tossup_game_winner_accuracy | 0.159336 | 0.0265976 | 5 |
| tossup_game_margin_mae | 55.8249 | 1.77207 | 5 |
| tossup_game_zero_margin_mae | 57.1639 | 1.97181 | 5 |
| tossup_outcome_schema_version | 3 | 0 | 5 |
| tossup_game_winner_accuracy_games | 453 | 3.39116 | 5 |
| tossup_game_margin_mae_games | 466.2 | 4.43847 | 5 |

## synergy-evaluation_bonus_metrics (5 folds)

| metric | mean | std | n_folds |
| --- | --- | --- | --- |
| auc | 0.895536 | 0.00188605 | 5 |
| log_loss | 0.411324 | 0.00319827 | 5 |
| ece | 0.02999 | 0.00422868 | 5 |
| brier | 0.131051 | 0.00114357 | 5 |
| accuracy_lift_over_all_correct | 0.292207 | 0.00177314 | 5 |
| probability_std | 0.339887 | 0.00039079 | 5 |
| probability_p10 | 0.0634613 | 0.00159441 | 5 |
| probability_p50 | 0.462824 | 0.00866678 | 5 |
| probability_p90 | 0.948463 | 0.00220714 | 5 |
| mean_predictive_variance | 0.134391 | 0.000321642 | 5 |
| part_accuracy | 0.813816 | 0.0022651 | 5 |
| part_all_correct_accuracy | 0.521609 | 0.00367649 | 5 |
| part_accuracy_macro_team | 0.816136 | 0.00356242 | 5 |
| part_accuracy_macro_bonus | 0.810637 | 0.00297513 | 5 |
| exact_acc | 0.524229 | 0.00521334 | 5 |
| ranked_probability_score | 0.112511 | 0.000813973 | 5 |
| ranked_probability_score_responses | 8540 | 94.8077 | 5 |
| bonus_total_score_log_loss | 0.992259 | 0.006666 | 5 |
| bonus_total_score_log_loss_responses | 8540 | 94.8077 | 5 |
| ppb_mae | 1.86773 | 0.0606564 | 5 |
