# MATS Grants — Research Dossier & Safe Vertical Slice

**Working title:** *From Oversight-Sensitive Behaviour to Causal Representation Tests: A Reproducible Empirical Framework for the Science of Scheming*

**Applicant:** Andrzej Mikulski  
**Target programme:** MATS Autumn 2026  
**Primary track:** Empirical  
**Primary stream:** Apollo Research — Science of Scheming  
**Status:** research dossier + runnable synthetic prototype

> **Application-integrity notice:** MATS currently states that LLMs may not be used to write any part of an application unless a specific work test or form explicitly permits it. This repository is therefore an engineering/research aid. The applicant must independently author, edit, fact-check and submit final application answers under the current rules. citeturn232071search3

## Current programme facts

MATS lists the Autumn 2026 programme as running from **September 28 to December 4, 2026**. It describes a 10-week main programme and an optional funded extension pathway. Applications close **September 6, 2026, end of day anywhere on Earth**. citeturn232071search4

The Apollo Research **Science of Scheming** stream explicitly focuses on oversight gaming, alignment faking and deceptive alignment, including controlled model-organism experiments and questions about scaling behaviour. citeturn232071search1

## Research thesis

The project asks a deliberately narrow question:

> When a model behaves differently under different oversight conditions, can we distinguish ordinary context dependence from a reproducible oversight-sensitive effect, and can internal representations provide additional predictive or causal evidence?

The project does **not** assume that a behavioural anomaly is deceptive alignment, that a probe discovers a semantic intention, or that a detector is a universal circuit breaker.

## Evidence ladder

`behavioural effect → predictive internal signal → causal intervention → robustness → safety relevance`

Each stage must earn the right to motivate the next. Negative results are first-class outcomes.

## Repository structure

```text
.
├── configs/
│   └── demo.yaml
├── docs/
│   ├── APPLICANT_PROFILE.md
│   ├── BUDGET.md
│   ├── CHANGELOG.md
│   ├── EVIDENCE.md
│   ├── EXPERIMENT_MATRIX.md
│   ├── GRANT_APPLICATION_MASTER.md
│   ├── GRANT_PROPOSAL.md
│   ├── METHODOLOGY.md
│   ├── RESEARCH_PLAN.md
│   └── SAFETY.md
├── scripts/
│   └── run_demo.py
├── src/
│   └── mats_research/
│       ├── __init__.py
│       ├── evaluate.py
│       └── synthetic.py
├── tests/
│   └── test_vertical_slice.py
├── pyproject.toml
└── README.md
```

## Run the vertical slice

```bash
python -m pip install -e ".[test]"
pytest -q
python scripts/run_demo.py
```

The demo uses a synthetic, harmless dataset. It does not train or deploy an agent, connect models to external systems, execute generated actions, or target real-world assets.

## What the prototype demonstrates

- deterministic synthetic data generation with schema validation;
- matched oversight conditions and a known synthetic data-generating process;
- behavioural effect measurement;
- held-out linear predictive baseline;
- AUROC/AUPRC reporting;
- a shuffled-label negative control;
- reproducibility and validation tests;
- configuration as code;
- continuous integration across supported Python versions.

This is **research infrastructure**, not evidence that the scientific hypotheses are true.

## Research documentation

`docs/GRANT_APPLICATION_MASTER.md` is the main English application-writing research draft. `docs/GRANT_PROPOSAL.md` is the shorter narrative. `docs/RESEARCH_PLAN.md`, `docs/METHODOLOGY.md` and `docs/EXPERIMENT_MATRIX.md` define the experimental standard. `docs/SAFETY.md` defines containment and stop conditions. `docs/EVIDENCE.md` tracks externally verifiable claims. `docs/BUDGET.md` separates programme facts from planning assumptions. `APPLICANT_PROFILE.md` contains administrative applicant metadata.

## Safety boundary

Only synthetic or explicitly approved contained environments should be used. Do not connect experiments to production credentials, personal accounts, real infrastructure, unrestricted external execution, real biological systems, financial targets or intrusion targets. Harmful-domain prompts should be abstracted into non-actionable placeholders wherever possible.

## Scientific standard

A candidate mechanism is not called explanatory merely because a probe correlates with behaviour. Stronger language requires held-out generalisation, causal intervention, negative controls and replication. See `docs/METHODOLOGY.md`.
