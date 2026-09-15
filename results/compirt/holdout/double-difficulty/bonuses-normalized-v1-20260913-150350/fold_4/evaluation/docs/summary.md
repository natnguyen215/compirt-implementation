# CompIRT Evaluation Summary

Evaluation folder: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/evaluation`
Result root: `results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: frozen matrix-infill holdout.** Player and question parameters were fit on the training folds and replayed on held-out games without fitting any held-out outcomes.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| compositional | tournament | all tournaments |
| compositional | dimensions | 3 |
| compositional | calibrate_correctness | False |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 1.56636 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.890772 |
| log_loss | 0.41746 |
| ece | 0.0194317 |
| brier | 0.133505 |
| part_accuracy | 0.807315 |
| part_all_correct_accuracy | 0.525555 |
| accuracy_lift_over_all_correct | 0.28176 |
| part_accuracy_macro_team | 0.810707 |
| part_accuracy_macro_bonus | 0.803836 |
| probability_std | 0.342949 |
| probability_p10 | 0.058817 |
| probability_p50 | 0.53765 |
| probability_p90 | 0.95696 |
| mean_predictive_variance | 0.131694 |
| exact_acc | 0.507423 |
| ranked_probability_score | 0.118782 |
| bonus_total_score_log_loss | 1.03777 |
| ppb_mae | 2.36623 |
| ranked_probability_score_responses | 8622 |
| bonus_total_score_log_loss_responses | 8622 |

## Stage 1 Tossup Metrics

No tossup metrics CSV was found.

## Tossup Game Replay

No tossup game replay metrics CSV was found.

## Calibration And Sharpness By Stratum

