# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.924131 | 0.934156 | 0.0100249 | synergy |
| log_loss | 0.358455 | 0.337141 | -0.0213141 | synergy |
| ece | 0.0366069 | 0.0389809 | 0.00237403 | no-synergy |
| brier | 0.111821 | 0.104816 | -0.00700466 | synergy |
| accuracy_lift_over_all_correct | 0.322806 | 0.332299 | 0.00949341 | synergy |
| part_accuracy | 0.843295 | 0.852788 | 0.00949341 | synergy |
| part_accuracy_macro_team | 0.845959 | 0.855759 | 0.00979968 | synergy |
| part_accuracy_macro_game | 0.843711 | 0.853329 | 0.00961888 | synergy |
| part_accuracy_macro_bonus | 0.851473 | 0.856721 | 0.00524836 | synergy |
| exact_acc | 0.590217 | 0.612471 | 0.0222537 | synergy |
| ranked_probability_score | 0.102047 | 0.0936624 | -0.00838462 | synergy |
| bonus_total_score_log_loss | 0.900859 | 0.843012 | -0.0578469 | synergy |
| ppb_mae | 1.97857 | 0.8459 | -1.13267 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
