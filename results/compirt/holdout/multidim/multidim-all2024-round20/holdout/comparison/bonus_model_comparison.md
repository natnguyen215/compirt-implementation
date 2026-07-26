# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.939166 | 0.950372 | 0.0112067 | synergy |
| log_loss | 0.362611 | 0.337456 | -0.0251551 | synergy |
| ece | 0.0919266 | 0.096014 | 0.00408742 | no-synergy |
| brier | 0.108595 | 0.101071 | -0.00752427 | synergy |
| accuracy_lift_over_all_correct | 0.352141 | 0.359276 | 0.00713543 | synergy |
| part_accuracy | 0.86197 | 0.869105 | 0.00713543 | synergy |
| part_accuracy_macro_team | 0.869828 | 0.87753 | 0.00770237 | synergy |
| part_accuracy_macro_game | 0.86287 | 0.869829 | 0.00695924 | synergy |
| part_accuracy_macro_bonus | 0.896265 | 0.879982 | -0.0162821 | no-synergy |
| exact_acc | 0.635526 | 0.65438 | 0.0188546 | synergy |
| ranked_probability_score | 0.0993972 | 0.0906584 | -0.0087388 | synergy |
| bonus_total_score_log_loss | 0.892599 | 0.831634 | -0.0609647 | synergy |
| ppb_mae | 2.45854 | 1.8091 | -0.649441 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
