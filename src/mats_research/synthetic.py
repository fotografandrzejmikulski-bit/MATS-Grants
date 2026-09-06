"""Harmless synthetic benchmark generator.

The generator creates tabular data with a known data-generating process so the
research stack can be tested end-to-end without training or deploying an agent.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Final

import numpy as np
import pandas as pd

REQUIRED_COLUMNS: Final[tuple[str, ...]] = (
    "oversight_condition",
    "task_family",
    "difficulty",
    "target_behaviour",
)


@dataclass(frozen=True)
class SyntheticConfig:
    n_samples: int = 2000
    n_features: int = 8
    n_task_families: int = 4
    seed: int = 7
    effect_size: float = 0.8
    noise_scale: float = 0.35

    def validate(self) -> None:
        if self.n_samples < 100:
            raise ValueError("n_samples must be >= 100")
        if self.n_features < 2:
            raise ValueError("n_features must be >= 2")
        if self.n_task_families < 2:
            raise ValueError("n_task_families must be >= 2")
        if self.noise_scale <= 0:
            raise ValueError("noise_scale must be > 0")


def generate(config: SyntheticConfig = SyntheticConfig()) -> pd.DataFrame:
    """Generate deterministic synthetic observations for a fixed seed."""
    config.validate()
    rng = np.random.default_rng(config.seed)
    x = rng.normal(size=(config.n_samples, config.n_features))
    oversight = rng.integers(0, 2, size=config.n_samples)
    task_family = rng.integers(0, config.n_task_families, size=config.n_samples)
    difficulty = rng.uniform(0, 1, size=config.n_samples)

    # Known latent signal. The sign flip by oversight_condition is deliberate:
    # it gives the evaluator a ground-truth effect to recover.
    latent = (
        config.effect_size * (1 - 2 * oversight)
        + 0.35 * x[:, 0]
        - 0.25 * x[:, 1]
        + 0.15 * difficulty
        + rng.normal(scale=config.noise_scale, size=config.n_samples)
    )
    probability = 1.0 / (1.0 + np.exp(-latent))
    target = rng.binomial(1, probability)

    columns = {f"feature_{i}": x[:, i] for i in range(config.n_features)}
    return pd.DataFrame(
        {
            **columns,
            "oversight_condition": oversight.astype(int),
            "task_family": task_family.astype(int),
            "difficulty": difficulty.astype(float),
            "target_behaviour": target.astype(int),
        }
    )


def validate_frame(df: pd.DataFrame, config: SyntheticConfig | None = None) -> None:
    """Validate schema and basic domain invariants."""
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    feature_columns = [c for c in df.columns if c.startswith("feature_")]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    if len(feature_columns) < 2:
        raise ValueError("At least two feature_* columns are required")
    if df.empty:
        raise ValueError("DataFrame must not be empty")
    if not set(df["oversight_condition"].unique()).issubset({0, 1}):
        raise ValueError("oversight_condition must be binary")
    if not set(df["target_behaviour"].unique()).issubset({0, 1}):
        raise ValueError("target_behaviour must be binary")
    if ((df["difficulty"] < 0) | (df["difficulty"] > 1)).any():
        raise ValueError("difficulty must be within [0, 1]")
    if config is not None and len(df) != config.n_samples:
        raise ValueError("Unexpected number of samples")