| scenario | stratum | value | observations | auc | log_loss | ece | brier | accuracy | all_correct_accuracy | accuracy_lift_over_all_correct | probability_std | probability_p10 | probability_p50 | probability_p90 | mean_predictive_variance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part_correctness | aggregate | all | 25866 | 0.890772 | 0.41746 | 0.0194317 | 0.133505 | 0.807315 | 0.525555 | 0.28176 | 0.342949 | 0.058817 | 0.53765 | 0.95696 | 0.131694 |
| bonus_part_correctness | tier | fall | 8259 | 0.890377 | 0.40979 | 0.02299 | 0.131843 | 0.805545 | 0.601283 | 0.204262 | 0.330843 | 0.105239 | 0.671342 | 0.967577 | 0.130819 |
| bonus_part_correctness | tier | nationals | 4167 | 0.883434 | 0.429654 | 0.0341321 | 0.136874 | 0.808015 | 0.438445 | 0.36957 | 0.328483 | 0.0553352 | 0.436252 | 0.919776 | 0.141049 |
| bonus_part_correctness | tier | regionals | 5457 | 0.885673 | 0.425965 | 0.0192448 | 0.136457 | 0.805754 | 0.493861 | 0.311893 | 0.343508 | 0.0470406 | 0.468552 | 0.949776 | 0.131913 |
| bonus_part_correctness | tier | winter | 7983 | 0.893532 | 0.413215 | 0.0222895 | 0.131448 | 0.809846 | 0.514343 | 0.295503 | 0.349844 | 0.0447467 | 0.498603 | 0.955407 | 0.127565 |
| bonus_part_correctness | category | Current Events | 258 | 0.879158 | 0.441516 | 0.0584746 | 0.141069 | 0.790698 | 0.515504 | 0.275194 | 0.352758 | 0.0644666 | 0.61378 | 0.945374 | 0.12491 |
| bonus_part_correctness | category | Fine Arts | 3000 | 0.884672 | 0.427765 | 0.0274955 | 0.13741 | 0.806333 | 0.508 | 0.298333 | 0.333208 | 0.0690737 | 0.519344 | 0.950643 | 0.138687 |
| bonus_part_correctness | category | Geography | 450 | 0.887973 | 0.418798 | 0.0387929 | 0.134726 | 0.808889 | 0.582222 | 0.226667 | 0.332069 | 0.101281 | 0.737967 | 0.962083 | 0.126217 |
| bonus_part_correctness | category | History | 4116 | 0.897088 | 0.403124 | 0.0186395 | 0.129171 | 0.807823 | 0.562196 | 0.245627 | 0.341263 | 0.0654958 | 0.614484 | 0.962329 | 0.129753 |
| bonus_part_correctness | category | Literature | 4092 | 0.893481 | 0.41134 | 0.0240094 | 0.131099 | 0.81305 | 0.522727 | 0.290323 | 0.346377 | 0.0591598 | 0.502029 | 0.960194 | 0.12966 |
| bonus_part_correctness | category | Mythology | 951 | 0.887362 | 0.412224 | 0.0413948 | 0.131702 | 0.804416 | 0.647739 | 0.156677 | 0.3195 | 0.110634 | 0.670765 | 0.967251 | 0.135996 |
| bonus_part_correctness | category | Other Academic | 276 | 0.909824 | 0.385963 | 0.0377107 | 0.121122 | 0.833333 | 0.532609 | 0.300725 | 0.354099 | 0.0563541 | 0.631938 | 0.954457 | 0.12185 |
| bonus_part_correctness | category | Philosophy | 957 | 0.876437 | 0.448946 | 0.0381827 | 0.14307 | 0.794148 | 0.474399 | 0.319749 | 0.332872 | 0.0494953 | 0.492539 | 0.939033 | 0.139196 |
| bonus_part_correctness | category | Popular Culture | 300 | 0.885875 | 0.404444 | 0.0739397 | 0.133607 | 0.783333 | 0.616667 | 0.166667 | 0.307816 | 0.146675 | 0.694338 | 0.972238 | 0.137605 |
| bonus_part_correctness | category | Religion | 1029 | 0.90009 | 0.401985 | 0.0488255 | 0.129145 | 0.804665 | 0.501458 | 0.303207 | 0.349374 | 0.050205 | 0.511725 | 0.94845 | 0.127831 |
| bonus_part_correctness | category | Science | 4089 | 0.88694 | 0.42506 | 0.0269107 | 0.13509 | 0.80582 | 0.533382 | 0.272438 | 0.342282 | 0.0643371 | 0.545784 | 0.958435 | 0.131652 |
| bonus_part_correctness | category | Social Science | 891 | 0.903075 | 0.386256 | 0.0512024 | 0.123751 | 0.822671 | 0.480359 | 0.342312 | 0.355905 | 0.0351253 | 0.425694 | 0.958715 | 0.122904 |
| bonus_part_correctness | category | Unknown | 5457 | 0.885673 | 0.425965 | 0.0192448 | 0.136457 | 0.805754 | 0.493861 | 0.311893 | 0.343508 | 0.0470406 | 0.468552 | 0.949776 | 0.131913 |

## Posterior Predictive Checks

No saved posterior predictive draws were available.

## No-Synergy Versus Synergy Deltas

No bonus model comparison CSV was found.

## Pyramidal Player And Tossup Parameters

No pyramidal parameter distribution summary CSV was found.

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum | parameter_source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 3768 | -0.204185 | 1.23979 | -2.71699 | -2.24556 | -1.25141 | -0.14012 | 0.831525 | 1.65654 | 2.16948 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/compositional |
| bonus_part | alpha_1 | 3768 | 0.792697 | 0.425968 | 0.18322 | 0.306556 | 0.441143 | 0.695336 | 1.06186 | 1.59606 | 2.86817 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/compositional |
| bonus_part | alpha_2 | 3768 | 0.748689 | 0.391634 | 0.211026 | 0.327772 | 0.427869 | 0.636919 | 0.979594 | 1.50237 | 2.77493 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/compositional |
| bonus_part | alpha_3 | 3768 | 0.774288 | 0.411051 | 0.188207 | 0.311754 | 0.439326 | 0.675956 | 1.02978 | 1.53135 | 2.96442 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/compositional |
| bonus_part | alpha_norm | 3768 | 1.39708 | 0.583378 | 0.483213 | 0.595783 | 0.863229 | 1.35019 | 1.85978 | 2.36077 | 3.51405 | /teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/double-difficulty/bonuses-normalized-v1-20260913-150350/fold_4/train/compositional |
