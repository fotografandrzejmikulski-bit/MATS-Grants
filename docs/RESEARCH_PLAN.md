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

## Causal standard

A candidate feature should not be described as mechanistically explanatory unless an intervention changes the target variable in the expected direction, the effect is reproducible, and reasonable alternative explanations have been tested.

## Analysis workflow

1. Define the phenomenon and primary metric.
2. Generate controlled datasets.
3. Split train/validation/test before inspecting held-out outcomes.
4. Establish behavioural baselines.
5. Fit probes or SAE features.
6. Test held-out generalisation.
7. Run causal interventions.
8. Replicate with changed seeds/prompts/tasks.
9. Document null results and failed hypotheses.
10. Package code and experiment metadata for reproducibility.

## Scaling policy

Start with the smallest model/environment that can answer the question. Scale model size, number of trajectories or representation width only when the previous stage passes its pre-defined evidence threshold. This converts the compute budget into a sequence of evidence-gated experiments rather than an unconditional request for maximum compute.
