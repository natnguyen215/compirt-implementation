# Synergy examples and hardest bonus questions

DD-Bernstein, held-out games. Probabilities below are for answering correctly;
50% is the cutoff. **Off → on** toggles synergy in the same saved fit.
**Synergyless** is the separately trained model without synergy.
Examples show large probability shifts across several teams, with the synergyless model
agreeing with the off prediction.

Case counts total **all five held-out folds** on the shared comparison's
**127,986 team–part observations**. They count synergy off → on within the
saved fit; the same question answered by different teams counts separately.

Across those observations, turning synergy on fixes **5,433** predictions and breaks
**4,002**. Accuracy rises from **80.54% to 81.66%**; the separately trained
synergyless model scores **80.84%**.

## Helpful: right → wrong (1,558 cases)

All five parts were missed.

| Answer | Team | Off → on | Synergyless | Synergy (log-odds) | Packet / bonus / part |
| --- | --- | ---: | ---: | ---: | --- |
| International Phonetic Alphabet | Cedarville | 78.66% → 32.56% | 80.83% | -2.0328 | 14 / 1 / 1 |
| Ida B. Wells | Cedarville | 58.16% → 15.40% | 55.73% | -2.0328 | 14 / 14 / 3 |
| Saṃsāra | JMU B | 63.49% → 22.42% | 57.71% | -1.7945 | 3 / 5 / 3 |
| Vidkun Quisling | Michigan State C | 73.40% → 36.04% | 79.08% | -1.5882 | 27 / 17 / 3 |
| Being and Time | Oxford C | 67.92% → 33.15% | 63.88% | -1.4516 | 3 / 13 / 2 |

**International Phonetic Alphabet — Cedarville.** 2024 ACF Regionals at
Ohio State, round 4, game 392, fold 4.

After a lead-in about a vowel diagram
for /i/: “The most common vowel diagram appears on the chart for this system
of symbols that is widely used to transcribe sounds in linguistics.”

**Ida B. Wells — Cedarville.** 2024 ACF Regionals at Ohio State,
round 4, game 392, fold 4.

“This NAACP co-founder and leading anti-lynching activist
described convict leasing and lynching as the ‘twin infamies’ of the South.
She documented such abuses in The Red Record and Southern Horrors.”

**Saṃsāra — JMU B.** 2024 ACF Regionals at JMU, round 3, game 211, fold 0.

“As per Mahāyāna’s emphasis on karuṇā and mettā, bodhisattvas may remain in
this cycle to help others instead of seeking nibbāna like a Theravāda arahant.
This cycle of existence is linked to rebirth and reincarnation.”

**Vidkun Quisling — Michigan State C.** 2024 ACF Winter at Ohio State,
round 11, game 921, fold 1.

“Nansen worked alongside this leader on refugee programs. This man, who
governed under Josef Terboven, was later executed at Akershus Fortress in 1945.”

**Being and Time — Oxford C.** 2024 ACF Regionals at Imperial,
round 2, game 96, fold 4.

“The analysis of hermeneutics in Hans-Georg Gadamer’s Truth and Method builds
on this earlier philosophical work, which claims humans are ‘thrown’ into the
world and describes the process of ‘world disclosure.’”

## Helpful: wrong → right (3,875 cases)

All five parts below were answered correctly.

| Answer | Team | Off → on | Synergyless | Synergy (log-odds) | Packet / bonus / part |
| --- | --- | ---: | ---: | ---: | --- |
| Gena Rowlands | Pitt A | 12.60% → 80.73% | 12.07% | +3.3691 | 22 / 18 / 1 |
| Photographer | Pitt A | 19.31% → 87.43% | 26.19% | +3.3691 | 22 / 14 / 3 |
| Anthony Wayne | Binghamton A | 16.68% → 83.74% | 31.14% | +3.2473 | 38 / 15 / 1 |
| Noun cases | Arizona State B | 22.25% → 78.00% | 35.73% | +2.5166 | 44 / 11 / 3 |
| Phidias | Harvard A | 23.96% → 79.36% | 29.98% | +2.5018 | 20 / 8 / 3 |

