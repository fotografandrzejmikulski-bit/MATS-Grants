# Quality Audit — MATS Grants

## Purpose

This is the repository-level audit standard. It is designed to prevent the project from looking more mature than the evidence supports.

## Macro-level acceptance criteria

| Area | Acceptance criterion | Status |
|---|---|---|
| Programme fit | Claims match the current official MATS cohort and target stream | PASS |
| Scientific question | Narrow, falsifiable, empirically tractable | PASS |
| Experimental logic | Controls distinguish major competing explanations | PASS |
| Causal claims | Intervention is required before mechanistic language | PASS |
| Robustness | Held-out prompts/tasks/seeds/checkpoints where feasible | PASS |
| Safety | Contained, non-operational evaluation boundary | PASS |
| Reproducibility | Configuration, seeds, environment, tests and CI | PASS |
| Application integrity | LLM-use restriction is explicitly respected | PASS |
| Applicant data | Stored only where operationally necessary | PASS |
| Evidence provenance | Programme claims trace to current official sources | PASS |

## Micro-level review checklist

### Research claims

- Claims are labelled as observation, hypothesis, inference, or aspiration.
- Behavioural anomalies are not equated with deception.
- Probes are not treated as proof of semantic intention.
- Causal claims are not inferred from correlation alone.
- Negative controls are specified before confirmatory analysis.
- Held-out data are protected from iterative tuning.

### Statistics

- Primary outcomes are defined before analysis.
- Effect sizes accompany point estimates.
- Uncertainty is reported where sample size permits.
- Multiple comparisons are controlled or explicitly treated as exploratory.
- Seed sensitivity is measured rather than assumed negligible.
- Class imbalance is handled explicitly.

### Engineering

- No secrets are committed.
- Configuration is version-controlled.
- Tests cover deterministic generation and evaluation invariants.
- CI executes the minimum verification path described in the README.
- Invalid inputs fail clearly.
- Experimental outputs can be regenerated from declared configuration.

### Safety

- No production credentials or unrestricted network access are required.
- Harmful capability is represented abstractly wherever possible.
- Stop conditions are operationally explicit.
- Prototype claims are limited to the benchmark regime actually tested.

## Current limitation

The repository contains a safe synthetic vertical slice, not a frontier-model mechanistic-interpretability result. The strongest future upgrade is empirical validation in an appropriate contained environment, not more ambitious prose.
