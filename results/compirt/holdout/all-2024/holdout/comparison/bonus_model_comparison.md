# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.932352 | 0.938384 | 0.00603197 | synergy |
| log_loss | 0.340014 | 0.325596 | -0.0144186 | synergy |
| ece | 0.0370095 | 0.0358433 | -0.00116626 | synergy |
| accuracy | 0.852323 | 0.858691 | 0.00636848 | synergy |
| part_accuracy | 0.852323 | 0.858691 | 0.00636848 | synergy |
| exact_acc | 0.609306 | 0.624094 | 0.0147881 | synergy |
| per_bonus_points_mae | 4.86941 | 4.57135 | -0.298059 | synergy |
| ppb_mae | 2.12287 | 1.65731 | -0.465569 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
