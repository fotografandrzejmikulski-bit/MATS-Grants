# MATS Autumn 2026 — Application Research Master Draft

> **Application-integrity warning:** MATS states that LLMs may not be used to write any part of an application unless a specific work test or form explicitly permits it. This document is therefore a research and verification draft. The applicant must independently author, edit, fact-check and submit final responses in accordance with the current MATS rules.

## Applicant

**Andrzej Mikulski**  
mojealterego21@gmail.com  
+48 455 575 337

## Target

**Programme:** MATS Autumn 2026  
**Primary track:** Empirical  
**Primary stream:** Apollo Research — Science of Scheming

MATS currently lists the Autumn 2026 programme as running from **September 28 to December 4, 2026**. The programme is described as a 10-week main programme with an optional funded extension pathway. citeturn232071search4

The Apollo Science of Scheming stream is explicitly focused on empirically studying oversight gaming, alignment faking and deceptive alignment, including controlled model-organism experiments and questions about how scheming-relevant behaviour scales. citeturn232071search1

## Working title

**From Oversight-Sensitive Behaviour to Causal Representation Tests: A Reproducible Empirical Framework for the Science of Scheming**

## Project summary

I propose to study a narrow empirical question: when a model behaves differently under different oversight conditions, can we distinguish ordinary context dependence from a reproducible oversight-sensitive effect, and can internal representations provide additional predictive or causal evidence?

The project deliberately avoids assuming that a behavioural anomaly is deceptive alignment. I will begin with small, contained model-organism environments, measure behaviour under matched conditions, and test whether candidate internal signals generalise to held-out prompts and tasks. Only candidates that survive robustness checks will be subjected to causal interventions. A final prototype will test whether a validated signal can support constrained monitoring or intervention without unacceptable capability loss.

## Why this question matters

The central methodological danger is confusing a striking output with the mechanism that produced it. Oversight-sensitive behaviour can be confounded by prompt framing, task difficulty, evaluator leakage, reward artefacts, distribution shift or generic refusal behaviour. A useful contribution therefore needs an evidence ladder:

**behavioural effect → predictive internal signal → causal intervention → robustness → safety relevance.**

This structure makes negative results scientifically valuable. A candidate that disappears under held-out evaluation or a negative control is evidence against a tempting interpretation and can prevent future researchers from mistaking brittle correlations for mechanisms.

## Research questions

### RQ1 — Behavioural consistency
Can a contained model organism exhibit a reproducible difference between stronger and weaker oversight conditions while task family and difficulty are matched?

### RQ2 — Internal signatures
Do activation-derived features predict the target behaviour on held-out prompts and task families better than prompt-only and behavioural baselines?

### RQ3 — Causal structure
Does intervention on a candidate representation change the target behaviour in the predicted direction while preserving task capability and controlling for generic refusal effects?

### RQ4 — Robustness
Do candidate signals survive changes in prompt wording, task family, random seed, evaluator configuration and, where feasible, model checkpoint?

## Falsifiable hypotheses

**H1:** A contained model organism can exhibit a repeatable oversight-condition effect.

**H2:** Some internal representation measurements predict that effect on held-out data above strong behavioural baselines.

**H3:** At least one candidate representation shows causal influence under controlled intervention.

**H4:** A substantial fraction of initially attractive candidate signals fail robustness or negative-control tests.

Rejecting H3 is a valid scientific outcome. The project does not require demonstrating a universal deceptive-alignment detector.

## Experimental design

### Phase 1 — Baselines

Establish capability, task difficulty, refusal and oversight-condition baselines. Use deterministic configurations and matched task families before introducing any manipulation.

### Phase 2 — Model-organism evaluation

Use synthetic or explicitly approved contained environments. Generate multiple seeds, task families and prompt templates. Freeze train/validation/test splits before inspecting held-out results.

### Phase 3 — Representation analysis

Compare simple linear probes with sparse-feature methods where justified. Report AUROC/AUPRC, calibration, held-out transfer, leakage controls and representation stability. A probe is a measurement instrument; it is not by itself evidence that the model has a human-interpretable internal intention.

### Phase 4 — Causal testing

