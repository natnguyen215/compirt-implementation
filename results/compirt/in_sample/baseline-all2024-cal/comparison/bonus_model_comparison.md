# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.930449 | 0.93325 | 0.00280107 | synergy |
| log_loss | 0.341971 | 0.337717 | -0.00425355 | synergy |
| ece | 0.0328726 | 0.0362837 | 0.00341105 | no-synergy |
| accuracy | 0.847439 | 0.851859 | 0.00442077 | synergy |
| part_accuracy | 0.847439 | 0.851859 | 0.00442077 | synergy |
| exact_acc | 0.60067 | 0.610043 | 0.00937352 | synergy |
| per_bonus_points_mae | 4.87996 | 4.67697 | -0.202989 | synergy |
| ppb_mae | 2.27113 | 1.76554 | -0.505585 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
