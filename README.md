# MATS Grants — Research Dossier & Safe Vertical Slice

**Working title:** *From Oversight-Sensitive Behaviour to Causal Representation Tests: A Reproducible Empirical Framework for the Science of Scheming*  
**Applicant:** Andrzej Mikulski  
**Target:** MATS Autumn 2026 — primarily the Apollo Research **Science of Scheming** stream  
**Status:** research dossier + runnable synthetic prototype

> **Application-integrity notice:** MATS currently states that LLMs may not be used to write any part of an application unless a specific work test or form explicitly permits it. This repository is therefore a research, verification and engineering aid. The applicant must independently author, edit, fact-check and submit final application answers under the current rules. citeturn621132search1turn621132search9

## Current programme fit

The current MATS Autumn 2026 materials identify Apollo Research — Science of Scheming as an **Empirical** stream focused on oversight gaming, alignment faking and deceptive alignment, including controlled model-organism experiments and empirical scaling questions. citeturn621132search0turn621132search2

The project is framed as a narrow empirical subproblem within that agenda rather than as an attempt to reproduce the entire stream.

## Research thesis

> When a model behaves differently under different oversight conditions, can we distinguish ordinary context dependence from a reproducible oversight-sensitive effect, and can internal representations provide additional predictive or causal evidence?

The project does **not** assume that a behavioural anomaly is deceptive alignment, that a probe discovers a semantic intention, or that a detector is a universal circuit breaker.

## Evidence ladder

`behavioural effect → predictive internal signal → causal intervention → robustness → safety relevance`

Each stage must earn the right to motivate the next. Negative results are first-class research outputs.

## Repository structure

```text
.
├── .github/workflows/ci.yml
├── configs/demo.yaml
├── docs/
│   ├── APPLICANT_PROFILE.md
│   ├── APPLICATION_METADATA.md
│   ├── BUDGET.md
│   ├── CHANGELOG.md
│   ├── COMPUTE_AND_REPRODUCIBILITY.md
│   ├── EVIDENCE.md
│   ├── EXPERIMENT_MATRIX.md
│   ├── GRANT_APPLICATION_MASTER.md
│   ├── GRANT_PROPOSAL.md
│   ├── METHODOLOGY.md
│   ├── QUALITY_AUDIT.md
│   ├── RESEARCH_PLAN.md
│   └── SAFETY.md
├── scripts/run_demo.py
├── src/mats_research/
│   ├── __init__.py
│   ├── evaluate.py
│   └── synthetic.py
├── tests/test_vertical_slice.py
├── pyproject.toml
└── README.md
```

## Runnable prototype

```bash
python -m pip install -e ".[test]"
pytest -q
python scripts/run_demo.py
```

The demo is synthetic and harmless. It does not train an agent, execute generated actions, connect to external systems, or target real-world assets.

## Prototype evidence boundary

The vertical slice demonstrates research infrastructure: deterministic generation, schema validation, matched oversight conditions, behavioural effect estimation, held-out linear prediction, AUROC/AUPRC, a shuffled-label negative control, reproducibility tests, configuration-as-code and CI.

It is **not** empirical evidence about frontier scheming, deceptive alignment, internal intentions or a production safety mechanism.

## Scientific standard

A candidate mechanism is not called explanatory merely because a probe correlates with behaviour. Stronger claims require held-out generalisation, appropriate negative controls, causal intervention and replication. The repository-level audit standard is in `docs/QUALITY_AUDIT.md`.

## Safety boundary

Public experiments must remain synthetic or explicitly approved and contained. Do not connect research agents to production credentials, personal accounts, real biological systems, financial targets, intrusion targets or unrestricted external execution. Safety-relevant behaviours should be represented with abstract, non-actionable tasks whenever possible. Stop conditions are defined in `docs/SAFETY.md`.

## Applicant data

Canonical contact metadata is stored separately from experimental code and datasets. See `docs/APPLICANT_PROFILE.md` and `docs/APPLICATION_METADATA.md`.

## Current programme facts

MATS's current Autumn 2026 materials describe a staged track/stream application process, sustained research engagement, and the Apollo Science of Scheming stream described above. The current FAQ also states the LLM-use restriction for application writing. citeturn621132search1turn621132search9

Programme funding, travel, visa and logistics details should be checked against the current official MATS materials at the point of submission rather than copied from historical cohort assumptions.
