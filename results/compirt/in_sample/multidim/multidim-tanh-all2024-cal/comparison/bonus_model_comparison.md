# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.927551 | 0.930311 | 0.00276002 | synergy |
| log_loss | 0.349442 | 0.34214 | -0.00730175 | synergy |
| ece | 0.0352078 | 0.0309183 | -0.0042895 | synergy |
| part_accuracy | 0.844404 | 0.849709 | 0.00530492 | synergy |
| part_accuracy_macro_team | 0.845488 | 0.851072 | 0.0055843 | synergy |
| part_accuracy_macro_game | 0.844588 | 0.84989 | 0.00530237 | synergy |
| part_accuracy_macro_bonus | 0.850389 | 0.851735 | 0.0013461 | synergy |
| exact_acc | 0.592937 | 0.605368 | 0.0124306 | synergy |
| ppb_mae | 1.82848 | 0.788364 | -1.04011 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
