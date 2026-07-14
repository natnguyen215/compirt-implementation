# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.932678 | 0.939241 | 0.00656315 | synergy |
| log_loss | 0.342423 | 0.327827 | -0.0145957 | synergy |
| ece | 0.0411874 | 0.0435584 | 0.00237102 | no-synergy |
| accuracy | 0.852594 | 0.859008 | 0.00641386 | synergy |
| part_accuracy | 0.852594 | 0.859008 | 0.00641386 | synergy |
| exact_acc | 0.612404 | 0.627015 | 0.014611 | synergy |
| per_bonus_points_mae | 4.83864 | 4.54743 | -0.291203 | synergy |
| ppb_mae | 2.19379 | 1.74084 | -0.452956 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
