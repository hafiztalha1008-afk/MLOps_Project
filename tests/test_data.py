"""Tests for src.data."""

import pandas as pd

from src.data import drop_duplicates, load_raw


def test_drop_duplicates_removes_exact_dupes():
    df = pd.DataFrame({"a": [1, 1, 2], "b": [1, 1, 2]})
    out = drop_duplicates(df)
    assert len(out) == 2


def test_load_raw_parses_semicolon_separator(tmp_path):
    """Regression test: UCI Wine Quality CSV uses ';' as separator."""
    csv = tmp_path / "wine.csv"
    csv.write_text("a;b;quality\n1;2;5\n3;4;7\n", encoding="utf-8")
    df = load_raw(csv)
    assert list(df.columns) == ["a", "b", "quality"]
    assert df["quality"].tolist() == [5, 7]
