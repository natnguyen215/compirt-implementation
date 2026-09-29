# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_3/fold_1/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_3/fold_1`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 335654 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.555738 |
| log_loss | 0.614696 |
| ece | 0.108909 |
| brier | 0.193351 |
| accuracy | 0.761795 |
| all_correct_accuracy | 0.762125 |
| accuracy_lift_over_all_correct | -0.000329924 |
| probability_std | 0.0921284 |
| probability_p10 | 0.738315 |
| probability_p50 | 0.892556 |
| probability_p90 | 0.952563 |
| mean_predictive_variance | 0.107422 |
| integrated_brier_score | 0.176047 |
| joint_tossup_event_log_loss | 7.76951 |
| buzz_position_mae | 0.346246 |
| buzz_position_median_absolute_error | 0.352239 |
| buzz_position_bias | -0.334432 |
| survival_events | 9240 |
| joint_tossup_event_log_loss_events | 9240 |
| first_buzzer_top1_accuracy | 0.352689 |
| first_buzzer_mean_reciprocal_rank | 0.568866 |
| first_buzzer_log_loss | 1.6551 |
| first_buzzer_events | 9093 |
| first_buzzer_team_top1_accuracy | 0.614979 |
| tossup_scorer_player_top1_accuracy | 0.274892 |
| tossup_scorer_team_top1_accuracy | 0.397727 |
| tossup_game_winner_accuracy | 0.718468 |
| tossup_game_margin_mae | 42.1881 |
| tournament_player_ppg_spearman | 0.589903 |
| tournament_player_ppg_mae | 10.2679 |
| tournament_player_ppg_top10_overlap | 0.589655 |
| neg_auroc | 0.555738 |
| neg_average_precision | 0.283191 |
| neg_precision | 0.451613 |
| neg_recall | 0.00647249 |
| full_pmf_events | 9240 |
| full_pmf_final_decile_mass | 0.0285263 |
| no_buzz_observed_rate | 0.0159091 |
| no_buzz_predicted_rate | 0.238169 |
| no_buzz_calibration_error | 0.22226 |
| no_buzz_brier | 0.0741156 |
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
| tossup_correctness | aggregate | all | 9093 | 0.555738 | 0.614696 | 0.108909 | 0.193351 | 0.761795 | 0.762125 | -0.000329924 | 0.0921284 | 0.738315 | 0.892556 | 0.952563 | 0.107422 |
| tossup_correctness | tier | fall | 2842 | 0.57055 | 0.55491 | 0.0885179 | 0.175266 | 0.785011 | 0.785362 | -0.000351865 | 0.0825721 | 0.76232 | 0.888086 | 0.943591 | 0.10906 |
| tossup_correctness | tier | nationals | 1564 | 0.571007 | 0.673158 | 0.125659 | 0.217996 | 0.71867 | 0.718031 | 0.000639386 | 0.110822 | 0.677071 | 0.869194 | 0.954177 | 0.122808 |
| tossup_correctness | tier | regionals | 1937 | 0.529545 | 0.637408 | 0.117961 | 0.198542 | 0.757357 | 0.758389 | -0.00103252 | 0.100659 | 0.717007 | 0.892594 | 0.955164 | 0.108385 |
| tossup_correctness | tier | winter | 2750 | 0.544686 | 0.627235 | 0.120773 | 0.194367 | 0.765455 | 0.765818 | -0.000363636 | 0.0783912 | 0.781013 | 0.905011 | 0.957512 | 0.0962993 |
| tossup_correctness | category | Current Events | 126 | 0.532172 | 0.596932 | 0.114749 | 0.190245 | 0.769841 | 0.769841 | 0 | 0.0909584 | 0.718938 | 0.876378 | 0.925028 | 0.121307 |
| tossup_correctness | category | Fine Arts | 1071 | 0.572404 | 0.608844 | 0.120687 | 0.191807 | 0.764706 | 0.766573 | -0.00186741 | 0.0820737 | 0.771806 | 0.900926 | 0.953834 | 0.100504 |
| tossup_correctness | category | Geography | 185 | 0.565476 | 0.719182 | 0.171777 | 0.235064 | 0.708108 | 0.697297 | 0.0108108 | 0.0955852 | 0.734668 | 0.890035 | 0.951813 | 0.108856 |
| tossup_correctness | category | History | 1440 | 0.542956 | 0.626566 | 0.110732 | 0.199108 | 0.754167 | 0.754167 | 0 | 0.0943051 | 0.719095 | 0.884099 | 0.949046 | 0.114556 |
| tossup_correctness | category | Literature | 1422 | 0.540659 | 0.519397 | 0.0683067 | 0.156665 | 0.814346 | 0.814346 | 0 | 0.0838522 | 0.771676 | 0.895159 | 0.957698 | 0.102912 |
| tossup_correctness | category | Mythology | 318 | 0.597491 | 0.54751 | 0.0960777 | 0.170498 | 0.795597 | 0.789308 | 0.00628931 | 0.089412 | 0.758236 | 0.905828 | 0.946165 | 0.100505 |
| tossup_correctness | category | Other Academic | 66 | 0.473684 | 0.770763 | 0.194743 | 0.241759 | 0.712121 | 0.712121 | 0 | 0.0953932 | 0.728481 | 0.89284 | 0.961157 | 0.10649 |
| tossup_correctness | category | Philosophy | 311 | 0.607213 | 0.642213 | 0.141778 | 0.202509 | 0.742765 | 0.745981 | -0.00321543 | 0.0891565 | 0.769226 | 0.912736 | 0.956811 | 0.0942526 |
| tossup_correctness | category | Popular Culture | 102 | 0.57963 | 0.375764 | 0.056291 | 0.109784 | 0.872549 | 0.882353 | -0.00980392 | 0.0837397 | 0.791254 | 0.8906 | 0.941682 | 0.106063 |
| tossup_correctness | category | Religion | 358 | 0.590939 | 0.71145 | 0.170668 | 0.231156 | 0.706704 | 0.712291 | -0.00558659 | 0.100449 | 0.724408 | 0.900068 | 0.948268 | 0.104601 |
| tossup_correctness | category | Science | 1433 | 0.567289 | 0.644234 | 0.119842 | 0.20625 | 0.739009 | 0.738311 | 0.000697837 | 0.0918588 | 0.727703 | 0.881089 | 0.950259 | 0.113288 |
| tossup_correctness | category | Social Science | 324 | 0.592415 | 0.656415 | 0.142776 | 0.211489 | 0.731481 | 0.731481 | 0 | 0.0794883 | 0.768077 | 0.897092 | 0.945329 | 0.103613 |
| tossup_correctness | category | Unknown | 1937 | 0.529545 | 0.637408 | 0.117961 | 0.198542 | 0.757357 | 0.758389 | -0.00103252 | 0.100659 | 0.717007 | 0.892594 | 0.955164 | 0.108385 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 167 | 0.511029 | 0.689438 | 0.130484 | 0.224162 | 0.712575 | 0.712575 | 0 | 0.0911741 | 0.691447 | 0.856047 | 0.934029 | 0.130208 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 912 | 0.557371 | 0.645023 | 0.117887 | 0.211363 | 0.722588 | 0.729167 | -0.00657895 | 0.0993834 | 0.703586 | 0.858165 | 0.934444 | 0.127843 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2115 | 0.539056 | 0.618984 | 0.109963 | 0.198066 | 0.756501 | 0.755083 | 0.00141844 | 0.0912609 | 0.734536 | 0.87891 | 0.941599 | 0.115636 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2844 | 0.559899 | 0.574571 | 0.0959977 | 0.180038 | 0.780942 | 0.780942 | 0 | 0.0882525 | 0.746722 | 0.893204 | 0.950831 | 0.106356 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3055 | 0.55582 | 0.635941 | 0.124934 | 0.195418 | 0.762029 | 0.762029 | 0 | 0.0901783 | 0.763044 | 0.90999 | 0.961333 | 0.0953857 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1167 | -1.43004 | 0.651516 | -2.99869 | -2.33847 | -1.82717 | -1.49853 | -1.11853 | -0.437557 | 1.94064 |
| player | beta | 1167 | -3.1819 | 1.04186 | -6.63588 | -5.39401 | -3.71752 | -2.93708 | -2.39707 | -1.88604 | -1.57467 |
| player | theta_1 | 1167 | 0.912838 | 0.927459 | -2.87319 | -0.862694 | 0.380741 | 1.0172 | 1.56965 | 2.25633 | 3.53087 |
| player | theta_2 | 1167 | 0.900544 | 0.931364 | -2.33771 | -0.767413 | 0.280903 | 1.03753 | 1.5762 | 2.25262 | 3.65239 |
| player | theta_3 | 1167 | 0.889585 | 0.904284 | -2.12541 | -0.823264 | 0.304566 | 1.01048 | 1.54437 | 2.17593 | 3.57292 |
| player | theta_norm | 1167 | 2.13478 | 0.64951 | 0.19432 | 0.956672 | 1.7197 | 2.20109 | 2.59656 | 3.05622 | 4.13573 |
| tossup | start_difficulty_d1 | 1220 | -1.03823 | 0.509743 | -2.19089 | -1.88932 | -1.46669 | -0.991761 | -0.583893 | -0.326285 | -0.0283019 |
| tossup | start_difficulty_d2 | 1220 | -0.976888 | 0.439883 | -2.00995 | -1.72655 | -1.34854 | -0.933042 | -0.589169 | -0.351294 | -0.156439 |
| tossup | start_difficulty_d3 | 1220 | -0.951955 | 0.408819 | -2.0313 | -1.68053 | -1.26751 | -0.909042 | -0.626304 | -0.364545 | -0.0888958 |
| tossup | end_difficulty_d1 | 1220 | -1.68341 | 0.428088 | -2.816 | -2.43017 | -2.0412 | -1.59715 | -1.32758 | -1.12023 | -0.930234 |
| tossup | end_difficulty_d2 | 1220 | -1.64261 | 0.363423 | -2.84975 | -2.2742 | -1.90288 | -1.59438 | -1.34951 | -1.14295 | -0.922867 |
| tossup | end_difficulty_d3 | 1220 | -1.62443 | 0.331635 | -2.80051 | -2.18967 | -1.87196 | -1.59372 | -1.36953 | -1.1421 | -0.950724 |
| tossup | total_drop_d1 | 1220 | 0.645178 | 0.184731 | 0.227248 | 0.296848 | 0.512185 | 0.681963 | 0.79079 | 0.898555 | 1.04663 |
| tossup | total_drop_d2 | 1220 | 0.665722 | 0.174649 | 0.22523 | 0.333518 | 0.551469 | 0.695585 | 0.797995 | 0.911335 | 1.0309 |
| tossup | total_drop_d3 | 1220 | 0.672475 | 0.178668 | 0.221764 | 0.343799 | 0.534992 | 0.721856 | 0.811417 | 0.91457 | 1.01452 |
| tossup | drop_share_1_d1 | 1220 | 0.327705 | 0.0297513 | 0.195365 | 0.284425 | 0.310488 | 0.324569 | 0.343494 | 0.379716 | 0.465765 |
| tossup | drop_share_2_d1 | 1220 | 0.321244 | 0.0174643 | 0.25543 | 0.287549 | 0.311186 | 0.324224 | 0.333457 | 0.345647 | 0.36317 |
| tossup | drop_share_3_d1 | 1220 | 0.351052 | 0.0308316 | 0.239591 | 0.306235 | 0.332762 | 0.348821 | 0.367305 | 0.40494 | 0.534539 |
| tossup | drop_share_1_d2 | 1220 | 0.322066 | 0.0247708 | 0.225182 | 0.281204 | 0.309022 | 0.322518 | 0.335949 | 0.361777 | 0.424811 |
| tossup | drop_share_2_d2 | 1220 | 0.322291 | 0.0185536 | 0.250527 | 0.284683 | 0.312317 | 0.326138 | 0.335066 | 0.346488 | 0.368152 |
| tossup | drop_share_3_d2 | 1220 | 0.355643 | 0.0323258 | 0.274009 | 0.316359 | 0.335732 | 0.348931 | 0.369389 | 0.419586 | 0.495955 |
| tossup | drop_share_1_d3 | 1220 | 0.323139 | 0.0264043 | 0.204279 | 0.282342 | 0.31091 | 0.322739 | 0.33665 | 0.365108 | 0.427209 |
| tossup | drop_share_2_d3 | 1220 | 0.322894 | 0.0182761 | 0.254946 | 0.287829 | 0.31194 | 0.326924 | 0.33641 | 0.346575 | 0.366117 |
| tossup | drop_share_3_d3 | 1220 | 0.353967 | 0.0331356 | 0.272858 | 0.312855 | 0.334005 | 0.348601 | 0.366311 | 0.420626 | 0.505676 |
| tossup | r_1 | 1220 | 0.355911 | 0.252338 | 0.0265292 | 0.0637877 | 0.131891 | 0.287842 | 0.573457 | 0.817406 | 0.924878 |
| tossup | r_2 | 1220 | 0.331412 | 0.251224 | 0.0341398 | 0.0654016 | 0.119646 | 0.234255 | 0.532318 | 0.801104 | 0.938352 |
| tossup | r_3 | 1220 | 0.312677 | 0.242794 | 0.0351188 | 0.066872 | 0.12253 | 0.219723 | 0.450675 | 0.81424 | 0.915669 |
| tossup | r_norm | 1220 | 0.715403 | 0.0897929 | 0.577412 | 0.587631 | 0.637328 | 0.707654 | 0.788481 | 0.870111 | 0.939384 |
