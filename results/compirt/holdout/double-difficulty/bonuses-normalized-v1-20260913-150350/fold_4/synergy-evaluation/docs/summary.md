# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/synergy-evaluation`
Result root: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4`

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
| tau | 1.63215 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.898912 |
| log_loss | 0.403292 |
| ece | 0.0187589 |
| brier | 0.127967 |
| part_accuracy | 0.817289 |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.291734 |
| part_accuracy_macro_team | 0.822807 |
| part_accuracy_macro_bonus | 0.814768 |
| probability_std | 0.349698 |
| probability_p10 | 0.0535397 |
| probability_p50 | 0.548285 |
| probability_p90 | 0.965973 |
| mean_predictive_variance | 0.126791 |
| exact_acc | 0.531199 |
| ranked_probability_score | 0.112765 |
| bonus_total_score_log_loss | 0.998791 |
| ppb_mae | 1.66831 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

## Stage 1 Tossup Metrics

No tossup metrics CSV was found.

## Tossup Game Replay

No tossup game replay metrics CSV was found.

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25866 | 0.898912 | 0.403292 | 0.0187589 | 0.127967 | 0.817289 | 0.525555 | 0.291734 | 0.349698 | 0.0535397 | 0.548285 | 0.965973 | 0.126791 |
| bonus_part_correctness | tier | fall | 8259 | 0.89617 | 0.401061 | 0.022272 | 0.128391 | 0.813537 | 0.601283 | 0.212253 | 0.340165 | 0.0922982 | 0.690492 | 0.97784 | 0.122546 |
| bonus_part_correctness | tier | nationals | 4167 | 0.894982 | 0.408 | 0.0267761 | 0.12832 | 0.821454 | 0.438445 | 0.383009 | 0.32782 | 0.0553543 | 0.404181 | 0.916644 | 0.140434 |
| bonus_part_correctness | tier | regionals | 5457 | 0.898066 | 0.404715 | 0.0127338 | 0.12798 | 0.819131 | 0.493861 | 0.32527 | 0.347679 | 0.0393116 | 0.459618 | 0.953241 | 0.128936 |
| bonus_part_correctness | tier | winter | 7983 | 0.899962 | 0.402169 | 0.0241645 | 0.127335 | 0.817738 | 0.514343 | 0.303395 | 0.356411 | 0.0420379 | 0.525746 | 0.966612 | 0.122597 |
| bonus_part_correctness | category | Current Events | 258 | 0.880782 | 0.443796 | 0.0407245 | 0.143278 | 0.79845 | 0.515504 | 0.282946 | 0.362012 | 0.0482194 | 0.589622 | 0.961412 | 0.118203 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.892571 | 0.415179 | 0.0336704 | 0.132744 | 0.807333 | 0.508 | 0.299333 | 0.340198 | 0.0625746 | 0.540054 | 0.963404 | 0.133524 |
| bonus_part_correctness | category | Geography | 450 | 0.896723 | 0.406915 | 0.0527151 | 0.129508 | 0.822222 | 0.582222 | 0.24 | 0.337716 | 0.0877863 | 0.748998 | 0.974743 | 0.120805 |
| bonus_part_correctness | category | History | 4116 | 0.904302 | 0.390626 | 0.023147 | 0.124252 | 0.820943 | 0.562196 | 0.258746 | 0.349034 | 0.0604491 | 0.626023 | 0.971953 | 0.123565 |
| bonus_part_correctness | category | Literature | 4092 | 0.903394 | 0.393505 | 0.0232805 | 0.124153 | 0.824047 | 0.522727 | 0.30132 | 0.352177 | 0.0549157 | 0.521459 | 0.969732 | 0.125387 |
| bonus_part_correctness | category | Mythology | 951 | 0.894306 | 0.400006 | 0.0358148 | 0.126211 | 0.819138 | 0.647739 | 0.171399 | 0.325209 | 0.116939 | 0.710173 | 0.975763 | 0.128981 |
| bonus_part_correctness | category | Other Academic | 276 | 0.912988 | 0.373314 | 0.0371852 | 0.116663 | 0.847826 | 0.532609 | 0.315217 | 0.359034 | 0.0569491 | 0.63342 | 0.968864 | 0.118889 |
| bonus_part_correctness | category | Philosophy | 957 | 0.891466 | 0.426181 | 0.0376339 | 0.133537 | 0.808777 | 0.474399 | 0.334378 | 0.342146 | 0.0510368 | 0.516943 | 0.955619 | 0.132892 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.875488 | 0.4299 | 0.0724609 | 0.144322 | 0.776667 | 0.616667 | 0.16 | 0.320094 | 0.130806 | 0.72964 | 0.980524 | 0.1268 |
| bonus_part_correctness | category | Religion | 1029 | 0.901677 | 0.39939 | 0.0480761 | 0.127207 | 0.812439 | 0.501458 | 0.310982 | 0.352277 | 0.0520159 | 0.518243 | 0.958243 | 0.125618 |
| bonus_part_correctness | category | Science | 4089 | 0.892953 | 0.415558 | 0.0249129 | 0.131793 | 0.812668 | 0.533382 | 0.279286 | 0.349876 | 0.0592274 | 0.559777 | 0.967009 | 0.126095 |
| bonus_part_correctness | category | Social Science | 891 | 0.911851 | 0.371911 | 0.0265515 | 0.118478 | 0.832772 | 0.480359 | 0.352413 | 0.365486 | 0.0352808 | 0.425598 | 0.966847 | 0.115956 |
| bonus_part_correctness | category | Unknown | 5457 | 0.898066 | 0.404715 | 0.0127338 | 0.12798 | 0.819131 | 0.493861 | 0.32527 | 0.347679 | 0.0393116 | 0.459618 | 0.953241 | 0.128936 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

No bonus model comparison CSV was found.

## Pyramidal Player And Tossup Parameters

No pyramidal parameter distribution summary CSV was found.

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum | parameter_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.184776 | 1.20672 | -2.68439 | -2.15909 | -1.23986 | -0.106658 | 0.849894 | 1.60132 | 2.29248 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/synergy |
| bonus_part | alpha_1 | 3768 | 0.832806 | 0.450205 | 0.204303 | 0.317367 | 0.450915 | 0.727541 | 1.12239 | 1.66182 | 3.11055 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/synergy |
| bonus_part | alpha_2 | 3768 | 0.821048 | 0.422317 | 0.23117 | 0.346714 | 0.466988 | 0.717124 | 1.07679 | 1.60023 | 3.08168 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/synergy |
| bonus_part | alpha_3 | 3768 | 0.807998 | 0.417753 | 0.178731 | 0.32143 | 0.457054 | 0.714769 | 1.08615 | 1.57861 | 3.11502 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/synergy |
| bonus_part | alpha_norm | 3768 | 1.47993 | 0.621191 | 0.501744 | 0.609254 | 0.910506 | 1.45552 | 1.98337 | 2.5018 | 3.80802 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/synergy |
| synergy_player | psi_1 | 1455 | 0.00692162 | 0.422308 | -1.42405 | -0.688297 | -0.244193 | -0.000608171 | 0.249041 | 0.75791 | 1.6813 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/synergy |
| synergy_player | psi_norm | 1455 | 0.309841 | 0.286922 | 4.1189e-05 | 0.00989375 | 0.0727472 | 0.245475 | 0.446835 | 0.901466 | 1.6813 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/synergy |
| synergy | synergy_score | 2514 | 0.0187741 | 0.230958 | -1.26138 | -0.386544 | -0.0115655 | 0.00699954 | 0.094762 | 0.316707 | 2.2188 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/synergy |
| synergy | synergy_contribution | 35865 | 0.181303 | 0.612588 | -1.95117 | -0.814358 | -0.0876143 | 0.0120363 | 0.526574 | 1.1944 | 2.45468 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/synergy |