**Gena Rowlands — Pitt A.** 2024 ACF Winter at Ohio State,
round 9, game 995, fold 2.

After a lead-in about an awkward spaghetti breakfast scene:
“Name this actor who used muttering tics in a 1974 film that ends with her
helping clean a trashed dining room with Peter Falk.”

**Photographer — Pitt A.** 2024 ACF Winter at Ohio State,
round 9, game 995, fold 2.

“A man in another Fugard play describes stealing Robert
Zwelinzima’s identity in a letter to his wife, which he dictates to the audience
in front of a character who has this profession. Styles leaves his Ford factory
job to take on this profession.” The play is *Sizwe Banzi Is Dead*.

**Anthony Wayne — Binghamton A.** 2024 ACF Fall at Cornell,
round 6, game 1379, fold 3.

“Name this general, nicknamed ‘Mad,’ who fought against the Northwestern
Confederacy. The second-most populous city in Indiana was built under this
general’s direction, and is named after him.”

**Noun cases — Arizona State B.** 2024 ACF Fall at Washington,
round 10, game 4764, fold 0.

“Generally, Tibetan nouns do not inflect for number, but use particles to mark
changes in this property. In many languages, the genitive, which marks a noun
as possessive, is an example of this property.”

**Phidias — Harvard A.** 2024 ACF Winter at Brandeis,
round 3, game 586, fold 1.

“This Athenian came second in the contest to sculpt an Amazon. This sculptor
included an Amazonmachy on the shield of his colossal Athena in the Parthenon.”

## Harmful: right → wrong (854 cases)

All five parts were answered correctly, but synergy predicted misses.

| Answer | Team | Off → on | Synergyless | Synergy (log-odds) | Packet / bonus / part |
| --- | --- | ---: | ---: | ---: | --- |
| Galicia | JMU B | 76.40% → 37.39% | 70.37% | -1.6901 | 6 / 5 / 1 |
| Andrés Manuel López Obrador | JMU B | 51.32% → 14.91% | 53.37% | -1.7945 | 11 / 5 / 3 |
| Draining blood | Oxford C | 68.32% → 33.56% | 65.07% | -1.4516 | 1 / 2 / 2 |
| William Makepeace Thackeray | Purdue | 67.75% → 33.32% | 60.34% | -1.4359 | 60 / 10 / 1 |
| Jimmy Hoffa | Roanoke College A | 67.67% → 33.44% | 62.44% | -1.4267 | 4 / 6 / 1 |

**Galicia — JMU B.** 2024 ACF Regionals at JMU,
round 12, game 183, fold 3.

“Name this region of Spain whose city of Santiago de Compostela
was often visited as the endpoint of the Way of Saint James, an important
pilgrimage of the medieval era.”

**Andrés Manuel López Obrador — JMU B.** 2024 ACF Regionals at JMU,
round 11, game 171, fold 0.

In a 2024 bonus about Claudia Sheinbaum:
“However, Sheinbaum has been silent on many of this current president’s
environmentally harmful projects, like the Dos Bocas oil refinery and the
Tren Maya.”

**Draining blood — Oxford C.** 2024 ACF Regionals at Imperial,
round 1, game 81, fold 4.

“You confirm that your lamb kebab is not too unclean because this process was
performed at the (emphasize) end of zabiha. Byproducts of this process are
always haram for eating. Description acceptable.”

**William Makepeace Thackeray — Purdue.** 2024 ACF Nationals,
round 14, game 1731, fold 4.

“Name this author whose novel Catherine satirizes the glamorized criminals
of his era’s Newgate novels. An Irishman created by this author is impressed
into the Prussian army after pretending to be Lieutenant Fakenham.”

**Jimmy Hoffa — Roanoke College A.** 2024 ACF Regionals at JMU,
round 4, game 226, fold 0.

“Name this person whose death is central to I Heard You Paint Houses, a
supposed biography of hitman Frank Sheeran. Thus far, searches for this
person’s body in Bloomfield Township, Michigan, have not been fruitful.”

## Harmful: wrong → right (3,148 cases)

