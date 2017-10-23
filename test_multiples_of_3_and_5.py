"""Test multiples_of_3_and_5 module."""


import pytest

NUMS = [
    (10, 23),
    # my tests below
    (21, 98),
    (6, 8),
    (0, 0),
    (2, 0),
    (500, 57918)
]


@pytest.mark.parametrize('num, result', NUMS)
def test_multiples_of_3_and_5(num, result):
    """Test for multiples of 3 and 5."""
    from multiples_of_3_and_5 import solution
    assert solution(num) == result
