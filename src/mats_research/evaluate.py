"""Evaluation utilities for the research prototype."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import train_test_split


@dataclass(frozen=True)
class EvaluationResult:
    baseline_rate: float
    oversight_effect: float
    probe_auroc: float
    probe_auprc: float


def evaluate(df: pd.DataFrame, seed: int = 7) -> EvaluationResult:
    y = df["target_behaviour"]
    baseline_rate = float(y.mean())
    monitored = df.loc[df["oversight_condition"] == 1, "target_behaviour"].mean()
    unmonitored = df.loc[df["oversight_condition"] == 0, "target_behaviour"].mean()
    oversight_effect = float(unmonitored - monitored)

    features = [c for c in df.columns if c.startswith("feature_")]
    x_train, x_test, y_train, y_test = train_test_split(
        df[features], y, test_size=0.30, random_state=seed, stratify=y
    )
    model = LogisticRegression(max_iter=2000)
    model.fit(x_train, y_train)
    score = model.predict_proba(x_test)[:, 1]

    return EvaluationResult(
        baseline_rate=baseline_rate,
        oversight_effect=oversight_effect,
        probe_auroc=float(roc_auc_score(y_test, score)),
        probe_auprc=float(average_precision_score(y_test, score)),
    )
