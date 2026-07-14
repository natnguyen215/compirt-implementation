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
| tournament_rank_correlation | 0.455 |
| actual_top_20_in_tournament_model_rank_top_20 | 4/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 18/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 17 | 17 | 0.694 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 73 | 73 | 0.605 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 139 | 139 | 0.509 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 18 | 18 | 0.693 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 81 | 81 | 0.590 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 77 | 77 | 0.600 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 11 | 11 | 0.720 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 96 | 96 | 0.563 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 130 | 130 | 0.522 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 84 | 84 | 0.584 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 32 | 32 | 0.662 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 103 | 103 | 0.556 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 54 | 54 | 0.627 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 8 | 8 | 0.732 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 92 | 92 | 0.568 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 108 | 108 | 0.546 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 31 | 31 | 0.670 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 154 | 154 | 0.490 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 40 | 40 | 0.640 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 64 | 64 | 0.609 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 134 | 134 | 0.518 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 49 | 49 | 0.630 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 61 | 61 | 0.622 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 109 | 109 | 0.546 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 66 | 66 | 0.608 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 123 | Michael Hunding | Illinois | 14 | 14.375 | 230 | 1 | 1 | 0.768 | 24 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 2 | 2 | 0.757 | 49 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 3 | 3 | 0.748 | 52 |
| 65 | Nathan Zhang | Cornell A | 21 | 21.765 | 370 | 4 | 4 | 0.741 | 32 |
| 49 | Tegan Kapadia | Georgia Tech | 25 | 25.588 | 435 | 5 | 5 | 0.737 | 51 |
| 146 | Megan Wang | Brown | 10 | 10.294 | 175 | 6 | 6 | 0.733 | 19 |
| 60 | Graham Troy | North Carolina B | 22 | 22.647 | 385 | 7 | 7 | 0.732 | 39 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 8 | 8 | 0.732 | 90 |
| 31 | Andrew Zeng | Stanford | 28 | 28.235 | 480 | 9 | 9 | 0.728 | 48 |
| 52 | Dean Ah Now | Claremont Colleges | 24 | 24.706 | 420 | 10 | 10 | 0.721 | 40 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 11 | 11 | 0.720 | 78 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 12 | 12 | 0.716 | 38 |
| 61 | Matt Schiavone | Purdue | 22 | 22.647 | 385 | 13 | 13 | 0.709 | 36 |
| 84 | Dennis Reppen | Chicago C | 19 | 19.688 | 315 | 14 | 14 | 0.702 | 32 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 15 | 15 | 0.700 | 55 |
| 64 | Jonathan Lau | Johns Hopkins | 22 | 22.059 | 375 | 16 | 16 | 0.698 | 30 |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 17 | 17 | 0.694 | 157 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 18 | 18 | 0.693 | 93 |
| 71 | Rosa Xia | Cornell B | 21 | 21.176 | 360 | 19 | 19 | 0.693 | 33 |
| 95 | Donal Ryan | Truman State | 17 | 17.059 | 290 | 20 | 20 | 0.683 | 26 |
| 158 | Justin Zhang | Duke | 8 | 8.235 | 140 | 21 | 21 | 0.683 | 20 |
| 28 | Andrew Kelley | Kentucky | 30 | 30.294 | 515 | 22 | 22 | 0.682 | 75 |
| 94 | Jisoo Yoo | Texas | 17 | 17.647 | 300 | 23 | 23 | 0.681 | 40 |
| 89 | Arthur Delot-Vilain | Yale A | 17 | 17.941 | 305 | 24 | 24 | 0.679 | 29 |
| 82 | Will Orr | Yale B | 19 | 19.706 | 335 | 25 | 25 | 0.677 | 51 |
