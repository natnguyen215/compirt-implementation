"""Group player observations into event rosters for posterior prediction."""

import torch


def event_rosters(data):
    """Return padded players, active slots, tossup indexes, and token lengths.

    Roster tensors have shape ``(n_events, max_roster_size)``; tossup indexes
    and lengths have shape ``(n_events,)``. Events retain ``event_ids`` order,
    and players retain their observation order within each event.
    """
    # Bounceback rows repeat opposing players after a neg. Only phase-0 rows
    # belong in the roster used to predict the event's first buzz.
    phase0 = data.get("is_phase0")
    if phase0 is None:
        phase0 = torch.ones_like(data["event"], dtype=torch.bool)
    n_events = len(data["event_ids"])
    counts = torch.bincount(data["event"][phase0], minlength=n_events)
    max_roster = int(counts.max().item())
    roster = data["player"].new_zeros((n_events, max_roster))
    roster_mask = torch.zeros_like(roster, dtype=torch.bool)
    event_tossup = data["tossup"].new_zeros(n_events)
    event_tokens = data["T_j"].new_ones(n_events)

    # Fill one slot per observation; the mask keeps padded player-zero indexes
    # out of the hazard product when events have different roster sizes.
    next_slot = [0] * n_events
    for row in torch.nonzero(phase0, as_tuple=True)[0].tolist():
        event = int(data["event"][row].item())
        slot = next_slot[event]
        roster[event, slot] = data["player"][row]
        roster_mask[event, slot] = True
        event_tossup[event] = data["tossup"][row]
        event_tokens[event] = data["T_j"][row]
        next_slot[event] += 1
    return roster, roster_mask, event_tossup, event_tokens
