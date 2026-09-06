import numpy as np
import pytest

from mats_research.evaluate import evaluate, permutation_auroc
from mats_research.synthetic import SyntheticConfig, generate, validate_frame


def test_generator_is_reproducible():
    cfg = SyntheticConfig(n_samples=200, seed=11)
    assert generate(cfg).equals(generate(cfg))


def test_generator_changes_with_seed():
    assert not generate(SyntheticConfig(n_samples=200, seed=11)).equals(
        generate(SyntheticConfig(n_samples=200, seed=12))
    )


def test_schema_validation_accepts_valid_frame():
    df = generate(SyntheticConfig(n_samples=200, seed=11))
    validate_frame(df)


def test_schema_validation_rejects_missing_columns():
    df = generate(SyntheticConfig(n_samples=200, seed=11)).drop(columns=["difficulty"])
    with pytest.raises(ValueError, match="Missing required columns"):
        validate_frame(df)


def test_evaluation_is_finite_and_nontrivial():
    df = generate(SyntheticConfig(n_samples=1200, seed=3, effect_size=1.0))
    result = evaluate(df, seed=3)
    assert np.isfinite(result.baseline_rate)
    assert np.isfinite(result.monitored_rate)
    assert np.isfinite(result.unmonitored_rate)
    assert np.isfinite(result.oversight_effect)
    assert 0.0 <= result.probe_auroc <= 1.0
    assert 0.0 <= result.probe_auprc <= 1.0
    assert result.oversight_effect > 0
    assert result.test_size > 0


def test_permutation_negative_control_is_finite():
    df = generate(SyntheticConfig(n_samples=1200, seed=5))
    scores = permutation_auroc(df, seed=5, repeats=5)
    assert scores.shape == (5,)
    assert np.isfinite(scores).all()
    assert np.all((scores >= 0.0) & (scores <= 1.0))
