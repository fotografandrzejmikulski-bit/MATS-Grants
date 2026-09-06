"""Run the complete safe vertical slice locally."""

from mats_research.evaluate import evaluate
from mats_research.synthetic import SyntheticConfig, generate


def main() -> None:
    df = generate(SyntheticConfig(n_samples=2000, seed=7, effect_size=0.8))
    result = evaluate(df, seed=7)
    print("MATS Grants safe research vertical slice")
    print(f"samples={len(df)}")
    print(f"baseline_rate={result.baseline_rate:.3f}")
    print(f"oversight_effect={result.oversight_effect:.3f}")
    print(f"probe_auroc={result.probe_auroc:.3f}")
    print(f"probe_auprc={result.probe_auprc:.3f}")


if __name__ == "__main__":
    main()
