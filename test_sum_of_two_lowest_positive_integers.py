"""Test sum_of_two_lowest_positive_integers module."""


import pytest

SUM_NUMS = [
    ([5, 8, 12, 18, 22], 13),
    ([7, 12, 15, 18, 22], 19),
    ([12, 18, 22, 25, 42], 30),
    ([1, 5, 8, 12, 18], 6),
    ([5, 12, 13, 22, 61], 17),
    # Below are my tests
    ([3, 100, 2, 90, 750], 5),
    ([5, 90, 34, 28, 100], 33),
    ([2, 3], 5),
    ([10000, 200000, 6734298, 230, 480], 710)
]


@pytest.mark.parametrize('numbers, result', SUM_NUMS)
def test_fibonacci(numbers, result):
    """Test for summing two lowest numbers in list."""
    from sum_of_two_lowest_positive_integers import sum_two_smallest_numbers
    assert sum_two_smallest_numbers(numbers) == result