All five parts below were missed.

| Answer | Team | Off → on | Synergyless | Synergy (log-odds) | Packet / bonus / part |
| --- | --- | ---: | ---: | ---: | --- |
| Childhood | Pitt A | 14.54% → 83.17% | 17.54% | +3.3691 | 22 / 13 / 2 |
| Intaglio | Pitt A | 17.18% → 85.77% | 21.65% | +3.3691 | 22 / 7 / 2 |
| p53 | Binghamton A | 15.66% → 82.68% | 36.58% | +3.2473 | 39 / 12 / 2 |
| Brothers | Harvard A | 22.48% → 77.96% | 29.38% | +2.5018 | 20 / 12 / 1 |
| Caryatids | Arizona State B | 17.63% → 72.61% | 27.23% | +2.5166 | 38 / 10 / 2 |

**Childhood — Pitt A.** 2024 ACF Winter at Ohio State,
round 9, game 995, fold 2.

“Jesperson heavily cites Jules Gill-Peterson, whose best-known
book documents trans people with this status in 20th-century America. Philippe
Ariès’s (‘ar-YES’s’) book Centuries of [this status] argues that this status is
a modern invention.”

**Intaglio — Pitt A.** 2024 ACF Winter at Ohio State,
round 9, game 995, fold 2.

“Callot etched his prints for The Great Miseries of War into
copper plates, meaning they belong to this class of print techniques. This
Italian word can also refer to a gemstone that, unlike a cameo, is engraved
as a counter-relief.”

**p53 — Binghamton A.** 2024 ACF Fall at Cornell,
round 7, game 1388, fold 3.

“Death of cells with damaged DNA can be induced via this tumor suppressor
protein. This protein contains four identical protein chains and induces
apoptosis.”

**Brothers — Harvard A.** 2024 ACF Winter at Brandeis,
round 3, game 586, fold 1.

“Name these people, the subject of a poem that Dirk Obbink’s team discovered
in 2014. One of these people is told ‘hail and farewell’ at the end of a poem
by Catullus.”

**Caryatids — Arizona State B.** 2024 ACF Fall at Washington,
round 5, game 4798, fold 0.

“You start work on six of these sculptures, which will be placed on a porch
in the Erechtheion (‘er-EK-thee-ahn’) in Athens. These sculpted female figures
can be used as an elaborate alternative to columns.”

The same roster adjustment fixes the Rowlands and photographer predictions
but creates confident errors on childhood and intaglio.

On new rosters overall, adding synergy to the separately trained DD model
worsens log loss from **0.42250 to 0.42797** across 6,393 parts.

## Highest difficulty in each dimension

Top three of 3,768 bonus parts in **fold 0** of
`multidim-difficulty-dot-additive-1d`, ranked by saved `beta_k` (higher is harder).
These are fitted coordinates, not subject labels; individual difficulty
coordinates are not separately identified by the responses.

| Dimension | Rank | Answer | Question / clue summary | Set; packet / bonus / part | Difficulty |
| ---: | ---: | --- | --- | --- | ---: |
| 1 | 1 | Tantalum, tin, or tungsten | Name any of the three “3TG” metals traded from the DRC conflict zone, besides gold. | 2024 Fall; 39 / 13 / 3 | 1.7438 |
| 1 | 2 | Adam Clayton Powell, Jr. | Politician criticized by Jackie Robinson for urging a boycott of the NAACP; former Abyssinian Baptist pastor. | 2024 Winter; 17 / 8 / 3 | 1.7147 |
| 1 | 3 | Information set | Group of decision nodes indistinguishable to a player, linked by a dotted line on a game tree. | 2024 Winter; 21 / 12 / 1 | 1.5528 |
| 2 | 1 | Claus | Shared name of Andersen's “Little” and “Big” characters who feud over horses and money. | 2024 Winter; 19 / 5 / 2 | 1.8158 |
| 2 | 2 | Pārśvanātha | Twenty-third Tirthankara whose successor added celibacy to four vows. | 2024 Winter; 17 / 3 / 1 | 1.8087 |
| 2 | 3 | Chromosomal rearrangements | Events clustered in chromothripsis; one type produces the BCR-ABL fusion. | 2024 Winter; 17 / 10 / 3 | 1.7769 |
| 3 | 1 | American West | Place named in Robert Adams's 1974 photobook and Richard Avedon's 1985 portrait book. | 2024 Winter; 19 / 16 / 2 | 1.7499 |
| 3 | 2 | Intentionality | Mental states' ability to be “about” or “directed at” something, reintroduced by Brentano. | 2024 Winter; 25 / 18 / 1 | 1.6084 |
| 3 | 3 | Quimbanda | Brazilian religion accused of devil worship for negative exú spirits; venerates Pomba Gira. | 2024 Winter; 18 / 5 / 3 | 1.5616 |

