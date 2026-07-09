# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.928679 | 0.934497 | 0.00581828 | synergy |
| log_loss | 0.342165 | 0.330613 | -0.011552 | synergy |
| ece | 0.0183743 | 0.0230218 | 0.00464754 | no-synergy |
| accuracy | 0.846472 | 0.854482 | 0.00800983 | synergy |
| part_accuracy | 0.846472 | 0.854482 | 0.00800983 | synergy |
| exact_acc | 0.597163 | 0.614899 | 0.0177355 | synergy |
| per_bonus_points_mae | 4.79037 | 4.60687 | -0.183498 | synergy |
| ppb_mae | 2.04274 | 1.66101 | -0.381722 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
