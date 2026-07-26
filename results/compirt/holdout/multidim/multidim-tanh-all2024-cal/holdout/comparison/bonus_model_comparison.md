# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.925767 | 0.930128 | 0.00436118 | synergy |
| log_loss | 0.35033 | 0.340836 | -0.00949429 | synergy |
| ece | 0.0281366 | 0.0273278 | -0.000808869 | synergy |
| part_accuracy | 0.843666 | 0.850939 | 0.00727275 | synergy |
| part_accuracy_macro_team | 0.844557 | 0.852141 | 0.00758453 | synergy |
| part_accuracy_macro_game | 0.843953 | 0.851306 | 0.00735301 | synergy |
| part_accuracy_macro_bonus | 0.854361 | 0.860163 | 0.00580198 | synergy |
| exact_acc | 0.588447 | 0.606494 | 0.0180468 | synergy |
| ppb_mae | 1.75481 | 0.649599 | -1.10521 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