## Sources

- [Predictions](results/compirt/holdout/double-difficulty/compositional/no-synergy-and-dot-additive-1d/): `fold_N/holdout/{compositional,synergy}/bonus_part_predictions.csv`.
- [Difficulty parameters](results/compirt/holdout/double-difficulty/compositional/multidim-difficulty-dot-additive-1d/fold_0/train/synergy/bonus_parts.csv).
- [Scored games](results/compirt/comparisons/bonuses/dd-bernstein-and-team-irt-5fold/README.md) and [roster scores](results/compirt/comparisons/bonuses/dd-bernstein-and-team-irt-5fold/aggregate/metrics_by_question_type.csv).
- Question text: `data/hf/quizbowl-irt/bonuses/all/`. Tables use dataset packet IDs and one-based part numbers.

## Reading the complete bonuses: 10 difficulty-ordering cases

These examples use the **full-season 2024–25 in-sample DD-Bernstein fit with
multidimensional difficulty and 1D additive dot synergy**, saved under
`bonus-difficulty-season-2024-25/dd/multidim-difficulty-synergy`.
They show the complete questions alongside fitted difficulty and conversion.
The six reversals were selected to cover different subjects, sets, and attempt
counts; four correctly ordered examples provide one comparison from each set.
This is a selected sample. Across the full fitted population,
**1,174/1,296 bonuses (90.59%)** follow the declared order.

**How to read the tables:** E, M, and H are the source's easy, medium, and hard
labels. Effective difficulty is **D = relevance · difficulty = Σₖ rₖβₖ**,
computed from the saved parameter medians; higher means harder. The order score
is 1 exactly when **D_E < D_M < D_H**, otherwise 0.
These are point estimates, with no posterior probability of ordering computed
here. D is the subtracted difficulty term in the logit, not a conversion rate;
relevance, roster skills, and synergy also affect predictions.

Each table stays in the original reading order. All three conversion columns use the
same team attempts in the saved season fit, pooling mirror sites for the same
question. **Observed** reports actual correct answers / attempts and their
percentage. **Predicted** reports expected correct answers / attempts and the
mean predicted probability of correctness. Expected counts sum the saved
`predicted_correct` probabilities, so they can be fractional; percentages use
the unrounded probabilities. **Snapped** counts each attempt as correct when its
saved probability is **≥ 0.5**, and incorrect otherwise, then reports the count
and percentage predicted correct. These are in-sample predictions with synergy
included. The lead-in and all three part texts are reproduced below each table;
answers in the tables are shortened.

### 1. Mass spectrometry

**Fall 2024 · Science / Chemistry · packet 41, bonus 5.**
Bonus ID: `2024-acf-fall::fall::p41::b5`.

| Part | Declared | Answer | D | Observed correct / attempts (conversion) | Predicted correct / attempts (conversion) | Snapped correct / attempts (p ≥ 0.5) |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | H | Ionization | +2.0722 | 6/64 (9.4%) | 6.55/64 (10.2%) | 0/64 (0.0%) |
| 2 | E | Mass | −2.5153 | 58/64 (90.6%) | 55.45/64 (86.6%) | 64/64 (100.0%) |
| 3 | M | Uranium | −6.3135 | 64/64 (100.0%) | 63.42/64 (99.1%) | 64/64 (100.0%) |

**Fitted order: M < E < H. Score: 0.**

