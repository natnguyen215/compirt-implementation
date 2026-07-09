# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.908908 | 0.917102 | 0.00819383 | synergy |
| log_loss | 0.380935 | 0.365193 | -0.0157425 | synergy |
| ece | 0.00665973 | 0.0111717 | 0.00451194 | no-synergy |
| accuracy | 0.825582 | 0.834468 | 0.00888649 | synergy |
| part_accuracy | 0.825582 | 0.834468 | 0.00888649 | synergy |
| exact_acc | 0.549621 | 0.569739 | 0.0201182 | synergy |
| per_bonus_points_mae | 5.21139 | 4.98293 | -0.22846 | synergy |
| ppb_mae | 2.31376 | 1.73168 | -0.582083 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
