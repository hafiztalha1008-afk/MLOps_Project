"""Train a Random Forest on the Wine Quality training split."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import joblib
import pandas as pd
import yaml
from sklearn.ensemble import RandomForestClassifier


def main(smoke: bool = False) -> None:
    params = yaml.safe_load(Path("params.yaml").read_text(encoding="utf-8"))
    seed = params["seed"]
    tp = params["train"]

    df = pd.read_csv("data/processed/train.csv")
    if smoke:
        df = df.head(200)
    X = df.drop(columns=["quality"])
    y = df["quality"]

    if tp["model"] == "random_forest":
        model = RandomForestClassifier(
            n_estimators=tp["n_estimators"],
            max_depth=tp["max_depth"],
            random_state=seed,
            n_jobs=-1,
        )
    else:
        raise ValueError(f"Unknown model: {tp['model']}")

    model.fit(X, y)

    out = Path("models")
    out.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, out / "model.pkl")
    print(f"Trained {tp['model']} on {len(df)} rows")


if __name__ == "__main__":
    main(smoke="--smoke" in sys.argv)
