# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-10000-20260913-195429/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/dd-332-normalized-v1-10000-20260913-195429/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 278693 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.707467 |
| log_loss | 0.499036 |
| ece | 0.014965 |
| brier | 0.162382 |
| accuracy | 0.770593 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | 0.00846805 |
| probability_std | 0.15141 |
| probability_p10 | 0.556347 |
| probability_p50 | 0.809623 |
| probability_p90 | 0.923805 |
| mean_predictive_variance | 0.154291 |
| integrated_brier_score | 0.0946409 |
| joint_tossup_event_log_loss | 6.45775 |
| buzz_position_mae | 0.141477 |
| buzz_position_median_absolute_error | 0.121228 |
| buzz_position_bias | -0.0192668 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.362477 |
| first_buzzer_mean_reciprocal_rank | 0.575306 |
| first_buzzer_log_loss | 1.64623 |
| first_buzzer_events | 9093 |
| first_buzzer_player_replay_accuracy | 0.208182 |
| first_buzzer_team_replay_accuracy | 0.468052 |
| tossup_scorer_player_replay_accuracy | 0.232576 |
| tossup_scorer_team_replay_accuracy | 0.433983 |
| tossup_game_winner_accuracy | 0.689579 |
| tossup_model_official_winner_accuracy | 0.707424 |
| tossup_game_margin_mae | 46.5584 |
| tossup_game_zero_margin_mae | 55.2922 |
| tournament_player_ppg_spearman | 0.610701 |
| tournament_player_ppg_mae | 12.2554 |
| tournament_player_ppg_top10_overlap | 0.589655 |
| tournament_player_ppg_top10_random_overlap | 0.269705 |
| tournament_player_ppg_top10_adjusted_overlap | 0.442768 |
| neg_auroc | 0.707467 |
| neg_average_precision | 0.44106 |
| neg_precision | 0.561997 |
| neg_recall | 0.16135 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.176868 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.0230869 |
| no_buzz_calibration_error | 0.00717783 |
| no_buzz_brier | 0.0165859 |
| full_pmf_max_mass_error | 5.55112e-16 |
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
| tossup_game_winner_accuracy | 0.689579 |
| tossup_game_margin_mae | 46.5584 |
| tossup_game_zero_margin_mae | 55.2922 |
| tossup_game_margin_mae_games | 462 |
| tossup_outcome_schema_version | 3 |
| tossup_game_winner_accuracy_games | 451 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9093 | 0.707467 | 0.499036 | 0.014965 | 0.162382 | 0.770593 | 0.762125 | 0.00846805 | 0.15141 | 0.556347 | 0.809623 | 0.923805 | 0.154291 |
| tossup_correctness | tier | fall | 2842 | 0.724867 | 0.465847 | 0.0150357 | 0.14967 | 0.792048 | 0.785362 | 0.00668543 | 0.143496 | 0.566872 | 0.820666 | 0.929349 | 0.150099 |
| tossup_correctness | tier | nationals | 1564 | 0.715885 | 0.539591 | 0.0445876 | 0.179493 | 0.732737 | 0.718031 | 0.0147059 | 0.160331 | 0.533571 | 0.797067 | 0.918085 | 0.158799 |
| tossup_correctness | tier | regionals | 1937 | 0.688399 | 0.513406 | 0.025895 | 0.168057 | 0.757873 | 0.758389 | -0.000516262 | 0.149232 | 0.555137 | 0.807066 | 0.917776 | 0.156276 |
| tossup_correctness | tier | winter | 2750 | 0.695532 | 0.500149 | 0.0163364 | 0.161792 | 0.778909 | 0.765818 | 0.0130909 | 0.154761 | 0.55687 | 0.806668 | 0.923806 | 0.154661 |
| tossup_correctness | category | Current Events | 126 | 0.721294 | 0.488962 | 0.0756196 | 0.159235 | 0.785714 | 0.769841 | 0.015873 | 0.131459 | 0.532956 | 0.770552 | 0.882537 | 0.175605 |
| tossup_correctness | category | Fine Arts | 1071 | 0.745505 | 0.471338 | 0.0237628 | 0.152312 | 0.784314 | 0.766573 | 0.0177404 | 0.15989 | 0.541479 | 0.803056 | 0.924871 | 0.1549 |
| tossup_correctness | category | Geography | 185 | 0.791944 | 0.496605 | 0.0690699 | 0.163836 | 0.745946 | 0.697297 | 0.0486486 | 0.224117 | 0.341311 | 0.755384 | 0.901365 | 0.1666 |
| tossup_correctness | category | History | 1440 | 0.700915 | 0.515078 | 0.0310072 | 0.169098 | 0.761111 | 0.754167 | 0.00694444 | 0.148756 | 0.561224 | 0.812593 | 0.927842 | 0.152997 |
| tossup_correctness | category | Literature | 1422 | 0.67542 | 0.455484 | 0.0208319 | 0.143679 | 0.805907 | 0.814346 | -0.00843882 | 0.134405 | 0.617717 | 0.837083 | 0.935629 | 0.140599 |
| tossup_correctness | category | Mythology | 318 | 0.652257 | 0.488344 | 0.0477206 | 0.154158 | 0.801887 | 0.789308 | 0.0125786 | 0.127353 | 0.626917 | 0.825991 | 0.931283 | 0.145267 |
| tossup_correctness | category | Other Academic | 66 | 0.790594 | 0.518103 | 0.0943518 | 0.174648 | 0.727273 | 0.712121 | 0.0151515 | 0.141064 | 0.610347 | 0.801864 | 0.89183 | 0.16104 |
| tossup_correctness | category | Philosophy | 311 | 0.714644 | 0.515497 | 0.0858781 | 0.171992 | 0.729904 | 0.745981 | -0.0160772 | 0.139408 | 0.595232 | 0.81577 | 0.925425 | 0.152429 |
| tossup_correctness | category | Popular Culture | 102 | 0.524074 | 0.381969 | 0.0628418 | 0.108654 | 0.882353 | 0.882353 | 0 | 0.0788435 | 0.724304 | 0.856996 | 0.916456 | 0.131452 |
| tossup_correctness | category | Religion | 358 | 0.711936 | 0.541289 | 0.0452999 | 0.180051 | 0.743017 | 0.712291 | 0.0307263 | 0.163149 | 0.480271 | 0.770486 | 0.898466 | 0.171989 |
| tossup_correctness | category | Science | 1433 | 0.696552 | 0.527904 | 0.0274966 | 0.173886 | 0.755059 | 0.738311 | 0.0167481 | 0.151753 | 0.543953 | 0.796606 | 0.917831 | 0.159623 |
| tossup_correctness | category | Social Science | 324 | 0.781415 | 0.483134 | 0.0583696 | 0.157236 | 0.777778 | 0.731481 | 0.0462963 | 0.160949 | 0.487329 | 0.787412 | 0.900624 | 0.164263 |
| tossup_correctness | category | Unknown | 1937 | 0.688399 | 0.513406 | 0.025895 | 0.168057 | 0.757873 | 0.758389 | -0.000516262 | 0.149232 | 0.555137 | 0.807066 | 0.917776 | 0.156276 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.594013 | 0.621263 | 0.0767328 | 0.208777 | 0.694611 | 0.712575 | -0.0179641 | 0.138434 | 0.55558 | 0.779235 | 0.889548 | 0.172837 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.718602 | 0.524649 | 0.0266258 | 0.173607 | 0.752193 | 0.729167 | 0.0230263 | 0.166986 | 0.501461 | 0.78535 | 0.912625 | 0.163807 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.710986 | 0.504762 | 0.0274764 | 0.164982 | 0.769267 | 0.755083 | 0.0141844 | 0.144227 | 0.579282 | 0.813181 | 0.922883 | 0.15252 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.690209 | 0.486085 | 0.0121398 | 0.156079 | 0.78692 | 0.780942 | 0.0059775 | 0.135252 | 0.60194 | 0.82012 | 0.924018 | 0.149673 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.719613 | 0.4928 | 0.0188182 | 0.160563 | 0.765957 | 0.762029 | 0.00392799 | 0.163543 | 0.517637 | 0.804792 | 0.927235 | 0.155961 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1167 | 1.28066 | 0.802544 | -1.02459 | 0.0146574 | 0.725265 | 1.28085 | 1.79221 | 2.678 | 3.55944 |
| player | theta_1 | 1167 | -0.595069 | 0.928176 | -3.07137 | -1.94321 | -1.21382 | -0.689542 | -0.0505254 | 1.07218 | 3.24787 |
| player | theta_2 | 1167 | -0.485377 | 0.848403 | -3.03437 | -1.82598 | -1.01093 | -0.547635 | 0.0083348 | 0.981928 | 2.59502 |
| player | theta_3 | 1167 | -0.512005 | 0.941935 | -3.43049 | -1.89277 | -1.13183 | -0.620715 | 0.011132 | 1.18778 | 2.89098 |
| player | theta_norm | 1167 | 1.70308 | 0.646637 | 0.220197 | 0.738618 | 1.26484 | 1.62124 | 2.11457 | 2.88677 | 4.43611 |
| tossup | start_difficulty_d1 | 1220 | -1.12729 | 0.529458 | -2.61513 | -1.87347 | -1.47301 | -1.15756 | -0.829166 | -0.335667 | 1.86849 |
| tossup | start_difficulty_d2 | 1220 | -1.12071 | 0.496213 | -2.74455 | -1.82731 | -1.46044 | -1.16425 | -0.832204 | -0.230407 | 1.02921 |
| tossup | start_difficulty_d3 | 1220 | -1.12634 | 0.499342 | -3.02099 | -1.88654 | -1.44759 | -1.12887 | -0.818214 | -0.332838 | 0.864855 |
| tossup | end_difficulty_d1 | 1220 | -2.1237 | 0.618991 | -3.78649 | -3.0281 | -2.50928 | -2.15892 | -1.7673 | -1.19361 | 1.18047 |
| tossup | end_difficulty_d2 | 1220 | -2.11659 | 0.579425 | -4.09583 | -2.95854 | -2.51999 | -2.16083 | -1.77542 | -1.10456 | 0.141884 |
| tossup | end_difficulty_d3 | 1220 | -2.12169 | 0.585834 | -4.34391 | -3.03166 | -2.50175 | -2.11273 | -1.75598 | -1.20805 | 0.252566 |
| tossup | total_drop_d1 | 1220 | 0.996408 | 0.110182 | 0.605657 | 0.811233 | 0.929472 | 0.996316 | 1.06437 | 1.17814 | 1.39882 |
| tossup | total_drop_d2 | 1220 | 0.995879 | 0.102994 | 0.644011 | 0.823941 | 0.929963 | 1.00028 | 1.06249 | 1.15684 | 1.4989 |
| tossup | total_drop_d3 | 1220 | 0.995346 | 0.104941 | 0.612289 | 0.835796 | 0.925113 | 0.991895 | 1.0611 | 1.17207 | 1.42771 |
| tossup | drop_share_1_d1 | 1220 | 0.304413 | 0.0150248 | 0.234256 | 0.279943 | 0.29538 | 0.305022 | 0.314085 | 0.327974 | 0.354945 |
| tossup | drop_share_2_d1 | 1220 | 0.346708 | 0.0115741 | 0.308632 | 0.328333 | 0.33866 | 0.34653 | 0.354676 | 0.366054 | 0.382212 |
| tossup | drop_share_3_d1 | 1220 | 0.348879 | 0.0156903 | 0.306283 | 0.32469 | 0.339 | 0.348055 | 0.358531 | 0.375458 | 0.444339 |
| tossup | drop_share_1_d2 | 1220 | 0.3046 | 0.014874 | 0.239743 | 0.279381 | 0.295569 | 0.30516 | 0.313935 | 0.327828 | 0.357222 |
| tossup | drop_share_2_d2 | 1220 | 0.347098 | 0.0116571 | 0.313062 | 0.327602 | 0.338952 | 0.346836 | 0.355206 | 0.3662 | 0.399203 |
| tossup | drop_share_3_d2 | 1220 | 0.348301 | 0.0155458 | 0.299617 | 0.323534 | 0.338465 | 0.347159 | 0.357376 | 0.375622 | 0.42775 |
| tossup | drop_share_1_d3 | 1220 | 0.304341 | 0.0146951 | 0.244671 | 0.281454 | 0.295188 | 0.30491 | 0.314037 | 0.326473 | 0.362045 |
| tossup | drop_share_2_d3 | 1220 | 0.347081 | 0.0113935 | 0.312178 | 0.328179 | 0.339257 | 0.347128 | 0.355046 | 0.365737 | 0.382284 |
| tossup | drop_share_3_d3 | 1220 | 0.348577 | 0.0153152 | 0.285861 | 0.324205 | 0.338131 | 0.348684 | 0.357834 | 0.374289 | 0.418767 |
| tossup | r_1 | 1220 | 0.321043 | 0.166105 | 0.0464805 | 0.107961 | 0.185769 | 0.288642 | 0.43507 | 0.636066 | 0.880216 |
| tossup | r_2 | 1220 | 0.336245 | 0.170104 | 0.0478497 | 0.11999 | 0.208926 | 0.293997 | 0.436503 | 0.681557 | 0.860669 |
| tossup | r_3 | 1220 | 0.342711 | 0.171665 | 0.0525701 | 0.117216 | 0.205484 | 0.31061 | 0.457276 | 0.675837 | 0.862484 |
| tossup | r_norm | 1220 | 0.645035 | 0.0586312 | 0.577401 | 0.581678 | 0.600443 | 0.628191 | 0.673232 | 0.768961 | 0.884325 |
| tossup_hazard | hazard_start_difficulty_d1 | 1220 | 7.50303 | 0.528005 | 4.52033 | 6.67277 | 7.29745 | 7.46169 | 7.72418 | 8.46759 | 9.4939 |
| tossup_hazard | hazard_start_difficulty_d2 | 1220 | 7.49424 | 0.478636 | 4.00306 | 6.701 | 7.35829 | 7.4894 | 7.66318 | 8.25706 | 9.82324 |
| tossup_hazard | hazard_start_difficulty_d3 | 1220 | 7.51884 | 0.490027 | 4.09516 | 6.76215 | 7.36632 | 7.50602 | 7.70876 | 8.30867 | 9.4169 |
| tossup_hazard | hazard_end_difficulty_d1 | 1220 | 3.83721 | 3.39317 | -12.1795 | -2.47164 | 1.37241 | 6.1175 | 6.43891 | 6.76511 | 7.77601 |
| tossup_hazard | hazard_end_difficulty_d2 | 1220 | 4.60544 | 3.29954 | -11.2345 | -2.2244 | 2.69496 | 6.37776 | 6.53329 | 6.82235 | 7.48926 |
| tossup_hazard | hazard_end_difficulty_d3 | 1220 | 4.78663 | 3.2966 | -15.6353 | -2.285 | 4.27015 | 6.40471 | 6.58412 | 6.95563 | 7.5221 |
| tossup_hazard | hazard_total_drop_d1 | 1220 | 3.66582 | 3.49339 | 0.858552 | 0.950878 | 1.00969 | 1.10204 | 6.26472 | 10.2114 | 19.9032 |
| tossup_hazard | hazard_total_drop_d2 | 1220 | 2.8888 | 3.37481 | 0.862494 | 0.946479 | 0.993492 | 1.03926 | 4.35597 | 10.1313 | 19.1141 |
| tossup_hazard | hazard_total_drop_d3 | 1220 | 2.73221 | 3.32513 | 0.868063 | 0.934978 | 0.985287 | 1.0299 | 3.00315 | 9.90095 | 23.8424 |
| tossup_hazard | hazard_drop_share_1_d1 | 1220 | 0.253418 | 0.0921919 | 0.0391381 | 0.0923966 | 0.179014 | 0.288551 | 0.305126 | 0.332095 | 0.703075 |
| tossup_hazard | hazard_drop_share_2_d1 | 1220 | 0.331568 | 0.0856761 | 0.0593174 | 0.15933 | 0.319782 | 0.345031 | 0.358628 | 0.471055 | 0.702144 |
| tossup_hazard | hazard_drop_share_3_d1 | 1220 | 0.415015 | 0.14028 | 0.085131 | 0.253591 | 0.342189 | 0.35844 | 0.460036 | 0.730585 | 0.89033 |
| tossup_hazard | hazard_drop_share_1_d2 | 1220 | 0.271327 | 0.0814054 | 0.0388744 | 0.105896 | 0.269763 | 0.294856 | 0.307265 | 0.327633 | 0.722854 |
| tossup_hazard | hazard_drop_share_2_d2 | 1220 | 0.337025 | 0.0742692 | 0.062066 | 0.173255 | 0.335729 | 0.346548 | 0.357619 | 0.430842 | 0.678766 |
| tossup_hazard | hazard_drop_share_3_d2 | 1220 | 0.391648 | 0.123771 | 0.0753972 | 0.27647 | 0.343017 | 0.354099 | 0.373809 | 0.69907 | 0.896361 |
| tossup_hazard | hazard_drop_share_1_d3 | 1220 | 0.27307 | 0.0783358 | 0.0453458 | 0.101364 | 0.270851 | 0.293129 | 0.305895 | 0.32655 | 0.694429 |
| tossup_hazard | hazard_drop_share_2_d3 | 1220 | 0.340065 | 0.065593 | 0.0857964 | 0.205979 | 0.334868 | 0.347021 | 0.35775 | 0.419873 | 0.701824 |
| tossup_hazard | hazard_drop_share_3_d3 | 1220 | 0.386865 | 0.110668 | 0.06642 | 0.280173 | 0.343319 | 0.35685 | 0.376835 | 0.672685 | 0.867752 |
| tossup_hazard | hazard_r_1 | 1220 | 0.389343 | 0.296941 | 0.0178721 | 0.0384906 | 0.105848 | 0.303452 | 0.654555 | 0.879894 | 0.941143 |
| tossup_hazard | hazard_r_2 | 1220 | 0.296269 | 0.273135 | 0.0109389 | 0.0301434 | 0.0715563 | 0.17438 | 0.522098 | 0.832952 | 0.928179 |
| tossup_hazard | hazard_r_3 | 1220 | 0.314388 | 0.2602 | 0.0147093 | 0.0299178 | 0.0827947 | 0.239979 | 0.499236 | 0.81251 | 0.971189 |
