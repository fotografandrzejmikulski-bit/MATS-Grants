# MATS Autumn 2026 — Application Research Master Draft

> **Application-integrity warning:** MATS currently states that LLMs may not be used to write any part of an application unless a specific work test or form explicitly permits it. This document is therefore a research and verification aid, not a submission-ready answer set. The applicant must independently author, edit, fact-check and submit final responses under the live MATS rules. citeturn621132search1turn621132search9

## Applicant

**Andrzej Mikulski**  
mojealterego21@gmail.com  
+48 455 575 337

## Target positioning

**Programme:** MATS Autumn 2026  
**Primary track:** Empirical  
**Primary stream:** Apollo Research — Science of Scheming

MATS currently describes the Apollo Science of Scheming stream as empirical research on oversight gaming, alignment faking and deceptive alignment, including controlled model-organism experiments and questions about scaling scheming-relevant behaviour. citeturn621132search0turn621132search2

## Working title

**From Oversight-Sensitive Behaviour to Causal Representation Tests: A Reproducible Empirical Framework for the Science of Scheming**

## Research question

When a model behaves differently under different oversight conditions, can we distinguish ordinary context dependence from a reproducible oversight-sensitive effect, and can internal representations provide additional predictive or causal evidence?

## Core thesis

I would treat this as a measurement problem before treating it as a deception problem. A behavioural anomaly can arise from prompt framing, task difficulty, evaluator leakage, reward artefacts, selection effects or generic refusal behaviour. The project therefore follows an evidence ladder:

**behavioural effect → predictive internal signal → causal intervention → robustness → safety relevance.**

The scientific target is not to prove a dramatic story quickly. It is to identify which explanations survive controlled tests.

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

Rejecting H3 is a valid scientific result. The project does not require demonstrating a universal deceptive-alignment detector or production-grade circuit breaker.

## Experimental strategy

### Phase 1 — Baselines

Establish capability, task difficulty, refusal and oversight-condition baselines. Freeze the measurement protocol before substantive screening.

### Phase 2 — Model-organism evaluation

Use synthetic or explicitly approved contained environments. Vary task families, prompt templates and random seeds. Freeze train/validation/test groups before looking at held-out outcomes, using group-aware partitioning where latent templates could leak.

### Phase 3 — Representation analysis

Start with simple predictors. Compare behavioural and prompt-only baselines with activation-derived linear probes and, where justified, sparse-feature representations. Report AUROC/AUPRC, calibration, transfer, leakage controls and uncertainty. A probe is a measurement instrument, not proof of an internal semantic concept.

### Phase 4 — Causal testing

Intervene minimally on shortlisted representations using ablation, patching or steering within the contained benchmark. Measure target behaviour, capability, refusal and collateral effects. Require replication before making mechanistic claims.

### Phase 5 — Constrained safety prototype

Only candidates that pass behavioural, predictive, robustness and causal gates progress to a detector/intervention prototype. Evaluate false positives, false negatives, distribution shift and capability degradation. The prototype is explicitly a research instrument, not a universal safety guarantee.

## Controls

The minimum negative-control suite is:

- prompt-only predictors;
- matched task-difficulty controls;
- shuffled-label or randomized-feature controls;
- generic refusal/safety baselines;
- held-out prompt templates;
- held-out task families;
- sham interventions where causal tests are performed.

## Statistical discipline

Primary metrics and decision gates should be recorded before confirmatory analysis. Report effect sizes, sample counts and uncertainty intervals. When many candidate features or interventions are screened, distinguish exploratory discovery from confirmatory testing and disclose the screening procedure. Null results and failed hypotheses are retained as first-class outputs.

## Scaling policy

Start with the smallest model and environment that can answer the next question. Increase model size, trajectory count, representation width or context length only when the preceding evidence gate passes. This makes compute conditional on information gained, rather than treating maximum spend as an objective.

## Deliverables

1. Reproducible synthetic model-organism benchmark.
2. Behavioural evaluation harness with held-out robustness tests.
3. Representation/probe analysis pipeline.
4. Causal-intervention evaluation code.
5. Safety-bounded monitoring/intervention prototype, only if evidence justifies it.
6. Technical report or paper draft containing positive and negative results.
7. Reproducibility metadata and safe open-source tooling where licensing permits.

## Ten-week execution frame

**Weeks 1–2:** reproduce baseline; lock environment; define metrics and analysis gates.  
**Weeks 3–4:** validate model-organism conditions; quantify behavioural effects; run initial robustness checks.  
**Weeks 5–7:** representation analysis; held-out prediction; candidate selection.  
**Weeks 8–9:** causal interventions; robustness; replication; collateral-effect measurement.  
**Week 10:** consolidate findings; document failures; package safe artifacts; define follow-on work.

## Fit with MATS

The project is primarily empirical and deliberately narrow. Its strongest fit is the Apollo Science of Scheming stream because that stream explicitly names oversight gaming, alignment faking, deceptive alignment, controlled model organisms and scaling questions. citeturn621132search0turn621132search2

The proposed contribution is not to assume scheming has already been demonstrated. It is to improve the evidential chain from an observed oversight-sensitive effect to a representation-level hypothesis and, only where justified, to causal evidence.

## Feasibility

The repository contains a safe synthetic vertical slice with deterministic generation, schema validation, held-out prediction, negative controls, tests, configuration-as-code and continuous integration. This demonstrates experimental infrastructure and implementation discipline; it is not presented as evidence that the scientific hypotheses are true in frontier models.

## Safety and dual-use

The research should remain in synthetic or explicitly approved contained environments. No production credentials, unrestricted external execution, real biological systems, financial targets or intrusion targets are required. Safety-relevant behaviour should be represented using abstract, non-actionable tasks whenever possible. Stop conditions are defined in `docs/SAFETY.md`.

## Honest failure criteria

The project is allowed to fail. If an apparent effect disappears under held-out tasks, changed prompts, negative controls or replication, the result should be reported as evidence against that candidate explanation. A null result should narrow the claim rather than trigger uncontrolled escalation of complexity or compute.

## Administrative note

MATS's current materials should be treated as the authoritative source for dates, application stages, funding, eligibility, logistics and any submission-specific instructions. The live application form outranks this repository.
