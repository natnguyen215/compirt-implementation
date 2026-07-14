# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.915671 | 0.920613 | 0.00494138 | synergy |
| log_loss | 0.383908 | 0.372648 | -0.0112597 | synergy |
| ece | 0.0565121 | 0.0559651 | -0.000546993 | synergy |
| accuracy | 0.835484 | 0.841996 | 0.00651184 | synergy |
| part_accuracy | 0.835484 | 0.841996 | 0.00651184 | synergy |
| exact_acc | 0.568565 | 0.58375 | 0.0151851 | synergy |
| per_bonus_points_mae | 5.05806 | 4.86024 | -0.19782 | synergy |
| ppb_mae | 2.14669 | 1.6915 | -0.455192 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
