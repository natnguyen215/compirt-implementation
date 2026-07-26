# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.908908 | 0.917102 | 0.00819383 | synergy |
| log_loss | 0.380935 | 0.365193 | -0.0157425 | synergy |
| ece | 0.00665973 | 0.0111717 | 0.00451194 | no-synergy |
| part_accuracy | 0.825582 | 0.834468 | 0.00888649 | synergy |
| part_accuracy_macro_team | 0.827881 | 0.836384 | 0.00850356 | synergy |
| part_accuracy_macro_game | 0.825736 | 0.834751 | 0.00901521 | synergy |
| part_accuracy_macro_bonus | 0.831701 | 0.838009 | 0.00630813 | synergy |
| exact_acc | 0.549621 | 0.569739 | 0.0201182 | synergy |
| ppb_mae | 1.53968 | 0.526738 | -1.01294 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
