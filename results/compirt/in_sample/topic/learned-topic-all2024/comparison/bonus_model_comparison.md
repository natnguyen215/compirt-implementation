# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.908621 | 0.916082 | 0.0074612 | synergy |
| log_loss | 0.400035 | 0.381829 | -0.018206 | synergy |
| ece | 0.0643658 | 0.0525872 | -0.0117786 | synergy |
| part_accuracy | 0.821933 | 0.835952 | 0.0140191 | synergy |
| part_accuracy_macro_team | 0.82478 | 0.838422 | 0.0136422 | synergy |
| part_accuracy_macro_game | 0.821776 | 0.836172 | 0.0143968 | synergy |
| part_accuracy_macro_bonus | 0.806527 | 0.831819 | 0.025292 | synergy |
| exact_acc | 0.544294 | 0.573089 | 0.0287949 | synergy |
| ppb_mae | 1.94098 | 0.745437 | -1.19554 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
