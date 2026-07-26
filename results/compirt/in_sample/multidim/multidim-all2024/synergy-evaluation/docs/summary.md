# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/in_sample/multidim/multidim-all2024/synergy-evaluation`
Result root: `results/compirt/in_sample/multidim/multidim-all2024`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: in-sample fit.** Player and question parameters were estimated on the same observations these metrics score, so they are optimization and inspection diagnostics, not generalization estimates.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all 2024 |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 360025 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all 2024 |
| synergy | dimensions | 5 |
| synergy | steps | 2000 |
| synergy | final_loss | 65783.3 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.518057 |
| mean_synergy_contribution | -0.679848 |
| median_synergy_contribution | -0.646619 |
| negative_synergy_fraction | 0.769955 |
| positive_synergy_fraction | 0.198642 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.935559 |
| log_loss | 0.336424 |
| ece | 0.0437654 |
| brier | 0.104196 |
| part_accuracy | 0.854017 |
| part_all_correct_accuracy | 0.520489 |
| accuracy_lift_over_all_correct | 0.333528 |
| part_accuracy_macro_team | 0.857456 |
| part_accuracy_macro_bonus | 0.857878 |
| probability_std | 0.349271 |
| probability_p10 | 0.0560399 |
| probability_p50 | 0.463619 |
| probability_p90 | 0.95868 |
| mean_predictive_variance | 0.127983 |
| exact_acc | 0.614764 |
| ranked_probability_score | 0.0931524 |
| bonus_total_score_log_loss | 0.840351 |
| ppb_mae | 0.905 |
| ranked_probability_score_responses | 44487 |
| bonus_total_score_log_loss_responses | 44487 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.700325 |
| log_loss | 0.57645 |
| ece | 0.128749 |
| brier | 0.192849 |
| accuracy | 0.715302 |
| all_correct_accuracy | 0.767271 |
| accuracy_lift_over_all_correct | -0.0519681 |
| probability_std | 0.256321 |
| probability_p10 | 0.237035 |
| probability_p50 | 0.709465 |
| probability_p90 | 0.92861 |
| mean_predictive_variance | 0.163477 |
| integrated_brier_score | 0.085288 |
| joint_tossup_event_log_loss | 6.10421 |
| buzz_position_mae | 0.134659 |
| buzz_position_median_absolute_error | 0.115784 |
| buzz_position_bias | -0.0398828 |
| survival_events | 48612 |
| joint_tossup_event_log_loss_events | 48612 |
| first_buzzer_top1_accuracy | 0.47938 |
| first_buzzer_mean_reciprocal_rank | 0.670549 |
| first_buzzer_log_loss | 1.34399 |
| first_buzzer_events | 47914 |

## Match Winner Simulation

