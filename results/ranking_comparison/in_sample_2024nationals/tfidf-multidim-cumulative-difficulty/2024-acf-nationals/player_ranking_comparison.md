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
| tournament_rank_correlation | 0.808 |
| actual_top_20_in_tournament_model_rank_top_20 | 10/20 |
| actual_top_50_in_tournament_model_rank_top_50 | 32/50 |

## Actual Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.860 | 157 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 18 | 18 | 0.740 | 125 |
| 3 | Joseph Chambers | Virginia | 52 | 52.941 | 900 | 91 | 91 | 0.601 | 137 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 3 | 3 | 0.804 | 93 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 19 | 19 | 0.738 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 11 | 11 | 0.759 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 2 | 2 | 0.843 | 78 |
| 8 | Jakob Myers | Indiana | 47 | 47.059 | 800 | 35 | 35 | 0.698 | 113 |
| 9 | Andrew Wang | Illinois | 44 | 44.062 | 705 | 36 | 36 | 0.698 | 100 |
| 10 | Sky Li | Toronto A | 43 | 43.529 | 740 | 57 | 57 | 0.663 | 87 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 21 | 21 | 0.735 | 89 |
| 12 | Ashish Subramanian | Duke | 40 | 40.294 | 685 | 95 | 95 | 0.592 | 111 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 12 | 12 | 0.759 | 81 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 16 | 16 | 0.743 | 90 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 25 | 25 | 0.726 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36 | 36.765 | 625 | 26 | 26 | 0.713 | 80 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 5 | 5 | 0.785 | 72 |
| 18 | Andrew Hanna | Penn | 35 | 35.294 | 600 | 98 | 98 | 0.592 | 102 |
| 19 | Joel Miles | Minnesota A | 35 | 35.000 | 560 | 41 | 41 | 0.692 | 62 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 14 | 14 | 0.757 | 62 |
| 21 | Matthew Siff | Yale A | 33 | 33.824 | 575 | 48 | 48 | 0.678 | 77 |
| 22 | Jack Rado | Columbia B | 33 | 33.529 | 570 | 29 | 29 | 0.707 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32 | 32.941 | 560 | 63 | 63 | 0.650 | 88 |
| 24 | Adrian Wong | Ottawa | 32 | 32.500 | 520 | 75 | 75 | 0.629 | 78 |
| 25 | Chinmay Murthy | Texas | 31 | 31.471 | 535 | 45 | 45 | 0.683 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_ppg | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86 | 86.176 | 1465 | 1 | 1 | 0.860 | 157 |
| 7 | Forrest Weintraub | Columbia A | 47 | 47.941 | 815 | 2 | 2 | 0.843 | 78 |
| 4 | Caleb Kendrick | Maryland | 52 | 52.059 | 885 | 3 | 3 | 0.804 | 93 |
| 65 | Nathan Zhang | Cornell A | 21 | 21.765 | 370 | 4 | 4 | 0.796 | 32 |
| 17 | Vincent Du | North Carolina A | 36 | 36.176 | 615 | 5 | 5 | 0.785 | 72 |
| 31 | Andrew Zeng | Stanford | 28 | 28.235 | 480 | 6 | 6 | 0.784 | 48 |
| 46 | Nathaniel Hull | Berkeley A | 25 | 25.882 | 440 | 7 | 7 | 0.783 | 49 |
| 61 | Matt Schiavone | Purdue | 22 | 22.647 | 385 | 8 | 8 | 0.773 | 36 |
| 68 | Khushi Umarwadia | South Carolina | 21 | 21.471 | 365 | 9 | 9 | 0.772 | 38 |
| 123 | Michael Hunding | Illinois | 14 | 14.375 | 230 | 10 | 10 | 0.760 | 24 |
| 6 | Matthew Lehmann | WUSTL A | 48 | 48.235 | 820 | 11 | 11 | 0.759 | 99 |
| 13 | Charles Hang | WUSTL A | 40 | 40.294 | 685 | 12 | 12 | 0.759 | 81 |
| 36 | Rasheeq Azad | North Carolina B | 27 | 27.353 | 465 | 13 | 13 | 0.759 | 55 |
| 20 | Richard Niu | Cornell A | 34 | 34.118 | 580 | 14 | 14 | 0.757 | 62 |
| 43 | Sam Baker | McGill | 26 | 26.176 | 445 | 15 | 15 | 0.748 | 52 |
| 14 | Aum Mundhe | Rutgers | 40 | 40.000 | 680 | 16 | 16 | 0.743 | 90 |
| 49 | Tegan Kapadia | Georgia Tech | 25 | 25.588 | 435 | 17 | 17 | 0.742 | 51 |
| 2 | Jason Hong | Brown | 58 | 58.235 | 990 | 18 | 18 | 0.740 | 125 |
| 5 | Conor Thompson | Iowa State | 50 | 50.588 | 860 | 19 | 19 | 0.738 | 92 |
| 32 | John John Groger | Columbia B | 27 | 27.941 | 475 | 20 | 20 | 0.738 | 36 |
| 11 | Chris Sims | Northwestern | 41 | 41.765 | 710 | 21 | 21 | 0.735 | 89 |
| 26 | Eve Fleisig | Berkeley A | 31 | 31.471 | 535 | 22 | 22 | 0.733 | 67 |
| 89 | Arthur Delot-Vilain | Yale A | 17 | 17.941 | 305 | 23 | 23 | 0.729 | 29 |
| 52 | Dean Ah Now | Claremont Colleges | 24 | 24.706 | 420 | 24 | 24 | 0.729 | 40 |
| 15 | Fred Garvey | Truman State | 39 | 39.706 | 675 | 25 | 25 | 0.726 | 69 |
