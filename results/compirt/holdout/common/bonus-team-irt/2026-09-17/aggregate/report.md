# Bonus-only team IRT

3,000 AutoNormal SVI steps, learning rate 0.01, fit seed 42; 5 year_2024 whole-game folds, split seed 42.

Team parameters use tournament-specific team IDs. P(correct) = sigmoid(theta_team dot alpha_part - beta_part), with independent theta ~ Normal(0,1), alpha ~ Gamma(2,2) (shape/rate), beta ~ Normal(0,1). Both team and part parameters are learned only from training bonuses and frozen at posterior medians.

All arms score the same 2,330 games and 127,986 parts. 2 whole games were excluded for missing training entity coverage or saved predictions. See excluded_games.csv and fold split manifests. Zero-bonus games remain in the game denominator.

Saved DD and multidimensional compositional arms are reused without refitting. Training summaries and prediction hashes are recorded in ../configuration.json; their optimization budgets and player-skill sources differ from this bonus-only study.

## Overall

| Model | Part AUC | Part log loss | Part accuracy | Brier | ECE | Exact accuracy | PPB MAE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| team_irt_1d | 0.9037 | 0.3978 | 0.8224 | 0.1254 | 0.0289 | 0.5419 | 0.5799 |
| team_irt_3d | 0.9039 | 0.3953 | 0.8231 | 0.1249 | 0.0231 | 0.5430 | 0.5112 |
| dd_compositional | 0.8903 | 0.4186 | 0.8079 | 0.1338 | 0.0208 | 0.5105 | 1.9888 |
| dd_synergy | 0.8982 | 0.4045 | 0.8171 | 0.1284 | 0.0184 | 0.5305 | 0.9039 |
| multidim_compositional | 0.8881 | 0.4227 | 0.8083 | 0.1346 | 0.0194 | 0.5122 | 2.0447 |
| multidim_synergy | 0.8955 | 0.4113 | 0.8139 | 0.1310 | 0.0298 | 0.5244 | 1.1759 |

## Difficulty, bonus-only team PPG and game margins

Bonus margins condition on recorded bonus opportunities and use expected points (10 * sum probabilities). They exclude tossup points. Team PPB and PPG pool held-out predictions across folds before scoring. Tournament PPG summaries weight tournaments equally; margin MAE weights games equally.

| Model | Easy acc. | Medium acc. | Hard acc. | PPG MAE | PPG Spearman | Margin MAE |
| --- | --- | --- | --- | --- | --- | --- |
| team_irt_1d | 0.9115 | 0.7097 | 0.8462 | 4.8136 | 0.9916 | 22.8432 |
| team_irt_3d | 0.9115 | 0.7108 | 0.8470 | 3.9942 | 0.9934 | 22.7917 |
| dd_compositional | 0.9062 | 0.6794 | 0.8382 | 18.1061 | 0.8855 | 33.2205 |
| dd_synergy | 0.9074 | 0.7007 | 0.8433 | 8.1208 | 0.9402 | 26.5163 |
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
| team_irt_3d | Current Events | 1224 | 0.8301 | 0.9115 | 0.3830 |
| team_irt_3d | Fine Arts | 14916 | 0.8075 | 0.8906 | 0.4179 |
| team_irt_3d | Geography | 2319 | 0.8159 | 0.8916 | 0.4080 |
| team_irt_3d | History | 20427 | 0.8195 | 0.9025 | 0.3951 |
| team_irt_3d | Literature | 20430 | 0.8387 | 0.9143 | 0.3742 |
| team_irt_3d | Mythology | 4707 | 0.8014 | 0.8810 | 0.4203 |
| team_irt_3d | Other Academic | 1245 | 0.8450 | 0.9200 | 0.3680 |
| team_irt_3d | Philosophy | 4785 | 0.8188 | 0.8962 | 0.4101 |
| team_irt_3d | Popular Culture | 1470 | 0.7844 | 0.8688 | 0.4333 |
| team_irt_3d | Religion | 5076 | 0.8245 | 0.9060 | 0.3933 |
| team_irt_3d | Science | 20349 | 0.8211 | 0.9013 | 0.3994 |
| team_irt_3d | Social Science | 4518 | 0.8424 | 0.9177 | 0.3651 |
| team_irt_3d | Unknown | 26520 | 0.8269 | 0.9065 | 0.3931 |
| dd_compositional | Current Events | 1224 | 0.8292 | 0.9026 | 0.3963 |
| dd_compositional | Fine Arts | 14916 | 0.7954 | 0.8765 | 0.4422 |
| dd_compositional | Geography | 2319 | 0.8133 | 0.8867 | 0.4173 |
| dd_compositional | History | 20427 | 0.8092 | 0.8948 | 0.4088 |
| dd_compositional | Literature | 20430 | 0.8179 | 0.8965 | 0.4060 |
| dd_compositional | Mythology | 4707 | 0.7933 | 0.8752 | 0.4301 |
| dd_compositional | Other Academic | 1245 | 0.8353 | 0.9073 | 0.3898 |
| dd_compositional | Philosophy | 4785 | 0.7935 | 0.8766 | 0.4419 |
| dd_compositional | Popular Culture | 1470 | 0.7905 | 0.8786 | 0.4181 |
| dd_compositional | Religion | 5076 | 0.8182 | 0.8966 | 0.4089 |
| dd_compositional | Science | 20349 | 0.8103 | 0.8903 | 0.4187 |
| dd_compositional | Social Science | 4518 | 0.8209 | 0.9054 | 0.3853 |
| dd_compositional | Unknown | 26520 | 0.8037 | 0.8855 | 0.4262 |
| dd_synergy | Current Events | 1224 | 0.8301 | 0.9026 | 0.3980 |
| dd_synergy | Fine Arts | 14916 | 0.8020 | 0.8849 | 0.4286 |
| dd_synergy | Geography | 2319 | 0.8137 | 0.8909 | 0.4085 |
| dd_synergy | History | 20427 | 0.8177 | 0.9013 | 0.3967 |
| dd_synergy | Literature | 20430 | 0.8278 | 0.9055 | 0.3899 |
| dd_synergy | Mythology | 4707 | 0.8026 | 0.8804 | 0.4232 |
| dd_synergy | Other Academic | 1245 | 0.8337 | 0.9134 | 0.3764 |
| dd_synergy | Philosophy | 4785 | 0.8096 | 0.8902 | 0.4195 |
| dd_synergy | Popular Culture | 1470 | 0.7789 | 0.8699 | 0.4405 |
| dd_synergy | Religion | 5076 | 0.8209 | 0.9010 | 0.4011 |
| dd_synergy | Science | 20349 | 0.8174 | 0.8965 | 0.4085 |
| dd_synergy | Social Science | 4518 | 0.8342 | 0.9153 | 0.3666 |
| dd_synergy | Unknown | 26520 | 0.8181 | 0.8972 | 0.4054 |
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
