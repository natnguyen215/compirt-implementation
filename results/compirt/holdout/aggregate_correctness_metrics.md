# Research Log models: in-sample versus held-out metrics

Both samples use unweighted fold means, matching the Research Log main table. Each model has one fitted-training row and one frozen-held-out row.

| model | sample | accuracy | Neg F1 | lift | joint event LL | correctness LL | AUC | ECE | position MAE | first-buzzer top-1 | no-buzz error | final-decile mass |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `double-difficulty/model-comparisons/compact-parameterization/full-bernstein-332/degree_3/curves_3/dirichlet_2` | in-sample | 0.810907 | 0.514289 | 0.043572 | 6.073468 | 0.425029 | 0.818831 | 0.056585 | 0.127629 | 0.433022 | -0.005036 | 0.191641 |
| `double-difficulty/model-comparisons/compact-parameterization/full-bernstein-332/degree_3/curves_3/dirichlet_2` | held-out | 0.765455 | 0.411095 | -0.001536 | 6.437505 | 0.505854 | 0.716635 | 0.070584 | 0.136436 | 0.379875 | -0.004869 | 0.189412 |
| `double-difficulty/reference-model` | in-sample | 0.797572 | 0.302886 | 0.030236 | 6.405448 | 0.435495 | 0.813563 | 0.054623 | 0.146273 | 0.393159 | 0.000216 | 0.190831 |
| `double-difficulty/reference-model` | held-out | 0.779493 | 0.232093 | 0.012502 | 6.612269 | 0.487803 | 0.715466 | 0.012510 | 0.151862 | 0.351634 | 0.000930 | 0.188189 |
| `double-difficulty/variants/player-neg-propensity` | in-sample | 0.798956 | 0.314159 | 0.031620 | 6.379021 | 0.432863 | 0.815790 | 0.053595 | 0.145785 | 0.400051 | 0.000038 | 0.189111 |
| `double-difficulty/variants/player-neg-propensity` | held-out | 0.779485 | 0.239176 | 0.012495 | 6.582795 | 0.487771 | 0.715776 | 0.012841 | 0.151078 | 0.360863 | 0.000690 | 0.186633 |
| `double-difficulty/ablations/terminal-cell-intercepts/off/degree_3/curves_3/dirichlet_2` | in-sample | 0.809894 | 0.468513 | 0.042558 | 6.548653 | 0.444923 | 0.810267 | 0.074991 | 0.172284 | 0.384083 | 0.064993 | 0.096939 |
| `double-difficulty/ablations/terminal-cell-intercepts/off/degree_3/curves_3/dirichlet_2` | held-out | 0.771619 | 0.368444 | 0.004629 | 6.744418 | 0.502547 | 0.711492 | 0.067294 | 0.178267 | 0.340354 | 0.064398 | 0.094827 |
| `double-difficulty/ablations/terminal-cell-intercepts/on/degree_3/curves_3/dirichlet_2` | in-sample | 0.809337 | 0.465761 | 0.042002 | 6.511866 | 0.447260 | 0.809035 | 0.077319 | 0.160666 | 0.381206 | -0.002308 | 0.178179 |
| `double-difficulty/ablations/terminal-cell-intercepts/on/degree_3/curves_3/dirichlet_2` | held-out | 0.773134 | 0.373405 | 0.006144 | 6.721603 | 0.502132 | 0.714030 | 0.070702 | 0.166723 | 0.336722 | -0.001945 | 0.175156 |
| `double-difficulty/ablations/hyperparameter-grid/degree_3/curves_3/dirichlet_2` | in-sample | 0.806299 | 0.498207 | 0.038964 | 6.148097 | 0.430863 | 0.812355 | 0.057210 | 0.130552 | 0.433970 | 0.045654 | 0.130964 |
| `double-difficulty/ablations/hyperparameter-grid/degree_3/curves_3/dirichlet_2` | held-out | 0.762799 | 0.400738 | -0.004192 | 6.495917 | 0.509441 | 0.711382 | 0.072503 | 0.138891 | 0.380824 | 0.045312 | 0.129172 |
| `double-difficulty/model-comparisons/curve-family/linear-spline/seed_42` | in-sample | 0.855812 | 0.674079 | 0.088477 | 5.730020 | 0.337989 | 0.898072 | 0.059008 | 0.125385 | 0.477136 | 0.033617 | 0.179825 |
| `double-difficulty/model-comparisons/curve-family/linear-spline/seed_42` | held-out | 0.734504 | 0.462773 | -0.032486 | 6.459592 | 0.565126 | 0.722822 | 0.118483 | 0.135931 | 0.397445 | 0.033684 | 0.177649 |
| `double-difficulty/model-comparisons/curve-family/monotone-linear-spline` | in-sample | 0.687854 | 0.501362 | -0.079481 | 7.421016 | 0.657955 | 0.746696 | 0.189938 | 0.141915 | 0.379718 | 0.187038 | 0.166575 |
| `double-difficulty/model-comparisons/curve-family/monotone-linear-spline` | held-out | 0.633953 | 0.430079 | -0.133037 | 8.144595 | 0.836675 | 0.657073 | 0.226474 | 0.150999 | 0.324749 | 0.182172 | 0.163887 |
| `double-difficulty/variants/perceived-difficulty/unconstrained` | in-sample | 0.784115 | 0.270023 | 0.016780 | 7.430461 | 0.479097 | 0.741427 | 0.037165 | 0.324755 | 0.396005 | 0.208716 | 0.033066 |
| `double-difficulty/variants/perceived-difficulty/unconstrained` | held-out | 0.768330 | 0.217730 | 0.001339 | 7.617837 | 0.516634 | 0.660483 | 0.035030 | 0.327728 | 0.350968 | 0.208150 | 0.032263 |
| `double-difficulty/variants/perceived-difficulty/positive-alpha` | in-sample | 0.696431 | 0.391013 | -0.070905 | 6.214868 | 0.595514 | 0.656492 | 0.184266 | 0.126521 | 0.455233 | 0.034885 | 0.140651 |
| `double-difficulty/variants/perceived-difficulty/positive-alpha` | held-out | 0.648728 | 0.355947 | -0.118263 | 6.637349 | 0.635948 | 0.601681 | 0.202172 | 0.136340 | 0.391843 | 0.034329 | 0.138518 |
| `double-difficulty/variants/perceived-difficulty/three-slice-alternating-10000-steps` | in-sample | 0.680686 | 0.420073 | -0.086650 | 6.280054 | 0.608138 | 0.671653 | 0.198744 | 0.129757 | 0.422249 | 0.035885 | 0.144310 |
| `double-difficulty/variants/perceived-difficulty/three-slice-alternating-10000-steps` | held-out | 0.628580 | 0.380605 | -0.138411 | 6.765616 | 0.661202 | 0.616429 | 0.220678 | 0.138908 | 0.366702 | 0.036269 | 0.142022 |
| `double-difficulty/variants/perceived-difficulty/three-slice-alternating` | in-sample | 0.600751 | 0.406063 | -0.166584 | 6.318673 | 0.687221 | 0.636733 | 0.262922 | 0.129636 | 0.421477 | 0.035534 | 0.140865 |
| `double-difficulty/variants/perceived-difficulty/three-slice-alternating` | held-out | 0.550420 | 0.381149 | -0.216570 | 6.862385 | 0.733708 | 0.593885 | 0.282242 | 0.139181 | 0.360909 | 0.035288 | 0.138012 |
| `double-difficulty/variants/perceived-difficulty/three-slice` | in-sample | 0.637266 | 0.411483 | -0.130069 | 6.246709 | 0.655321 | 0.650030 | 0.237859 | 0.128748 | 0.436307 | 0.037643 | 0.139734 |
| `double-difficulty/variants/perceived-difficulty/three-slice` | held-out | 0.585725 | 0.379898 | -0.181266 | 6.807457 | 0.704994 | 0.600866 | 0.258387 | 0.138301 | 0.375047 | 0.037590 | 0.136705 |
| `double-difficulty/variants/perceived-logit/unconstrained` | in-sample | 0.767944 | 0.019759 | 0.000609 | 7.589886 | 0.562989 | 0.622808 | 0.089990 | 0.340038 | 0.400857 | 0.222538 | 0.029189 |
| `double-difficulty/variants/perceived-logit/unconstrained` | held-out | 0.766490 | 0.016726 | -0.000501 | 7.777616 | 0.608011 | 0.548631 | 0.105813 | 0.341802 | 0.351546 | 0.222829 | 0.028632 |
| `double-difficulty/variants/perceived-logit/positive-alpha` | in-sample | 0.396744 | 0.399181 | -0.370592 | 6.437382 | 0.764628 | 0.628399 | 0.334871 | 0.129701 | 0.437494 | 0.036821 | 0.129145 |
| `double-difficulty/variants/perceived-logit/positive-alpha` | held-out | 0.375861 | 0.392111 | -0.391130 | 6.758884 | 0.787527 | 0.606510 | 0.345781 | 0.137620 | 0.391814 | 0.036482 | 0.127520 |
