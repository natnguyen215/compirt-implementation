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
| tournament_rank_correlation | 0.717 |
| actual_top_20_in_tournament_model_rank_top_20 | 11/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 32/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.849 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 11 | 11 | 0.800 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 70 | 70 | 0.740 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 3 | 3 | 0.838 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 47 | 47 | 0.754 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 5 | 5 | 0.817 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 2 | 2 | 0.845 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 74 | 74 | 0.738 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 27 | 27 | 0.772 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 20 | 20 | 0.790 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 15 | 15 | 0.796 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 132 | 132 | 0.702 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 29 | 29 | 0.770 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 6 | 6 | 0.813 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 22 | 22 | 0.786 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 62 | 62 | 0.747 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 14 | 14 | 0.798 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 87 | 87 | 0.729 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 18 | 18 | 0.790 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 4 | 4 | 0.826 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 58 | 58 | 0.747 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 38 | 38 | 0.761 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 34 | 34 | 0.764 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 42 | 42 | 0.757 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 85 | 85 | 0.732 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.849 | 157 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 2 | 2 | 0.845 | 78 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 3 | 3 | 0.838 | 93 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 4 | 4 | 0.826 | 62 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 5 | 5 | 0.817 | 99 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 6 | 6 | 0.813 | 90 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 7 | 7 | 0.811 | 49 |
| 31 | Andrew Zeng | Stanford | 28 | 28.235 | 480 | 8 | 8 | 0.804 | 48 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 9 | 9 | 0.801 | 52 |
| 26 | Eve Fleisig | Berkeley A | 31 | 31.471 | 535 | 10 | 10 | 0.801 | 67 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 11 | 11 | 0.800 | 125 |
| 50 | Jeremy Cummings | WUSTL B | 25 | 25.294 | 430 | 12 | 12 | 0.799 | 50 |
| 123 | Michael Hunding | Illinois | 14 | 14.375 | 230 | 13 | 13 | 0.799 | 24 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 14 | 14 | 0.798 | 72 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 15 | 15 | 0.796 | 89 |
| 65 | Nathan Zhang | Cornell A | 21 | 21.765 | 370 | 16 | 16 | 0.792 | 32 |
| 32 | John John Groger | Columbia B | 27 | 27.941 | 475 | 17 | 17 | 0.792 | 36 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 18 | 18 | 0.790 | 62 |
| 29 | Tim Morrison | Stanford | 30 | 30.294 | 515 | 19 | 19 | 0.790 | 72 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 20 | 20 | 0.790 | 87 |
| 38 | Mattias Ehatamm | Waterloo | 27 | 27.059 | 460 | 21 | 21 | 0.789 | 55 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 22 | 22 | 0.786 | 69 |
| 52 | Dean Ah Now | Claremont Colleges | 24 | 24.706 | 420 | 23 | 23 | 0.784 | 40 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 24 | 24 | 0.780 | 55 |
| 49 | Tegan Kapadia | Georgia Tech | 25 | 25.588 | 435 | 25 | 25 | 0.779 | 51 |
