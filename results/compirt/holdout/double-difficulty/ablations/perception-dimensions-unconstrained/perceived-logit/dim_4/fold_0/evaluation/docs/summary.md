# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_4/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/ablations/perception-dimensions-unconstrained/perceived-logit/dim_4/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 4 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 335313 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.541251 |
| log_loss | 0.603626 |
| ece | 0.0975108 |
| brier | 0.190663 |
| accuracy | 0.763959 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.00129102 |
| probability_std | 0.0978194 |
| probability_p10 | 0.716799 |
| probability_p50 | 0.882088 |
| probability_p90 | 0.947906 |
| mean_predictive_variance | 0.114835 |
| integrated_brier_score | 0.172061 |
| joint_tossup_event_log_loss | 7.73115 |
| buzz_position_mae | 0.336909 |
| buzz_position_median_absolute_error | 0.338166 |
| buzz_position_bias | -0.323691 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.366541 |
| first_buzzer_mean_reciprocal_rank | 0.578021 |
| first_buzzer_log_loss | 1.63446 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.62496 |
| tossup_scorer_player_top1_accuracy | 0.270382 |
| tossup_scorer_team_top1_accuracy | 0.400425 |
| tossup_game_winner_accuracy | 0.711454 |
| tossup_game_margin_mae | 43.3735 |
| tournament_player_ppg_spearman | 0.591695 |
| tournament_player_ppg_mae | 10.0468 |
| tournament_player_ppg_top10_overlap | 0.603448 |
| neg_auroc | 0.541251 |
| neg_average_precision | 0.274456 |
| neg_precision | 0.403226 |
| neg_recall | 0.0114574 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0294529 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.239375 |
| no_buzz_calibration_error | 0.226105 |
| no_buzz_brier | 0.0735066 |
| full_pmf_max_mass_error | 1.33227e-15 |
| tossup_outcome_events | 9420 |
| first_buzzer_team_top1_accuracy_events | 9295 |
| tossup_scorer_player_top1_accuracy_events | 9420 |
| tossup_scorer_team_top1_accuracy_events | 9420 |
| tossup_game_winner_accuracy_games | 454 |
| tossup_game_margin_mae_games | 471 |
| tournament_player_ppg_tournaments | 29 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9295 | 0.541251 | 0.603626 | 0.0975108 | 0.190663 | 0.763959 | 0.76525 | -0.00129102 | 0.0978194 | 0.716799 | 0.882088 | 0.947906 | 0.114835 |
| tossup_correctness | tier | fall | 2933 | 0.545083 | 0.546105 | 0.0764766 | 0.171568 | 0.790999 | 0.791681 | -0.000681896 | 0.0812361 | 0.750317 | 0.87929 | 0.938566 | 0.114678 |
| tossup_correctness | tier | nationals | 1584 | 0.562128 | 0.647904 | 0.103866 | 0.211393 | 0.718434 | 0.724747 | -0.00631313 | 0.133198 | 0.595017 | 0.854952 | 0.943613 | 0.137188 |
| tossup_correctness | tier | regionals | 1886 | 0.527035 | 0.64186 | 0.112936 | 0.205013 | 0.745493 | 0.746023 | -0.000530223 | 0.102631 | 0.692795 | 0.868071 | 0.950711 | 0.1215 |
| tossup_correctness | tier | winter | 2892 | 0.523028 | 0.612775 | 0.112815 | 0.189316 | 0.773513 | 0.773167 | 0.000345781 | 0.0737294 | 0.783118 | 0.901837 | 0.953718 | 0.098405 |
| tossup_correctness | category | Current Events | 124 | 0.491502 | 0.615152 | 0.131297 | 0.199513 | 0.758065 | 0.75 | 0.00806452 | 0.0982271 | 0.732 | 0.851114 | 0.916668 | 0.134543 |
| tossup_correctness | category | Fine Arts | 1103 | 0.50082 | 0.650169 | 0.137608 | 0.202575 | 0.759746 | 0.759746 | 0 | 0.0932245 | 0.731505 | 0.899794 | 0.953959 | 0.104152 |
| tossup_correctness | category | Geography | 197 | 0.651399 | 0.735173 | 0.197694 | 0.247923 | 0.664975 | 0.670051 | -0.00507614 | 0.0834397 | 0.767147 | 0.884631 | 0.940489 | 0.111581 |
| tossup_correctness | category | History | 1491 | 0.539581 | 0.558136 | 0.0736427 | 0.175339 | 0.784038 | 0.787391 | -0.00335345 | 0.0967633 | 0.712209 | 0.869077 | 0.940726 | 0.121805 |
| tossup_correctness | category | Literature | 1472 | 0.532162 | 0.541406 | 0.087305 | 0.164968 | 0.805027 | 0.804348 | 0.000679348 | 0.0937151 | 0.748381 | 0.900234 | 0.953732 | 0.103105 |
| tossup_correctness | category | Mythology | 332 | 0.621864 | 0.496171 | 0.0954997 | 0.155128 | 0.810241 | 0.813253 | -0.00301205 | 0.0796862 | 0.785848 | 0.902869 | 0.947171 | 0.100314 |
| tossup_correctness | category | Other Academic | 69 | 0.477376 | 0.643455 | 0.135886 | 0.197498 | 0.753623 | 0.753623 | 0 | 0.0941694 | 0.727278 | 0.889948 | 0.939399 | 0.109629 |
| tossup_correctness | category | Philosophy | 324 | 0.549569 | 0.538355 | 0.0837299 | 0.16467 | 0.799383 | 0.799383 | 0 | 0.0910449 | 0.726803 | 0.902941 | 0.948701 | 0.105199 |
| tossup_correctness | category | Popular Culture | 102 | 0.413149 | 0.507453 | 0.0660052 | 0.151166 | 0.833333 | 0.833333 | 0 | 0.0668392 | 0.785263 | 0.887907 | 0.930797 | 0.10787 |
| tossup_correctness | category | Religion | 372 | 0.61767 | 0.673708 | 0.157424 | 0.220488 | 0.698925 | 0.709677 | -0.0107527 | 0.112101 | 0.706738 | 0.891928 | 0.943665 | 0.111816 |
| tossup_correctness | category | Science | 1487 | 0.559649 | 0.601524 | 0.0875068 | 0.192853 | 0.751177 | 0.752522 | -0.00134499 | 0.0994383 | 0.697172 | 0.861296 | 0.937696 | 0.126486 |
| tossup_correctness | category | Social Science | 336 | 0.517331 | 0.751122 | 0.182667 | 0.242788 | 0.702381 | 0.702381 | 0 | 0.0909912 | 0.767836 | 0.894039 | 0.94609 | 0.106203 |
| tossup_correctness | category | Unknown | 1886 | 0.527035 | 0.64186 | 0.112936 | 0.205013 | 0.745493 | 0.746023 | -0.000530223 | 0.102631 | 0.692795 | 0.868071 | 0.950711 | 0.1215 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.54443 | 0.612645 | 0.113686 | 0.203858 | 0.730964 | 0.736041 | -0.00507614 | 0.104602 | 0.66425 | 0.821148 | 0.916586 | 0.147531 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.517231 | 0.640847 | 0.0956701 | 0.20781 | 0.732995 | 0.735025 | -0.00203046 | 0.098035 | 0.688859 | 0.851342 | 0.928042 | 0.132842 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.558104 | 0.576628 | 0.0856107 | 0.18463 | 0.768103 | 0.769436 | -0.00133274 | 0.0923126 | 0.729426 | 0.870542 | 0.937838 | 0.121079 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.55119 | 0.563593 | 0.0853853 | 0.176887 | 0.783322 | 0.78402 | -0.000697837 | 0.0936979 | 0.727425 | 0.884193 | 0.945382 | 0.113713 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.530105 | 0.649374 | 0.123033 | 0.201868 | 0.754673 | 0.756008 | -0.00133511 | 0.101603 | 0.716028 | 0.904251 | 0.95685 | 0.103148 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1186 | -1.34464 | 0.770664 | -3.19525 | -2.38675 | -1.79961 | -1.43573 | -1.02426 | 0.0390321 | 2.17724 |
| player | beta | 1186 | -3.44526 | 1.13396 | -6.92433 | -5.88883 | -4.00653 | -3.1588 | -2.60686 | -2.0767 | -1.6834 |
| player | theta_1 | 1186 | 0.839594 | 0.94695 | -2.13192 | -0.932426 | 0.229326 | 0.947923 | 1.56008 | 2.15523 | 3.519 |
| player | theta_2 | 1186 | 0.837528 | 0.952566 | -3.10377 | -0.820007 | 0.277993 | 0.938499 | 1.47238 | 2.26067 | 3.63022 |
| player | theta_3 | 1186 | 0.809992 | 0.938785 | -2.14173 | -0.911501 | 0.230858 | 0.954973 | 1.47712 | 2.15135 | 3.27692 |
| player | theta_4 | 1186 | 0.778166 | 0.782022 | -1.87446 | -0.697738 | 0.306475 | 0.872252 | 1.30695 | 1.92756 | 3.30648 |
| player | theta_norm | 1186 | 2.35763 | 0.635703 | 0.221247 | 1.26077 | 1.9532 | 2.39081 | 2.78149 | 3.37306 | 4.6679 |
| tossup | start_difficulty_d1 | 1240 | -0.893996 | 0.398242 | -2.11118 | -1.65922 | -1.17156 | -0.806856 | -0.589888 | -0.365494 | -0.126745 |
| tossup | start_difficulty_d2 | 1240 | -0.910644 | 0.445583 | -2.25499 | -1.68412 | -1.23097 | -0.889913 | -0.564441 | -0.238165 | -0.0411341 |
| tossup | start_difficulty_d3 | 1240 | -0.858047 | 0.471115 | -2.29941 | -1.75183 | -1.1724 | -0.764339 | -0.462746 | -0.284714 | -0.0725704 |
| tossup | start_difficulty_d4 | 1240 | -0.806512 | 0.333701 | -1.91911 | -1.41921 | -1.00951 | -0.788215 | -0.560079 | -0.317166 | -0.107409 |
| tossup | end_difficulty_d1 | 1240 | -1.63326 | 0.316895 | -2.77018 | -2.18935 | -1.85343 | -1.59788 | -1.39279 | -1.16955 | -1.01414 |
| tossup | end_difficulty_d2 | 1240 | -1.6529 | 0.387138 | -3.00309 | -2.27508 | -1.93542 | -1.63463 | -1.33723 | -1.07374 | -0.805006 |
| tossup | end_difficulty_d3 | 1240 | -1.6151 | 0.408113 | -2.9226 | -2.37408 | -1.9023 | -1.52372 | -1.27106 | -1.10019 | -0.840456 |
| tossup | end_difficulty_d4 | 1240 | -1.58195 | 0.313837 | -2.6434 | -2.14015 | -1.78507 | -1.55286 | -1.34742 | -1.12303 | -0.874786 |
| tossup | total_drop_d1 | 1240 | 0.739262 | 0.19855 | 0.229386 | 0.36228 | 0.616574 | 0.770588 | 0.888779 | 1.02152 | 1.20116 |
| tossup | total_drop_d2 | 1240 | 0.742254 | 0.180807 | 0.256327 | 0.396696 | 0.636348 | 0.762817 | 0.867426 | 1.01455 | 1.24022 |
| tossup | total_drop_d3 | 1240 | 0.757051 | 0.187727 | 0.239244 | 0.375875 | 0.663628 | 0.797218 | 0.881465 | 1.00624 | 1.39015 |
| tossup | total_drop_d4 | 1240 | 0.775435 | 0.164772 | 0.27543 | 0.433208 | 0.696033 | 0.796536 | 0.87587 | 1.01686 | 1.34909 |
| tossup | drop_share_1_d1 | 1240 | 0.319821 | 0.0225796 | 0.223234 | 0.285397 | 0.307407 | 0.319487 | 0.331717 | 0.35664 | 0.431876 |
| tossup | drop_share_2_d1 | 1240 | 0.326865 | 0.0184745 | 0.254568 | 0.289106 | 0.318182 | 0.329908 | 0.339744 | 0.350993 | 0.366865 |
| tossup | drop_share_3_d1 | 1240 | 0.353315 | 0.0284797 | 0.270762 | 0.318633 | 0.336206 | 0.348771 | 0.363131 | 0.410248 | 0.50001 |
| tossup | drop_share_1_d2 | 1240 | 0.319516 | 0.0221934 | 0.209838 | 0.287011 | 0.306456 | 0.318523 | 0.33145 | 0.355537 | 0.413856 |
| tossup | drop_share_2_d2 | 1240 | 0.327583 | 0.0170934 | 0.246697 | 0.29452 | 0.318719 | 0.329919 | 0.339555 | 0.350773 | 0.362668 |
| tossup | drop_share_3_d2 | 1240 | 0.3529 | 0.0261309 | 0.265609 | 0.318236 | 0.337066 | 0.350109 | 0.363573 | 0.400039 | 0.484108 |
| tossup | drop_share_1_d3 | 1240 | 0.321134 | 0.0238393 | 0.240089 | 0.289752 | 0.306004 | 0.317965 | 0.331957 | 0.367369 | 0.450625 |
| tossup | drop_share_2_d3 | 1240 | 0.329603 | 0.0157476 | 0.26978 | 0.298203 | 0.321474 | 0.332036 | 0.340203 | 0.351566 | 0.365715 |
| tossup | drop_share_3_d3 | 1240 | 0.349264 | 0.0237625 | 0.256294 | 0.312845 | 0.335861 | 0.348067 | 0.360954 | 0.389606 | 0.444592 |
| tossup | drop_share_1_d4 | 1240 | 0.318033 | 0.0201836 | 0.202972 | 0.287108 | 0.30801 | 0.318306 | 0.330308 | 0.348336 | 0.40349 |
| tossup | drop_share_2_d4 | 1240 | 0.330207 | 0.0155248 | 0.263264 | 0.298912 | 0.32356 | 0.33263 | 0.340621 | 0.351169 | 0.365371 |
| tossup | drop_share_3_d4 | 1240 | 0.35176 | 0.02621 | 0.280944 | 0.320587 | 0.33633 | 0.347606 | 0.360298 | 0.403125 | 0.508703 |
| tossup | r_1 | 1240 | 0.254155 | 0.208009 | 0.0313942 | 0.0602188 | 0.117533 | 0.168061 | 0.32494 | 0.758953 | 0.880351 |
| tossup | r_2 | 1240 | 0.273672 | 0.205387 | 0.0355052 | 0.0576975 | 0.108736 | 0.200129 | 0.395208 | 0.692954 | 0.898229 |
| tossup | r_3 | 1240 | 0.256753 | 0.183593 | 0.0262452 | 0.0557342 | 0.110143 | 0.1947 | 0.376479 | 0.642668 | 0.834827 |
| tossup | r_4 | 1240 | 0.21542 | 0.143175 | 0.0335142 | 0.0594532 | 0.111479 | 0.186036 | 0.274228 | 0.496219 | 0.869006 |
| tossup | r_norm | 1240 | 0.618694 | 0.0926722 | 0.502301 | 0.514238 | 0.544237 | 0.590092 | 0.676618 | 0.805161 | 0.900218 |
