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
| tournament_rank_correlation | 0.794 |
| actual_top_20_in_tournament_model_rank_top_20 | 10/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 32/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.793 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 11 | 11 | 0.675 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 62 | 62 | 0.588 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 10 | 10 | 0.691 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 5 | 5 | 0.716 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 19 | 19 | 0.662 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 2 | 2 | 0.729 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 39 | 39 | 0.623 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 33 | 33 | 0.632 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 27 | 27 | 0.639 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 22 | 22 | 0.646 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 80 | 80 | 0.561 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 15 | 15 | 0.670 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 8 | 8 | 0.694 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 20 | 20 | 0.661 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 21 | 21 | 0.658 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 7 | 7 | 0.700 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 103 | 103 | 0.542 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 29 | 29 | 0.636 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 26 | 26 | 0.640 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 65 | 65 | 0.587 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 35 | 35 | 0.630 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 68 | 68 | 0.583 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 93 | 93 | 0.551 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 50 | 50 | 0.605 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.793 | 157 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 2 | 2 | 0.729 | 78 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 3 | 3 | 0.726 | 55 |
| 71 | Rosa Xia | Cornell B | 21 | 21.176 | 360 | 4 | 4 | 0.722 | 33 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 5 | 5 | 0.716 | 92 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 6 | 6 | 0.701 | 38 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 7 | 7 | 0.700 | 72 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 8 | 8 | 0.694 | 90 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 9 | 9 | 0.693 | 49 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 10 | 10 | 0.691 | 93 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 11 | 11 | 0.675 | 125 |
| 92 | Alex Akridge | Indiana | 17 | 17.647 | 300 | 12 | 12 | 0.673 | 41 |
| 57 | Rohan Shelke | Berkeley B | 23 | 23.235 | 395 | 13 | 13 | 0.672 | 49 |
| 50 | Jeremy Cummings | WUSTL B | 25 | 25.294 | 430 | 14 | 14 | 0.670 | 50 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 15 | 15 | 0.670 | 81 |
| 58 | Adam Fine | Chicago A | 22 | 22.941 | 390 | 16 | 16 | 0.670 | 38 |
| 31 | Andrew Zeng | Stanford | 28 | 28.235 | 480 | 17 | 17 | 0.668 | 48 |
| 32 | John John Groger | Columbia B | 27 | 27.941 | 475 | 18 | 18 | 0.664 | 36 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 19 | 19 | 0.662 | 99 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 20 | 20 | 0.661 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 21 | 21 | 0.658 | 80 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 22 | 22 | 0.646 | 89 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 23 | 23 | 0.646 | 52 |
| 49 | Tegan Kapadia | Georgia Tech | 25 | 25.588 | 435 | 24 | 24 | 0.643 | 51 |
| 112 | Arunn Sankar | Georgia Tech | 15 | 15.294 | 260 | 25 | 25 | 0.643 | 25 |
