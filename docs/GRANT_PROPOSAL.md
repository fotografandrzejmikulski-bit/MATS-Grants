# From Oversight-Sensitive Behaviour to Causal Representation Tests

## Executive summary

I propose an empirical study of oversight-sensitive behaviour in language models. The central question is whether a reproducible behavioural difference between matched oversight conditions can be distinguished from ordinary context dependence, and whether internal representations provide additional predictive or causal evidence.

The project deliberately avoids beginning with the assumption that an observed anomaly is deceptive alignment. Instead, it follows an evidence ladder: **behavioural effect → predictive internal signal → causal intervention → robustness → safety relevance**. Each stage has to pass explicit controls before the project scales.

The work is strongly aligned with the Autumn 2026 Apollo Research Science of Scheming stream, which MATS describes as empirical research on oversight gaming, alignment faking and deceptive alignment, including controlled model-organism experiments and scaling questions. citeturn252053search4turn252053search6

## Research questions

### RQ1 — Behavioural consistency
Can a contained model organism exhibit a reproducible difference between stronger and weaker oversight conditions while task family and difficulty are matched?

### RQ2 — Internal signatures
Do activation-derived features predict the target behaviour on held-out prompts and tasks better than prompt-only and behavioural baselines?

### RQ3 — Causal structure
Does intervention on a candidate representation change the target behaviour in the expected direction, while preserving task capability and controlling for generic refusal effects?

### RQ4 — Robustness
Do candidate signals survive changes in prompt wording, task family, random seed, evaluator configuration and, where feasible, model checkpoint?

## Falsifiable hypotheses

**H1:** A contained model organism can exhibit a repeatable oversight-condition effect.

**H2:** Some internal representation measurements predict that effect on held-out data above strong behavioural baselines.

**H3:** At least one candidate representation shows causal influence under controlled intervention.

**H4:** A substantial fraction of initially attractive candidate signals fail robustness or negative-control tests.

Rejection of H3 is a scientifically useful outcome. The project does not require demonstrating a universal detector or circuit breaker.

## Experimental design

### Phase 1 — Baselines and model organisms

Use synthetic or explicitly approved contained environments. Establish capability, difficulty, refusal and oversight-condition baselines before introducing any manipulation. Use matched tasks so that changes cannot be explained simply by task difficulty.

### Phase 2 — Behavioural evaluation

Run multiple seeds, task families and prompt templates. Define train/validation/test splits before inspecting held-out outcomes. Measure target-behaviour rate, oversight-condition effect size, capability, refusal and calibration.

### Phase 3 — Representation analysis

Collect activations from selected layers and compare simple linear probes with sparse-feature methods when justified. Report AUROC/AUPRC, calibration, cross-prompt transfer, cross-task transfer and leakage controls. Treat probes as measurement instruments, not proof of semantic concepts.

### Phase 4 — Causal intervention

Intervene on candidate representations in the contained benchmark using minimal ablations, patching or steering. Measure target behaviour, task capability, refusal and collateral effects. Require replication before describing a candidate as mechanistically explanatory.

### Phase 5 — Constrained safety prototype

Only validated candidates progress to a detector/intervention prototype. The prototype is a research instrument with explicit false-positive, false-negative, distribution-shift and capability-degradation evaluation. It is not presented as universal pre-emption.

## Methodological standard

The project distinguishes correlation from causation and exploratory from confirmatory analysis. Negative controls include shuffled labels, randomized features, task-difficulty matching, generic refusal baselines, prompt-only predictors and held-out task families where feasible.

A strong result must survive at least one meaningful replication with altered nuisance variables. A weak or non-replicating result is recorded rather than promoted through increasingly elaborate interpretations.

## Deliverables

1. A reproducible benchmark and synthetic model-organism generator.
2. An evaluation harness with held-out robustness tests.
3. Representation/probe analysis code.
4. Causal-intervention analysis code.
5. A safety-bounded monitoring/intervention prototype if the evidence permits.
6. A technical report or paper draft containing positive and negative results.
7. Reproducible experiment metadata and open-source tooling where licensing permits.

## Milestones

**Weeks 1–2:** reproduce baselines, lock the environment, define metrics, build the initial benchmark.

**Weeks 3–4:** validate model-organism conditions, quantify behavioural effects, run first robustness checks.

**Weeks 5–7:** representation analysis, probe comparison, held-out generalisation and candidate selection.

**Weeks 8–9:** causal interventions, replication and collateral-effect measurement.

**Week 10:** consolidate results, document failures and prepare the follow-on research agenda.

MATS's current Autumn 2026 programme page states that the programme runs from September 28 to December 4, 2026. citeturn252053search3

## Fit with MATS

This project is primarily empirical. It is intentionally framed as a tractable subproblem within the Apollo Science of Scheming agenda rather than as a claim to reproduce a mentor's exact project. MATS identifies controlled model organisms, oversight gaming, alignment faking, deceptive alignment and scaling questions as relevant directions for the stream. citeturn252053search4

## Theory of impact

The immediate contribution is a more reliable methodology for separating behaviour from mechanism. A positive result would provide a reusable path from observed oversight sensitivity to causal representation tests. A negative result would identify brittle signatures and help prevent researchers from treating prompt-sensitive artefacts as evidence of deceptive intent.

The longer-term objective is better empirical understanding of scheming dynamics and more reliable monitoring research, not a single universal detector.

## Feasibility and prototype status

The repository contains a runnable synthetic vertical slice: deterministic data generation, matched oversight conditions, held-out evaluation, AUROC/AUPRC metrics, tests and CI. The prototype is intentionally harmless and does not connect models to external systems.

## Application-integrity constraint

MATS currently states that LLMs may not be used to write any part of the application unless a specific work test or form explicitly permits it. citeturn252053search1 This repository therefore serves as a research, verification and engineering dossier. Any final application submission must be independently authored and checked by the applicant in accordance with MATS rules.
