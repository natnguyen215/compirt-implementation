"""Fixed-specification correctness baselines and event-likelihood audit.

Run from repository root with PYTHONPATH=.; see results/compirt/holdout/common/paper-readiness-tossups/REPORT.md.
No CompIRT fits or existing result artifacts are changed.
"""
import json
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, SplineTransformer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import log_loss,roc_auc_score,brier_score_loss,accuracy_score
from compirt_data import load_hf_tables
from holdout.game_splits import GameHoldoutSpec, game_holdout_masks
OUTPUT = Path('results/compirt/holdout/common/paper-readiness-tossups')
OUTPUT.mkdir(parents=True, exist_ok=True)
root=Path('results/compirt/holdout/double-difficulty/ablations/model-components/relevance-locations-terminal/dd-bernstein-332-simplex-locations-terminal')
t=load_hf_tables(split='year_2024'); b=t['tossup_buzzes'].copy(); b['_order']=b.buzz_id.str.rsplit('-',n=1).str[-1].astype(int)
b=b.sort_values(['game_id','tossup_id','token_position','_order']).drop_duplicates(['game_id','tossup_id']).copy()
b['T_j']=b.num_tokens_total.clip(lower=1);b['t_star']=np.minimum(b.token_position.clip(lower=1),b.T_j);b['relative_position']=b.t_star/b.T_j;b['terminal']=(b.t_star==b.T_j).astype(int);b['y']=b.correct.astype(int)
b['event_id']=b.game_id+'::'+b.tossup_id
rows=[]; audits=[];pooled=[]
for fold in range(5):
 d=pd.read_csv(root/f'fold_{fold}/holdout/pyramidal/tossup_predictions.csv');test=d[d.z=='BUZZ'].copy();test['terminal']=(test.t_star==test.T_j).astype(int)
 mask=game_holdout_masks(t,GameHoldoutSpec('year_2024','test',5,fold,42));testgames=set(t['games'].loc[mask,'game_id']);train=b[~b.game_id.isin(testgames)].copy()
 assert set(test.game_id)<=testgames
 check=b.set_index('event_id').loc[test.event_id]
 assert np.array_equal(check.y.to_numpy(),test.y.to_numpy()) and np.allclose(check.relative_position,test.relative_position)
 y=test.y.to_numpy(); probs={'constant_training_prevalence':np.full(len(test),train.y.mean()),'saved_simplex_332':test.predicted_correct.to_numpy()}
 for name,cat in [('position_terminal',[]),('player_item_position_terminal',['player_id','tossup_id'])]:
  terms=[('position',SplineTransformer(n_knots=5,degree=3,include_bias=False),['relative_position']),('terminal','passthrough',['terminal'])]
  if cat:terms.append(('ids',OneHotEncoder(handle_unknown='ignore'),cat))
  model=make_pipeline(ColumnTransformer(terms),LogisticRegression(C=1.0,solver='lbfgs',max_iter=1000,tol=1e-7))
  model.fit(train,train.y);probs[name]=model.predict_proba(test)[:,1]
  print('fit',fold,name,'iterations',model[-1].n_iter_.tolist(),flush=True)
 for name,p in probs.items():
  row={'fold':fold,'model':name,'n_train':len(train),'n_test':len(test),'log_loss':log_loss(y,p),'auc':roc_auc_score(y,p),'brier':brier_score_loss(y,p),'accuracy':accuracy_score(y,p>=.5)};rows.append(row);print(json.dumps(row),flush=True)
 frame=test[['event_id','game_id','y']].copy();frame['fold']=fold
 for name,p in probs.items():frame[name]=p
 pooled.append(frame)
 # At the observed event cell: quantify exactly the change of event factor.
 h=d.predicted_hazard.clip(1e-10,1-1e-10);d['no_cell']=1-h;d['odds']=h/(1-h)
 agg=d.groupby('event_id').agg(no_cell=('no_cell','prod'),sum_odds=('odds','sum'),sum_h=('predicted_hazard','sum'))
 z=agg.loc[test.event_id].copy();z.index=test.index
 d['unique_weight']=d.predicted_hazard * d.event_id.map(agg.no_cell) / np.clip(1-d.predicted_hazard,1e-6,None)
 sums=d.groupby('event_id').unique_weight.sum().loc[test.event_id].to_numpy()
 unique=test.predicted_hazard.to_numpy()*z.no_cell.to_numpy()/np.clip(1-test.predicted_hazard.to_numpy(),1e-6,None)
 attribution=np.where(sums>1e-12,unique/np.clip(sums,1e-12,None),test.predicted_hazard.to_numpy()/z.sum_h.to_numpy())
 factor=(1-z.no_cell)*attribution
 delta=np.log(test.predicted_hazard/factor)
 excess=z.no_cell+z.sum_h-1
 audits.append({'fold':fold,'mean_normalized_minus_training_form_nll_at_buzz':float(delta.mean()),'terminal_mean_delta':float(delta[test.terminal==1].mean()),'nonterminal_mean_delta':float(delta[test.terminal==0].mean()),'terminal_buzzes':int(test.terminal.sum()),'max_cell_excess_mass':float(excess.max()),'mean_cell_excess_mass':float(excess.mean())})
res=pd.DataFrame(rows);res.to_csv(str(OUTPUT / 'correctness_baselines.csv'),index=False)
pd.concat(pooled).to_csv(str(OUTPUT / 'correctness_predictions.csv'),index=False)
Path(str(OUTPUT / 'likelihood_audit.json')).write_text(json.dumps(audits,indent=2))
print('MEANS',res.groupby('model')[['log_loss','auc','brier','accuracy']].mean().to_json(orient='index'),flush=True)
print('LIKELIHOOD',json.dumps(audits),flush=True)
