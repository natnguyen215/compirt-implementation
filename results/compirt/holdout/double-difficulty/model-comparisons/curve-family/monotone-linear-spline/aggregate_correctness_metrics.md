# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.687854 | 0.501362 | -0.079481 | 7.421016 | 0.657955 | 0.746696 | 0.189938 | 0.141915 | 0.379718 | 0.187038 | 0.166575 |
| `.` | held-out | 0.633953 | 0.430079 | -0.133037 | 8.144595 | 0.836675 | 0.657073 | 0.226474 | 0.150999 | 0.324749 | 0.182172 | 0.163887 |
