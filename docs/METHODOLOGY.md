# Methodology Standard

## Objective

The methodology prevents the project from collapsing three different claims into one:

1. **Behavioural claim:** the model behaves differently under specified conditions.
2. **Predictive claim:** an internal measurement predicts that difference out of sample.
3. **Mechanistic claim:** intervening on the measured representation changes behaviour causally.

Evidence must become stronger at each level.

## Experimental unit and independence

The preferred unit is a complete task trajectory within a fixed, versioned environment. Repeated observations sharing a latent task, template, generated seed or trajectory should be grouped during splitting and analysis when treating them as independent would leak information or inflate the effective sample size.

## Pre-registration-lite

Before confirmatory runs, record:

- primary outcome and minimum effect of interest;
- treatment/oversight conditions;
- key covariates and exclusion rules;
- train/validation/test split rule;
- primary baseline;
- candidate intervention family;
- stopping and scaling criteria.

Exploratory analyses remain permitted, but any analysis that influences a later hypothesis must be labelled exploratory.

## Baseline ladder

Run the simplest informative model first:

**majority predictor → prompt/context-only predictor → matched-task behavioural baseline → linear representation probe → sparse-feature method → causal intervention.**

Complexity is justified only when it adds information over the preceding baseline.

## Representation analysis

For each activation-derived measurement, record:

- exact model/checkpoint and layer;
- token/span aggregation rule;
- preprocessing and normalization;
- feature-selection procedure;
- train/validation/test grouping;
- calibration and class balance treatment;
- leakage controls;
- randomized or shuffled controls.

A high-performing probe is evidence of predictability, not proof of a human-interpretable intention or latent goal.

## Causal analysis

Every intervention must specify:

- target representation and selection rule;
- intervention magnitude or rule;
- sham/unrelated-feature control;
- expected direction;
- target-behaviour outcome;
- matched capability outcome;
- refusal/safety outcome;
- replication result.

The mechanistic claim should be weakened whenever the effect can be explained by generic refusal, loss of capability, distribution shift or another confounder.

## Robustness ladder

Stress-test candidate mechanisms against nuisance changes that should not erase the phenomenon itself: prompt wording, task template, task family, random seed, evaluator instructions, model checkpoint and relevant preprocessing choices.

## Interpretation policy

Use calibrated labels:

- **Observed:** directly measured in the benchmark.
- **Supported:** consistent across pre-specified controls and replications.
- **Causal evidence:** intervention changes the target with appropriate controls.
- **Speculative:** plausible interpretation not established by the experiment.

Do not upgrade an interpretation merely because it produces a coherent narrative.

## Reproducibility package

Every reported experiment should include:

- immutable experiment ID;
- code revision;
- configuration snapshot;
- random seeds;
- model/checkpoint identifier where applicable;
- dataset/task-generator version;
- train/validation/test partition rule;
- metrics, sample sizes and uncertainty estimates;
- pass/fail/null/ambiguous status;
- deviations from protocol.

## Quality bar

The project prefers a smaller result with clean controls over a larger result with ambiguous interpretation. A failure to replicate is itself an output that should change the research trajectory.
