import numpy as np

from mats_research.evaluate import evaluate
from mats_research.synthetic import SyntheticConfig, generate


def test_generator_is_reproducible():
    a = generate(SyntheticConfig(n_samples=200, seed=11))
    b = generate(SyntheticConfig(n_samples=200, seed=11))
    assert a.equals(b)


def test_evaluation_is_finite_and_nontrivial():
    df = generate(SyntheticConfig(n_samples=1000, seed=3, effect_size=1.0))
    result = evaluate(df, seed=3)
    assert np.isfinite(result.baseline_rate)
    assert np.isfinite(result.oversight_effect)
    assert 0.0 <= result.probe_auroc <= 1.0
    assert 0.0 <= result.probe_auprc <= 1.0
    assert result.oversight_effect > 0
