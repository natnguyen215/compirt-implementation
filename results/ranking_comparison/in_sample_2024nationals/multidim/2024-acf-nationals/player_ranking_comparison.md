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
| tournament_rank_correlation | 0.803 |
| actual_top_20_in_tournament_model_rank_top_20 | 9/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 32/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.857 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 23 | 23 | 0.730 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 77 | 77 | 0.625 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 3 | 3 | 0.814 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 20 | 20 | 0.735 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 17 | 17 | 0.746 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 2 | 2 | 0.841 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 37 | 37 | 0.704 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 36 | 36 | 0.706 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 48 | 48 | 0.676 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 16 | 16 | 0.747 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 105 | 105 | 0.582 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 12 | 12 | 0.761 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 14 | 14 | 0.753 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 21 | 21 | 0.732 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 35 | 35 | 0.707 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 9 | 9 | 0.778 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 94 | 94 | 0.598 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 42 | 42 | 0.694 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 22 | 22 | 0.731 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 58 | 58 | 0.655 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 41 | 41 | 0.697 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 65 | 65 | 0.649 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 79 | 79 | 0.624 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 50 | 50 | 0.672 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.857 | 157 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 2 | 2 | 0.841 | 78 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 3 | 3 | 0.814 | 93 |
| 31 | Andrew Zeng | Stanford | 28 | 28.235 | 480 | 4 | 4 | 0.806 | 48 |
| 65 | Nathan Zhang | Cornell A | 21 | 21.765 | 370 | 5 | 5 | 0.801 | 32 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 6 | 6 | 0.789 | 38 |
| 61 | Matt Schiavone | Purdue | 22 | 22.647 | 385 | 7 | 7 | 0.780 | 36 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 8 | 8 | 0.779 | 55 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 9 | 9 | 0.778 | 72 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 10 | 10 | 0.777 | 49 |
| 123 | Michael Hunding | Illinois | 14 | 14.375 | 230 | 11 | 11 | 0.762 | 24 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 12 | 12 | 0.761 | 81 |
| 32 | John John Groger | Columbia B | 27 | 27.941 | 475 | 13 | 13 | 0.760 | 36 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 14 | 14 | 0.753 | 90 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 15 | 15 | 0.751 | 52 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 16 | 16 | 0.747 | 89 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 17 | 17 | 0.746 | 99 |
| 84 | Dennis Reppen | Chicago C | 19 | 19.688 | 315 | 18 | 18 | 0.740 | 32 |
| 89 | Arthur Delot-Vilain | Yale A | 17 | 17.941 | 305 | 19 | 19 | 0.737 | 29 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 20 | 20 | 0.735 | 92 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 21 | 21 | 0.732 | 69 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 22 | 22 | 0.731 | 62 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 23 | 23 | 0.730 | 125 |
| 49 | Tegan Kapadia | Georgia Tech | 25 | 25.588 | 435 | 24 | 24 | 0.730 | 51 |
| 101 | Claire Jones | Chicago A | 16 | 16.471 | 280 | 25 | 25 | 0.729 | 26 |
