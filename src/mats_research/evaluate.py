"""Evaluation utilities for the safe research prototype."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import average_precision_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from .synthetic import validate_frame


@dataclass(frozen=True)
class EvaluationResult:
    baseline_rate: float
    monitored_rate: float
    unmonitored_rate: float
    oversight_effect: float
    probe_auroc: float
    probe_auprc: float
    test_size: int


def evaluate(df: pd.DataFrame, seed: int = 7) -> EvaluationResult:
    """Evaluate behavioural effect and a held-out linear predictive baseline."""
    validate_frame(df)
    y = df["target_behaviour"].astype(int)
    baseline_rate = float(y.mean())
    monitored = float(df.loc[df["oversight_condition"] == 1, "target_behaviour"].mean())
    unmonitored = float(df.loc[df["oversight_condition"] == 0, "target_behaviour"].mean())
    oversight_effect = unmonitored - monitored

    features = sorted(c for c in df.columns if c.startswith("feature_"))
    x_train, x_test, y_train, y_test = train_test_split(
        df[features], y, test_size=0.30, random_state=seed, stratify=y
    )

    model = Pipeline(
        steps=[
            ("scale", StandardScaler()),
            ("logreg", LogisticRegression(max_iter=2000, random_state=seed)),
        ]
    )
    model.fit(x_train, y_train)
    score = model.predict_proba(x_test)[:, 1]

    return EvaluationResult(
        baseline_rate=baseline_rate,
        monitored_rate=monitored,
        unmonitored_rate=unmonitored,
        oversight_effect=oversight_effect,
        probe_auroc=float(roc_auc_score(y_test, score)),
        probe_auprc=float(average_precision_score(y_test, score)),
        test_size=int(len(y_test)),
    )


def permutation_auroc(df: pd.DataFrame, seed: int = 7, repeats: int = 5) -> np.ndarray:
    """Return AUROC scores after label permutation as a negative-control distribution."""
    validate_frame(df)
    if repeats < 2:
        raise ValueError("repeats must be >= 2")
    rng = np.random.default_rng(seed)
    scores = []
    features = sorted(c for c in df.columns if c.startswith("feature_"))
    x_train, x_test, y_train, y_test = train_test_split(
        df[features], df["target_behaviour"].astype(int),
        test_size=0.30, random_state=seed, stratify=df["target_behaviour"],
    )
    for _ in range(repeats):
        shuffled = y_train.to_numpy(copy=True)
        rng.shuffle(shuffled)
        model = Pipeline([
            ("scale", StandardScaler()),
            ("logreg", LogisticRegression(max_iter=2000, random_state=seed)),
        ])
        model.fit(x_train, shuffled)
        scores.append(roc_auc_score(y_test, model.predict_proba(x_test)[:, 1]))
    return np.asarray(scores, dtype=float)
