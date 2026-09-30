"""Interpret the DD-Bernstein multidimensional-difficulty bonus model.

The part logit is sum_k r_k * (ts_k(R) - d_k) + synergy(R), where ts_k is the
LSE-pooled roster skill on axis k. Only r and r . d enter the likelihood, so the
identified per-part quantities are the direction w = r / sum(r), discrimination
sum(r), and location loc = r . d / sum(r). This script reads saved fits only,
prints every number quoted in README.md, and writes the plotted tables to data/.

Run from the repository root:

    .venv/bin/python -B -m dd_model_interpretation.bonus.analyze
"""

import ast
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.special import expit, logsumexp
from scipy.stats import spearmanr
from sklearn.cluster import KMeans
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import RidgeCV
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score, silhouette_score
from sklearn.mixture import GaussianMixture
from sklearn.model_selection import GroupKFold, cross_val_predict
from sklearn.preprocessing import normalize

from dd_model_interpretation.shared.common import (
    AXES, BONUS_FIT, SEASON, TOSSUP_FIT, bonus_part_metadata, bonus_part_table, eta2, eta2_with_null,
)

REPLICATE = SEASON / "multidim-difficulty-synergy-3d"   # same fixed player skills, 3D synergy
FOLDS = Path("results/compirt/holdout/double-difficulty/compositional/"
             "multidim-difficulty-dot-additive-1d")
OUT = Path(__file__).parent / "data"
rng = np.random.default_rng(0)
pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 30)


def section(title):
    print(f"\n## {title}\n")


def save(frame, name):
    """Write a plotted table beside the code; figures.py reads these files."""
    frame.to_csv(OUT / f"{name}.csv", index=isinstance(frame.index, pd.MultiIndex) or frame.index.name is not None)


def ilr(r):
    """Isometric log-ratio coordinates of a positive 3-vector's direction."""
    log_r = np.log(r)
    return np.stack([(log_r[..., 0] - log_r[..., 1]) / np.sqrt(2),
                     (log_r[..., 0] + log_r[..., 1] - 2 * log_r[..., 2]) / np.sqrt(6)], -1)


def posterior_draws(fit, n_draws=100):
    """Mean-field AutoNormal draws: log r and d (site 'beta') are Normal per coordinate."""
    quantiles = pd.read_csv(fit / "posterior_quantiles.csv")
    draws = {}
    for site, log in (("r", True), ("beta", False)):
        rows = quantiles[quantiles.site == site]
        low, mid, high = (rows[c].to_numpy().reshape(-1, 3) for c in ("p025", "p500", "p975"))
        if log:
            low, mid, high = np.log(low), np.log(mid), np.log(high)
        x = mid + (high - low) / 3.92 * rng.standard_normal((n_draws,) + mid.shape)
        draws[site] = np.exp(x) if log else x
    return draws["r"], draws["beta"]


def cluster_features(r, d):
    rd = (r * d).sum(-1)[..., None]
    direction = ilr(r)
    return {"r.d": rd, "direction": direction,
            "joint": np.concatenate([direction, np.log(r.sum(-1))[..., None], rd], -1)}


