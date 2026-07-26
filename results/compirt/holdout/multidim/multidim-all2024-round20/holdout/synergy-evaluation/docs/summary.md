# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/multidim-all2024-round20/holdout/synergy-evaluation`
Result root: `results/compirt/holdout/multidim-all2024-round20`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 58402.2 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 13444.4 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.225623 |
| mean_synergy_contribution | -0.486045 |
| median_synergy_contribution | -0.331023 |
| negative_synergy_fraction | 0.730082 |
| positive_synergy_fraction | 0.240573 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.950372 |
| log_loss | 0.337456 |
| ece | 0.096014 |
| brier | 0.101071 |
| part_accuracy | 0.869105 |
| part_all_correct_accuracy | 0.509829 |
| accuracy_lift_over_all_correct | 0.359276 |
| part_accuracy_macro_team | 0.87753 |
| part_accuracy_macro_game | 0.869829 |
| part_accuracy_macro_bonus | 0.879982 |
| probability_std | 0.318428 |
| probability_p10 | 0.0639274 |
| probability_p50 | 0.422935 |
| probability_p90 | 0.903017 |
| mean_predictive_variance | 0.146904 |
| exact_acc | 0.65438 |
| ranked_probability_score | 0.0906584 |
| bonus_total_score_log_loss | 0.831634 |
| ppb_mae | 1.8091 |
| ranked_probability_score_responses | 7054 |
| bonus_total_score_log_loss_responses | 7054 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.691036 |
| log_loss | 0.596193 |
| ece | 0.133886 |
| brier | 0.200237 |
| accuracy | 0.70701 |
| all_correct_accuracy | 0.754791 |
| accuracy_lift_over_all_correct | -0.0477816 |
| probability_std | 0.249098 |
| probability_p10 | 0.235105 |
| probability_p50 | 0.68194 |
| probability_p90 | 0.910628 |
| mean_predictive_variance | 0.172049 |
| integrated_brier_score | 0.0809954 |
| joint_tossup_event_log_loss | 6.10918 |
| buzz_position_mae | 0.129597 |
| buzz_position_median_absolute_error | 0.109263 |
| buzz_position_bias | -0.0479821 |
| survival_events | 7740 |
| joint_tossup_event_log_loss_events | 7740 |
| first_buzzer_top1_accuracy | 0.490024 |
| first_buzzer_mean_reciprocal_rank | 0.677516 |
| first_buzzer_log_loss | 1.35285 |
| first_buzzer_events | 7618 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.75 |
| match_winner_brier | 0.162926 |
| match_games | 384 |
| match_simulations_per_game | 500 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 7618 | 0.691036 | 0.596193 | 0.133886 | 0.200237 | 0.70701 | 0.754791 | -0.0477816 | 0.249098 | 0.235105 | 0.68194 | 0.910628 | 0.172049 |
| tossup_correctness | tier | fall | 2044 | 0.688582 | 0.604007 | 0.159288 | 0.204428 | 0.695205 | 0.764677 | -0.0694716 | 0.243253 | 0.225687 | 0.656072 | 0.890821 | 0.17962 |
| tossup_correctness | tier | nationals | 1870 | 0.65859 | 0.643291 | 0.110468 | 0.217795 | 0.680749 | 0.707487 | -0.026738 | 0.257823 | 0.240598 | 0.716402 | 0.934036 | 0.161181 |
| tossup_correctness | tier | regionals | 1376 | 0.727185 | 0.546883 | 0.123589 | 0.181342 | 0.742733 | 0.763081 | -0.0203488 | 0.240032 | 0.265157 | 0.697939 | 0.905491 | 0.172926 |
| tossup_correctness | tier | winter | 2328 | 0.71947 | 0.580645 | 0.162051 | 0.19362 | 0.717354 | 0.77921 | -0.0618557 | 0.25032 | 0.224532 | 0.674879 | 0.906303 | 0.173614 |
| tossup_correctness | category | Current Events | 95 | 0.647715 | 0.630094 | 0.193034 | 0.219976 | 0.652632 | 0.726316 | -0.0736842 | 0.239098 | 0.277675 | 0.679383 | 0.885407 | 0.178574 |
| tossup_correctness | category | Fine Arts | 936 | 0.685671 | 0.619078 | 0.165827 | 0.209083 | 0.683761 | 0.753205 | -0.0694444 | 0.257558 | 0.20286 | 0.658295 | 0.909653 | 0.173454 |
| tossup_correctness | category | Geography | 182 | 0.639031 | 0.695349 | 0.128629 | 0.248373 | 0.593407 | 0.615385 | -0.021978 | 0.238056 | 0.19961 | 0.574928 | 0.810382 | 0.192658 |
| tossup_correctness | category | History | 1258 | 0.657603 | 0.636513 | 0.137405 | 0.214777 | 0.687599 | 0.745628 | -0.0580286 | 0.25217 | 0.230261 | 0.691752 | 0.910278 | 0.170993 |
| tossup_correctness | category | Literature | 1229 | 0.692454 | 0.573148 | 0.131428 | 0.190012 | 0.728234 | 0.787632 | -0.0593979 | 0.246185 | 0.272659 | 0.722232 | 0.924779 | 0.164777 |
| tossup_correctness | category | Mythology | 269 | 0.662831 | 0.601796 | 0.219128 | 0.202232 | 0.717472 | 0.814126 | -0.0966543 | 0.246991 | 0.231706 | 0.656678 | 0.910059 | 0.175378 |
| tossup_correctness | category | Other Academic | 75 | 0.583686 | 0.694079 | 0.187369 | 0.232933 | 0.653333 | 0.786667 | -0.133333 | 0.244957 | 0.216513 | 0.682796 | 0.874967 | 0.17529 |
| tossup_correctness | category | Philosophy | 257 | 0.665344 | 0.619557 | 0.139065 | 0.208433 | 0.696498 | 0.735409 | -0.0389105 | 0.247058 | 0.218303 | 0.66602 | 0.905212 | 0.173751 |
| tossup_correctness | category | Popular Culture | 73 | 0.640762 | 0.77683 | 0.329785 | 0.269316 | 0.589041 | 0.849315 | -0.260274 | 0.250919 | 0.17034 | 0.538833 | 0.835177 | 0.186658 |
| tossup_correctness | category | Religion | 314 | 0.725397 | 0.566584 | 0.120118 | 0.191399 | 0.713376 | 0.748408 | -0.0350318 | 0.262114 | 0.203864 | 0.690431 | 0.926085 | 0.164838 |
| tossup_correctness | category | Science | 1252 | 0.703939 | 0.587487 | 0.109677 | 0.196341 | 0.717252 | 0.729233 | -0.0119808 | 0.245975 | 0.245009 | 0.680433 | 0.917314 | 0.172687 |
| tossup_correctness | category | Social Science | 302 | 0.714956 | 0.57937 | 0.156256 | 0.196496 | 0.688742 | 0.764901 | -0.0761589 | 0.242646 | 0.22386 | 0.679158 | 0.870795 | 0.179319 |
| tossup_correctness | category | Unknown | 1376 | 0.727185 | 0.546883 | 0.123589 | 0.181342 | 0.742733 | 0.763081 | -0.0203488 | 0.240032 | 0.265157 | 0.697939 | 0.905491 | 0.172926 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 125 | 0.715366 | 0.802629 | 0.309199 | 0.286589 | 0.568 | 0.696 | -0.128 | 0.22736 | 0.0924874 | 0.369738 | 0.714125 | 0.185493 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 769 | 0.745946 | 0.753157 | 0.288615 | 0.262748 | 0.596879 | 0.712614 | -0.115735 | 0.240916 | 0.107205 | 0.406317 | 0.758898 | 0.186183 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 1822 | 0.697293 | 0.648229 | 0.204327 | 0.220032 | 0.675082 | 0.767838 | -0.0927552 | 0.245337 | 0.189106 | 0.60079 | 0.86989 | 0.185776 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2322 | 0.714774 | 0.544207 | 0.109272 | 0.181753 | 0.732989 | 0.760982 | -0.0279931 | 0.235253 | 0.29089 | 0.705382 | 0.913963 | 0.17164 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2580 | 0.677748 | 0.549446 | 0.0626942 | 0.180077 | 0.745736 | 0.755426 | -0.00968992 | 0.210106 | 0.407064 | 0.773272 | 0.935692 | 0.157859 |
| bonus_part_correctness | aggregate | all | 21162 | 0.950372 | 0.337456 | 0.096014 | 0.101071 | 0.869105 | 0.509829 | 0.359276 | 0.318428 | 0.0639274 | 0.422935 | 0.903017 | 0.146904 |
| bonus_part_correctness | tier | fall | 5877 | 0.94427 | 0.351657 | 0.0974791 | 0.104783 | 0.869151 | 0.620895 | 0.248256 | 0.295565 | 0.13326 | 0.61506 | 0.925926 | 0.158533 |
| bonus_part_correctness | tier | nationals | 4923 | 0.946681 | 0.311085 | 0.0608784 | 0.0951556 | 0.865935 | 0.399959 | 0.465976 | 0.334351 | 0.0334824 | 0.227459 | 0.898811 | 0.121026 |
| bonus_part_correctness | tier | regionals | 3873 | 0.959981 | 0.332733 | 0.120575 | 0.098915 | 0.870901 | 0.50142 | 0.369481 | 0.312319 | 0.0761313 | 0.384125 | 0.904645 | 0.149352 |
| bonus_part_correctness | tier | winter | 6489 | 0.952876 | 0.347418 | 0.11791 | 0.103484 | 0.870396 | 0.497611 | 0.372785 | 0.303121 | 0.0766013 | 0.387008 | 0.872323 | 0.154544 |
| bonus_part_correctness | category | Current Events | 189 | 0.964778 | 0.319765 | 0.133519 | 0.0917641 | 0.883598 | 0.544974 | 0.338624 | 0.31036 | 0.12047 | 0.526436 | 0.909863 | 0.153661 |
| bonus_part_correctness | category | Fine Arts | 2508 | 0.941309 | 0.356952 | 0.0881022 | 0.108724 | 0.854864 | 0.48126 | 0.373604 | 0.304374 | 0.0622775 | 0.394733 | 0.865145 | 0.153407 |
| bonus_part_correctness | category | Geography | 363 | 0.948083 | 0.348042 | 0.108781 | 0.105313 | 0.865014 | 0.575758 | 0.289256 | 0.31169 | 0.0602732 | 0.568097 | 0.888259 | 0.152843 |
| bonus_part_correctness | category | History | 3456 | 0.94476 | 0.347143 | 0.0935288 | 0.104714 | 0.864005 | 0.543113 | 0.320891 | 0.316305 | 0.0577 | 0.505835 | 0.896141 | 0.149746 |
| bonus_part_correctness | category | Literature | 3555 | 0.952436 | 0.328382 | 0.0899118 | 0.0975041 | 0.877918 | 0.491139 | 0.386779 | 0.321906 | 0.0608708 | 0.392465 | 0.905536 | 0.143568 |
| bonus_part_correctness | category | Mythology | 777 | 0.939167 | 0.358299 | 0.102924 | 0.107371 | 0.866152 | 0.580438 | 0.285714 | 0.308389 | 0.0846843 | 0.569444 | 0.895224 | 0.154616 |
| bonus_part_correctness | category | Other Academic | 249 | 0.964711 | 0.275568 | 0.0969429 | 0.0808033 | 0.891566 | 0.46988 | 0.421687 | 0.343967 | 0.0271112 | 0.437548 | 0.905273 | 0.127773 |
| bonus_part_correctness | category | Philosophy | 858 | 0.957101 | 0.313674 | 0.0900735 | 0.0934524 | 0.875291 | 0.454545 | 0.420746 | 0.327601 | 0.0527893 | 0.304033 | 0.914321 | 0.134912 |
| bonus_part_correctness | category | Popular Culture | 204 | 0.937857 | 0.329408 | 0.086462 | 0.100617 | 0.872549 | 0.676471 | 0.196078 | 0.305679 | 0.158006 | 0.704196 | 0.954735 | 0.14019 |
| bonus_part_correctness | category | Religion | 870 | 0.941502 | 0.348156 | 0.0858637 | 0.105582 | 0.85977 | 0.497701 | 0.362069 | 0.317021 | 0.0588671 | 0.460704 | 0.892194 | 0.147204 |
| bonus_part_correctness | category | Science | 3468 | 0.949688 | 0.33604 | 0.0920057 | 0.100448 | 0.8688 | 0.516436 | 0.352364 | 0.323037 | 0.0655739 | 0.413635 | 0.907221 | 0.144313 |
| bonus_part_correctness | category | Social Science | 792 | 0.952602 | 0.317924 | 0.0850555 | 0.0941069 | 0.886364 | 0.486111 | 0.400253 | 0.332525 | 0.0589556 | 0.346126 | 0.920856 | 0.136765 |
| bonus_part_correctness | category | Unknown | 3873 | 0.959981 | 0.332733 | 0.120575 | 0.098915 | 0.870901 | 0.50142 | 0.369481 | 0.312319 | 0.0761313 | 0.384125 | 0.904645 | 0.149352 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.939166 | 0.950372 | 0.0112067 | synergy |
| log_loss | 0.362611 | 0.337456 | -0.0251551 | synergy |
| ece | 0.0919266 | 0.096014 | 0.00408742 | no-synergy |
| brier | 0.108595 | 0.101071 | -0.00752427 | synergy |
| accuracy_lift_over_all_correct | 0.352141 | 0.359276 | 0.00713543 | synergy |
| part_accuracy | 0.86197 | 0.869105 | 0.00713543 | synergy |
| part_accuracy_macro_team | 0.869828 | 0.87753 | 0.00770237 | synergy |
| part_accuracy_macro_game | 0.86287 | 0.869829 | 0.00695924 | synergy |
| part_accuracy_macro_bonus | 0.896265 | 0.879982 | -0.0162821 | no-synergy |
| exact_acc | 0.635526 | 0.65438 | 0.0188546 | synergy |
| ranked_probability_score | 0.0993972 | 0.0906584 | -0.0087388 | synergy |
| bonus_total_score_log_loss | 0.892599 | 0.831634 | -0.0609647 | synergy |
| ppb_mae | 2.45854 | 1.8091 | -0.649441 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1131 | 4.69859 | 1.14525 | 1.21344 | 2.17571 | 4.14885 | 4.94176 | 5.45052 | 6.16422 | 7.04665 |
| player | theta_1 | 1131 | 0.0747444 | 0.736661 | -2.12283 | -1.3902 | -0.319613 | 0.165051 | 0.618513 | 1.1104 | 1.66469 |
| player | theta_2 | 1131 | 0.0995677 | 0.788887 | -2.6601 | -1.38224 | -0.365147 | 0.191033 | 0.682575 | 1.27167 | 1.9086 |
| player | theta_3 | 1131 | 0.0199035 | 0.738216 | -2.66044 | -1.44795 | -0.351983 | 0.136404 | 0.535676 | 1.05435 | 2.36883 |
| player | theta_4 | 1131 | -0.0345205 | 0.778002 | -2.90485 | -1.52215 | -0.434848 | 0.105827 | 0.512463 | 1.02791 | 2.16995 |
| player | theta_5 | 1131 | 0.150223 | 0.759025 | -2.61985 | -1.35624 | -0.255629 | 0.240431 | 0.674521 | 1.25554 | 1.86206 |
| player | theta_norm | 1131 | 1.59824 | 0.611911 | 0.277331 | 0.763089 | 1.1601 | 1.50528 | 1.94377 | 2.79785 | 3.73984 |
| tossup | beta_1 | 780 | 0.84932 | 0.469197 | -0.215746 | 0.328066 | 0.526108 | 0.709413 | 1.03645 | 1.82534 | 2.77972 |
| tossup | beta_2 | 780 | 0.767594 | 0.431265 | -0.19746 | 0.290089 | 0.49977 | 0.65178 | 0.878446 | 1.77767 | 2.5673 |
| tossup | beta_3 | 780 | 0.746746 | 0.389808 | -0.164675 | 0.305197 | 0.503371 | 0.649451 | 0.869676 | 1.57967 | 2.5656 |
| tossup | beta_4 | 780 | 0.753227 | 0.392912 | -0.141923 | 0.318022 | 0.518506 | 0.670422 | 0.869235 | 1.6361 | 2.57456 |
| tossup | beta_5 | 780 | 0.77933 | 0.398727 | -0.422482 | 0.348036 | 0.530446 | 0.68634 | 0.91222 | 1.67012 | 2.38663 |
| tossup | gamma_1 | 780 | 9.68195 | 55.9872 | 1.32387 | 3.98229 | 4.73511 | 5.24688 | 6.18114 | 17.8034 | 1538.93 |
| tossup | gamma_2 | 780 | 6.93236 | 14.4531 | 1.8982 | 3.99948 | 4.66234 | 5.13336 | 5.78121 | 11.2549 | 324.744 |
| tossup | gamma_3 | 780 | 10.2281 | 60.1378 | 1.33758 | 3.76517 | 4.65676 | 5.11898 | 5.68677 | 10.2057 | 1419.22 |
| tossup | gamma_4 | 780 | 6.19279 | 6.81013 | 1.97827 | 3.85445 | 4.66783 | 5.12828 | 5.7066 | 10.3827 | 131.969 |
| tossup | gamma_5 | 780 | 5.98788 | 7.31782 | 2.07048 | 3.90076 | 4.60953 | 5.06398 | 5.62565 | 9.68149 | 168.382 |
| tossup | mu_1 | 780 | 0.517914 | 0.0923338 | 0.210773 | 0.425841 | 0.470146 | 0.497538 | 0.531969 | 0.724958 | 0.957754 |
| tossup | mu_2 | 780 | 0.511912 | 0.0845506 | 0.297874 | 0.426629 | 0.468847 | 0.493965 | 0.524475 | 0.694297 | 0.971329 |
| tossup | mu_3 | 780 | 0.507149 | 0.0767245 | 0.20067 | 0.428204 | 0.464396 | 0.491131 | 0.522788 | 0.666514 | 0.886898 |
| tossup | mu_4 | 780 | 0.50957 | 0.0777339 | 0.29837 | 0.429483 | 0.466658 | 0.49224 | 0.52554 | 0.672448 | 0.871283 |
| tossup | mu_5 | 780 | 0.515481 | 0.080337 | 0.25386 | 0.429317 | 0.472614 | 0.499497 | 0.535574 | 0.670311 | 0.962284 |
| tossup | r_1 | 780 | 1.00567 | 0.65883 | 0.123188 | 0.327528 | 0.537793 | 0.779907 | 1.27528 | 2.45545 | 3.44473 |
| tossup | r_2 | 780 | 0.903395 | 0.665404 | 0.147947 | 0.285693 | 0.487926 | 0.677287 | 1.00353 | 2.51204 | 3.67004 |
| tossup | r_3 | 780 | 0.909142 | 0.562921 | 0.132783 | 0.305052 | 0.529264 | 0.77072 | 1.10835 | 2.07604 | 3.80923 |
| tossup | r_4 | 780 | 0.923643 | 0.571637 | 0.126942 | 0.311944 | 0.547065 | 0.771402 | 1.09556 | 2.26079 | 3.25906 |
| tossup | r_5 | 780 | 0.936943 | 0.65005 | 0.116326 | 0.331707 | 0.526428 | 0.725208 | 1.08543 | 2.38633 | 4.36547 |
| tossup | r_norm | 780 | 2.43448 | 0.631956 | 1.05565 | 1.61593 | 1.91235 | 2.31875 | 2.84034 | 3.65676 | 4.67621 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 2304 | 0.275722 | 1.052 | -2.18156 | -1.39549 | -0.433126 | 0.27682 | 1.00942 | 2.12258 | 3.44096 |
| bonus_part | alpha_1 | 2304 | 0.0355017 | 0.301712 | -1.17752 | -0.450609 | -0.148225 | 0.0422523 | 0.206333 | 0.542736 | 1.50625 |
| bonus_part | alpha_2 | 2304 | 0.0238634 | 0.339965 | -1.6218 | -0.542945 | -0.175871 | 0.0352716 | 0.226487 | 0.572706 | 1.69374 |
| bonus_part | alpha_3 | 2304 | 0.0362144 | 0.309234 | -1.64416 | -0.464584 | -0.139194 | 0.0390114 | 0.217477 | 0.530375 | 1.35308 |
| bonus_part | alpha_4 | 2304 | 0.0447531 | 0.315744 | -1.71991 | -0.444667 | -0.137358 | 0.0484594 | 0.22481 | 0.546571 | 1.51488 |
| bonus_part | alpha_5 | 2304 | 0.0237249 | 0.379866 | -1.50615 | -0.595844 | -0.221068 | 0.0382498 | 0.240374 | 0.656217 | 1.42484 |
| bonus_part | alpha_norm | 2304 | 0.657545 | 0.345515 | 0.0657507 | 0.204943 | 0.397964 | 0.598864 | 0.864066 | 1.31297 | 2.13591 |
