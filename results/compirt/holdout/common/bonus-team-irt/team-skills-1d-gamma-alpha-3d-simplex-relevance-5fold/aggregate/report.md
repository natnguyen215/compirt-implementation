# Bonus-only team IRT

3,000 AutoNormal SVI steps, learning rate 0.01, fit seed 42; 5 year_2024 whole-game folds, split seed 42.

Team parameters use tournament-specific team IDs. 1D: P(correct) = sigmoid(theta_team * alpha_part - beta_part), with alpha ~ Gamma(2,2) (shape/rate). Multidimensional: P(correct) = sigmoid(sum_k r_part,k * (theta_team,k - beta_part,k)), with r_part ~ Dirichlet(1) on the simplex. Priors are independent theta ~ Normal(0,1) and beta ~ Normal(0,1) per dimension; only r dot beta is identified, not each beta_k. Both team and part parameters are learned only from training bonuses and frozen at posterior medians.

All arms score the same 2,330 games and 127,986 parts. 2 whole games were excluded for missing training entity coverage or saved predictions. See excluded_games.csv and fold split manifests. Zero-bonus games remain in the game denominator.

Saved DD and multidimensional compositional arms are reused without refitting. Training provenance is recorded in ../configuration.json. Optimization budgets and player-skill sources differ between model families.

## Overall

| Model | Part AUC | Part log loss | Part accuracy | Brier | ECE | Exact accuracy | PPB MAE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| team_irt_1d | 0.9037 | 0.3978 | 0.8224 | 0.1254 | 0.0289 | 0.5419 | 0.5799 |
| team_irt_3d | 0.9037 | 0.3939 | 0.8222 | 0.1248 | 0.0171 | 0.5422 | 0.4636 |
| dd_compositional | 0.8904 | 0.4183 | 0.8084 | 0.1337 | 0.0203 | 0.5117 | 1.9769 |
| dd_synergy | 0.8981 | 0.4049 | 0.8166 | 0.1286 | 0.0204 | 0.5294 | 0.9445 |
| multidim_compositional | 0.8881 | 0.4227 | 0.8083 | 0.1346 | 0.0194 | 0.5122 | 2.0447 |
| multidim_synergy | 0.8955 | 0.4113 | 0.8139 | 0.1310 | 0.0298 | 0.5244 | 1.1759 |

## Difficulty, bonus-only team PPG and game margins

Bonus margins condition on recorded bonus opportunities and use expected points (10 * sum probabilities). They exclude tossup points. Team PPB and PPG pool held-out predictions across folds before scoring. Tournament PPG summaries weight tournaments equally; margin MAE weights games equally.

| Model | Easy acc. | Medium acc. | Hard acc. | PPG MAE | PPG Spearman | Margin MAE |
| --- | --- | --- | --- | --- | --- | --- |
| team_irt_1d | 0.9115 | 0.7097 | 0.8462 | 4.8136 | 0.9916 | 22.8432 |
| team_irt_3d | 0.9118 | 0.7099 | 0.8449 | 3.6000 | 0.9954 | 22.7640 |
| dd_compositional | 0.9061 | 0.6805 | 0.8385 | 18.0595 | 0.8898 | 33.2099 |
| dd_synergy | 0.9074 | 0.7001 | 0.8423 | 8.3434 | 0.9374 | 26.5383 |
| multidim_compositional | 0.9076 | 0.6781 | 0.8392 | 18.8560 | 0.9585 | 32.1381 |
| multidim_synergy | 0.9003 | 0.6985 | 0.8430 | 11.0717 | 0.9702 | 26.6915 |

Difficulty accuracy includes correctly predicted misses; declared-label counts and observed conversion rates are in metrics_by_question_type.csv. Each difficulty gives one vote per observed part.

## Subject category

