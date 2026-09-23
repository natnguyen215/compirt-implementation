# Bonus difficulty, team tournament PPG and game margins

Saved predictions from the same five whole-game folds as the original comparison; no parameters were refit. These historical Stage-1 fits predate the normalized first-buzz likelihood. Difficulty is the source's declared part label, not part position or fitted difficulty. Each roster group has one easy, medium and hard part per bonus; no labels are unknown.

The always-predict-correct baseline over all rosters is 90.94% easy, 49.34% medium, 16.21% hard. This equals the observed correct-answer rate. Baselines are shared by both models and synergy settings; n counts parts per configuration.

## Familiar roster

| Model | Synergy | Bonuses | Part acc. ↑ | Easy acc. ↑ (n = 40,549) | Medium acc. ↑ (n = 40,549) | Hard acc. ↑ (n = 40,549) | Exact bonus acc. ↑ | AUC ↑ | Log loss ↓ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD-Bernstein | off | 40549 | 80.79% | 90.67% | 67.98% | 83.72% | 50.98% | 0.890393 | 0.418379 |
| DD-Bernstein | on | 40549 | 81.75% | 90.80% | 70.18% | 84.27% | 53.06% | 0.898896 | 0.403178 |
| Multidim | off | 40549 | 80.80% | 90.80% | 67.79% | 83.80% | 51.14% | 0.888037 | 0.422893 |
| Multidim | on | 40549 | 81.48% | 90.06% | 70.07% | 84.32% | 52.61% | 0.896831 | 0.409438 |

Always-predict-correct baseline: 91.02% easy, 49.57% medium, 16.29% hard.

## New roster, known players

| Model | Synergy | Bonuses | Part acc. ↑ | Easy acc. ↑ (n = 2,151) | Medium acc. ↑ (n = 2,151) | Hard acc. ↑ (n = 2,151) | Exact bonus acc. ↑ | AUC ↑ | Log loss ↓ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD-Bernstein | off | 2151 | 80.88% | 89.87% | 66.90% | 85.87% | 52.30% | 0.888405 | 0.422167 |
| DD-Bernstein | on | 2151 | 81.11% | 89.68% | 68.11% | 85.54% | 53.14% | 0.887072 | 0.428144 |
| Multidim | off | 2151 | 81.39% | 90.10% | 67.92% | 86.15% | 52.77% | 0.889247 | 0.419169 |
| Multidim | on | 2151 | 79.70% | 89.45% | 65.50% | 84.15% | 49.28% | 0.875336 | 0.445376 |

Always-predict-correct baseline: 89.40% easy, 44.91% medium, 14.60% hard.

## Bonus-only team PPG and margins

Sum each team's observed or expected points on its recorded bonuses. Expected response points are 10 times the sum of the three part probabilities. Divide by unique games played, including zero-bonus games. All held-out folds are pooled before computing team PPG. Each team's absolute PPG error is in the leaderboard CSV; tournament MAE averages these errors. Spearman ranks teams within each mirror tournament with average ranks for ties. Constant rankings have undefined correlation and are excluded from its macro mean. Games with incomplete bonus predictions are excluded entirely. Bonus margin is team A's points minus team B's in a game, with teams ordered by ID. Its MAE averages absolute errors in these signed margins, one vote per game. Both metrics are conditional on the actual bonus opportunities; bonus ownership is not replayed.

| model | arm | tournament_team_bonus_ppg_mae | tournament_team_bonus_ppg_spearman | bonus_ppg_tournaments | bonus_ppg_spearman_tournaments | bonus_ppg_incomplete_games | bonus_ppg_games | bonus_game_margin_mae | bonus_game_margin_mae_games |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DD-Bernstein | compositional | 18.0827 | 0.883903 | 29 | 29 | 99 | 2332 | 33.2347 | 2332 |
| DD-Bernstein | synergy | 8.09265 | 0.940012 | 29 | 29 | 99 | 2332 | 26.5165 | 2332 |
| Multidim | compositional | 18.7633 | 0.958326 | 29 | 29 | 99 | 2332 | 32.1506 | 2332 |
| Multidim | synergy | 10.9749 | 0.969583 | 29 | 29 | 99 | 2332 | 26.6835 | 2332 |

[All tournament metrics](bonus_ppg_by_tournament.csv). The PPG summary averages tournaments equally after computing their metrics; the overall margin MAE weights games equally.

