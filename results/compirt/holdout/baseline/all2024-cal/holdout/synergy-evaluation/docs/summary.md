# CompIRT Evaluation Summary

Evaluation folder: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/all2024-cal/holdout/synergy-evaluation`
Result root: `/teapot/students/natnguyen/CompIRT-Implementation/results/compirt/holdout/all2024-cal`

This file consolidates the metric CSVs, bonus-model comparison deltas, and fitted-parameter distribution summaries for quick review.

**Evaluation regime: transductive temporal holdout.** Returning-player priors come from the training split, but question parameters are co-estimated on the test-split outcomes being scored (paper Section 4.2), so these metrics are not fully inductive predictions of unseen questions.

**Correctness calibration was fit on the scored outcomes.** This run learned a Platt scale/bias on the same split these metrics score, so tossup ECE and log loss are flattered by construction and are not comparable to uncalibrated runs.

## Run Variables And Stage Scalars

| stage | field | value |
| --- | --- | --- |
| pyramidal | tournament | all tournaments |
| pyramidal | dimensions | 5 |
| pyramidal | steps | 5000 |
| pyramidal | final_loss | 453236 |
| pyramidal | calibrate_correctness | True |
| synergy | tournament | all tournaments |
| synergy | dimensions | 5 |
| synergy | steps | 3000 |
| synergy | final_loss | 84395.6 |
| synergy | calibrate_correctness | True |
| synergy | synergy_dimensions | 3 |

## Bonus Stage Scalars

| field | value |
| --- | --- |
| tau | 0.48899 |
| mean_synergy_contribution | 0.392416 |
| median_synergy_contribution | 0.313542 |
| negative_synergy_fraction | 0.315165 |
| positive_synergy_fraction | 0.660453 |

## Stage 2 Bonus Metrics

| metric | value |
| --- | --- |
| auc | 0.932626 |
| log_loss | 0.335881 |
| ece | 0.0286101 |
| part_accuracy | 0.852852 |
| part_accuracy_macro_team | 0.854272 |
| part_accuracy_macro_game | 0.853226 |
| part_accuracy_macro_bonus | 0.862939 |
| exact_acc | 0.611291 |
| ppb_mae | 0.697841 |

## Stage 1 Tossup Metrics

| metric | value |
| --- | --- |
| auc | 0.630624 |
| log_loss | 0.520031 |
| ece | 0.0118527 |
| accuracy | 0.771077 |
| buzz_position_mae | 0.137267 |
| buzz_position_median_absolute_error | 0.11807 |

## No-Synergy Versus Synergy Deltas

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.929564 | 0.932626 | 0.00306151 | synergy |
| log_loss | 0.34149 | 0.335881 | -0.00560899 | synergy |
| ece | 0.0268148 | 0.0286101 | 0.00179532 | no-synergy |
| part_accuracy | 0.847631 | 0.852852 | 0.0052216 | synergy |
| part_accuracy_macro_team | 0.848914 | 0.854272 | 0.0053586 | synergy |
| part_accuracy_macro_game | 0.848022 | 0.853226 | 0.00520495 | synergy |
| part_accuracy_macro_bonus | 0.858451 | 0.862939 | 0.0044879 | synergy |
| exact_acc | 0.598091 | 0.611291 | 0.0132001 | synergy |
| ppb_mae | 1.51927 | 0.697841 | -0.82143 | synergy |

## Pyramidal Player And Tossup Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| player | c | 1755 | 1.4317 | 0.603907 | -0.325915 | 0.467042 | 1.00887 | 1.40904 | 1.83342 | 2.48035 | 3.66229 |
| player | theta_1 | 1755 | 1.22293 | 0.507999 | -0.641644 | 0.353356 | 0.887629 | 1.25834 | 1.58084 | 1.99659 | 3.07936 |
| player | theta_2 | 1755 | 0.240113 | 0.624155 | -1.86318 | -0.674213 | -0.177823 | 0.171768 | 0.598633 | 1.35321 | 2.83106 |
| player | theta_3 | 1755 | 1.01111 | 0.44711 | -0.82587 | 0.235275 | 0.751772 | 1.04845 | 1.2946 | 1.70938 | 2.45766 |
| player | theta_4 | 1755 | 0.536001 | 0.657487 | -1.77645 | -0.669554 | 0.125967 | 0.624821 | 0.999384 | 1.51505 | 2.40403 |
| player | theta_5 | 1755 | 0.523896 | 0.767195 | -2.10031 | -0.743562 | -0.0268291 | 0.54383 | 1.10834 | 1.71428 | 2.82676 |
| player | theta_norm | 1755 | 2.19093 | 0.452328 | 0.850866 | 1.42609 | 1.88698 | 2.18791 | 2.50845 | 2.94251 | 3.53843 |
| tossup | beta | 1350 | 3.7846 | 0.776799 | 0.729853 | 2.50687 | 3.36219 | 3.78042 | 4.27951 | 4.91997 | 7.22907 |
| tossup | gamma | 1350 | 59.1859 | 187.419 | 3.42459 | 6.13964 | 9.16061 | 13.0087 | 25.8248 | 234.06 | 2064.57 |
| tossup | mu | 1350 | 0.637176 | 0.135423 | 0.14524 | 0.413451 | 0.548255 | 0.637642 | 0.723742 | 0.857187 | 0.993332 |
| tossup | alpha_1 | 1350 | -1.36575 | 0.616562 | -2.98741 | -2.31815 | -1.79205 | -1.38153 | -0.969476 | -0.337749 | 0.743578 |
| tossup | alpha_2 | 1350 | -0.29962 | 0.703684 | -2.53949 | -1.48614 | -0.773172 | -0.295511 | 0.13588 | 0.894626 | 2.14733 |
| tossup | alpha_3 | 1350 | -1.0416 | 0.608499 | -3.18043 | -2.02842 | -1.40884 | -1.04001 | -0.663997 | -0.0241797 | 1.26231 |
| tossup | alpha_4 | 1350 | -0.457134 | 0.774136 | -2.91404 | -1.69951 | -1.00399 | -0.453008 | 0.13044 | 0.784304 | 1.69631 |
| tossup | alpha_5 | 1350 | -0.357359 | 0.80261 | -2.35115 | -1.50551 | -0.999591 | -0.467421 | 0.229352 | 1.03495 | 2.21464 |
| tossup | alpha_norm | 1350 | 2.37264 | 0.484348 | 0.706383 | 1.54981 | 2.04489 | 2.39974 | 2.69855 | 3.1251 | 3.76717 |

## Bonus And Synergy Parameters

| group | parameter | observations | mean | standard_deviation | minimum | p05 | p25 | median | p75 | p95 | maximum |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| bonus_part | beta | 4716 | 0.000462377 | 0.913328 | -1.82281 | -1.31994 | -0.763147 | -0.0391627 | 0.710308 | 1.5441 | 2.2377 |
| bonus_part | alpha_1 | 4716 | -0.0443127 | 0.883665 | -2.55988 | -1.30973 | -0.78911 | -0.115092 | 0.703024 | 1.45283 | 2.14115 |
| bonus_part | alpha_2 | 4716 | -0.0210214 | 0.566811 | -1.87043 | -0.850019 | -0.413806 | -0.0301972 | 0.321236 | 0.928453 | 2.89455 |
| bonus_part | alpha_3 | 4716 | -0.0203684 | 0.824216 | -2.32328 | -1.23591 | -0.718725 | -0.0449425 | 0.676053 | 1.32045 | 1.65175 |
| bonus_part | alpha_4 | 4716 | -0.111466 | 0.609994 | -3.11313 | -1.19657 | -0.422537 | -0.0696846 | 0.256554 | 0.746973 | 2.10908 |
| bonus_part | alpha_5 | 4716 | -0.0676609 | 0.590108 | -2.45107 | -1.07666 | -0.455749 | -0.0720389 | 0.359034 | 0.822452 | 1.87264 |
| bonus_part | alpha_norm | 4716 | 1.4908 | 0.546508 | 0.0990115 | 0.541039 | 1.11788 | 1.5415 | 1.85921 | 2.35688 | 3.49028 |
| synergy_player | psi_1 | 1755 | 0.0082213 | 0.306937 | -1.67542 | -0.495569 | -0.0479443 | 0.00296212 | 0.0586527 | 0.507895 | 2.25738 |
| synergy_player | psi_2 | 1755 | 0.00266497 | 0.307764 | -1.91263 | -0.494765 | -0.0533565 | 0.000526158 | 0.0508118 | 0.522966 | 1.59015 |
| synergy_player | psi_3 | 1755 | 0.00989206 | 0.291759 | -1.5664 | -0.474542 | -0.0508386 | 0.00190708 | 0.0567276 | 0.535879 | 1.56502 |
| synergy_player | psi_norm | 1755 | 0.416194 | 0.317662 | 0.00798531 | 0.0476978 | 0.165893 | 0.37115 | 0.563975 | 1.08432 | 2.25816 |
| synergy | synergy_score | 3042 | 0.0293596 | 0.306846 | -2.78625 | -0.482604 | -0.0139559 | 0.0350605 | 0.166258 | 0.395886 | 1.43671 |
| synergy | synergy_contribution | 60454 | 0.392416 | 0.878699 | -3.99609 | -1.03534 | -0.0693305 | 0.313542 | 1.02932 | 1.73987 | 4.25005 |
