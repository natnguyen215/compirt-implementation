# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.904664 | 0.927831 | 0.0231677 | synergy |
| log_loss | 0.393597 | 0.347097 | -0.0465 | synergy |
| ece | 0.0258666 | 0.0297489 | 0.00388227 | no-synergy |
| part_accuracy | 0.821214 | 0.848323 | 0.027109 | synergy |
| part_accuracy_macro_team | 0.822742 | 0.850983 | 0.0282408 | synergy |
| part_accuracy_macro_game | 0.821361 | 0.848868 | 0.0275071 | synergy |
| part_accuracy_macro_bonus | 0.82273 | 0.848751 | 0.0260214 | synergy |
| exact_acc | 0.543305 | 0.602198 | 0.0588936 | synergy |
| ppb_mae | 2.51394 | 0.613089 | -1.90085 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
