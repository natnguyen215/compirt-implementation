# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.911241 | 0.930739 | 0.0194986 | synergy |
| log_loss | 0.378279 | 0.339997 | -0.0382825 | synergy |
| ece | 0.0186362 | 0.0277283 | 0.00909204 | no-synergy |
| part_accuracy | 0.827687 | 0.850272 | 0.0225847 | synergy |
| part_accuracy_macro_team | 0.828648 | 0.851535 | 0.0228868 | synergy |
| part_accuracy_macro_game | 0.828205 | 0.850688 | 0.0224832 | synergy |
| part_accuracy_macro_bonus | 0.827157 | 0.861585 | 0.0344286 | synergy |
| exact_acc | 0.554124 | 0.605502 | 0.0513779 | synergy |
| ppb_mae | 2.32404 | 0.552226 | -1.77181 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
