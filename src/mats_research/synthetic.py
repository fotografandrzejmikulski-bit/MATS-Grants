"""Synthetic, harmless model-organism generator.

This prototype does not train or deploy an agent. It creates tabular synthetic
trajectories whose only purpose is to exercise the research/evaluation stack.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class SyntheticConfig:
    n_samples: int = 2000
    n_features: int = 8
    seed: int = 7
    effect_size: float = 0.8


def generate(config: SyntheticConfig = SyntheticConfig()) -> pd.DataFrame:
    rng = np.random.default_rng(config.seed)
    x = rng.normal(size=(config.n_samples, config.n_features))
    oversight = rng.integers(0, 2, size=config.n_samples)
    task_family = rng.integers(0, 4, size=config.n_samples)
    difficulty = rng.uniform(0, 1, size=config.n_samples)

    # A latent, synthetic oversight-sensitive signal. It is intentionally
    # observable so that the pipeline can be validated end-to-end.
    latent = (
        config.effect_size * (1 - 2 * oversight)
        + 0.35 * x[:, 0]
        - 0.25 * x[:, 1]
        + 0.15 * difficulty
    )
    probability = 1.0 / (1.0 + np.exp(-latent))
    target = rng.binomial(1, probability)

    columns = {f"feature_{i}": x[:, i] for i in range(config.n_features)}
    return pd.DataFrame(
        {
            **columns,
            "oversight_condition": oversight,
            "task_family": task_family,
            "difficulty": difficulty,
            "target_behaviour": target,
        }
    )
