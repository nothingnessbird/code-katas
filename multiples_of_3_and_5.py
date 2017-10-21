"""Kata: Multiples of 3 and 5.

#1 Best Practices Solution by Process,
zyxwhut, lowicz, simpajj, benjaminfigueiredo, nueks (plus 79 more warriors)

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
"""


def solution(number):
    """Return sum of all multiples of 3 or 5 in range given."""
    sum_multiples = 0
    for num in range(number):
        if (num % 3) == 0 or (num % 5) == 0:
            sum_multiples += num
    return sum_multiples
