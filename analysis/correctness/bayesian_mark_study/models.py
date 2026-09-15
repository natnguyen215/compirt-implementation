"""Isolated conditional-mark experiments; no changes to production models.

Gaussian penalties are MAP priors. `variational` uses a diagonal Gaussian
posterior, deterministic Gauss-Hermite expected likelihood, and type-II MAP
group prior scales (approximate empirical Bayes, not full hyperparameter Bayes).
"""
import numpy as np
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder, SplineTransformer
import torch
from torch.nn import functional as F


def features(train, evaluation, config):
    left, right, groups, names = [], [], [], []

    def add(name, a, b):
        a, b = sparse.csr_matrix(a), sparse.csr_matrix(b)
        left.append(a); right.append(b)
        groups.extend([len(names)] * a.shape[1]); names.append(name)

    spline = SplineTransformer(n_knots=5, degree=3, include_bias=False)
    a = spline.fit_transform(train[['relative_position']])
    b = spline.transform(evaluation[['relative_position']])
    add('global', np.column_stack([np.ones(len(train)), a, train.terminal]),
        np.column_stack([np.ones(len(evaluation)), b, evaluation.terminal]))
    encoders = {}
    for col, name in [('player_id', 'player'), ('tossup_id', 'item')]:
        enc = OneHotEncoder(handle_unknown='ignore')
        u, v = enc.fit_transform(train[[col]]), enc.transform(evaluation[[col]])
        add(name, u, v); encoders[name] = (u, v)
    # Exactly the previously selected correctness feature structure and scales.
    u, v = encoders['item']
    add('item_curve', sparse.hstack([u.multiply(a[:, k, None])*3 for k in range(a.shape[1])]),
        sparse.hstack([v.multiply(b[:, k, None])*3 for k in range(b.shape[1])]))
    add('item_terminal', u.multiply(train.terminal.to_numpy()[:, None])*3,
        v.multiply(evaluation.terminal.to_numpy()[:, None])*3)
    if config.get('player_curve'):
        scale = config['player_curve']
        u, v = encoders['player']
        add('player_curve', u.multiply((train.relative_position.to_numpy()-.7)[:, None])*scale,
            v.multiply((evaluation.relative_position.to_numpy()-.7)[:, None])*scale)
        add('player_terminal', u.multiply(train.terminal.to_numpy()[:, None])*scale,
            v.multiply(evaluation.terminal.to_numpy()[:, None])*scale)
    if config.get('subcategory'):
        scale = config['subcategory']
        for column in ['subcategory', 'player_subcategory']:
            enc = OneHotEncoder(handle_unknown='ignore')
            u, v = enc.fit_transform(train[[column]]), enc.transform(evaluation[[column]])
            add(column, u*scale, v*scale)
            if column == 'subcategory':
                add('subcategory_curve', sparse.hstack([u.multiply(a[:, k, None])*scale for k in range(a.shape[1])]),
                    sparse.hstack([v.multiply(b[:, k, None])*scale for k in range(b.shape[1])]))
    if config.get('text'):
        vectorizer = TfidfVectorizer(min_df=5, max_features=12000, ngram_range=(1, 2),
                                     sublinear_tf=True, strip_accents='unicode')
        column = config.get('text_column', 'window_text')
        add('text', vectorizer.fit_transform(train[column])*config['text'],
            vectorizer.transform(evaluation[column])*config['text'])
    if config.get('expertise'):
        # Freeze an unsupervised representation learned ONLY from fit prefixes.
        # Player coefficients share knowledge across questions via this basis.
        vectorizer = TfidfVectorizer(min_df=5, max_features=12000, ngram_range=(1, 2),
                                     sublinear_tf=True, strip_accents='unicode')
        u = vectorizer.fit_transform(train.prefix_text)
        v = vectorizer.transform(evaluation.prefix_text)
        reducer = TruncatedSVD(n_components=16, n_iter=5, random_state=42)
        a_text, b_text = reducer.fit_transform(u), reducer.transform(v)
        mean = a_text.mean(0); sd = a_text.std(0).clip(.03)
        a_text, b_text = (a_text-mean)/sd, (b_text-mean)/sd
        add('text_global', a_text*.3, b_text*.3)
        u, v = encoders['player']
        scale = config['expertise']/np.sqrt(16)
        add('player_text', sparse.hstack([u.multiply(a_text[:, k, None])*scale for k in range(16)]),
            sparse.hstack([v.multiply(b_text[:, k, None])*scale for k in range(16)]))
    return (sparse.hstack(left, format='csr'), sparse.hstack(right, format='csr'),
            np.asarray(groups), names)


