"""Read-only coverage audit; run from repo root with PYTHONPATH=."""
import json
from pathlib import Path
import pandas as pd
from compirt_data import load_hf_tables
from holdout.game_splits import GameHoldoutSpec,game_holdout_masks,game_holdout_fold_assignment
out={}
t=load_hf_tables(split='year_2024')
b=t['tossup_buzzes'].copy(); b['_order']=b.buzz_id.str.rsplit('-',n=1).str[-1].astype(int)
f=b.sort_values(['game_id','tossup_id','token_position','_order']).drop_duplicates(['game_id','tossup_id'])
def quant(s):return {str(k):float(v) for k,v in s.quantile([0,.1,.25,.5,.75,.9,1]).items()}
out['year2024']={'table_counts':{k:len(v) for k,v in t.items()},'first_buzz_count':len(f),'raw_buzz_count':len(b),'first_correct_rate':float(f.correct.mean()),'first_buzz_per_player':quant(f.groupby('player_id').size()),'first_buzz_per_item':quant(f.groupby('tossup_id').size()),'first_incorrect_per_item':quant(f.assign(neg=~f.correct.astype(bool)).groupby('tossup_id').neg.sum()),'missing_tossup_categories':int(t['tossups'].category.isna().sum()+t['tossups'].category.eq('').sum())}
counts=f.groupby('player_id').size();out['year2024']['first_buzz_players']=len(counts);out['year2024']['players_under_20_first_buzzes']=int((counts<20).sum())
folds=[]
for i in range(5):
 a=game_holdout_fold_assignment(t['games'],5,42);m=game_holdout_masks(t,GameHoldoutSpec('year_2024','test',5,i,42));folds.append({'fold':i,'assigned_games':int((a==i).sum()),'retained_games':int(m.sum())})
out['fold_coverage']=folds
l=pd.read_csv('data/lineups/lineup_segments.csv')
l24=l[l.game_id.isin(t['games'].game_id)]
out['year2024']['lineup_segments']=len(l24);out['year2024']['lineup_rules']=l24.resolution_rule.value_counts().to_dict();out['year2024']['lineup_sizes']=l24.lineup_size.value_counts().sort_index().to_dict();out['year2024']['large_roster_game_teams']=int(l24.loc[l24.roster_size>4,['game_id','team_id']].drop_duplicates().shape[0])
alltables=load_hf_tables(split='all');tr=alltables['tournaments']; rows=[]
for q,g in tr.groupby('question_set_event_id'):
 ids=set(g.tournament_id);gs=alltables['games'].loc[alltables['games'].tournament_id.isin(ids),'game_id']; ts=alltables['tossups'][alltables['tossups'].question_set_event_id.eq(q)];bs=alltables['bonus_responses'][alltables['bonus_responses'].game_id.isin(gs)]
 rows.append({'set':q,'sites':len(g),'games':len(gs),'tossups':len(ts),'bonus_responses':len(bs)})
out['all_sets']=rows

output=Path('results/compirt/holdout/common/paper-readiness-tossups/data_audit.json')
output.parent.mkdir(parents=True,exist_ok=True)
output.write_text(json.dumps(out,indent=2,default=str)+'\n')
print(json.dumps(out,indent=2,default=str))
