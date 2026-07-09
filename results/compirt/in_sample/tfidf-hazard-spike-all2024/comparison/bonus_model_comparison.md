# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.91835 | 0.930545 | 0.0121952 | synergy |
| log_loss | 0.367102 | 0.343603 | -0.0234986 | synergy |
| ece | 0.0282857 | 0.0352786 | 0.00699293 | no-synergy |
| accuracy | 0.835428 | 0.849087 | 0.0136594 | synergy |
| part_accuracy | 0.835428 | 0.849087 | 0.0136594 | synergy |
| exact_acc | 0.574055 | 0.604087 | 0.0300312 | synergy |
| per_bonus_points_mae | 5.15446 | 4.75804 | -0.396421 | synergy |
| ppb_mae | 2.51519 | 1.80026 | -0.714928 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
