# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/multidim/multidim-all2024-bounceback-cal/evaluation`
Result root: `results/compirt/in_sample/multidim/multidim-all2024-bounceback-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 391292 |
| pyramidal | calibrate_correctness | True |
| compositional | tournament | all 2024 |
| compositional | dimensions | 5 |
| compositional | steps | 2000 |
| compositional | final_loss | 62830.1 |
| compositional | calibrate_correctness | True |
| compositional | synergy_dimensions | 0 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.742581 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.936141 |
| log_loss | 0.331058 |
| ece | 0.0382418 |
| brier | 0.10349 |
| part_accuracy | 0.853987 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.333498 |
| part_accuracy_macro_team | 0.856057 |
| part_accuracy_macro_game | 0.854284 |
| part_accuracy_macro_bonus | 0.861529 |
| probability_std | 0.360323 |
| probability_p10 | 0.0432157 |
| probability_p50 | 0.453928 |
| probability_p90 | 0.969606 |
| mean_predictive_variance | 0.120092 |
| exact_acc | 0.61591 |
| ranked_probability_score | 0.0941761 |
| bonus_total_score_log_loss | 0.838958 |
| ppb_mae | 1.52347 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.663602 |
| log_loss | 0.512191 |
| ece | 0.0114169 |
| brier | 0.167145 |
| accuracy | 0.770526 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | 0.00325583 |
| probability_std | 0.0934659 |
| probability_p10 | 0.645357 |
| probability_p50 | 0.787441 |
| probability_p90 | 0.877345 |
| mean_predictive_variance | 0.16713 |
| integrated_brier_score | 0.0862266 |
| joint_tossup_event_log_loss | 6.01746 |
| buzz_position_mae | 0.130462 |
| buzz_position_median_absolute_error | 0.110282 |
| buzz_position_bias | -0.00629646 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |
| first_buzzer_top1_accuracy | 0.485996 |
| first_buzzer_mean_reciprocal_rank | 0.6741 |
| first_buzzer_log_loss | 1.33989 |
| first_buzzer_events | 47914 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.803238 |
| match_winner_brier | 0.134394 |
| match_games | 2409 |
| match_simulations_per_game | 500 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.663602 | 0.512191 | 0.0114169 | 0.167145 | 0.770526 | 0.767271 | 0.00325583 | 0.0934659 | 0.645357 | 0.787441 | 0.877345 | 0.16713 |
| tossup_correctness | tier | fall | 14760 | 0.684439 | 0.482364 | 0.0264963 | 0.154897 | 0.791125 | 0.787466 | 0.00365854 | 0.0897309 | 0.652239 | 0.787984 | 0.872607 | 0.167545 |
| tossup_correctness | tier | nationals | 7940 | 0.633137 | 0.572932 | 0.0521448 | 0.191848 | 0.728841 | 0.72733 | 0.00151134 | 0.0997314 | 0.640029 | 0.795304 | 0.891992 | 0.162184 |
| tossup_correctness | tier | regionals | 10202 | 0.655768 | 0.523878 | 0.0139978 | 0.171838 | 0.764556 | 0.758969 | 0.00558714 | 0.0970989 | 0.642002 | 0.789486 | 0.881784 | 0.166061 |
| tossup_correctness | tier | winter | 15012 | 0.675015 | 0.501447 | 0.0235072 | 0.162932 | 0.776379 | 0.774181 | 0.00219824 | 0.090843 | 0.644418 | 0.781752 | 0.870953 | 0.170066 |
| tossup_correctness | category | Current Events | 640 | 0.663504 | 0.5501 | 0.028778 | 0.183371 | 0.734375 | 0.734375 | 0 | 0.0918076 | 0.628812 | 0.76154 | 0.854979 | 0.179586 |
| tossup_correctness | category | Fine Arts | 5640 | 0.6633 | 0.512429 | 0.00996907 | 0.167219 | 0.770745 | 0.766489 | 0.00425532 | 0.0950567 | 0.640428 | 0.785777 | 0.878464 | 0.167835 |
| tossup_correctness | category | Geography | 972 | 0.668034 | 0.603658 | 0.0752848 | 0.208938 | 0.680041 | 0.675926 | 0.00411523 | 0.0854401 | 0.62706 | 0.74687 | 0.845731 | 0.185245 |
| tossup_correctness | category | History | 7599 | 0.691196 | 0.506183 | 0.0247385 | 0.16537 | 0.767075 | 0.764969 | 0.00210554 | 0.0900924 | 0.653725 | 0.788655 | 0.874724 | 0.166856 |
| tossup_correctness | category | Literature | 7469 | 0.636401 | 0.467578 | 0.0275937 | 0.147948 | 0.811086 | 0.812157 | -0.00107109 | 0.0966827 | 0.652456 | 0.805673 | 0.887338 | 0.159676 |
| tossup_correctness | category | Mythology | 1692 | 0.660287 | 0.471768 | 0.0600082 | 0.148787 | 0.807329 | 0.80792 | -0.000591017 | 0.0871946 | 0.642725 | 0.767487 | 0.86102 | 0.176243 |
| tossup_correctness | category | Other Academic | 357 | 0.622691 | 0.538485 | 0.040398 | 0.177016 | 0.756303 | 0.756303 | 0 | 0.0901343 | 0.62334 | 0.757416 | 0.851869 | 0.180822 |
| tossup_correctness | category | Philosophy | 1649 | 0.672104 | 0.492607 | 0.0274453 | 0.158697 | 0.790176 | 0.77926 | 0.0109157 | 0.094912 | 0.636317 | 0.786504 | 0.872033 | 0.169187 |
| tossup_correctness | category | Popular Culture | 538 | 0.598144 | 0.427662 | 0.108705 | 0.129102 | 0.864312 | 0.864312 | 0 | 0.0790537 | 0.644359 | 0.760919 | 0.851833 | 0.178416 |
| tossup_correctness | category | Religion | 1889 | 0.690078 | 0.547773 | 0.0353825 | 0.183043 | 0.730016 | 0.724722 | 0.00529381 | 0.0945876 | 0.626533 | 0.773786 | 0.863793 | 0.174774 |
| tossup_correctness | category | Science | 7556 | 0.667362 | 0.528029 | 0.028119 | 0.173881 | 0.757544 | 0.754235 | 0.00330863 | 0.0874986 | 0.659176 | 0.791962 | 0.877354 | 0.164686 |
| tossup_correctness | category | Social Science | 1711 | 0.646793 | 0.567717 | 0.0358571 | 0.189697 | 0.728814 | 0.722385 | 0.00642899 | 0.0914301 | 0.638763 | 0.767818 | 0.87001 | 0.174952 |
| tossup_correctness | category | Unknown | 10202 | 0.655768 | 0.523878 | 0.0139978 | 0.171838 | 0.764556 | 0.758969 | 0.00558714 | 0.0970989 | 0.642002 | 0.789486 | 0.881784 | 0.166061 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.687133 | 0.553595 | 0.0837066 | 0.184468 | 0.755037 | 0.727466 | 0.0275716 | 0.111904 | 0.508567 | 0.666956 | 0.801093 | 0.211719 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.686899 | 0.53857 | 0.0462848 | 0.178713 | 0.748819 | 0.736496 | 0.0123229 | 0.106522 | 0.554359 | 0.709303 | 0.826477 | 0.199776 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.689854 | 0.511788 | 0.0290967 | 0.167748 | 0.764629 | 0.761053 | 0.00357548 | 0.0947397 | 0.618629 | 0.755888 | 0.858255 | 0.18107 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.691278 | 0.483619 | 0.030005 | 0.155684 | 0.787562 | 0.786033 | 0.00152976 | 0.0803065 | 0.672769 | 0.788281 | 0.873336 | 0.165668 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.639725 | 0.529287 | 0.0503062 | 0.17309 | 0.766154 | 0.765769 | 0.000384615 | 0.0684709 | 0.725814 | 0.82471 | 0.895985 | 0.145408 |
| bonus_part_correctness | aggregate | all | 133461 | 0.936141 | 0.331058 | 0.0382418 | 0.10349 | 0.853987 | 0.520489 | 0.333498 | 0.360323 | 0.0432157 | 0.453928 | 0.969606 | 0.120092 |
| bonus_part_correctness | tier | fall | 42336 | 0.928006 | 0.339147 | 0.0302286 | 0.107512 | 0.845002 | 0.598828 | 0.246173 | 0.351459 | 0.0753707 | 0.616116 | 0.984972 | 0.120981 |
| bonus_part_correctness | tier | nationals | 21051 | 0.945336 | 0.317023 | 0.0553168 | 0.0972663 | 0.865232 | 0.428911 | 0.436321 | 0.342184 | 0.0337022 | 0.267189 | 0.919369 | 0.121113 |
| bonus_part_correctness | tier | regionals | 27762 | 0.942261 | 0.321139 | 0.0466617 | 0.0993857 | 0.861898 | 0.483611 | 0.378287 | 0.357524 | 0.0353135 | 0.364454 | 0.952685 | 0.119608 |
| bonus_part_correctness | tier | winter | 42312 | 0.932698 | 0.336455 | 0.03224 | 0.105255 | 0.852193 | 0.511864 | 0.340329 | 0.361642 | 0.0412907 | 0.435603 | 0.967748 | 0.119011 |
| bonus_part_correctness | category | Current Events | 1281 | 0.937221 | 0.327924 | 0.0438493 | 0.101694 | 0.862607 | 0.501952 | 0.360656 | 0.369154 | 0.0368269 | 0.425691 | 0.958754 | 0.112857 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.926043 | 0.353497 | 0.0372035 | 0.111229 | 0.843221 | 0.507697 | 0.335523 | 0.351516 | 0.0472497 | 0.430204 | 0.96449 | 0.125947 |
| bonus_part_correctness | category | Geography | 2427 | 0.929073 | 0.340172 | 0.0396171 | 0.107246 | 0.853317 | 0.60033 | 0.252987 | 0.351582 | 0.056106 | 0.619856 | 0.977899 | 0.122102 |
| bonus_part_correctness | category | History | 21273 | 0.935543 | 0.329738 | 0.0356457 | 0.103424 | 0.852207 | 0.555446 | 0.296761 | 0.359585 | 0.0470001 | 0.540968 | 0.976623 | 0.119942 |
| bonus_part_correctness | category | Literature | 21312 | 0.942014 | 0.316391 | 0.0375433 | 0.0980426 | 0.862847 | 0.515813 | 0.347035 | 0.36611 | 0.0446783 | 0.434024 | 0.974643 | 0.11584 |
| bonus_part_correctness | category | Mythology | 4923 | 0.914763 | 0.364638 | 0.034824 | 0.116768 | 0.828763 | 0.617713 | 0.21105 | 0.331812 | 0.103975 | 0.618347 | 0.980972 | 0.132315 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.947165 | 0.302384 | 0.0417922 | 0.092827 | 0.871069 | 0.522799 | 0.34827 | 0.373228 | 0.0313648 | 0.497313 | 0.971005 | 0.110686 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.927718 | 0.351254 | 0.0411235 | 0.110484 | 0.844257 | 0.491481 | 0.352776 | 0.349316 | 0.0465347 | 0.395745 | 0.956854 | 0.126579 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.91375 | 0.360921 | 0.0259092 | 0.116581 | 0.828125 | 0.622396 | 0.205729 | 0.338223 | 0.0945996 | 0.630832 | 0.989729 | 0.125826 |
| bonus_part_correctness | category | Religion | 5280 | 0.93358 | 0.335219 | 0.03625 | 0.105348 | 0.849432 | 0.505871 | 0.343561 | 0.361303 | 0.0345422 | 0.434474 | 0.963843 | 0.118962 |
| bonus_part_correctness | category | Science | 21183 | 0.934437 | 0.333293 | 0.0350975 | 0.104277 | 0.852523 | 0.529812 | 0.322712 | 0.361122 | 0.047584 | 0.47773 | 0.973017 | 0.11958 |
| bonus_part_correctness | category | Social Science | 4698 | 0.941775 | 0.310792 | 0.0326735 | 0.097365 | 0.861005 | 0.476799 | 0.384206 | 0.372573 | 0.0277356 | 0.331255 | 0.973314 | 0.109048 |
| bonus_part_correctness | category | Unknown | 27762 | 0.942261 | 0.321139 | 0.0466617 | 0.0993857 | 0.861898 | 0.483611 | 0.378287 | 0.357524 | 0.0353135 | 0.364454 | 0.952685 | 0.119608 |

## Posterior Predictive Checks

| stage | discrepancy | stratum | observed | replicated_mean | replicated_p05 | replicated_p95 | posterior_predictive_p_value | draws |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| compositional | bonus_score_mass | 0 | 0.074 | 0.0658 | 0.0519 | 0.082 | 0.3 | 20 |
| compositional | bonus_score_mass | 10 | 0.442 | 0.4285 | 0.3998 | 0.4586 | 0.2 | 20 |
| compositional | bonus_score_mass | 20 | 0.378 | 0.4118 | 0.3879 | 0.4462 | 1 | 20 |
| compositional | bonus_score_mass | 30 | 0.106 | 0.0939 | 0.0738 | 0.1161 | 0.15 | 20 |
| pyramidal | buzz_position_mass | Q1 | 0.0162602 | 0.0669732 | 0.0510337 | 0.0903712 | 1 | 20 |
| pyramidal | buzz_position_mass | Q2 | 0.0934959 | 0.0954916 | 0.075213 | 0.112045 | 0.6 | 20 |
| pyramidal | buzz_position_mass | Q3 | 0.25813 | 0.210521 | 0.187023 | 0.23371 | 0 | 20 |
| pyramidal | buzz_position_mass | Q4 | 0.329268 | 0.325247 | 0.30453 | 0.346334 | 0.4 | 20 |
| pyramidal | buzz_position_mass | Q5 | 0.302846 | 0.301767 | 0.28054 | 0.330081 | 0.4 | 20 |
| pyramidal | dead_tossup_rate | all | 0.016 | 0.0627 | 0.0495 | 0.0821 | 1 | 20 |
| pyramidal | neg_rate | all | 0.254065 | 0.236095 | 0.197042 | 0.270536 | 0.3 | 20 |
| pyramidal | player_neg_rate | alec-riso | 0 | 0.104167 | 0 | 0.441667 | 1 | 8 |
| pyramidal | player_neg_rate | andrew-kelley | 0 | 0 | 0 | 0 | 1 | 1 |
| pyramidal | player_neg_rate | arhith-dharanendra | 0.666667 | 0 | 0 | 0 | 0 | 1 |
| pyramidal | player_neg_rate | arunn-sankar | 0.25 | 0.233333 | 0 | 0.466667 | 0.6 | 5 |
| pyramidal | player_neg_rate | biniam-alaro | 0 | 0.333333 | 0.0333333 | 0.633333 | 1 | 2 |
| pyramidal | player_neg_rate | caleb-kendrick | 0 | 0.227273 | 0 | 0.5 | 1 | 11 |
| pyramidal | player_neg_rate | cormac-beirne | 0 | 0.134615 | 0 | 0.666667 | 1 | 13 |
| pyramidal | player_neg_rate | daniel-chen | 0.666667 | 0.444444 | 0.333333 | 0.633333 | 0.333333 | 3 |
| pyramidal | player_neg_rate | henry-bylinowski | 0.4 | 0.0909091 | 0 | 0.291667 | 0 | 11 |
| pyramidal | player_neg_rate | jack-rado | 0 | 0.241667 | 0 | 0.666667 | 1 | 10 |
| pyramidal | player_neg_rate | jason-zhang | 0 | 0.291667 | 0.254167 | 0.329167 | 1 | 2 |
| pyramidal | player_neg_rate | jonathan-shauf | 0.333333 | 0.238095 | 0 | 0.566667 | 0.571429 | 7 |
| pyramidal | player_neg_rate | kevin-park | 0.333333 | 0.166667 | 0 | 0.333333 | 0.5 | 6 |
| pyramidal | player_neg_rate | liam-starnes | 0.333333 | 0.291667 | 0.254167 | 0.329167 | 0.5 | 2 |
| pyramidal | player_neg_rate | malachi-ledford | 0 | 0.32381 | 0 | 0.7 | 1 | 13 |
| pyramidal | player_neg_rate | michal-gerasimiuk | 0.666667 | 0.15625 | 0 | 0.55 | 0.125 | 8 |
| pyramidal | player_neg_rate | omer-keskin | 0 | 0.17 | 0 | 0.425 | 1 | 10 |
| pyramidal | player_neg_rate | orion-keller | 0 | 0.252778 | 0 | 0.666667 | 1 | 12 |
| pyramidal | player_neg_rate | owen-ashbrook | 0 | 0.4 | 0.4 | 0.4 | 1 | 1 |
| pyramidal | player_neg_rate | patrick-torre | 0 | 0.416667 | 0.05 | 0.666667 | 1 | 4 |
| pyramidal | player_neg_rate | rohan-dalal | 0.25 | 0.22619 | 0 | 0.691667 | 0.466667 | 15 |
| pyramidal | player_neg_rate | rosie-zhang | 0.333333 | 0.333333 | 0.333333 | 0.333333 | 1 | 1 |
| pyramidal | player_neg_rate | sam-macchi | 0 | 0.45 | 0.266667 | 0.666667 | 1 | 5 |
| pyramidal | player_neg_rate | shardul-rao | 0.6 | 0.125 | 0.0125 | 0.2375 | 0 | 2 |
| pyramidal | player_neg_rate | sinecio-morales | 0 | 0 | 0 | 0 | 1 | 3 |
| pyramidal | player_neg_rate | stella-brown | 0.333333 | 0 | 0 | 0 | 0 | 1 |
| pyramidal | player_neg_rate | teigue-kelly | 0.333333 | 0 | 0 | 0 | 0 | 2 |
| pyramidal | player_neg_rate | william-orr | 0 | 0.190476 | 0 | 0.566667 | 1 | 7 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.936141 | 0.936291 | 0.000149888 | synergy |
| log_loss | 0.331058 | 0.330929 | -0.000128668 | synergy |
| ece | 0.0382418 | 0.037406 | -0.000835819 | synergy |
| brier | 0.10349 | 0.102833 | -0.000657292 | synergy |
| accuracy_lift_over_all_correct | 0.333498 | 0.335237 | 0.00173834 | synergy |
| part_accuracy | 0.853987 | 0.855726 | 0.00173834 | synergy |
| part_accuracy_macro_team | 0.856057 | 0.858083 | 0.00202585 | synergy |
| part_accuracy_macro_game | 0.854284 | 0.856058 | 0.00177425 | synergy |
| part_accuracy_macro_bonus | 0.861529 | 0.860165 | -0.00136367 | no-synergy |
| exact_acc | 0.61591 | 0.620586 | 0.00467552 | synergy |
| ranked_probability_score | 0.0941761 | 0.0920475 | -0.00212862 | synergy |
| bonus_total_score_log_loss | 0.838958 | 0.828797 | -0.0101609 | synergy |
| ppb_mae | 1.52347 | 0.86116 | -0.66231 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 0.92243 | 0.68624 | -2.00637 | -0.236352 | 0.513703 | 0.89398 | 1.32605 | 2.05122 | 3.99296 |
| player | theta_1 | 1455 | -0.318297 | 0.620208 | -2.11265 | -1.36203 | -0.724307 | -0.285834 | 0.107053 | 0.683286 | 1.35884 |
| player | theta_2 | 1455 | -0.544197 | 0.660279 | -2.62173 | -1.63752 | -0.999509 | -0.546412 | -0.059649 | 0.536743 | 1.28957 |
| player | theta_3 | 1455 | -0.376151 | 0.670758 | -2.55483 | -1.4467 | -0.860124 | -0.368892 | 0.0863452 | 0.741453 | 1.66749 |
| player | theta_4 | 1455 | -0.365854 | 0.619832 | -2.97902 | -1.3722 | -0.791978 | -0.361685 | 0.0615182 | 0.651666 | 1.47326 |
| player | theta_5 | 1455 | -0.461707 | 0.611735 | -2.34887 | -1.46216 | -0.860956 | -0.480121 | -0.0490942 | 0.516115 | 1.46659 |
| player | theta_norm | 1455 | 1.62195 | 0.531979 | 0.20058 | 0.793185 | 1.23665 | 1.61493 | 2.00493 | 2.54005 | 3.48353 |
| tossup | beta_1 | 1260 | 0.861065 | 0.449273 | -0.318857 | 0.3104 | 0.558046 | 0.754328 | 1.0959 | 1.74695 | 3.6387 |
| tossup | beta_2 | 1260 | 0.958252 | 0.537212 | -0.337806 | 0.282582 | 0.547261 | 0.819133 | 1.33032 | 1.92499 | 3.16618 |
| tossup | beta_3 | 1260 | 0.890807 | 0.516699 | -0.221309 | 0.297358 | 0.532158 | 0.72841 | 1.15486 | 1.88667 | 3.68116 |
| tossup | beta_4 | 1260 | 0.950943 | 0.50881 | -0.389747 | 0.337072 | 0.563476 | 0.815805 | 1.28136 | 1.89618 | 3.06184 |
| tossup | beta_5 | 1260 | 0.887633 | 0.507007 | -0.228542 | 0.315943 | 0.542273 | 0.755075 | 1.13453 | 1.84072 | 3.92602 |
| tossup | gamma_1 | 1260 | 14.0648 | 63.3886 | 0.938455 | 2.55415 | 3.91273 | 4.87588 | 5.99562 | 20.2782 | 1040.05 |
| tossup | gamma_2 | 1260 | 19.3022 | 83.7804 | 0.488869 | 2.7849 | 4.1661 | 5.12073 | 6.77039 | 32.4124 | 1056.73 |
| tossup | gamma_3 | 1260 | 21.2664 | 99.6381 | 1.36696 | 2.95653 | 4.08711 | 5.00341 | 6.35078 | 33.9034 | 1509.72 |
| tossup | gamma_4 | 1260 | 19.229 | 93.6178 | 1.03945 | 2.8738 | 4.04224 | 5.07567 | 6.99453 | 28.9506 | 1658.59 |
| tossup | gamma_5 | 1260 | 17.2275 | 78.4381 | 0.929284 | 2.68183 | 3.91089 | 4.93505 | 6.4143 | 29.9432 | 1232.73 |
| tossup | mu_1 | 1260 | 0.546819 | 0.124294 | 0.209211 | 0.395988 | 0.472384 | 0.513265 | 0.602542 | 0.795511 | 0.991732 |
| tossup | mu_2 | 1260 | 0.565357 | 0.143312 | 0.184419 | 0.409392 | 0.463956 | 0.51996 | 0.643545 | 0.865374 | 0.993681 |
| tossup | mu_3 | 1260 | 0.556503 | 0.139592 | 0.238918 | 0.410884 | 0.464228 | 0.511282 | 0.617398 | 0.873776 | 0.989589 |
| tossup | mu_4 | 1260 | 0.573316 | 0.147744 | 0.142884 | 0.407901 | 0.46931 | 0.524163 | 0.656277 | 0.89104 | 0.99319 |
| tossup | mu_5 | 1260 | 0.551824 | 0.128476 | 0.224905 | 0.403817 | 0.468079 | 0.513806 | 0.614905 | 0.80051 | 0.992586 |
| tossup | r_1 | 1260 | 1.23978 | 0.745452 | 0.124448 | 0.316083 | 0.666529 | 1.10049 | 1.64009 | 2.67502 | 4.04237 |
| tossup | r_2 | 1260 | 1.36364 | 0.807752 | 0.106206 | 0.347007 | 0.759183 | 1.15229 | 1.84609 | 2.90243 | 3.87477 |
| tossup | r_3 | 1260 | 1.26294 | 0.836967 | 0.0739993 | 0.335806 | 0.655869 | 1.0072 | 1.5854 | 3.03323 | 4.4989 |
| tossup | r_4 | 1260 | 1.42758 | 0.921802 | 0.124671 | 0.376616 | 0.709946 | 1.12325 | 1.99377 | 3.21066 | 5.36964 |
| tossup | r_5 | 1260 | 1.21018 | 0.656682 | 0.0872471 | 0.30963 | 0.702616 | 1.11401 | 1.624 | 2.44052 | 3.57261 |
| tossup | r_norm | 1260 | 3.34581 | 0.697984 | 1.56506 | 2.23764 | 2.86166 | 3.31953 | 3.78981 | 4.53484 | 6.36193 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.00486959 | 1.20638 | -2.38745 | -1.77726 | -1.05824 | -0.0751058 | 0.977561 | 1.97416 | 2.57619 |
| bonus_part | alpha_1 | 3768 | 0.311628 | 0.571649 | -1.58114 | -0.575228 | -0.0347003 | 0.235028 | 0.632338 | 1.37558 | 2.78366 |
| bonus_part | alpha_2 | 3768 | 0.217704 | 0.646909 | -1.91712 | -0.921245 | -0.239394 | 0.328296 | 0.691344 | 1.12699 | 2.34589 |
| bonus_part | alpha_3 | 3768 | 0.216465 | 0.595695 | -1.7901 | -0.724587 | -0.185877 | 0.23641 | 0.568273 | 1.23802 | 2.52146 |
| bonus_part | alpha_4 | 3768 | 0.30966 | 0.615106 | -1.77535 | -0.66351 | -0.0833034 | 0.268832 | 0.672943 | 1.40937 | 2.53851 |
| bonus_part | alpha_5 | 3768 | 0.19317 | 0.59353 | -1.68227 | -0.818546 | -0.230247 | 0.255307 | 0.61671 | 1.09612 | 1.93275 |
| bonus_part | alpha_norm | 3768 | 1.37321 | 0.518856 | 0.126299 | 0.581961 | 1.00773 | 1.32963 | 1.70292 | 2.32089 | 3.35904 |
