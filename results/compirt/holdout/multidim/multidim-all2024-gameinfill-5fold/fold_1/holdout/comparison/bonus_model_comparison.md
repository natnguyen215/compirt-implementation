# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.886937 | 0.895033 | 0.00809623 | synergy |
| log_loss | 0.424365 | 0.412246 | -0.0121185 | synergy |
| ece | 0.0171191 | 0.0296166 | 0.0124975 | no-synergy |
| brier | 0.13514 | 0.131349 | -0.00379076 | synergy |
| accuracy_lift_over_all_correct | 0.288599 | 0.294933 | 0.00633413 | synergy |
| part_accuracy | 0.807601 | 0.813935 | 0.00633413 | synergy |
| part_accuracy_macro_team | 0.811346 | 0.815481 | 0.0041355 | synergy |
| part_accuracy_macro_bonus | 0.80443 | 0.81202 | 0.00759039 | synergy |
| exact_acc | 0.516033 | 0.527316 | 0.0112827 | synergy |
| ranked_probability_score | 0.115895 | 0.111424 | -0.00447144 | synergy |
| bonus_total_score_log_loss | 1.01453 | 0.983064 | -0.0314695 | synergy |
| ppb_mae | 2.37596 | 1.96012 | -0.415845 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
