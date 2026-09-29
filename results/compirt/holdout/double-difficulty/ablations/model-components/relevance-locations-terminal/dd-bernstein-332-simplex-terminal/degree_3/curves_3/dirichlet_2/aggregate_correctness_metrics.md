# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `.` | in-sample | 0.809337 | 0.465761 | 0.042002 | 6.511866 | 0.447260 | 0.809035 | 0.077319 | 0.160666 | 0.381206 | -0.002308 | 0.178179 |
| `.` | held-out | 0.773134 | 0.373405 | 0.006144 | 6.721603 | 0.502132 | 0.714030 | 0.070702 | 0.166723 | 0.336722 | -0.001945 | 0.175156 |
