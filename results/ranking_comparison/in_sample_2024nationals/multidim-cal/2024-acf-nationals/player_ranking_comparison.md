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
| tournament_rank_correlation | 0.760 |
| actual_top_20_in_tournament_model_rank_top_20 | 11/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 32/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.853 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 6 | 6 | 0.811 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 77 | 77 | 0.743 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 2 | 2 | 0.828 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 37 | 37 | 0.765 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 4 | 4 | 0.820 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 3 | 3 | 0.827 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 40 | 40 | 0.763 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 17 | 17 | 0.789 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 12 | 12 | 0.794 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 20 | 20 | 0.787 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 121 | 121 | 0.713 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 24 | 24 | 0.781 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 22 | 22 | 0.786 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 18 | 18 | 0.789 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 30 | 30 | 0.771 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 13 | 13 | 0.793 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 71 | 71 | 0.746 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 28 | 28 | 0.774 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 8 | 8 | 0.798 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 57 | 57 | 0.751 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 75 | 75 | 0.744 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 42 | 42 | 0.760 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 64 | 64 | 0.749 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 68 | 68 | 0.747 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.853 | 157 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 2 | 2 | 0.828 | 93 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 3 | 3 | 0.827 | 78 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 4 | 4 | 0.820 | 99 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 5 | 5 | 0.818 | 49 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 6 | 6 | 0.811 | 125 |
| 31 | Andrew Zeng | Stanford | 28 | 28.235 | 480 | 7 | 7 | 0.807 | 48 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 8 | 8 | 0.798 | 62 |
| 26 | Eve Fleisig | Berkeley A | 31 | 31.471 | 535 | 9 | 9 | 0.795 | 67 |
| 87 | Ryan Humphrey | Texas | 18 | 18.529 | 315 | 10 | 10 | 0.795 | 36 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 11 | 11 | 0.794 | 38 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 12 | 12 | 0.794 | 87 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 13 | 13 | 0.793 | 72 |
| 32 | John John Groger | Columbia B | 27 | 27.941 | 475 | 14 | 14 | 0.793 | 36 |
| 38 | Mattias Ehatamm | Waterloo | 27 | 27.059 | 460 | 15 | 15 | 0.791 | 55 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 16 | 16 | 0.790 | 52 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 17 | 17 | 0.789 | 100 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 18 | 18 | 0.789 | 69 |
| 50 | Jeremy Cummings | WUSTL B | 25 | 25.294 | 430 | 19 | 19 | 0.788 | 50 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 20 | 20 | 0.787 | 89 |
| 49 | Tegan Kapadia | Georgia Tech | 25 | 25.588 | 435 | 21 | 21 | 0.787 | 51 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 22 | 22 | 0.786 | 90 |
| 123 | Michael Hunding | Illinois | 14 | 14.375 | 230 | 23 | 23 | 0.786 | 24 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 24 | 24 | 0.781 | 81 |
| 34 | Bryan Ugaz | Arizona State | 27 | 27.647 | 470 | 25 | 25 | 0.777 | 67 |
