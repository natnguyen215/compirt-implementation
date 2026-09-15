# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_4/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-difficulty-three-slice/dim_4/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 323824 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.640472 |
| log_loss | 0.514227 |
| ece | 0.0249283 |
| brier | 0.167328 |
| accuracy | 0.774973 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00161812 |
| probability_std | 0.116662 |
| probability_p10 | 0.605782 |
| probability_p50 | 0.785152 |
| probability_p90 | 0.899555 |
| mean_predictive_variance | 0.165268 |
| integrated_brier_score | 0.102662 |
| joint_tossup_event_log_loss | 6.90431 |
| buzz_position_mae | 0.162239 |
| buzz_position_median_absolute_error | 0.148129 |
| buzz_position_bias | -0.0684378 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.369903 |
| first_buzzer_mean_reciprocal_rank | 0.578704 |
| first_buzzer_log_loss | 1.64918 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.642179 |
| tossup_scorer_player_top1_accuracy | 0.323241 |
| tossup_scorer_team_top1_accuracy | 0.492857 |
| tossup_game_winner_accuracy | 0.792123 |
| tossup_game_margin_mae | 35.546 |
| tournament_player_ppg_spearman | 0.687782 |
| tournament_player_ppg_mae | 9.24887 |
| tournament_player_ppg_top10_overlap | 0.641379 |
| neg_auroc | 0.640472 |
| neg_average_precision | 0.355432 |
| neg_precision | 0.527076 |
| neg_recall | 0.0694907 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0552449 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.090979 |
| no_buzz_calibration_error | 0.0792519 |
| no_buzz_brier | 0.0245967 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9380 |
| first_buzzer_team_top1_accuracy_events | 9270 |
| tossup_scorer_player_top1_accuracy_events | 9380 |
| tossup_scorer_team_top1_accuracy_events | 9380 |
| tossup_game_winner_accuracy_games | 457 |
| tossup_game_margin_mae_games | 469 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.640472 | 0.514227 | 0.0249283 | 0.167328 | 0.774973 | 0.773355 | 0.00161812 | 0.116662 | 0.605782 | 0.785152 | 0.899555 | 0.165268 |
| tossup_correctness | tier | fall | 2876 | 0.616397 | 0.497253 | 0.0357535 | 0.159684 | 0.793463 | 0.793115 | 0.000347705 | 0.107006 | 0.637679 | 0.812727 | 0.902356 | 0.155531 |
| tossup_correctness | tier | nationals | 1579 | 0.660029 | 0.552935 | 0.034557 | 0.184866 | 0.737809 | 0.729576 | 0.00823306 | 0.122663 | 0.523969 | 0.708797 | 0.842816 | 0.19655 |
| tossup_correctness | tier | regionals | 1990 | 0.662914 | 0.514439 | 0.018887 | 0.168543 | 0.768342 | 0.765829 | 0.00251256 | 0.105831 | 0.606525 | 0.763595 | 0.867257 | 0.17752 |
| tossup_correctness | tier | winter | 2825 | 0.631661 | 0.509722 | 0.0295005 | 0.164451 | 0.781593 | 0.783009 | -0.00141593 | 0.110501 | 0.645348 | 0.815793 | 0.922732 | 0.149066 |
| tossup_correctness | category | Current Events | 123 | 0.641966 | 0.529494 | 0.0734351 | 0.173568 | 0.772358 | 0.764228 | 0.00813008 | 0.110442 | 0.565942 | 0.720342 | 0.843283 | 0.19672 |
| tossup_correctness | category | Fine Arts | 1093 | 0.644108 | 0.516461 | 0.0239916 | 0.168842 | 0.774016 | 0.769442 | 0.00457457 | 0.103497 | 0.650378 | 0.810239 | 0.901923 | 0.155701 |
| tossup_correctness | category | Geography | 191 | 0.755008 | 0.536416 | 0.0592037 | 0.178233 | 0.727749 | 0.691099 | 0.0366492 | 0.146155 | 0.507054 | 0.767194 | 0.878282 | 0.177719 |
| tossup_correctness | category | History | 1469 | 0.653926 | 0.528359 | 0.0387062 | 0.173798 | 0.751532 | 0.758339 | -0.00680735 | 0.111364 | 0.619201 | 0.784899 | 0.898328 | 0.164637 |
| tossup_correctness | category | Literature | 1436 | 0.590566 | 0.481024 | 0.0418547 | 0.150574 | 0.811281 | 0.81546 | -0.00417827 | 0.0955808 | 0.697821 | 0.853214 | 0.932648 | 0.130861 |
| tossup_correctness | category | Mythology | 325 | 0.595034 | 0.476545 | 0.126943 | 0.150153 | 0.818462 | 0.843077 | -0.0246154 | 0.113418 | 0.574884 | 0.735895 | 0.864332 | 0.187438 |
| tossup_correctness | category | Other Academic | 67 | 0.626685 | 0.536675 | 0.115551 | 0.1763 | 0.776119 | 0.791045 | -0.0149254 | 0.116457 | 0.520519 | 0.689796 | 0.807058 | 0.20564 |
| tossup_correctness | category | Philosophy | 322 | 0.651601 | 0.496199 | 0.0305716 | 0.161015 | 0.785714 | 0.785714 | 0 | 0.103461 | 0.654837 | 0.814616 | 0.916477 | 0.151864 |
| tossup_correctness | category | Popular Culture | 100 | 0.480082 | 0.416461 | 0.124962 | 0.124331 | 0.88 | 0.89 | -0.01 | 0.108379 | 0.615934 | 0.790439 | 0.896683 | 0.166504 |
| tossup_correctness | category | Religion | 365 | 0.630963 | 0.578679 | 0.0589554 | 0.195663 | 0.723288 | 0.723288 | 0 | 0.119521 | 0.599353 | 0.78992 | 0.899548 | 0.165984 |
| tossup_correctness | category | Science | 1456 | 0.640776 | 0.519389 | 0.0536752 | 0.169181 | 0.780907 | 0.76717 | 0.0137363 | 0.129588 | 0.56241 | 0.756686 | 0.881628 | 0.177668 |
| tossup_correctness | category | Social Science | 333 | 0.647005 | 0.553927 | 0.0272879 | 0.18506 | 0.738739 | 0.72973 | 0.00900901 | 0.114951 | 0.582013 | 0.733096 | 0.867958 | 0.18368 |
| tossup_correctness | category | Unknown | 1990 | 0.662914 | 0.514439 | 0.018887 | 0.168543 | 0.768342 | 0.765829 | 0.00251256 | 0.105831 | 0.606525 | 0.763595 | 0.867257 | 0.17752 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.54942 | 0.574101 | 0.131711 | 0.191989 | 0.731844 | 0.748603 | -0.0167598 | 0.130541 | 0.496678 | 0.71074 | 0.820079 | 0.198517 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.58866 | 0.560851 | 0.0607588 | 0.186491 | 0.745037 | 0.754441 | -0.00940439 | 0.121704 | 0.539255 | 0.729346 | 0.852786 | 0.190646 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.635533 | 0.523637 | 0.0286295 | 0.17144 | 0.768044 | 0.766682 | 0.00136178 | 0.113764 | 0.589802 | 0.762516 | 0.87622 | 0.176773 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.654813 | 0.490349 | 0.0205436 | 0.157679 | 0.79315 | 0.787441 | 0.00570853 | 0.110155 | 0.623618 | 0.79771 | 0.899984 | 0.160796 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.656034 | 0.512546 | 0.0229163 | 0.166286 | 0.774128 | 0.771758 | 0.00237047 | 0.111244 | 0.635669 | 0.816157 | 0.918807 | 0.150955 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | -1.92699 | 1.10813 | -4.38663 | -3.4429 | -2.73517 | -2.14486 | -0.713981 | -0.13983 | 0.457331 |
| player | theta_2 | 1196 | -1.65004 | 0.667752 | -4.35165 | -2.85641 | -2.07271 | -1.5973 | -1.17883 | -0.632341 | 0.00263384 |
| player | theta_3 | 1196 | -1.06173 | 0.701016 | -3.72558 | -2.4489 | -1.48371 | -0.922229 | -0.552479 | -0.132057 | 0.785497 |
| player | theta_4 | 1196 | -1.65829 | 1.08577 | -4.79856 | -3.34926 | -2.54662 | -1.72637 | -0.523999 | -0.198095 | 0.231177 |
| player | theta_norm | 1196 | 3.59735 | 0.845105 | 1.60744 | 2.31703 | 2.95566 | 3.54399 | 4.17063 | 5.03271 | 6.30934 |
| tossup | start_difficulty_d1 | 1240 | -2.3835 | 1.28028 | -4.27726 | -3.65327 | -3.26092 | -2.91565 | -2.16944 | -0.0149965 | 0.400498 |
| tossup | start_difficulty_d2 | 1240 | -1.46735 | 1.12079 | -4.57037 | -3.42856 | -2.33448 | -1.38204 | -0.516283 | 0.0863018 | 0.805943 |
| tossup | start_difficulty_d3 | 1240 | -1.02743 | 0.904856 | -3.54559 | -2.6134 | -1.70392 | -0.870088 | -0.281038 | 0.222663 | 0.912205 |
| tossup | start_difficulty_d4 | 1240 | -1.46474 | 1.45359 | -4.71151 | -4.04289 | -2.77604 | -0.853691 | -0.197138 | 0.0526506 | 0.534841 |
| tossup | end_difficulty_d1 | 1240 | -3.47661 | 1.38193 | -6.53164 | -5.09903 | -4.41443 | -3.95451 | -2.98596 | -0.998089 | -0.52224 |
| tossup | end_difficulty_d2 | 1240 | -2.55581 | 1.26379 | -8.30725 | -4.70794 | -3.45401 | -2.47423 | -1.49767 | -0.834668 | -0.00272107 |
| tossup | end_difficulty_d3 | 1240 | -2.08464 | 1.03132 | -5.31448 | -3.95925 | -2.84633 | -1.89307 | -1.24679 | -0.705012 | 0.0679743 |
| tossup | end_difficulty_d4 | 1240 | -2.49964 | 1.50615 | -7.00147 | -5.17553 | -3.8348 | -1.9001 | -1.18979 | -0.911249 | -0.362374 |
| tossup | total_drop_d1 | 1240 | 1.09311 | 0.303898 | 0.579922 | 0.748522 | 0.933245 | 1.01763 | 1.18379 | 1.65117 | 4.1108 |
| tossup | total_drop_d2 | 1240 | 1.08846 | 0.331593 | 0.636905 | 0.822727 | 0.940526 | 1.01758 | 1.14071 | 1.52246 | 6.0498 |
| tossup | total_drop_d3 | 1240 | 1.0572 | 0.162821 | 0.819343 | 0.885489 | 0.953787 | 1.01374 | 1.11568 | 1.34772 | 2.61642 |
| tossup | total_drop_d4 | 1240 | 1.0349 | 0.203835 | 0.363739 | 0.761904 | 0.955536 | 1.00535 | 1.08153 | 1.34278 | 3.00184 |
| tossup | drop_share_1_d1 | 1240 | 0.355057 | 0.0417085 | 0.227592 | 0.296966 | 0.3165 | 0.356001 | 0.386131 | 0.424221 | 0.503816 |
| tossup | drop_share_2_d1 | 1240 | 0.337096 | 0.0163084 | 0.288236 | 0.310625 | 0.32629 | 0.33675 | 0.347243 | 0.361902 | 0.420276 |
| tossup | drop_share_3_d1 | 1240 | 0.307846 | 0.0392974 | 0.191416 | 0.240874 | 0.278604 | 0.311211 | 0.339842 | 0.361682 | 0.422527 |
| tossup | drop_share_1_d2 | 1240 | 0.333645 | 0.0313676 | 0.230352 | 0.298808 | 0.312307 | 0.325973 | 0.348183 | 0.394222 | 0.590477 |
| tossup | drop_share_2_d2 | 1240 | 0.343229 | 0.0130234 | 0.267711 | 0.319579 | 0.335871 | 0.34396 | 0.351614 | 0.362034 | 0.394173 |
| tossup | drop_share_3_d2 | 1240 | 0.323125 | 0.0297692 | 0.141812 | 0.2667 | 0.308391 | 0.328991 | 0.342888 | 0.359856 | 0.420346 |
| tossup | drop_share_1_d3 | 1240 | 0.324759 | 0.0199112 | 0.27326 | 0.296353 | 0.310481 | 0.322457 | 0.33824 | 0.360511 | 0.400521 |
| tossup | drop_share_2_d3 | 1240 | 0.345925 | 0.00973983 | 0.316877 | 0.330849 | 0.339286 | 0.345876 | 0.352392 | 0.36177 | 0.392127 |
| tossup | drop_share_3_d3 | 1240 | 0.329316 | 0.0201092 | 0.257946 | 0.294051 | 0.315656 | 0.331672 | 0.343632 | 0.359142 | 0.382661 |
| tossup | drop_share_1_d4 | 1240 | 0.334061 | 0.0402641 | 0.248432 | 0.297778 | 0.308628 | 0.321248 | 0.346986 | 0.418506 | 0.585279 |
| tossup | drop_share_2_d4 | 1240 | 0.341417 | 0.0167107 | 0.258652 | 0.31123 | 0.333861 | 0.343833 | 0.351342 | 0.361536 | 0.482868 |
| tossup | drop_share_3_d4 | 1240 | 0.324522 | 0.0332722 | 0.150204 | 0.256244 | 0.312174 | 0.333767 | 0.344976 | 0.359132 | 0.422658 |
| tossup | r_1 | 1240 | 0.438257 | 0.241982 | 0.0138635 | 0.0280182 | 0.318614 | 0.50987 | 0.609772 | 0.751492 | 0.861138 |
| tossup | r_2 | 1240 | 0.174084 | 0.130092 | 0.0311243 | 0.0432974 | 0.0680431 | 0.132906 | 0.251696 | 0.446452 | 0.634463 |
| tossup | r_3 | 1240 | 0.127108 | 0.0943593 | 0.0169139 | 0.0279886 | 0.0529248 | 0.0946999 | 0.183109 | 0.331978 | 0.465973 |
| tossup | r_4 | 1240 | 0.260551 | 0.282822 | 0.0205793 | 0.0313549 | 0.0544348 | 0.113461 | 0.359757 | 0.802164 | 0.901845 |
| tossup | r_norm | 1240 | 0.681512 | 0.078754 | 0.502137 | 0.564625 | 0.625187 | 0.669511 | 0.74084 | 0.823435 | 0.903663 |
