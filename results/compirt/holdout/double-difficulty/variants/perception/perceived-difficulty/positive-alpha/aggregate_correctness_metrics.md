# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.696431 | 0.391013 | -0.070905 | 6.214868 | 0.595514 | 0.656492 | 0.184266 | 0.126521 | 0.455233 | 0.034885 | 0.140651 |
| `.` | held-out | 0.648728 | 0.355947 | -0.118263 | 6.637349 | 0.635948 | 0.601681 | 0.202172 | 0.136340 | 0.391843 | 0.034329 | 0.138518 |
