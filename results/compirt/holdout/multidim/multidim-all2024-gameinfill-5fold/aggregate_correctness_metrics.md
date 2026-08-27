# All held-out model correctness metrics

Pooled metrics use only rows with an observed buzz. Training metrics pool each fold's fitted training predictions; held-out metrics pool the corresponding frozen-replay predictions.

The three training columns are pooled across fitted training folds. All held-out columns are unweighted fold means, matching the Research Log main table.

| model | train accuracy | train AUC | train log loss | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | 0.707540 | 0.705408 | 0.587462 | 0.627567 |  | -0.139423 | 6.775575 | 0.810913 | 0.631977 | 0.219323 | 0.145426 | 0.395818 |  |  |
