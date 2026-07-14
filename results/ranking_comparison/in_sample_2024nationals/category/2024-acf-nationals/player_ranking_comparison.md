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
| tournament_rank_correlation | 0.603 |
| actual_top_20_in_tournament_model_rank_top_20 | 7/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 26/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 2 | 2 | 0.731 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 22 | 22 | 0.653 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 85 | 85 | 0.564 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 19 | 19 | 0.655 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 21 | 21 | 0.653 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 49 | 49 | 0.605 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 6 | 6 | 0.703 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 86 | 86 | 0.561 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 61 | 61 | 0.593 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 33 | 33 | 0.624 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 39 | 39 | 0.612 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 115 | 115 | 0.526 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 45 | 45 | 0.608 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 7 | 7 | 0.686 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 20 | 20 | 0.654 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 27 | 27 | 0.638 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 4 | 4 | 0.717 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 93 | 93 | 0.553 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 60 | 60 | 0.593 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 16 | 16 | 0.657 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 76 | 76 | 0.572 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 44 | 44 | 0.609 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 81 | 81 | 0.569 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 112 | 112 | 0.530 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 98 | 98 | 0.548 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 71 | Rosa Xia | Cornell B | 21 | 21.176 | 360 | 1 | 1 | 0.741 | 33 |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 2 | 2 | 0.731 | 157 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 3 | 3 | 0.722 | 38 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 4 | 4 | 0.717 | 72 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 5 | 5 | 0.707 | 55 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 6 | 6 | 0.703 | 78 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 7 | 7 | 0.686 | 90 |
| 112 | Arunn Sankar | Georgia Tech | 15 | 15.294 | 260 | 8 | 8 | 0.681 | 25 |
| 92 | Alex Akridge | Indiana | 17 | 17.647 | 300 | 9 | 9 | 0.680 | 41 |
| 50 | Jeremy Cummings | WUSTL B | 25 | 25.294 | 430 | 10 | 10 | 0.680 | 50 |
| 136 | Mason Yu | Brown | 11 | 11.471 | 195 | 11 | 11 | 0.671 | 19 |
| 172 | Sean Jackson | South Carolina | 5 | 5.588 | 95 | 12 | 12 | 0.670 | 4 |
| 52 | Dean Ah Now | Claremont Colleges | 24 | 24.706 | 420 | 13 | 13 | 0.663 | 40 |
| 58 | Adam Fine | Chicago A | 22 | 22.941 | 390 | 14 | 14 | 0.658 | 38 |
| 123 | Michael Hunding | Illinois | 14 | 14.375 | 230 | 15 | 15 | 0.657 | 24 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 16 | 16 | 0.657 | 62 |
| 57 | Rohan Shelke | Berkeley B | 23 | 23.235 | 395 | 17 | 17 | 0.655 | 49 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 18 | 18 | 0.655 | 49 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 19 | 19 | 0.655 | 93 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 20 | 20 | 0.654 | 69 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 21 | 21 | 0.653 | 92 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 22 | 22 | 0.653 | 125 |
| 82 | Will Orr | Yale B | 19 | 19.706 | 335 | 23 | 23 | 0.650 | 51 |
| 117 | Liam Kusalik | Waterloo | 15 | 15.000 | 255 | 24 | 24 | 0.646 | 23 |
| 32 | John John Groger | Columbia B | 27 | 27.941 | 475 | 25 | 25 | 0.645 | 36 |
