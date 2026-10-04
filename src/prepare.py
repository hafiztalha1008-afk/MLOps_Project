"""Split raw Wine Quality data into train/test sets."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yaml

from src.data import load_raw


def main() -> None:
    params = yaml.safe_load(Path("params.yaml").read_text(encoding="utf-8"))
    seed = params["seed"]
    test_size = params["split"]["test_size"]

    df = load_raw()
    df = df.drop_duplicates().reset_index(drop=True)

    rng = df.sample(frac=1.0, random_state=seed).reset_index(drop=True)
    n_test = int(len(rng) * test_size)
    test = rng.iloc[:n_test].reset_index(drop=True)
    train = rng.iloc[n_test:].reset_index(drop=True)

    out = Path("data/processed")
    out.mkdir(parents=True, exist_ok=True)
    train.to_csv(out / "train.csv", index=False)
    test.to_csv(out / "test.csv", index=False)
    print(f"Train: {train.shape}, Test: {test.shape}")


if __name__ == "__main__":
    main()