def model_terms(parts, obs):
    section("Model terms: logit = sum(r) * (s - loc) + synergy, with s = sum_k w_k ts_k")
    summary = json.loads((BONUS_FIT / "summary.json").read_text())
    print(f"tau {summary['tau']:.3f}; synergy contribution per attempt: mean {summary['mean_synergy_contribution']:+.3f}, "
          f"median {summary['median_synergy_contribution']:+.3f}, negative {summary['negative_synergy_fraction']:.0%}")
    aggregate = (obs[["r1", "r2", "r3"]].to_numpy() * obs[["ts1", "ts2", "ts3"]].to_numpy()).sum(1)
    logit = aggregate - obs.rd + obs.synergy_contribution
    print(f"reconstruction check: max |sum_k r_k ts_k - saved aggregate| = {np.abs(aggregate - obs["aggregate"]).max():.1e}; "
          f"max |sigmoid(logit) - saved prediction| = {np.abs(expit(logit) - obs.predicted_correct).max():.1e}")

    section("What d says on its own: per-axis d_k is not identified")
    quantiles = pd.read_csv(BONUS_FIT / "posterior_quantiles.csv").query("site == 'beta'")
    d_sd = ((quantiles.p975 - quantiles.p025) / 3.92).to_numpy().reshape(-1, 3)
    print("mean posterior SD of d_k by axis (prior SD 1):", d_sd.mean(0).round(2).tolist())
    r, d = parts[["r1", "r2", "r3"]].to_numpy(), parts[["d1", "d2", "d3"]].to_numpy()
    cos2 = (r * d).sum(1) ** 2 / ((r ** 2).sum(1) * (d ** 2).sum(1))
    print(f"share of |d|^2 along r: median {np.median(cos2):.3f} (a random direction gives 1/3)")
    # With the orthogonal part at its prior mean, d is r.d spread along r: d_k = r.d * r_k / |r|^2.
    along = parts.rd.to_numpy()[:, None] * r / (r ** 2).sum(1, keepdims=True)
    print("correlation of d_k with r.d * r_k / |r|^2:",
          [round(float(np.corrcoef(d[:, k], along[:, k])[0, 1]), 3) for k in range(3)])
    print("Spearman of d_k with loc:", [round(float(spearmanr(d[:, k], parts["loc"])[0]), 2) for k in range(3)])

    section("Location vs team skill (loc and s share the pooled team-skill scale)")
    obs = obs.assign(s=(obs[AXES].to_numpy() * obs[["ts1", "ts2", "ts3"]].to_numpy()).sum(1))
    obs["above"] = obs.s > obs["loc"]
    table = parts.groupby("label").agg(loc_median=("loc", "median"), loc_sd=("loc", "std"),
                                       rsum_median=("rsum", "median"))
    table = table.join(obs.groupby("label").agg(
        s_median=("s", "median"), s_sd=("s", "std"), team_above_loc=("above", "mean"),
        synergy_mean=("synergy_contribution", "mean"), predicted=("predicted_correct", "mean"),
        observed=("correct", "mean"))).loc[["easy", "medium", "hard"]]
    print(table.round(3).to_string())
    save(table, "location_vs_skill")
    tiers = {"fall": "Fall 2024", "2024-11-16": "Winter 2024", "2025-02-01": "Regionals 2025", "04192025": "Nationals 2025"}
    by_set = (parts.assign(tier=parts.set.str.split("::").str[1].map(tiers))
              .pivot_table(index="tier", columns="label", values="loc", aggfunc="median")[["easy", "medium", "hard"]])
    field = (obs.assign(tier=obs.bonus_part_id.str.split("::").str[1].map(tiers))
             .groupby("tier").s.median().rename("team_s_median"))
    by_set = by_set.join(field).loc[list(tiers.values())]
    print("\nmedian loc by question set and label, with the median team skill s of the teams that heard the set:")
    print(by_set.round(2).to_string())
    save(by_set, "location_by_set")
    # Cover the central 99% of both parts and attempts, so neither set of tails is clipped.
    low = min(np.quantile(parts["loc"], 0.005), np.quantile(obs.s, 0.005))
    high = max(np.quantile(parts["loc"], 0.995), np.quantile(obs.s, 0.995))
    bins = np.linspace(low, high, 61)
    hist = pd.DataFrame({"left": bins[:-1], "right": bins[1:]})
    for label in ("easy", "medium", "hard"):
        hist[f"parts_{label}"] = np.histogram(parts["loc"][parts.label == label], bins)[0]
    hist["attempts"] = np.histogram(obs.s, bins)[0]
    save(hist, "location_skill_hist")


def team_axes(obs):
    section("Team pooled skill axes vs subject-specific conversion (teams with >= 60 parts)")
    teams = obs.groupby("team_id")
    table = teams[["ts1", "ts2", "ts3"]].mean().assign(all=teams.correct.mean(), n=teams.size())
    for subject in ["Science", "Literature", "History", "Fine Arts"]:
        table[subject] = obs[obs.category == subject].groupby("team_id").correct.mean() - table["all"]
    table = table[table.n >= 60]
    rows = [{"conversion minus overall": s,
             **{k: round(spearmanr(table[k], table[s], nan_policy="omit")[0], 2) for k in ("ts1", "ts2", "ts3")}}
            for s in ["Science", "Literature", "History", "Fine Arts"]]
    print(f"teams: {len(table)}")
    print(pd.DataFrame(rows).to_string(index=False))
    print("\nSD of LSE-pooled team skill per axis over observations:",
          obs[["ts1", "ts2", "ts3"]].std().round(3).to_list())


