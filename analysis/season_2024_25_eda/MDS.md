# Multidimensional scaling

Two MDS maps are produced: team entries and mirror sites. Both use the same algorithm and differ only in features and population.

## Why there is no event map

The season has four question-set events. Classical MDS embeds `n` points exactly in `n-1` dimensions, so a two-dimensional embedding of four points is near-exact by construction and its stress carries no information about structure. An event map here would look convincing and mean nothing.

The nine-event map in [`../full_dataset_eda/`](../full_dataset_eda/MDS.md) answers that question at a point count where it is meaningful.

## Algorithm

Classical (Torgerson) metric MDS, implemented in `classical_mds` in [analyze.py](analyze.py) with NumPy only.

1. Select the feature columns and coerce to numeric.
2. Impute missing values with the column median.
3. Standardize each column to zero mean and unit population standard deviation, so a rate in [0,1] and a mean score near 250 contribute comparably. Zero-variance columns are divided by 1 rather than by zero.
4. Form pairwise Euclidean distances in standardized feature space.
5. Double-centre the squared-distance matrix, eigendecompose, and take the top two eigenvectors scaled by the square roots of their eigenvalues. Negative eigenvalues are clamped to zero.
6. Report Kruskal stress-1 over all distinct pairs.

Because the input distances are Euclidean this is equivalent to PCA on the standardized features. The MDS framing is kept because the object of interest is the map of pairwise similarity.

Classical MDS produces no loadings of its own. To make the axes readable, `add_mds` correlates each standardized input feature with each embedded coordinate and writes `*_mds_loadings.csv`; [figure 23](figures/23_mds_loadings.png) plots both.

## Fit quality

| Grain | Points | Features | Stress-1 | Variance in top 2 |
|---|---:|---:|---:|---:|
| Team entries | 480 | 12 | 0.132 | 83.6% |
| Mirror sites | 33 | 10 | 0.150 | 82.0% |

Stress-1 below about 0.10 is conventionally "good" and below 0.20 "fair", so both are usable.

## Team map

**Population.** 480 of 492 team entries, filtered to at least 5 games, 30 attempts, and 15 bonuses heard. A team entry is one team at one mirror site, so a program playing Fall, Winter, and Regionals contributes three separate points — there is no cross-tournament team identity in the source data.

**Features (12).** All-attempt accuracy, scored accuracy, neg rate, zero rate, mean position, early share, very-late share, PPB, 30-point rate, 0-point bonus rate, points per game, mean margin.

**Axis 1 — general strength, sign-reversed.** PPB −0.96, points per game −0.95, early share −0.83, all-attempt accuracy −0.80, against very-late share +0.93, mean position +0.92, zero rate +0.85, 0-point bonus rate +0.80. Negative is a strong team that buzzes early, converts bonuses, and wins by more.

Note that scored accuracy loads only −0.36 on this axis while all-attempt accuracy loads −0.80. That is the season's central finding appearing in the geometry: the strength axis is built out of timing and zero rate, not out of conditional correctness.

**Axis 2 — risk appetite.** Neg rate +0.97 against scored accuracy −0.92, with everything else inside ±0.5. High on this axis means a team that negs; low means a team that converts the buzzes it takes. Close to orthogonal to strength, so how aggressively a team buzzes is largely independent of how good it is.

## Mirror-site map

**Population.** All 33 sites, no filtering.

**Features (10).** All-attempt accuracy, neg rate, zero rate, median position, PPB, 30-point rate, 0-point bonus rate, mean team score, median absolute margin, mean tossups read.

**Axis 1 — set difficulty.** Mean team score −0.99, PPB −0.97, all-attempt accuracy −0.92, 30-point rate −0.90, against median position +0.97, zero rate +0.94, 0-point bonus rate +0.88. Sites separate by which tier they ran, which is the expected sanity check: the map is dominated by the question set, not by the venue.

**Axis 2 — competitiveness.** Neg rate −0.84 and mean tossups read −0.52 against median absolute margin +0.65. Positive is blowout-heavy; negative is close, neg-heavy, longer games. Nationals sits at the negative end, consistent with its 95-point median margin.

## Limitations

- **Team entries are not teams.** No cross-tournament team identity is attempted, so a program's four appearances across the season are four unrelated points. The map cannot show a team improving through the season.
- **Standardization is over the pooled population.** Team features are standardized across all four tiers at once, so axis 1 partly encodes which tier a team played rather than how strong it was.
- **Tier is confounded with calendar time.** Within one season these cannot be separated, so "difficulty" and "later in the season" mean the same thing on axis 1 of the site map.
- **Classical MDS is linear.** Curved structure is flattened. No non-metric or stress-minimizing variant is fitted, and no dimension-selection procedure is run beyond taking two for plotting.
- **No uncertainty is quantified.** The embedding is not bootstrapped, so proximity between two points carries no error bar.
- **Coordinates are identified only up to reflection and rotation.** Interpret axes through the loadings file, never through the raw sign of a coordinate.
