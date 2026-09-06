# MATS Autumn 2026 — Application Research Master Draft

> **Important:** This document is a research-writing aid. MATS's Autumn 2026 application FAQ states that LLMs may not be used to write application content unless a specific work test or form explicitly permits it. The applicant must independently rewrite, verify and submit any application text in accordance with the current rules.

## Working title

**From Oversight-Sensitive Behaviour to Causal Representation Tests: A Reproducible Empirical Framework for the Science of Scheming**

## Project summary

I want to investigate a narrow empirical question: when a model behaves differently under different oversight conditions, can we distinguish ordinary context sensitivity from a reproducible change associated with oversight-sensitive behaviour, and can internal representations provide additional predictive or causal evidence?

The project deliberately avoids assuming that a behavioural anomaly is deceptive alignment. Instead, I will construct small, contained model-organism environments, measure behaviour under matched conditions, and then test whether candidate internal signals predict the effect on held-out tasks. Only candidate signals that survive robustness tests will be subjected to causal interventions. A final prototype will explore whether a validated signal can support a constrained monitoring or intervention mechanism without unacceptable capability loss.

This direction closely matches the Autumn 2026 Apollo Research Science of Scheming stream, which explicitly focuses on empirical study of oversight gaming, alignment faking and deceptive alignment, including controlled model-organism experiments and scaling questions. citeturn252053search4turn252053search6

## Why this project

The central scientific risk is confusing compelling behaviour with the mechanism that caused it. A model can appear deceptive because of prompt framing, reward artefacts, evaluator leakage, task-selection effects or ordinary strategic adaptation. My proposed contribution is therefore an evidence ladder: behavioural effect → predictive internal signal → causal intervention → robustness → safety relevance.

This creates a tractable path to useful negative results as well as positive ones. If candidate features fail held-out generalisation, the result still informs future evaluations by showing which apparent signatures are non-robust.

## Research questions

### RQ1 — Behavioural consistency
Can a controlled model organism exhibit a reproducible difference between monitored and weakly monitored conditions while matched for task family and difficulty?

### RQ2 — Internal signatures
Do activation-derived features predict oversight-sensitive behaviour on held-out prompts and tasks better than behavioural or prompt-only baselines?

### RQ3 — Causal structure
Does intervention on a candidate representation change the target behaviour in a reproducible direction, while preserving task capability and accounting for generic refusal effects?

### RQ4 — Robustness
Do candidate signals survive changes in prompt wording, task family, random seed, model checkpoint and evaluator configuration where feasible?

## Falsifiable hypotheses

**H1:** Controlled training/evaluation can produce a repeatable oversight-condition effect in a synthetic or otherwise contained model-organism environment.

**H2:** Some internal representation measurements predict this effect on held-out data above strong behavioural baselines.

**H3:** At least one candidate representation will show causal influence under intervention, rather than merely correlating with the target.

**H4:** A substantial fraction of initially attractive candidate signals will fail robustness or negative-control tests.

The project is successful even if H3 is rejected, provided the failure mode is measured rigorously and produces a reusable benchmark or methodological insight.

## Experimental strategy

### Stage 1 — Baselines

Establish capability, task difficulty, refusal and oversight-condition baselines using deterministic configurations and matched tasks.

### Stage 2 — Model-organism evaluation

Use only contained, synthetic or otherwise approved research environments. Generate multiple conditions and seeds. Lock train/validation/test splits before evaluating held-out data.

### Stage 3 — Representation analysis

Compare simple linear probes with sparse-feature methods where appropriate. Report AUROC/AUPRC, calibration, cross-prompt transfer, cross-task transfer and leakage controls. A probe is treated as a measurement instrument, not as proof of a semantic concept.

### Stage 4 — Causal tests

Ablate, patch or steer candidate representations in the contained benchmark. Measure target behaviour, task performance, refusal rate and collateral changes. Require replication before making mechanistic claims.

### Stage 5 — Constrained safety prototype

Only validated candidates are connected to a detector/intervention prototype. The prototype is framed as an experimental safety mechanism, not a universal deceptive-alignment detector or guaranteed circuit breaker.

## Expected deliverables

1. Reproducible benchmark and synthetic model-organism generator.
2. Evaluation harness with held-out robustness tests.
3. Representation/probe analysis pipeline.
4. Causal-intervention analysis scripts.
5. Safety-bounded prototype and documented failure modes.
6. Technical report or paper draft containing both positive and negative results.
7. Open-source code and experiment metadata where model/data licenses permit.

## Impact pathway

The immediate impact is methodological: improve the ability of alignment researchers to distinguish behavioural evidence from mechanistic evidence. A successful result could provide a reusable measurement strategy for oversight-sensitive behaviour; a negative result could prevent wasted effort on brittle signatures. The longer-term pathway is better empirical understanding of scheming dynamics and more reliable monitoring research.

## Feasibility

The repository already contains a runnable vertical slice using a harmless synthetic generator, deterministic evaluation, metrics, tests and continuous integration. The prototype is intentionally small: the scaling policy is evidence-gated, so larger models or more compute are introduced only when preceding experiments establish a reason to scale.

## Fit with MATS

The project is primarily empirical. It is intentionally aligned with the Autumn 2026 Apollo Research Science of Scheming agenda rather than claiming to reproduce a mentor's exact project. MATS describes the stream as empirical work on oversight gaming, alignment faking and deceptive alignment, with examples including controlled model organisms and scaling laws. citeturn252053search4

MATS's Autumn 2026 program runs from September 28 to December 4, 2026 and describes a 10-week Berkeley/London main program with optional funded extensions. citeturn252053search3

## Programme awareness

The applicant should tailor the final application to the exact MATS form and any work tests. MATS explicitly states that LLMs may not be used to write application content unless a specific work test or form permits it. citeturn252053search1

## What I would do differently after a null result

If no robust internal signal is found, I would not broaden the claim. I would publish the benchmark, identify which controls eliminate the apparent effect, and use the result to choose a narrower next experiment. This is a deliberate part of the project design rather than an afterthought.