**Lead-in**

> An inert gas such as xenon is used to accomplish this task in fast atom bombardment. For 10 points each:

**Part 1 — hard**

> Identify this process, which follows matrix-assisted laser desorption in one technique. This process is classified as either “hard” or “soft” based on the amount of fragmentation.

**Part 2 — easy**

> Ionization is the first step of a form of spectrometry named for this quantity that measures its ratio to charge. Daltons are the unit used to report atoms’ value of this quantity instead of grams.

**Part 3 — medium**

> The calutron, an early mass spectrometer, was designed to help separate this element’s isotopes. This element’s “depleted” form contains almost none of its 235 isotope.

### 2. Caribbean history

**Fall 2024 · History / Other · packet 39, bonus 16.**
Bonus ID: `2024-acf-fall::fall::p39::b16`.

| Part | Declared | Answer | D | Observed correct / attempts (conversion) | Predicted correct / attempts (conversion) | Snapped correct / attempts (p ≥ 0.5) |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | H | Taíno | −1.7376 | 42/56 (75.0%) | 41.88/56 (74.8%) | 49/56 (87.5%) |
| 2 | E | 1492 | −6.3378 | 55/56 (98.2%) | 54.82/56 (97.9%) | 55/56 (98.2%) |
| 3 | M | Puerto Rico | +0.0555 | 25/56 (44.6%) | 25.57/56 (45.7%) | 21/56 (37.5%) |

**Fitted order: E < H < M. Score: 0.**

**Lead-in**

> According to Charles Mann, this people drilled holes into gourds and stuffed them with chili peppers to create an early form of chemical grenade. For 10 points each:

**Part 1 — hard**

> Name this Indigenous people of Hispaniola and other Caribbean islands. Some of them on the Bahamas were the first to encounter Christopher Columbus.

**Part 2 — easy**

> Mann discusses the Taíno in his two books titled for the years before and after this other year in which Columbus first landed in the Americas.

**Part 3 — medium**

> Residents of this island adopted the denonym Boricua from the Taíno word Borinquen. The cacique (“kah-SEE-kay”) Agüeybaná (“ah-GWAY-bah-nah”) rebelled against its first Spanish governor, Ponce de León.

### 3. Chinese concert music

**Winter 2024 · Fine Arts / Classical Music · packet 21, bonus 13.**
Bonus ID: `2024-acf-winter::2024-11-16::p21::b13`.

| Part | Declared | Answer | D | Observed correct / attempts (conversion) | Predicted correct / attempts (conversion) | Snapped correct / attempts (p ≥ 0.5) |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | H | Yellow River Cantata | +1.8760 | 5/62 (8.1%) | 6.35/62 (10.2%) | 0/62 (0.0%) |
| 2 | E | China | −6.6573 | 62/62 (100.0%) | 61.55/62 (99.3%) | 62/62 (100.0%) |
| 3 | M | Paul Dukas | +3.6062 | 2/62 (3.2%) | 2.02/62 (3.3%) | 0/62 (0.0%) |

**Fitted order: E < H < M. Score: 0.**

**Lead-in**

> At the 2008 Olympics Opening Ceremony, Láng Lǎng performed the fourth movement of Yīn Chéngzōng and Chu Wanghua’s piano concerto arrangement of this choral piece. For 10 points each:

**Part 1 — hard**

> Name this piece allegedly written in six days after its composer read a patriotic poem by Guāng Wèirán. This piece’s first movement opens with a male speaker extolling the strength and bravery of boatmen.

**Part 2 — easy**

> The Yellow River Cantata was composed by Xiǎn Xīnghǎi, a composer from this country also home to Láng Lǎng.

**Part 3 — medium**

> Xiǎn studied composition at the Paris Conservatory under this composer. A jaunty bassoon melody in 3/8 opens the main theme of a tone poem by this composer subtitled “Scherzo after a ballad by Goethe.”

### 4. Electron models

**Regionals 2025 · Science / Physics · packet 123, bonus 1.**
Bonus ID: `2025-acf-regionals::2025-02-01::p123::b1`.

