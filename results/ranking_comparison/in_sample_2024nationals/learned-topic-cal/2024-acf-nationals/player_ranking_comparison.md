# Player Ranking Comparison: 2024-acf-nationals

The real-world comparator here is tournament individual scoring from the source database. The default `ppg` mode follows the public [2024 ACF Nationals player standings](https://quizbowlstats.com/tournaments/2045), which are ordered by points per game and do not state a minimum-games or minimum-TUH eligibility floor. The fitted model ranks players by mean predicted correctness on observed buzzes, so it rewards accuracy more than scoring volume.

This report uses `actual_ppg` (`actual_points / games`) as its real rank metric.

Only games with at least `20` tossups are included as a source-data integrity filter; this is separate from player eligibility.

Caveat: the source database does not include game-specific lineups, so games played and tossups heard are inferred from registered rosters. That matches the modeling assumption used by this project, but can blur players who did not play every game for their listed team.

## Summary

| metric | value |
| --- | --- |
| actual_players_after_floor | 187 |
| actual_rank_mode | ppg |
| actual_rank_metric | actual_ppg |
| min_games | 1 |
| min_tuh | 1 |
| min_game_tossups | 20 |
| tournament_model_matches | 184 |
| tournament_rank_correlation | 0.068 |
| actual_top_20_in_tournament_model_rank_top_20 | 2/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 14/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 19 | 19 | 0.759 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 89 | 89 | 0.724 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 149 | 149 | 0.701 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 54 | 54 | 0.737 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 23 | 23 | 0.755 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 144 | 144 | 0.705 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 35 | 35 | 0.746 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 159 | 159 | 0.694 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 142 | 142 | 0.706 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 107 | 107 | 0.721 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 96 | 96 | 0.722 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 154 | 154 | 0.699 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 108 | 108 | 0.720 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 17 | 17 | 0.760 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 24 | 24 | 0.755 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 66 | 66 | 0.732 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 32 | 32 | 0.749 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 183 | 183 | 0.676 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 67 | 67 | 0.732 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 114 | 114 | 0.718 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 132 | 132 | 0.712 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 84 | 84 | 0.727 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 97 | 97 | 0.722 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 148 | 148 | 0.702 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 105 | 105 | 0.721 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 169 | Lydia Tarekegn | Yale B | 6 | 6.176 | 105 | 1 | 1 | 0.782 | 12 |
| 92 | Alex Akridge | Indiana | 17 | 17.647 | 300 | 2 | 2 | 0.782 | 41 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 3 | 3 | 0.780 | 55 |
| 112 | Arunn Sankar | Georgia Tech | 15 | 15.294 | 260 | 4 | 4 | 0.779 | 25 |
| 136 | Mason Yu | Brown | 11 | 11.471 | 195 | 5 | 5 | 0.775 | 19 |
| 57 | Rohan Shelke | Berkeley B | 23 | 23.235 | 395 | 7 | 7 | 0.768 | 49 |
| 117 | Liam Kusalik | Waterloo | 15 | 15.000 | 255 | 8 | 8 | 0.767 | 23 |
| 180 | Kenny Zhang | Virginia | 2 | 2.647 | 45 | 9 | 9 | 0.766 | 8 |
| 71 | Rosa Xia | Cornell B | 21 | 21.176 | 360 | 10 | 10 | 0.766 | 33 |
| 130 | Jason Zhang | Toronto B | 12 | 12.647 | 215 | 11 | 11 | 0.764 | 28 |
| 158 | Justin Zhang | Duke | 8 | 8.235 | 140 | 12 | 12 | 0.764 | 20 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 13 | 13 | 0.763 | 49 |
| 143 | Derek Chen | Columbia B | 10 | 10.294 | 175 | 14 | 14 | 0.763 | 26 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 15 | 15 | 0.762 | 38 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 16 | 16 | 0.760 | 52 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 17 | 17 | 0.760 | 90 |
| 58 | Adam Fine | Chicago A | 22 | 22.941 | 390 | 18 | 18 | 0.760 | 38 |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 19 | 19 | 0.759 | 157 |
| 172 | Sean Jackson | South Carolina | 5 | 5.588 | 95 | 20 | 20 | 0.757 | 4 |
| 176 | Drew Wetterlind | Iowa State | 3 | 3.824 | 65 | 21 | 21 | 0.756 | 7 |
| 98 | Guy Indorante | Iowa State | 16 | 16.765 | 285 | 22 | 22 | 0.756 | 39 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 23 | 23 | 0.755 | 92 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 24 | 24 | 0.755 | 69 |
| 49 | Tegan Kapadia | Georgia Tech | 25 | 25.588 | 435 | 25 | 25 | 0.754 | 51 |
| 183 | Denis Liu | Arizona State | 2 | 2.059 | 35 | 26 | 26 | 0.753 | 18 |
