"""Kata: Sum of two lowest positive integers.

#1 Best Practices Solution by danman1979, MirzaI, mstrfx, VadimPopov, dmpage,
redundnt (plus 356 more warriors)

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
"""


def sum_two_smallest_numbers(numbers):
    """Sum the two smallest positive numbers in a given list."""
    sorted_nums = numbers
    sorted_nums.sort()
    return sorted_nums[0] + sorted_nums[1]
