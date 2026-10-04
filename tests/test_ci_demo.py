"""Temporary broken test to demonstrate CI blocking a PR."""


def test_deliberately_broken():
    assert 1 == 2, "This test is intentionally broken to demo CI red"
