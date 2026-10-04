"""Evaluate trained model on test set, write metrics.json."""

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score


def main() -> None:
    model = joblib.load("models/model.pkl")
    test = pd.read_csv("data/processed/test.csv")
    X = test.drop(columns=["quality"])
    y = test["quality"]

    preds = model.predict(X)
    metrics = {
        "accuracy": float(accuracy_score(y, preds)),
        "f1_macro": float(f1_score(y, preds, average="macro")),
        "n_test": int(len(test)),
    }

    try:
        sha = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
    except Exception:
        sha = "unknown"
    metrics["commit_sha"] = sha[:8]

    Path("metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