| Part | Declared | Answer | D | Observed correct / attempts (conversion) | Predicted correct / attempts (conversion) | Snapped correct / attempts (p ≥ 0.5) |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | M | Free | −2.8222 | 19/20 (95.0%) | 18.32/20 (91.6%) | 20/20 (100.0%) |
| 2 | E | Pauli exclusion principle | −0.5520 | 13/20 (65.0%) | 12.15/20 (60.8%) | 14/20 (70.0%) |
| 3 | H | Empty lattice model | +3.8183 | 0/20 (0.0%) | 0.49/20 (2.4%) | 0/20 (0.0%) |

**Fitted order: M < E < H. Score: 0.**

**Lead-in**

> A model named for this property assumes that electrostatic interactions are sufficiently screened and that the probability of collision is inversely proportional to relaxation time. For 10 points each:

**Part 1 — medium**

> Name this property of electrons in the Drude–Sommerfeld model, an extension of which is named for electrons that “nearly” have this property. Electrons with this property are not bound to atoms.

**Part 2 — easy**

> The free electron model also assumes this result in which each quantum state contains at most one electron.

**Part 3 — hard**

> The nearly free electron model can be derived by adding a small perturbation to this other model that contains a vanishingly small periodic potential, which allows free electrons to travel unperturbed.

### 5. Appalachia

**Nationals 2025 · History / American · packet 143, bonus 15.**
Bonus ID: `2025-acf-nationals::04192025::p143::b15`.

| Part | Declared | Answer | D | Observed correct / attempts (conversion) | Predicted correct / attempts (conversion) | Snapped correct / attempts (p ≥ 0.5) |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | E | Quilts | +0.9210 | 7/24 (29.2%) | 7.78/24 (32.4%) | 2/24 (8.3%) |
| 2 | H | Melungeons | +0.8784 | 5/24 (20.8%) | 6.08/24 (25.3%) | 1/24 (4.2%) |
| 3 | M | Cumberland Gap | −0.9220 | 19/24 (79.2%) | 16.68/24 (69.5%) | 23/24 (95.8%) |

**Fitted order: M < H < E. Score: 0.**

**Lead-in**

> A museum dedicated to these objects in Paducah (“puh-DOO-kuh”), Kentucky showcases the artistic influence of various groups who settled in Appalachia. For 10 points each:

**Part 1 — easy**

> Name these objects. An urban legend claims that these objects were hung in front of houses to help slaves escape on the Underground Railroad.

**Part 2 — hard**

> Appalachia’s multi-ethnic composition manifests in the traditions of these people, who have a mixture of European, African, and Native-American ancestry. Though the term for these people was once a slur, it has now been reclaimed by various “tri-racial isolates.”

**Part 3 — medium**

> The Melungeons were once thought to have inhabited this region, which was named after a duke victorious at the Battle of Culloden (“kuh-LOD-un”). Daniel Boone blazed the Wilderness Road through this region.

### 6. Medieval drama

**Nationals 2025 · Literature / European · packet 133, bonus 5.**
Bonus ID: `2025-acf-nationals::04192025::p133::b5`.

| Part | Declared | Answer | D | Observed correct / attempts (conversion) | Predicted correct / attempts (conversion) | Snapped correct / attempts (p ≥ 0.5) |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | H | Terence | −0.6760 | 1/1 (100.0%) | 0.87/1 (86.6%) | 1/1 (100.0%) |
| 2 | E | Nuns | −0.5343 | 1/1 (100.0%) | 0.85/1 (85.0%) | 1/1 (100.0%) |
| 3 | M | Thaïs | +0.7948 | 0/1 (0.0%) | 0.37/1 (37.1%) | 0/1 (0.0%) |

**Fitted order: H < E < M. Score: 0.**

**Lead-in**

> Paul von Winterfeld collected a dialogue in which this writer rebuffs a director’s criticism with works by a “strong voiced” author who noted his “wickedness” in a preface. For 10 points each:

**Part 1 — hard**

> Name this author who [emphasize] inspired a play in which a governor has sex with pots and pans after mistaking them for three virgin sisters, one of six plays based on him in The Book of Drama.

