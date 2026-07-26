# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.904623 | 0.912869 | 0.00824554 | synergy |
| log_loss | 0.409574 | 0.390657 | -0.0189167 | synergy |
| ece | 0.0707294 | 0.0609813 | -0.00974809 | synergy |
| part_accuracy | 0.816125 | 0.833841 | 0.0177159 | synergy |
| part_accuracy_macro_team | 0.818909 | 0.835974 | 0.0170653 | synergy |
| part_accuracy_macro_game | 0.816401 | 0.834301 | 0.0179007 | synergy |
| part_accuracy_macro_bonus | 0.793945 | 0.828449 | 0.0345035 | synergy |
| exact_acc | 0.527624 | 0.566348 | 0.0387237 | synergy |
| ppb_mae | 1.9993 | 0.603698 | -1.39561 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
