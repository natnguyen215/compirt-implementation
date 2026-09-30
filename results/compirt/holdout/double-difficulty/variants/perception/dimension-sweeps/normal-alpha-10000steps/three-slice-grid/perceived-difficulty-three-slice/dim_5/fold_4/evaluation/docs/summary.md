# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_5/fold_4/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-10000steps/three-slice-grid/perceived-difficulty-three-slice/dim_5/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 10000 |
| pyramidal | final_loss | 316030 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.668406 |
| log_loss | 0.504451 |
| ece | 0.0281993 |
| brier | 0.163332 |
| accuracy | 0.777994 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | 0.00463862 |
| probability_std | 0.130272 |
| probability_p10 | 0.579438 |
| probability_p50 | 0.777938 |
| probability_p90 | 0.907635 |
| mean_predictive_variance | 0.167047 |
| integrated_brier_score | 0.100427 |
| joint_tossup_event_log_loss | 6.88307 |
| buzz_position_mae | 0.159432 |
| buzz_position_median_absolute_error | 0.147624 |
| buzz_position_bias | -0.0634688 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.352859 |
| first_buzzer_mean_reciprocal_rank | 0.561911 |
| first_buzzer_log_loss | 1.6887 |
| first_buzzer_events | 9270 |
| first_buzzer_team_top1_accuracy | 0.638296 |
| tossup_scorer_player_top1_accuracy | 0.316205 |
| tossup_scorer_team_top1_accuracy | 0.502878 |
| tossup_game_winner_accuracy | 0.805252 |
| tossup_game_margin_mae | 34.8366 |
| tournament_player_ppg_spearman | 0.695679 |
| tournament_player_ppg_mae | 9.15292 |
| tournament_player_ppg_top10_overlap | 0.672414 |
| neg_auroc | 0.668406 |
| neg_average_precision | 0.392671 |
| neg_precision | 0.549884 |
| neg_recall | 0.112803 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.0551391 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.0875559 |
| no_buzz_calibration_error | 0.0758288 |
| no_buzz_brier | 0.0235634 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| tossup_correctness | aggregate | all | 9270 | 0.668406 | 0.504451 | 0.0281993 | 0.163332 | 0.777994 | 0.773355 | 0.00463862 | 0.130272 | 0.579438 | 0.777938 | 0.907635 | 0.167047 |
| tossup_correctness | tier | fall | 2876 | 0.656055 | 0.484395 | 0.0266698 | 0.155098 | 0.794506 | 0.793115 | 0.00139082 | 0.123289 | 0.605557 | 0.803657 | 0.912302 | 0.157487 |
| tossup_correctness | tier | nationals | 1579 | 0.681117 | 0.544221 | 0.0352272 | 0.181256 | 0.740975 | 0.729576 | 0.0113996 | 0.136583 | 0.500872 | 0.715346 | 0.860051 | 0.19195 |
| tossup_correctness | tier | regionals | 1990 | 0.690772 | 0.506943 | 0.0444828 | 0.165103 | 0.772864 | 0.765829 | 0.00703518 | 0.120609 | 0.559652 | 0.742401 | 0.861898 | 0.185327 |
| tossup_correctness | tier | winter | 2825 | 0.654754 | 0.500886 | 0.0299337 | 0.160448 | 0.785487 | 0.783009 | 0.00247788 | 0.123427 | 0.621197 | 0.813865 | 0.928559 | 0.149983 |
| tossup_correctness | category | Current Events | 123 | 0.73661 | 0.506383 | 0.0982867 | 0.163971 | 0.788618 | 0.764228 | 0.0243902 | 0.137913 | 0.496099 | 0.710718 | 0.828212 | 0.199394 |
| tossup_correctness | category | Fine Arts | 1093 | 0.667978 | 0.507362 | 0.0267796 | 0.16448 | 0.778591 | 0.769442 | 0.00914913 | 0.115968 | 0.614892 | 0.791352 | 0.909462 | 0.161147 |
| tossup_correctness | category | Geography | 191 | 0.764766 | 0.525401 | 0.0750472 | 0.173704 | 0.759162 | 0.691099 | 0.0680628 | 0.163896 | 0.431107 | 0.703917 | 0.851842 | 0.194518 |
| tossup_correctness | category | History | 1469 | 0.689648 | 0.511002 | 0.0192277 | 0.167712 | 0.761062 | 0.758339 | 0.00272294 | 0.125648 | 0.561699 | 0.765949 | 0.884656 | 0.175055 |
| tossup_correctness | category | Literature | 1436 | 0.612423 | 0.483224 | 0.0530856 | 0.150552 | 0.812674 | 0.81546 | -0.00278552 | 0.113699 | 0.663629 | 0.864694 | 0.954412 | 0.124091 |
| tossup_correctness | category | Mythology | 325 | 0.643409 | 0.447746 | 0.095187 | 0.139053 | 0.821538 | 0.843077 | -0.0215385 | 0.120773 | 0.588193 | 0.773038 | 0.896726 | 0.171984 |
| tossup_correctness | category | Other Academic | 67 | 0.641509 | 0.526015 | 0.120401 | 0.172178 | 0.791045 | 0.791045 | 0 | 0.128496 | 0.488883 | 0.707426 | 0.841175 | 0.199294 |
| tossup_correctness | category | Philosophy | 322 | 0.605316 | 0.513911 | 0.0488153 | 0.166757 | 0.782609 | 0.785714 | -0.00310559 | 0.107957 | 0.652772 | 0.806356 | 0.922148 | 0.152659 |
| tossup_correctness | category | Popular Culture | 100 | 0.526047 | 0.427427 | 0.157712 | 0.128114 | 0.88 | 0.89 | -0.01 | 0.104821 | 0.593357 | 0.765547 | 0.878993 | 0.178067 |
| tossup_correctness | category | Religion | 365 | 0.656466 | 0.565231 | 0.0448649 | 0.191437 | 0.709589 | 0.723288 | -0.0136986 | 0.130203 | 0.551133 | 0.766833 | 0.891048 | 0.174624 |
| tossup_correctness | category | Science | 1456 | 0.677275 | 0.503153 | 0.0273274 | 0.163258 | 0.777473 | 0.76717 | 0.0103022 | 0.135493 | 0.558029 | 0.779029 | 0.899192 | 0.168393 |
| tossup_correctness | category | Social Science | 333 | 0.693919 | 0.533967 | 0.0309482 | 0.177273 | 0.735736 | 0.72973 | 0.00600601 | 0.128147 | 0.555495 | 0.737736 | 0.870579 | 0.184482 |
| tossup_correctness | category | Unknown | 1990 | 0.690772 | 0.506943 | 0.0444828 | 0.165103 | 0.772864 | 0.765829 | 0.00703518 | 0.120609 | 0.559652 | 0.742401 | 0.861898 | 0.185327 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.643449 | 0.548591 | 0.0940347 | 0.181845 | 0.748603 | 0.748603 | 0 | 0.131086 | 0.501455 | 0.686017 | 0.812747 | 0.204261 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.625308 | 0.547812 | 0.0615617 | 0.181823 | 0.745037 | 0.754441 | -0.00940439 | 0.131631 | 0.517952 | 0.725253 | 0.864322 | 0.18985 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.657157 | 0.515155 | 0.0318452 | 0.168205 | 0.772583 | 0.766682 | 0.00590104 | 0.126971 | 0.565525 | 0.759869 | 0.88713 | 0.175506 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.691304 | 0.476281 | 0.0295912 | 0.152436 | 0.797179 | 0.787441 | 0.00973808 | 0.123489 | 0.602367 | 0.788535 | 0.908484 | 0.162631 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.670141 | 0.508147 | 0.025165 | 0.16357 | 0.775144 | 0.771758 | 0.00338639 | 0.131064 | 0.601161 | 0.800273 | 0.92515 | 0.155543 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | theta_1 | 1196 | -1.21204 | 1.38816 | -4.70611 | -3.68365 | -2.62869 | -0.302183 | -0.161064 | -0.00561857 | 0.592632 |
| player | theta_2 | 1196 | -2.16712 | 1.1811 | -4.94239 | -3.74811 | -3.02798 | -2.45253 | -1.53104 | -0.170227 | 1.53162 |
| player | theta_3 | 1196 | -0.22848 | 0.278199 | -1.10951 | -0.675883 | -0.383723 | -0.228529 | -0.0915755 | 0.228417 | 0.976692 |
| player | theta_4 | 1196 | -0.263985 | 0.419192 | -2.27732 | -0.999434 | -0.474566 | -0.242802 | -0.0741273 | 0.427577 | 2.12485 |
| player | theta_5 | 1196 | -0.302772 | 0.42822 | -1.9325 | -0.983215 | -0.544341 | -0.297975 | -0.114001 | 0.410504 | 1.76311 |
| player | theta_norm | 1196 | 3.0853 | 0.784727 | 1.39469 | 1.95829 | 2.52205 | 3.0321 | 3.5738 | 4.49121 | 5.92797 |
| tossup | start_difficulty_d1 | 1240 | -1.81371 | 1.6367 | -4.54088 | -3.8654 | -3.32554 | -2.5969 | -0.055063 | 0.174186 | 0.533334 |
| tossup | start_difficulty_d2 | 1240 | -1.7511 | 1.88814 | -5.93811 | -4.50226 | -3.66505 | -0.489957 | 0.00116597 | 0.194718 | 0.555911 |
| tossup | start_difficulty_d3 | 1240 | 0.017261 | 0.221748 | -1.47328 | -0.381334 | -0.06468 | 0.0457703 | 0.138282 | 0.2948 | 0.694944 |
| tossup | start_difficulty_d4 | 1240 | -0.0429741 | 0.385632 | -1.64652 | -0.874679 | -0.209351 | 0.0523914 | 0.208348 | 0.44855 | 0.747291 |
| tossup | start_difficulty_d5 | 1240 | -0.0788285 | 0.53152 | -2.20517 | -1.27845 | -0.23184 | 0.0631265 | 0.239894 | 0.511135 | 1.64871 |
| tossup | end_difficulty_d1 | 1240 | -2.96894 | 1.86588 | -9.74986 | -5.62063 | -4.5607 | -3.49883 | -1.04129 | -0.78912 | -0.422259 |
| tossup | end_difficulty_d2 | 1240 | -2.81959 | 2.02766 | -9.37818 | -6.06915 | -4.70132 | -1.54464 | -0.989923 | -0.752489 | -0.324141 |
| tossup | end_difficulty_d3 | 1240 | -0.975189 | 0.260695 | -2.60238 | -1.43493 | -1.07935 | -0.942975 | -0.830232 | -0.636557 | -0.167216 |
| tossup | end_difficulty_d4 | 1240 | -1.05049 | 0.466158 | -3.18482 | -2.04727 | -1.2408 | -0.931109 | -0.751771 | -0.468504 | -0.102747 |
| tossup | end_difficulty_d5 | 1240 | -1.09651 | 0.656768 | -3.83592 | -2.57788 | -1.25008 | -0.912879 | -0.700059 | -0.394806 | 0.791926 |
| tossup | total_drop_d1 | 1240 | 1.15523 | 0.475064 | 0.498335 | 0.782018 | 0.95239 | 1.0076 | 1.17464 | 1.9646 | 5.62413 |
| tossup | total_drop_d2 | 1240 | 1.06849 | 0.431089 | 0.358278 | 0.667645 | 0.923703 | 0.987123 | 1.06417 | 1.89574 | 5.14464 |
| tossup | total_drop_d3 | 1240 | 0.99245 | 0.0525901 | 0.849223 | 0.914623 | 0.957633 | 0.98848 | 1.02033 | 1.08249 | 1.38915 |
| tossup | total_drop_d4 | 1240 | 1.00752 | 0.0915904 | 0.813161 | 0.896542 | 0.949122 | 0.989231 | 1.04288 | 1.18013 | 1.65513 |
| tossup | total_drop_d5 | 1240 | 1.01768 | 0.140449 | 0.771763 | 0.881022 | 0.940059 | 0.98149 | 1.04078 | 1.31817 | 2.44617 |
| tossup | drop_share_1_d1 | 1240 | 0.347404 | 0.0509373 | 0.225008 | 0.29251 | 0.306042 | 0.329564 | 0.383486 | 0.435656 | 0.656173 |
| tossup | drop_share_2_d1 | 1240 | 0.341125 | 0.0177308 | 0.225329 | 0.314049 | 0.331724 | 0.341622 | 0.351497 | 0.365059 | 0.443766 |
| tossup | drop_share_3_d1 | 1240 | 0.311471 | 0.045275 | 0.118499 | 0.227904 | 0.278209 | 0.328991 | 0.346692 | 0.362951 | 0.427638 |
| tossup | drop_share_1_d2 | 1240 | 0.337119 | 0.0588021 | 0.213616 | 0.284917 | 0.30284 | 0.314674 | 0.358346 | 0.463357 | 0.664139 |
| tossup | drop_share_2_d2 | 1240 | 0.339075 | 0.0241481 | 0.223537 | 0.298686 | 0.327521 | 0.341588 | 0.351758 | 0.369151 | 0.513496 |
| tossup | drop_share_3_d2 | 1240 | 0.323806 | 0.0498564 | 0.112324 | 0.213514 | 0.310239 | 0.340123 | 0.352337 | 0.376507 | 0.448867 |
| tossup | drop_share_1_d3 | 1240 | 0.305157 | 0.0112067 | 0.270051 | 0.286789 | 0.297614 | 0.30496 | 0.312393 | 0.324133 | 0.341441 |
| tossup | drop_share_2_d3 | 1240 | 0.346982 | 0.0109639 | 0.307627 | 0.329456 | 0.339385 | 0.34686 | 0.354437 | 0.364563 | 0.386236 |
| tossup | drop_share_3_d3 | 1240 | 0.347862 | 0.0116191 | 0.30216 | 0.327902 | 0.340964 | 0.347858 | 0.355325 | 0.367234 | 0.381588 |
| tossup | drop_share_1_d4 | 1240 | 0.3066 | 0.0119238 | 0.272129 | 0.288979 | 0.297816 | 0.306059 | 0.31403 | 0.327598 | 0.347985 |
| tossup | drop_share_2_d4 | 1240 | 0.347695 | 0.0104124 | 0.318982 | 0.330136 | 0.340922 | 0.347333 | 0.354519 | 0.365228 | 0.383085 |
| tossup | drop_share_3_d4 | 1240 | 0.345706 | 0.0128727 | 0.289572 | 0.323945 | 0.337744 | 0.346429 | 0.354636 | 0.365177 | 0.380614 |
| tossup | drop_share_1_d5 | 1240 | 0.307857 | 0.0137594 | 0.254785 | 0.288174 | 0.298896 | 0.306402 | 0.315299 | 0.332545 | 0.366698 |
| tossup | drop_share_2_d5 | 1240 | 0.34722 | 0.0113245 | 0.31073 | 0.329138 | 0.338986 | 0.347223 | 0.355146 | 0.365649 | 0.38345 |
| tossup | drop_share_3_d5 | 1240 | 0.344923 | 0.0149836 | 0.271899 | 0.318157 | 0.336922 | 0.346208 | 0.355049 | 0.366714 | 0.398146 |
| tossup | r_1 | 1240 | 0.402967 | 0.334911 | 0.00941753 | 0.0230336 | 0.0369451 | 0.58649 | 0.715845 | 0.803874 | 0.877397 |
| tossup | r_2 | 1240 | 0.396386 | 0.361261 | 0.0264631 | 0.0401085 | 0.0618484 | 0.125297 | 0.782881 | 0.887818 | 0.963815 |
| tossup | r_3 | 1240 | 0.058098 | 0.0306861 | 0.00834153 | 0.0232898 | 0.0385194 | 0.0516165 | 0.0694304 | 0.119924 | 0.23483 |
| tossup | r_4 | 1240 | 0.0703843 | 0.0442486 | 0.00877201 | 0.0249907 | 0.0413339 | 0.0580019 | 0.0827604 | 0.168326 | 0.280148 |
| tossup | r_5 | 1240 | 0.0721654 | 0.0443471 | 0.00965351 | 0.0269808 | 0.0441752 | 0.0600079 | 0.0823369 | 0.178351 | 0.267495 |
| tossup | r_norm | 1240 | 0.757648 | 0.0797276 | 0.563178 | 0.626629 | 0.702164 | 0.755435 | 0.815698 | 0.889601 | 0.963986 |
