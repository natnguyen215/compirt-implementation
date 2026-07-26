# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.936507 | 0.937058 | 0.000551069 | synergy |
| log_loss | 0.330569 | 0.329052 | -0.00151681 | synergy |
| ece | 0.0390519 | 0.0370202 | -0.00203175 | synergy |
| brier | 0.10326 | 0.102179 | -0.00108093 | synergy |
| accuracy_lift_over_all_correct | 0.33385 | 0.33645 | 0.00260001 | synergy |
| part_accuracy | 0.854339 | 0.856939 | 0.00260001 | synergy |
| part_accuracy_macro_team | 0.85652 | 0.859393 | 0.00287372 | synergy |
| part_accuracy_macro_game | 0.854685 | 0.857336 | 0.00265074 | synergy |
| part_accuracy_macro_bonus | 0.861601 | 0.860519 | -0.00108124 | no-synergy |
| exact_acc | 0.617012 | 0.623261 | 0.00624902 | synergy |
| ranked_probability_score | 0.0938353 | 0.0912963 | -0.00253901 | synergy |
| bonus_total_score_log_loss | 0.836281 | 0.822843 | -0.0134378 | synergy |
| ppb_mae | 1.55185 | 0.846956 | -0.704891 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
