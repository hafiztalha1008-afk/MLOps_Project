"""Tests for src.data."""

import pandas as pd

from src.data import drop_duplicates


def test_drop_duplicates_removes_exact_dupes():
    df = pd.DataFrame({"a": [1, 1, 2], "b": [1, 1, 2]})
    out = drop_duplicates(df)
    assert len(out) == 2
