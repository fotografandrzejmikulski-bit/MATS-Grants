# Budget Plan — Autumn 2026 Research Project

## Programme-fact policy

Funding and logistics must be copied from the live official MATS materials immediately before submission. The repository does not treat historical cohort amounts, inferred reimbursement terms, or a nominal budget envelope as guaranteed applicant entitlements. citeturn621132search1turn621132search9

## Planning principle

The project uses **evidence-gated scaling**. Compute is allocated to experiments that have passed predefined evidence thresholds. A null result is a valid stopping condition.

## Proposed planning envelope

| Workstream | Planning allocation | Gate to expand |
|---|---:|---|
| Baselines and model-organism evaluation | $7,000 | Reproducible behavioural effect |
| Representation analysis | $6,000 | Held-out predictive signal above baseline |
| Robustness and replication | $4,000 | Candidate survives negative controls |
| Causal/safety prototype evaluation | $3,000 | Candidate survives causal test and safety review |
| **Planning envelope** | **$20,000** | Subject to actual programme rules and usage |

These figures are planning assumptions, not claims about guaranteed reimbursement, required spend, or a commitment to any specific vendor.

## Cost accounting

Every substantive experiment should record:

- experiment ID and hypothesis;
- model/checkpoint and software revision;
- trajectories, tokens or samples;
- accelerator configuration and runtime;
- estimated and actual compute cost where available;
- result class: `pass`, `fail`, `null`, or `exploratory`;
- reason for scaling, replication, or termination.

## Spend controls

Do not scale when the previous stage fails its evidence gate, produces only prompt-specific behaviour, or cannot distinguish the candidate from a strong baseline. Prefer a cheaper experiment that resolves a key confounder over a larger experiment that merely increases sample count.

## Application-budget language

When converting this document into application answers, describe the budget as a **conditional research plan** tied to evidence gates. Avoid asserting that large-scale compute is intrinsically necessary. The scientific argument should be that additional compute becomes useful only after lower-cost experiments establish a reason to scale.
