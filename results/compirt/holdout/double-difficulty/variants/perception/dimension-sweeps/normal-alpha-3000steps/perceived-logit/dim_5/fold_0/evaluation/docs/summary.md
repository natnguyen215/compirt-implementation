# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_5/fold_0/evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/variants/perception/dimension-sweeps/normal-alpha-3000steps/perceived-logit/dim_5/fold_0`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 335914 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.551374 |
| log_loss | 0.58911 |
| ece | 0.088897 |
| brier | 0.18811 |
| accuracy | 0.764282 |
| all_correct_accuracy | 0.76525 |
| accuracy_lift_over_all_correct | -0.000968263 |
| probability_std | 0.105564 |
| probability_p10 | 0.684468 |
| probability_p50 | 0.872429 |
| probability_p90 | 0.94094 |
| mean_predictive_variance | 0.123416 |
| integrated_brier_score | 0.171899 |
| joint_tossup_event_log_loss | 7.7189 |
| buzz_position_mae | 0.333371 |
| buzz_position_median_absolute_error | 0.333432 |
| buzz_position_bias | -0.319719 |
| survival_events | 9420 |
| joint_tossup_event_log_loss_events | 9420 |
| first_buzzer_top1_accuracy | 0.35277 |
| first_buzzer_mean_reciprocal_rank | 0.565925 |
| first_buzzer_log_loss | 1.66771 |
| first_buzzer_events | 9295 |
| first_buzzer_team_top1_accuracy | 0.625605 |
| tossup_scorer_player_top1_accuracy | 0.265287 |
| tossup_scorer_team_top1_accuracy | 0.396815 |
| tossup_game_winner_accuracy | 0.69163 |
| tossup_game_margin_mae | 43.5098 |
| tournament_player_ppg_spearman | 0.576682 |
| tournament_player_ppg_mae | 10.3509 |
| tournament_player_ppg_top10_overlap | 0.603448 |
| neg_auroc | 0.551374 |
| neg_average_precision | 0.283229 |
| neg_precision | 0.449438 |
| neg_recall | 0.0183318 |
| full_pmf_events | 9420 |
| full_pmf_final_decile_mass | 0.0310022 |
| no_buzz_observed_rate | 0.0132696 |
| no_buzz_predicted_rate | 0.230991 |
| no_buzz_calibration_error | 0.217721 |
| no_buzz_brier | 0.0690733 |
| full_pmf_max_mass_error | 1.22125e-15 |
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
| tossup_correctness | aggregate | all | 9295 | 0.551374 | 0.58911 | 0.088897 | 0.18811 | 0.764282 | 0.76525 | -0.000968263 | 0.105564 | 0.684468 | 0.872429 | 0.94094 | 0.123416 |
| tossup_correctness | tier | fall | 2933 | 0.561712 | 0.535334 | 0.0709779 | 0.169428 | 0.79134 | 0.791681 | -0.000340948 | 0.0857862 | 0.727098 | 0.875201 | 0.93443 | 0.119261 |
| tossup_correctness | tier | nationals | 1584 | 0.569961 | 0.620173 | 0.0816682 | 0.20564 | 0.721591 | 0.724747 | -0.00315657 | 0.136795 | 0.573143 | 0.800135 | 0.928918 | 0.157901 |
| tossup_correctness | tier | regionals | 1886 | 0.522964 | 0.630647 | 0.105851 | 0.20326 | 0.744963 | 0.746023 | -0.00106045 | 0.112558 | 0.657814 | 0.850486 | 0.941728 | 0.133767 |
| tossup_correctness | tier | winter | 2892 | 0.536473 | 0.599546 | 0.109353 | 0.187575 | 0.772822 | 0.773167 | -0.000345781 | 0.0739769 | 0.777319 | 0.89933 | 0.948989 | 0.101991 |
| tossup_correctness | category | Current Events | 124 | 0.522373 | 0.593683 | 0.0971771 | 0.195696 | 0.75 | 0.75 | 0 | 0.111837 | 0.643618 | 0.832415 | 0.898373 | 0.145659 |
| tossup_correctness | category | Fine Arts | 1103 | 0.522407 | 0.629187 | 0.122432 | 0.198787 | 0.761559 | 0.759746 | 0.00181324 | 0.0973415 | 0.711424 | 0.895558 | 0.946892 | 0.110818 |
| tossup_correctness | category | Geography | 197 | 0.654429 | 0.713739 | 0.178391 | 0.241778 | 0.675127 | 0.670051 | 0.00507614 | 0.0968259 | 0.729348 | 0.876626 | 0.936589 | 0.119213 |
| tossup_correctness | category | History | 1491 | 0.558639 | 0.546071 | 0.0793779 | 0.174015 | 0.781355 | 0.787391 | -0.00603622 | 0.100701 | 0.687352 | 0.865214 | 0.933394 | 0.126986 |
| tossup_correctness | category | Literature | 1472 | 0.552547 | 0.528352 | 0.0783901 | 0.16299 | 0.805027 | 0.804348 | 0.000679348 | 0.0970485 | 0.725492 | 0.895888 | 0.949702 | 0.108485 |
| tossup_correctness | category | Mythology | 332 | 0.601732 | 0.494822 | 0.0835639 | 0.154952 | 0.816265 | 0.813253 | 0.00301205 | 0.0873561 | 0.740519 | 0.893469 | 0.938594 | 0.109508 |
| tossup_correctness | category | Other Academic | 69 | 0.514706 | 0.604344 | 0.0846116 | 0.192102 | 0.753623 | 0.753623 | 0 | 0.114325 | 0.619341 | 0.867888 | 0.932634 | 0.130175 |
| tossup_correctness | category | Philosophy | 324 | 0.584675 | 0.51559 | 0.0793664 | 0.160162 | 0.802469 | 0.799383 | 0.00308642 | 0.100011 | 0.69158 | 0.88839 | 0.943894 | 0.116732 |
| tossup_correctness | category | Popular Culture | 102 | 0.357785 | 0.516933 | 0.121018 | 0.155433 | 0.833333 | 0.833333 | 0 | 0.0728454 | 0.753988 | 0.880885 | 0.932115 | 0.115945 |
| tossup_correctness | category | Religion | 372 | 0.619774 | 0.657903 | 0.138452 | 0.217004 | 0.706989 | 0.709677 | -0.00268817 | 0.120292 | 0.675099 | 0.883693 | 0.938593 | 0.11894 |
| tossup_correctness | category | Science | 1487 | 0.568753 | 0.587789 | 0.0761893 | 0.189796 | 0.749832 | 0.752522 | -0.00268998 | 0.108794 | 0.663106 | 0.844025 | 0.931814 | 0.136941 |
| tossup_correctness | category | Social Science | 336 | 0.534407 | 0.719318 | 0.162638 | 0.235716 | 0.705357 | 0.702381 | 0.00297619 | 0.102506 | 0.703748 | 0.882836 | 0.938686 | 0.116658 |
| tossup_correctness | category | Unknown | 1886 | 0.522964 | 0.630647 | 0.105851 | 0.20326 | 0.744963 | 0.746023 | -0.00106045 | 0.112558 | 0.657814 | 0.850486 | 0.941728 | 0.133767 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 197 | 0.53939 | 0.610329 | 0.109702 | 0.205376 | 0.725888 | 0.736041 | -0.0101523 | 0.112583 | 0.637276 | 0.81102 | 0.908053 | 0.156818 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 985 | 0.525116 | 0.627577 | 0.0950645 | 0.205406 | 0.73198 | 0.735025 | -0.00304569 | 0.103834 | 0.671781 | 0.841918 | 0.919695 | 0.140341 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2251 | 0.571374 | 0.563728 | 0.0757792 | 0.181965 | 0.767659 | 0.769436 | -0.00177699 | 0.0987319 | 0.693247 | 0.862553 | 0.929168 | 0.128102 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2866 | 0.555875 | 0.553194 | 0.0789075 | 0.175149 | 0.785066 | 0.78402 | 0.00104676 | 0.1024 | 0.692964 | 0.876636 | 0.937623 | 0.12236 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2996 | 0.545097 | 0.628495 | 0.111929 | 0.198304 | 0.755007 | 0.756008 | -0.00100134 | 0.110559 | 0.678253 | 0.894506 | 0.95156 | 0.113144 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | alpha | 1186 | -1.20961 | 0.901184 | -3.31335 | -2.40327 | -1.7592 | -1.3383 | -0.859181 | 0.756066 | 2.15227 |
| player | beta | 1186 | -3.77344 | 1.23329 | -7.22889 | -6.3915 | -4.42106 | -3.46445 | -2.81632 | -2.27867 | -1.84322 |
| player | theta_1 | 1186 | 0.802325 | 1.03208 | -2.61233 | -1.07442 | 0.114776 | 0.983 | 1.58205 | 2.21132 | 3.43474 |
| player | theta_2 | 1186 | 0.775376 | 0.916361 | -2.88959 | -1.00035 | 0.222704 | 0.920118 | 1.41657 | 2.04998 | 3.39327 |
| player | theta_3 | 1186 | 0.718088 | 0.75065 | -2.04316 | -0.717709 | 0.278465 | 0.843026 | 1.25057 | 1.77085 | 2.42318 |
| player | theta_4 | 1186 | 0.669386 | 0.729331 | -1.75595 | -0.741341 | 0.301485 | 0.773621 | 1.13727 | 1.7099 | 3.0807 |
| player | theta_5 | 1186 | 0.6598 | 0.652168 | -1.67486 | -0.589542 | 0.343362 | 0.743609 | 1.07385 | 1.60795 | 2.70066 |
| player | theta_norm | 1186 | 2.36008 | 0.705116 | 0.30996 | 1.16121 | 1.94183 | 2.42223 | 2.80195 | 3.48572 | 4.99303 |
| tossup | start_difficulty_d1 | 1240 | -0.85944 | 0.428715 | -2.07985 | -1.64931 | -1.16542 | -0.792926 | -0.522977 | -0.262538 | 0.0160305 |
| tossup | start_difficulty_d2 | 1240 | -0.838956 | 0.474543 | -2.35943 | -1.71617 | -1.17369 | -0.755481 | -0.483282 | -0.187197 | 0.100438 |
| tossup | start_difficulty_d3 | 1240 | -0.753671 | 0.356486 | -1.9953 | -1.38341 | -0.998421 | -0.702675 | -0.495855 | -0.238524 | 0.0253333 |
| tossup | start_difficulty_d4 | 1240 | -0.72006 | 0.336492 | -2.02469 | -1.33986 | -0.908574 | -0.684704 | -0.488874 | -0.24233 | 0.0779246 |
| tossup | start_difficulty_d5 | 1240 | -0.716554 | 0.318101 | -1.73627 | -1.22937 | -0.963368 | -0.701112 | -0.478464 | -0.21918 | 0.127662 |
| tossup | end_difficulty_d1 | 1240 | -1.65346 | 0.355646 | -2.9048 | -2.27816 | -1.8966 | -1.61639 | -1.39839 | -1.11207 | -0.707767 |
| tossup | end_difficulty_d2 | 1240 | -1.65214 | 0.42311 | -3.02838 | -2.41407 | -1.94193 | -1.6142 | -1.33179 | -1.04012 | -0.66409 |
| tossup | end_difficulty_d3 | 1240 | -1.59187 | 0.329386 | -2.54579 | -2.16468 | -1.82462 | -1.57826 | -1.34768 | -1.07882 | -0.696052 |
| tossup | end_difficulty_d4 | 1240 | -1.57071 | 0.317734 | -2.49134 | -2.12897 | -1.77422 | -1.54788 | -1.34079 | -1.08172 | -0.609468 |
| tossup | end_difficulty_d5 | 1240 | -1.57239 | 0.318394 | -2.44385 | -2.09799 | -1.79208 | -1.57378 | -1.33319 | -1.08568 | -0.571891 |
| tossup | total_drop_d1 | 1240 | 0.79402 | 0.220979 | 0.254119 | 0.385236 | 0.648608 | 0.816883 | 0.956054 | 1.11971 | 1.33176 |
| tossup | total_drop_d2 | 1240 | 0.813181 | 0.1973 | 0.30797 | 0.454707 | 0.689687 | 0.831342 | 0.940467 | 1.11442 | 1.48798 |
| tossup | total_drop_d3 | 1240 | 0.838202 | 0.179465 | 0.289796 | 0.498121 | 0.735196 | 0.841429 | 0.956011 | 1.11355 | 1.36265 |
| tossup | total_drop_d4 | 1240 | 0.850654 | 0.166555 | 0.250802 | 0.564723 | 0.753496 | 0.846663 | 0.949155 | 1.12916 | 1.55774 |
| tossup | total_drop_d5 | 1240 | 0.855838 | 0.157074 | 0.321661 | 0.611368 | 0.752468 | 0.843855 | 0.950282 | 1.12906 | 1.50015 |
| tossup | drop_share_1_d1 | 1240 | 0.316812 | 0.0222529 | 0.228959 | 0.284536 | 0.304283 | 0.314469 | 0.32857 | 0.355836 | 0.41711 |
| tossup | drop_share_2_d1 | 1240 | 0.330335 | 0.0182507 | 0.260254 | 0.294364 | 0.320584 | 0.333076 | 0.34323 | 0.355001 | 0.372911 |
| tossup | drop_share_3_d1 | 1240 | 0.352852 | 0.026531 | 0.275503 | 0.318115 | 0.337532 | 0.349559 | 0.363081 | 0.405741 | 0.480114 |
| tossup | drop_share_1_d2 | 1240 | 0.316689 | 0.0217636 | 0.253471 | 0.286425 | 0.303352 | 0.314756 | 0.327711 | 0.357568 | 0.421363 |
| tossup | drop_share_2_d2 | 1240 | 0.332301 | 0.0149358 | 0.267413 | 0.304465 | 0.323608 | 0.33344 | 0.342572 | 0.35469 | 0.373011 |
| tossup | drop_share_3_d2 | 1240 | 0.35101 | 0.0214426 | 0.265186 | 0.318705 | 0.338044 | 0.350195 | 0.362871 | 0.386899 | 0.455491 |
| tossup | drop_share_1_d3 | 1240 | 0.315643 | 0.0184132 | 0.221926 | 0.286902 | 0.304369 | 0.316305 | 0.326799 | 0.344542 | 0.38099 |
| tossup | drop_share_2_d3 | 1240 | 0.333557 | 0.0151409 | 0.268288 | 0.304685 | 0.325825 | 0.335539 | 0.343443 | 0.354574 | 0.376244 |
| tossup | drop_share_3_d3 | 1240 | 0.3508 | 0.0225089 | 0.298163 | 0.320428 | 0.337327 | 0.348106 | 0.359555 | 0.393218 | 0.474892 |
| tossup | drop_share_1_d4 | 1240 | 0.314146 | 0.0161726 | 0.242084 | 0.288652 | 0.303867 | 0.314006 | 0.324441 | 0.339441 | 0.387809 |
| tossup | drop_share_2_d4 | 1240 | 0.334638 | 0.0143965 | 0.271763 | 0.308859 | 0.327023 | 0.335578 | 0.344157 | 0.356104 | 0.373723 |
| tossup | drop_share_3_d4 | 1240 | 0.351216 | 0.0194947 | 0.27904 | 0.324357 | 0.338377 | 0.349227 | 0.361024 | 0.386003 | 0.44076 |
| tossup | drop_share_1_d5 | 1240 | 0.315261 | 0.0170402 | 0.227286 | 0.290276 | 0.304292 | 0.314064 | 0.326039 | 0.343213 | 0.386847 |
| tossup | drop_share_2_d5 | 1240 | 0.334805 | 0.0129865 | 0.277728 | 0.31296 | 0.326811 | 0.335573 | 0.34368 | 0.354447 | 0.377303 |
| tossup | drop_share_3_d5 | 1240 | 0.349934 | 0.018351 | 0.278176 | 0.322333 | 0.337794 | 0.34953 | 0.360646 | 0.379927 | 0.467723 |
| tossup | r_1 | 1240 | 0.243111 | 0.188411 | 0.0310267 | 0.0606488 | 0.112789 | 0.168243 | 0.309391 | 0.684211 | 0.842182 |
| tossup | r_2 | 1240 | 0.220176 | 0.135546 | 0.0318761 | 0.0594261 | 0.11714 | 0.18961 | 0.283559 | 0.506232 | 0.782515 |
| tossup | r_3 | 1240 | 0.181977 | 0.106978 | 0.0323913 | 0.0613079 | 0.12142 | 0.171237 | 0.20506 | 0.401724 | 0.816144 |
| tossup | r_4 | 1240 | 0.181556 | 0.0983807 | 0.0339397 | 0.0617175 | 0.113908 | 0.179217 | 0.221696 | 0.320516 | 0.799446 |
| tossup | r_5 | 1240 | 0.17318 | 0.0728185 | 0.0383004 | 0.0638498 | 0.116938 | 0.173464 | 0.222174 | 0.271583 | 0.616798 |
| tossup | r_norm | 1240 | 0.525586 | 0.0874494 | 0.447366 | 0.450736 | 0.459838 | 0.489973 | 0.562659 | 0.720493 | 0.845905 |
