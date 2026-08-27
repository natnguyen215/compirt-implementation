# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.600751 | 0.406063 | -0.166584 | 6.318673 | 0.687221 | 0.636733 | 0.262922 | 0.129636 | 0.421477 | 0.035534 | 0.140865 |
| `.` | held-out | 0.550420 | 0.381149 | -0.216570 | 6.862385 | 0.733708 | 0.593885 | 0.282242 | 0.139181 | 0.360909 | 0.035288 | 0.138012 |