**Part 2 — easy**

> Hrosvitha (“h’ROTS-vith-uh”) of Gandersheim wrote those Terence-inspired plays for these people. Hildegard of Bingen’s Ordo Virtutum was likely performed by fellow members of this occupation.

**Part 3 — medium**

> A Hrosvitha play depicts this saint, who names a courtesan sought by Phaedria in Terence’s The Eunuch. A monk in the desert kisses this woman’s lifeless body after she has a vision of God in a novel by Anatole France.

### 7. The Brontës

**Fall 2024 · Literature / British · packet 40, bonus 9.**
Bonus ID: `2024-acf-fall::fall::p40::b9`.

| Part | Declared | Answer | D | Observed correct / attempts (conversion) | Predicted correct / attempts (conversion) | Snapped correct / attempts (p ≥ 0.5) |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | M | Governess | −0.4427 | 38/66 (57.6%) | 37.02/66 (56.1%) | 44/66 (66.7%) |
| 2 | E | Charlotte Brontë | −2.3260 | 59/66 (89.4%) | 57.70/66 (87.4%) | 66/66 (100.0%) |
| 3 | H | Agnes Grey | +2.4166 | 4/66 (6.1%) | 5.17/66 (7.8%) | 0/66 (0.0%) |

**Fitted order: E < M < H. Score: 1.**

**Lead-in**

> In one novel, a character with this profession states, “I am no bird, and no net ensnares me,” when her employer tries to stop her from leaving Thornfield Hall. For 10 points each:

**Part 1 — medium**

> Name this profession which one character enters after she leaves Lowood School due to a typhus outbreak. That character educates Adèle Varens as part of this profession.

**Part 2 — easy**

> The title character of this author’s novel Jane Eyre works as a governess. She published under the pen name Currer Bell as part of a group of three sisters.

**Part 3 — hard**

> The youngest Brontë sister, Anne, wrote this novel about the title governess who meets her husband Edward Weston while working for the Murray family.

### 8. DNA damage

**Winter 2024 · Science / Biology · packet 17, bonus 10.**
Bonus ID: `2024-acf-winter::2024-11-16::p17::b10`.

| Part | Declared | Answer | D | Observed correct / attempts (conversion) | Predicted correct / attempts (conversion) | Snapped correct / attempts (p ≥ 0.5) |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | M | DNA damage | +1.2409 | 16/68 (23.5%) | 15.33/68 (22.6%) | 9/68 (13.2%) |
| 2 | E | Nucleus | −3.1547 | 64/68 (94.1%) | 62.06/68 (91.3%) | 67/68 (98.5%) |
| 3 | H | Chromosomal rearrangements | +2.7449 | 2/68 (2.9%) | 3.61/68 (5.3%) | 0/68 (0.0%) |

**Fitted order: E < M < H. Score: 1.**

**Lead-in**

> Detection of the phosphorylated histone protein gamma-H2AX (“gamma-h-two-a-x”) is commonly used to assay for this phenomenon. For 10 points each:

**Part 1 — medium**

> Name this phenomenon induced by Cas9 during CRISPR editing to trigger either non-homologous end joining or HDR. Thymine dimers are produced in the “direct” form of this general phenomenon.

**Part 2 — easy**

> Unrepaired DNA damage can cause aberrant “micro” examples of this organelle to form. This organelle dissolves during mitosis and contains a cell’s chromosomes.

**Part 3 — hard**

> DNA damage in micronuclei can result in chromothripsis, in which many of these events catastrophically occur simultaneously in a localized cluster. One type of these events forms in the BCR-ABL protein in CML.

### 9. Hume and aesthetics

**Regionals 2025 · Philosophy · packet 113, bonus 8.**
Bonus ID: `2025-acf-regionals::2025-02-01::p113::b8`.

