# Bonus difficulty, team tournament PPG and game margins

Saved predictions from the same five whole-game folds as the original comparison; no parameters were refit by this analysis. DD sources use skills from the normalized first-buzz likelihood. Difficulty is the source's declared part label, not part position or fitted difficulty. Each roster group has one easy, medium and hard part per bonus; no labels are unknown.

The always-predict-correct baseline over all rosters is 90.94% easy, 49.34% medium, 16.21% hard. This equals the observed correct-answer rate. Baselines are shared by both models and synergy settings; n counts parts per configuration.

## Familiar roster

| Model | Synergy | Bonuses | Part acc. ↑ | Easy acc. ↑ (n = 40,549) | Medium acc. ↑ (n = 40,549) | Hard acc. ↑ (n = 40,549) | Exact bonus acc. ↑ | AUC ↑ | Log loss ↓ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD additive phi-psi 1D | on | 40549 | 81.67% | 90.78% | 69.96% | 84.28% | 52.91% | 0.898214 | 0.404256 |
| DD additive phi-psi 3D | on | 40549 | 81.72% | 90.80% | 70.01% | 84.34% | 53.00% | 0.898231 | 0.404363 |
| DD multidim difficulty additive dot 1D | on | 40549 | 81.76% | 90.31% | 70.54% | 84.43% | 53.31% | 0.899326 | 0.400859 |
| DD multidim difficulty additive dot 3D | on | 40549 | 81.78% | 90.34% | 70.61% | 84.39% | 53.30% | 0.899307 | 0.401237 |
| DD multiplicative dot 1D | on | 40549 | 80.80% | 90.67% | 68.03% | 83.71% | 50.98% | 0.89022 | 0.418185 |
| DD multiplicative dot 3D | on | 40549 | 80.80% | 90.64% | 68.07% | 83.69% | 51.00% | 0.890178 | 0.418344 |
| DD multiplicative phi-psi 1D | on | 40549 | 80.90% | 90.69% | 68.22% | 83.80% | 51.19% | 0.890528 | 0.41754 |
| DD multiplicative phi-psi 3D | on | 40549 | 80.91% | 90.71% | 68.24% | 83.78% | 51.26% | 0.890406 | 0.417623 |
| DD-Bernstein | off | 40549 | 80.82% | 90.66% | 68.06% | 83.75% | 51.09% | 0.890515 | 0.418109 |
| DD-Bernstein | on | 40549 | 81.69% | 90.80% | 70.10% | 84.16% | 52.93% | 0.898772 | 0.403682 |
| Multidim | off | 40549 | 80.80% | 90.80% | 67.79% | 83.80% | 51.14% | 0.888037 | 0.422893 |
| Multidim | on | 40549 | 81.48% | 90.06% | 70.07% | 84.32% | 52.61% | 0.896831 | 0.409438 |

Always-predict-correct baseline: 91.02% easy, 49.57% medium, 16.29% hard.

## New roster, known players

| Model | Synergy | Bonuses | Part acc. ↑ | Easy acc. ↑ (n = 2,151) | Medium acc. ↑ (n = 2,151) | Hard acc. ↑ (n = 2,151) | Exact bonus acc. ↑ | AUC ↑ | Log loss ↓ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD additive phi-psi 1D | on | 2151 | 81.28% | 89.49% | 68.90% | 85.45% | 52.86% | 0.887799 | 0.426189 |
| DD additive phi-psi 3D | on | 2151 | 81.39% | 89.45% | 68.99% | 85.73% | 53.56% | 0.889257 | 0.424104 |
| DD multidim difficulty additive dot 1D | on | 2151 | 81.37% | 89.45% | 68.76% | 85.91% | 53.70% | 0.889547 | 0.423685 |
| DD multidim difficulty additive dot 3D | on | 2151 | 81.56% | 89.54% | 69.46% | 85.68% | 53.60% | 0.890984 | 0.422556 |
| DD multiplicative dot 1D | on | 2151 | 81.13% | 89.68% | 67.50% | 86.19% | 52.63% | 0.888533 | 0.423046 |
| DD multiplicative dot 3D | on | 2151 | 81.33% | 89.77% | 68.20% | 86.01% | 53.18% | 0.888945 | 0.423376 |
| DD multiplicative phi-psi 1D | on | 2151 | 81.08% | 89.82% | 67.55% | 85.87% | 52.39% | 0.888567 | 0.421157 |
| DD multiplicative phi-psi 3D | on | 2151 | 80.97% | 89.68% | 67.27% | 85.96% | 52.25% | 0.888568 | 0.420892 |
| DD-Bernstein | off | 2151 | 81.09% | 89.77% | 67.55% | 85.96% | 52.63% | 0.888371 | 0.422197 |
| DD-Bernstein | on | 2151 | 81.28% | 89.91% | 68.29% | 85.63% | 53.37% | 0.887278 | 0.427293 |
| Multidim | off | 2151 | 81.39% | 90.10% | 67.92% | 86.15% | 52.77% | 0.889247 | 0.419169 |
| Multidim | on | 2151 | 79.70% | 89.45% | 65.50% | 84.15% | 49.28% | 0.875336 | 0.445376 |

Always-predict-correct baseline: 89.40% easy, 44.91% medium, 14.60% hard.

## Bonus-only team PPG and margins

Sum each team's observed or expected points on its recorded bonuses. Expected response points are 10 times the sum of the three part probabilities. Divide by unique games played, including zero-bonus games. All held-out folds are pooled before computing team PPG. Each team's absolute PPG error is in the leaderboard CSV; tournament MAE averages these errors. Spearman ranks teams within each mirror tournament with average ranks for ties. Constant rankings have undefined correlation and are excluded from its macro mean. Games with incomplete bonus predictions are excluded entirely. Bonus margin is team A's points minus team B's in a game, with teams ordered by ID. Its MAE averages absolute errors in these signed margins, one vote per game. Both metrics are conditional on the actual bonus opportunities; bonus ownership is not replayed.

