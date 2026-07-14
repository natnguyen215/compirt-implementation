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
| tournament_rank_correlation | 0.220 |
| actual_top_20_in_tournament_model_rank_top_20 | 5/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 19/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 10 | 10 | 0.771 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 45 | 45 | 0.743 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 142 | 142 | 0.710 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 37 | 37 | 0.748 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 21 | 21 | 0.758 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 104 | 104 | 0.723 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 19 | 19 | 0.760 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 167 | 167 | 0.693 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 121 | 121 | 0.718 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 78 | 78 | 0.731 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 109 | 109 | 0.723 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 157 | 157 | 0.700 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 64 | 64 | 0.737 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 14 | 14 | 0.768 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 13 | 13 | 0.768 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 42 | 42 | 0.744 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 20 | 20 | 0.760 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 169 | 169 | 0.693 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 44 | 44 | 0.744 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 125 | 125 | 0.716 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 103 | 103 | 0.723 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 76 | 76 | 0.732 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 65 | 65 | 0.737 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 114 | 114 | 0.721 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 117 | 117 | 0.720 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 1 | 1 | 0.792 | 55 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 3 | 3 | 0.777 | 38 |
| 136 | Mason Yu | Brown | 11 | 11.471 | 195 | 4 | 4 | 0.775 | 19 |
| 92 | Alex Akridge | Indiana | 17 | 17.647 | 300 | 5 | 5 | 0.773 | 41 |
| 71 | Rosa Xia | Cornell B | 21 | 21.176 | 360 | 6 | 6 | 0.773 | 33 |
| 49 | Tegan Kapadia | Georgia Tech | 25 | 25.588 | 435 | 7 | 7 | 0.772 | 51 |
| 117 | Liam Kusalik | Waterloo | 15 | 15.000 | 255 | 8 | 8 | 0.771 | 23 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 9 | 9 | 0.771 | 49 |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 10 | 10 | 0.771 | 157 |
| 57 | Rohan Shelke | Berkeley B | 23 | 23.235 | 395 | 11 | 11 | 0.769 | 49 |
| 169 | Lydia Tarekegn | Yale B | 6 | 6.176 | 105 | 12 | 12 | 0.769 | 12 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 13 | 13 | 0.768 | 69 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 14 | 14 | 0.768 | 90 |
| 143 | Derek Chen | Columbia B | 10 | 10.294 | 175 | 15 | 15 | 0.767 | 26 |
| 112 | Arunn Sankar | Georgia Tech | 15 | 15.294 | 260 | 16 | 16 | 0.763 | 25 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 17 | 17 | 0.762 | 52 |
| 58 | Adam Fine | Chicago A | 22 | 22.941 | 390 | 18 | 18 | 0.761 | 38 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 19 | 19 | 0.760 | 78 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 20 | 20 | 0.760 | 72 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 21 | 21 | 0.758 | 92 |
| 50 | Jeremy Cummings | WUSTL B | 25 | 25.294 | 430 | 22 | 22 | 0.758 | 50 |
| 51 | Nicolas Edwards | McGill | 25 | 25.000 | 425 | 23 | 23 | 0.757 | 45 |
| 31 | Andrew Zeng | Stanford | 28 | 28.235 | 480 | 24 | 24 | 0.757 | 48 |
| 99 | Yared Tadesse | Cornell B | 16 | 16.765 | 285 | 25 | 25 | 0.757 | 34 |
| 163 | William Groger | Columbia B | 7 | 7.647 | 130 | 26 | 26 | 0.756 | 17 |
