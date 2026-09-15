"""Isolated model implementations for the tossup correctness study."""

import numpy as np
from scipy import sparse
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, SplineTransformer
import torch
from torch import nn
from torch.nn import functional as F


def linear_features(train, evaluation, config, skills=None):
    spline = SplineTransformer(n_knots=5, degree=3, include_bias=False)
    a = [sparse.csr_matrix(spline.fit_transform(train[['relative_position']]))]
    b = [sparse.csr_matrix(spline.transform(evaluation[['relative_position']]))]
    a.append(sparse.csr_matrix(train[['terminal']].to_numpy()))
    b.append(sparse.csr_matrix(evaluation[['terminal']].to_numpy()))
    item_train = item_test = None
    for column, scale in [('player_id', config['player']), ('tossup_id', config['item'])]:
        encoder = OneHotEncoder(handle_unknown='ignore')
        left = encoder.fit_transform(train[[column]])
        right = encoder.transform(evaluation[[column]])
        a.append(left * scale)
        b.append(right * scale)
        if column == 'tossup_id':
            item_train, item_test = left, right
    train_local = np.column_stack([train.relative_position.to_numpy() - .7, train.terminal])
    test_local = np.column_stack([evaluation.relative_position.to_numpy() - .7, evaluation.terminal])
    if config.get('curve') == 'spline':
        train_local = np.column_stack([spline.transform(train[['relative_position']]), train.terminal])
        test_local = np.column_stack([spline.transform(evaluation[['relative_position']]), evaluation.terminal])
    for k in range(train_local.shape[1]):
        a.append(item_train.multiply(train_local[:, k, None]) * config['local'])
        b.append(item_test.multiply(test_local[:, k, None]) * config['local'])
    if config.get('clue'):
        encoder = OneHotEncoder(handle_unknown='ignore')
        a.append(encoder.fit_transform(train[['item_clue']]) * config['clue'])
        b.append(encoder.transform(evaluation[['item_clue']]) * config['clue'])
    if skills is not None:
        left = skills[train.player_index.to_numpy()]
        right = skills[evaluation.player_index.to_numpy()]
        mean, sd = left.mean(0), left.std(0).clip(.1)
        left, right = (left-mean)/sd, (right-mean)/sd
        for k in range(left.shape[1]):
            a.append(item_train.multiply(left[:, k, None]) * config.get('skill', .5))
            b.append(item_test.multiply(right[:, k, None]) * config.get('skill', .5))
    return sparse.hstack(a, format='csr'), sparse.hstack(b, format='csr')


def fit_linear(train, evaluation, config, skills=None):
    x, z = linear_features(train, evaluation, config, skills)
    model = LogisticRegression(C=1, max_iter=2000, tol=1e-6, solver='lbfgs')
    model.fit(x, train.neg)
    if model.n_iter_[0] >= model.max_iter:
        raise RuntimeError('Logistic fit reached its iteration limit')
    return model.predict_proba(z)[:, 1]


class TimingModel(nn.Module):
    """Normalized race with monotone log-rate and a separate terminal exposure.

    lambda_ij(x) = exp(theta_i dot softmax(w_j) + speed_i + start_j + slope_j*x).
    Each ordinary token has exposure 1/T. The terminal cell has learned exposure.
    No correctness outcomes enter a timing-only fit.
    """

    def __init__(self, players, items, dimensions=3):
        super().__init__()
        self.theta = nn.Parameter(torch.randn(players, dimensions) * .1)
        self.speed = nn.Parameter(torch.zeros(players))
        self.relevance = nn.Parameter(torch.randn(items, dimensions) * .3)
        self.start = nn.Parameter(torch.full((items,), -2.0))
        self.slope = nn.Parameter(torch.full((items,), 2.0))
        self.end = nn.Parameter(torch.tensor(-2.3))

    def event_loss(self, race):
        players, mask, item, token, total, winner = race
        theta = self.theta[players]
        projection = (theta * self.relevance[item].softmax(-1)[:, None, :]).sum(-1)
        log_base = projection + self.speed[players] + self.start[item, None]
        rate_base = log_base.clamp(-15, 12).exp() * mask
        field_base = rate_base.sum(1)
        slope = F.softplus(self.slope[item]).clamp(max=15)
        step = slope / total
        previous = torch.minimum(token-1, total-1)
        exposure = step.exp() * torch.expm1(previous*step) / torch.expm1(step).clamp_min(1e-8) / total
        survival_loss = field_base * exposure
        current_rate = field_base * (slope * token / total).exp()
        duration = torch.where(token == total, self.end.exp(), 1/total)
        current_exposure = current_rate * duration
        no_buzz = winner < 0
        winner_rate = rate_base.gather(1, winner.clamp_min(0)[:, None]).squeeze(1)
        log_attribution = (winner_rate / field_base.clamp_min(1e-15)).clamp_min(1e-15).log()
        log_any_buzz = (-torch.expm1(-current_exposure)).clamp_min(1e-15).log()
        return (survival_loss + torch.where(no_buzz, current_exposure, -log_any_buzz-log_attribution)).sum()

    def penalty(self):
        return .5*(self.theta.square().sum() + self.speed.square().sum()
                   + self.relevance.square().sum()
                   + ((self.start+2)/2).square().sum()
                   + ((self.slope-2)/2).square().sum() + ((self.end+2.3)/2).square())

    def skills(self):
        return torch.cat([self.theta, self.speed[:, None]], dim=1)


def fit_timing(race, players, items, seed, steps=800):
    torch.manual_seed(seed)
    model = TimingModel(players, items).cuda()
    optimizer = torch.optim.Adam(model.parameters(), lr=.025)
    for _ in range(steps):
        optimizer.zero_grad()
        loss = (model.event_loss(race) + model.penalty()) / len(race[2])
        if not torch.isfinite(loss):
            raise RuntimeError('Nonfinite timing loss')
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 10)
        optimizer.step()
    return model


NUMERIC = ['relative_position', 'terminal', 'margin', 'late_margin',
           'question_fraction', 'log_length', 'clue_phase', 'boundary']

