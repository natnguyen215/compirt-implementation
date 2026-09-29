"""Which Team IRT 3D quantities are identified, and what do the axes track?

Reads saved fits and refits only; nothing is trained. Writes ../output.txt.
Run from the repository root after refit.py:

    .venv/bin/python -B results/compirt/holdout/common/bonus-team-irt/team-skills-1d-gamma-alpha-3d-simplex-relevance-5fold/identifiability/code/analyze.py
"""

import itertools
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[8]))

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

from analysis.bonus_team_irt.model import observations, part_logits
from compirt_data import load_hf_tables
from compirt_eval.common.categories import top_level_category

STUDY = Path(__file__).resolve().parents[1]
RUN = STUDY.parent
DD = Path("results/compirt/holdout/double-difficulty/compositional/multidim-difficulty-dot-additive-3d")
FOLDS = range(5)
PERMS = list(itertools.permutations(range(3)))
RNG = np.random.default_rng(0)


def question_set(ids):
    return pd.Series(ids).str.split("::p").str[0].to_numpy()


def load_fit(fold):
    path = RUN / f"fold_{fold}/team_irt_3d"
    with np.load(path / "parameters.npz") as saved:
        parameters = {key: value.astype(float) for key, value in saved.items()}
    ids = json.loads((path / "ids.json").read_text())
    return parameters, pd.Index(ids["team_ids"]), pd.Index(ids["part_ids"])


def spearman_axes(a, b):
    return np.mean([spearmanr(a[:, k], b[:, k])[0] for k in range(a.shape[1])])


def align_by_set(reference, other, sets):
    """Best axis permutation of 'other' per question set, matching loading shares."""
    aligned, chosen = other.copy(), {}
    for value in np.unique(sets):
        rows = sets == value
        best = max(PERMS, key=lambda p: spearman_axes(reference[rows], other[rows][:, p]))
        aligned[rows] = other[rows][:, best]
        chosen[value] = best
    return aligned, chosen


def eta2(values, groups):
    frame = pd.DataFrame({"x": values, "g": groups})
    within = frame.groupby("g").x.var(ddof=0).mul(frame.groupby("g").size()).sum()
    return 1 - within / (frame.x.var(ddof=0) * len(frame))


def eta2_within_set(share, groups, sets, shuffle=False):
    """Mean over axes and sets of eta^2; 'shuffle' permutes labels within set."""
    values = []
    for value in np.unique(sets):
        rows = sets == value
        labels = RNG.permutation(groups[rows]) if shuffle else groups[rows]
        values += [eta2(share[rows, k], labels) for k in range(3)]
    return float(np.mean(values))


def log_odds_words(texts, selected, top=10, prior_mass=500.0):
    """Monroe et al. log-odds with an informative Dirichlet prior (z-scores)."""
    tokens = [set(w for w in re.findall(r"[a-z]{3,}", t.lower()) if w not in ENGLISH_STOP_WORDS) for t in texts]
    inside = pd.Series([w for s, keep in zip(tokens, selected) if keep for w in s]).value_counts()
    outside = pd.Series([w for s, keep in zip(tokens, selected) if not keep for w in s]).value_counts()
    words = inside.index.union(outside.index)
    inside, outside = inside.reindex(words, fill_value=0), outside.reindex(words, fill_value=0)
    total = inside + outside
    alpha = prior_mass * total / total.sum()
    n_in, n_out, a0 = inside.sum(), outside.sum(), alpha.sum()
    delta = (np.log((inside + alpha) / (n_in + a0 - inside - alpha))
             - np.log((outside + alpha) / (n_out + a0 - outside - alpha)))
    z = delta / np.sqrt(1 / (inside + alpha) + 1 / (outside + alpha))
    return z[inside >= 5].sort_values(ascending=False).head(top)


