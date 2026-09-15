"""Original spline equivalence and correctness-feedback gradient contracts."""
import numpy as np
import pandas as pd
import torch

from analysis.correctness.tossup_accuracy_study.models import TimingModel
from analysis.correctness.tossup_accuracy_study.predictor import CorrectnessPredictor
from frozen_skills.joint import design, unpack_coefficients, mark_logits, standardized_traits, predict_saved
from frozen_skills.train_holdout import detached_cpu


def setup():
    torch.manual_seed(4)
    timing=TimingModel(4,2)
    with torch.no_grad():
        timing.speed.copy_(torch.tensor([-.3, .1, .5, -.2]))
    rows=pd.DataFrame([dict(player_id=f'p{i%4}',tossup_id=f'q{i%2}',relative_position=(i%5+1)/5,
                            terminal=int(i%5==4),neg=int(i%3==0)) for i in range(40)])
    skills={f'p{i}':v for i,v in enumerate(timing.skills().detach().numpy())}
    config=dict(player=1.,item=1.,local=3.,skill=.5,curve='spline')
    predictor=CorrectnessPredictor(config,skills).fit(rows)
    # Reverse item order to exercise coefficient remapping.
    transforms=dict(spline=predictor.spline, player_map={f'p{i}':i for i in range(4)},
                    item_map={'q1':0,'q0':1},correctness_players={f'p{i}':i for i in range(4)})
    coefficients={k:v.requires_grad_() for k,v in unpack_coefficients(predictor,transforms['item_map']).items()}
    data=design(rows,transforms,'cpu')
    return timing,rows,predictor,transforms,coefficients,data


def test_exact_original_spline_and_saved_prediction():
    timing,rows,predictor,transforms,coefficients,data=setup()
    penalty=sum(v.detach().square().sum().item() for k,v in coefficients.items() if k!='intercept')
    np.testing.assert_allclose(penalty,np.square(predictor.model.coef_).sum(),rtol=1e-6)
    predicted=mark_logits(timing,coefficients,data,data['trait_index'],predictor.config,False).sigmoid()
    np.testing.assert_allclose(predicted.detach().numpy(),predictor.predict_proba(rows)[:,1],atol=2e-6)
    _,mean,sd=standardized_traits(timing,data['trait_index'],data['trait_index'],False)
    artifact=dict(timing=detached_cpu(timing.state_dict()), coefficients=detached_cpu(coefficients),
                  transforms=transforms, config=predictor.config,mean=mean,sd=sd)
    np.testing.assert_allclose(predict_saved(rows.drop(columns='neg'),artifact),predicted.detach().numpy(),atol=2e-6)


def test_only_joint_mode_sends_correctness_gradients_to_traits():
    timing,rows,predictor,transforms,coefficients,data=setup()
    target=torch.tensor(rows.neg.to_numpy(),dtype=torch.float32)
    for feedback in [False,True]:
        z=mark_logits(timing,coefficients,data,data['trait_index'],predictor.config,feedback)
        loss=torch.nn.functional.binary_cross_entropy_with_logits(z,target)
        gradients=torch.autograd.grad(loss,[timing.theta,timing.speed],allow_unused=True)
        if feedback:
            assert all(g is not None and torch.isfinite(g).all() and g.abs().sum()>0 for g in gradients)
        else:
            assert gradients==(None,None)
