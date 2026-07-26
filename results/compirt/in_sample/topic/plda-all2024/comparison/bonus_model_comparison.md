# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.903899 | 0.913454 | 0.00955532 | synergy |
| log_loss | 0.416895 | 0.393717 | -0.0231778 | synergy |
| ece | 0.0795391 | 0.0646788 | -0.0148602 | synergy |
| part_accuracy | 0.813586 | 0.833996 | 0.0204105 | synergy |
| part_accuracy_macro_team | 0.818199 | 0.835996 | 0.0177968 | synergy |
| part_accuracy_macro_game | 0.813384 | 0.834276 | 0.0208926 | synergy |
| part_accuracy_macro_bonus | 0.794929 | 0.830191 | 0.0352622 | synergy |
| exact_acc | 0.527323 | 0.568076 | 0.0407535 | synergy |
| ppb_mae | 2.1892 | 0.740042 | -1.44916 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
