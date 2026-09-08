# Decision Gates

The project is deliberately staged. The purpose of each gate is to prevent additional compute and methodological complexity from being used to rescue a weak hypothesis.

| Gate | Question | Required evidence | If failed |
|---|---|---|---|
| G0 | Is the measurement valid? | Schema, deterministic generation, unit tests, fixed protocol | Fix infrastructure |
| G1 | Is there an oversight-sensitive behavioural effect? | Effect persists under matched task difficulty and basic controls | Revise organism or stop |
| G2 | Is there incremental internal predictive value? | Held-out representation signal beats prompt/behavioural baselines | Investigate confounds or stop |
| G3 | Is the signal robust? | Transfer across prompts/tasks/seeds and, where feasible, checkpoints | Narrow claim or stop |
| G4 | Is the signal causally relevant? | Controlled intervention changes target with capability/refusal controls | Keep claim correlational |
| G5 | Is mitigation useful? | Detection/intervention improves the target metric without unacceptable collateral cost | Do not promote to safety mechanism |

## Evidence ledger requirement

Each gate decision should record:

- experiment IDs;
- code revision;
- configuration hash or immutable config snapshot;
- sample sizes;
- primary metric and estimate;
- uncertainty estimate;
- negative-control outcome;
- deviations from protocol;
- decision and rationale.

## Scaling principle

No gate may be passed merely because a result is visually striking, statistically convenient after repeated searching, or theoretically attractive. The next stage begins only when the predefined evidence requirement is met.
