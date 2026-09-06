# Research Plan

## Primary outcome
A reproducible, safely contained benchmark for distinguishing oversight-sensitive behaviour from ordinary prompt-following, together with mechanistic analyses that are predictive, causally tested and robust to distribution shift.

## Core principle

The project follows an evidence ladder:

**behavioural effect → predictive internal signal → causal intervention → robustness → safety relevance.**

No stage is treated as established merely because the previous stage produced an interesting observation.

## Primary endpoints

### Behavioural
- target-behaviour rate;
- monitored vs weaker-oversight effect size;
- matched-task capability;
- refusal rate and calibration;
- false-positive and false-negative rates.

### Mechanistic
- probe AUROC/AUPRC on held-out data;
- cross-prompt and cross-task transfer;
- cross-seed stability;
- cross-checkpoint transfer where feasible;
- intervention effect size;
- collateral capability change;
- sensitivity to representation-location choices.

## Controls

Every positive result should be compared against:

1. prompt-only baseline;
2. matched task-difficulty baseline;
3. shuffled-label / randomized-feature baseline;
4. generic refusal or safety-feature baseline;
5. held-out prompt templates;
6. held-out task families where feasible.

## Data split discipline

Create train, validation and test splits before inspecting held-out outcomes. Group-aware splitting should be used whenever examples share latent templates, tasks or generated trajectories that could otherwise leak information across partitions.

## Causal standard

A candidate feature should not be described as mechanistically explanatory unless:

1. the representation predicts the target above strong baselines;
2. intervention changes the target in the predicted direction;
3. the effect is reproducible;
4. generic capability/refusal changes do not fully explain the result;
5. negative controls fail to reproduce the same effect.

## Analysis workflow

1. Define the phenomenon and primary metric.
2. Specify confounders and competing hypotheses.
3. Generate controlled datasets.
4. Freeze train/validation/test partitions.
5. Establish behavioural baselines.
6. Fit simple probes before complex representation methods.
7. Evaluate held-out transfer.
8. Run pre-specified causal interventions.
9. Replicate with changed seeds/prompts/tasks.
10. Record null results and failed interpretations.
11. Package code, configuration and metadata for reproduction.

## Scaling policy

Start with the smallest model/environment that can answer the question. Scale model size, trajectory count, representation width or context length only when the previous stage passes its evidence threshold. A failed gate is a reason to revise the hypothesis, not automatically spend more compute.

## Decision gates

| Gate | Minimum evidence before proceeding | Action if failed |
|---|---|---|
| G1 Behaviour | reproducible effect above matched-task noise | revise organism / stop |
| G2 Prediction | held-out performance above behavioural baseline | inspect confounders / stop |
| G3 Robustness | survives material prompt/task changes | narrow claim / stop |
| G4 Causality | intervention effect with collateral controls | report correlational result only |
| G5 Safety relevance | benefit persists with acceptable false-positive cost | do not promote to safety mechanism |

## Statistical reporting

Report effect sizes with uncertainty intervals and sample sizes. Avoid binary claims based solely on a single p-value. When multiple candidates or interventions are screened, distinguish exploratory discovery from confirmatory testing and disclose the screening procedure.
