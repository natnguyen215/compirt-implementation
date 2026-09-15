"""Load and replay portable timing draws and conditional coefficient posteriors."""

import json
from pathlib import Path

import joblib
import numpy as np
import torch

from frozen_skills.data import races, first_buzzes, evaluation_design
from frozen_skills.evaluation import predict_events
from frozen_skills.pyramidal_model import correctness_predictive, TIMING_SITES


class FrozenSkillsPredictor:
    """Replay the cut posterior without Pyro fitting or a live parameter store."""

    def __init__(self, directory, device='cpu'):
        self.directory = Path(directory)
        self.device = device
        self.transforms = joblib.load(self.directory / 'correctness/transforms.joblib')
        self.config = json.loads((self.directory / 'feature_config.json').read_text())
        self.draws = {k: torch.as_tensor(np.load(self.directory / f'timing/posterior_draws/{k}.npy'), device=device)
                      for k in TIMING_SITES}
        coefficients = torch.load(self.directory / 'correctness/guide.pt', map_location=device, weights_only=False)
        self.locations, self.scales = coefficients['locations'], coefficients['scales']
        assert all(v.shape[0] == self.draws['theta'].shape[0] for v in self.locations.values())

    @torch.no_grad()
    def predict(self, rows, components=None, quadrature=48):
        """Full timing plus correctness at observed buzzes; ignores y labels.

        Input contains full event rosters, token counts and observed winner/time.
        Known player and question IDs are required, as in the holdout protocol.
        ``components`` evaluates a prefix for Monte Carlo sensitivity checks.
        """
        rows = rows.copy()
        rows['y'] = np.nan  # Explicitly prevent evaluation-label access.
        draws = self.draws if components is None else {k: v[:components] for k, v in self.draws.items()}
        locations = self.locations if components is None else {k: v[:components] for k, v in self.locations.items()}
        scales = self.scales if components is None else {k: v[:components] for k, v in self.scales.items()}
        buzz = first_buzzes(rows)
        design = evaluation_design(buzz, draws, self.transforms, self.device)
        mark = correctness_predictive(design, locations, scales, self.config, quadrature=quadrature)
        data, metadata = races(rows, self.transforms['player_map'], self.transforms['item_map'], self.device)
        return predict_events(data, metadata, draws, mark, buzz.index)
