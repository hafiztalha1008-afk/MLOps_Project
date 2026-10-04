"""Data loading and cleaning utilities for the Wine Quality dataset."""
from pathlib import Path

import pandas as pd

RAW_PATH = Path("data/raw/winequality.csv")


def load_raw(path: Path = RAW_PATH) -> pd.DataFrame:
    """Load the raw Wine Quality CSV."""
    return pd.read_csv(path)


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Return the dataframe with duplicate rows removed."""
    return df.drop_duplicates().reset_index(drop=True)
