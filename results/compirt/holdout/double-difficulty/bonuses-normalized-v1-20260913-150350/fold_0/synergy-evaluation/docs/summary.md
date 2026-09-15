# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/synergy-evaluation`
Result root: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| synergy | tournament | all tournaments |
| synergy | dimensions | 3 |
| synergy | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.51081 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.89906 |
| log_loss | 0.403038 |
| ece | 0.0206284 |
| brier | 0.128121 |
| part_accuracy | 0.819118 |
| part_all_correct_accuracy | 0.518437 |
| accuracy_lift_over_all_correct | 0.300682 |
| part_accuracy_macro_team | 0.821057 |
| part_accuracy_macro_bonus | 0.817208 |
| probability_std | 0.351266 |
| probability_p10 | 0.0523124 |
| probability_p50 | 0.550438 |
| probability_p90 | 0.965487 |
| mean_predictive_variance | 0.125661 |
| exact_acc | 0.532535 |
| ranked_probability_score | 0.111197 |
| bonus_total_score_log_loss | 0.983876 |
| ppb_mae | 1.81008 |
| ranked_probability_score_responses | 8606 |
| bonus_total_score_log_loss_responses | 8606 |

## Stage 1 Tossup Metrics

No tossup metrics CSV was found.

## Tossup Game Replay

No tossup game replay metrics CSV was found.

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25818 | 0.89906 | 0.403038 | 0.0206284 | 0.128121 | 0.819118 | 0.518437 | 0.300682 | 0.351266 | 0.0523124 | 0.550438 | 0.965487 | 0.125661 |
| bonus_part_correctness | tier | fall | 8415 | 0.891323 | 0.408953 | 0.0207383 | 0.131734 | 0.810695 | 0.600475 | 0.21022 | 0.340463 | 0.0886657 | 0.701488 | 0.978529 | 0.12197 |
| bonus_part_correctness | tier | nationals | 4179 | 0.89945 | 0.398546 | 0.0356751 | 0.124964 | 0.828428 | 0.413975 | 0.414453 | 0.332408 | 0.0479191 | 0.380942 | 0.91266 | 0.136483 |
| bonus_part_correctness | tier | regionals | 5070 | 0.900296 | 0.399362 | 0.0163903 | 0.126943 | 0.81854 | 0.477318 | 0.341223 | 0.350891 | 0.032258 | 0.450566 | 0.945844 | 0.126284 |
| bonus_part_correctness | tier | winter | 8154 | 0.900046 | 0.401522 | 0.0244909 | 0.126744 | 0.8234 | 0.512877 | 0.310522 | 0.354563 | 0.0491541 | 0.534096 | 0.965891 | 0.123535 |
| bonus_part_correctness | category | Current Events | 258 | 0.925841 | 0.351344 | 0.032997 | 0.104915 | 0.864341 | 0.496124 | 0.368217 | 0.360672 | 0.0401616 | 0.52588 | 0.958644 | 0.119736 |
| bonus_part_correctness | category | Fine Arts | 3075 | 0.886313 | 0.42728 | 0.026903 | 0.13647 | 0.810081 | 0.506667 | 0.303415 | 0.343263 | 0.0637181 | 0.533654 | 0.963578 | 0.131597 |
| bonus_part_correctness | category | Geography | 453 | 0.893078 | 0.407916 | 0.0363025 | 0.129328 | 0.818985 | 0.600442 | 0.218543 | 0.333174 | 0.0695948 | 0.716474 | 0.971193 | 0.124912 |
| bonus_part_correctness | category | History | 4176 | 0.896971 | 0.405105 | 0.0238074 | 0.12937 | 0.812261 | 0.55364 | 0.258621 | 0.34767 | 0.0624879 | 0.624685 | 0.970891 | 0.124498 |
| bonus_part_correctness | category | Literature | 4197 | 0.911666 | 0.378862 | 0.0317802 | 0.119355 | 0.834406 | 0.508458 | 0.325947 | 0.353911 | 0.054973 | 0.524413 | 0.968315 | 0.123966 |
| bonus_part_correctness | category | Mythology | 951 | 0.885704 | 0.416148 | 0.0336116 | 0.134732 | 0.811777 | 0.608833 | 0.202944 | 0.319432 | 0.140325 | 0.728634 | 0.97792 | 0.129135 |
| bonus_part_correctness | category | Other Academic | 258 | 0.929398 | 0.347663 | 0.040579 | 0.106555 | 0.841085 | 0.55814 | 0.282946 | 0.35888 | 0.0474907 | 0.594602 | 0.966728 | 0.119932 |
| bonus_part_correctness | category | Philosophy | 969 | 0.885996 | 0.424408 | 0.0295438 | 0.135551 | 0.80805 | 0.493292 | 0.314757 | 0.340291 | 0.0657891 | 0.488252 | 0.961125 | 0.134097 |
| bonus_part_correctness | category | Popular Culture | 303 | 0.858557 | 0.457741 | 0.0793029 | 0.156375 | 0.765677 | 0.620462 | 0.145215 | 0.321322 | 0.139648 | 0.769384 | 0.982329 | 0.125029 |
| bonus_part_correctness | category | Religion | 1041 | 0.899204 | 0.405979 | 0.0372239 | 0.128194 | 0.825168 | 0.509126 | 0.316042 | 0.356337 | 0.0402158 | 0.546572 | 0.960547 | 0.122453 |
| bonus_part_correctness | category | Science | 4152 | 0.897459 | 0.405716 | 0.0212006 | 0.128422 | 0.821291 | 0.529383 | 0.291908 | 0.352234 | 0.0593802 | 0.564852 | 0.966673 | 0.1242 |
| bonus_part_correctness | category | Social Science | 915 | 0.898591 | 0.401302 | 0.0424881 | 0.127587 | 0.815301 | 0.485246 | 0.330055 | 0.364752 | 0.0291512 | 0.466646 | 0.968973 | 0.116933 |
| bonus_part_correctness | category | Unknown | 5070 | 0.900296 | 0.399362 | 0.0163903 | 0.126943 | 0.81854 | 0.477318 | 0.341223 | 0.350891 | 0.032258 | 0.450566 | 0.945844 | 0.126284 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