| model | arm | tournament_team_bonus_ppg_mae | tournament_team_bonus_ppg_spearman | bonus_ppg_tournaments | bonus_ppg_spearman_tournaments | bonus_ppg_incomplete_games | bonus_ppg_games | bonus_game_margin_mae | bonus_game_margin_mae_games |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD additive phi-psi 1D | synergy | 9.28186 | 0.935755 | 29 | 29 | 99 | 2332 | 26.8987 | 2332 |
| DD additive phi-psi 3D | synergy | 9.20848 | 0.93272 | 29 | 29 | 99 | 2332 | 26.7811 | 2332 |
| DD multidim difficulty additive dot 1D | synergy | 6.88966 | 0.944202 | 29 | 29 | 99 | 2332 | 25.76 | 2332 |
| DD multidim difficulty additive dot 3D | synergy | 6.87354 | 0.943242 | 29 | 29 | 99 | 2332 | 25.7625 | 2332 |
| DD multiplicative dot 1D | synergy | 17.9726 | 0.885137 | 29 | 29 | 99 | 2332 | 33.358 | 2332 |
| DD multiplicative dot 3D | synergy | 17.9744 | 0.88433 | 29 | 29 | 99 | 2332 | 33.4498 | 2332 |
| DD multiplicative phi-psi 1D | synergy | 18.0157 | 0.883893 | 29 | 29 | 99 | 2332 | 33.2195 | 2332 |
| DD multiplicative phi-psi 3D | synergy | 18.0476 | 0.883945 | 29 | 29 | 99 | 2332 | 33.3571 | 2332 |
| DD-Bernstein | compositional | 18.0353 | 0.887232 | 29 | 29 | 99 | 2332 | 33.2264 | 2332 |
| DD-Bernstein | synergy | 8.2974 | 0.93717 | 29 | 29 | 99 | 2332 | 26.5344 | 2332 |
| Multidim | compositional | 18.7633 | 0.958326 | 29 | 29 | 99 | 2332 | 32.1506 | 2332 |
| Multidim | synergy | 10.9749 | 0.969583 | 29 | 29 | 99 | 2332 | 26.6835 | 2332 |

[All tournament metrics](bonus_ppg_by_tournament.csv). The PPG summary averages tournaments equally after computing their metrics; the overall margin MAE weights games equally.

- DD additive phi-psi 1D synergy: [team PPG and errors](bonus_metrics/DD additive phi-psi 1D/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD additive phi-psi 1D/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD additive phi-psi 1D/synergy/bonus_game_margin_predictions.csv).
- DD additive phi-psi 3D synergy: [team PPG and errors](bonus_metrics/DD additive phi-psi 3D/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD additive phi-psi 3D/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD additive phi-psi 3D/synergy/bonus_game_margin_predictions.csv).
- DD multidim difficulty additive dot 1D synergy: [team PPG and errors](bonus_metrics/DD multidim difficulty additive dot 1D/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD multidim difficulty additive dot 1D/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD multidim difficulty additive dot 1D/synergy/bonus_game_margin_predictions.csv).
- DD multidim difficulty additive dot 3D synergy: [team PPG and errors](bonus_metrics/DD multidim difficulty additive dot 3D/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD multidim difficulty additive dot 3D/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD multidim difficulty additive dot 3D/synergy/bonus_game_margin_predictions.csv).
- DD multiplicative dot 1D synergy: [team PPG and errors](bonus_metrics/DD multiplicative dot 1D/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD multiplicative dot 1D/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD multiplicative dot 1D/synergy/bonus_game_margin_predictions.csv).
- DD multiplicative dot 3D synergy: [team PPG and errors](bonus_metrics/DD multiplicative dot 3D/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD multiplicative dot 3D/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD multiplicative dot 3D/synergy/bonus_game_margin_predictions.csv).
- DD multiplicative phi-psi 1D synergy: [team PPG and errors](bonus_metrics/DD multiplicative phi-psi 1D/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD multiplicative phi-psi 1D/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD multiplicative phi-psi 1D/synergy/bonus_game_margin_predictions.csv).
- DD multiplicative phi-psi 3D synergy: [team PPG and errors](bonus_metrics/DD multiplicative phi-psi 3D/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD multiplicative phi-psi 3D/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD multiplicative phi-psi 3D/synergy/bonus_game_margin_predictions.csv).
- DD-Bernstein compositional: [team PPG and errors](bonus_metrics/DD-Bernstein/compositional/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD-Bernstein/compositional/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD-Bernstein/compositional/bonus_game_margin_predictions.csv).
- DD-Bernstein synergy: [team PPG and errors](bonus_metrics/DD-Bernstein/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD-Bernstein/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD-Bernstein/synergy/bonus_game_margin_predictions.csv).
- Multidim compositional: [team PPG and errors](bonus_metrics/Multidim/compositional/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/Multidim/compositional/bonus_team_game_predictions.csv), [game margins](bonus_metrics/Multidim/compositional/bonus_game_margin_predictions.csv).
- Multidim synergy: [team PPG and errors](bonus_metrics/Multidim/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/Multidim/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/Multidim/synergy/bonus_game_margin_predictions.csv).

