# Methodology and Evidence Standard

## Scope

The project studies whether controlled, oversight-sensitive behaviour can be measured and linked to internal representations. It does not assume that observed behaviour is deceptive, that a probe is a mechanistic explanation, or that a detected representation is sufficient for deployment-time intervention.

## Evidence ladder

1. **Behavioural effect:** a prespecified metric differs between matched conditions.
2. **Predictive representation:** an internal measurement predicts the target on held-out prompts/tasks.
3. **Causal evidence:** intervention on a candidate representation changes the target variable.
4. **Robustness:** the result survives changes in prompts, task family, seed and, where feasible, checkpoint.
5. **Safety relevance:** the effect remains useful under realistic nuisance variables without unacceptable collateral effects.

A result is not promoted up the ladder merely because it is visually striking or statistically significant on one split.

## Experimental discipline

All primary train/validation/test splits are defined before inspecting held-out outcomes. Primary analyses should use fixed seeds, explicit dataset manifests, versioned configurations and machine-readable outputs. Exploratory analyses are labelled separately from confirmatory analyses.

## Negative controls

The minimum negative-control suite is:

- shuffled labels;
- randomized feature directions;
- matched task difficulty;
- generic refusal/safety features;
- prompt-only predictors;
- held-out prompt templates;
- held-out task families where feasible.

## Interpretation rules

A probe identifies predictive information, not semantic truth. An SAE feature identifies a direction in a learned dictionary, not automatically a human-interpretable concept. Activation steering or patching demonstrates causal dependence only relative to the intervention and controls actually used.

## Reproducibility

Every reported result should have:

- configuration file;
- code version / commit SHA;
- model identifier and checkpoint where legally shareable;
- random seeds;
- dataset manifest or generator parameters;
- metric definitions;
- raw machine-readable result;
- summary interpretation and known limitations.
