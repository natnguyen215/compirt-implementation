# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.926833 | 0.935844 | 0.00901157 | synergy |
| log_loss | 0.35305 | 0.333794 | -0.0192555 | synergy |
| ece | 0.0384582 | 0.040041 | 0.00158276 | no-synergy |
| accuracy | 0.847123 | 0.856072 | 0.00894895 | synergy |
| part_accuracy | 0.847123 | 0.856072 | 0.00894895 | synergy |
| exact_acc | 0.595941 | 0.617792 | 0.0218513 | synergy |
| per_bonus_points_mae | 5.05987 | 4.65716 | -0.402712 | synergy |
| ppb_mae | 2.33471 | 1.72912 | -0.60559 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
