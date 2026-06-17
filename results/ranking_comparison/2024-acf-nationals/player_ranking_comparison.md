# Player Ranking Comparison: 2024-acf-nationals

The real-world comparator here is tournament individual scoring from the source database, ranked by points per 20 tossups heard. The fitted model ranks players by mean predicted correctness on observed buzzes, so it rewards accuracy more than scoring volume.

Caveat: the source database does not include game-specific lineups, so tossups heard are inferred from registered rosters. That matches the modeling assumption used by this project, but it can blur players who did not play every game for their listed team.

## Summary

| metric | value |
| --- | --- |
| actual_players_after_floor | 187 |
| min_games | 8 |
| min_tuh | 160 |
| global_model_matches | 184 |
| tournament_model_matches | 184 |
| global_rank_correlation | 0.555 |
| tournament_rank_correlation | 0.553 |
| actual_top_20_in_global_model_rank_top_20 | 3/20 |
| actual_top_20_in_global_model_rank_top_50 | 4/20 |
| actual_top_20_in_global_model_rank_top_100 | 5/20 |
| actual_top_20_in_global_model_rank_top_200 | 10/20 |
| actual_top_20_in_tournament_model_rank_top_20 | 4/20 |
| actual_top_20_in_tournament_model_rank_top_50 | 10/20 |
| actual_top_20_in_tournament_model_rank_top_100 | 18/20 |
| actual_top_20_in_tournament_model_rank_top_200 | 20/20 |

## Actual Top 25

| actual_rank | name | team_name | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Matt Jackson | Chicago A | 86.176 | 1465 | 8 | 5 | 0.845 | 157 |
| 2 | Jason Hong | Brown | 58.235 | 990 | 172 | 41 | 0.727 | 125 |
| 3 | Joseph Chambers | Virginia | 52.941 | 900 | 354 | 80 | 0.665 | 137 |
| 4 | Caleb Kendrick | Maryland | 52.059 | 885 | 12 | 6 | 0.823 | 93 |
| 5 | Conor Thompson | Iowa State | 50.588 | 860 | 47 | 15 | 0.783 | 92 |
| 6 | Matthew Lehmann | WUSTL A | 48.235 | 820 | 223 | 58 | 0.712 | 99 |
| 7 | Forrest Weintraub | Columbia A | 47.941 | 815 | 9 | 4 | 0.850 | 78 |
| 8 | Jakob Myers | Indiana | 47.059 | 800 | 378 | 82 | 0.664 | 113 |
| 9 | Andrew Wang | Illinois | 44.062 | 705 | 406 | 93 | 0.652 | 100 |
| 10 | Sky Li | Toronto A | 43.529 | 740 | 382 | 83 | 0.662 | 87 |
| 11 | Chris Sims | Northwestern | 41.765 | 710 | 237 | 62 | 0.708 | 89 |
| 12 | Ashish Subramanian | Duke | 40.294 | 685 | 644 | 136 | 0.547 | 111 |
| 13 | Charles Hang | WUSTL A | 40.294 | 685 | 248 | 66 | 0.704 | 81 |
| 14 | Aum Mundhe | Rutgers | 40.000 | 680 | 146 | 34 | 0.740 | 90 |
| 15 | Fred Garvey | Truman State | 39.706 | 675 | 244 | 63 | 0.706 | 69 |
| 16 | Kevin Park | Claremont Colleges | 36.765 | 625 | 70 | 27 | 0.752 | 80 |
| 17 | Vincent Du | North Carolina A | 36.176 | 615 | 106 | 24 | 0.756 | 72 |
| 18 | Andrew Hanna | Penn | 35.294 | 600 | 462 | 108 | 0.628 | 102 |
| 19 | Joel Miles | Minnesota A | 35.000 | 560 | 125 | 35 | 0.737 | 62 |
| 20 | Richard Niu | Cornell A | 34.118 | 580 | 174 | 40 | 0.729 | 62 |
| 21 | Matthew Siff | Yale A | 33.824 | 575 | 141 | 42 | 0.727 | 77 |
| 22 | Jack Rado | Columbia B | 33.529 | 570 | 185 | 49 | 0.721 | 74 |
| 23 | Anuttam Ramji | Berkeley B | 32.941 | 560 | 448 | 84 | 0.660 | 88 |
| 24 | Adrian Wong | Ottawa | 32.500 | 520 | 593 | 129 | 0.573 | 78 |
| 25 | Chinmay Murthy | Texas | 31.471 | 535 | 144 | 47 | 0.724 | 69 |

