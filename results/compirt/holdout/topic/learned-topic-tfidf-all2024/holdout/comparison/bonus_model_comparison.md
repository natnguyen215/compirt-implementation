# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.915671 | 0.920613 | 0.00494138 | synergy |
| log_loss | 0.383908 | 0.372648 | -0.0112597 | synergy |
| ece | 0.0565121 | 0.0559651 | -0.000546993 | synergy |
| part_accuracy | 0.835484 | 0.841996 | 0.00651184 | synergy |
| part_accuracy_macro_team | 0.836636 | 0.843601 | 0.00696525 | synergy |
| part_accuracy_macro_game | 0.835732 | 0.842397 | 0.00666522 | synergy |
| part_accuracy_macro_bonus | 0.827187 | 0.837406 | 0.0102197 | synergy |
| exact_acc | 0.568565 | 0.58375 | 0.0151851 | synergy |
| ppb_mae | 1.38685 | 0.49215 | -0.8947 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