No bonus model comparison CSV was found.

## Pyramidal Player And Tossup Parameters

No pyramidal parameter distribution summary CSV was found.

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum | parameter_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.205828 | 1.21195 | -2.7272 | -2.20461 | -1.2481 | -0.131537 | 0.827389 | 1.56911 | 2.1973 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/synergy |
| bonus_part | alpha_1 | 3768 | 0.828028 | 0.456597 | 0.207906 | 0.31633 | 0.446272 | 0.711829 | 1.13098 | 1.65108 | 3.10885 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/synergy |
| bonus_part | alpha_2 | 3768 | 0.81659 | 0.43107 | 0.181351 | 0.346406 | 0.457505 | 0.69164 | 1.08463 | 1.63804 | 3.33843 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/synergy |
| bonus_part | alpha_3 | 3768 | 0.797409 | 0.405033 | 0.210779 | 0.326908 | 0.47194 | 0.709207 | 1.04204 | 1.55316 | 3.10938 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/synergy |
| bonus_part | alpha_norm | 3768 | 1.46866 | 0.624215 | 0.514238 | 0.605359 | 0.895936 | 1.43586 | 1.96012 | 2.48993 | 3.55605 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/synergy |
| synergy_player | psi_1 | 1455 | 0.00819683 | 0.424773 | -1.44748 | -0.703072 | -0.259907 | 0.0100076 | 0.292978 | 0.69204 | 1.55715 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/synergy |
| synergy_player | psi_norm | 1455 | 0.321393 | 0.277732 | 1.43354e-05 | 0.0116271 | 0.0852152 | 0.2753 | 0.467864 | 0.878617 | 1.55715 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/synergy |
| synergy | synergy_score | 2506 | 0.0371831 | 0.229884 | -1.30632 | -0.354393 | -0.00622682 | 0.0137932 | 0.127416 | 0.367915 | 2.26927 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/synergy |
| synergy | synergy_contribution | 35881 | 0.284583 | 0.652304 | -1.72588 | -0.773104 | -0.0726433 | 0.0995469 | 0.728509 | 1.44953 | 2.45254 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_0/train/synergy |