| metric | value |
| --- | --- |
| match_winner_accuracy | 0.808219 |
| match_winner_brier | 0.128797 |
| match_games | 2409 |
| match_simulations_per_game | 500 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 47914 | 0.700325 | 0.57645 | 0.128749 | 0.192849 | 0.715302 | 0.767271 | -0.0519681 | 0.256321 | 0.237035 | 0.709465 | 0.92861 | 0.163477 |
| tossup_correctness | tier | fall | 14760 | 0.70572 | 0.561576 | 0.143458 | 0.186969 | 0.72439 | 0.787466 | -0.0630759 | 0.253991 | 0.243996 | 0.711148 | 0.925278 | 0.164317 |
| tossup_correctness | tier | nationals | 7940 | 0.691216 | 0.58643 | 0.0904968 | 0.197388 | 0.706675 | 0.72733 | -0.0206549 | 0.249351 | 0.273071 | 0.736643 | 0.9388 | 0.159609 |
| tossup_correctness | tier | regionals | 10202 | 0.701128 | 0.583724 | 0.123581 | 0.194809 | 0.711429 | 0.758969 | -0.0475397 | 0.260262 | 0.229176 | 0.711791 | 0.932555 | 0.161282 |
| tossup_correctness | tier | winter | 15012 | 0.706701 | 0.580852 | 0.145523 | 0.194897 | 0.713562 | 0.774181 | -0.0606182 | 0.258562 | 0.222686 | 0.690158 | 0.922421 | 0.166189 |
| tossup_correctness | category | Current Events | 640 | 0.668661 | 0.621403 | 0.135781 | 0.213773 | 0.673438 | 0.734375 | -0.0609375 | 0.257388 | 0.18271 | 0.654167 | 0.901982 | 0.172606 |
| tossup_correctness | category | Fine Arts | 5640 | 0.703603 | 0.578562 | 0.136787 | 0.194849 | 0.709574 | 0.766489 | -0.0569149 | 0.258828 | 0.221364 | 0.695694 | 0.926731 | 0.165172 |
| tossup_correctness | category | Geography | 972 | 0.659361 | 0.660724 | 0.125307 | 0.232341 | 0.632716 | 0.675926 | -0.0432099 | 0.246039 | 0.2038 | 0.6001 | 0.870712 | 0.185861 |
| tossup_correctness | category | History | 7599 | 0.715954 | 0.553338 | 0.114515 | 0.183856 | 0.729438 | 0.764969 | -0.035531 | 0.25248 | 0.254849 | 0.723082 | 0.927855 | 0.162467 |
| tossup_correctness | category | Literature | 7469 | 0.677603 | 0.568442 | 0.145958 | 0.187592 | 0.728879 | 0.812157 | -0.0832775 | 0.256317 | 0.261858 | 0.752678 | 0.941625 | 0.154274 |
| tossup_correctness | category | Mythology | 1692 | 0.652222 | 0.631835 | 0.209866 | 0.213939 | 0.683215 | 0.80792 | -0.124704 | 0.248221 | 0.226421 | 0.654424 | 0.894169 | 0.177687 |
| tossup_correctness | category | Other Academic | 357 | 0.703448 | 0.586898 | 0.154439 | 0.197862 | 0.722689 | 0.756303 | -0.0336134 | 0.240471 | 0.226468 | 0.661095 | 0.868729 | 0.181798 |
| tossup_correctness | category | Philosophy | 1649 | 0.726333 | 0.547089 | 0.13629 | 0.183984 | 0.722256 | 0.77926 | -0.0570042 | 0.256484 | 0.235423 | 0.704448 | 0.926305 | 0.163775 |
| tossup_correctness | category | Popular Culture | 538 | 0.60545 | 0.737916 | 0.308739 | 0.252309 | 0.64684 | 0.864312 | -0.217472 | 0.24505 | 0.172937 | 0.592442 | 0.846479 | 0.186862 |
| tossup_correctness | category | Religion | 1889 | 0.715781 | 0.58688 | 0.117903 | 0.197633 | 0.700371 | 0.724722 | -0.0243515 | 0.261326 | 0.201283 | 0.673592 | 0.910189 | 0.16862 |
| tossup_correctness | category | Science | 7556 | 0.705795 | 0.560853 | 0.105061 | 0.187062 | 0.728295 | 0.754235 | -0.0259397 | 0.248699 | 0.267856 | 0.72136 | 0.933012 | 0.162849 |
| tossup_correctness | category | Social Science | 1711 | 0.723514 | 0.576966 | 0.108324 | 0.19541 | 0.701929 | 0.722385 | -0.0204559 | 0.256552 | 0.20773 | 0.677703 | 0.90919 | 0.171091 |
| tossup_correctness | category | Unknown | 10202 | 0.701128 | 0.583724 | 0.123581 | 0.194809 | 0.711429 | 0.758969 | -0.0475397 | 0.260262 | 0.229176 | 0.711791 | 0.932555 | 0.161282 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 943 | 0.744768 | 0.949603 | 0.383773 | 0.327888 | 0.502651 | 0.727466 | -0.224814 | 0.244478 | 0.049232 | 0.312351 | 0.703948 | 0.166215 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 4869 | 0.728459 | 0.783167 | 0.296392 | 0.271254 | 0.579791 | 0.736496 | -0.156706 | 0.264035 | 0.0898744 | 0.434194 | 0.813244 | 0.176755 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 11467 | 0.717273 | 0.617892 | 0.185283 | 0.210047 | 0.680126 | 0.761053 | -0.0809279 | 0.260011 | 0.184768 | 0.616373 | 0.893394 | 0.176653 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 15035 | 0.711255 | 0.520188 | 0.107127 | 0.172145 | 0.749052 | 0.786033 | -0.0369804 | 0.229639 | 0.331946 | 0.734975 | 0.931853 | 0.164798 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 15600 | 0.705167 | 0.513135 | 0.0529966 | 0.167527 | 0.763782 | 0.765769 | -0.00198718 | 0.208197 | 0.433402 | 0.803974 | 0.949268 | 0.148209 |
| bonus_part_correctness | aggregate | all | 133461 | 0.935559 | 0.336424 | 0.0437654 | 0.104196 | 0.854017 | 0.520489 | 0.333528 | 0.349271 | 0.0560399 | 0.463619 | 0.95868 | 0.127983 |
| bonus_part_correctness | tier | fall | 42336 | 0.925623 | 0.349121 | 0.0357081 | 0.109473 | 0.842049 | 0.598828 | 0.243221 | 0.336208 | 0.0968071 | 0.6283 | 0.966918 | 0.131157 |
| bonus_part_correctness | tier | nationals | 21051 | 0.944678 | 0.323589 | 0.0657616 | 0.0992411 | 0.863332 | 0.428911 | 0.434421 | 0.33526 | 0.039145 | 0.264685 | 0.908638 | 0.125025 |
| bonus_part_correctness | tier | regionals | 27762 | 0.942588 | 0.325298 | 0.0550532 | 0.0996818 | 0.863446 | 0.483611 | 0.379836 | 0.347518 | 0.0480946 | 0.376724 | 0.950387 | 0.127012 |
| bonus_part_correctness | tier | winter | 42312 | 0.933609 | 0.337405 | 0.0359545 | 0.104344 | 0.855171 | 0.511864 | 0.343307 | 0.350786 | 0.0573434 | 0.453306 | 0.96166 | 0.126917 |
| bonus_part_correctness | category | Current Events | 1281 | 0.93354 | 0.33847 | 0.0383892 | 0.104088 | 0.857143 | 0.501952 | 0.355191 | 0.356833 | 0.0488684 | 0.44645 | 0.947783 | 0.122048 |
| bonus_part_correctness | category | Fine Arts | 15525 | 0.925571 | 0.356621 | 0.0403131 | 0.111592 | 0.843156 | 0.507697 | 0.335459 | 0.34201 | 0.0586474 | 0.444927 | 0.952893 | 0.132785 |
| bonus_part_correctness | category | Geography | 2427 | 0.928613 | 0.34382 | 0.044587 | 0.107078 | 0.84796 | 0.60033 | 0.247631 | 0.339312 | 0.0719454 | 0.647943 | 0.964503 | 0.129826 |
| bonus_part_correctness | category | History | 21273 | 0.934193 | 0.337071 | 0.0421292 | 0.104799 | 0.851643 | 0.555446 | 0.296197 | 0.348443 | 0.0603437 | 0.5448 | 0.960981 | 0.127783 |
| bonus_part_correctness | category | Literature | 21312 | 0.939602 | 0.3267 | 0.0447473 | 0.100453 | 0.859985 | 0.515813 | 0.344172 | 0.351688 | 0.0585147 | 0.448152 | 0.962447 | 0.126271 |
| bonus_part_correctness | category | Mythology | 4923 | 0.915085 | 0.368271 | 0.0429416 | 0.116649 | 0.832419 | 0.617713 | 0.214706 | 0.322845 | 0.119173 | 0.637149 | 0.966435 | 0.138273 |
| bonus_part_correctness | category | Other Academic | 1272 | 0.948322 | 0.306015 | 0.0463663 | 0.0920423 | 0.872642 | 0.522799 | 0.349843 | 0.36426 | 0.040274 | 0.48193 | 0.961636 | 0.11726 |
| bonus_part_correctness | category | Philosophy | 4989 | 0.93137 | 0.347935 | 0.0514305 | 0.108273 | 0.847264 | 0.491481 | 0.355783 | 0.34001 | 0.0570669 | 0.4123 | 0.949296 | 0.133486 |
| bonus_part_correctness | category | Popular Culture | 1536 | 0.903389 | 0.38355 | 0.028445 | 0.123882 | 0.818359 | 0.622396 | 0.195964 | 0.32609 | 0.112588 | 0.648672 | 0.970949 | 0.134784 |
| bonus_part_correctness | category | Religion | 5280 | 0.936503 | 0.332068 | 0.041645 | 0.102911 | 0.853788 | 0.505871 | 0.347917 | 0.35536 | 0.0489874 | 0.44637 | 0.957421 | 0.123468 |
| bonus_part_correctness | category | Science | 21183 | 0.933551 | 0.338935 | 0.0390492 | 0.105122 | 0.851201 | 0.529812 | 0.32139 | 0.349784 | 0.0593143 | 0.490356 | 0.96037 | 0.127601 |
| bonus_part_correctness | category | Social Science | 4698 | 0.943551 | 0.313038 | 0.038 | 0.0959742 | 0.869519 | 0.476799 | 0.39272 | 0.360477 | 0.0433007 | 0.350024 | 0.960029 | 0.118053 |
| bonus_part_correctness | category | Unknown | 27762 | 0.942588 | 0.325298 | 0.0550532 | 0.0996818 | 0.863446 | 0.483611 | 0.379836 | 0.347518 | 0.0480946 | 0.376724 | 0.950387 | 0.127012 |

