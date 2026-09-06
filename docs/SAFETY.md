# Safety, Containment and Dual-Use Policy

## Scope

This repository concerns AI alignment research involving deceptive or oversight-sensitive behaviour. The goal is to improve measurement and causal understanding without turning the research environment into an operational misuse platform.

## Hard boundaries

Experiments MUST remain within approved, sandboxed environments. Do not provide experimental agents with:

- production credentials or secrets;
- access to personal accounts or private data;
- unrestricted network access or shell access to external systems;
- real financial targets or transaction authority;
- real biological systems or laboratory execution;
- real intrusion targets or persistence mechanisms.

The prototype in this repository is synthetic-only.

## Safe experimental design

Use abstract task environments and non-actionable placeholders for misuse-relevant domains. Keep measurement and intervention separate: first establish whether a phenomenon exists, then test a minimal intervention in the same controlled environment.

## Data governance

Track model/data provenance, configuration hashes, experiment IDs and access permissions. Avoid committing secrets, private datasets or proprietary model weights. Store large or sensitive artefacts outside Git when required by their licence or sensitivity.

## Stop conditions

Stop and review the experiment when any of the following occurs:

1. the sandbox boundary is unexpectedly crossed;
2. a model produces operationally dangerous content outside the approved test envelope;
3. an intervention increases harmful capability outside the intended benchmark;
4. logs are insufficient to reconstruct what happened;
5. a dependency or data source introduces an unreviewed external capability.

## Publication policy

Publish reproducible methods, benchmark definitions, safe outputs and negative results where possible. Withhold or abstract details whose disclosure would materially increase real-world misuse capability. The objective is scientific utility, not operational exploit dissemination.

## Research integrity

A visually compelling activation map is not a result by itself. Claims about internal mechanisms require explicit controls, held-out evaluation, causal tests and replication. Exploratory analyses must be labelled as exploratory.
