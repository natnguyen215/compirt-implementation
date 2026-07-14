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
| tournament_rank_correlation | 0.674 |
| actual_top_20_in_tournament_model_rank_top_20 | 5/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 25/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 2 | 2 | 0.817 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 29 | 29 | 0.746 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 102 | 102 | 0.644 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 6 | 6 | 0.802 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 39 | 39 | 0.722 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 36 | 36 | 0.733 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 1 | 1 | 0.826 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 79 | 79 | 0.676 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 45 | 45 | 0.715 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 33 | 33 | 0.735 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 42 | 42 | 0.717 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 128 | 128 | 0.602 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 44 | 44 | 0.716 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 8 | 8 | 0.798 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 34 | 34 | 0.734 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 76 | 76 | 0.677 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 7 | 7 | 0.799 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 116 | 116 | 0.630 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 35 | 35 | 0.733 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 30 | 30 | 0.741 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 103 | 103 | 0.641 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 74 | 74 | 0.680 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 71 | 71 | 0.683 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 81 | 81 | 0.672 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 67 | 67 | 0.687 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 1 | 1 | 0.826 | 78 |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 2 | 2 | 0.817 | 157 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 3 | 3 | 0.811 | 38 |
| 123 | Michael Hunding | Illinois | 14 | 14.375 | 230 | 4 | 4 | 0.809 | 24 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 5 | 5 | 0.806 | 49 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 6 | 6 | 0.802 | 93 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 7 | 7 | 0.799 | 72 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 8 | 8 | 0.798 | 90 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 9 | 9 | 0.792 | 52 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 10 | 10 | 0.789 | 55 |
| 32 | John John Groger | Columbia B | 27 | 27.941 | 475 | 11 | 11 | 0.786 | 36 |
| 64 | Jonathan Lau | Johns Hopkins | 22 | 22.059 | 375 | 12 | 12 | 0.784 | 30 |
| 50 | Jeremy Cummings | WUSTL B | 25 | 25.294 | 430 | 13 | 13 | 0.782 | 50 |
| 65 | Nathan Zhang | Cornell A | 21 | 21.765 | 370 | 14 | 14 | 0.778 | 32 |
| 61 | Matt Schiavone | Purdue | 22 | 22.647 | 385 | 15 | 15 | 0.777 | 36 |
| 84 | Dennis Reppen | Chicago C | 19 | 19.688 | 315 | 16 | 16 | 0.775 | 32 |
| 31 | Andrew Zeng | Stanford | 28 | 28.235 | 480 | 17 | 17 | 0.774 | 48 |
| 49 | Tegan Kapadia | Georgia Tech | 25 | 25.588 | 435 | 18 | 18 | 0.770 | 51 |
| 60 | Graham Troy | North Carolina B | 22 | 22.647 | 385 | 19 | 19 | 0.768 | 39 |
| 71 | Rosa Xia | Cornell B | 21 | 21.176 | 360 | 20 | 20 | 0.766 | 33 |
| 26 | Eve Fleisig | Berkeley A | 31 | 31.471 | 535 | 21 | 21 | 0.760 | 67 |
| 54 | Jeffrey Fung | Harvard | 23 | 23.824 | 405 | 22 | 22 | 0.758 | 36 |
| 52 | Dean Ah Now | Claremont Colleges | 24 | 24.706 | 420 | 23 | 23 | 0.758 | 40 |
| 146 | Megan Wang | Brown | 10 | 10.294 | 175 | 24 | 24 | 0.756 | 19 |
| 57 | Rohan Shelke | Berkeley B | 23 | 23.235 | 395 | 25 | 25 | 0.752 | 49 |