## Per-tournament results

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae | model | arm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 6.79704 | 1 | 27.3528 | DD additive phi-psi 1D | synergy |
| 2024-acf-fall-at-cornell | 18 | 89 | 6.75801 | 0.95302 | 25.9539 | DD additive phi-psi 1D | synergy |
| 2024-acf-fall-at-georgia | 24 | 124 | 4.42157 | 0.993043 | 26.6686 | DD additive phi-psi 1D | synergy |
| 2024-acf-fall-at-illinois | 20 | 99 | 6.24581 | 0.98797 | 26.6842 | DD additive phi-psi 1D | synergy |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 10.5774 | 0.918797 | 29.6134 | DD additive phi-psi 1D | synergy |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 5.47797 | 0.995872 | 25.6462 | DD additive phi-psi 1D | synergy |
| 2024-acf-fall-at-rutgers | 17 | 92 | 11.3974 | 0.889706 | 33.6367 | DD additive phi-psi 1D | synergy |
| 2024-acf-fall-at-washington | 14 | 64 | 5.33369 | 0.986813 | 26.403 | DD additive phi-psi 1D | synergy |
| 2024-acf-nationals | 48 | 400 | 6.06676 | 0.982685 | 23.0056 | DD additive phi-psi 1D | synergy |
| 2024-acf-regionals-berkeley | 6 | 30 | 3.53823 | 1 | 23.9702 | DD additive phi-psi 1D | synergy |
| 2024-acf-regionals-cornell | 6 | 31 | 14.8468 | 0.657143 | 35.2481 | DD additive phi-psi 1D | synergy |
| 2024-acf-regionals-imperial | 16 | 89 | 9.78591 | 0.964706 | 27.7975 | DD additive phi-psi 1D | synergy |
| 2024-acf-regionals-jmu | 20 | 120 | 9.15867 | 0.971429 | 22.5912 | DD additive phi-psi 1D | synergy |
| 2024-acf-regionals-minnesota | 4 | 20 | 6.47536 | 0.8 | 23.7128 | DD additive phi-psi 1D | synergy |
| 2024-acf-regionals-mit | 12 | 14 | 17.9002 | 0.970229 | 30.2897 | DD additive phi-psi 1D | synergy |
| 2024-acf-regionals-nebraska | 12 | 67 | 14.7402 | 0.888112 | 31.4587 | DD additive phi-psi 1D | synergy |
| 2024-acf-regionals-ohio-state | 7 | 28 | 9.21018 | 1 | 22.1097 | DD additive phi-psi 1D | synergy |
| 2024-acf-regionals-rutgers | 11 | 56 | 13.596 | 0.963636 | 32.658 | DD additive phi-psi 1D | synergy |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 15.4276 | 0.9 | 32.987 | DD additive phi-psi 1D | synergy |
| 2024-acf-winter-at-brandeis | 21 | 85 | 8.82973 | 0.983756 | 23.7413 | DD additive phi-psi 1D | synergy |
| 2024-acf-winter-at-central-florida | 11 | 49 | 7.28332 | 0.972727 | 20.1899 | DD additive phi-psi 1D | synergy |
| 2024-acf-winter-at-clemson | 18 | 85 | 6.39382 | 0.931819 | 25.6337 | DD additive phi-psi 1D | synergy |
| 2024-acf-winter-at-lehigh | 15 | 65 | 5.70458 | 0.985714 | 23.8844 | DD additive phi-psi 1D | synergy |
| 2024-acf-winter-at-northwestern | 21 | 98 | 5.28854 | 0.994479 | 24.4951 | DD additive phi-psi 1D | synergy |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 10.6971 | 0.984211 | 28.2387 | DD additive phi-psi 1D | synergy |
| 2024-acf-winter-at-online | 18 | 96 | 9.43211 | 0.941662 | 30.0152 | DD additive phi-psi 1D | synergy |
| 2024-acf-winter-at-oxford | 22 | 96 | 10.787 | 0.862225 | 31.3659 | DD additive phi-psi 1D | synergy |
| 2024-acf-winter-at-ubc | 6 | 30 | 4.84393 | 1 | 27.8162 | DD additive phi-psi 1D | synergy |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 22.1591 | 0.657143 | 52.4853 | DD additive phi-psi 1D | synergy |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 6.69669 | 0.963636 | 25.9241 | DD additive phi-psi 3D | synergy |
| 2024-acf-fall-at-cornell | 18 | 89 | 6.40175 | 0.970573 | 25.1114 | DD additive phi-psi 3D | synergy |
| 2024-acf-fall-at-georgia | 24 | 124 | 5.09694 | 0.989565 | 27.0121 | DD additive phi-psi 3D | synergy |
| 2024-acf-fall-at-illinois | 20 | 99 | 5.44379 | 0.981955 | 28.0017 | DD additive phi-psi 3D | synergy |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 9.61772 | 0.920301 | 30.2758 | DD additive phi-psi 3D | synergy |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 3.69693 | 0.995872 | 23.5497 | DD additive phi-psi 3D | synergy |
| 2024-acf-fall-at-rutgers | 17 | 92 | 9.84777 | 0.906863 | 32.6315 | DD additive phi-psi 3D | synergy |
| 2024-acf-fall-at-washington | 14 | 64 | 5.91906 | 0.964835 | 26.8303 | DD additive phi-psi 3D | synergy |
| 2024-acf-nationals | 48 | 400 | 6.17416 | 0.977745 | 22.8004 | DD additive phi-psi 3D | synergy |
| 2024-acf-regionals-berkeley | 6 | 30 | 2.87396 | 1 | 23.0115 | DD additive phi-psi 3D | synergy |
| 2024-acf-regionals-cornell | 6 | 31 | 14.3256 | 0.657143 | 33.9443 | DD additive phi-psi 3D | synergy |
| 2024-acf-regionals-imperial | 16 | 89 | 11.7395 | 0.955882 | 28.7173 | DD additive phi-psi 3D | synergy |
| 2024-acf-regionals-jmu | 20 | 120 | 8.87071 | 0.981955 | 22.7859 | DD additive phi-psi 3D | synergy |
| 2024-acf-regionals-minnesota | 4 | 20 | 8.78694 | 0.8 | 28.8247 | DD additive phi-psi 3D | synergy |
| 2024-acf-regionals-mit | 12 | 14 | 16.9831 | 0.970229 | 28.5579 | DD additive phi-psi 3D | synergy |
| 2024-acf-regionals-nebraska | 12 | 67 | 13.3788 | 0.867133 | 31.7241 | DD additive phi-psi 3D | synergy |
| 2024-acf-regionals-ohio-state | 7 | 28 | 10.5291 | 1 | 22.6699 | DD additive phi-psi 3D | synergy |
| 2024-acf-regionals-rutgers | 11 | 56 | 13.6456 | 0.963636 | 32.0141 | DD additive phi-psi 3D | synergy |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 14.7751 | 0.9 | 32.4356 | DD additive phi-psi 3D | synergy |
| 2024-acf-winter-at-brandeis | 21 | 85 | 9.0295 | 0.983756 | 23.6692 | DD additive phi-psi 3D | synergy |
| 2024-acf-winter-at-central-florida | 11 | 49 | 7.51863 | 0.972727 | 21.1313 | DD additive phi-psi 3D | synergy |
| 2024-acf-winter-at-clemson | 18 | 85 | 6.77057 | 0.95248 | 25.2611 | DD additive phi-psi 3D | synergy |
| 2024-acf-winter-at-lehigh | 15 | 65 | 4.73635 | 0.989286 | 22.5204 | DD additive phi-psi 3D | synergy |
| 2024-acf-winter-at-northwestern | 21 | 98 | 5.32888 | 0.994479 | 25.1632 | DD additive phi-psi 3D | synergy |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 8.98292 | 0.984211 | 27.4875 | DD additive phi-psi 3D | synergy |
| 2024-acf-winter-at-online | 18 | 96 | 9.83705 | 0.945793 | 28.8313 | DD additive phi-psi 3D | synergy |
| 2024-acf-winter-at-oxford | 22 | 96 | 11.2381 | 0.858837 | 32.5862 | DD additive phi-psi 3D | synergy |
| 2024-acf-winter-at-ubc | 6 | 30 | 5.19025 | 0.942857 | 27.0143 | DD additive phi-psi 3D | synergy |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 23.6103 | 0.657143 | 51.6925 | DD additive phi-psi 3D | synergy |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 4.22152 | 0.987879 | 30.6293 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-fall-at-cornell | 18 | 89 | 4.60881 | 0.978833 | 25.0497 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-fall-at-georgia | 24 | 124 | 2.58589 | 0.995652 | 26.0923 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-fall-at-illinois | 20 | 99 | 4.53019 | 0.981955 | 24.7236 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 6.70011 | 0.944361 | 28.5215 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 2.93744 | 1 | 22.6093 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-fall-at-rutgers | 17 | 92 | 9.60421 | 0.904412 | 32.8391 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-fall-at-washington | 14 | 64 | 3.23524 | 0.982418 | 26.9867 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-nationals | 48 | 400 | 3.11558 | 0.982576 | 21.605 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-regionals-berkeley | 6 | 30 | 3.78351 | 1 | 25.9115 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-regionals-cornell | 6 | 31 | 14.2948 | 0.657143 | 35.7212 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-regionals-imperial | 16 | 89 | 5.02502 | 0.964706 | 23.8789 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-regionals-jmu | 20 | 120 | 4.6655 | 0.993985 | 20.9634 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-regionals-minnesota | 4 | 20 | 5.40884 | 0.8 | 25.8896 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-regionals-mit | 12 | 14 | 15.1416 | 0.977234 | 24.1248 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-regionals-nebraska | 12 | 67 | 9.65375 | 0.951049 | 32.0355 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-regionals-ohio-state | 7 | 28 | 6.5025 | 1 | 22.5671 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-regionals-rutgers | 11 | 56 | 12.5033 | 0.963636 | 28.8075 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 11.1219 | 0.927273 | 26.3122 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-winter-at-brandeis | 21 | 85 | 5.96665 | 0.987655 | 24.3465 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-winter-at-central-florida | 11 | 49 | 4.94087 | 1 | 18.4416 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-winter-at-clemson | 18 | 85 | 4.29255 | 0.970042 | 23.9905 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-winter-at-lehigh | 15 | 65 | 4.46456 | 0.982143 | 23.15 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-winter-at-northwestern | 21 | 98 | 3.727 | 0.989282 | 24.8328 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 6.4195 | 0.978947 | 25.5999 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-winter-at-online | 18 | 96 | 9.54299 | 0.94889 | 28.8882 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-winter-at-oxford | 22 | 96 | 9.52197 | 0.874647 | 32.9295 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-winter-at-ubc | 6 | 30 | 2.10221 | 1 | 28.2932 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 19.1822 | 0.657143 | 48.2101 | DD multidim difficulty additive dot 1D | synergy |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 4.24806 | 0.987879 | 31.3324 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-fall-at-cornell | 18 | 89 | 4.41591 | 0.978833 | 25.6505 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-fall-at-georgia | 24 | 124 | 3.00169 | 0.995652 | 26.796 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-fall-at-illinois | 20 | 99 | 4.12318 | 0.98797 | 25.8583 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 6.39104 | 0.93985 | 28.0497 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 3.12529 | 1 | 23.0719 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-fall-at-rutgers | 17 | 92 | 9.6014 | 0.901961 | 33.3075 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-fall-at-washington | 14 | 64 | 4.41219 | 0.986813 | 26.7982 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-nationals | 48 | 400 | 3.25991 | 0.986267 | 21.7568 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-regionals-berkeley | 6 | 30 | 4.51282 | 1 | 26.7552 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-regionals-cornell | 6 | 31 | 14.3699 | 0.657143 | 36.6672 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-regionals-imperial | 16 | 89 | 5.14035 | 0.964706 | 24.5196 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-regionals-jmu | 20 | 120 | 5.275 | 0.989474 | 20.7307 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-regionals-minnesota | 4 | 20 | 5.41658 | 0.8 | 25.7196 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-regionals-mit | 12 | 14 | 15.8727 | 0.970229 | 25.1089 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-regionals-nebraska | 12 | 67 | 9.90585 | 0.93007 | 32.0676 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-regionals-ohio-state | 7 | 28 | 7.14286 | 1 | 22.6722 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-regionals-rutgers | 11 | 56 | 11.5601 | 0.972727 | 29.4502 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 11.0572 | 0.927273 | 26.9644 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-winter-at-brandeis | 21 | 85 | 5.20761 | 0.985055 | 22.9791 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-winter-at-central-florida | 11 | 49 | 3.58127 | 0.990909 | 18.1986 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-winter-at-clemson | 18 | 85 | 4.84222 | 0.963843 | 23.5317 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-winter-at-lehigh | 15 | 65 | 3.87446 | 0.982143 | 20.4503 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-winter-at-northwestern | 21 | 98 | 3.98853 | 0.985385 | 25.0781 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 5.69771 | 0.985965 | 25.3124 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-winter-at-online | 18 | 96 | 8.58202 | 0.950955 | 27.4862 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-winter-at-oxford | 22 | 96 | 9.41634 | 0.875776 | 32.4633 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-winter-at-ubc | 6 | 30 | 1.541 | 1 | 28.2673 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 19.7696 | 0.657143 | 48.0108 | DD multidim difficulty additive dot 3D | synergy |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 4.74779 | 1 | 27.5117 | DD multiplicative dot 1D | synergy |
| 2024-acf-fall-at-cornell | 18 | 89 | 17.2563 | 0.792979 | 31.8859 | DD multiplicative dot 1D | synergy |
| 2024-acf-fall-at-georgia | 24 | 124 | 14.3332 | 0.93913 | 33.8718 | DD multiplicative dot 1D | synergy |
| 2024-acf-fall-at-illinois | 20 | 99 | 13.3512 | 0.962406 | 30.9585 | DD multiplicative dot 1D | synergy |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 14.1295 | 0.896241 | 29.1685 | DD multiplicative dot 1D | synergy |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 18.071 | 0.925697 | 33.798 | DD multiplicative dot 1D | synergy |
| 2024-acf-fall-at-rutgers | 17 | 92 | 14.8596 | 0.887255 | 36.1283 | DD multiplicative dot 1D | synergy |
| 2024-acf-fall-at-washington | 14 | 64 | 16.9526 | 0.881319 | 35.1761 | DD multiplicative dot 1D | synergy |
| 2024-acf-nationals | 48 | 400 | 16.0942 | 0.863214 | 32.1416 | DD multiplicative dot 1D | synergy |
| 2024-acf-regionals-berkeley | 6 | 30 | 27.2264 | 0.828571 | 45.5462 | DD multiplicative dot 1D | synergy |
| 2024-acf-regionals-cornell | 6 | 31 | 24.5092 | 0.6 | 38.7515 | DD multiplicative dot 1D | synergy |
| 2024-acf-regionals-imperial | 16 | 89 | 18.6928 | 0.941176 | 36.4966 | DD multiplicative dot 1D | synergy |
| 2024-acf-regionals-jmu | 20 | 120 | 19.8045 | 0.93985 | 29.4184 | DD multiplicative dot 1D | synergy |
| 2024-acf-regionals-minnesota | 4 | 20 | 23.4559 | 0.8 | 44.7432 | DD multiplicative dot 1D | synergy |
| 2024-acf-regionals-mit | 12 | 14 | 22.0802 | 0.942208 | 35.3262 | DD multiplicative dot 1D | synergy |
| 2024-acf-regionals-nebraska | 12 | 67 | 16.609 | 0.881119 | 34.7816 | DD multiplicative dot 1D | synergy |
| 2024-acf-regionals-ohio-state | 7 | 28 | 12.016 | 1 | 25.1679 | DD multiplicative dot 1D | synergy |
| 2024-acf-regionals-rutgers | 11 | 56 | 22.6711 | 0.954545 | 37.9263 | DD multiplicative dot 1D | synergy |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 18.004 | 0.881818 | 37.2131 | DD multiplicative dot 1D | synergy |
| 2024-acf-winter-at-brandeis | 21 | 85 | 18.3013 | 0.962963 | 31.5343 | DD multiplicative dot 1D | synergy |
| 2024-acf-winter-at-central-florida | 11 | 49 | 14.4617 | 0.963636 | 25.1132 | DD multiplicative dot 1D | synergy |
| 2024-acf-winter-at-clemson | 18 | 85 | 15.5016 | 0.91529 | 32.8986 | DD multiplicative dot 1D | synergy |
| 2024-acf-winter-at-lehigh | 15 | 65 | 16.9275 | 0.964286 | 36.2163 | DD multiplicative dot 1D | synergy |
| 2024-acf-winter-at-northwestern | 21 | 98 | 16.6671 | 0.936668 | 33.71 | DD multiplicative dot 1D | synergy |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 20.723 | 0.938596 | 30.1468 | DD multiplicative dot 1D | synergy |
| 2024-acf-winter-at-online | 18 | 96 | 14.53 | 0.901394 | 33.0601 | DD multiplicative dot 1D | synergy |
| 2024-acf-winter-at-oxford | 22 | 96 | 14.4739 | 0.85432 | 34.1368 | DD multiplicative dot 1D | synergy |
| 2024-acf-winter-at-ubc | 6 | 30 | 19.6634 | 0.771429 | 36.9197 | DD multiplicative dot 1D | synergy |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 35.0919 | 0.542857 | 59.0516 | DD multiplicative dot 1D | synergy |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 4.96781 | 0.987879 | 27.24 | DD multiplicative dot 3D | synergy |
| 2024-acf-fall-at-cornell | 18 | 89 | 17.3714 | 0.786784 | 32.2671 | DD multiplicative dot 3D | synergy |
| 2024-acf-fall-at-georgia | 24 | 124 | 14.3205 | 0.93913 | 34.0455 | DD multiplicative dot 3D | synergy |
| 2024-acf-fall-at-illinois | 20 | 99 | 13.0981 | 0.962406 | 30.7743 | DD multiplicative dot 3D | synergy |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 14.2415 | 0.905263 | 29.1019 | DD multiplicative dot 3D | synergy |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 17.9537 | 0.925697 | 33.9603 | DD multiplicative dot 3D | synergy |
| 2024-acf-fall-at-rutgers | 17 | 92 | 15.0474 | 0.887255 | 36.265 | DD multiplicative dot 3D | synergy |
| 2024-acf-fall-at-washington | 14 | 64 | 17.1631 | 0.898901 | 35.5827 | DD multiplicative dot 3D | synergy |
| 2024-acf-nationals | 48 | 400 | 16.1282 | 0.865114 | 32.2575 | DD multiplicative dot 3D | synergy |
| 2024-acf-regionals-berkeley | 6 | 30 | 27.4261 | 0.828571 | 45.6204 | DD multiplicative dot 3D | synergy |
| 2024-acf-regionals-cornell | 6 | 31 | 24.4534 | 0.6 | 38.5301 | DD multiplicative dot 3D | synergy |
| 2024-acf-regionals-imperial | 16 | 89 | 18.6204 | 0.941176 | 36.8615 | DD multiplicative dot 3D | synergy |
| 2024-acf-regionals-jmu | 20 | 120 | 19.7207 | 0.936842 | 29.4974 | DD multiplicative dot 3D | synergy |
| 2024-acf-regionals-minnesota | 4 | 20 | 23.7179 | 0.8 | 44.7735 | DD multiplicative dot 3D | synergy |
| 2024-acf-regionals-mit | 12 | 14 | 21.8658 | 0.942208 | 35.2704 | DD multiplicative dot 3D | synergy |
| 2024-acf-regionals-nebraska | 12 | 67 | 16.336 | 0.881119 | 35.0909 | DD multiplicative dot 3D | synergy |
| 2024-acf-regionals-ohio-state | 7 | 28 | 11.8304 | 1 | 25.448 | DD multiplicative dot 3D | synergy |
| 2024-acf-regionals-rutgers | 11 | 56 | 22.7321 | 0.954545 | 38.1847 | DD multiplicative dot 3D | synergy |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 18.0496 | 0.881818 | 37.1007 | DD multiplicative dot 3D | synergy |
| 2024-acf-winter-at-brandeis | 21 | 85 | 18.0156 | 0.959065 | 31.6087 | DD multiplicative dot 3D | synergy |
| 2024-acf-winter-at-central-florida | 11 | 49 | 14.0621 | 0.963636 | 25.0183 | DD multiplicative dot 3D | synergy |
| 2024-acf-winter-at-clemson | 18 | 85 | 15.543 | 0.91529 | 33.1695 | DD multiplicative dot 3D | synergy |
| 2024-acf-winter-at-lehigh | 15 | 65 | 16.7714 | 0.95 | 35.6653 | DD multiplicative dot 3D | synergy |
| 2024-acf-winter-at-northwestern | 21 | 98 | 16.7655 | 0.936668 | 33.8221 | DD multiplicative dot 3D | synergy |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 20.4616 | 0.938596 | 30.0651 | DD multiplicative dot 3D | synergy |
| 2024-acf-winter-at-online | 18 | 96 | 14.557 | 0.889004 | 33.0894 | DD multiplicative dot 3D | synergy |
| 2024-acf-winter-at-oxford | 22 | 96 | 14.4512 | 0.85432 | 33.9246 | DD multiplicative dot 3D | synergy |
| 2024-acf-winter-at-ubc | 6 | 30 | 20.2314 | 0.771429 | 37.9719 | DD multiplicative dot 3D | synergy |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 35.3549 | 0.542857 | 59.5328 | DD multiplicative dot 3D | synergy |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 4.87281 | 0.987879 | 27.0795 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-fall-at-cornell | 18 | 89 | 16.7154 | 0.792979 | 31.5502 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-fall-at-georgia | 24 | 124 | 14.2439 | 0.946087 | 33.2843 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-fall-at-illinois | 20 | 99 | 13.8221 | 0.966917 | 31.2631 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 13.9988 | 0.902256 | 29.1449 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 18.1862 | 0.925697 | 33.8293 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-fall-at-rutgers | 17 | 92 | 14.8053 | 0.887255 | 35.2368 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-fall-at-washington | 14 | 64 | 17.0956 | 0.881319 | 35.3435 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-nationals | 48 | 400 | 16.0767 | 0.863486 | 31.9006 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-regionals-berkeley | 6 | 30 | 27.6711 | 0.828571 | 45.7109 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-regionals-cornell | 6 | 31 | 24.447 | 0.6 | 38.226 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-regionals-imperial | 16 | 89 | 18.2355 | 0.929412 | 36.1269 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-regionals-jmu | 20 | 120 | 19.729 | 0.948872 | 29.4012 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-regionals-minnesota | 4 | 20 | 24.0163 | 0.8 | 44.6289 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-regionals-mit | 12 | 14 | 22.2717 | 0.914187 | 36.2785 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-regionals-nebraska | 12 | 67 | 16.4768 | 0.881119 | 34.8719 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-regionals-ohio-state | 7 | 28 | 11.9635 | 1 | 25.3208 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-regionals-rutgers | 11 | 56 | 22.751 | 0.954545 | 37.9062 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 17.7171 | 0.881818 | 36.9268 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-winter-at-brandeis | 21 | 85 | 18.4657 | 0.962963 | 31.7184 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-winter-at-central-florida | 11 | 49 | 14.6136 | 0.963636 | 25.288 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-winter-at-clemson | 18 | 85 | 15.2926 | 0.91529 | 32.7102 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-winter-at-lehigh | 15 | 65 | 17.3747 | 0.95 | 36.7188 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-winter-at-northwestern | 21 | 98 | 16.3448 | 0.935369 | 33.3229 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 20.7792 | 0.942105 | 30.3526 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-winter-at-online | 18 | 96 | 14.8028 | 0.901394 | 32.9161 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-winter-at-oxford | 22 | 96 | 14.6421 | 0.855449 | 34.1681 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-winter-at-ubc | 6 | 30 | 19.7655 | 0.771429 | 36.3843 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 35.2788 | 0.542857 | 58.3752 | DD multiplicative phi-psi 1D | synergy |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 4.71125 | 0.987879 | 27.3279 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-fall-at-cornell | 18 | 89 | 16.9875 | 0.792979 | 31.8107 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-fall-at-georgia | 24 | 124 | 14.2815 | 0.946087 | 33.6681 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-fall-at-illinois | 20 | 99 | 13.7754 | 0.962406 | 31.2209 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 13.746 | 0.899248 | 28.9978 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 18.046 | 0.925697 | 34.0991 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-fall-at-rutgers | 17 | 92 | 15.0625 | 0.887255 | 35.7052 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-fall-at-washington | 14 | 64 | 17.1623 | 0.898901 | 35.3764 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-nationals | 48 | 400 | 16.0818 | 0.863486 | 32.0196 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-regionals-berkeley | 6 | 30 | 27.9085 | 0.828571 | 45.9644 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-regionals-cornell | 6 | 31 | 24.4194 | 0.6 | 38.1544 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-regionals-imperial | 16 | 89 | 18.4037 | 0.929412 | 36.5624 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-regionals-jmu | 20 | 120 | 19.6914 | 0.948872 | 29.3728 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-regionals-minnesota | 4 | 20 | 24.0706 | 0.8 | 44.4899 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-regionals-mit | 12 | 14 | 22.3039 | 0.914187 | 36.5212 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-regionals-nebraska | 12 | 67 | 16.3519 | 0.881119 | 34.934 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-regionals-ohio-state | 7 | 28 | 11.9277 | 1 | 25.4917 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-regionals-rutgers | 11 | 56 | 22.8848 | 0.954545 | 38.0691 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 17.7222 | 0.881818 | 37.0861 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-winter-at-brandeis | 21 | 85 | 18.4885 | 0.959065 | 31.7834 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-winter-at-central-florida | 11 | 49 | 14.3817 | 0.963636 | 25.3377 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-winter-at-clemson | 18 | 85 | 15.3504 | 0.91529 | 32.8642 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-winter-at-lehigh | 15 | 65 | 17.2358 | 0.95 | 36.5761 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-winter-at-northwestern | 21 | 98 | 16.7341 | 0.935369 | 33.8278 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 20.7438 | 0.938596 | 30.181 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-winter-at-online | 18 | 96 | 14.9592 | 0.901394 | 33.0241 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-winter-at-oxford | 22 | 96 | 14.6989 | 0.85432 | 34.2779 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-winter-at-ubc | 6 | 30 | 19.7891 | 0.771429 | 36.3975 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 35.4603 | 0.542857 | 58.5802 | DD multiplicative phi-psi 3D | synergy |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 5.1031 | 0.987879 | 27.2487 | DD-Bernstein | compositional |
| 2024-acf-fall-at-cornell | 18 | 89 | 16.719 | 0.792979 | 31.2112 | DD-Bernstein | compositional |
| 2024-acf-fall-at-georgia | 24 | 124 | 14.3856 | 0.946087 | 33.1438 | DD-Bernstein | compositional |
| 2024-acf-fall-at-illinois | 20 | 99 | 13.6037 | 0.974436 | 31.0526 | DD-Bernstein | compositional |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 14.3061 | 0.902256 | 29.0673 | DD-Bernstein | compositional |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 18.4381 | 0.925697 | 33.749 | DD-Bernstein | compositional |
| 2024-acf-fall-at-rutgers | 17 | 92 | 14.6807 | 0.887255 | 34.5423 | DD-Bernstein | compositional |
| 2024-acf-fall-at-washington | 14 | 64 | 16.9472 | 0.881319 | 35.3424 | DD-Bernstein | compositional |
| 2024-acf-nationals | 48 | 400 | 16.6854 | 0.857949 | 32.4499 | DD-Bernstein | compositional |
| 2024-acf-regionals-berkeley | 6 | 30 | 27.1388 | 0.942857 | 45.3545 | DD-Bernstein | compositional |
| 2024-acf-regionals-cornell | 6 | 31 | 24.551 | 0.6 | 37.8654 | DD-Bernstein | compositional |
| 2024-acf-regionals-imperial | 16 | 89 | 18.286 | 0.929412 | 35.7662 | DD-Bernstein | compositional |
| 2024-acf-regionals-jmu | 20 | 120 | 20.6239 | 0.93985 | 30.1071 | DD-Bernstein | compositional |
| 2024-acf-regionals-minnesota | 4 | 20 | 23.3598 | 0.8 | 44.5068 | DD-Bernstein | compositional |
| 2024-acf-regionals-mit | 12 | 14 | 21.8771 | 0.914187 | 35.7577 | DD-Bernstein | compositional |
| 2024-acf-regionals-nebraska | 12 | 67 | 16.8338 | 0.881119 | 34.8019 | DD-Bernstein | compositional |
| 2024-acf-regionals-ohio-state | 7 | 28 | 12.3796 | 1 | 25.5042 | DD-Bernstein | compositional |
| 2024-acf-regionals-rutgers | 11 | 56 | 21.9656 | 0.954545 | 37.1137 | DD-Bernstein | compositional |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 17.5854 | 0.881818 | 36.4959 | DD-Bernstein | compositional |
| 2024-acf-winter-at-brandeis | 21 | 85 | 18.5591 | 0.959065 | 31.4861 | DD-Bernstein | compositional |
| 2024-acf-winter-at-central-florida | 11 | 49 | 14.9953 | 0.963636 | 25.6437 | DD-Bernstein | compositional |
| 2024-acf-winter-at-clemson | 18 | 85 | 15.7741 | 0.907025 | 33.2507 | DD-Bernstein | compositional |
| 2024-acf-winter-at-lehigh | 15 | 65 | 17.1196 | 0.946429 | 36.1228 | DD-Bernstein | compositional |
| 2024-acf-winter-at-northwestern | 21 | 98 | 15.6915 | 0.936668 | 32.7001 | DD-Bernstein | compositional |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 21.1165 | 0.942105 | 30.421 | DD-Bernstein | compositional |
| 2024-acf-winter-at-online | 18 | 96 | 14.3933 | 0.906557 | 33.0976 | DD-Bernstein | compositional |
| 2024-acf-winter-at-oxford | 22 | 96 | 14.952 | 0.85432 | 34.0145 | DD-Bernstein | compositional |
| 2024-acf-winter-at-ubc | 6 | 30 | 19.5494 | 0.771429 | 36.3255 | DD-Bernstein | compositional |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 35.402 | 0.542857 | 59.4727 | DD-Bernstein | compositional |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 3.37698 | 0.939394 | 29.4918 | DD-Bernstein | synergy |
| 2024-acf-fall-at-cornell | 18 | 89 | 4.05514 | 0.980898 | 24.0819 | DD-Bernstein | synergy |
| 2024-acf-fall-at-georgia | 24 | 124 | 3.82921 | 0.995652 | 27.3154 | DD-Bernstein | synergy |
| 2024-acf-fall-at-illinois | 20 | 99 | 4.57798 | 0.992481 | 26.256 | DD-Bernstein | synergy |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 8.79497 | 0.938346 | 29.6933 | DD-Bernstein | synergy |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 5.89874 | 0.995872 | 23.6863 | DD-Bernstein | synergy |
| 2024-acf-fall-at-rutgers | 17 | 92 | 10.2303 | 0.894608 | 33.2033 | DD-Bernstein | synergy |
| 2024-acf-fall-at-washington | 14 | 64 | 4.49802 | 0.982418 | 27.7915 | DD-Bernstein | synergy |
| 2024-acf-nationals | 48 | 400 | 6.43381 | 0.985724 | 22.2521 | DD-Bernstein | synergy |
| 2024-acf-regionals-berkeley | 6 | 30 | 4.01955 | 1 | 28.5542 | DD-Bernstein | synergy |
| 2024-acf-regionals-cornell | 6 | 31 | 15.4928 | 0.657143 | 35.0756 | DD-Bernstein | synergy |
| 2024-acf-regionals-imperial | 16 | 89 | 10.6889 | 0.964706 | 26.7302 | DD-Bernstein | synergy |
| 2024-acf-regionals-jmu | 20 | 120 | 8.2529 | 0.983459 | 21.0772 | DD-Bernstein | synergy |
| 2024-acf-regionals-minnesota | 4 | 20 | 5.9765 | 0.8 | 24.8632 | DD-Bernstein | synergy |
| 2024-acf-regionals-mit | 12 | 14 | 12.8771 | 0.991245 | 19.6473 | DD-Bernstein | synergy |
| 2024-acf-regionals-nebraska | 12 | 67 | 13.9469 | 0.888112 | 31.4135 | DD-Bernstein | synergy |
| 2024-acf-regionals-ohio-state | 7 | 28 | 8.82554 | 1 | 21.8522 | DD-Bernstein | synergy |
| 2024-acf-regionals-rutgers | 11 | 56 | 12.3627 | 0.963636 | 31.8427 | DD-Bernstein | synergy |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 13.6055 | 0.881818 | 31.5237 | DD-Bernstein | synergy |
| 2024-acf-winter-at-brandeis | 21 | 85 | 7.31913 | 0.986355 | 24.8419 | DD-Bernstein | synergy |
| 2024-acf-winter-at-central-florida | 11 | 49 | 5.74536 | 0.981818 | 18.5567 | DD-Bernstein | synergy |
| 2024-acf-winter-at-clemson | 18 | 85 | 6.98495 | 0.975207 | 24.1168 | DD-Bernstein | synergy |
| 2024-acf-winter-at-lehigh | 15 | 65 | 4.41079 | 0.989286 | 22.4061 | DD-Bernstein | synergy |
| 2024-acf-winter-at-northwestern | 21 | 98 | 5.29307 | 0.990581 | 25.0324 | DD-Bernstein | synergy |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 8.50068 | 0.975439 | 27.7713 | DD-Bernstein | synergy |
| 2024-acf-winter-at-online | 18 | 96 | 9.82446 | 0.962313 | 31.4328 | DD-Bernstein | synergy |
| 2024-acf-winter-at-oxford | 22 | 96 | 8.77885 | 0.881423 | 31.6864 | DD-Bernstein | synergy |
| 2024-acf-winter-at-ubc | 6 | 30 | 3.52497 | 0.942857 | 28.0863 | DD-Bernstein | synergy |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 22.4987 | 0.657143 | 53.7164 | DD-Bernstein | synergy |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 19.5268 | 0.963636 | 33.1113 | Multidim | compositional |
| 2024-acf-fall-at-cornell | 18 | 89 | 12.0121 | 0.946825 | 28.0762 | Multidim | compositional |
| 2024-acf-fall-at-georgia | 24 | 124 | 16.3015 | 0.975652 | 31.0746 | Multidim | compositional |
| 2024-acf-fall-at-illinois | 20 | 99 | 21.5634 | 0.978947 | 35.3629 | Multidim | compositional |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 16.1299 | 0.977444 | 31.5594 | Multidim | compositional |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 19.7897 | 0.981424 | 31.7508 | Multidim | compositional |
| 2024-acf-fall-at-rutgers | 17 | 92 | 19.6374 | 0.960784 | 36.4689 | Multidim | compositional |
| 2024-acf-fall-at-washington | 14 | 64 | 14.8066 | 0.947253 | 28.1899 | Multidim | compositional |
| 2024-acf-nationals | 48 | 400 | 17.1683 | 0.898985 | 29.8078 | Multidim | compositional |
| 2024-acf-regionals-berkeley | 6 | 30 | 29.4078 | 1 | 45.1546 | Multidim | compositional |
| 2024-acf-regionals-cornell | 6 | 31 | 16.4873 | 0.828571 | 29.0599 | Multidim | compositional |
| 2024-acf-regionals-imperial | 16 | 89 | 18.8077 | 0.967647 | 30.8269 | Multidim | compositional |
| 2024-acf-regionals-jmu | 20 | 120 | 19.8616 | 0.977444 | 27.9319 | Multidim | compositional |
| 2024-acf-regionals-minnesota | 4 | 20 | 16.0067 | 1 | 30.0977 | Multidim | compositional |
| 2024-acf-regionals-mit | 12 | 14 | 22.542 | 0.991245 | 42.1308 | Multidim | compositional |
| 2024-acf-regionals-nebraska | 12 | 67 | 15.058 | 0.951049 | 29.2681 | Multidim | compositional |
| 2024-acf-regionals-ohio-state | 7 | 28 | 18.2102 | 1 | 29.4151 | Multidim | compositional |
| 2024-acf-regionals-rutgers | 11 | 56 | 29.5662 | 0.990909 | 41.3755 | Multidim | compositional |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 15.7076 | 0.927273 | 29.7085 | Multidim | compositional |
| 2024-acf-winter-at-brandeis | 21 | 85 | 17.53 | 0.981807 | 34.5326 | Multidim | compositional |
| 2024-acf-winter-at-central-florida | 11 | 49 | 19.5534 | 0.981818 | 30.3387 | Multidim | compositional |
| 2024-acf-winter-at-clemson | 18 | 85 | 15.6429 | 0.954546 | 31.1157 | Multidim | compositional |
| 2024-acf-winter-at-lehigh | 15 | 65 | 21.955 | 0.989286 | 41.9226 | Multidim | compositional |
| 2024-acf-winter-at-northwestern | 21 | 98 | 18.7533 | 0.97824 | 35.0457 | Multidim | compositional |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 18.1976 | 0.963158 | 30.1154 | Multidim | compositional |
| 2024-acf-winter-at-online | 18 | 96 | 15.0766 | 0.947858 | 32.0516 | Multidim | compositional |
| 2024-acf-winter-at-oxford | 22 | 96 | 15.6562 | 0.958216 | 34.4422 | Multidim | compositional |
| 2024-acf-winter-at-ubc | 6 | 30 | 13.5541 | 0.942857 | 28.2139 | Multidim | compositional |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 29.6247 | 0.828571 | 41.6659 | Multidim | compositional |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 9.82636 | 1 | 31.4746 | Multidim | synergy |
| 2024-acf-fall-at-cornell | 18 | 89 | 8.30536 | 0.990191 | 27.7936 | Multidim | synergy |
| 2024-acf-fall-at-georgia | 24 | 124 | 9.26961 | 0.992174 | 26.909 | Multidim | synergy |
| 2024-acf-fall-at-illinois | 20 | 99 | 10.1237 | 0.990977 | 26.6529 | Multidim | synergy |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 7.72732 | 0.972932 | 25.2502 | Multidim | synergy |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 8.92926 | 0.991744 | 24.153 | Multidim | synergy |
| 2024-acf-fall-at-rutgers | 17 | 92 | 9.56473 | 0.980392 | 27.4779 | Multidim | synergy |
| 2024-acf-fall-at-washington | 14 | 64 | 7.79881 | 0.978022 | 26.6039 | Multidim | synergy |
| 2024-acf-nationals | 48 | 400 | 14.072 | 0.959127 | 24.2666 | Multidim | synergy |
| 2024-acf-regionals-berkeley | 6 | 30 | 10.8318 | 1 | 26.2609 | Multidim | synergy |
| 2024-acf-regionals-cornell | 6 | 31 | 12.2327 | 1 | 34.1099 | Multidim | synergy |
| 2024-acf-regionals-imperial | 16 | 89 | 11.55 | 0.955882 | 25.28 | Multidim | synergy |
| 2024-acf-regionals-jmu | 20 | 120 | 9.14327 | 0.989474 | 25.3576 | Multidim | synergy |
| 2024-acf-regionals-minnesota | 4 | 20 | 26.1214 | 0.8 | 43.521 | Multidim | synergy |
| 2024-acf-regionals-mit | 12 | 14 | 19.7114 | 0.970229 | 34.9435 | Multidim | synergy |
| 2024-acf-regionals-nebraska | 12 | 67 | 12.4871 | 0.979021 | 31.9945 | Multidim | synergy |
| 2024-acf-regionals-ohio-state | 7 | 28 | 8.91454 | 1 | 26.1934 | Multidim | synergy |
| 2024-acf-regionals-rutgers | 11 | 56 | 16.5095 | 0.963636 | 31.0334 | Multidim | synergy |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 13.8108 | 0.990909 | 26.2322 | Multidim | synergy |
| 2024-acf-winter-at-brandeis | 21 | 85 | 8.41373 | 0.977908 | 26.0052 | Multidim | synergy |
| 2024-acf-winter-at-central-florida | 11 | 49 | 6.38426 | 1 | 20.3026 | Multidim | synergy |
| 2024-acf-winter-at-clemson | 18 | 85 | 8.21012 | 0.974174 | 25.8961 | Multidim | synergy |
| 2024-acf-winter-at-lehigh | 15 | 65 | 13.9462 | 0.935714 | 31.3088 | Multidim | synergy |
| 2024-acf-winter-at-northwestern | 21 | 98 | 7.67887 | 0.989282 | 26.3603 | Multidim | synergy |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 10.191 | 0.959649 | 25.2888 | Multidim | synergy |
| 2024-acf-winter-at-online | 18 | 96 | 7.78235 | 0.971606 | 28.3314 | Multidim | synergy |
| 2024-acf-winter-at-oxford | 22 | 96 | 8.20165 | 0.976285 | 27.8687 | Multidim | synergy |
| 2024-acf-winter-at-ubc | 6 | 30 | 5.72565 | 1 | 26.9985 | Multidim | synergy |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 14.8081 | 0.828571 | 27.3177 | Multidim | synergy |
