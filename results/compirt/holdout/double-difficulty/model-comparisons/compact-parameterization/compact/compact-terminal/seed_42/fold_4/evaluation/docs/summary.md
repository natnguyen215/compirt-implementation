# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/compact-vs-332/compact/compact-terminal/seed_42/fold_4/evaluation`
Result root: `results/compirt/holdout/compact-vs-332/compact/compact-terminal/seed_42/fold_4`

This file consolidates the metric CSVs and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 3 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 288880 |
| pyramidal | calibrate_correctness | False |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.714402 |
| log_loss | 0.522372 |
| ece | 0.0853859 |
| brier | 0.170982 |
| accuracy | 0.753722 |
| all_correct_accuracy | 0.773355 |
| accuracy_lift_over_all_correct | -0.0196332 |
| probability_std | 0.230819 |
| probability_p10 | 0.342184 |
| probability_p50 | 0.761333 |
| probability_p90 | 0.939467 |
| mean_predictive_variance | 0.158058 |
| integrated_brier_score | 0.098332 |
| joint_tossup_event_log_loss | 6.48549 |
| buzz_position_mae | 0.148397 |
| buzz_position_median_absolute_error | 0.130176 |
| buzz_position_bias | -0.050299 |
| survival_events | 9380 |
| joint_tossup_event_log_loss_events | 9380 |
| first_buzzer_top1_accuracy | 0.388026 |
| first_buzzer_mean_reciprocal_rank | 0.597181 |
| first_buzzer_log_loss | 1.58603 |
| first_buzzer_events | 9270 |
| neg_auroc | 0.714402 |
| neg_average_precision | 0.427265 |
| neg_precision | 0.450164 |
| neg_recall | 0.391242 |
| full_pmf_events | 9380 |
| full_pmf_final_decile_mass | 0.167102 |
| no_buzz_observed_rate | 0.0117271 |
| no_buzz_predicted_rate | 0.00877221 |
| no_buzz_calibration_error | -0.00295487 |
| no_buzz_brier | 0.0104981 |
| full_pmf_max_mass_error | 1.22125e-15 |

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tossup_correctness | aggregate | all | 9270 | 0.714402 | 0.522372 | 0.0853859 | 0.170982 | 0.753722 | 0.773355 | -0.0196332 | 0.230819 | 0.342184 | 0.761333 | 0.939467 | 0.158058 |
| tossup_correctness | tier | fall | 2876 | 0.717394 | 0.487879 | 0.0771572 | 0.158551 | 0.773992 | 0.793115 | -0.0191238 | 0.21506 | 0.407471 | 0.783677 | 0.945387 | 0.154032 |
| tossup_correctness | tier | nationals | 1579 | 0.698695 | 0.56438 | 0.0841548 | 0.189862 | 0.716276 | 0.729576 | -0.0132996 | 0.225802 | 0.315941 | 0.702239 | 0.907048 | 0.175572 |
| tossup_correctness | tier | regionals | 1990 | 0.73608 | 0.534553 | 0.0982952 | 0.173243 | 0.754774 | 0.765829 | -0.0110553 | 0.246455 | 0.28193 | 0.738608 | 0.928005 | 0.160139 |
| tossup_correctness | tier | winter | 2825 | 0.697927 | 0.525427 | 0.0892145 | 0.171493 | 0.753274 | 0.783009 | -0.0297345 | 0.2323 | 0.345513 | 0.780663 | 0.950495 | 0.150901 |
| tossup_correctness | category | Current Events | 123 | 0.692957 | 0.561635 | 0.132904 | 0.190797 | 0.739837 | 0.764228 | -0.0243902 | 0.217107 | 0.288645 | 0.687469 | 0.902032 | 0.179588 |
| tossup_correctness | category | Fine Arts | 1093 | 0.717598 | 0.503052 | 0.074547 | 0.163572 | 0.768527 | 0.769442 | -0.000914913 | 0.219735 | 0.365841 | 0.770365 | 0.935937 | 0.157884 |
| tossup_correctness | category | Geography | 191 | 0.739728 | 0.53721 | 0.106991 | 0.178731 | 0.722513 | 0.691099 | 0.0314136 | 0.23339 | 0.326456 | 0.681703 | 0.897593 | 0.176624 |
| tossup_correctness | category | History | 1469 | 0.716507 | 0.528885 | 0.0637704 | 0.176959 | 0.737236 | 0.758339 | -0.0211028 | 0.23038 | 0.345612 | 0.762208 | 0.941797 | 0.15699 |
| tossup_correctness | category | Literature | 1436 | 0.686132 | 0.507492 | 0.106393 | 0.162848 | 0.764624 | 0.81546 | -0.0508357 | 0.235371 | 0.361383 | 0.809715 | 0.96039 | 0.140693 |
| tossup_correctness | category | Mythology | 325 | 0.669171 | 0.451933 | 0.111937 | 0.14227 | 0.803077 | 0.843077 | -0.04 | 0.171689 | 0.49423 | 0.78949 | 0.930154 | 0.159015 |
| tossup_correctness | category | Other Academic | 67 | 0.61186 | 0.609096 | 0.179695 | 0.205753 | 0.731343 | 0.791045 | -0.0597015 | 0.206712 | 0.359243 | 0.680114 | 0.898332 | 0.183533 |
| tossup_correctness | category | Philosophy | 322 | 0.718795 | 0.491814 | 0.0759806 | 0.163016 | 0.763975 | 0.785714 | -0.0217391 | 0.215797 | 0.399527 | 0.757505 | 0.952605 | 0.157535 |
| tossup_correctness | category | Popular Culture | 100 | 0.599591 | 0.384918 | 0.0765251 | 0.115263 | 0.88 | 0.89 | -0.01 | 0.112559 | 0.660197 | 0.843605 | 0.915318 | 0.139064 |
| tossup_correctness | category | Religion | 365 | 0.677543 | 0.576557 | 0.0718651 | 0.195527 | 0.693151 | 0.723288 | -0.030137 | 0.209575 | 0.36939 | 0.705721 | 0.91651 | 0.177155 |
| tossup_correctness | category | Science | 1456 | 0.698906 | 0.538738 | 0.0856723 | 0.176943 | 0.746566 | 0.76717 | -0.0206044 | 0.230779 | 0.339651 | 0.755556 | 0.931886 | 0.160815 |
| tossup_correctness | category | Social Science | 333 | 0.755784 | 0.516579 | 0.0760729 | 0.171247 | 0.753754 | 0.72973 | 0.024024 | 0.224188 | 0.299936 | 0.710241 | 0.913471 | 0.174344 |
| tossup_correctness | category | Unknown | 1990 | 0.73608 | 0.534553 | 0.0982952 | 0.173243 | 0.754774 | 0.765829 | -0.0110553 | 0.246455 | 0.28193 | 0.738608 | 0.928005 | 0.160139 |
| tossup_correctness | buzz_position_quintile | Q1 (0-.2) | 179 | 0.697512 | 0.594855 | 0.149374 | 0.196405 | 0.72067 | 0.748603 | -0.027933 | 0.24109 | 0.223879 | 0.667595 | 0.867704 | 0.179852 |
| tossup_correctness | buzz_position_quintile | Q2 (.2-.4) | 957 | 0.711304 | 0.547228 | 0.0926451 | 0.179972 | 0.743992 | 0.754441 | -0.0104493 | 0.230717 | 0.29969 | 0.730704 | 0.919101 | 0.168969 |
| tossup_correctness | buzz_position_quintile | Q3 (.4-.6) | 2203 | 0.714016 | 0.51999 | 0.0718799 | 0.170611 | 0.755334 | 0.766682 | -0.0113482 | 0.224565 | 0.353429 | 0.767362 | 0.940068 | 0.15785 |
| tossup_correctness | buzz_position_quintile | Q4 (.6-.8) | 2978 | 0.712858 | 0.499174 | 0.0809255 | 0.162111 | 0.768637 | 0.787441 | -0.0188046 | 0.22245 | 0.379231 | 0.786653 | 0.945921 | 0.152145 |
| tossup_correctness | buzz_position_quintile | Q5 (.8-1) | 2953 | 0.717014 | 0.535093 | 0.0948516 | 0.175752 | 0.742635 | 0.771758 | -0.0291229 | 0.239599 | 0.322621 | 0.745669 | 0.940651 | 0.159319 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1196 | 2.85992 | 0.605534 | 1.00161 | 1.86729 | 2.45121 | 2.85243 | 3.26077 | 3.84566 | 4.90218 |
| player | theta_1 | 1196 | -1.28488 | 0.698296 | -3.25462 | -2.44381 | -1.79095 | -1.26055 | -0.765158 | -0.16434 | 0.394793 |
| player | theta_2 | 1196 | -1.27476 | 0.702032 | -3.22971 | -2.3948 | -1.78406 | -1.30979 | -0.782503 | -0.0519193 | 0.608742 |
| player | theta_3 | 1196 | -1.18449 | 0.678601 | -2.88577 | -2.30531 | -1.68891 | -1.16301 | -0.700294 | -0.109512 | 0.873209 |
| player | theta_norm | 1196 | 2.3605 | 0.739715 | 0.333762 | 1.16732 | 1.82731 | 2.32591 | 2.90529 | 3.58119 | 4.5633 |
| tossup | start_difficulty | 1240 | -1.60505 | 0.737557 | -3.75381 | -2.74969 | -2.09753 | -1.6554 | -1.14382 | -0.342042 | 1.46129 |
| tossup | end_difficulty | 1240 | -3.53484 | 1.48316 | -9.53609 | -6.23427 | -4.42778 | -3.35919 | -2.48109 | -1.38069 | 0.647382 |
| tossup | total_drop | 1240 | 1.92979 | 1.10304 | 0.706342 | 0.899819 | 1.16072 | 1.49459 | 2.38608 | 4.3437 | 7.60998 |
| tossup | drop_share_1 | 1240 | 0.336534 | 0.0610336 | 0.128637 | 0.255003 | 0.302873 | 0.32592 | 0.358377 | 0.456197 | 0.609666 |
| tossup | drop_share_2 | 1240 | 0.351922 | 0.0289813 | 0.220144 | 0.311564 | 0.338323 | 0.350726 | 0.363406 | 0.395319 | 0.552462 |
| tossup | drop_share_3 | 1240 | 0.311545 | 0.0546131 | 0.138306 | 0.211869 | 0.28469 | 0.316656 | 0.341709 | 0.3873 | 0.651219 |
| tossup | r_1 | 1240 | 0.92459 | 0.678855 | 0.0412644 | 0.131529 | 0.393783 | 0.743259 | 1.29609 | 2.33515 | 3.50834 |
| tossup | r_2 | 1240 | 0.930611 | 0.810686 | 0.044384 | 0.123508 | 0.313299 | 0.653441 | 1.34929 | 2.5809 | 4.84504 |
| tossup | r_3 | 1240 | 0.771059 | 0.689482 | 0.0397206 | 0.12387 | 0.296746 | 0.539096 | 0.966982 | 2.36854 | 3.90594 |
| tossup | r_norm | 1240 | 1.86144 | 0.665584 | 0.476339 | 0.88134 | 1.36671 | 1.8129 | 2.28877 | 3.02831 | 5.09886 |
| tossup_hazard | hazard_start_difficulty | 1240 | 2.56836 | 0.572294 | 0.676183 | 1.6322 | 2.15975 | 2.57245 | 2.97425 | 3.50922 | 4.22546 |
| tossup_hazard | hazard_end_difficulty | 1240 | -1.6263 | 1.51897 | -7.03526 | -4.15002 | -2.57104 | -1.63422 | -0.592378 | 0.77882 | 2.31431 |
| tossup_hazard | hazard_total_drop | 1240 | 4.19466 | 1.54059 | 0.621646 | 1.48005 | 3.25836 | 4.23483 | 5.16025 | 6.70158 | 9.98815 |
| tossup_hazard | hazard_drop_share_1 | 1240 | 0.133248 | 0.0724801 | 0.0311984 | 0.0575663 | 0.0823343 | 0.112453 | 0.164616 | 0.267431 | 0.610375 |
| tossup_hazard | hazard_drop_share_2 | 1240 | 0.306731 | 0.141157 | 0.0469565 | 0.113266 | 0.187552 | 0.298796 | 0.400702 | 0.567208 | 0.774856 |
| tossup_hazard | hazard_drop_share_3 | 1240 | 0.560021 | 0.18656 | 0.0811846 | 0.235179 | 0.411462 | 0.574664 | 0.717259 | 0.824843 | 0.916994 |