def variance_shares(parts):
    section("Variance explained by metadata (eta^2, permutation-null mean in parentheses)")
    rows = []
    for feature in AXES + ["rsum", "rd"]:
        rows.append({"feature": feature, **{g: eta2_with_null(parts[feature], parts[g], rng)
                                            for g in ["label", "category", "subcategory", "set", "bonus_id"]}})
    print(pd.DataFrame(rows).to_string(index=False))
    print("\nMeans by declared difficulty:")
    print(parts.groupby("label")[AXES + ["rsum", "rd", "conv"]].mean().round(3))
    print("\nMeans by subcategory (>= 30 parts), sorted by w1 - w3:")
    by_sub = parts.groupby("subcategory")[AXES + ["rsum", "conv"]].mean().assign(n=parts.groupby("subcategory").size())
    by_sub = by_sub[by_sub.n >= 30]
    save(by_sub, "subcategory_directions")
    print(by_sub.assign(w1_minus_w3=by_sub.w1 - by_sub.w3).sort_values("w1_minus_w3").round(3).to_string())
    print("\nSpearman(r.d, observed conversion):", round(spearmanr(parts.rd, parts.conv)[0], 3))
    print("Spearman(r.d, loc):", round(spearmanr(parts.rd, parts["loc"])[0], 3))
    print("mean 95% posterior interval width of r_k:", round(parts.r_width.mean(), 2))


def pair_similarity(parts):
    section("Direction similarity by pair type (normalized cross-product of centered clr log r)")
    log_r = np.log(parts[["r1", "r2", "r3"]].to_numpy())
    clr = log_r - log_r.mean(1, keepdims=True)
    clr -= clr.mean(0)
    i, j = np.triu_indices(len(parts), 1)
    same = {c: parts[c].to_numpy()[i] == parts[c].to_numpy()[j]
            for c in ["bonus_id", "packet", "set", "category", "subcategory"]}
    pairs = {
        "same bonus": same["bonus_id"],
        "same packet, other bonus, same category": same["packet"] & ~same["bonus_id"] & same["category"],
        "same packet, other category": same["packet"] & ~same["category"],
        "other set, same subcategory": ~same["set"] & same["subcategory"],
        "other set, same category": ~same["set"] & same["category"],
        "other set, other category": ~same["set"] & ~same["category"],
    }
    scale = (clr ** 2).sum(1).mean()
    rows = []
    for name, mask in pairs.items():
        similarity = (clr[i[mask]] * clr[j[mask]]).sum(1).mean() / scale
        print(f"{name:42s} pairs={mask.sum():>9,d}  similarity={similarity:+.3f}")
        rows.append({"pair_type": name, "pairs": int(mask.sum()), "similarity": similarity})
    save(pd.DataFrame(rows), "pair_similarity")


