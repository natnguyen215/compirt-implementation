# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.910852 | 0.917969 | 0.00711632 | synergy |
| log_loss | 0.390789 | 0.373174 | -0.0176158 | synergy |
| ece | 0.0536683 | 0.0410241 | -0.0126442 | synergy |
| part_accuracy | 0.825312 | 0.837818 | 0.0125055 | synergy |
| part_accuracy_macro_team | 0.828182 | 0.839702 | 0.0115201 | synergy |
| part_accuracy_macro_game | 0.825204 | 0.837968 | 0.0127639 | synergy |
| part_accuracy_macro_bonus | 0.81442 | 0.83599 | 0.0215697 | synergy |
| exact_acc | 0.548969 | 0.576213 | 0.0272439 | synergy |
| ppb_mae | 1.84142 | 0.716918 | -1.1245 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
