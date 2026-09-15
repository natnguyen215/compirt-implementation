# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.887122 | 0.893603 | 0.00648163 | synergy |
| log_loss | 0.42405 | 0.413455 | -0.0105948 | synergy |
| ece | 0.0166041 | 0.0239176 | 0.00731347 | no-synergy |
| brier | 0.134864 | 0.131928 | -0.00293557 | synergy |
| accuracy_lift_over_all_correct | 0.291425 | 0.292664 | 0.00123945 | synergy |
| part_accuracy | 0.809861 | 0.811101 | 0.00123945 | synergy |
| part_accuracy_macro_team | 0.811903 | 0.812432 | 0.000528696 | synergy |
| part_accuracy_macro_bonus | 0.805403 | 0.808617 | 0.00321426 | synergy |
| exact_acc | 0.51313 | 0.515571 | 0.00244016 | synergy |
| ranked_probability_score | 0.117189 | 0.113096 | -0.00409343 | synergy |
| bonus_total_score_log_loss | 1.02505 | 0.996407 | -0.0286404 | synergy |
| ppb_mae | 2.36785 | 1.81969 | -0.548168 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