def cluster_parts(parts, r, d):
    section("Parameter-space clustering")
    features = cluster_features(r, d)
    draw_features = cluster_features(*posterior_draws(BONUS_FIT))
    replicate = pd.read_csv(REPLICATE / "bonus_parts.csv")
    assert (replicate.bonus_part_id == parts.bonus_part_id).all()
    replicate_features = cluster_features(replicate[["r_1", "r_2", "r_3"]].to_numpy(),
                                          replicate[["beta_1", "beta_2", "beta_3"]].to_numpy())
    validity = []
    for name, x in features.items():
        mean, sd = x.mean(0), x.std(0)
        z = (x - mean) / sd
        bic = {k: round(GaussianMixture(k, n_init=5, random_state=0).fit(z).bic(z)) for k in range(1, 9)}
        print(f"{name} ({x.shape[1]}D) GMM BIC by k: {bic}")
        for k in (3, 4):
            kmeans = KMeans(k, n_init=20, random_state=0).fit(z)
            labels = kmeans.labels_
            kept = np.mean([kmeans.predict((draw - mean) / sd) == labels for draw in draw_features[name]], 0)
            y = replicate_features[name]
            replicate_labels = KMeans(k, n_init=20, random_state=0).fit_predict((y - y.mean(0)) / y.std(0))
            gaussian = rng.multivariate_normal(np.zeros(z.shape[1]), np.atleast_2d(np.cov(z.T)), len(z))
            null_silhouette = silhouette_score(gaussian, KMeans(k, n_init=10, random_state=0).fit_predict(gaussian))
            print(f"  k={k}: silhouette {silhouette_score(z, labels):.3f} (single-Gaussian null {null_silhouette:.3f}); "
                  f"posterior-draw agreement {kept.mean():.2f}, parts kept in >=80% of draws {np.mean(kept >= .8):.0%}; "
                  f"ARI vs 3D-synergy fit {adjusted_rand_score(labels, replicate_labels):.2f}; "
                  f"NMI label {normalized_mutual_info_score(parts.label, labels):.3f}, "
                  f"category {normalized_mutual_info_score(parts.category, labels):.3f}")
            parts[f"{name}_k{k}"] = labels
            parts[f"{name}_k{k}_draw_agreement"] = kept
            validity.append({"features": name, "k": k, "silhouette": silhouette_score(z, labels),
                             "null_silhouette": null_silhouette, "draw_agreement": kept.mean(),
                             "kept_80": np.mean(kept >= .8),
                             "ari_replicate": adjusted_rand_score(labels, replicate_labels)})
    save(pd.DataFrame(validity), "cluster_validity")
    for column in ["r.d_k3", "direction_k4", "joint_k4"]:
        print(f"\n{column} profiles:")
        groups = parts.groupby(column)
        print(groups[AXES + ["rsum", "rd", "loc", "conv"]].mean().round(2)
              .join(pd.crosstab(parts[column], parts.label, normalize="index").round(2))
              .assign(size=groups.size()).to_string())
        counts = pd.crosstab(parts[column], parts.category)
        lift = (counts / counts.sum(axis=0)) / (counts.sum(axis=1).to_numpy()[:, None] / counts.to_numpy().sum())
        print("category lift (share of the category in the cluster / cluster share):")
        print(lift.round(2).to_string())


def cluster_bonuses(parts):
    section("Bonus-level profiles: r.d of the easy, medium, and hard parts")
    bonuses = parts.pivot_table(index="bonus_id", columns="label", values="rd")[["easy", "medium", "hard"]]
    z = ((bonuses - bonuses.mean()) / bonuses.std()).to_numpy()
    print("GMM BIC by k:", {k: round(GaussianMixture(k, n_init=5, random_state=0).fit(z).bic(z)) for k in range(1, 7)})
    print("within-bonus correlation of part difficulties:")
    print(bonuses.corr().round(2))
    print(f"strictly easy < medium < hard: {((bonuses.easy < bonuses.medium) & (bonuses.medium < bonuses.hard)).mean():.3f}")
    save(bonuses, "bonus_profiles")
    show = ["bonus_part_id", "category", "answer", "rd", "conv", "n"]
    print("\nhardest declared-easy parts:")
    print(parts[parts.label == "easy"].nlargest(6, "rd")[show].round(2).to_string(index=False))
    print("easiest declared-hard parts:")
    print(parts[parts.label == "hard"].nsmallest(6, "rd")[show].round(2).to_string(index=False))


