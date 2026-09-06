# MATS Grants — Research Dossier & Safe Vertical Slice

**Working title:** *From Oversight-Sensitive Behaviour to Causal Representation Tests: A Reproducible Empirical Framework for the Science of Scheming*

**Target:** MATS Autumn 2026 — primarily the Apollo Research **Science of Scheming** stream.

**Status:** research dossier + runnable synthetic prototype.

> **Application-integrity notice:** MATS states that LLMs may not be used to write any part of an application unless a specific work test or form explicitly permits it. This repository is therefore an engineering/research aid, not a claim that its prose is eligible for direct submission. The applicant must independently produce and submit application answers in accordance with the current rules.

## Verified programme context

MATS currently describes Autumn 2026 as running from **September 28 to December 4, 2026**. The programme page describes a 10-week Berkeley/London programme and an optional funded extension pathway. citeturn252053search3

The Apollo Research Science of Scheming stream explicitly focuses on empirical study of oversight gaming, alignment faking and deceptive alignment, including controlled model-organism experiments and scaling questions. citeturn252053search4turn252053search6

## Research thesis

The project asks a deliberately narrow question:

> When a model behaves differently under different oversight conditions, can we distinguish ordinary context sensitivity from a reproducible oversight-sensitive effect, and can internal representations provide additional predictive or causal evidence?

The project does **not** assume that an observed behavioural anomaly is deceptive alignment, that a probe discovers a semantic "intention" feature, or that a detector is a universal circuit breaker.

## Evidence ladder

`behavioural effect → predictive internal signal → causal intervention → robustness → safety relevance`

Each stage has to earn the right to motivate the next. Negative results are first-class outcomes.

## Repository structure

```text
.
├── configs/
│   └── demo.yaml
├── docs/
│   ├── BUDGET.md
│   ├── CHANGELOG.md
│   ├── EVIDENCE.md
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

The demo uses a synthetic, harmless dataset. It does not train an agent, connect to external systems, execute generated actions, or target real-world assets.

## What the prototype demonstrates

The current vertical slice provides:

- deterministic synthetic model-organism data generation;
- matched oversight conditions;
- a measurable target behaviour;
- a held-out predictive baseline;
- AUROC/AUPRC metrics;
- reproducibility tests;
- configuration as code;
- GitHub Actions CI across Python versions.

This is a **research-infrastructure prototype**, not evidence that the scientific hypotheses are true.

## Research documentation

`docs/GRANT_APPLICATION_MASTER.md` is the main English application-writing research draft. `docs/GRANT_PROPOSAL.md` is the shorter proposal narrative. `docs/RESEARCH_PLAN.md` and `docs/METHODOLOGY.md` define the experimental standard. `docs/SAFETY.md` defines containment and stop conditions. `docs/EVIDENCE.md` tracks externally verifiable claims. `docs/BUDGET.md` separates programme facts from planning assumptions.

## Safety boundary

Only synthetic or explicitly approved contained environments should be used. Do not connect experiments to production credentials, personal accounts, real infrastructure, unrestricted external execution, real biological systems, financial targets or intrusion targets. Harmful-domain prompts should be abstracted into non-actionable placeholders wherever possible.

## Scientific standard

A candidate mechanism is not called explanatory merely because a probe correlates with behaviour. Stronger language requires held-out generalisation, causal intervention, negative controls and replication. See `docs/METHODOLOGY.md`.
