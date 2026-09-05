# Detecting and Mitigating Deceptive Behaviour in Advanced Language Models

## Executive summary

This project proposes an empirical investigation of deceptive or oversight-sensitive behaviour in language models using controlled model organisms, behavioural evaluations, activation-level analysis and causal interventions. The core objective is narrower than building a universal "neural circuit breaker": first establish whether a reproducible internal signal exists, whether it predicts behaviour out of distribution, and whether interventions on that signal change behaviour causally without unacceptable capability degradation.

The project is designed around four principles: falsifiability, containment, causal evidence, and fast iteration. The research will begin with small, reproducible model organisms and scale only when earlier stages produce robust evidence.

## Research questions

### RQ1 — Behavioural consistency
Can controlled training or prompting produce a reproducible gap between behaviour under strong versus weak oversight conditions, while holding task difficulty and capability requirements approximately constant?

### RQ2 — Internal signatures
Do activation-level features or learned representations predict the oversight-sensitive behaviour better than behavioural proxies alone?

### RQ3 — Causality
Do interventions on candidate representations change the probability or severity of the target behaviour, with appropriate controls and without merely changing general refusal or task competence?

### RQ4 — Robustness
Do candidate signatures survive changes in prompt wording, task family, random seed, model checkpoint, and evaluator setup?

## Hypotheses

**H1.** A deliberately constructed model organism can exhibit a measurable and repeatable difference between monitored and weakly monitored conditions.

**H2.** At least some behavioural variance can be predicted from internal representations above strong behavioural baselines.

**H3.** A subset of candidate representation directions will demonstrate causal influence in intervention experiments.

**H4.** Many apparently striking signals will fail robustness tests; these negative results are first-class outcomes.

## Experimental design

### Phase 1 — Baselines and model organisms

Construct contained toy environments and benign proxy tasks in which the target variable is observable and the failure mode can be measured without requiring deployment against real systems. Establish capability, reward, and refusal baselines before introducing any adversarial manipulation.

### Phase 2 — Behavioural evaluations

Evaluate multiple oversight conditions, task families, seeds and prompt templates. Pre-register primary metrics where practical. Use held-out prompts and tasks to separate genuine generalisation from prompt-specific imitation.

### Phase 3 — Mechanistic analysis

Collect activations from selected layers and train sparse feature dictionaries / probes where justified. Compare linear probes, SAE-based representations and simpler behavioural baselines. Report reconstruction error, probe calibration, leakage and out-of-distribution performance rather than treating a probe as evidence of a human-interpretable concept by itself.

### Phase 4 — Causal intervention

Patch, ablate or steer candidate representations in controlled settings. Measure target-behaviour change, capability change, refusal change and collateral effects. A candidate mechanism is considered promising only when intervention results replicate and survive negative controls.

### Phase 5 — Safety mechanism prototype

Only after a causal signal has survived replication will a constrained detector/intervention prototype be tested. The prototype is a research instrument, not a claim of universal pre-emption. Evaluation includes false positives, false negatives, distribution shift and capability degradation.

## Success criteria

The project succeeds scientifically if it produces one or more of:

- a reproducible behavioural model organism with well-defined controls;
- an internal feature that predicts the target behaviour on held-out conditions;
- causal evidence connecting that feature to behaviour;
- a robust negative result showing that a tempting interpretation does not generalise;
- a reusable benchmark, dataset specification, evaluation harness or open-source analysis tool.

The project does **not** require demonstrating a universal detector of deceptive alignment within the fellowship period.

## Milestones

**Weeks 1–2:** reproduce baselines; lock environments; establish metrics and safety controls.

**Weeks 3–4:** generate and validate model-organism conditions; run first robustness checks.

**Weeks 5–7:** representation analysis and probe comparison; identify candidate mechanisms.

**Weeks 8–9:** causal interventions and replication; measure collateral effects.

**Weeks 10–12:** consolidate results, publish code and negative results, prepare follow-on research plan.

## Positioning within MATS

The project is primarily empirical and intersects with interpretability, evaluations, oversight and the science of scheming. MATS's Autumn 2026 program describes an Apollo Research stream focused on empirically studying oversight gaming, alignment faking and deceptive alignment, including controlled model-organism experiments and scaling of misaligned behaviour. citeturn213781search6

MATS also describes an Autumn 2026 ARC stream whose agenda is more theoretically oriented and emphasises mathematical maturity; this proposal should therefore be presented as empirical first, with theory used to sharpen hypotheses rather than as a claim that the project belongs to ARC's core agenda. citeturn213781search3