def cluster_text(parts):
    section("Text-topic clustering (TF-IDF + 100-component LSA of lead-in, part text, and answer)")
    tfidf = TfidfVectorizer(min_df=3, max_df=0.3, stop_words="english", sublinear_tf=True, ngram_range=(1, 2))
    x = normalize(TruncatedSVD(100, random_state=0).fit_transform(tfidf.fit_transform(parts.document)))
    log_r = np.log(parts[["r1", "r2", "r3"]].to_numpy())
    parts["clr1"], parts["clr3"] = (log_r - log_r.mean(1, keepdims=True))[:, [0, 2]].T
    topics = KMeans(26, n_init=10, random_state=0).fit_predict(x)
    parts["topic"] = topics
    for feature in ["clr1", "clr3", "rd"]:
        within = parts[feature] - parts.groupby("subcategory")[feature].transform("mean")
        print(f"{feature}: 26 topics eta2 {eta2_with_null(parts[feature], topics, rng, 100)}; "
              f"after subcategory means {eta2_with_null(within, topics, rng, 100)}")
    dummies = pd.get_dummies(parts.subcategory).to_numpy(float)
    for feature in ["clr1", "clr3", "rd"]:
        y = parts[feature]
        scores = {}
        for name, design in [("text", x), ("subcategory", dummies), ("both", np.hstack([x, dummies]))]:
            p = cross_val_predict(RidgeCV(alphas=np.logspace(-2, 3, 12)), design, y,
                                  groups=parts.bonus_id, cv=GroupKFold(5))
            scores[name] = round(float(1 - ((y - p) ** 2).sum() / ((y - y.mean()) ** 2).sum()), 3)
        print(f"held-out R2 (bonus-grouped 5-fold) for {feature}: {scores}")
    words = TfidfVectorizer(min_df=3, max_df=0.3, stop_words="english", sublinear_tf=True)
    matrix = words.fit_transform(parts.document)
    vocabulary = np.array(words.get_feature_names_out())
    groups = parts.groupby("topic")
    profile = groups[AXES].mean().assign(
        n=groups.size(), hard=groups.label.apply(lambda s: (s == "hard").mean()),
        top_category=groups.category.agg(lambda s: s.value_counts().index[0]))
    profile["terms"] = [", ".join(vocabulary[np.asarray(matrix[(topics == t)].mean(0)).ravel().argsort()[::-1][:6]])
                        for t in profile.index]
    print(profile.sort_values("w1").round(2).to_string())
    save(profile, "topics")


def residuals(obs):
    section("Residual structure (observed - predicted), split-half by bonus")
    obs = obs.assign(residual=obs.correct - obs.predicted_correct)
    bonuses = obs.bonus_id.unique()
    obs["half"] = obs.bonus_id.map(dict(zip(bonuses, np.random.default_rng(1).integers(0, 2, len(bonuses)))))
    overall = obs.groupby(["team_id", "half"]).residual.mean().unstack().dropna()
    print(f"team overall residual, split-half r = {np.corrcoef(overall[0], overall[1])[0, 1]:.3f} ({len(overall)} teams)")
    totals = obs.groupby(["team_id", "half"]).residual.agg(total="sum", count="size").reset_index()
    reliability = []
    for group in ["category", "label"]:
        cells = obs.groupby(["team_id", "half", group]).residual.agg(["sum", "size"]).reset_index()
        cells = cells.merge(totals, on=["team_id", "half"])
        cells = cells[(cells["size"] >= 8) & (cells["count"] - cells["size"] >= 8)]
        # In-group mean residual minus the same team's out-of-group mean residual.
        cells["deviation"] = cells["sum"] / cells["size"] - (cells.total - cells["sum"]) / (cells["count"] - cells["size"])
        wide = cells.pivot_table(index=["team_id", group], columns="half", values="deviation").dropna()
        result = {level: (np.corrcoef(sub[0], sub[1])[0, 1], len(sub))
                  for level, sub in wide.groupby(level=1) if len(sub) >= 40}
        print(f"team {group}-specific deviation, split-half r:",
              {level: f"{r:+.2f} (n={n})" for level, (r, n) in result.items()})
        reliability += [{"grouping": group, "level": level, "split_half_r": r, "teams": n}
                        for level, (r, n) in result.items()]
    save(pd.DataFrame(reliability), "residual_reliability")
    teams = obs.groupby("team_id").agg(conv=("correct", "mean"), n=("residual", "size"))
    for label in ["easy", "medium", "hard"]:
        teams[label] = obs[obs.label == label].groupby("team_id").residual.mean()
    teams = teams[teams.n >= 60]
    print("Spearman(team conversion, mean residual by label):",
          {label: round(float(spearmanr(teams.conv, teams[label])[0]), 2) for label in ["easy", "medium", "hard"]})
    obs["bin"] = pd.cut(obs.predicted_correct, [0, .1, .3, .5, .7, .9, 1])
    calibration = (obs.groupby(["label", "bin"], observed=True)
                   .agg(predicted=("predicted_correct", "mean"), observed=("correct", "mean"), n=("residual", "size")))
    print(calibration.round(3).to_string())
    save(calibration, "calibration")


