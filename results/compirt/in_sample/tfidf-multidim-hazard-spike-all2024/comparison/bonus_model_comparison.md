# CompIRT Bonus Model Comparison

| metric | no_synergy | synergy | synergy_minus_no_synergy | better_in_sample |
| --- | --- | --- | --- | --- |
| auc | 0.919742 | 0.924446 | 0.00470428 | synergy |
| log_loss | 0.368009 | 0.357296 | -0.0107127 | synergy |
| ece | 0.0373874 | 0.0356475 | -0.00173996 | synergy |
| accuracy | 0.837526 | 0.842711 | 0.00518504 | synergy |
| part_accuracy | 0.837526 | 0.842711 | 0.00518504 | synergy |
| exact_acc | 0.576101 | 0.588914 | 0.0128127 | synergy |
| per_bonus_points_mae | 5.12906 | 4.87721 | -0.251851 | synergy |
| ppb_mae | 2.27471 | 1.9496 | -0.325109 | synergy |

These metrics use the same observations for training and evaluation. They diagnose fit but do not establish that synergy generalizes to unseen team compositions.
