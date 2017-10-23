"""Kata: Sum of the first nth term of Series.

#1 Best Practices Solution by MMMAAANNN, doctornick5, Slx64, ninja37,
FablehavenGeek, nabrarpour4 (plus 20 more warriors)



def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))
"""


def series_sum(n):
    """Sum the first nth terms of a series."""
    return '{:.2f}'.format(sum(1.0 / (3 * i + 1) for i in range(n)))
