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
| tournament_rank_correlation | 0.854 |
| actual_top_20_in_tournament_model_rank_top_20 | 14/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 32/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.830 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 13 | 13 | 0.683 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 63 | 63 | 0.601 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 4 | 4 | 0.731 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 3 | 3 | 0.737 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 11 | 11 | 0.690 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 2 | 2 | 0.758 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 34 | 34 | 0.644 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 40 | 40 | 0.634 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 33 | 33 | 0.654 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 17 | 17 | 0.678 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 86 | 86 | 0.562 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 19 | 19 | 0.678 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 5 | 5 | 0.723 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 16 | 16 | 0.680 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 15 | 15 | 0.681 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 7 | 7 | 0.715 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 92 | 92 | 0.550 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 18 | 18 | 0.678 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 20 | 20 | 0.674 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 54 | 54 | 0.613 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 26 | 26 | 0.663 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 66 | 66 | 0.595 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 77 | 77 | 0.576 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 51 | 51 | 0.618 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.830 | 157 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 2 | 2 | 0.758 | 78 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 3 | 3 | 0.737 | 92 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 4 | 4 | 0.731 | 93 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 5 | 5 | 0.723 | 90 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 6 | 6 | 0.716 | 49 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 7 | 7 | 0.715 | 72 |
| 31 | Andrew Zeng | Stanford | 28 | 28.235 | 480 | 8 | 8 | 0.707 | 48 |
| 71 | Rosa Xia | Cornell B | 21 | 21.176 | 360 | 9 | 9 | 0.701 | 33 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 10 | 10 | 0.691 | 38 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 11 | 11 | 0.690 | 99 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 12 | 12 | 0.689 | 55 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 13 | 13 | 0.683 | 125 |
| 32 | John John Groger | Columbia B | 27 | 27.941 | 475 | 14 | 14 | 0.682 | 36 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 15 | 15 | 0.681 | 80 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 16 | 16 | 0.680 | 69 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 17 | 17 | 0.678 | 89 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 18 | 18 | 0.678 | 62 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 19 | 19 | 0.678 | 81 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 20 | 20 | 0.674 | 62 |
| 52 | Dean Ah Now | Claremont Colleges | 24 | 24.706 | 420 | 21 | 21 | 0.671 | 40 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 22 | 22 | 0.670 | 52 |
| 49 | Tegan Kapadia | Georgia Tech | 25 | 25.588 | 435 | 23 | 23 | 0.668 | 51 |
| 57 | Rohan Shelke | Berkeley B | 23 | 23.235 | 395 | 24 | 24 | 0.666 | 49 |
| 65 | Nathan Zhang | Cornell A | 21 | 21.765 | 370 | 25 | 25 | 0.665 | 32 |
