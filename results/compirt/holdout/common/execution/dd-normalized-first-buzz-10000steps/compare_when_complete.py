import json,sys,time
from pathlib import Path
import numpy as np
import pandas as pd
from analysis.correctness.tossup_accuracy_study.evaluate_timing import summarize
from compirt_eval.common.metrics import classification_metrics,negative_class_metrics
q=Path(sys.argv[1]);meta=json.loads((q/'launch.json').read_text())
while True:
    status=json.loads((q/'status.json').read_text())
    if status['state']=='complete':break
    if status['state'] in ('failed','interrupted'):raise SystemExit('Queue did not complete: '+status['state'])
    time.sleep(30)
oldq=Path('results/compirt/holdout/common/execution/dd-and-multidim-normalized-first-buzz-3000steps')
roots={'3000':Path('results/compirt/holdout/double-difficulty/likelihood-refits/dd-bernstein-332-simplex-locations-terminal-normalized-first-buzz-3000steps'),'10000':Path(meta['fit_root'])}
rows=[];parameter_rows=[]
for steps,root in roots.items():
    score_root=(oldq if steps=='3000' else q)/'dd_full_comparison'
    frames=[];buzzes=[]
    for f in range(5):
        events=pd.read_csv(score_root/f'fold_{f}_events.csv')
        pred=pd.read_csv(root/f'fold_{f}/holdout/pyramidal/tossup_predictions.csv')
        buzz=pred[pred.z.eq('BUZZ')]
        frames.append(events);buzzes.append(buzz)
        s=json.loads((root/f'fold_{f}/train/pyramidal/summary.json').read_text())
        parameter_rows.append(dict(steps=int(steps),fold=f,**{k:s[k] for k in ['end_hazard','end_correct','curve_location_hazard','curve_location_correct','final_loss','best_loss','last_100_loss_slope','finite_losses']}))
    for fold,events,buzz in list(zip(range(5),frames,buzzes))+[('pooled',pd.concat(frames),pd.concat(buzzes))]:
        correctness=classification_metrics(buzz.y,buzz.predicted_correct)
        negative=negative_class_metrics(buzz.y,buzz.predicted_correct)
        p,r=negative['neg_precision'],negative['neg_recall']
        rows.append(dict(steps=int(steps),fold=fold,**summarize(events),**{f'correctness_{k}':v for k,v in correctness.items()},incorrect_probability=(1-buzz.predicted_correct).mean(),incorrect_observed_rate=1-buzz.y.mean(),neg_f1=2*p*r/(p+r) if p+r else 0))
metrics=pd.DataFrame(rows);params=pd.DataFrame(parameter_rows)
output=q/'comparison';output.mkdir(exist_ok=True)
metrics.to_csv(output/'per_fold.csv',index=False);params.to_csv(output/'training_parameters.csv',index=False)
pooled=metrics[metrics.fold.eq('pooled')].set_index('steps').drop(columns='fold').T
pooled['delta_10000_minus_3000']=pooled[10000]-pooled[3000]
pooled.index.name='metric';pooled.to_csv(output/'pooled.csv')
report='# DD-Bernstein: 3,000 versus 10,000 steps\n\nFresh fits with identical degree 3, dimensions 3, drop concentration 2, simplex relevance, learned locations, terminal intercepts, learning rate 0.005 and seeds 42. All five year_2024 game folds. Historical 3,000-step comparator already uses the normalized likelihood. No bonus stages were refit in this convergence experiment.\n\nPooled normalized full-grid event scoring on matched observations. Correctness and position metrics condition on observed buzzes. No-buzz rate is the model probability, not deterministic threshold replay.\n\n'
report+='| Metric | 3,000 steps | 10,000 steps | Change |\n| --- | ---: | ---: | ---: |\n'
for key,row in pooled.iterrows():report+=f'| {key} | {row[3000]:.8f} | {row[10000]:.8f} | {row["delta_10000_minus_3000"]:+.8f} |\n'
report+='\n## Training diagnostics\n\n| Steps | Fold | Terminal hazard intercept | Final loss | Last 100-step loss slope |\n| --- | --- | ---: | ---: | ---: |\n'
for row in params.itertuples():report+=f'| {row.steps} | {row.fold} | {row.end_hazard:.6f} | {row.final_loss:.3f} | {row.last_100_loss_slope:.6f} |\n'
report+='\nSingle optimization seed, reused development folds. The likelihood correction is held fixed; this comparison changes optimization duration.\n'
(output/'REPORT.md').write_text(report)
print(pooled.to_string(),flush=True)
print('Report: '+str(output/'REPORT.md'),flush=True)
