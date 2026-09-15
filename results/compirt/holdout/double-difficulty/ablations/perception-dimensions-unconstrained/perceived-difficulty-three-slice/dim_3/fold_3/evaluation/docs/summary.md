# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_3/fold_3/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_3/fold_3`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 316179 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.652376 |
| log_loss | 0.514444 |
| ece | 0.0280563 |
| brier | 0.167255 |
| accuracy | 0.774229 |
| all_correct_accuracy | 0.770044 |
| accuracy_lift_over_all_correct | 0.00418502 |
| probability_std | 0.130364 |
| probability_p10 | 0.58219 |
| probability_p50 | 0.785859 |
| probability_p90 | 0.90376 |
| mean_predictive_variance | 0.164992 |
| integrated_brier_score | 0.102237 |
| joint_tossup_event_log_loss | 6.85288 |
| buzz_position_mae | 0.161437 |
| buzz_position_median_absolute_error | 0.145781 |
| buzz_position_bias | -0.0720698 |
| survival_events | 9220 |
| joint_tossup_event_log_loss_events | 9220 |
| first_buzzer_top1_accuracy | 0.364978 |
| first_buzzer_mean_reciprocal_rank | 0.573001 |
| first_buzzer_log_loss | 1.66192 |
| first_buzzer_events | 9080 |
| first_buzzer_team_top1_accuracy | 0.660793 |
| tossup_scorer_player_top1_accuracy | 0.324187 |
| tossup_scorer_team_top1_accuracy | 0.50423 |
| tossup_game_winner_accuracy | 0.780973 |
| tossup_game_margin_mae | 36.4434 |
| tournament_player_ppg_spearman | 0.698597 |
| tournament_player_ppg_mae | 8.92986 |
| tournament_player_ppg_top10_overlap | 0.662069 |
| neg_auroc | 0.652376 |
| neg_average_precision | 0.37605 |
| neg_precision | 0.543779 |
| neg_recall | 0.113027 |
| full_pmf_events | 9220 |
| full_pmf_final_decile_mass | 0.0542324 |
| no_buzz_observed_rate | 0.0151844 |
| no_buzz_predicted_rate | 0.0875792 |
| no_buzz_calibration_error | 0.0723948 |
| no_buzz_brier | 0.0247787 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9220 |
| first_buzzer_team_top1_accuracy_events | 9080 |
| tossup_scorer_player_top1_accuracy_events | 9220 |
| tossup_scorer_team_top1_accuracy_events | 9220 |
| tossup_game_winner_accuracy_games | 452 |
| tossup_game_margin_mae_games | 461 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9080 | 0.652376 | 0.514444 | 0.0280563 | 0.167255 | 0.774229 | 0.770044 | 0.00418502 | 0.130364 | 0.58219 | 0.785859 | 0.90376 | 0.164992 |
| tossup_correctness | tier | fall | 2817 | 0.646984 | 0.501012 | 0.0179426 | 0.161472 | 0.786297 | 0.781683 | 0.00461484 | 0.10295 | 0.651418 | 0.818586 | 0.906197 | 0.152145 |
| tossup_correctness | tier | nationals | 1542 | 0.689948 | 0.54433 | 0.0653953 | 0.181756 | 0.73476 | 0.73476 | 0 | 0.136715 | 0.482755 | 0.686196 | 0.836795 | 0.201856 |
| tossup_correctness | tier | regionals | 1934 | 0.629007 | 0.540816 | 0.0404108 | 0.177731 | 0.758532 | 0.75698 | 0.00155119 | 0.126503 | 0.600531 | 0.789974 | 0.909903 | 0.161787 |
| tossup_correctness | tier | winter | 2787 | 0.654011 | 0.493184 | 0.0328536 | 0.157807 | 0.794761 | 0.786868 | 0.00789379 | 0.132203 | 0.583659 | 0.795182 | 0.910981 | 0.159804 |
| tossup_correctness | category | Current Events | 125 | 0.694103 | 0.559452 | 0.0882455 | 0.189722 | 0.728 | 0.704 | 0.024 | 0.123088 | 0.525599 | 0.716333 | 0.832497 | 0.197248 |
| tossup_correctness | category | Fine Arts | 1072 | 0.642956 | 0.516131 | 0.0384152 | 0.168649 | 0.773321 | 0.770522 | 0.00279851 | 0.121822 | 0.597363 | 0.783112 | 0.898963 | 0.16709 |
| tossup_correctness | category | Geography | 185 | 0.769091 | 0.515525 | 0.0613812 | 0.170278 | 0.745946 | 0.702703 | 0.0432432 | 0.152664 | 0.458441 | 0.711952 | 0.857972 | 0.192946 |
| tossup_correctness | category | History | 1443 | 0.699262 | 0.502874 | 0.0412462 | 0.163927 | 0.772003 | 0.765073 | 0.00693001 | 0.145712 | 0.513703 | 0.751832 | 0.888998 | 0.17867 |
| tossup_correctness | category | Literature | 1411 | 0.58494 | 0.487557 | 0.045207 | 0.152787 | 0.807938 | 0.81219 | -0.0042523 | 0.106157 | 0.66685 | 0.830215 | 0.924507 | 0.143646 |
| tossup_correctness | category | Mythology | 320 | 0.588165 | 0.514401 | 0.0845523 | 0.164608 | 0.8 | 0.79375 | 0.00625 | 0.13507 | 0.539436 | 0.763258 | 0.886013 | 0.174056 |
| tossup_correctness | category | Other Academic | 64 | 0.58724 | 0.576017 | 0.138391 | 0.194342 | 0.71875 | 0.75 | -0.03125 | 0.125851 | 0.485032 | 0.67531 | 0.80298 | 0.208834 |
| tossup_correctness | category | Philosophy | 312 | 0.604452 | 0.492137 | 0.0563767 | 0.157046 | 0.794872 | 0.801282 | -0.00641026 | 0.111386 | 0.630696 | 0.803508 | 0.897988 | 0.159784 |
| tossup_correctness | category | Popular Culture | 104 | 0.504261 | 0.47346 | 0.123796 | 0.145596 | 0.855769 | 0.846154 | 0.00961538 | 0.112725 | 0.591367 | 0.75898 | 0.880362 | 0.176575 |
| tossup_correctness | category | Religion | 358 | 0.680416 | 0.546899 | 0.0282797 | 0.182809 | 0.740223 | 0.726257 | 0.0139665 | 0.141808 | 0.562979 | 0.769404 | 0.890882 | 0.174026 |
| tossup_correctness | category | Science | 1431 | 0.687119 | 0.50339 | 0.0186866 | 0.163996 | 0.774284 | 0.765199 | 0.00908456 | 0.121717 | 0.610897 | 0.798117 | 0.907285 | 0.159265 |
| tossup_correctness | category | Social Science | 321 | 0.67114 | 0.537773 | 0.0500665 | 0.178899 | 0.744548 | 0.744548 | 0 | 0.131657 | 0.559901 | 0.752181 | 0.880477 | 0.179949 |
| tossup_correctness | category | Unknown | 1934 | 0.629007 | 0.540816 | 0.0404108 | 0.177731 | 0.758532 | 0.75698 | 0.00155119 | 0.126503 | 0.600531 | 0.789974 | 0.909903 | 0.161787 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 192 | 0.695831 | 0.573058 | 0.0501273 | 0.193948 | 0.703125 | 0.697917 | 0.00520833 | 0.138991 | 0.470395 | 0.685976 | 0.816279 | 0.2049 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 889 | 0.676238 | 0.540536 | 0.0377584 | 0.179611 | 0.751406 | 0.733408 | 0.0179978 | 0.136977 | 0.506189 | 0.724944 | 0.858129 | 0.190139 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2210 | 0.636536 | 0.534514 | 0.0254216 | 0.175619 | 0.760181 | 0.759276 | 0.000904977 | 0.12718 | 0.572569 | 0.771203 | 0.88946 | 0.172339 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2869 | 0.637989 | 0.497788 | 0.0309306 | 0.160027 | 0.789822 | 0.789125 | 0.000697107 | 0.123734 | 0.602397 | 0.795407 | 0.906202 | 0.161254 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2920 | 0.660774 | 0.503822 | 0.0279285 | 0.162509 | 0.781164 | 0.775342 | 0.00582192 | 0.126854 | 0.604296 | 0.813926 | 0.920643 | 0.152822 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1133 | -2.47609 | 0.654251 | -4.86592 | -3.59743 | -2.90517 | -2.4197 | -2.02771 | -1.51544 | -0.198219 |
| player | theta_2 | 1133 | -1.32986 | 0.847695 | -4.8072 | -2.76512 | -2.00377 | -1.23876 | -0.611612 | -0.198323 | 0.896239 |
| player | theta_3 | 1133 | -1.10329 | 0.927202 | -4.35998 | -3.10071 | -1.36382 | -0.858349 | -0.463577 | -0.0715124 | 0.712106 |
| player | theta_norm | 1133 | 3.25258 | 0.736599 | 1.37019 | 2.13219 | 2.7271 | 3.20117 | 3.74495 | 4.50196 | 6.35814 |
| tossup | start_difficulty_d1 | 1240 | -2.52771 | 1.15567 | -4.87255 | -3.93495 | -3.40165 | -2.89828 | -1.68237 | -0.360442 | 0.168524 |
| tossup | start_difficulty_d2 | 1240 | -1.07522 | 1.30695 | -4.80973 | -3.62811 | -1.97658 | -0.53208 | -0.0849228 | 0.328984 | 1.37411 |
| tossup | start_difficulty_d3 | 1240 | -1.33167 | 1.18159 | -3.82074 | -3.15159 | -2.51843 | -1.1079 | -0.29056 | 0.262564 | 0.914794 |
| tossup | end_difficulty_d1 | 1240 | -3.63085 | 1.28713 | -8.27329 | -5.49396 | -4.54885 | -3.84899 | -2.73444 | -1.33394 | -0.735754 |
| tossup | end_difficulty_d2 | 1240 | -2.11745 | 1.39905 | -6.77688 | -4.71207 | -3.22237 | -1.57671 | -1.05294 | -0.572194 | 0.592469 |
| tossup | end_difficulty_d3 | 1240 | -2.38631 | 1.29942 | -6.19724 | -4.53856 | -3.53414 | -2.14098 | -1.27024 | -0.634917 | 0.0750675 |
| tossup | total_drop_d1 | 1240 | 1.10314 | 0.427409 | 0.355873 | 0.654794 | 0.865912 | 1.01611 | 1.19212 | 1.85428 | 5.24965 |
| tossup | total_drop_d2 | 1240 | 1.04223 | 0.230314 | 0.544801 | 0.793539 | 0.927689 | 0.988152 | 1.08515 | 1.47863 | 3.023 |
| tossup | total_drop_d3 | 1240 | 1.05464 | 0.215244 | 0.588834 | 0.846417 | 0.940897 | 1.00583 | 1.10705 | 1.42707 | 3.43954 |
| tossup | drop_share_1_d1 | 1240 | 0.358658 | 0.0506304 | 0.21272 | 0.29912 | 0.322005 | 0.348926 | 0.387057 | 0.457584 | 0.625655 |
| tossup | drop_share_2_d1 | 1240 | 0.336354 | 0.0208946 | 0.244616 | 0.303814 | 0.322781 | 0.336823 | 0.348833 | 0.366409 | 0.504474 |
| tossup | drop_share_3_d1 | 1240 | 0.304988 | 0.0459812 | 0.12973 | 0.224057 | 0.277001 | 0.312603 | 0.337076 | 0.367771 | 0.471299 |
| tossup | drop_share_1_d2 | 1240 | 0.324221 | 0.0281181 | 0.241067 | 0.292668 | 0.306573 | 0.317456 | 0.333734 | 0.380634 | 0.505584 |
| tossup | drop_share_2_d2 | 1240 | 0.344577 | 0.0137386 | 0.296721 | 0.316874 | 0.338393 | 0.345924 | 0.353169 | 0.363387 | 0.436513 |
| tossup | drop_share_3_d2 | 1240 | 0.331202 | 0.0260376 | 0.189619 | 0.281088 | 0.32031 | 0.335399 | 0.347311 | 0.364228 | 0.433607 |
| tossup | drop_share_1_d3 | 1240 | 0.332695 | 0.0327849 | 0.248747 | 0.295069 | 0.310371 | 0.323547 | 0.347361 | 0.402982 | 0.465317 |
| tossup | drop_share_2_d3 | 1240 | 0.343535 | 0.012009 | 0.302493 | 0.323362 | 0.336446 | 0.343628 | 0.350684 | 0.362935 | 0.409017 |
| tossup | drop_share_3_d3 | 1240 | 0.323771 | 0.0307562 | 0.208028 | 0.256987 | 0.311647 | 0.331295 | 0.344483 | 0.360433 | 0.390526 |
| tossup | r_1 | 1240 | 0.542642 | 0.298579 | 0.0488618 | 0.0843414 | 0.244191 | 0.642231 | 0.82481 | 0.902367 | 0.965611 |
| tossup | r_2 | 1240 | 0.185341 | 0.177253 | 0.0186604 | 0.0353956 | 0.0613434 | 0.102041 | 0.247656 | 0.573528 | 0.883327 |
| tossup | r_3 | 1240 | 0.272016 | 0.282904 | 0.0153176 | 0.0318486 | 0.0643883 | 0.115945 | 0.573119 | 0.80258 | 0.908301 |
| tossup | r_norm | 1240 | 0.771665 | 0.0882373 | 0.577395 | 0.62615 | 0.700578 | 0.776491 | 0.841801 | 0.905522 | 0.96592 |
