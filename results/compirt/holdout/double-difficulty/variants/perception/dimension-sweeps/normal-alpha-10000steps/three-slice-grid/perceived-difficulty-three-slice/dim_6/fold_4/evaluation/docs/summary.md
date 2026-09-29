# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_6/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_6/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 6 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 322001 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.661695 |
| log_loss | 0.507282 |
| ece | 0.0221173 |
| brier | 0.164587 |
| accuracy | 0.775944 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.002589 |
| probability_std | 0.131296 |
| probability_p10 | 0.579097 |
| probability_p50 | 0.783126 |
| probability_p90 | 0.909321 |
| mean_predictive_variance | 0.164571 |
| integrated_brier_score | 0.100886 |
| joint_tossup_event_log_loss | 6.94517 |
| buzz_position_mae | 0.159007 |
| buzz_position_median_absolute_error | 0.144411 |
| buzz_position_bias | -0.0608312 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.34822 |
| first_buzzer_mean_reciprocal_rank | 0.557207 |
| first_buzzer_log_loss | 1.71215 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.637864 |
| tossup_scorer_player_top1_accuracy | 0.314392 |
| tossup_scorer_team_top1_accuracy | 0.495309 |
| tossup_game_winner_accuracy | 0.800875 |
| tossup_game_margin_mae | 33.7513 |
| tournament_player_ppg_spearman | 0.70001 |
| tournament_player_ppg_mae | 9.04653 |
| tournament_player_ppg_top10_overlap | 0.67931 |
| neg_auroc | 0.661695 |
| neg_average_precision | 0.380979 |
| neg_precision | 0.528986 |
| neg_recall | 0.104236 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0562101 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.091796 |
| no_buzz_calibration_error | 0.0800689 |
| no_buzz_brier | 0.0250189 |
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
| tossup_correctness | aggregate | all | 9270 | 0.661695 | 0.507282 | 0.0221173 | 0.164587 | 0.775944 | 0.773355 | 0.002589 | 0.131296 | 0.579097 | 0.783126 | 0.909321 | 0.164571 |
| tossup_correctness | tier | fall | 2876 | 0.656805 | 0.483704 | 0.0173012 | 0.154923 | 0.793115 | 0.793115 | 0 | 0.121469 | 0.622969 | 0.8161 | 0.920775 | 0.15052 |
| tossup_correctness | tier | nationals | 1579 | 0.665299 | 0.554931 | 0.0546623 | 0.18576 | 0.737809 | 0.729576 | 0.00823306 | 0.129623 | 0.503765 | 0.686899 | 0.831464 | 0.202603 |
| tossup_correctness | tier | regionals | 1990 | 0.672395 | 0.511209 | 0.0283164 | 0.166399 | 0.771357 | 0.765829 | 0.00552764 | 0.12575 | 0.580312 | 0.766407 | 0.889532 | 0.172649 |
| tossup_correctness | tier | winter | 2825 | 0.652686 | 0.501886 | 0.0205207 | 0.161315 | 0.783009 | 0.783009 | 0 | 0.122896 | 0.617522 | 0.809713 | 0.924863 | 0.151927 |
| tossup_correctness | category | Current Events | 123 | 0.699193 | 0.518251 | 0.0865629 | 0.168816 | 0.772358 | 0.764228 | 0.00813008 | 0.133822 | 0.521836 | 0.693354 | 0.831896 | 0.197581 |
| tossup_correctness | category | Fine Arts | 1093 | 0.657683 | 0.511199 | 0.0235658 | 0.166217 | 0.776761 | 0.769442 | 0.0073193 | 0.120401 | 0.616782 | 0.802808 | 0.914334 | 0.157431 |
| tossup_correctness | category | Geography | 191 | 0.74602 | 0.538433 | 0.0674596 | 0.180279 | 0.732984 | 0.691099 | 0.0418848 | 0.15602 | 0.446675 | 0.711323 | 0.857574 | 0.192703 |
| tossup_correctness | category | History | 1469 | 0.68655 | 0.513346 | 0.0326301 | 0.168758 | 0.760381 | 0.758339 | 0.00204221 | 0.123588 | 0.562049 | 0.753873 | 0.879169 | 0.180036 |
| tossup_correctness | category | Literature | 1436 | 0.609355 | 0.48214 | 0.0537819 | 0.150543 | 0.812674 | 0.81546 | -0.00278552 | 0.115184 | 0.663392 | 0.863105 | 0.952653 | 0.126517 |
| tossup_correctness | category | Mythology | 325 | 0.622871 | 0.455529 | 0.098991 | 0.141913 | 0.818462 | 0.843077 | -0.0246154 | 0.122977 | 0.591848 | 0.773154 | 0.899335 | 0.17082 |
| tossup_correctness | category | Other Academic | 67 | 0.598383 | 0.547087 | 0.118524 | 0.180907 | 0.776119 | 0.791045 | -0.0149254 | 0.127196 | 0.501024 | 0.682437 | 0.823813 | 0.204058 |
| tossup_correctness | category | Philosophy | 322 | 0.609612 | 0.513459 | 0.0505741 | 0.166344 | 0.785714 | 0.785714 | 0 | 0.11355 | 0.639017 | 0.805571 | 0.92449 | 0.153341 |
| tossup_correctness | category | Popular Culture | 100 | 0.551583 | 0.428831 | 0.145835 | 0.129825 | 0.83 | 0.89 | -0.06 | 0.11458 | 0.603176 | 0.759425 | 0.882971 | 0.177255 |
| tossup_correctness | category | Religion | 365 | 0.645402 | 0.569674 | 0.0445882 | 0.193346 | 0.712329 | 0.723288 | -0.0109589 | 0.130024 | 0.556959 | 0.770471 | 0.892358 | 0.17273 |
| tossup_correctness | category | Science | 1456 | 0.675329 | 0.504553 | 0.0223853 | 0.164222 | 0.775412 | 0.76717 | 0.00824176 | 0.140321 | 0.55333 | 0.783304 | 0.905161 | 0.16638 |
| tossup_correctness | category | Social Science | 333 | 0.691312 | 0.534338 | 0.0277064 | 0.177668 | 0.741742 | 0.72973 | 0.012012 | 0.127946 | 0.562068 | 0.741628 | 0.875989 | 0.18343 |
| tossup_correctness | category | Unknown | 1990 | 0.672395 | 0.511209 | 0.0283164 | 0.166399 | 0.771357 | 0.765829 | 0.00552764 | 0.12575 | 0.580312 | 0.766407 | 0.889532 | 0.172649 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.642952 | 0.546033 | 0.083793 | 0.180658 | 0.75419 | 0.748603 | 0.00558659 | 0.131382 | 0.508991 | 0.69746 | 0.815112 | 0.202633 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.619025 | 0.549984 | 0.0556755 | 0.182625 | 0.743992 | 0.754441 | -0.0104493 | 0.132574 | 0.515236 | 0.734177 | 0.866066 | 0.186889 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.660137 | 0.51403 | 0.0206016 | 0.168047 | 0.768044 | 0.766682 | 0.00136178 | 0.127281 | 0.56864 | 0.768032 | 0.891866 | 0.17293 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.678379 | 0.481409 | 0.0190716 | 0.154778 | 0.795165 | 0.787441 | 0.0077233 | 0.125201 | 0.603024 | 0.796525 | 0.912837 | 0.159369 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.660715 | 0.512152 | 0.0262973 | 0.165078 | 0.774128 | 0.771758 | 0.00237047 | 0.132687 | 0.594612 | 0.805427 | 0.926892 | 0.15404 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | -0.665591 | 1.053 | -4.64174 | -3.30559 | -0.440836 | -0.241057 | -0.138199 | -0.00054036 | 0.226736 |
| player | theta_2 | 1196 | -0.991708 | 1.23926 | -5.04109 | -3.52131 | -2.06562 | -0.323921 | -0.159673 | 0.0303093 | 0.686621 |
| player | theta_3 | 1196 | -0.263257 | 0.285471 | -1.60021 | -0.778831 | -0.401152 | -0.240208 | -0.110689 | 0.144713 | 1.02201 |
| player | theta_4 | 1196 | -1.42594 | 1.32716 | -4.88961 | -3.59785 | -2.65094 | -0.861674 | -0.219872 | 0.0155037 | 1.16404 |
| player | theta_5 | 1196 | -0.322782 | 0.40167 | -1.8649 | -0.985952 | -0.553923 | -0.310962 | -0.133829 | 0.376194 | 1.95759 |
| player | theta_6 | 1196 | -1.28277 | 1.24014 | -5.02036 | -3.36091 | -2.47107 | -0.542414 | -0.225866 | -0.0362791 | 0.442275 |
| player | theta_norm | 1196 | 3.25074 | 0.945406 | 1.31146 | 1.92821 | 2.54039 | 3.1656 | 3.82675 | 5.03032 | 6.9306 |
| tossup | start_difficulty_d1 | 1240 | -0.968985 | 1.44942 | -4.23125 | -3.59968 | -2.65886 | -0.140478 | 0.0425834 | 0.218759 | 0.506264 |
| tossup | start_difficulty_d2 | 1240 | -0.990601 | 1.53487 | -4.83886 | -3.90555 | -2.74887 | -0.166095 | 0.0167451 | 0.174172 | 0.457663 |
| tossup | start_difficulty_d3 | 1240 | -0.00233649 | 0.202868 | -1.18986 | -0.398644 | -0.0806232 | 0.0353403 | 0.123492 | 0.245507 | 0.45585 |
| tossup | start_difficulty_d4 | 1240 | -1.00549 | 1.6263 | -6.13101 | -4.31314 | -0.927299 | -0.167364 | 0.0344344 | 0.20789 | 0.543659 |
| tossup | start_difficulty_d5 | 1240 | -0.0810283 | 0.468542 | -2.13428 | -1.18112 | -0.191139 | 0.0489072 | 0.203522 | 0.410898 | 0.91637 |
| tossup | start_difficulty_d6 | 1240 | -0.808116 | 1.56339 | -5.49732 | -4.19076 | -0.319189 | -0.0559473 | 0.0630483 | 0.232754 | 0.473127 |
| tossup | end_difficulty_d1 | 1240 | -2.05651 | 1.6375 | -7.53903 | -5.26263 | -3.56652 | -1.15036 | -0.93816 | -0.73628 | -0.430695 |
| tossup | end_difficulty_d2 | 1240 | -2.07072 | 1.73929 | -10.5709 | -5.43677 | -3.50561 | -1.1736 | -0.963578 | -0.781862 | -0.428686 |
| tossup | end_difficulty_d3 | 1240 | -0.998429 | 0.242168 | -2.60161 | -1.45929 | -1.08866 | -0.956576 | -0.844893 | -0.711944 | -0.415806 |
| tossup | end_difficulty_d4 | 1240 | -2.05506 | 1.75521 | -8.87285 | -5.63476 | -2.09711 | -1.17964 | -0.946525 | -0.736256 | -0.371201 |
| tossup | end_difficulty_d5 | 1240 | -1.09873 | 0.57597 | -3.53813 | -2.47217 | -1.21371 | -0.932894 | -0.753921 | -0.514693 | 0.0449532 |
| tossup | end_difficulty_d6 | 1240 | -1.82257 | 1.62576 | -8.53157 | -5.34877 | -1.36464 | -1.0543 | -0.910685 | -0.709434 | -0.454681 |
| tossup | total_drop_d1 | 1240 | 1.08753 | 0.321585 | 0.572138 | 0.870674 | 0.962684 | 1.00294 | 1.05931 | 1.63758 | 3.64053 |
| tossup | total_drop_d2 | 1240 | 1.08012 | 0.437716 | 0.508862 | 0.834951 | 0.960451 | 0.996013 | 1.04571 | 1.62326 | 6.68856 |
| tossup | total_drop_d3 | 1240 | 0.996093 | 0.0535835 | 0.866819 | 0.925134 | 0.960924 | 0.990466 | 1.02363 | 1.08106 | 1.41175 |
| tossup | total_drop_d4 | 1240 | 1.04957 | 0.324865 | 0.374441 | 0.773065 | 0.950206 | 0.995591 | 1.04998 | 1.45628 | 4.62968 |
| tossup | total_drop_d5 | 1240 | 1.0177 | 0.11858 | 0.83772 | 0.89942 | 0.950829 | 0.988 | 1.03969 | 1.25692 | 1.80934 |
| tossup | total_drop_d6 | 1240 | 1.01445 | 0.246866 | 0.529873 | 0.751511 | 0.950333 | 0.989774 | 1.02948 | 1.23039 | 4.46569 |
| tossup | drop_share_1_d1 | 1240 | 0.32879 | 0.0430977 | 0.260296 | 0.29002 | 0.301795 | 0.311346 | 0.342894 | 0.416313 | 0.575133 |
| tossup | drop_share_2_d1 | 1240 | 0.344322 | 0.0146221 | 0.264236 | 0.319403 | 0.336067 | 0.345085 | 0.353476 | 0.365434 | 0.421992 |
| tossup | drop_share_3_d1 | 1240 | 0.326888 | 0.0386962 | 0.155448 | 0.244983 | 0.321357 | 0.341532 | 0.351107 | 0.362642 | 0.380919 |
| tossup | drop_share_1_d2 | 1240 | 0.328994 | 0.0469469 | 0.220948 | 0.290423 | 0.302538 | 0.311846 | 0.330802 | 0.425891 | 0.664571 |
| tossup | drop_share_2_d2 | 1240 | 0.342655 | 0.0163762 | 0.210066 | 0.316377 | 0.334729 | 0.344031 | 0.352367 | 0.36406 | 0.429271 |
| tossup | drop_share_3_d2 | 1240 | 0.328351 | 0.0393263 | 0.122859 | 0.240408 | 0.32574 | 0.341814 | 0.351019 | 0.362638 | 0.418518 |
| tossup | drop_share_1_d3 | 1240 | 0.306278 | 0.0105876 | 0.276244 | 0.288626 | 0.299323 | 0.305872 | 0.313532 | 0.32408 | 0.339001 |
| tossup | drop_share_2_d3 | 1240 | 0.347142 | 0.0106286 | 0.308979 | 0.329342 | 0.340066 | 0.3472 | 0.354053 | 0.364523 | 0.381484 |
| tossup | drop_share_3_d3 | 1240 | 0.34658 | 0.0114306 | 0.308424 | 0.327754 | 0.338983 | 0.346892 | 0.354352 | 0.3649 | 0.381718 |
| tossup | drop_share_1_d4 | 1240 | 0.327565 | 0.0510752 | 0.225503 | 0.290996 | 0.301701 | 0.311164 | 0.324393 | 0.434347 | 0.674634 |
| tossup | drop_share_2_d4 | 1240 | 0.341638 | 0.0198121 | 0.20918 | 0.30556 | 0.334174 | 0.343767 | 0.353292 | 0.365252 | 0.503472 |
| tossup | drop_share_3_d4 | 1240 | 0.330797 | 0.0412284 | 0.116186 | 0.234917 | 0.329624 | 0.34228 | 0.352141 | 0.364893 | 0.450181 |
| tossup | drop_share_1_d5 | 1240 | 0.307411 | 0.0132713 | 0.273001 | 0.288768 | 0.29853 | 0.306143 | 0.314726 | 0.33189 | 0.370994 |
| tossup | drop_share_2_d5 | 1240 | 0.347795 | 0.0109085 | 0.308169 | 0.330102 | 0.340231 | 0.347874 | 0.355684 | 0.365091 | 0.382906 |
| tossup | drop_share_3_d5 | 1240 | 0.344794 | 0.0142849 | 0.269259 | 0.320593 | 0.33729 | 0.345797 | 0.354141 | 0.365704 | 0.382213 |
| tossup | drop_share_1_d6 | 1240 | 0.318911 | 0.0396465 | 0.221637 | 0.287119 | 0.300321 | 0.309384 | 0.319634 | 0.399469 | 0.608034 |
| tossup | drop_share_2_d6 | 1240 | 0.343154 | 0.0188541 | 0.245814 | 0.307697 | 0.335403 | 0.344273 | 0.353644 | 0.366746 | 0.509528 |
| tossup | drop_share_3_d6 | 1240 | 0.337934 | 0.0346163 | 0.146151 | 0.26029 | 0.334797 | 0.344866 | 0.353675 | 0.368141 | 0.452678 |
| tossup | r_1 | 1240 | 0.210276 | 0.269264 | 0.00997361 | 0.0201764 | 0.0318473 | 0.044336 | 0.5567 | 0.69362 | 0.80227 |
| tossup | r_2 | 1240 | 0.22268 | 0.29144 | 0.0114827 | 0.0218028 | 0.0348727 | 0.0616179 | 0.586477 | 0.766013 | 0.887146 |
| tossup | r_3 | 1240 | 0.0503996 | 0.0297881 | 0.00925407 | 0.0185786 | 0.0301337 | 0.0440429 | 0.0602957 | 0.114556 | 0.260835 |
| tossup | r_4 | 1240 | 0.240405 | 0.31313 | 0.0151956 | 0.0276884 | 0.0465934 | 0.0671117 | 0.18842 | 0.847261 | 0.946933 |
| tossup | r_5 | 1240 | 0.0629667 | 0.0371648 | 0.0101441 | 0.0213133 | 0.0384071 | 0.0551935 | 0.0735969 | 0.142855 | 0.234957 |
| tossup | r_6 | 1240 | 0.213273 | 0.296139 | 0.0122121 | 0.0298969 | 0.0496324 | 0.0685976 | 0.106456 | 0.852121 | 0.938959 |
| tossup | r_norm | 1240 | 0.735637 | 0.087232 | 0.512777 | 0.602456 | 0.669129 | 0.735791 | 0.801268 | 0.881852 | 0.947234 |