def main():
    tables = load_hf_tables(split="year_2024")
    frame = observations(tables)
    bonuses = tables["bonuses"].set_index("bonus_id")
    part_meta = {}
    for bonus_id, row in bonuses.iterrows():
        for index, part in enumerate(row.parts, 1):
            part_meta[f"{bonus_id}::part-{index}"] = {
                "category": top_level_category(row.category), "subcategory": row.subcategory or "Unknown",
                "difficulty": part["difficulty"], "position": index, "answer": part["answer"],
                "text": f"{row.leadin} {part['text']} {part['answer']}"}
    fits = {fold: load_fit(fold) for fold in FOLDS}
    parameters, team_ids, part_ids = fits[0]
    theta, r, beta = parameters["theta"], parameters["r"], parameters["beta"]
    meta = pd.DataFrame([part_meta[p] for p in part_ids], index=part_ids)
    part_set, team_set = question_set(part_ids), None
    effective = (r * beta).sum(1)
    out = []

    # Fold-0 training observations, needed for exact likelihood checks.
    split = json.loads((RUN / "fold_0/split.json").read_text())
    train = frame[frame.game_id.isin(split["train_game_ids"])]
    teams, parts = team_ids.get_indexer(train.team_id), part_ids.get_indexer(train.bonus_part_id)
    team_set = pd.Series(part_set[parts]).groupby(teams).first().reindex(range(len(team_ids))).to_numpy()
    base = part_logits(parameters, teams, parts)
    y = train.correct.to_numpy()
    loglik = lambda z: float(np.sum(y * z - np.logaddexp(0, z)))

    out.append("## 1. Exact likelihood symmetries (fold 0 training responses)")
    unit = np.cross(r, RNG.normal(size=r.shape))  # orthogonal to r_b
    unit /= np.linalg.norm(unit, axis=1, keepdims=True)
    moved = {"beta + 3 * (unit vector orthogonal to r_b)": {**parameters, "beta": beta + 3 * unit}}
    rows = part_set == "2024-acf-nationals::2024-04-21"
    team_rows = team_set == "2024-acf-nationals::2024-04-21"
    shift = np.array([1.0, -2.0, 0.5])
    moved["theta_k + c_k and beta_k + c_k for the Nationals set only, c = (1, -2, 0.5)"] = {
        **parameters, "theta": theta + shift * team_rows[:, None], "beta": beta + shift * rows[:, None]}
    permuted = {key: value.copy() for key, value in parameters.items()}
    for key in ("r", "beta"):
        permuted[key][rows] = permuted[key][rows][:, [2, 0, 1]]
    permuted["theta"][team_rows] = permuted["theta"][team_rows][:, [2, 0, 1]]
    moved["relabel axes (3,1,2) for the Nationals set only"] = permuted
    for name, values in moved.items():
        changed = part_logits(values, teams, parts)
        out.append(f"- {name}: max |change in logit| = {np.abs(changed - base).max():.2e}, "
                   f"change in log-likelihood = {loglik(changed) - loglik(base):+.2e}")
    minimum_norm = effective[:, None] * r / (r * r).sum(1, keepdims=True)
    out.append(f"- beta_b is the prior's minimum-norm solution (r_b dot beta_b) r_b / |r_b|^2: "
               f"R^2 = {1 - ((beta - minimum_norm) ** 2).sum() / ((beta - beta.mean(0)) ** 2).sum():.4f}; "
               f"median |cos(beta_b, r_b)| = {np.median(np.abs((beta * r).sum(1)) / np.linalg.norm(beta, axis=1) / np.linalg.norm(r, axis=1)):.4f}")
    quantiles = np.load(RUN / "fold_0/team_irt_3d/posterior_quantiles.npz")
    width = quantiles["r__p975"] - quantiles["r__p025"]
    out.append(f"- Data informativeness about r: median 95% interval width {np.median(width):.3f} "
               f"(Dirichlet(1) prior: 0.829); SD of r medians per axis {np.round(r.std(0), 3).tolist()}; "
               f"parts with max share > 0.5: {np.mean(r.max(1) > 0.5):.1%}")
    out.append(f"- Team skill axes: correlation matrix {np.round(np.corrcoef(theta.T)[np.triu_indices(3, 1)], 3).tolist()} "
               f"(pairs 12, 13, 23); singular-value variance shares "
               f"{np.round(np.linalg.svd(theta - theta.mean(0), compute_uv=False) ** 2 / ((theta - theta.mean(0)) ** 2).sum(), 3).tolist()}")

    out.append("\n## 2. Same fold-0 data, different seed or difficulty prior")
    probability = 1 / (1 + np.exp(-base))
    for name in ("seed_43", "seed_44", "shifted_beta_prior_seed_42"):
        with np.load(STUDY / f"refits/{name}.npz") as saved:
            other = {key: value.astype(float) for key, value in saved.items()}
        other_probability = 1 / (1 + np.exp(-part_logits(other, teams, parts)))
        other_effective = (other["r"] * other["beta"]).sum(1)
        global_perm = max(PERMS, key=lambda p: spearman_axes(r, other["r"][:, p]))
        aligned_r, chosen = align_by_set(r, other["r"], part_set)
        aligned_beta = other["beta"].copy()
        for value, perm in chosen.items():
            aligned_beta[part_set == value] = other["beta"][part_set == value][:, perm]
        null = lambda b, w: b - ((b * w).sum(1, keepdims=True) / (w * w).sum(1, keepdims=True)) * w
        line = (f"- {name}: training probabilities max |diff| {np.abs(other_probability - probability).max():.3f}, "
                f"corr {np.corrcoef(other_probability, probability)[0, 1]:.4f}; effective difficulty Spearman "
                f"{spearmanr(effective, other_effective)[0]:.4f}; per-axis r Spearman: global best perm "
                f"{spearman_axes(r, other['r'][:, global_perm]):.3f}, per-set best perm {spearman_axes(r, aligned_r):.3f} "
                f"(perms {sorted(set(chosen.values()))}); per-axis beta Spearman {spearman_axes(beta, aligned_beta):.3f}; "
                f"null-space beta Spearman {spearman_axes(null(beta, r), null(aligned_beta, aligned_r)):.3f}")
        if name.startswith("shifted"):
            line += (f"; mean beta per axis {np.round(beta.mean(0), 3).tolist()} -> {np.round(other['beta'].mean(0), 3).tolist()} "
                     f"under prior mean (1, 0, -1); mean effective difficulty {effective.mean():.3f} -> {other_effective.mean():.3f}")
        out.append(line)

    out.append("\n## 3. Cross-fold stability (10 fold pairs; each part is in every training fold)")
    rows = []
    for f, g in itertools.combinations(FOLDS, 2):
        (pf, _, idf), (pg, _, idg) = fits[f], fits[g]
        j = idg.get_indexer(idf)
        rf, rg = pf["r"], pg["r"][j]
        aligned, chosen = align_by_set(rf, rg, question_set(idf))
        rows.append({"effective": spearmanr((rf * pf["beta"]).sum(1), (rg * pg["beta"][j]).sum(1))[0],
                     "r_per_axis": spearman_axes(rf, aligned),
                     "identity": all(p == (0, 1, 2) for p in chosen.values())})
    rows = pd.DataFrame(rows)
    out.append(f"- effective difficulty Spearman {rows.effective.mean():.3f}; per-axis r Spearman "
               f"{rows.r_per_axis.mean():.3f}; identity permutation in {rows.identity.sum()}/10 pairs")

    out.append("\n## 4. Question sets are disconnected blocks; cross-set difficulty is prior-anchored")
    dd = pd.read_csv(DD / "fold_0/train/synergy/bonus_parts.csv").set_index("bonus_part_id").reindex(part_ids)
    dd_effective = (dd[["r_1", "r_2", "r_3"]].to_numpy() * dd[["beta_1", "beta_2", "beta_3"]].to_numpy()).sum(1)
    table = pd.DataFrame({"set": part_set, "team_irt_3d": effective, "dd_multidim": dd_effective})
    conversion = train.assign(set=question_set(train.bonus_part_id)).groupby("set").correct.mean()
    team_mean = pd.Series((theta).mean(1)).groupby(team_set).mean()
    summary = table.groupby("set").mean().assign(observed_conversion=conversion, team_irt_mean_theta=team_mean)
    out.append(summary.round(3).to_string())
    for name, column in (("Team IRT 3D", effective), ("DD multidim", dd_effective)):
        within = np.mean([spearmanr(column[part_set == s], meta.difficulty.map({"easy": 0, "medium": 1, "hard": 2})[part_set == s])[0]
                          for s in np.unique(part_set)])
        out.append(f"- {name}: Spearman of effective difficulty with declared easy<medium<hard, mean within set {within:.3f}")

    out.append("\n## 5. What the identified relevance r tracks (fold 0)")
    share = r
    labels = {"category": meta.category.to_numpy(), "subcategory": meta.subcategory.to_numpy(),
              "declared difficulty": meta.difficulty.to_numpy(), "part position": meta.position.to_numpy()}
    known = (meta.category != "Unknown").to_numpy()  # Regionals parts have no category metadata
    for name, groups in labels.items():
        rows = known if name in ("category", "subcategory") else np.ones(len(groups), bool)
        chance = np.mean([eta2_within_set(share[rows], groups[rows], part_set[rows], shuffle=True) for _ in range(20)])
        out.append(f"- within-set eta^2 of r shares by {name}{' (sets with category labels)' if name in ('category', 'subcategory') else ''}: "
                   f"{eta2_within_set(share[rows], groups[rows], part_set[rows]):.3f} (label-shuffle chance {chance:.3f})")
    out.append(f"- pooled eta^2 of r shares by question set: {np.mean([eta2(share[:, k], part_set) for k in range(3)]):.3f}")
    means = pd.DataFrame(share, columns=["r1", "r2", "r3"]).assign(set=part_set, difficulty=meta.difficulty.to_numpy(),
                                                                 category=meta.category.to_numpy())
    out.append("Mean r by set and declared difficulty:\n" + means.groupby(["set", "difficulty"])[["r1", "r2", "r3"]].mean().round(3).to_string())
    main_categories = ["Literature", "Science", "History", "Fine Arts", "Religion", "Mythology", "Philosophy", "Social Science"]
    out.append("Mean r by set and category (last column: axis with the largest mean):")
    grouped = means[means.category.isin(main_categories)].groupby(["set", "category"])[["r1", "r2", "r3"]].mean()
    out.append(grouped.round(3).assign(dominant=grouped.to_numpy().argmax(1) + 1).to_string())

    out.append("\n## 6. Words and answers on the most-loaded parts of each axis, per set (fold 0)")
    for value in np.unique(part_set):
        rows = np.flatnonzero(part_set == value)
        for k in range(3):
            order = rows[np.argsort(-share[rows, k])]
            top = order[: max(1, len(order) // 10)]
            selected = np.isin(rows, top)
            words = log_odds_words(meta.text.to_numpy()[rows], selected)
            categories = meta.category.iloc[top].value_counts(normalize=True).head(3)
            difficulties = meta.difficulty.iloc[top].value_counts(normalize=True)
            out.append(f"- {value} axis {k + 1}: top-decile r{k + 1} parts; categories "
                       f"{', '.join(f'{c} {v:.0%}' for c, v in categories.items())}; difficulty "
                       f"{', '.join(f'{c} {v:.0%}' for c, v in difficulties.items())}; distinctive words "
                       f"{', '.join(words.index)}")
            answers = [re.sub(r"\s+", " ", re.sub(r"\[.*?\]|\(.*?\)|<.*?>", "", meta.answer.iloc[i])).strip()[:40] for i in order[:5]]
            out.append(f"    top answers: {' | '.join(answers)}")

    out.append("\n## 7. Do team skill axes track subject strengths? (fold 0, within set)")
    observed = train.assign(category=train.bonus_part_id.map(meta.category), team=teams)
    predicted = 1 / (1 + np.exp(-base))
    observed = observed.assign(residual=observed.correct - predicted)
    residual = observed[observed.category.isin(main_categories)].pivot_table(index="team", columns="category", values="residual", aggfunc="mean")
    counts = observed[observed.category.isin(main_categories)].pivot_table(index="team", columns="category", values="residual", aggfunc="size")
    contrast = theta - theta.mean(1, keepdims=True)
    lines = []
    for category in main_categories:
        keep = counts[category].reindex(residual.index).fillna(0) >= 15
        index = residual.index[keep]
        corr = [spearmanr(contrast[index, k], residual.loc[index, category])[0] for k in range(3)]
        raw = [spearmanr(contrast[index, k],
                         observed[(observed.category == category)].groupby("team").correct.mean().reindex(index)
                         - observed.groupby("team").correct.mean().reindex(index))[0] for k in range(3)]
        lines.append(f"- {category} (teams with >= 15 parts: {keep.sum()}): Spearman of axis contrast theta_k - mean(theta) "
                     f"with the team's category conversion minus overall conversion {np.round(raw, 3).tolist()}; "
                     f"with the fitted model's residual {np.round(corr, 3).tolist()}")
    out += lines

    out.append("\n## 8. Axes aligned to declared-difficulty roles within each set")
    levels = np.array(["easy", "medium", "hard"])

    def roles(share, ids):
        """Per set, the axis permutation that best assigns axes to easy/medium/hard."""
        sets, difficulty = question_set(ids), np.array([part_meta[p]["difficulty"] for p in ids])
        mapping = {}
        for value in np.unique(sets):
            means = np.array([[share[(sets == value) & (difficulty == level), k].mean() for level in levels] for k in range(3)])
            mapping[value] = max(PERMS, key=lambda p: sum(means[p[j], j] for j in range(3)))  # p[j] = axis for level j
        return mapping, eta2_within_set(share, difficulty, sets)

    fits_to_check = {f"fold {fold} seed 42": (fits[fold][0]["r"], fits[fold][2]) for fold in FOLDS}
    for name in ("seed_43", "seed_44", "shifted_beta_prior_seed_42"):
        with np.load(STUDY / f"refits/{name}.npz") as saved:
            fits_to_check[f"fold 0 {name}"] = (saved["r"], part_ids)
    for name, (share_k, ids) in fits_to_check.items():
        mapping, e = roles(share_k, ids)
        described = "; ".join(f"{s.split('::')[0].replace('2024-acf-', '')} easy/med/hard = axes "
                              f"{'/'.join(str(a + 1) for a in p)}" for s, p in mapping.items())
        out.append(f"- {name}: within-set eta^2 by declared difficulty {e:.3f}; {described}")
    mapping, _ = roles(r, part_ids)
    team_roles = np.zeros_like(theta)
    for value, perm in mapping.items():
        team_roles[team_set == value] = theta[team_set == value][:, list(perm)]
    corr = pd.DataFrame(team_roles, columns=levels).groupby(team_set).corr()
    out.append("- Within-set correlation of role-aligned team skills (theta_easy, theta_medium, theta_hard):")
    for value in np.unique(team_set):
        c = corr.loc[value]
        out.append(f"    {value}: easy-medium {c.loc['easy', 'medium']:.3f}, easy-hard {c.loc['easy', 'hard']:.3f}, "
                   f"medium-hard {c.loc['medium', 'hard']:.3f}")
    by_level = observed.assign(level=observed.bonus_part_id.map(meta.difficulty)).pivot_table(
        index="team", columns="level", values="correct", aggfunc="mean")
    index = by_level.dropna().index
    out.append(f"- Spearman of theta_hard - theta_easy with the team's hard-part minus easy-part conversion: "
               f"{spearmanr(team_roles[index, 2] - team_roles[index, 0], by_level.loc[index, 'hard'] - by_level.loc[index, 'easy'])[0]:.3f}; "
               f"theta_hard with hard-part conversion {spearmanr(team_roles[index, 2], by_level.loc[index, 'hard'])[0]:.3f}; "
               f"theta_easy with easy-part conversion {spearmanr(team_roles[index, 0], by_level.loc[index, 'easy'])[0]:.3f}")
    role_contrast = team_roles - team_roles.mean(1, keepdims=True)
    lines = []
    for category in main_categories:
        keep = counts[category].reindex(residual.index).fillna(0) >= 15
        index = residual.index[keep]
        gap = (observed[observed.category == category].groupby("team").correct.mean().reindex(index)
               - observed.groupby("team").correct.mean().reindex(index))
        lines.append(f"{category} {np.round([spearmanr(role_contrast[index, k], gap)[0] for k in range(3)], 3).tolist()}")
    out.append("- Role-aligned team contrasts (easy, medium, hard) vs category conversion minus overall, Spearman: " + "; ".join(lines))

    out.append("\n## 9. Same declared-difficulty and category tests for the other 3D models (fold 0)")
    commit = "f0206078"
    from subprocess import check_output
    import io
    old_parameters = dict(np.load(io.BytesIO(check_output(
        ["git", "show", f"{commit}:results/compirt/holdout/common/bonus-team-irt/2026-09-17/fold_0/team_irt_3d/parameters.npz"]))))
    old_ids = json.loads(check_output(["git", "show", f"{commit}:results/compirt/holdout/common/bonus-team-irt/2026-09-17/fold_0/team_irt_3d/ids.json"]))
    alpha = old_parameters["alpha"]
    dd_r = dd[["r_1", "r_2", "r_3"]].to_numpy()
    for name, share_k, ids in (("Old Team IRT 3D (alpha / sum alpha, from git " + commit + ")", alpha / alpha.sum(1, keepdims=True), pd.Index(old_ids["part_ids"])),
                               ("DD multidim difficulty 3D synergy (r / sum r)", dd_r / dd_r.sum(1, keepdims=True), part_ids),
                               ("New Team IRT 3D (r)", r, part_ids)):
        sets = question_set(ids)
        difficulty = np.array([part_meta[p]["difficulty"] for p in ids])
        category = np.array([part_meta[p]["category"] for p in ids])
        known = category != "Unknown"
        out.append(f"- {name}: within-set eta^2 by declared difficulty {eta2_within_set(share_k, difficulty, sets):.3f}, "
                   f"by category (known labels) {eta2_within_set(share_k[known], category[known], sets[known]):.3f}; "
                   f"pooled by difficulty {np.mean([eta2(share_k[:, k], difficulty) for k in range(3)]):.3f}")
    text = "\n".join(out) + "\n"
    (STUDY / "output.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
