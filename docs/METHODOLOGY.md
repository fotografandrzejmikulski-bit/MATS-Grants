# Methodology Standard

## Objective

The methodology is designed to prevent the project from confusing three different claims:

1. **Behavioural claim:** the model behaves differently under specified conditions.
2. **Predictive claim:** an internal measurement predicts that difference out of sample.
3. **Mechanistic claim:** intervening on the measured representation changes the behaviour causally.

The strength of evidence must increase from one level to the next.

## Experimental units

The preferred unit is a complete task trajectory within a fixed, versioned environment. Repeated samples generated from the same latent task or template must not be treated as independent observations when doing so would create leakage or inflate effective sample size.

## Pre-registration-lite

Before confirmatory runs, record:

- primary outcome;
- treatment/oversight conditions;
- key covariates and exclusion rules;
- train/validation/test split rule;
- primary baseline;
- candidate intervention family;
- stopping/scaling criteria.

Exploratory analyses remain allowed, but must be labelled as exploratory when they influence later hypothesis formation.

## Baseline ladder

Run the simplest informative baseline first:

**majority predictor → prompt/context-only predictor → matched-task behavioural baseline → linear representation probe → sparse-feature method → causal intervention.**

A more complicated method must demonstrate incremental information over the simpler baseline it replaces.

## Representation analysis

Activation-derived measurements may be useful even when their semantics are uncertain. Therefore:

- report the exact layer/token aggregation;
- report preprocessing and normalization;
- retain the feature-selection procedure;
- evaluate held-out examples;
- test transfer across prompts/tasks;
- quantify leakage from task or condition labels;
- compare against randomized controls.

A high-performing probe is evidence of predictability, not proof of a human-interpretable concept.

## Causal analysis

Interventions should be minimal and hypothesis-directed. For each intervention, record:

- target representation;
- intervention magnitude or rule;
- control intervention;
- expected direction;
- target-behaviour outcome;
- capability outcome;
- refusal/safety outcome;
- replication result.

Where practical, include matched interventions on unrelated features as negative controls.

## Robustness

A claimed mechanism should be stress-tested against changes that should not alter the underlying phenomenon but could alter superficial correlations: prompt wording, task templates, task families, random seeds, evaluator instructions and model checkpoint.

## Interpretation policy

Use calibrated language:

- **Observed:** directly measured in the benchmark.
- **Supported:** consistent across pre-specified controls and replications.
- **Causal evidence:** intervention changes the target with controls.
- **Speculative:** plausible interpretation not established by the experiment.

Never upgrade a speculative interpretation into a scientific conclusion solely because it provides a coherent narrative.

## Reproducibility package

Every reported experiment should have:

- immutable experiment ID;
- code revision;
- configuration snapshot;
- random seeds;
- model/checkpoint identifier where applicable;
- dataset/task generator version;
- metrics and uncertainty estimates;
- pass/fail/ambiguous status;
- notes on deviations from protocol.