- DD-Bernstein compositional: [team PPG and errors](bonus_metrics/DD-Bernstein/compositional/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD-Bernstein/compositional/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD-Bernstein/compositional/bonus_game_margin_predictions.csv).
- DD-Bernstein synergy: [team PPG and errors](bonus_metrics/DD-Bernstein/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/DD-Bernstein/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/DD-Bernstein/synergy/bonus_game_margin_predictions.csv).
- Multidim compositional: [team PPG and errors](bonus_metrics/Multidim/compositional/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/Multidim/compositional/bonus_team_game_predictions.csv), [game margins](bonus_metrics/Multidim/compositional/bonus_game_margin_predictions.csv).
- Multidim synergy: [team PPG and errors](bonus_metrics/Multidim/synergy/bonus_team_ppg_leaderboard.csv), [team-game totals](bonus_metrics/Multidim/synergy/bonus_team_game_predictions.csv), [game margins](bonus_metrics/Multidim/synergy/bonus_game_margin_predictions.csv).

## Per-tournament results

| tournament_id | teams | games | bonus_ppg_mae | bonus_ppg_spearman | bonus_game_margin_mae | model | arm |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 5.21198 | 0.987879 | 27.4997 | DD-Bernstein | compositional |
| 2024-acf-fall-at-cornell | 18 | 89 | 16.9461 | 0.786784 | 31.4929 | DD-Bernstein | compositional |
| 2024-acf-fall-at-georgia | 24 | 124 | 14.466 | 0.946087 | 32.9623 | DD-Bernstein | compositional |
| 2024-acf-fall-at-illinois | 20 | 99 | 13.42 | 0.969925 | 30.7029 | DD-Bernstein | compositional |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 14.4163 | 0.893233 | 29.0473 | DD-Bernstein | compositional |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 18.3541 | 0.925697 | 33.3864 | DD-Bernstein | compositional |
| 2024-acf-fall-at-rutgers | 17 | 92 | 14.5778 | 0.887255 | 34.3621 | DD-Bernstein | compositional |
| 2024-acf-fall-at-washington | 14 | 64 | 16.7904 | 0.898901 | 35.0413 | DD-Bernstein | compositional |
| 2024-acf-nationals | 48 | 400 | 16.74 | 0.856701 | 32.4608 | DD-Bernstein | compositional |
| 2024-acf-regionals-berkeley | 6 | 30 | 26.9035 | 0.828571 | 45.3489 | DD-Bernstein | compositional |
| 2024-acf-regionals-cornell | 6 | 31 | 24.3561 | 0.6 | 38.1109 | DD-Bernstein | compositional |
| 2024-acf-regionals-imperial | 16 | 89 | 18.7575 | 0.929412 | 36.0045 | DD-Bernstein | compositional |
| 2024-acf-regionals-jmu | 20 | 120 | 20.7463 | 0.948872 | 30.2796 | DD-Bernstein | compositional |
| 2024-acf-regionals-minnesota | 4 | 20 | 23.644 | 0.8 | 44.8328 | DD-Bernstein | compositional |
| 2024-acf-regionals-mit | 12 | 14 | 21.8108 | 0.942208 | 35.528 | DD-Bernstein | compositional |
| 2024-acf-regionals-nebraska | 12 | 67 | 17.3106 | 0.881119 | 35.2318 | DD-Bernstein | compositional |
| 2024-acf-regionals-ohio-state | 7 | 28 | 12.177 | 1 | 25.5375 | DD-Bernstein | compositional |
| 2024-acf-regionals-rutgers | 11 | 56 | 22.0961 | 0.954545 | 37.1992 | DD-Bernstein | compositional |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 18.0035 | 0.881818 | 36.9791 | DD-Bernstein | compositional |
| 2024-acf-winter-at-brandeis | 21 | 85 | 18.7052 | 0.959065 | 31.5588 | DD-Bernstein | compositional |
| 2024-acf-winter-at-central-florida | 11 | 49 | 15.0678 | 0.963636 | 25.6083 | DD-Bernstein | compositional |
| 2024-acf-winter-at-clemson | 18 | 85 | 15.7499 | 0.907025 | 32.9564 | DD-Bernstein | compositional |
| 2024-acf-winter-at-lehigh | 15 | 65 | 17.0428 | 0.946429 | 36.3664 | DD-Bernstein | compositional |
| 2024-acf-winter-at-northwestern | 21 | 98 | 15.765 | 0.936668 | 32.7605 | DD-Bernstein | compositional |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 21.3979 | 0.938596 | 30.6032 | DD-Bernstein | compositional |
| 2024-acf-winter-at-online | 18 | 96 | 14.3202 | 0.894166 | 32.9556 | DD-Bernstein | compositional |
| 2024-acf-winter-at-oxford | 22 | 96 | 15.0508 | 0.85432 | 34.0087 | DD-Bernstein | compositional |
| 2024-acf-winter-at-ubc | 6 | 30 | 19.3483 | 0.771429 | 36.4096 | DD-Bernstein | compositional |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 35.2218 | 0.542857 | 59.3212 | DD-Bernstein | compositional |
| 2024-acf-fall-at-claremont-colleges | 10 | 44 | 2.89894 | 1 | 30.7348 | DD-Bernstein | synergy |
| 2024-acf-fall-at-cornell | 18 | 89 | 3.31526 | 0.980898 | 24.4563 | DD-Bernstein | synergy |
| 2024-acf-fall-at-georgia | 24 | 124 | 3.96887 | 0.993913 | 27.8845 | DD-Bernstein | synergy |
| 2024-acf-fall-at-illinois | 20 | 99 | 5.89983 | 0.98797 | 26.24 | DD-Bernstein | synergy |
| 2024-acf-fall-at-north-carolina | 20 | 110 | 8.3755 | 0.938346 | 29.6871 | DD-Bernstein | synergy |
| 2024-acf-fall-at-ohio-state | 18 | 97 | 5.20117 | 0.995872 | 24.4112 | DD-Bernstein | synergy |
| 2024-acf-fall-at-rutgers | 17 | 92 | 10.4418 | 0.897059 | 33.9026 | DD-Bernstein | synergy |
| 2024-acf-fall-at-washington | 14 | 64 | 4.08579 | 0.978022 | 27.7111 | DD-Bernstein | synergy |
| 2024-acf-nationals | 48 | 400 | 5.23119 | 0.98453 | 22.0212 | DD-Bernstein | synergy |
| 2024-acf-regionals-berkeley | 6 | 30 | 4.59571 | 1 | 28.0973 | DD-Bernstein | synergy |
| 2024-acf-regionals-cornell | 6 | 31 | 14.8425 | 0.6 | 33.6821 | DD-Bernstein | synergy |
| 2024-acf-regionals-imperial | 16 | 89 | 9.28771 | 0.958824 | 26.9866 | DD-Bernstein | synergy |
| 2024-acf-regionals-jmu | 20 | 120 | 7.58993 | 0.981955 | 20.5882 | DD-Bernstein | synergy |
| 2024-acf-regionals-minnesota | 4 | 20 | 6.87644 | 0.8 | 26.0498 | DD-Bernstein | synergy |
| 2024-acf-regionals-mit | 12 | 14 | 13.2896 | 0.991245 | 20.5416 | DD-Bernstein | synergy |
| 2024-acf-regionals-nebraska | 12 | 67 | 12.8805 | 0.888112 | 31.3751 | DD-Bernstein | synergy |
| 2024-acf-regionals-ohio-state | 7 | 28 | 8.19582 | 1 | 22.4127 | DD-Bernstein | synergy |
| 2024-acf-regionals-rutgers | 11 | 56 | 13.0486 | 0.963636 | 32.2329 | DD-Bernstein | synergy |
| 2024-acf-regionals-vanderbilt | 11 | 45 | 13.8418 | 0.918182 | 31.1521 | DD-Bernstein | synergy |
| 2024-acf-winter-at-brandeis | 21 | 85 | 6.81261 | 0.986355 | 24.724 | DD-Bernstein | synergy |
| 2024-acf-winter-at-central-florida | 11 | 49 | 6.39219 | 0.981818 | 18.7667 | DD-Bernstein | synergy |
| 2024-acf-winter-at-clemson | 18 | 85 | 5.50603 | 0.971075 | 23.802 | DD-Bernstein | synergy |
| 2024-acf-winter-at-lehigh | 15 | 65 | 5.52023 | 0.989286 | 22.8861 | DD-Bernstein | synergy |
| 2024-acf-winter-at-northwestern | 21 | 98 | 5.04049 | 0.989282 | 24.8733 | DD-Bernstein | synergy |
| 2024-acf-winter-at-ohio-state | 19 | 82 | 7.81301 | 0.978947 | 27.158 | DD-Bernstein | synergy |
| 2024-acf-winter-at-online | 18 | 96 | 9.63056 | 0.966443 | 30.8976 | DD-Bernstein | synergy |
| 2024-acf-winter-at-oxford | 22 | 96 | 8.35513 | 0.881423 | 31.5356 | DD-Bernstein | synergy |
| 2024-acf-winter-at-ubc | 6 | 30 | 4.09471 | 1 | 27.4397 | DD-Bernstein | synergy |
| 2024-acf-winter-at-uc-berkeley | 6 | 27 | 21.655 | 0.657143 | 51.8491 | DD-Bernstein | synergy |
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
