"""Replay stratified held-out examples from saved artifacts, with labels erased."""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import torch

from analysis.correctness.paper_readiness.first_buzz_features import ROOT
from frozen_skills.predict import FrozenSkillsPredictor
from frozen_skills.train_holdout import DEFAULT_OUTPUT


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=DEFAULT_OUTPUT)
    parser.add_argument('--device',default='cpu')
    parser.add_argument('--folds',type=int,nargs='+',choices=range(5),default=list(range(5)))
    args=parser.parse_args()
    torch.set_num_threads(1)
    path=args.output/'replay_checks.json'
    results=json.loads(path.read_text()) if path.exists() else []
    results=[row for row in results if row['fold'] not in args.folds]
    for fold in args.folds:
        directory=args.output/f'fold_{fold}'
        saved=pd.read_csv(directory/'events.csv').set_index('event_id')
        # Deterministic coverage of ordinary, terminal and dead events.
        selected=set(saved.head(200).index)
        selected.update(saved[saved.buzz.eq(0)].head(40).index)
        selected.update(saved[saved.buzz.eq(1)&saved.observed_position.eq(1)].head(40).index)
        rows=pd.read_csv(ROOT/f'fold_{fold}/holdout/pyramidal/tossup_predictions.csv')
        rows=rows[rows.event_id.isin(selected)]
        predictor=FrozenSkillsPredictor(directory,args.device)
        replay,checks=predictor.predict(rows)
        replay=replay.set_index('event_id')
        errors={}
        for column in ['predicted_dead','predicted_position','predicted_neg','mark_only_neg',
                       'timing_nll','race_nll','first_buzzer_nll','integrated_brier']:
            a=replay[column];b=saved.loc[replay.index,column]
            np.testing.assert_allclose(a,b,rtol=2e-5,atol=3e-6,equal_nan=True,err_msg=column)
            errors[column]=float((a-b).abs().max())
        assert len(replay)==len(selected)
        small,_=predictor.predict(rows,components=8)
        small=small.set_index('event_id')
        refined,_=predictor.predict(rows,quadrature=96)
        refined=refined.set_index('event_id')
        results.append(dict(fold=fold,events=len(replay),outcomes_erased_before_prediction=True,
                            replay_maximum_errors=errors,**checks,
                            quadrature_48_vs_96_maximum_neg_difference=float((refined.predicted_neg-replay.predicted_neg).abs().max()),
                            quadrature_48_vs_96_mean_neg_difference=float((refined.predicted_neg-replay.predicted_neg).abs().mean()),
                            eight_vs_sixteen_mean_absolute_neg_difference=float((small.predicted_neg-replay.predicted_neg).abs().mean()),
                            eight_vs_sixteen_mean_absolute_position_difference=float((small.predicted_position-replay.predicted_position).abs().mean())))
        print(f'Fold {fold}: replayed {len(replay)} events; maximum errors {errors}',flush=True)
    path.write_text(json.dumps(sorted(results,key=lambda row:row['fold']),indent=2))


if __name__=='__main__':
    main()