| Model | Category | Parts | Part accuracy | Part AUC | Part log loss |
| --- | --- | --- | --- | --- | --- |
| team_irt_1d | Current Events | 1224 | 0.8350 | 0.9085 | 0.3895 |
| team_irt_1d | Fine Arts | 14916 | 0.8079 | 0.8918 | 0.4174 |
| team_irt_1d | Geography | 2319 | 0.8124 | 0.8917 | 0.4100 |
| team_irt_1d | History | 20427 | 0.8199 | 0.9025 | 0.3970 |
| team_irt_1d | Literature | 20430 | 0.8324 | 0.9104 | 0.3835 |
| team_irt_1d | Mythology | 4707 | 0.8050 | 0.8847 | 0.4168 |
| team_irt_1d | Other Academic | 1245 | 0.8410 | 0.9197 | 0.3690 |
| team_irt_1d | Philosophy | 4785 | 0.8230 | 0.8992 | 0.4064 |
| team_irt_1d | Popular Culture | 1470 | 0.7878 | 0.8754 | 0.4246 |
| team_irt_1d | Religion | 5076 | 0.8276 | 0.9082 | 0.3906 |
| team_irt_1d | Science | 20349 | 0.8199 | 0.8999 | 0.4035 |
| team_irt_1d | Social Science | 4518 | 0.8411 | 0.9184 | 0.3669 |
| team_irt_1d | Unknown | 26520 | 0.8270 | 0.9068 | 0.3950 |
| team_irt_3d | Current Events | 1224 | 0.8325 | 0.9106 | 0.3820 |
| team_irt_3d | Fine Arts | 14916 | 0.8075 | 0.8906 | 0.4164 |
| team_irt_3d | Geography | 2319 | 0.8137 | 0.8931 | 0.4036 |
| team_irt_3d | History | 20427 | 0.8174 | 0.9028 | 0.3932 |
| team_irt_3d | Literature | 20430 | 0.8351 | 0.9131 | 0.3761 |
| team_irt_3d | Mythology | 4707 | 0.8033 | 0.8829 | 0.4171 |
| team_irt_3d | Other Academic | 1245 | 0.8402 | 0.9215 | 0.3601 |
| team_irt_3d | Philosophy | 4785 | 0.8211 | 0.8967 | 0.4075 |
| team_irt_3d | Popular Culture | 1470 | 0.7721 | 0.8702 | 0.4331 |
| team_irt_3d | Religion | 5076 | 0.8266 | 0.9069 | 0.3886 |
| team_irt_3d | Science | 20349 | 0.8186 | 0.9003 | 0.3993 |
| team_irt_3d | Social Science | 4518 | 0.8431 | 0.9173 | 0.3632 |
| team_irt_3d | Unknown | 26520 | 0.8283 | 0.9062 | 0.3899 |
| dd_compositional | Current Events | 1224 | 0.8325 | 0.9032 | 0.3954 |
| dd_compositional | Fine Arts | 14916 | 0.7958 | 0.8768 | 0.4419 |
| dd_compositional | Geography | 2319 | 0.8150 | 0.8862 | 0.4179 |
| dd_compositional | History | 20427 | 0.8098 | 0.8949 | 0.4085 |
| dd_compositional | Literature | 20430 | 0.8186 | 0.8964 | 0.4059 |
| dd_compositional | Mythology | 4707 | 0.7918 | 0.8750 | 0.4303 |
| dd_compositional | Other Academic | 1245 | 0.8386 | 0.9081 | 0.3885 |
| dd_compositional | Philosophy | 4785 | 0.7933 | 0.8762 | 0.4424 |
| dd_compositional | Popular Culture | 1470 | 0.7912 | 0.8792 | 0.4172 |
| dd_compositional | Religion | 5076 | 0.8158 | 0.8965 | 0.4091 |
| dd_compositional | Science | 20349 | 0.8120 | 0.8905 | 0.4183 |
| dd_compositional | Social Science | 4518 | 0.8214 | 0.9054 | 0.3850 |
| dd_compositional | Unknown | 26520 | 0.8035 | 0.8859 | 0.4257 |
| dd_synergy | Current Events | 1224 | 0.8276 | 0.9014 | 0.3991 |
| dd_synergy | Fine Arts | 14916 | 0.8023 | 0.8853 | 0.4283 |
| dd_synergy | Geography | 2319 | 0.8120 | 0.8903 | 0.4100 |
| dd_synergy | History | 20427 | 0.8170 | 0.9010 | 0.3977 |
| dd_synergy | Literature | 20430 | 0.8271 | 0.9055 | 0.3897 |
| dd_synergy | Mythology | 4707 | 0.8020 | 0.8801 | 0.4238 |
| dd_synergy | Other Academic | 1245 | 0.8361 | 0.9137 | 0.3760 |
| dd_synergy | Philosophy | 4785 | 0.8082 | 0.8896 | 0.4206 |
| dd_synergy | Popular Culture | 1470 | 0.7796 | 0.8694 | 0.4410 |
| dd_synergy | Religion | 5076 | 0.8227 | 0.9009 | 0.4018 |
| dd_synergy | Science | 20349 | 0.8170 | 0.8963 | 0.4091 |
| dd_synergy | Social Science | 4518 | 0.8336 | 0.9149 | 0.3671 |
| dd_synergy | Unknown | 26520 | 0.8171 | 0.8971 | 0.4059 |
| multidim_compositional | Current Events | 1224 | 0.8423 | 0.8973 | 0.4057 |
| multidim_compositional | Fine Arts | 14916 | 0.7971 | 0.8755 | 0.4441 |
| multidim_compositional | Geography | 2319 | 0.8064 | 0.8817 | 0.4252 |
| multidim_compositional | History | 20427 | 0.8038 | 0.8888 | 0.4210 |
| multidim_compositional | Literature | 20430 | 0.8193 | 0.8950 | 0.4091 |
| multidim_compositional | Mythology | 4707 | 0.7848 | 0.8660 | 0.4458 |
| multidim_compositional | Other Academic | 1245 | 0.8217 | 0.9028 | 0.3958 |
| multidim_compositional | Philosophy | 4785 | 0.7912 | 0.8716 | 0.4474 |
| multidim_compositional | Popular Culture | 1470 | 0.7823 | 0.8716 | 0.4354 |
| multidim_compositional | Religion | 5076 | 0.8075 | 0.8913 | 0.4175 |
| multidim_compositional | Science | 20349 | 0.8082 | 0.8883 | 0.4221 |
| multidim_compositional | Social Science | 4518 | 0.8302 | 0.9037 | 0.3896 |
| multidim_compositional | Unknown | 26520 | 0.8126 | 0.8872 | 0.4222 |
| multidim_synergy | Current Events | 1224 | 0.8276 | 0.8945 | 0.4138 |
| multidim_synergy | Fine Arts | 14916 | 0.8033 | 0.8840 | 0.4304 |
| multidim_synergy | Geography | 2319 | 0.8103 | 0.8897 | 0.4121 |
| multidim_synergy | History | 20427 | 0.8123 | 0.8956 | 0.4094 |
| multidim_synergy | Literature | 20430 | 0.8241 | 0.9032 | 0.3955 |
| multidim_synergy | Mythology | 4707 | 0.7878 | 0.8734 | 0.4347 |
| multidim_synergy | Other Academic | 1245 | 0.8217 | 0.9058 | 0.3934 |
| multidim_synergy | Philosophy | 4785 | 0.8077 | 0.8941 | 0.4131 |
| multidim_synergy | Popular Culture | 1470 | 0.7837 | 0.8634 | 0.4467 |
| multidim_synergy | Religion | 5076 | 0.8166 | 0.9000 | 0.4034 |
| multidim_synergy | Science | 20349 | 0.8135 | 0.8946 | 0.4119 |
| multidim_synergy | Social Science | 4518 | 0.8400 | 0.9123 | 0.3752 |
| multidim_synergy | Unknown | 26520 | 0.8155 | 0.8943 | 0.4155 |

Category x difficulty results, counts, conversion rates, AUC and calibration diagnostics are in metrics_by_question_type.csv. Missing/unmapped categories remain Unknown. Difficulty is joined from source labels, never inferred from part position.

These are reused development folds with familiar teams and questions, not an untouched test or a new-team/new-question transfer estimate. Team vectors ignore lineup changes; latent dimensions are not identified subject traits. One optimization seed was used. Loss traces and variational marginal quantiles are saved per fit; probabilities use parameter medians, not posterior-predictive integration.