Apply minimal ablations, activation patching or steering to candidate representations in the contained benchmark. Measure target behaviour, task performance, refusal rate and collateral effects. Require replication before making mechanistic claims.

### Phase 5 — Constrained safety prototype

Only validated candidates progress to a detector/intervention prototype. The prototype is explicitly experimental and bounded. It is evaluated for false positives, false negatives, distribution shift and capability degradation rather than presented as a universal circuit breaker.

## Analysis and statistical discipline

The analysis distinguishes exploratory from confirmatory work. Primary metrics and decision gates should be written down before inspecting held-out outcomes. Results are stratified by task family and condition where sample size permits. Effect sizes and uncertainty intervals should accompany point estimates. Multiple seeds and materially changed nuisance variables should be used for replication where feasible.

The core negative controls are:

- prompt-only predictors;
- matched task-difficulty controls;
- shuffled-label or randomized-feature baselines;
- generic refusal/safety baselines;
- held-out prompt templates;
- held-out task families.

## Scaling policy

Start with the smallest model and environment capable of testing the next hypothesis. Increase model size, trajectory count or representation width only after the preceding stage meets a predefined evidence threshold. This makes compute an evidence-gated resource rather than an unconditional budget target.

## Deliverables

1. Reproducible synthetic model-organism benchmark.
2. Behavioural evaluation harness with held-out robustness tests.
3. Representation/probe analysis pipeline.
4. Causal-intervention evaluation code.
5. Safety-bounded monitoring/intervention prototype, if justified by evidence.
6. Technical report or paper draft containing positive and negative results.
7. Reproducibility metadata and open-source tooling where licensing and safety permit.

## Ten-week execution plan

**Weeks 1–2:** reproduce baseline, lock environment, define metrics and pre-analysis criteria.

**Weeks 3–4:** validate model-organism conditions and quantify behavioural effects.

**Weeks 5–7:** representation analysis, held-out prediction and candidate selection.

**Weeks 8–9:** causal interventions, robustness checks and replication.

**Week 10:** consolidate findings, document failures, release safe artifacts and define follow-on work.

## Fit with the Apollo stream

The fit is direct and deliberately narrow. MATS describes Apollo Research's Autumn 2026 Science of Scheming stream as empirical work on oversight gaming, alignment faking and deceptive alignment, with controlled model-organism experiments and scaling questions among its stated directions. citeturn232071search1

The project is designed to contribute to this agenda without assuming the conclusion in advance. Its strongest value is a disciplined bridge between behavioural evaluation and mechanistic evidence: first establish a reliable phenomenon, then determine whether internal measurements add information, then ask whether those measurements are causally relevant.

## Fit with MATS expectations

MATS's current programme material emphasises fast empirical iteration, strong experimental design, attention to confounders and baselines, and the ability to implement and debug evaluation pipelines. citeturn232071search5 The repository is therefore intentionally structured around a small runnable vertical slice, explicit tests, configuration-as-code, reproducibility checks and evidence-gated scaling.

## Feasibility and prototype evidence

The repository contains a harmless synthetic vertical slice with deterministic data generation, matched oversight conditions, held-out predictive evaluation, AUROC/AUPRC metrics, negative-control tests and CI. This demonstrates engineering discipline and experimental scaffolding; it is not presented as empirical evidence that deceptive alignment or scheming exists in the synthetic generator.

## Safety and dual-use boundary

All initial experiments remain in synthetic or sandboxed environments. No production credentials, real-world control systems, real biological systems, real financial targets or unrestricted external execution are required. Safety-relevant behaviours should be represented with abstract non-actionable tasks whenever possible. Stop conditions are defined in `docs/SAFETY.md`.

## Honest failure criteria

The project will explicitly record and analyse null results. A candidate mechanism is not promoted merely because it is interesting. If the apparent signal disappears under held-out tasks, altered prompts, negative controls or replication, the result will be treated as evidence against that candidate explanation.

## Programme compliance

MATS currently states that LLMs may not be used to write application content unless a specific work test or form explicitly permits it, and that use may be monitored. citeturn232071search3 Any submission must therefore be independently authored and verified by the applicant under the current application rules.
