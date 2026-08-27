# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.797572 | 0.302886 | 0.030236 | 6.405448 | 0.435495 | 0.813563 | 0.054623 | 0.146273 | 0.393159 | 0.000216 | 0.190831 |
| `.` | held-out | 0.779493 | 0.232093 | 0.012502 | 6.612269 | 0.487803 | 0.715466 | 0.012510 | 0.151862 | 0.351634 | 0.000930 | 0.188189 |
