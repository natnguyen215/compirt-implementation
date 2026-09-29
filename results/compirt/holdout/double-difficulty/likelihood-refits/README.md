# First-buzz likelihood refits

These runs refit the same Bernstein 3/3/2, simplex-relevance, learned-location,
terminal-intercept model with the corrected first-buzz probability law.
`normalized-first-buzz` means that winner probabilities and survival form a
normalized distribution, including a dead tossup through the final token.
See the [likelihood definition](../../../../../docs/first-buzz-likelihood.md).

| Budget | Results |
| --- | --- |
| 3,000 steps | [Run](dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps/) |
| 10,000 steps | [Run](dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-10000steps/) |

The [historical reference](../ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal/)
uses the older fitted likelihood. Replaying it does not refit its parameters.
[Bonus fits using the 3,000-step skills](../compositional/no-synergy-and-dot-additive-1d/)
live with the other compositional results.
