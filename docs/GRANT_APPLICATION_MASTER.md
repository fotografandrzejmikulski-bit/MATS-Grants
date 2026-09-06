# MATS Autumn 2026 — Application Research Master Draft

> **Application-integrity notice:** MATS's Autumn 2026 FAQ states that LLMs may not be used to write application content unless a specific work test or form explicitly permits it. This document is therefore a research-writing aid and must not be submitted verbatim where prohibited. The applicant must independently author, verify and submit the final application.

## Working title

**From Oversight-Sensitive Behaviour to Causal Representation Tests: A Reproducible Empirical Framework for the Science of Scheming**

## Project summary

I want to study a narrow empirical question: when a model behaves differently under different oversight conditions, can we distinguish ordinary context sensitivity from a reproducible oversight-sensitive effect, and can internal representations provide additional predictive or causal evidence?

Rather than assuming that an anomaly is deceptive alignment, I will construct small, contained model-organism environments, measure behaviour under matched conditions, and test whether candidate internal signals predict the effect on held-out data. Only signals that survive robustness checks will be subjected to causal interventions. A final stage will explore whether a validated signal can support a constrained monitoring or intervention mechanism without unacceptable capability loss.

This direction is closely aligned with MATS's Autumn 2026 Apollo Research Science of Scheming stream, which explicitly describes empirical work on oversight gaming, alignment faking and deceptive alignment, including controlled model-organism experiments and scaling questions. citeturn252053search4turn252053search6

## Research motivation

The main methodological failure mode I want to address is confusing compelling behaviour with the mechanism that caused it. Apparent deception can arise from prompt framing, reward artefacts, evaluator leakage, task-selection effects or ordinary strategic adaptation. My proposed contribution is an evidence ladder:

**behavioural effect → predictive internal signal → causal intervention → robustness → safety relevance**

Each stage must earn the next. Negative results are first-class outcomes.

## Research questions

### RQ1 — Behavioural consistency
Can a contained model organism exhibit a reproducible difference between stronger and weaker oversight conditions while task family and difficulty are matched?

### RQ2 — Internal signatures
Do activation-derived features predict the target behaviour on held-out prompts and tasks better than prompt-only and behavioural baselines?

### RQ3 — Causal structure
Does intervention on a candidate representation change the target behaviour in the expected direction while preserving task capability and controlling for generic refusal effects?

### RQ4 — Robustness
Do candidate signals survive changes in prompt wording, task family, random seed, evaluator configuration and, where feasible, model checkpoint?

## Falsifiable hypotheses

**H1:** A contained model organism can exhibit a repeatable oversight-condition effect.

**H2:** Some internal representation measurements predict that effect on held-out data above strong behavioural baselines.

**H3:** At least one candidate representation shows causal influence under controlled intervention.

**H4:** A substantial fraction of initially attractive candidate signals fail robustness or negative-control tests.

Rejection of H3 is a scientifically useful outcome. The project does not require demonstrating a universal detector of deceptive alignment.

## Experimental strategy

### Stage 1 — Baselines

Establish capability, task difficulty, refusal and oversight-condition baselines using deterministic configurations and matched tasks.

### Stage 2 — Model-organism evaluation

Use synthetic or explicitly approved contained environments. Generate multiple conditions and random seeds. Freeze train/validation/test splits before inspecting held-out outcomes.

### Stage 3 — Representation analysis

Compare simple linear probes with sparse-feature methods where justified. Report AUROC/AUPRC, calibration, cross-prompt transfer, cross-task transfer and leakage controls. A probe is a measurement instrument; it is not automatically a semantic label for an intention or goal.

### Stage 4 — Causal intervention

Ablate, patch or steer candidate representations in the contained benchmark. Measure target behaviour, task capability, refusal rate and collateral changes. Require replication before making mechanistic claims.

### Stage 5 — Constrained safety prototype

Only validated candidates progress to a detector/intervention prototype. The prototype is a research instrument with explicit false-positive, false-negative, distribution-shift and capability-degradation evaluation. It is not presented as a universal circuit breaker.

## Experimental design

The minimum confirmatory design should cover two oversight conditions, at least four task families, at least four prompt templates per family, and at least three random seeds, with task difficulty matched within family. Where feasible, a second checkpoint should be used to test transfer.

Primary analyses should be frozen before confirmatory evaluation. Record the primary metric, comparison, splits, exclusion rules, seeds, minimum effect of interest, stopping/scaling rule, negative controls and intervention specification.

## Evidence standard

A behavioural difference supports a behavioural claim, not a claim about deception. A predictive probe supports the presence of predictive information, not semantic interpretability. A successful intervention supports causal influence under that intervention, not a universal mechanism. Strong claims require robustness and replication.

Negative controls include shuffled labels, randomized feature directions, matched task difficulty, generic refusal/safety baselines, prompt-only predictors and held-out prompt/task families where feasible.

## Deliverables

1. Reproducible benchmark and synthetic model-organism generator.
2. Evaluation harness with held-out robustness tests.
3. Representation/probe analysis pipeline.
4. Causal-intervention analysis code.
5. Safety-bounded monitoring/intervention prototype if the evidence permits.
6. Technical report or paper draft containing positive and negative results.
7. Reproducible experiment metadata and open-source tooling where licensing permits.

## Milestones

**Weeks 1–2:** reproduce baselines, lock the environment, define metrics and build the benchmark.

**Weeks 3–4:** validate model-organism conditions, quantify behavioural effects and run initial robustness checks.

**Weeks 5–7:** representation analysis, probe comparison, held-out generalisation and candidate selection.

**Weeks 8–9:** causal interventions, replication and collateral-effect measurement.

**Week 10:** consolidate results, document failures, package reproducible artefacts and define the follow-on research agenda.

MATS's current Autumn 2026 page states that the programme runs from September 28 to December 4, 2026. citeturn252053search3

## Theory of impact

The immediate impact is methodological: improve the ability of alignment researchers to distinguish behavioural evidence from mechanistic evidence. A positive result would provide a reusable route from observed oversight sensitivity to causal representation tests. A negative result would identify brittle signatures and reduce the chance that prompt-sensitive artefacts are treated as evidence of deceptive intent.

The longer-term contribution would be better empirical understanding of scheming dynamics and more reliable monitoring research.

## Feasibility

The repository includes a runnable synthetic vertical slice with deterministic generation, matched oversight conditions, held-out evaluation, AUROC/AUPRC metrics, automated tests, configuration as code and continuous integration. The prototype is intentionally small and harmless. Scaling is evidence-gated rather than assumed.

## Fit with MATS

This is primarily an empirical project. It is intentionally scoped as a tractable contribution to the Apollo Science of Scheming agenda rather than an attempt to claim ownership of a mentor's project. MATS explicitly identifies controlled model organisms, oversight gaming, alignment faking, deceptive alignment and scaling questions as relevant directions for this stream. citeturn252053search4

## Application-integrity constraint

MATS currently states that LLMs may not be used to write any part of the application unless a specific work test or form explicitly permits it. citeturn252053search1 Any final submission must therefore be independently authored and checked by the applicant under the applicable MATS rules.
