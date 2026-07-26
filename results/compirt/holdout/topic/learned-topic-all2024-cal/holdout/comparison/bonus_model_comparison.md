# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.91557 | 0.924418 | 0.00884849 | synergy |
| log_loss | 0.367116 | 0.349253 | -0.0178621 | synergy |
| ece | 0.00873569 | 0.0133964 | 0.00466075 | no-synergy |
| part_accuracy | 0.832727 | 0.844659 | 0.0119319 | synergy |
| part_accuracy_macro_team | 0.833564 | 0.845921 | 0.0123561 | synergy |
| part_accuracy_macro_game | 0.833 | 0.84509 | 0.0120895 | synergy |
| part_accuracy_macro_bonus | 0.842 | 0.850455 | 0.00845507 | synergy |
| exact_acc | 0.562494 | 0.589225 | 0.0267311 | synergy |
| ppb_mae | 1.69111 | 0.456804 | -1.2343 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