def folds(meta, season_parts):
    section("Replication in the five-fold calendar-2024 fits (each fold has its own player skills)")
    season = season_parts.groupby("subcategory")[AXES].mean()
    rows = [{"fit": "season", "label": label, "w2": value.w2, "rsum": value.rsum}
            for label, value in season_parts.groupby("label")[["w2", "rsum"]].mean().iterrows()]
    for fold in range(5):
        parts, _, _ = bonus_part_table(FOLDS / f"fold_{fold}/train/synergy", meta)
        by_sub = parts.groupby("subcategory")[AXES].mean()
        common = by_sub.index.intersection(season.index)
        diagonal = [round(float(spearmanr(by_sub.loc[common, a], season.loc[common, a])[0]), 2) for a in AXES]
        print(f"fold {fold}: category eta2 {[round(float(eta2(parts[a], parts.category)), 3) for a in AXES]}; "
              f"subcategory profile Spearman with season (same axis) {diagonal}; "
              f"w2 easy/medium/hard {parts.groupby('label').w2.mean()[['easy', 'medium', 'hard']].round(3).to_list()}; "
              f"rsum {parts.groupby('label').rsum.mean()[['easy', 'medium', 'hard']].round(2).to_list()}")
        rows += [{"fit": f"fold {fold}", "label": label, "w2": value.w2, "rsum": value.rsum}
                 for label, value in parts.groupby("label")[["w2", "rsum"]].mean().iterrows()]
    save(pd.DataFrame(rows), "folds")


def main():
    OUT.mkdir(exist_ok=True)
    meta = bonus_part_metadata()
    parts, r, d = bonus_part_table(BONUS_FIT, meta)
    quantiles = pd.read_csv(BONUS_FIT / "posterior_quantiles.csv").query("site == 'r'")
    parts["r_width"] = (quantiles.p975 - quantiles.p025).to_numpy().reshape(-1, 3).mean(1)
    obs = pd.read_csv(BONUS_FIT / "bonus_part_predictions.csv",
                      usecols=["team_id", "player_ids", "bonus_id", "bonus_part_id", "correct", "predicted_correct",
                               "aggregate", "synergy_contribution"])
    parts = parts.merge(obs.groupby("bonus_part_id").agg(n=("correct", "size"), conv=("correct", "mean")),
                        on="bonus_part_id", how="left")
    obs = obs.merge(parts[["bonus_part_id", "category", "label", "r1", "r2", "r3", "rd", "loc"] + AXES],
                    on="bonus_part_id")
    # Team skill ts_k: the fitted LSE pool of the roster's fixed player skills on each axis.
    tau = float((BONUS_FIT / "tau.txt").read_text())
    theta = pd.read_csv(TOSSUP_FIT / "players.csv").set_index("player_id")[["theta_1", "theta_2", "theta_3"]]
    pooled = {roster: tau * logsumexp(theta.loc[ast.literal_eval(roster)].to_numpy() / tau, axis=0)
              for roster in obs.player_ids.unique()}
    obs[["ts1", "ts2", "ts3"]] = np.stack(obs.player_ids.map(pooled).to_numpy())

    print(f"# Multidimensional-difficulty bonus model: {BONUS_FIT}")
    print(f"parts {len(parts)}, responses {len(obs)}")
    model_terms(parts, obs)
    team_axes(obs)
    variance_shares(parts)
    pair_similarity(parts)
    cluster_parts(parts, r, d)
    cluster_bonuses(parts)
    cluster_text(parts)
    residuals(obs)
    folds(meta, parts)
    parts.drop(columns=["document"]).to_csv(OUT / "parts.csv", index=False)


if __name__ == "__main__":
    main()
