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
| tournament_rank_correlation | 0.593 |
| actual_top_20_in_tournament_model_rank_top_20 | 7/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 28/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 2 | 2 | 0.797 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 30 | 30 | 0.759 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 112 | 112 | 0.713 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 4 | 4 | 0.794 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 23 | 23 | 0.763 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 15 | 15 | 0.771 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 5 | 5 | 0.790 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 108 | 108 | 0.716 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 22 | 22 | 0.764 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 14 | 14 | 0.772 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 32 | 32 | 0.758 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 131 | 131 | 0.697 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 93 | 93 | 0.724 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 6 | 6 | 0.785 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 24 | 24 | 0.762 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 86 | 86 | 0.729 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 33 | 33 | 0.757 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 82 | 82 | 0.730 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 25 | 25 | 0.762 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 17 | 17 | 0.769 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 125 | 125 | 0.702 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 104 | 104 | 0.718 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 46 | 46 | 0.748 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 44 | 44 | 0.750 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 90 | 90 | 0.726 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 1 | 1 | 0.803 | 49 |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 2 | 2 | 0.797 | 157 |
| 123 | Michael Hunding | Illinois | 14 | 14.375 | 230 | 3 | 3 | 0.794 | 24 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 4 | 4 | 0.794 | 93 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 5 | 5 | 0.790 | 78 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 6 | 6 | 0.785 | 90 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 7 | 7 | 0.785 | 38 |
| 57 | Rohan Shelke | Berkeley B | 23 | 23.235 | 395 | 8 | 8 | 0.782 | 49 |
| 50 | Jeremy Cummings | WUSTL B | 25 | 25.294 | 430 | 9 | 9 | 0.781 | 50 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 10 | 10 | 0.779 | 55 |
| 32 | John John Groger | Columbia B | 27 | 27.941 | 475 | 11 | 11 | 0.776 | 36 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 12 | 12 | 0.775 | 52 |
| 38 | Mattias Ehatamm | Waterloo | 27 | 27.059 | 460 | 13 | 13 | 0.772 | 55 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 14 | 14 | 0.772 | 87 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 15 | 15 | 0.771 | 99 |
| 26 | Eve Fleisig | Berkeley A | 31 | 31.471 | 535 | 16 | 16 | 0.769 | 67 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 17 | 17 | 0.769 | 62 |
| 31 | Andrew Zeng | Stanford | 28 | 28.235 | 480 | 18 | 18 | 0.769 | 48 |
| 49 | Tegan Kapadia | Georgia Tech | 25 | 25.588 | 435 | 19 | 19 | 0.768 | 51 |
| 158 | Justin Zhang | Duke | 8 | 8.235 | 140 | 20 | 20 | 0.768 | 20 |
| 29 | Tim Morrison | Stanford | 30 | 30.294 | 515 | 21 | 21 | 0.764 | 72 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 22 | 22 | 0.764 | 100 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 23 | 23 | 0.763 | 92 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 24 | 24 | 0.762 | 69 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 25 | 25 | 0.762 | 62 |
