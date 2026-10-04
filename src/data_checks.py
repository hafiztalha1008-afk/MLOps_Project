"""Basic data sanity checks for the Wine Quality dataset."""

import sys

import pandas as pd

EXPECTED_COLUMNS = [
    "fixed acidity",
    "volatile acidity",
    "citric acid",
    "residual sugar",
    "chlorides",
    "free sulfur dioxide",
    "total sulfur dioxide",
    "density",
    "pH",
    "sulphates",
    "alcohol",
    "quality",
]


def main(path: str = "data/raw/winequality.csv") -> None:
    df = pd.read_csv(path, sep=";")

    missing = set(EXPECTED_COLUMNS) - set(df.columns)
    assert not missing, f"Missing columns: {missing}"

    assert df.isna().sum().sum() == 0, "Dataset contains nulls"
    assert df["quality"].between(0, 10).all(), "quality out of range [0,10]"
    assert df["alcohol"].between(0, 20).all(), "alcohol out of range"

    print(f"data_checks OK: {df.shape[0]} rows, {df.shape[1]} cols")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/raw/winequality.csv")
