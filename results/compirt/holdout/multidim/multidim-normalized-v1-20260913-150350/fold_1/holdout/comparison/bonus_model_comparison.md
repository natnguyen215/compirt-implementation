# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.88705 | 0.895076 | 0.00802578 | synergy |
| log_loss | 0.424268 | 0.412245 | -0.0120228 | synergy |
| ece | 0.017465 | 0.0298494 | 0.0123844 | no-synergy |
| brier | 0.135077 | 0.131336 | -0.00374053 | synergy |
| accuracy_lift_over_all_correct | 0.288599 | 0.294656 | 0.00605701 | synergy |
| part_accuracy | 0.807601 | 0.813658 | 0.00605701 | synergy |
| part_accuracy_macro_team | 0.811147 | 0.814874 | 0.00372705 | synergy |
| part_accuracy_macro_bonus | 0.804574 | 0.811703 | 0.0071289 | synergy |
| exact_acc | 0.516746 | 0.526128 | 0.00938242 | synergy |
| ranked_probability_score | 0.115834 | 0.111419 | -0.00441518 | synergy |
| bonus_total_score_log_loss | 1.01423 | 0.98312 | -0.0311109 | synergy |
| ppb_mae | 2.37194 | 1.96136 | -0.410583 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
