# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold/fold_2/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/multidim/multidim-all2024-gameinfill-5fold/fold_2`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 297692 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.545641 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.894051 |
| log_loss | 0.414519 |
| ece | 0.0328488 |
| brier | 0.132156 |
| part_accuracy | 0.81195 |
| part_all_correct_accuracy | 0.519367 |
| accuracy_lift_over_all_correct | 0.292583 |
| part_accuracy_macro_team | 0.81624 |
| part_accuracy_macro_bonus | 0.808329 |
| probability_std | 0.340723 |
| probability_p10 | 0.0608722 |
| probability_p50 | 0.453559 |
| probability_p90 | 0.946469 |
| mean_predictive_variance | 0.133726 |
| exact_acc | 0.523787 |
| ranked_probability_score | 0.112259 |
| bonus_total_score_log_loss | 0.992657 |
| ppb_mae | 1.87625 |
| ranked_probability_score_responses | 8597 |
| bonus_total_score_log_loss_responses | 8597 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.625247 |
| log_loss | 0.819321 |
| ece | 0.220132 |
| brier | 0.261846 |
| accuracy | 0.619423 |
| all_correct_accuracy | 0.764178 |
| accuracy_lift_over_all_correct | -0.144755 |
| probability_std | 0.291752 |
| probability_p10 | 0.102781 |
| probability_p50 | 0.618182 |
| probability_p90 | 0.908259 |
| mean_predictive_variance | 0.161437 |
| integrated_brier_score | 0.0958602 |
| joint_tossup_event_log_loss | 6.77617 |
| buzz_position_mae | 0.145638 |
| buzz_position_median_absolute_error | 0.125505 |
| buzz_position_bias | -0.0385668 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.395809 |
| first_buzzer_mean_reciprocal_rank | 0.603629 |
| first_buzzer_log_loss | 1.59788 |
| first_buzzer_events | 9257 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.801296 |
| match_winner_brier | 0.138423 |
| match_games | 463 |
| match_simulations_per_game | 500 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9257 | 0.625247 | 0.819321 | 0.220132 | 0.261846 | 0.619423 | 0.764178 | -0.144755 | 0.291752 | 0.102781 | 0.618182 | 0.908259 | 0.161437 |
| tossup_correctness | tier | fall | 2798 | 0.642351 | 0.830272 | 0.241171 | 0.261778 | 0.620086 | 0.785204 | -0.165118 | 0.290366 | 0.0925015 | 0.597108 | 0.897612 | 0.16355 |
| tossup_correctness | tier | nationals | 1545 | 0.610675 | 0.773007 | 0.193128 | 0.258927 | 0.617476 | 0.721036 | -0.10356 | 0.288802 | 0.123417 | 0.641059 | 0.921993 | 0.160384 |
| tossup_correctness | tier | regionals | 2039 | 0.620758 | 0.841413 | 0.219741 | 0.263018 | 0.625307 | 0.762138 | -0.136832 | 0.2983 | 0.091885 | 0.633178 | 0.924624 | 0.156581 |
| tossup_correctness | tier | winter | 2875 | 0.627366 | 0.817884 | 0.223858 | 0.262649 | 0.615652 | 0.768348 | -0.152696 | 0.289229 | 0.108972 | 0.608997 | 0.90386 | 0.163391 |
| tossup_correctness | category | Current Events | 129 | 0.585992 | 0.881871 | 0.267636 | 0.29321 | 0.55814 | 0.666667 | -0.108527 | 0.306259 | 0.0673975 | 0.624598 | 0.893449 | 0.155014 |
| tossup_correctness | category | Fine Arts | 1074 | 0.605496 | 0.887447 | 0.264942 | 0.285786 | 0.590317 | 0.776536 | -0.18622 | 0.297103 | 0.0795826 | 0.568193 | 0.899888 | 0.16089 |
| tossup_correctness | category | Geography | 180 | 0.596553 | 0.817306 | 0.191961 | 0.280547 | 0.544444 | 0.616667 | -0.0722222 | 0.259283 | 0.11159 | 0.492743 | 0.81685 | 0.182482 |
| tossup_correctness | category | History | 1454 | 0.640517 | 0.777552 | 0.206793 | 0.25038 | 0.644429 | 0.757909 | -0.11348 | 0.286273 | 0.109255 | 0.627149 | 0.902866 | 0.163627 |
| tossup_correctness | category | Literature | 1435 | 0.59648 | 0.808058 | 0.232295 | 0.254632 | 0.632056 | 0.810453 | -0.178397 | 0.289244 | 0.12067 | 0.660897 | 0.922315 | 0.157709 |
| tossup_correctness | category | Mythology | 324 | 0.629073 | 0.898282 | 0.259688 | 0.271505 | 0.598765 | 0.79321 | -0.194444 | 0.283679 | 0.0975383 | 0.555001 | 0.895949 | 0.168395 |
| tossup_correctness | category | Other Academic | 71 | 0.591503 | 0.782372 | 0.24038 | 0.26699 | 0.577465 | 0.760563 | -0.183099 | 0.276293 | 0.164891 | 0.579038 | 0.90373 | 0.169613 |
| tossup_correctness | category | Philosophy | 310 | 0.686441 | 0.75461 | 0.229949 | 0.251752 | 0.612903 | 0.76129 | -0.148387 | 0.293364 | 0.0833661 | 0.553894 | 0.910449 | 0.162955 |
| tossup_correctness | category | Popular Culture | 108 | 0.543403 | 1.00951 | 0.423695 | 0.332172 | 0.481481 | 0.888889 | -0.407407 | 0.253468 | 0.101069 | 0.468981 | 0.808312 | 0.184687 |
| tossup_correctness | category | Religion | 361 | 0.645723 | 0.800278 | 0.242481 | 0.267367 | 0.620499 | 0.742382 | -0.121884 | 0.285358 | 0.0906158 | 0.550124 | 0.866748 | 0.168303 |
| tossup_correctness | category | Science | 1445 | 0.63693 | 0.794157 | 0.192507 | 0.252998 | 0.625606 | 0.746021 | -0.120415 | 0.289701 | 0.110176 | 0.62502 | 0.914461 | 0.161354 |
| tossup_correctness | category | Social Science | 327 | 0.66605 | 0.729945 | 0.174831 | 0.244529 | 0.629969 | 0.718654 | -0.088685 | 0.284305 | 0.120372 | 0.631886 | 0.889769 | 0.166086 |
| tossup_correctness | category | Unknown | 2039 | 0.620758 | 0.841413 | 0.219741 | 0.263018 | 0.625307 | 0.762138 | -0.136832 | 0.2983 | 0.091885 | 0.633178 | 0.924624 | 0.156581 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 183 | 0.706821 | 1.38879 | 0.499743 | 0.431551 | 0.398907 | 0.743169 | -0.344262 | 0.21273 | 0.0139292 | 0.193522 | 0.550897 | 0.138916 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 955 | 0.658179 | 1.11473 | 0.379497 | 0.356423 | 0.46911 | 0.728796 | -0.259686 | 0.263921 | 0.0382757 | 0.302351 | 0.749231 | 0.157635 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2239 | 0.657119 | 0.880983 | 0.269225 | 0.281213 | 0.597588 | 0.752568 | -0.15498 | 0.284875 | 0.0741222 | 0.513909 | 0.862001 | 0.168621 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2875 | 0.630184 | 0.750392 | 0.200398 | 0.241095 | 0.643826 | 0.786087 | -0.142261 | 0.275613 | 0.170063 | 0.650803 | 0.913842 | 0.165463 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 3005 | 0.598003 | 0.710762 | 0.149768 | 0.226877 | 0.673544 | 0.764393 | -0.0908486 | 0.259488 | 0.242235 | 0.739914 | 0.936617 | 0.154813 |
| bonus_part_correctness | aggregate | all | 25791 | 0.894051 | 0.414519 | 0.0328488 | 0.132156 | 0.81195 | 0.519367 | 0.292583 | 0.340723 | 0.0608722 | 0.453559 | 0.946469 | 0.133726 |
| bonus_part_correctness | tier | fall | 7995 | 0.898406 | 0.398571 | 0.0279125 | 0.126857 | 0.814634 | 0.595122 | 0.219512 | 0.328277 | 0.105161 | 0.621288 | 0.95555 | 0.137251 |
| bonus_part_correctness | tier | nationals | 4095 | 0.885145 | 0.435192 | 0.0592254 | 0.139729 | 0.800733 | 0.425153 | 0.37558 | 0.31445 | 0.0420734 | 0.243399 | 0.858191 | 0.133146 |
| bonus_part_correctness | tier | regionals | 5580 | 0.887965 | 0.426762 | 0.0413799 | 0.136046 | 0.812903 | 0.495878 | 0.317025 | 0.339923 | 0.0548526 | 0.377707 | 0.938296 | 0.132382 |
| bonus_part_correctness | tier | winter | 8121 | 0.894557 | 0.411384 | 0.0218748 | 0.13088 | 0.814309 | 0.508435 | 0.305874 | 0.344017 | 0.0593954 | 0.445473 | 0.953421 | 0.131472 |
| bonus_part_correctness | category | Current Events | 216 | 0.89393 | 0.406968 | 0.0609379 | 0.127763 | 0.842593 | 0.467593 | 0.375 | 0.344421 | 0.0447499 | 0.356042 | 0.921219 | 0.128921 |
| bonus_part_correctness | category | Fine Arts | 2970 | 0.879731 | 0.440237 | 0.0405187 | 0.142818 | 0.786869 | 0.512795 | 0.274074 | 0.335586 | 0.0636003 | 0.4304 | 0.941444 | 0.136773 |
| bonus_part_correctness | category | Geography | 501 | 0.893093 | 0.40811 | 0.028209 | 0.130332 | 0.816367 | 0.572854 | 0.243513 | 0.332121 | 0.0766362 | 0.597677 | 0.944315 | 0.136793 |
| bonus_part_correctness | category | History | 4068 | 0.896934 | 0.408876 | 0.0365377 | 0.130549 | 0.810964 | 0.549164 | 0.261799 | 0.339682 | 0.0636185 | 0.514878 | 0.950073 | 0.134428 |
| bonus_part_correctness | category | Literature | 4065 | 0.904492 | 0.39294 | 0.025896 | 0.123663 | 0.82829 | 0.510947 | 0.317343 | 0.342425 | 0.0629837 | 0.448919 | 0.950376 | 0.132567 |
| bonus_part_correctness | category | Mythology | 945 | 0.861576 | 0.454375 | 0.03616 | 0.14877 | 0.779894 | 0.606349 | 0.173545 | 0.317719 | 0.126195 | 0.605136 | 0.955355 | 0.143438 |
| bonus_part_correctness | category | Other Academic | 219 | 0.865199 | 0.473258 | 0.068308 | 0.15576 | 0.762557 | 0.493151 | 0.269406 | 0.351145 | 0.043407 | 0.462646 | 0.928062 | 0.125669 |
| bonus_part_correctness | category | Philosophy | 963 | 0.897773 | 0.408382 | 0.0334547 | 0.130277 | 0.811007 | 0.483904 | 0.327103 | 0.330691 | 0.0650765 | 0.392971 | 0.933638 | 0.13879 |
| bonus_part_correctness | category | Popular Culture | 288 | 0.840432 | 0.485779 | 0.050781 | 0.159902 | 0.763889 | 0.625 | 0.138889 | 0.328244 | 0.11282 | 0.674605 | 0.965674 | 0.129427 |
| bonus_part_correctness | category | Religion | 1008 | 0.90089 | 0.404088 | 0.0425996 | 0.129408 | 0.815476 | 0.503968 | 0.311508 | 0.347354 | 0.0503806 | 0.418017 | 0.938215 | 0.128462 |
| bonus_part_correctness | category | Science | 4059 | 0.898539 | 0.407531 | 0.0364681 | 0.128902 | 0.816457 | 0.530673 | 0.285785 | 0.340077 | 0.0636232 | 0.461028 | 0.949325 | 0.134321 |
| bonus_part_correctness | category | Social Science | 909 | 0.922267 | 0.353537 | 0.0331132 | 0.108469 | 0.847085 | 0.458746 | 0.388339 | 0.351095 | 0.0529009 | 0.355413 | 0.949079 | 0.124542 |
| bonus_part_correctness | category | Unknown | 5580 | 0.887965 | 0.426762 | 0.0413799 | 0.136046 | 0.812903 | 0.495878 | 0.317025 | 0.339923 | 0.0548526 | 0.377707 | 0.938296 | 0.132382 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.886487 | 0.894051 | 0.00756392 | synergy |
| log_loss | 0.425455 | 0.414519 | -0.0109356 | synergy |
| ece | 0.0195432 | 0.0328488 | 0.0133056 | no-synergy |
| brier | 0.135467 | 0.132156 | -0.0033111 | synergy |
| accuracy_lift_over_all_correct | 0.286224 | 0.292583 | 0.00635881 | synergy |
| part_accuracy | 0.805591 | 0.81195 | 0.00635881 | synergy |
| part_accuracy_macro_team | 0.809463 | 0.81624 | 0.00677697 | synergy |
| part_accuracy_macro_bonus | 0.805242 | 0.808329 | 0.00308709 | synergy |
| exact_acc | 0.507619 | 0.523787 | 0.0161684 | synergy |
| ranked_probability_score | 0.116623 | 0.112259 | -0.00436389 | synergy |
| bonus_total_score_log_loss | 1.02168 | 0.992657 | -0.0290258 | synergy |
| ppb_mae | 2.35346 | 1.87625 | -0.477213 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1197 | 4.59763 | 1.16213 | 0.853684 | 2.02535 | 4.05272 | 4.81723 | 5.38188 | 6.09235 | 7.14394 |
| player | theta_1 | 1197 | 0.065209 | 0.728583 | -2.44361 | -1.32246 | -0.35176 | 0.179047 | 0.568345 | 1.06503 | 2.06677 |
| player | theta_2 | 1197 | 0.0444176 | 0.738469 | -2.8425 | -1.42352 | -0.364589 | 0.156304 | 0.550528 | 1.10028 | 1.84782 |
| player | theta_3 | 1197 | 0.088853 | 0.720164 | -2.19393 | -1.32143 | -0.305118 | 0.17014 | 0.575132 | 1.18943 | 2.13594 |
| player | theta_4 | 1197 | 0.0704689 | 0.725329 | -2.67166 | -1.31753 | -0.351108 | 0.192343 | 0.562519 | 1.12928 | 1.88896 |
| player | theta_5 | 1197 | -0.0185873 | 0.743274 | -2.64604 | -1.45167 | -0.426809 | 0.107115 | 0.499427 | 1.02183 | 1.61412 |
| player | theta_norm | 1197 | 1.52885 | 0.594536 | 0.320833 | 0.709383 | 1.08228 | 1.42548 | 1.895 | 2.67612 | 3.488 |
| tossup | beta_1 | 1240 | 0.756998 | 0.515528 | -1.27994 | 0.221919 | 0.40402 | 0.588983 | 0.973349 | 1.85969 | 2.74839 |
| tossup | beta_2 | 1240 | 0.870013 | 0.589757 | -1.03921 | 0.218174 | 0.431182 | 0.656635 | 1.25181 | 2.03383 | 2.86037 |
| tossup | beta_3 | 1240 | 0.740734 | 0.524546 | -0.808635 | 0.224724 | 0.403181 | 0.567294 | 0.880235 | 1.92319 | 2.94688 |
| tossup | beta_4 | 1240 | 0.739047 | 0.523695 | -1.14892 | 0.219557 | 0.401138 | 0.566411 | 0.90353 | 1.90575 | 2.76495 |
| tossup | beta_5 | 1240 | 0.802671 | 0.583354 | -1.85973 | 0.200678 | 0.386691 | 0.589746 | 1.13234 | 2.00744 | 2.73583 |
| tossup | gamma_1 | 1240 | 13.2292 | 82.3327 | 0.52216 | 3.27372 | 4.50472 | 5.13548 | 6.05247 | 23.8721 | 1922.23 |
| tossup | gamma_2 | 1240 | 11.5554 | 57.4392 | 1.11522 | 3.22244 | 4.47112 | 5.16891 | 6.35495 | 21.487 | 1273.6 |
| tossup | gamma_3 | 1240 | 11.4846 | 47.4584 | 0.965284 | 3.30434 | 4.48732 | 5.04986 | 5.93966 | 23.4488 | 853.856 |
| tossup | gamma_4 | 1240 | 13.4848 | 72.7665 | 0.485441 | 3.21619 | 4.51606 | 5.119 | 5.96011 | 19.6581 | 1447.8 |
| tossup | gamma_5 | 1240 | 12.987 | 64.3344 | 0.612626 | 3.31031 | 4.54847 | 5.15378 | 6.39904 | 24.6926 | 1469.28 |
| tossup | mu_1 | 1240 | 0.503567 | 0.100777 | 0.143635 | 0.396329 | 0.449201 | 0.478719 | 0.525575 | 0.717592 | 0.978542 |
| tossup | mu_2 | 1240 | 0.525528 | 0.125518 | 0.144137 | 0.390578 | 0.446791 | 0.485151 | 0.583321 | 0.78564 | 0.977226 |
| tossup | mu_3 | 1240 | 0.503062 | 0.106812 | 0.142085 | 0.391097 | 0.447636 | 0.478502 | 0.517636 | 0.731814 | 0.991413 |
| tossup | mu_4 | 1240 | 0.503338 | 0.107246 | 0.215919 | 0.392707 | 0.449329 | 0.477595 | 0.517217 | 0.738832 | 0.969861 |
| tossup | mu_5 | 1240 | 0.508853 | 0.11245 | 0.143738 | 0.380348 | 0.447389 | 0.478883 | 0.537889 | 0.741001 | 0.984586 |
| tossup | r_1 | 1240 | 1.0032 | 0.782781 | 0.091795 | 0.23569 | 0.43248 | 0.7473 | 1.35147 | 2.60751 | 5.48406 |
| tossup | r_2 | 1240 | 1.3948 | 1.12216 | 0.0779637 | 0.243471 | 0.534114 | 0.984437 | 2.04594 | 3.6898 | 5.98262 |
| tossup | r_3 | 1240 | 1.00759 | 0.872232 | 0.10036 | 0.210195 | 0.417825 | 0.705281 | 1.25878 | 2.99103 | 5.76123 |
| tossup | r_4 | 1240 | 0.995083 | 0.785043 | 0.0859882 | 0.217565 | 0.436281 | 0.718901 | 1.35914 | 2.72919 | 4.52992 |
| tossup | r_5 | 1240 | 1.13589 | 0.836182 | 0.0547561 | 0.220777 | 0.477787 | 0.873745 | 1.63582 | 2.7813 | 4.24501 |
| tossup | r_norm | 1240 | 3.08999 | 0.803194 | 1.20438 | 1.94067 | 2.50928 | 3.02103 | 3.58938 | 4.54631 | 6.36813 |

## Bonus And Synergy Parameters

No bonus parameter distribution summary CSV was found.