## Tournament-Filtered Model Top 25

| actual_rank | name | team_name | actual_pp20 | actual_points | global_model_rank | tournament_model_rank | tournament_fitted_correctness | tournament_model_buzzes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 122 | Michael Hunding | Illinois | 14.375 | 230 | 1 | 1 | 0.870 | 24 |
| 49 | Tegan Kapadia | Georgia Tech | 25.588 | 435 | 4 | 2 | 0.868 | 51 |
| 46 | Nathaniel Hull | Berkeley A | 25.882 | 440 | 10 | 3 | 0.856 | 49 |
| 7 | Forrest Weintraub | Columbia A | 47.941 | 815 | 9 | 4 | 0.850 | 78 |
| 1 | Matt Jackson | Chicago A | 86.176 | 1465 | 8 | 5 | 0.845 | 157 |
| 4 | Caleb Kendrick | Maryland | 52.059 | 885 | 12 | 6 | 0.823 | 93 |
| 32 | John John Groger | Columbia B | 27.941 | 475 | 20 | 7 | 0.814 | 36 |
| 68 | Khushi Umarwadia | South Carolina | 21.471 | 365 | 32 | 8 | 0.814 | 38 |
| 125 | Andy Yu | Maryland | 13.529 | 230 | 3 | 9 | 0.811 | 18 |
| 172 | Sean Jackson | South Carolina | 5.588 | 95 | 39 | 10 | 0.806 | 4 |
| 112 | Arunn Sankar | Georgia Tech | 15.294 | 260 | 56 | 11 | 0.805 | 25 |
| 150 | William Foster | Chicago D | 9.412 | 160 | 204 | 12 | 0.799 | 18 |
| 59 | Neal Joshi | WUSTL B | 22.941 | 390 | 43 | 13 | 0.797 | 39 |
| 50 | Jeremy Cummings | WUSTL B | 25.294 | 430 | 94 | 14 | 0.794 | 50 |
| 5 | Conor Thompson | Iowa State | 50.588 | 860 | 47 | 15 | 0.783 | 92 |
| 52 | Dean Ah Now | Claremont Colleges | 24.706 | 420 | 50 | 16 | 0.780 | 40 |
| 57 | Rohan Shelke | Berkeley B | 23.235 | 395 | 142 | 17 | 0.778 | 49 |
| 120 | Eshan Pant | NYU | 14.412 | 245 | 28 | 18 | 0.778 | 34 |
| 31 | Andrew Zeng | Stanford | 28.235 | 480 | 114 | 19 | 0.775 | 48 |
| 62 | Ryan Sun | Berkeley B | 22.647 | 385 | 98 | 20 | 0.767 | 47 |
| 30 | Sinecio Morales | Johns Hopkins | 28.824 | 490 | 115 | 21 | 0.765 | 59 |
| 65 | Nathan Zhang | Cornell A | 21.765 | 370 | 100 | 22 | 0.761 | 32 |
| 36 | Rasheeq Azad | North Carolina B | 27.353 | 465 | 67 | 23 | 0.758 | 55 |
| 17 | Vincent Du | North Carolina A | 36.176 | 615 | 106 | 24 | 0.756 | 72 |
| 26 | Eve Fleisig | Berkeley A | 31.471 | 535 | 48 | 25 | 0.754 | 67 |
