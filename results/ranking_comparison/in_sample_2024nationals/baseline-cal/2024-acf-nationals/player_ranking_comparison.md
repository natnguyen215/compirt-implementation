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
| tournament_rank_correlation | 0.546 |
| actual_top_20_in_tournament_model_rank_top_20 | 5/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 25/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 11 | 11 | 0.784 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 28 | 28 | 0.762 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 111 | 111 | 0.714 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 4 | 4 | 0.795 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 64 | 64 | 0.741 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 26 | 26 | 0.764 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 5 | 5 | 0.790 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 128 | 128 | 0.697 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 61 | 61 | 0.744 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 12 | 12 | 0.778 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 31 | 31 | 0.761 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 133 | 133 | 0.695 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 105 | 105 | 0.719 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 6 | 6 | 0.789 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 35 | 35 | 0.759 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 104 | 104 | 0.719 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 51 | 51 | 0.751 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 101 | 101 | 0.720 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 29 | 29 | 0.761 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 25 | 25 | 0.766 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 122 | 122 | 0.701 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 102 | 102 | 0.719 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 60 | 60 | 0.745 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 39 | 39 | 0.756 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 59 | 59 | 0.745 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 123 | Michael Hunding | Illinois | 14 | 14.375 | 230 | 1 | 1 | 0.820 | 24 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 2 | 2 | 0.803 | 49 |
| 50 | Jeremy Cummings | WUSTL B | 25 | 25.294 | 430 | 3 | 3 | 0.802 | 50 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 4 | 4 | 0.795 | 93 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 5 | 5 | 0.790 | 78 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 6 | 6 | 0.789 | 90 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 7 | 7 | 0.788 | 52 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 8 | 8 | 0.788 | 38 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 9 | 9 | 0.785 | 55 |
| 57 | Rohan Shelke | Berkeley B | 23 | 23.235 | 395 | 10 | 10 | 0.784 | 49 |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 11 | 11 | 0.784 | 157 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 12 | 12 | 0.778 | 87 |
| 92 | Alex Akridge | Indiana | 17 | 17.647 | 300 | 13 | 13 | 0.777 | 41 |
| 146 | Megan Wang | Brown | 10 | 10.294 | 175 | 14 | 14 | 0.776 | 19 |
| 32 | John John Groger | Columbia B | 27 | 27.941 | 475 | 15 | 15 | 0.773 | 36 |
| 26 | Eve Fleisig | Berkeley A | 31 | 31.471 | 535 | 16 | 16 | 0.773 | 67 |
| 38 | Mattias Ehatamm | Waterloo | 27 | 27.059 | 460 | 17 | 17 | 0.772 | 55 |
| 158 | Justin Zhang | Duke | 8 | 8.235 | 140 | 18 | 18 | 0.772 | 20 |
| 64 | Jonathan Lau | Johns Hopkins | 22 | 22.059 | 375 | 19 | 19 | 0.772 | 30 |
| 71 | Rosa Xia | Cornell B | 21 | 21.176 | 360 | 20 | 20 | 0.770 | 33 |
| 31 | Andrew Zeng | Stanford | 28 | 28.235 | 480 | 21 | 21 | 0.769 | 48 |
| 59 | Neal Joshi | WUSTL B | 22 | 22.941 | 390 | 22 | 22 | 0.768 | 39 |
| 77 | Jacob Hardin-Bernhardt | NYU | 20 | 20.294 | 345 | 23 | 23 | 0.767 | 43 |
| 34 | Bryan Ugaz | Arizona State | 27 | 27.647 | 470 | 24 | 24 | 0.767 | 67 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 25 | 25 | 0.766 | 62 |
