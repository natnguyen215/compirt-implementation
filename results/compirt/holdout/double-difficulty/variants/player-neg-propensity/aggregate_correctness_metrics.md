# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.798956 | 0.314159 | 0.031620 | 6.379021 | 0.432863 | 0.815790 | 0.053595 | 0.145785 | 0.400051 | 0.000038 | 0.189111 |
| `.` | held-out | 0.779485 | 0.239176 | 0.012495 | 6.582795 | 0.487771 | 0.715776 | 0.012841 | 0.151078 | 0.360863 | 0.000690 | 0.186633 |
