# Experiment Matrix

The matrix is designed to prevent accidental overfitting to one prompt, task, seed or model choice and to make each research decision auditable.

## Design axes

| Axis | Minimum design target | Purpose |
|---|---|---|
| Oversight | monitored / weak-oversight | Estimate oversight-condition effect |
| Task family | ≥4 | Test whether the effect transfers beyond one task template |
| Prompt template | ≥4 per family | Detect prompt-specific artefacts |
| Seed | ≥3 | Measure stochastic stability |
| Difficulty | matched low/medium/high where feasible | Separate capability effects from oversight effects |
| Model checkpoint | ≥2 when feasible | Test checkpoint robustness |
| Predictor | prompt-only / behavioural / linear probe / sparse feature | Establish incremental information value |
| Intervention | none / sham / candidate | Support causal inference |

## Experiment ledger

| ID | Question that must be answered | Treatment | Strongest control | Primary readout | Advance condition |
|---|---|---|---|---|---|
| E1 | Does an oversight-sensitive behavioural effect exist? | Matched oversight conditions | matched difficulty + task family + seed | condition effect size | reproducible effect above baseline noise |
| E2 | Is the effect prompt-dependent? | Prompt-template perturbation | original template | cross-template effect | effect survives material wording changes |
| E3 | Is the effect task-dependent? | Held-out task families | source task family | cross-task transfer | effect transfers beyond source family |
| E4 | Does internal state add predictive information? | Representation probe | prompt-only + behavioural baselines | held-out AUROC/AUPRC | incremental predictive value |
| E5 | Is the candidate representation robust? | Seeds/checkpoints | randomized feature | transfer + stability | candidate survives robustness controls |
| E6 | Is the candidate causally relevant? | Minimal intervention | sham/unrelated-feature intervention | target delta + capability delta | directional effect with collateral controls |
| E7 | Does causality replicate? | Altered nuisance variables | original intervention | replicated intervention effect | effect survives replication |
| E8 | Is there safety value? | Constrained monitor/intervention | behavioural baseline | benefit vs false-positive/capability cost | net utility justified |

## Primary analysis

The primary behavioural outcome is the difference in target-behaviour rate between matched oversight conditions. Secondary outcomes are capability, refusal, predictive performance, transfer, calibration and intervention effect size.

## Pre-registration fields

Before confirmatory analysis, record:

- primary metric;
- primary comparison;
- train/validation/test split;
- grouping/leakage rule;
- exclusion criteria;
- seed set;
- minimum effect of interest;
- stopping/scaling rule;
- planned negative controls;
- interpretation threshold.

## Interpretation matrix

| Observation | Permitted interpretation | Not sufficient for |
|---|---|---|
| Behaviour changes with oversight | Oversight-sensitive behaviour | Deceptive intent or deceptive alignment |
| Probe predicts held-out behaviour | Internal predictive signal | Semantic interpretation |
| Intervention changes behaviour | Causal influence under the tested intervention | Universal mechanism |
| Effect replicates across prompts/seeds | Robustness evidence | Frontier-model generality |
| Prototype reduces benchmark behaviour | Controlled mitigation evidence | Deployment-grade safety guarantee |
