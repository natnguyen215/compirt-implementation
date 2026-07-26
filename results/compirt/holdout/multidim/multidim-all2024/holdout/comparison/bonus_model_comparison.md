# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.926833 | 0.935844 | 0.00901157 | synergy |
| log_loss | 0.35305 | 0.333794 | -0.0192555 | synergy |
| ece | 0.0384582 | 0.040041 | 0.00158276 | no-synergy |
| part_accuracy | 0.847123 | 0.856072 | 0.00894895 | synergy |
| part_accuracy_macro_team | 0.849199 | 0.858234 | 0.00903482 | synergy |
| part_accuracy_macro_game | 0.847631 | 0.856581 | 0.00894993 | synergy |
| part_accuracy_macro_bonus | 0.85991 | 0.864618 | 0.00470782 | synergy |
| exact_acc | 0.595941 | 0.617792 | 0.0218513 | synergy |
| ppb_mae | 1.7272 | 0.779055 | -0.948146 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
