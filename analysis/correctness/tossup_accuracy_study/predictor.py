"""Serializable correctness predictor using the study's sparse design."""
import numpy as np
from scipy import sparse
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, SplineTransformer


class CorrectnessPredictor:
    """Predict P(incorrect | observed first buzzer, question, buzz position).

    Frames require player_id, tossup_id, relative_position, terminal, and
    item_clue only when the selected config enables clue effects.
    """
    def __init__(self, config, skill_by_player=None):
        self.config = config
        self.skill_by_player = skill_by_player

    def _skills(self, frame):
        width = len(next(iter(self.skill_by_player.values())))
        return np.asarray([self.skill_by_player.get(p, np.zeros(width)) for p in frame.player_id])

    def fit(self, frame):
        self.spline = SplineTransformer(n_knots=5, degree=3, include_bias=False).fit(frame[['relative_position']])
        self.player = OneHotEncoder(handle_unknown='ignore').fit(frame[['player_id']])
        self.item = OneHotEncoder(handle_unknown='ignore').fit(frame[['tossup_id']])
        if self.config.get('clue'):
            self.clue = OneHotEncoder(handle_unknown='ignore').fit(frame[['item_clue']])
        if self.skill_by_player is not None:
            skills = self._skills(frame)
            self.mean, self.sd = skills.mean(0), skills.std(0).clip(.1)
        self.model = LogisticRegression(C=1, max_iter=2000, tol=1e-6, solver='lbfgs')
        self.model.fit(self.transform(frame), frame.neg)
        if self.model.n_iter_[0] >= self.model.max_iter:
            raise RuntimeError('Logistic fit reached iteration limit')
        return self

    def transform(self, frame):
        config = self.config
        basis = self.spline.transform(frame[['relative_position']])
        item = self.item.transform(frame[['tossup_id']])
        pieces = [sparse.csr_matrix(basis), sparse.csr_matrix(frame[['terminal']].to_numpy()),
                  self.player.transform(frame[['player_id']])*config['player'], item*config['item']]
        local = np.column_stack([frame.relative_position.to_numpy()-.7, frame.terminal])
        if config.get('curve') == 'spline':
            local = np.column_stack([basis, frame.terminal])
        pieces.extend(item.multiply(local[:, k, None])*config['local'] for k in range(local.shape[1]))
        if config.get('clue'):
            pieces.append(self.clue.transform(frame[['item_clue']])*config['clue'])
        if self.skill_by_player is not None:
            skills = (self._skills(frame)-self.mean)/self.sd
            pieces.extend(item.multiply(skills[:, k, None])*config.get('skill', .5)
                          for k in range(skills.shape[1]))
        return sparse.hstack(pieces, format='csr')

    def predict_proba(self, frame):
        return self.model.predict_proba(self.transform(frame))
