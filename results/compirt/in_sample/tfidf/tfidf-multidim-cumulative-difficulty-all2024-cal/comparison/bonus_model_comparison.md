# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.928679 | 0.934497 | 0.00581828 | synergy |
| log_loss | 0.342165 | 0.330613 | -0.011552 | synergy |
| ece | 0.0183743 | 0.0230218 | 0.00464754 | no-synergy |
| part_accuracy | 0.846472 | 0.854482 | 0.00800983 | synergy |
| part_accuracy_macro_team | 0.84877 | 0.856319 | 0.00754927 | synergy |
| part_accuracy_macro_game | 0.846498 | 0.854567 | 0.00806912 | synergy |
| part_accuracy_macro_bonus | 0.851405 | 0.857408 | 0.00600345 | synergy |
| exact_acc | 0.597163 | 0.614899 | 0.0177355 | synergy |
| ppb_mae | 1.30245 | 0.592242 | -0.710206 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