## Posterior Predictive Checks

| stage | discrepancy | stratum | observed | replicated_mean | replicated_p05 | replicated_p95 | posterior_predictive_p_value | draws |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| compositional | bonus_score_mass | 0 | 0.074 | 0.0793 | 0.0594 | 0.1002 | 0.65 | 20 |
| compositional | bonus_score_mass | 10 | 0.442 | 0.4017 | 0.3658 | 0.4382 | 0.05 | 20 |
| compositional | bonus_score_mass | 20 | 0.378 | 0.4057 | 0.3759 | 0.4263 | 0.9 | 20 |
| compositional | bonus_score_mass | 30 | 0.106 | 0.1133 | 0.0919 | 0.1441 | 0.65 | 20 |
| pyramidal | buzz_position_mass | Q1 | 0.0162602 | 0.0708647 | 0.0552414 | 0.0966422 | 1 | 20 |
| pyramidal | buzz_position_mass | Q2 | 0.0934959 | 0.111717 | 0.089903 | 0.130928 | 0.85 | 20 |
| pyramidal | buzz_position_mass | Q3 | 0.25813 | 0.247374 | 0.203754 | 0.277032 | 0.3 | 20 |
| pyramidal | buzz_position_mass | Q4 | 0.329268 | 0.337336 | 0.310958 | 0.362684 | 0.7 | 20 |
| pyramidal | buzz_position_mass | Q5 | 0.302846 | 0.232708 | 0.216898 | 0.251187 | 0 | 20 |
| pyramidal | dead_tossup_rate | all | 0.016 | 0.0598 | 0.0476 | 0.0702 | 1 | 20 |
| pyramidal | neg_rate | all | 0.254065 | 0.417197 | 0.386124 | 0.444681 | 1 | 20 |
## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.927123 | 0.935559 | 0.00843554 | synergy |
| log_loss | 0.355133 | 0.336424 | -0.0187089 | synergy |
| ece | 0.0417817 | 0.0437654 | 0.00198365 | no-synergy |
| brier | 0.110096 | 0.104196 | -0.00589924 | synergy |
| accuracy_lift_over_all_correct | 0.325189 | 0.333528 | 0.00833951 | synergy |
| part_accuracy | 0.845678 | 0.854017 | 0.00833951 | synergy |
| part_accuracy_macro_team | 0.848976 | 0.857456 | 0.00847967 | synergy |
| part_accuracy_macro_game | 0.846101 | 0.854597 | 0.00849552 | synergy |
| part_accuracy_macro_bonus | 0.853912 | 0.857878 | 0.0039661 | synergy |
| exact_acc | 0.596534 | 0.614764 | 0.01823 | synergy |
| ranked_probability_score | 0.100243 | 0.0931524 | -0.00709033 | synergy |
| bonus_total_score_log_loss | 0.889913 | 0.840351 | -0.0495621 | synergy |
| ppb_mae | 1.83683 | 0.905 | -0.931831 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1455 | 4.51098 | 1.35343 | 0.723138 | 1.61455 | 3.9081 | 4.8549 | 5.45127 | 6.14437 | 7.0507 |
| player | theta_1 | 1455 | 0.0105468 | 0.729681 | -2.29718 | -1.3337 | -0.467246 | 0.120122 | 0.551619 | 1.05555 | 2.328 |
| player | theta_2 | 1455 | -0.0675416 | 0.730803 | -2.81725 | -1.42729 | -0.516298 | 0.0383081 | 0.443084 | 1.01004 | 1.69692 |
| player | theta_3 | 1455 | 0.109091 | 0.73321 | -2.09547 | -1.24056 | -0.350461 | 0.23776 | 0.610819 | 1.18357 | 2.26385 |
| player | theta_4 | 1455 | 0.0619244 | 0.74244 | -2.16384 | -1.33199 | -0.402477 | 0.197639 | 0.594157 | 1.14547 | 2.04531 |
| player | theta_5 | 1455 | -0.0166705 | 0.747911 | -2.6008 | -1.4037 | -0.462318 | 0.120182 | 0.527514 | 1.04083 | 1.64749 |
| player | theta_norm | 1455 | 1.54835 | 0.579974 | 0.292146 | 0.754318 | 1.12206 | 1.45277 | 1.92279 | 2.65475 | 3.70676 |
| tossup | beta_1 | 1260 | 0.730598 | 0.501776 | -2.41418 | 0.213117 | 0.395197 | 0.572758 | 0.945376 | 1.75774 | 2.75765 |
| tossup | beta_2 | 1260 | 0.822327 | 0.580847 | -1.01539 | 0.197013 | 0.39633 | 0.604864 | 1.23712 | 1.9625 | 2.65647 |
| tossup | beta_3 | 1260 | 0.725846 | 0.512934 | -1.6722 | 0.210046 | 0.392162 | 0.562407 | 0.908339 | 1.81302 | 2.89195 |
| tossup | beta_4 | 1260 | 0.768572 | 0.549474 | -0.802486 | 0.210858 | 0.401261 | 0.574868 | 0.998464 | 2.00726 | 3.38218 |
| tossup | beta_5 | 1260 | 0.808082 | 0.576291 | -1.32519 | 0.20626 | 0.389406 | 0.597827 | 1.14069 | 1.99113 | 2.88054 |
| tossup | gamma_1 | 1260 | 13.1646 | 73.7075 | 0.663624 | 3.14656 | 4.42507 | 5.11935 | 6.02534 | 26.5331 | 2046.72 |
| tossup | gamma_2 | 1260 | 13.8264 | 80.8711 | 0.881303 | 3.3239 | 4.52733 | 5.16583 | 6.46508 | 24.3964 | 2031.4 |
| tossup | gamma_3 | 1260 | 11.341 | 47.4914 | 0.153922 | 2.89244 | 4.42057 | 5.05636 | 5.85229 | 20.8066 | 805.69 |
| tossup | gamma_4 | 1260 | 17.0952 | 119.47 | 1.29639 | 3.1945 | 4.4522 | 5.09351 | 6.00226 | 23.5765 | 2156.82 |
| tossup | gamma_5 | 1260 | 15.1222 | 78.0386 | 0.77931 | 2.95593 | 4.47727 | 5.15946 | 6.50493 | 28.9149 | 1632.4 |
| tossup | mu_1 | 1260 | 0.498907 | 0.103286 | 0.156009 | 0.383461 | 0.443312 | 0.474716 | 0.524684 | 0.719273 | 0.956272 |
| tossup | mu_2 | 1260 | 0.51482 | 0.123002 | 0.233629 | 0.379105 | 0.439186 | 0.474986 | 0.556062 | 0.788815 | 0.976916 |
| tossup | mu_3 | 1260 | 0.50587 | 0.110171 | 0.173911 | 0.384152 | 0.449581 | 0.478697 | 0.52784 | 0.742186 | 0.988322 |
| tossup | mu_4 | 1260 | 0.503973 | 0.112898 | 0.104119 | 0.372506 | 0.446767 | 0.477923 | 0.521811 | 0.74891 | 0.986156 |
| tossup | mu_5 | 1260 | 0.511348 | 0.115064 | 0.126147 | 0.374966 | 0.445138 | 0.482212 | 0.550756 | 0.753014 | 0.992188 |
| tossup | r_1 | 1260 | 0.973098 | 0.736791 | 0.0865554 | 0.220677 | 0.425502 | 0.744118 | 1.31146 | 2.55225 | 4.948 |
| tossup | r_2 | 1260 | 1.30327 | 1.07824 | 0.0983441 | 0.218858 | 0.493551 | 0.914733 | 1.81759 | 3.54456 | 5.75502 |
| tossup | r_3 | 1260 | 1.09275 | 0.937037 | 0.0630926 | 0.196739 | 0.43657 | 0.750178 | 1.46365 | 3.02639 | 5.5279 |
| tossup | r_4 | 1260 | 1.0894 | 0.921586 | 0.0650252 | 0.227398 | 0.450391 | 0.762929 | 1.40119 | 3.17055 | 5.63893 |
| tossup | r_5 | 1260 | 1.18041 | 0.833939 | 0.0718148 | 0.21812 | 0.500455 | 0.94339 | 1.72389 | 2.76025 | 4.65232 |
| tossup | r_norm | 1260 | 3.13563 | 0.844448 | 1.047 | 1.90537 | 2.52854 | 3.04788 | 3.63211 | 4.62946 | 6.58415 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | 0.30726 | 1.54051 | -3.00985 | -2.21623 | -1.02123 | 0.497602 | 1.5728 | 2.5897 | 3.79354 |
| bonus_part | alpha_1 | 3768 | 0.077296 | 0.454364 | -1.63736 | -0.634487 | -0.217588 | 0.0642585 | 0.373497 | 0.824694 | 1.91671 |
| bonus_part | alpha_2 | 3768 | 0.108423 | 0.508038 | -1.71976 | -0.667441 | -0.22071 | 0.0911411 | 0.416453 | 0.985213 | 1.99948 |
| bonus_part | alpha_3 | 3768 | 0.0665277 | 0.531158 | -1.75905 | -0.737884 | -0.309577 | 0.0289406 | 0.442704 | 0.934679 | 2.04719 |
| bonus_part | alpha_4 | 3768 | 0.0762108 | 0.540883 | -2.06051 | -0.720563 | -0.302356 | 0.040794 | 0.42976 | 0.999318 | 2.31503 |
| bonus_part | alpha_5 | 3768 | 0.116437 | 0.453422 | -1.76132 | -0.606946 | -0.157213 | 0.0946382 | 0.385103 | 0.883724 | 2.1369 |
| bonus_part | alpha_norm | 3768 | 1.04107 | 0.449704 | 0.0918246 | 0.391523 | 0.698843 | 0.988449 | 1.34209 | 1.86454 | 2.72679 |
| synergy_player | psi_1 | 1455 | -0.00966028 | 0.411553 | -1.83625 | -0.678498 | -0.0774471 | -0.00513045 | 0.0636269 | 0.686991 | 1.89607 |
| synergy_player | psi_2 | 1455 | 0.00950977 | 0.406969 | -1.7382 | -0.672103 | -0.0755229 | 0.00377326 | 0.0828229 | 0.690359 | 1.75401 |
| synergy_player | psi_3 | 1455 | -0.00603905 | 0.422675 | -1.59423 | -0.748391 | -0.0782016 | -0.00322754 | 0.0705263 | 0.690039 | 1.93932 |
| synergy_player | psi_norm | 1455 | 0.568676 | 0.436188 | 0.0192676 | 0.0727409 | 0.204876 | 0.466742 | 0.824912 | 1.44657 | 1.94817 |
| synergy | synergy_score | 2521 | -0.144672 | 0.484413 | -2.86209 | -1.12483 | -0.345445 | -0.000258708 | 0.110911 | 0.426642 | 1.58784 |
| synergy | synergy_contribution | 44487 | -0.679848 | 0.826631 | -3.30042 | -2.13437 | -1.29078 | -0.646619 | -0.0072783 | 0.585895 | 1.39932 |
