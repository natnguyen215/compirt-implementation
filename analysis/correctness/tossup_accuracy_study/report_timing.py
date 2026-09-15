"""Summarize the saved timing replay and existing correctness evaluation."""

import json

import numpy as np
import pandas as pd

from analysis.correctness.paper_readiness.first_buzz_features import ROOT
from analysis.correctness.tossup_accuracy_study.evaluate_timing import OUTPUT, STUDY


def main():
    timing = pd.read_csv(OUTPUT / 'summary.csv').set_index('family')
    correctness = pd.read_csv(STUDY / 'summary.csv')
    correctness = correctness[correctness.policy.eq('default')].set_index('family')
    events = pd.concat([pd.read_csv(OUTPUT / f'fold_{fold}_events.csv') for fold in range(5)])
    assert not events.duplicated(['family', 'event_id']).any()
    replay_checks = []
    for fold in range(5):
        saved = pd.read_csv(ROOT / f'fold_{fold}/holdout/pyramidal/buzz_event_predictions.csv')
        replay = events[(events.fold == fold) & events.family.eq('saved_compirt') & events.buzz.eq(1)]
        paired = saved.merge(replay, on='event_id', validate='one_to_one')
        assert len(paired) == len(saved) == len(replay)
        assert np.allclose(paired.observed_relative_position, paired.observed_position)
        difference = np.abs(paired.predicted_relative_position - paired.predicted_position)
        # Stored predictions use float32 Torch; replay uses float64 NumPy.
        assert difference.max() < 1e-4, difference.max()
        replay_checks.append(dict(fold=fold, events=len(paired), maximum_difference=difference.max()))
    (OUTPUT / 'saved_prediction_checks.json').write_text(json.dumps(replay_checks, indent=2))

    # Conditional uncertainty: paired game-cluster bootstrap, fixed fitted models.
    intervals = []
    for metric in ['absolute_error', 'integrated_brier', 'timing_nll', 'joint_nll']:
        a = events[events.family.eq('frozen_skills')].set_index('event_id')
        b = events[events.family.eq('saved_compirt')].set_index('event_id')
        delta = a[metric] - b[metric]
        grouped = pd.DataFrame({'delta': delta, 'game_id': a.game_id}).dropna().groupby('game_id').delta.agg(['sum', 'count'])
        sums, counts = grouped['sum'].to_numpy(), grouped['count'].to_numpy()
        rng = np.random.default_rng(20260907)
        samples = []
        for _ in range(2000):
            indexes = rng.integers(0, len(grouped), len(grouped))
            samples.append(sums[indexes].sum() / counts[indexes].sum())
        low, high = np.quantile(samples, [.025, .975])
        intervals.append(dict(metric=metric, frozen_minus_saved=delta.mean(), low=low, high=high))
    pd.DataFrame(intervals).to_csv(OUTPUT / 'game_bootstrap.csv', index=False)

    def table(frame, entries):
        lines = ['| Metric | Saved DD-Bernstein | Frozen skills |', '|---|---:|---:|']
        for label, key, percent in entries:
            values = [frame.loc[family, key] for family in ['saved_compirt', 'frozen_skills']]
            formatted = [f'{v * 100:.2f}%' if percent else f'{v:.5f}' for v in values]
            lines.append(f'| {label} | {formatted[0]} | {formatted[1]} |')
        return '\n'.join(lines)

    timing_table = table(timing, [
        ('Relative-position MAE ↓', 'timing_mae', False),
        ('Relative-position RMSE ↓', 'timing_rmse', False),
        ('Mean signed position error (prediction − observation)', 'timing_bias', False),
        ('Integrated timing Brier score ↓', 'integrated_brier', False),
        ('Timing log loss, including no-buzz ↓', 'timing_nll', False),
        ('First-buzzer accuracy ↑', 'first_buzzer_accuracy', True),
        ('First-buzzer log loss ↓', 'first_buzzer_nll', False),
        ('Timing + identity log loss ↓', 'race_nll', False),
        ('Timing + identity + correctness log loss ↓', 'joint_nll', False),
        ('No-buzz Brier score ↓', 'dead_brier', False),
        ('Predicted no-buzz rate', 'predicted_dead_rate', True),
        ('Observed no-buzz rate', 'observed_dead_rate', True),
    ])
    correctness_table = table(correctness, [
        ('Accuracy ↑', 'accuracy', True), ('Incorrect-buzz precision ↑', 'neg_precision', True),
        ('Incorrect-buzz recall ↑', 'neg_recall', True), ('Incorrect-buzz F1 ↑', 'neg_f1', True),
        ('Incorrect-buzz average precision ↑', 'neg_ap', True),
        ('ROC AUC ↑', 'auc', False), ('Correctness log loss ↓', 'log_loss', False),
    ])
    mae_reduction = 100 * (1 - timing.loc['frozen_skills', 'timing_mae'] / timing.loc['saved_compirt', 'timing_mae'])
    report = f'''# Frozen skills versus saved DD-Bernstein: timing and correctness

Frozen timing changes relative-position MAE from
{timing.loc['saved_compirt', 'timing_mae']:.5f} to
{timing.loc['frozen_skills', 'timing_mae']:.5f} ({mae_reduction:.2f}% reduction).
Its correctness accuracy is {100 * correctness.loc['frozen_skills', 'accuracy']:.2f}%
versus {100 * correctness.loc['saved_compirt', 'accuracy']:.2f}% for saved DD-Bernstein.

Replayed all five saved outer timing checkpoints, without fitting or selection,
against the saved DD-Bernstein reference on identical held-out event rosters.
There are {int(timing.loc['frozen_skills', 'events']):,} events, including
{int(timing.loc['frozen_skills', 'buzz_events']):,} observed first buzzes.

## Timing and first-buzzer results

{timing_table}

Position MAE/RMSE use E[relative position | a buzz occurs] on observed-buzz
events. A relative-position error of 0.01 is 1% of question length. First-buzzer
metrics also condition on a buzz occurring and integrate over its possible time.
The integrated Brier score uses a 21-point grid from 0 to 1, including dead
events. Timing log loss scores the exact observed token or no-buzz outcome;
race log loss additionally scores buzzer identity. The joint score additionally
uses each model's saved correctness probability at the observed player/token.
All log losses use natural logarithms; smaller is better.

## Correctness at threshold 0.5

{correctness_table}

Correctness metrics reuse the original study's saved probabilities and are
conditional on the observed buzzer and position. Their event IDs and outcomes
were checked against the timing evaluation. This is not full-game simulation.

## Verification and interpretation

- Every replayed event PMF sums to one, including no-buzz mass.
- Frozen replay likelihoods were checked independently against TimingModel.event_loss
  on initial examples and all terminal/no-buzz events (see checks.json).
- Reconstructed DD-Bernstein expected positions match its saved predictions to
  within 1e-4 (see saved_prediction_checks.json).
- The DD-Bernstein distribution uses the repository's normalized categorical
  first-buzz replay law. These scores evaluate the saved model's predictive
  distribution; they are not a claim about its historical training objective.
- Frozen-skills here means its separately fitted timing-only model paired with
  its frozen-skill correctness predictor. It does not reuse DD-Bernstein timing.
- Differences cannot isolate exponential versus Bernstein curves: fitting,
  regularization, timing/correctness coupling, and rate parameterization also differ.
- game_bootstrap.csv gives 95% paired game-cluster bootstrap intervals for
  frozen minus saved (2,000 resamples, fixed fitted models). These omit refitting,
  model-search uncertainty, and dependence across games sharing questions.

## Reproduce

```sh
.venv/bin/python -m analysis.correctness.tossup_accuracy_study.evaluate_timing
.venv/bin/python -m analysis.correctness.tossup_accuracy_study.report_timing
```

Pooled timing: summary.csv. Per-fold timing: fold_metrics.csv. Per-event scores:
fold_0_events.csv through fold_4_events.csv. Original correctness: ../summary.csv.
'''
    (OUTPUT / 'REPORT.md').write_text(report)
    print(report)
    print(pd.DataFrame(intervals).to_string(index=False))


if __name__ == '__main__':
    main()
