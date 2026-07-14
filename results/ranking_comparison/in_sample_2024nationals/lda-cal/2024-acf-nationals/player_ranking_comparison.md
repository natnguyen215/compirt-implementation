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
| tournament_rank_correlation | 0.096 |
| actual_top_20_in_tournament_model_rank_top_20 | 2/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 12/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 13 | 13 | 0.774 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 103 | 103 | 0.729 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 171 | 171 | 0.698 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 60 | 60 | 0.743 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 17 | 17 | 0.768 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 138 | 138 | 0.717 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 51 | 51 | 0.750 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 149 | 149 | 0.712 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 124 | 124 | 0.723 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 108 | 108 | 0.728 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 89 | 89 | 0.733 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 165 | 165 | 0.701 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 69 | 69 | 0.740 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 27 | 27 | 0.761 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 32 | 32 | 0.760 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 97 | 97 | 0.731 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 30 | 30 | 0.760 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 182 | 182 | 0.681 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 61 | 61 | 0.743 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 111 | 111 | 0.727 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 130 | 130 | 0.721 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 107 | 107 | 0.728 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 92 | 92 | 0.732 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 166 | 166 | 0.701 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 95 | 95 | 0.731 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 71 | Rosa Xia | Cornell B | 21 | 21.176 | 360 | 1 | 1 | 0.798 | 33 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 2 | 2 | 0.798 | 55 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 3 | 3 | 0.794 | 38 |
| 92 | Alex Akridge | Indiana | 17 | 17.647 | 300 | 4 | 4 | 0.793 | 41 |
| 117 | Liam Kusalik | Waterloo | 15 | 15.000 | 255 | 5 | 5 | 0.788 | 23 |
| 169 | Lydia Tarekegn | Yale B | 6 | 6.176 | 105 | 6 | 6 | 0.785 | 12 |
| 136 | Mason Yu | Brown | 11 | 11.471 | 195 | 7 | 7 | 0.784 | 19 |
| 112 | Arunn Sankar | Georgia Tech | 15 | 15.294 | 260 | 8 | 8 | 0.781 | 25 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 9 | 9 | 0.780 | 49 |
| 180 | Kenny Zhang | Virginia | 2 | 2.647 | 45 | 10 | 10 | 0.779 | 8 |
| 57 | Rohan Shelke | Berkeley B | 23 | 23.235 | 395 | 11 | 11 | 0.777 | 49 |
| 58 | Adam Fine | Chicago A | 22 | 22.941 | 390 | 12 | 12 | 0.775 | 38 |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 13 | 13 | 0.774 | 157 |
| 130 | Jason Zhang | Toronto B | 12 | 12.647 | 215 | 14 | 14 | 0.774 | 28 |
| 143 | Derek Chen | Columbia B | 10 | 10.294 | 175 | 16 | 16 | 0.771 | 26 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 17 | 17 | 0.768 | 92 |
| 158 | Justin Zhang | Duke | 8 | 8.235 | 140 | 18 | 18 | 0.767 | 20 |
| 172 | Sean Jackson | South Carolina | 5 | 5.588 | 95 | 19 | 19 | 0.767 | 4 |
| 50 | Jeremy Cummings | WUSTL B | 25 | 25.294 | 430 | 20 | 20 | 0.767 | 50 |
| 95 | Donal Ryan | Truman State | 17 | 17.059 | 290 | 21 | 21 | 0.766 | 26 |
| 176 | Drew Wetterlind | Iowa State | 3 | 3.824 | 65 | 22 | 22 | 0.765 | 7 |
| 64 | Jonathan Lau | Johns Hopkins | 22 | 22.059 | 375 | 23 | 23 | 0.765 | 30 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 24 | 24 | 0.762 | 52 |
| 123 | Michael Hunding | Illinois | 14 | 14.375 | 230 | 25 | 25 | 0.762 | 24 |
| 99 | Yared Tadesse | Cornell B | 16 | 16.765 | 285 | 26 | 26 | 0.761 | 34 |
