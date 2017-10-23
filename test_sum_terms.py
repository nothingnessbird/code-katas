"""Test for sum_series."""


import pytest


TEST_NUMS = [
    (1, '1.00'),
    (2, '1.25'),
    (3, '1.39'),
    # My tests below
    (5, '1.57'),
    (125, '2.65'),
    (5000, '3.88'),
    (8, '1.73')
]


@pytest.mark.parametrize('num, result', TEST_NUMS)
def test_sum_terms(num, result):
    """Test for summing the first nth term of a series."""
    from sum_terms import series_sum
    assert series_sum(num) == result
