# Experiment Matrix

The matrix is designed to prevent accidental overfitting to a single prompt, task or seed.

| Axis | Minimum levels | Purpose |
|---|---|---|
| Oversight | monitored / weak-oversight | Estimate oversight-condition effect |
| Task family | ≥4 | Test transfer beyond one task template |
| Prompt template | ≥4 per family | Detect prompt-specific artefacts |
| Seed | ≥3 | Measure stochastic stability |
| Difficulty | matched low/medium/high | Separate capability from oversight effects |
| Model checkpoint | ≥2 when feasible | Test representation stability |
| Predictor | prompt-only / behavioural / linear probe / sparse feature | Establish incremental value |
| Intervention | none / sham / candidate | Support causal inference |

## Primary analysis

The primary outcome is the difference in target-behaviour rate between matched oversight conditions. Secondary outcomes are predictive performance, transfer and intervention effect size.

## Pre-registration fields

Before confirmatory analysis, record:

- primary metric;
- primary comparison;
- train/validation/test split;
- exclusion rules;
- seed set;
- stopping rule;
- minimum effect of interest;
- planned negative controls.

## Interpretation matrix

| Observation | Permitted interpretation | Not sufficient for |
|---|---|---|
| Behaviour changes with oversight | Oversight-sensitive behaviour | Deceptive intent |
| Probe predicts held-out behaviour | Internal predictive signal | Semantic interpretation |
| Intervention changes behaviour | Causal influence under intervention | Universal mechanism |
| Effect replicates across prompts/seeds | Robustness evidence | Frontier-model generality |
| Prototype reduces benchmark behaviour | Controlled mitigation evidence | Deployment-grade safety guarantee |
