"""Test mutual_recursion module."""


import pytest

FEMALE_SEQUENCE = [
    (0, 1),
    (5, 3),
    (10, 6),
    # my tests below
    (2, 2),
    (1, 1),
    (7, 5),
    (12, 8)
]

MALE_SEQUENCE = [
    (0, 0),
    (5, 3),
    (10, 6),
    # my tests below
    (2, 1),
    (1, 0),
    (7, 4),
    (12, 7)
]


@pytest.mark.parametrize('num, result', FEMALE_SEQUENCE)
def test_mutual_recursion_f(num, result):
    """Test for Hofstadter Female Sequence."""
    from mutual_recursion import f
    assert f(num) == result


@pytest.mark.parametrize('num, result', MALE_SEQUENCE)
def test_mutual_recursion_m(num, result):
    """Test for Hofstadter Male Sequence."""
    from mutual_recursion import m
    assert m(num) == result
