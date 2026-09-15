# GRACE data analysis

Exploratory analysis of the GRACE live-competition buzz data and the QANTA reference corpus stored in `grace_data/`. The two components are reported separately because the QANTA `buzztrain`/`buzzdev` files are retrieval/reference questions, not the 240 questions from the GRACE live competitions.

## Summary

| Item | Count |
|---|---:|
| Live competitions (paper) | 3 |
| Matches (paper) | 93 |
| Packets in the public event archive | 12 |
| Live questions in those packets | 240 (20 per packet) |
| Recorded team-question buzz events | 1,749 |
| Team IDs with a recorded buzz | 20 |
| Human team IDs | 17 |
| Model team IDs | 3 |
| Individual players | Not recoverable from the released files |
| QANTA reference questions | 19,612 |
| Named tournaments in the QANTA corpus | 191 |

The paper reports 243 GRACE question-answer pairs: the 12 public packet files account for 240, while the remaining three were tiebreakers. It also reports 55 human-versus-model and 38 human-versus-human matches. Model identifiers follow the authors' analysis code: M1 is GPT-4, M2 is GPT-4o, and M3 is Mistral-7b-Instruct.

## Spread of buzzes

There are 1,749 event records. Humans account for 1,371 (78.4%) and models for 378 (21.6%). A question has a mean of 7.29 and median of 8 recorded buzzes, with a range of 1–14. Thirteen questions have no human buzz in the archive and 36 have no model buzz. Overall, 1,347 buzzes are correct and 402 are incorrect (77.0% accuracy when a buzz occurs).

Buzz position is reported as the raw word position divided by the whitespace-tokenized question length, so it is an approximate percentage of the question revealed. There is a large end-of-question mass: 575 events (32.9%) occur at or after 90% revealed. This is visible in [buzz_position_distribution.png](figures/buzz_position_distribution.png).

| Group | Buzzes | Accuracy | Median position, all | Median correct | Median incorrect |
|---|---:|---:|---:|---:|---:|
| Human | 1,371 | 78.7% | 78.9% | 80.0% | 71.0% |
| Model | 378 | 70.9% | 46.8% | 57.7% | 32.4% |

Model errors come especially early: the median incorrect model buzz occurs after only 32.4% of the question, versus 57.7% for correct model buzzes. For humans, the corresponding medians are 71.0% and 80.0%. In this sample, models are 7.8 percentage points less accurate when buzzing and make their errors much earlier.

Accuracy rises steadily with the amount of question revealed. In the first quarter, humans are correct on 64.0% of 50 buzzes and models on 46.2% of 39. In the final quarter, the rates increase to 82.2% of 760 human buzzes and 87.1% of 116 model buzzes. The complete four-band breakdown is in [timing_band_summary.csv](data/timing_band_summary.csv).

The three model profiles are quite different:

| Team | Model | Buzzes | Accuracy | Median position |
|---|---|---:|---:|---:|
| M1 | GPT-4 | 157 | 60.5% | 31.4% |
| M2 | GPT-4o | 128 | 86.7% | 57.3% |
| M3 | Mistral-7b-Instruct | 93 | 66.7% | 99.0% |

M1 is the most aggressive and least accurate model in the live records. M2 has the best model accuracy while buzzing later. M3 is concentrated at the very end of questions. Human team performance also varies substantially: observed accuracy ranges from 58.3% (H4) to 91.2% (H3), although those rates have different sample sizes and participant schedules. See [team_buzz_profiles.png](figures/team_buzz_profiles.png) and [team_summary.csv](data/team_summary.csv).

## Category and packet patterns

The 24 raw category labels contain several aliases. They are normalized to six standard groups: Science, Literature, History, and RMPSS each contain 48 questions; Arts contains 36; and Geography/Current Events contains 12.

Human teams are strongest on Literature buzzes (86.9% correct), while models are weakest there (54.8%). Models are strongest on Science (81.0%), where they slightly exceed the human event accuracy of 75.6%. The gap is descriptive rather than causal because participant pools and the number of recorded buzzes differ across packets and categories. Full counts and timing medians are in [category_summary.csv](data/category_summary.csv) and [category_performance.png](figures/category_performance.png).

Packet totals vary greatly—from 20 recorded events in packet 1 to 207 in packet 3—because different collections of teams encountered different packets. Packet-level counts should not be interpreted as packet difficulty without controlling for that participation structure. See [packet_overview.png](figures/packet_overview.png).

## QANTA retrieval/reference corpus

The local `qanta.buzztrain.json.gz` and `qanta.buzzdev.json.gz` files contain 18,460 training and 1,152 development questions, respectively. Together they span 1997–2015, 11 broad categories, 191 named tournaments, and 19,612 unique QANTA IDs. Literature (4,276), History (4,217), and Science (3,999) make up 63.7% of the corpus. There are 651 missing Wikipedia-page labels and 91 rows whose question text duplicates another row. The split/category/year summaries are plotted in [qanta_reference_corpus.png](figures/qanta_reference_corpus.png).

## Important data limitations

- `player_team_per_packet.pkl` is zero bytes, and live events identify teams rather than individual players. The number of individual human players cannot be derived; 17 is the number of human team IDs, not a player count.
- Tossup ID `128` occurs in both packet 3 and packet 10. `human_model_team_per_question.pkl` is keyed only by tossup ID and therefore contains 239 entries for 240 questions. All analysis joins use `(packet, tossup_index)` through `question_key`.
- The auxiliary `seen` roster field is not a reliable opportunity denominator: 159 mapped questions have at least one recorded buzzer absent from `seen`, totaling 309 team-question memberships. Consequently this analysis reports event counts and accuracy conditional on buzzing, not “buzzes divided by opportunities.”
- The event archive contains team, word position, and correctness, but not answer text, per-player identity, confidence, or a complete match schedule. Those quantities cannot be analyzed from this release.
- About one third of positions are at the end of a question, so medians and histograms should be read with that pileup in mind.

Machine-readable checks are in [validation.json](data/validation.json), including the source archive checksum and position bounds.

## Folder contents

- `analyze_grace.py`: end-to-end analysis and plotting script.
- `data/buzz_events.csv`: normalized event-level table (1,749 rows).
- `data/question_summary.csv`: one row per live question.
- `data/team_summary.csv`, `team_type_summary.csv`: team and human/model summaries.
- `data/category_summary.csv`, `packet_summary.csv`, `buzz_position_bins.csv`, `timing_band_summary.csv`: grouped live-event summaries.
- `data/qanta_*_summary.csv`: retrieval-corpus summaries.
- `data/dataset_summary.csv`: compact inventory of headline counts.
- `data/input_inventory.csv`: source paths, sizes, and SHA-256 hashes.
- `figures/`: five exploratory charts.

## Reproduction

The live buzz archive is not in `grace_data/`; download it from the authors' repository and run:

```bash
curl -L -o /tmp/grace_full.zip \
  'https://raw.githubusercontent.com/Pinafore/advcalibration/main/%5Bpublic%5DALL_final_buzzpoints_enc.zip'
.venv/bin/python archive/grace_analysis/analyze_grace.py --buzz-archive /tmp/grace_full.zip
```

The archive password (`buzzbuzz`) is published by the authors and handled by the script. The analyzed release has SHA-256 `05eb4e5965c31d97182882e814c0365a0dd4caba9519f4fc354e4660f65a84c0`.

## Sources

- [GRACE paper, ACL 2025](https://aclanthology.org/2025.acl-long.962/)
- [Authors' code and data repository](https://github.com/Pinafore/advcalibration)
