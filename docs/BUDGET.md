# Budget Plan — Autumn 2026 Research Project

## Verified programme context

The official MATS Autumn 2026 page currently describes the main programme as running from September 28 to December 4, 2026. It also describes the programme as 10 weeks and an optional 6–12 month funded extension pathway. citeturn252053search3

MATS's current programme information should be treated as the source of truth for any application-specific funding or logistics claims. Do not present historical or inferred amounts as guaranteed entitlements.

## Planning principle

The project uses **evidence-gated scaling**. Compute is not requested because a large budget exists; it is allocated to experiments that have passed predefined evidence thresholds.

## Proposed compute allocation

| Workstream | Planning allocation | Decision gate |
|---|---:|---|
| Baselines and model-organism evaluation | $7,000 | Scale only after reproducible behavioural effect |
| Representation analysis | $6,000 | Scale only after held-out predictive signal |
| Robustness and replication | $4,000 | Expand only if candidate survives controls |
| Causal/safety prototype evaluation | $3,000 | Use only for validated candidate mechanisms |
| **Total planning envelope** | **$20,000** | Subject to programme rules and actual usage |

These allocations are planning assumptions, not claims about guaranteed reimbursement, vendor commitments or minimum required spend.

## Cost tracking

Each experiment should record:

- experiment ID;
- model/checkpoint;
- number of trajectories or tokens;
- wall-clock runtime;
- accelerator configuration;
- estimated cloud cost;
- result status: `pass`, `fail`, `exploratory`;
- reason for scaling or termination.

## Stop-spend criteria

Do not increase compute when the previous stage fails its evidence gate, produces only prompt-specific effects, or cannot distinguish the candidate signal from a strong baseline. A null result should reduce spend rather than trigger automatic scaling.
