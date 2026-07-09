# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.920995 | 0.925582 | 0.00458725 | synergy |
| log_loss | 0.366105 | 0.35573 | -0.010375 | synergy |
| ece | 0.0388104 | 0.0375613 | -0.00124909 | synergy |
| accuracy | 0.838567 | 0.843602 | 0.00503518 | synergy |
| part_accuracy | 0.838567 | 0.843602 | 0.00503518 | synergy |
| exact_acc | 0.579068 | 0.591431 | 0.0123632 | synergy |
| per_bonus_points_mae | 5.10018 | 4.85701 | -0.243174 | synergy |
| ppb_mae | 2.24734 | 1.94933 | -0.298014 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