| Part | Declared | Answer | D | Observed correct / attempts (conversion) | Predicted correct / attempts (conversion) | Snapped correct / attempts (p ≥ 0.5) |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | H | Aesthetic taste | +2.6255 | 3/63 (4.8%) | 4.06/63 (6.4%) | 0/63 (0.0%) |
| 2 | E | David Hume | −3.5911 | 59/63 (93.7%) | 58.79/63 (93.3%) | 62/63 (98.4%) |
| 3 | M | Moral sense | +0.2611 | 25/63 (39.7%) | 24.65/63 (39.1%) | 17/63 (27.0%) |

**Fitted order: E < M < H. Score: 1.**

**Lead-in**

> A book by George Dickie calls the 1700s the “century of” this concept and discusses Alexander Gerard’s “Essay on” it and Archibald Alison’s associationism in his “Essays on the Nature and Principle of” it. For 10 points each:

**Part 1 — hard**

> Name this concept that can have either “variety” or “unanimity” among people, according to an essay titled for this concept from a thinker’s Four Dissertations, which uses an example about John Ogilby and John Milton.

**Part 2 — easy**

> This philosopher acknowledged subjectivity in his essay “Of the Standard of Taste.” This Scot wrote A Treatise of Human Nature and posed the problem of induction.

**Part 3 — medium**

> Hume’s aesthetics drew on the Earl of Shaftesbury and Francis Hutcheson’s theory named for this ethical concept. Adam Smith’s book titled for this two-word concept considers the “sympathy” of the “impartial spectator.”

### 10. Dostoevsky's influence

**Nationals 2025 · Literature / World · packet 143, bonus 9.**
Bonus ID: `2025-acf-nationals::04192025::p143::b9`.

| Part | Declared | Answer | D | Observed correct / attempts (conversion) | Predicted correct / attempts (conversion) | Snapped correct / attempts (p ≥ 0.5) |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | E | Fyodor Dostoevsky | −4.2661 | 24/24 (100.0%) | 23.65/24 (98.5%) | 24/24 (100.0%) |
| 2 | M | No Longer Human | −0.0537 | 13/24 (54.2%) | 12.27/24 (51.1%) | 14/24 (58.3%) |
| 3 | H | Yi Sang | +2.0387 | 2/24 (8.3%) | 3.04/24 (12.7%) | 0/24 (0.0%) |

**Fitted order: E < M < H. Score: 1.**

**Lead-in**

> The narrator of the story “Cogwheels” is lent a misbound copy of a novel by this author by an old man with a “Pan-like expression.” For 10 points each:

**Part 1 — easy**

> What author’s “Parable of the Onion” inspired Ryūnosuke Akutagawa’s “The Spider’s Thread”? His last novel also includes the parable of “The Grand Inquisitor.”

**Part 2 — medium**

> This novel’s narrator ponders Crime and Punishment during a “game of antonyms.” In this I-novel, Yōzō’s “clowning” and morphine addiction fail to prevent his spiraling depression.

**Part 3 — hard**

> This author wrote, “close down the 19th century” as the “spirit of Dostoevsky” is “easily wasted” in a story about a recluse who survives on his wife’s prostitution, titled “The Wings.” This pioneer of Korean modernism also wrote the poem sequence Crow’s Eye View.

### Sources for the difficulty-ordering cases

- [Season fit and population](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/README.md).
- [Saved part parameters](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/dd/multidim-difficulty-synergy/bonus_parts.csv): `r_1..3` and `beta_1..3` determine D.
- [Saved season responses and predictions](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/dd/multidim-difficulty-synergy/bonus_part_predictions.csv): sums and means of `correct` and `predicted_correct`, grouped by `bonus_part_id`, determine observed and predicted counts and conversion; snapping counts `predicted_correct >= 0.5` before aggregation.
- [Per-bonus ordering scores](results/compirt/in_sample/common/bonus-difficulty-season-2024-25/bonus_difficulty_order.csv): model `DD-Bernstein, multidimensional difficulty + synergy`.
- [Existing part interpretation table](dd_model_interpretation/bonus/data/parts.csv) and [model interpretation](dd_model_interpretation/bonus/README.md).
- [Local bonus text and labels](data/hf/quizbowl-irt/bonuses/all/), joined by the exact bonus IDs above. Packet numbers are dataset packet IDs.
