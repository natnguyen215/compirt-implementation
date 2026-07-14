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
| tournament_rank_correlation | -0.100 |
| actual_top_20_in_tournament_model_rank_top_20 | 1/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 9/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 153 | 153 | 0.710 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 105 | 105 | 0.727 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 143 | 143 | 0.713 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 127 | 127 | 0.720 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 109 | 109 | 0.726 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 178 | 178 | 0.692 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 91 | 91 | 0.730 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 181 | 181 | 0.688 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 152 | 152 | 0.711 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 98 | 98 | 0.729 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 139 | 139 | 0.715 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 154 | 154 | 0.709 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 161 | 161 | 0.706 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 20 | 20 | 0.755 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 28 | 28 | 0.752 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 82 | 82 | 0.732 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 27 | 27 | 0.752 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 128 | 128 | 0.719 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 130 | 130 | 0.719 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 89 | 89 | 0.731 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 129 | 129 | 0.719 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 99 | 99 | 0.729 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 75 | 75 | 0.734 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 149 | 149 | 0.711 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 166 | 166 | 0.704 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 172 | Sean Jackson | South Carolina | 5 | 5.588 | 95 | 1 | 1 | 0.784 | 4 |
| 71 | Rosa Xia | Cornell B | 21 | 21.176 | 360 | 2 | 2 | 0.774 | 33 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 3 | 3 | 0.773 | 38 |
| 136 | Mason Yu | Brown | 11 | 11.471 | 195 | 4 | 4 | 0.772 | 19 |
| 169 | Lydia Tarekegn | Yale B | 6 | 6.176 | 105 | 5 | 5 | 0.771 | 12 |
| 92 | Alex Akridge | Indiana | 17 | 17.647 | 300 | 6 | 6 | 0.766 | 41 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 7 | 7 | 0.765 | 55 |
| 180 | Kenny Zhang | Virginia | 2 | 2.647 | 45 | 8 | 8 | 0.765 | 8 |
| 112 | Arunn Sankar | Georgia Tech | 15 | 15.294 | 260 | 9 | 9 | 0.764 | 25 |
| 130 | Jason Zhang | Toronto B | 12 | 12.647 | 215 | 10 | 10 | 0.762 | 28 |
| 143 | Derek Chen | Columbia B | 10 | 10.294 | 175 | 11 | 11 | 0.761 | 26 |
| 139 | Nermeen Rahman | Chicago C | 11 | 11.875 | 190 | 12 | 12 | 0.761 | 26 |
| 57 | Rohan Shelke | Berkeley B | 23 | 23.235 | 395 | 13 | 13 | 0.761 | 49 |
| 98 | Guy Indorante | Iowa State | 16 | 16.765 | 285 | 14 | 14 | 0.759 | 39 |
| 59 | Neal Joshi | WUSTL B | 22 | 22.941 | 390 | 15 | 15 | 0.757 | 39 |
| 52 | Dean Ah Now | Claremont Colleges | 24 | 24.706 | 420 | 17 | 17 | 0.756 | 40 |
| 183 | Denis Liu | Arizona State | 2 | 2.059 | 35 | 18 | 18 | 0.756 | 18 |
| 117 | Liam Kusalik | Waterloo | 15 | 15.000 | 255 | 19 | 19 | 0.755 | 23 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 20 | 20 | 0.755 | 90 |
| 114 | Morgan Bozeman | Minnesota B | 15 | 15.294 | 260 | 21 | 21 | 0.755 | 40 |
| 123 | Michael Hunding | Illinois | 14 | 14.375 | 230 | 22 | 22 | 0.754 | 24 |
| 82 | Will Orr | Yale B | 19 | 19.706 | 335 | 23 | 23 | 0.754 | 51 |
| 100 | Andrew Ellis | Kentucky | 16 | 16.471 | 280 | 24 | 24 | 0.754 | 40 |
| 34 | Bryan Ugaz | Arizona State | 27 | 27.647 | 470 | 25 | 25 | 0.754 | 67 |
| 50 | Jeremy Cummings | WUSTL B | 25 | 25.294 | 430 | 26 | 26 | 0.752 | 50 |
