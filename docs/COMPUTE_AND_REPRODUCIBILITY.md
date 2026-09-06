# Compute and Reproducibility Protocol

## Objective

Make every computational result auditable without requiring a large unconditional compute commitment.

## Experiment identity

Every run should have an immutable identifier containing:

- experiment family;
- configuration hash or exact configuration snapshot;
- code revision;
- model/checkpoint identifier;
- dataset/task generator version;
- random seed;
- timestamp.

## Required run metadata

Record:

- number of examples/trajectories/tokens;
- accelerator type and count when applicable;
- wall-clock duration;
- estimated cost;
- software environment;
- output artifact paths;
- success/failure status;
- deviations from the protocol.

## Reproducibility tiers

**Tier 1 — Deterministic local reproduction:** same configuration and seed reproduce the same synthetic outputs and metric values within documented numerical tolerances.

**Tier 2 — Statistical reproduction:** changed seed or environment reproduces the qualitative effect and effect direction.

**Tier 3 — Scientific replication:** a materially changed prompt/task/checkpoint setup reproduces the claimed relationship.

A result should not be described as robust merely because Tier 1 succeeds.

## Compute discipline

Use evidence-gated scaling:

1. run the smallest sufficient experiment;
2. inspect predefined decision criteria;
3. scale only when the next stage can answer a clearly specified unresolved question;
4. terminate branches that fail their evidence gate;
5. preserve null results and cost records.

## Public release

Where licensing and safety permit, release code, configuration, synthetic benchmark definitions and aggregate results. Keep secrets, private credentials and operational misuse-enabling artifacts out of the repository.
