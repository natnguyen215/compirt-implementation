# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_1/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/tfidf-multidim-ablation-gamma/dim_1`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 1 |
| pyramidal | steps | 3000 |
| pyramidal | final_loss | 470216 |
| pyramidal | calibrate_correctness | False |
| synergy | tournament | all tournaments |
| synergy | dimensions | 1 |
| synergy | steps | 2000 |
| synergy | final_loss | 81094.3 |
| synergy | calibrate_correctness | False |
| synergy | synergy_dimensions | 1 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.0154747 |
| mean_synergy_contribution | 0.0180342 |
| median_synergy_contribution | 0 |
| negative_synergy_fraction | 0.496162 |
| positive_synergy_fraction | 0.479455 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.919107 |
| log_loss | 0.368168 |
| ece | 0.0361416 |
| part_accuracy | 0.837811 |
| part_accuracy_macro_team | 0.839145 |
| part_accuracy_macro_game | 0.838209 |
| part_accuracy_macro_bonus | 0.845326 |
| exact_acc | 0.574569 |
| ppb_mae | 0.51059 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.627418 |
| log_loss | 0.636677 |
| ece | 0.160861 |
| accuracy | 0.678471 |
| buzz_position_mae | 0.145446 |
| buzz_position_median_absolute_error | 0.123203 |

## No-Synergy Versus Synergy Deltas

No sibling comparison/bonus_model_comparison.csv was found.

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 5.27986 | 0.989073 | 1.30289 | 3.29842 | 4.84282 | 5.3921 | 5.89117 | 6.63588 | 7.8989 |
| player | theta_1 | 1755 | -0.112651 | 0.617324 | -3.09243 | -1.3074 | -0.319434 | -0.0246508 | 0.251263 | 0.657926 | 1.24242 |
| player | theta_norm | 1755 | 0.419403 | 0.466677 | 3.52924e-05 | 0.0248781 | 0.126215 | 0.282155 | 0.522748 | 1.3074 | 3.09243 |
| tossup | beta_1 | 1350 | 1.49085 | 0.522601 | -0.280814 | 0.623836 | 1.09756 | 1.49309 | 1.88077 | 2.29753 | 3.07156 |
| tossup | gamma_1 | 1350 | 56.8448 | 197.732 | 0.0482031 | 1.49261 | 4.08141 | 6.96384 | 17.403 | 283.898 | 2363.32 |
| tossup | mu_1 | 1350 | 0.621719 | 0.189076 | 0.0701999 | 0.302867 | 0.494091 | 0.618699 | 0.760433 | 0.942072 | 0.994606 |
| tossup | r_1 | 1350 | 3.01092 | 1.32844 | 0.446894 | 1.38848 | 2.06377 | 2.74165 | 3.74277 | 5.63826 | 8.94723 |
| tossup | r_norm | 1350 | 3.01092 | 1.32844 | 0.446894 | 1.38848 | 2.06377 | 2.74165 | 3.74277 | 5.63826 | 8.94723 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.161936 | 1.5794 | -3.58218 | -2.44911 | -1.19726 | 0.298047 | 1.4779 | 2.49092 | 3.74957 |
| bonus_part | alpha_1 | 4716 | 0.890402 | 0.515174 | 0.2496 | 0.37749 | 0.543704 | 0.764171 | 1.05765 | 1.7815 | 5.30409 |
| bonus_part | alpha_norm | 4716 | 0.890402 | 0.515174 | 0.2496 | 0.37749 | 0.543704 | 0.764171 | 1.05765 | 1.7815 | 5.30409 |
