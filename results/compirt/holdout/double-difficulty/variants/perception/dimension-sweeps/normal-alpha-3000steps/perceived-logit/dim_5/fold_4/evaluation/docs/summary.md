# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_5/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_5/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 335824 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.553633 |
| log_loss | 0.573001 |
| ece | 0.0806123 |
| brier | 0.181946 |
| accuracy | 0.773031 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.000323625 |
| probability_std | 0.107555 |
| probability_p10 | 0.677108 |
| probability_p50 | 0.868294 |
| probability_p90 | 0.94181 |
| mean_predictive_variance | 0.125674 |
| integrated_brier_score | 0.173329 |
| joint_tossup_event_log_loss | 7.72993 |
| buzz_position_mae | 0.334384 |
| buzz_position_median_absolute_error | 0.33599 |
| buzz_position_bias | -0.320895 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.348759 |
| first_buzzer_mean_reciprocal_rank | 0.559539 |
| first_buzzer_log_loss | 1.68794 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.624703 |
| tossup_scorer_player_top1_accuracy | 0.258209 |
| tossup_scorer_team_top1_accuracy | 0.400959 |
| tossup_game_winner_accuracy | 0.700219 |
| tossup_game_margin_mae | 45.6982 |
| tournament_player_ppg_spearman | 0.594533 |
| tournament_player_ppg_mae | 10.8177 |
| tournament_player_ppg_top10_overlap | 0.610345 |
| neg_auroc | 0.553633 |
| neg_average_precision | 0.279233 |
| neg_precision | 0.481013 |
| neg_recall | 0.0180866 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0310736 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.227207 |
| no_buzz_calibration_error | 0.21548 |
| no_buzz_brier | 0.0679452 |
| full_pmf_max_mass_error | 1.11022e-15 |
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
| tossup_correctness | aggregate | all | 9270 | 0.553633 | 0.573001 | 0.0806123 | 0.181946 | 0.773031 | 0.773355 | -0.000323625 | 0.107555 | 0.677108 | 0.868294 | 0.94181 | 0.125674 |
| tossup_correctness | tier | fall | 2876 | 0.535535 | 0.544629 | 0.0808684 | 0.17031 | 0.793463 | 0.793115 | 0.000347705 | 0.0850984 | 0.733007 | 0.879448 | 0.937914 | 0.116548 |
| tossup_correctness | tier | nationals | 1579 | 0.583368 | 0.602013 | 0.0723239 | 0.199309 | 0.730209 | 0.729576 | 0.000633312 | 0.132152 | 0.580407 | 0.786642 | 0.926682 | 0.162067 |
| tossup_correctness | tier | regionals | 1990 | 0.536174 | 0.590956 | 0.0899834 | 0.189151 | 0.762814 | 0.765829 | -0.00301508 | 0.117397 | 0.642292 | 0.841235 | 0.941027 | 0.137144 |
| tossup_correctness | tier | winter | 2825 | 0.545381 | 0.573022 | 0.0933996 | 0.17901 | 0.783363 | 0.783009 | 0.000353982 | 0.0804822 | 0.750517 | 0.892801 | 0.948424 | 0.106543 |
| tossup_correctness | category | Current Events | 123 | 0.622157 | 0.543765 | 0.0995783 | 0.177314 | 0.756098 | 0.764228 | -0.00813008 | 0.129351 | 0.609676 | 0.852963 | 0.932898 | 0.137291 |
| tossup_correctness | category | Fine Arts | 1093 | 0.552847 | 0.59021 | 0.106307 | 0.186423 | 0.769442 | 0.769442 | 0 | 0.0981459 | 0.712046 | 0.889018 | 0.945542 | 0.113635 |
| tossup_correctness | category | Geography | 191 | 0.65511 | 0.652799 | 0.142996 | 0.221896 | 0.691099 | 0.691099 | 0 | 0.104615 | 0.678294 | 0.858202 | 0.926092 | 0.131722 |
| tossup_correctness | category | History | 1469 | 0.559442 | 0.586521 | 0.0877075 | 0.189152 | 0.760381 | 0.758339 | 0.00204221 | 0.101398 | 0.683264 | 0.857085 | 0.931586 | 0.131266 |
| tossup_correctness | category | Literature | 1436 | 0.522936 | 0.519784 | 0.0787489 | 0.157405 | 0.81337 | 0.81546 | -0.00208914 | 0.094096 | 0.727143 | 0.896154 | 0.952061 | 0.107125 |
| tossup_correctness | category | Mythology | 325 | 0.601188 | 0.4363 | 0.0554878 | 0.132683 | 0.836923 | 0.843077 | -0.00615385 | 0.0976657 | 0.726811 | 0.891668 | 0.93967 | 0.111848 |
| tossup_correctness | category | Other Academic | 67 | 0.572776 | 0.516496 | 0.0914108 | 0.162333 | 0.791045 | 0.791045 | 0 | 0.125205 | 0.635936 | 0.835192 | 0.92439 | 0.143208 |
| tossup_correctness | category | Philosophy | 322 | 0.469897 | 0.602676 | 0.114188 | 0.185909 | 0.785714 | 0.785714 | 0 | 0.103539 | 0.704326 | 0.897013 | 0.948597 | 0.112252 |
| tossup_correctness | category | Popular Culture | 100 | 0.588355 | 0.363559 | 0.0506209 | 0.104994 | 0.89 | 0.89 | 0 | 0.0849627 | 0.742766 | 0.87579 | 0.921567 | 0.119798 |
| tossup_correctness | category | Religion | 365 | 0.588809 | 0.6608 | 0.137673 | 0.215239 | 0.723288 | 0.723288 | 0 | 0.105933 | 0.693514 | 0.892073 | 0.93949 | 0.115024 |
| tossup_correctness | category | Science | 1456 | 0.56719 | 0.565367 | 0.0646132 | 0.181188 | 0.770604 | 0.76717 | 0.00343407 | 0.108552 | 0.660575 | 0.846001 | 0.932269 | 0.13748 |
| tossup_correctness | category | Social Science | 333 | 0.514449 | 0.660232 | 0.128425 | 0.215143 | 0.732733 | 0.72973 | 0.003003 | 0.108696 | 0.671467 | 0.864132 | 0.932261 | 0.128961 |
| tossup_correctness | category | Unknown | 1990 | 0.536174 | 0.590956 | 0.0899834 | 0.189151 | 0.762814 | 0.765829 | -0.00301508 | 0.117397 | 0.642292 | 0.841235 | 0.941027 | 0.137144 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.533167 | 0.590285 | 0.0870363 | 0.190017 | 0.77095 | 0.748603 | 0.0223464 | 0.109023 | 0.678549 | 0.829817 | 0.909743 | 0.146562 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.49054 | 0.610805 | 0.106465 | 0.198201 | 0.751306 | 0.754441 | -0.0031348 | 0.110538 | 0.64857 | 0.836809 | 0.918275 | 0.143467 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.544133 | 0.577889 | 0.0814593 | 0.186356 | 0.765774 | 0.766682 | -0.000907853 | 0.101064 | 0.686866 | 0.854498 | 0.929995 | 0.13271 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.572336 | 0.539205 | 0.0649489 | 0.169967 | 0.787441 | 0.787441 | 0 | 0.104139 | 0.68835 | 0.875202 | 0.940099 | 0.122859 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.556877 | 0.590139 | 0.0945173 | 0.184978 | 0.77108 | 0.771758 | -0.000677277 | 0.111833 | 0.672424 | 0.890219 | 0.952536 | 0.11623 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1196 | -1.20532 | 0.900828 | -3.36708 | -2.40271 | -1.76853 | -1.34794 | -0.854127 | 0.769527 | 2.19486 |
| player | beta | 1196 | -3.78433 | 1.24091 | -7.26269 | -6.35918 | -4.48903 | -3.49394 | -2.82354 | -2.29115 | -1.88932 |
| player | theta_1 | 1196 | 0.803739 | 1.01941 | -2.46736 | -1.07055 | 0.100651 | 1.01126 | 1.56207 | 2.20216 | 3.25642 |
| player | theta_2 | 1196 | 0.749823 | 0.915636 | -2.44901 | -0.977829 | 0.2247 | 0.89871 | 1.38176 | 2.02059 | 3.24907 |
| player | theta_3 | 1196 | 0.744859 | 0.817144 | -2.03072 | -0.77607 | 0.209618 | 0.879877 | 1.3432 | 1.87042 | 2.41877 |
| player | theta_4 | 1196 | 0.635618 | 0.625668 | -1.63471 | -0.574343 | 0.331292 | 0.73558 | 1.02817 | 1.47532 | 3.07017 |
| player | theta_5 | 1196 | 0.68508 | 0.762026 | -2.31404 | -0.767083 | 0.24172 | 0.81062 | 1.1837 | 1.83193 | 2.55657 |
| player | theta_norm | 1196 | 2.37521 | 0.713936 | 0.288996 | 1.12317 | 1.95742 | 2.41577 | 2.82288 | 3.48907 | 5.0766 |
| tossup | start_difficulty_d1 | 1240 | -0.834972 | 0.405221 | -2.07266 | -1.5742 | -1.13387 | -0.780507 | -0.517019 | -0.263353 | 0.0226288 |
| tossup | start_difficulty_d2 | 1240 | -0.813845 | 0.43902 | -2.02527 | -1.62996 | -1.09223 | -0.757471 | -0.489516 | -0.193852 | 0.0748842 |
| tossup | start_difficulty_d3 | 1240 | -0.770805 | 0.416198 | -2.30094 | -1.58993 | -1.01047 | -0.698948 | -0.475487 | -0.225965 | 0.0068136 |
| tossup | start_difficulty_d4 | 1240 | -0.696311 | 0.294901 | -1.88123 | -1.16554 | -0.886678 | -0.686442 | -0.490932 | -0.229092 | 0.0264368 |
| tossup | start_difficulty_d5 | 1240 | -0.72541 | 0.36547 | -2.13505 | -1.38955 | -0.970178 | -0.653723 | -0.45687 | -0.225624 | 0.00420842 |
| tossup | end_difficulty_d1 | 1240 | -1.63611 | 0.335469 | -2.91834 | -2.23053 | -1.87542 | -1.61946 | -1.38342 | -1.12267 | -0.872742 |
| tossup | end_difficulty_d2 | 1240 | -1.63475 | 0.399248 | -3.15544 | -2.32322 | -1.89961 | -1.6196 | -1.32703 | -1.05333 | -0.737537 |
| tossup | end_difficulty_d3 | 1240 | -1.60179 | 0.368817 | -2.86509 | -2.29255 | -1.82684 | -1.56723 | -1.32396 | -1.07312 | -0.826455 |
| tossup | end_difficulty_d4 | 1240 | -1.55777 | 0.305798 | -2.51912 | -2.10119 | -1.76112 | -1.54615 | -1.33912 | -1.08181 | -0.731783 |
| tossup | end_difficulty_d5 | 1240 | -1.57322 | 0.339045 | -2.70656 | -2.1712 | -1.80491 | -1.54453 | -1.30466 | -1.07385 | -0.765623 |
| tossup | total_drop_d1 | 1240 | 0.801134 | 0.216959 | 0.252107 | 0.39882 | 0.657715 | 0.818352 | 0.958423 | 1.12814 | 1.36104 |
| tossup | total_drop_d2 | 1240 | 0.820903 | 0.194834 | 0.286795 | 0.460353 | 0.713052 | 0.825644 | 0.938283 | 1.13341 | 1.55161 |
| tossup | total_drop_d3 | 1240 | 0.830986 | 0.190235 | 0.330283 | 0.470161 | 0.731843 | 0.838196 | 0.950601 | 1.13 | 1.42386 |
| tossup | total_drop_d4 | 1240 | 0.86146 | 0.153011 | 0.276247 | 0.642181 | 0.760094 | 0.843989 | 0.954287 | 1.13464 | 1.4684 |
| tossup | total_drop_d5 | 1240 | 0.84781 | 0.17268 | 0.299792 | 0.53179 | 0.753197 | 0.84686 | 0.954271 | 1.12781 | 1.36625 |
| tossup | drop_share_1_d1 | 1240 | 0.31658 | 0.0215669 | 0.235004 | 0.284236 | 0.304002 | 0.314539 | 0.327495 | 0.352147 | 0.414019 |
| tossup | drop_share_2_d1 | 1240 | 0.330893 | 0.0179159 | 0.252264 | 0.295906 | 0.320423 | 0.334071 | 0.343261 | 0.355502 | 0.37419 |
| tossup | drop_share_3_d1 | 1240 | 0.352527 | 0.0258476 | 0.267039 | 0.317462 | 0.337004 | 0.349553 | 0.362355 | 0.405426 | 0.479431 |
| tossup | drop_share_1_d2 | 1240 | 0.315547 | 0.0204679 | 0.239602 | 0.285567 | 0.303127 | 0.314388 | 0.32658 | 0.350806 | 0.417445 |
| tossup | drop_share_2_d2 | 1240 | 0.332604 | 0.0154078 | 0.26709 | 0.303645 | 0.324305 | 0.334538 | 0.343309 | 0.353942 | 0.371111 |
| tossup | drop_share_3_d2 | 1240 | 0.351849 | 0.02253 | 0.277194 | 0.320414 | 0.337555 | 0.350264 | 0.363178 | 0.391185 | 0.464279 |
| tossup | drop_share_1_d3 | 1240 | 0.316359 | 0.0200146 | 0.209057 | 0.288939 | 0.304079 | 0.315252 | 0.327236 | 0.348567 | 0.407135 |
| tossup | drop_share_2_d3 | 1240 | 0.333141 | 0.0159187 | 0.269027 | 0.302865 | 0.324506 | 0.335582 | 0.343633 | 0.355087 | 0.378977 |
| tossup | drop_share_3_d3 | 1240 | 0.3505 | 0.0234455 | 0.288502 | 0.319345 | 0.33663 | 0.348015 | 0.359839 | 0.39223 | 0.469966 |
| tossup | drop_share_1_d4 | 1240 | 0.314032 | 0.015939 | 0.232015 | 0.288825 | 0.30396 | 0.314021 | 0.324675 | 0.340095 | 0.402907 |
| tossup | drop_share_2_d4 | 1240 | 0.335513 | 0.0130785 | 0.276611 | 0.313055 | 0.327864 | 0.335747 | 0.344152 | 0.356546 | 0.377066 |
| tossup | drop_share_3_d4 | 1240 | 0.350454 | 0.018825 | 0.269704 | 0.324006 | 0.337694 | 0.348655 | 0.360244 | 0.383649 | 0.474044 |
| tossup | drop_share_1_d5 | 1240 | 0.316211 | 0.0186828 | 0.22798 | 0.289715 | 0.304746 | 0.314705 | 0.326431 | 0.350264 | 0.422202 |
| tossup | drop_share_2_d5 | 1240 | 0.334341 | 0.0137024 | 0.278338 | 0.310869 | 0.32677 | 0.335074 | 0.343405 | 0.354885 | 0.374375 |
| tossup | drop_share_3_d5 | 1240 | 0.349448 | 0.0193025 | 0.255537 | 0.318329 | 0.337643 | 0.349141 | 0.360168 | 0.380588 | 0.459164 |
| tossup | r_1 | 1240 | 0.23324 | 0.18734 | 0.0344297 | 0.0640738 | 0.108797 | 0.156674 | 0.291133 | 0.68985 | 0.839095 |
| tossup | r_2 | 1240 | 0.21589 | 0.147485 | 0.0346287 | 0.0598487 | 0.113469 | 0.176242 | 0.265674 | 0.566489 | 0.815335 |
| tossup | r_3 | 1240 | 0.196834 | 0.128218 | 0.0345144 | 0.0616787 | 0.117746 | 0.17584 | 0.214337 | 0.503845 | 0.817105 |
| tossup | r_4 | 1240 | 0.167742 | 0.0724968 | 0.0435106 | 0.0639054 | 0.107828 | 0.171905 | 0.21876 | 0.260679 | 0.721428 |
| tossup | r_5 | 1240 | 0.186294 | 0.102347 | 0.0358009 | 0.0602122 | 0.117461 | 0.183066 | 0.222218 | 0.394547 | 0.77025 |
| tossup | r_norm | 1240 | 0.531992 | 0.0923775 | 0.44774 | 0.450729 | 0.460096 | 0.49202 | 0.57623 | 0.735231 | 0.842953 |
