# Research Plan

## Primary outcome
A reproducible, safely contained benchmark for distinguishing oversight-sensitive behaviour from ordinary prompt-following, together with mechanistic analyses that are predictive, causally tested and robust to distribution shift.

## Metrics

### Behavioural
- target-behaviour rate;
- performance on matched benign tasks;
- oversight-condition effect size;
- refusal rate and calibration;
- false-positive and false-negative rates.

### Mechanistic
- probe AUROC/AUPRC on held-out data;
- cross-prompt and cross-task transfer;
- cross-checkpoint transfer where feasible;
- intervention effect size;
- collateral capability change;
- representation stability across seeds.

## Controls

Every positive result should be compared against:

1. prompt-only baseline;
2. random-feature or shuffled-label baseline;
3. matched task-difficulty baseline;
4. generic refusal / safety-feature baseline;
5. held-out prompt templates;
6. held-out task families where feasible.

## Experiment matrix

The minimum confirmatory matrix uses 2 oversight conditions × 4 task families × 4 prompt templates × 3 random seeds, with difficulty matched within task family. Where feasible, add a second checkpoint to test representation transfer.

## Preregistration fields

Before confirmatory evaluation, freeze:

- primary metric and comparison;
- train/validation/test split;
- exclusion rules;
- seed set;
- minimum effect of interest;
- stopping/scaling rule;
- negative controls;
- intervention specification.

## Causal standard

A candidate feature should not be described as mechanistically explanatory unless an intervention changes the target variable in the expected direction, the effect is reproducible, and reasonable alternative explanations have been tested. Sham interventions and capability controls should be included where technically feasible.

## Interpretation hierarchy

1. **Behavioural effect:** evidence of an oversight-sensitive behavioural difference.
2. **Predictive representation:** evidence that an internal measurement contains predictive information.
3. **Causal dependence:** evidence that intervention on that measurement changes the target variable.
4. **Robustness:** evidence that the effect generalises across nuisance variables.
5. **Safety relevance:** evidence that a constrained mitigation reduces the target without unacceptable collateral effects.

Do not skip levels because a result appears intuitive.

## Analysis workflow

1. Define the phenomenon and primary metric.
2. Generate controlled datasets.
3. Split train/validation/test before inspecting held-out outcomes.
4. Establish behavioural baselines.
5. Fit probes or sparse-feature models.
6. Test held-out generalisation.
7. Run causal interventions.
8. Replicate with changed seeds, prompts and tasks.
9. Document null results and failed hypotheses.
10. Package code, configuration and experiment metadata for reproducibility.

## Scaling policy

Start with the smallest model/environment that can answer the question. Increase model size, trajectory count or representation width only after a predefined evidence gate passes. This converts compute into an evidence-gated sequence rather than an unconditional maximum-compute request.
