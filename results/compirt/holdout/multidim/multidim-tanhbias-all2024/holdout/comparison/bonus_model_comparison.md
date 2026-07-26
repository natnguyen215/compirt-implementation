# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.927318 | 0.938054 | 0.0107367 | synergy |
| log_loss | 0.339205 | 0.314144 | -0.0250606 | synergy |
| ece | 0.00837581 | 0.00380027 | -0.00457554 | synergy |
| part_accuracy | 0.842552 | 0.857335 | 0.0147826 | synergy |
| part_accuracy_macro_team | 0.842337 | 0.857711 | 0.0153736 | synergy |
| part_accuracy_macro_game | 0.842776 | 0.857649 | 0.014873 | synergy |
| part_accuracy_macro_bonus | 0.858138 | 0.871275 | 0.0131379 | synergy |
| exact_acc | 0.587868 | 0.620571 | 0.0327026 | synergy |
| ppb_mae | 1.77381 | 0.412961 | -1.36085 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