def fit_map(x, z, train, config):
    # The first feature is an explicit intercept, with a weak N(0, 10^2) prior.
    x, z = x.copy(), z.copy()
    x[:, 0] *= 10; z[:, 0] *= 10
    target = np.where(train.neg.eq(0), 0, np.where(train.value.lt(0), 1, 2)) if config.get('multinomial') else train.neg
    model = LogisticRegression(C=1, fit_intercept=False, max_iter=2500, tol=1e-7)
    model.fit(x, target)
    if model.n_iter_.max() >= model.max_iter:
        raise RuntimeError('MAP optimization did not converge')
    prob = model.predict_proba(z)
    neg = 1-prob[:, 0] if config.get('multinomial') else prob[:, 1]
    info = {'iterations': int(model.n_iter_.max()), 'parameters': int(model.coef_.size)}
    return neg, info


def as_sparse(x, device):
    a = x.tocoo()
    return torch.sparse_coo_tensor(np.stack([a.row, a.col]), a.data,
                                   a.shape, device=device, dtype=torch.float64,
                                   check_invariants=True).coalesce()


def variational(x, z, train, groups, names, config, device='cuda', max_steps=2400):
    """Integrate each normal linear predictor with 16-point quadrature.

    All fitting, including scale estimation and stopping, uses training data.
    Group prior log-scales have N(0, .75^2) priors; global scale is fixed at 3.
    Evaluation labels never enter the objective or the stopping rule.
    """
    torch.set_num_threads(1)
    a, a2 = as_sparse(x, device), as_sparse(x.power(2), device)
    b, b2 = as_sparse(z, device), as_sparse(z.power(2), device)
    y = torch.as_tensor(train.neg.to_numpy(copy=True), dtype=torch.float64, device=device)
    group = torch.as_tensor(groups, device=device)
    mu = torch.zeros(x.shape[1], dtype=torch.float64, device=device, requires_grad=True)
    rho = torch.full_like(mu, -1.5, requires_grad=True)
    log_scale = torch.zeros(len(names), dtype=torch.float64, device=device, requires_grad=True)
    nodes, weights = np.polynomial.hermite.hermgauss(16)
    nodes = torch.as_tensor(nodes*np.sqrt(2), device=device)
    weights = torch.as_tensor(weights/np.sqrt(np.pi), device=device)
    opt = torch.optim.Adam([mu, rho, log_scale], lr=.035)
    trace = []

    def moments(matrix, squared):
        mean = torch.sparse.mm(matrix, mu[:, None]).squeeze(1)
        variance = torch.sparse.mm(squared, (2*rho).exp()[:, None]).squeeze(1)
        return mean, variance

    def objective():
        mean, variance = moments(a, a2)
        eta = mean[:, None] + variance.clamp_min(1e-12).sqrt()[:, None]*nodes
        nll = ((F.softplus(eta)-y[:, None]*eta)*weights).sum()
        scales = log_scale[group]
        scales = torch.where(group.eq(0), np.log(3.), scales)
        kl = (scales-rho + .5*((2*rho).exp()+mu.square())*(-2*scales).exp()-.5).sum()
        hyper = .5*(log_scale[1:]/.75).square().sum()
        return (nll+kl+hyper)/len(y)

    for step in range(max_steps):
        opt.zero_grad(); loss = objective()
        if not torch.isfinite(loss):
            raise RuntimeError('Nonfinite variational objective')
        loss.backward(); opt.step()
        if (step+1) % 100 == 0:
            trace.append(float(loss.detach()))
            if len(trace) >= 5 and abs(trace[-1]-trace[-5]) < 2e-6:
                break
    # Refine the deterministic ELBO to avoid interpreting optimizer drift as signal.
    opt = torch.optim.LBFGS([mu, rho, log_scale], max_iter=300,
                           tolerance_grad=1e-8, tolerance_change=1e-11,
                           line_search_fn='strong_wolfe')
    def closure():
        opt.zero_grad(); loss = objective(); loss.backward(); return loss
    opt.step(closure)
    final_loss = closure()
    grad = max(float(p.grad.abs().max()) for p in [mu, rho, log_scale])
    with torch.no_grad():
        mean, variance = moments(b, b2)
        prediction = (torch.sigmoid(mean[:, None]+variance.sqrt()[:, None]*nodes)*weights).sum(1)
        plug_in = torch.sigmoid(mean)
    info = {'adam_steps': step+1, 'negative_elbo_per_row': float(final_loss.detach()),
            'max_abs_gradient': grad, 'trace': trace,
            'prior_scales': dict(zip(names, [3.] + log_scale[1:].exp().detach().cpu().tolist())),
            'mean_prediction_sd_logit': float(variance.sqrt().mean()),
            'parameters': int(mu.numel())}
    return prediction.cpu().numpy(), plug_in.cpu().numpy(), info
