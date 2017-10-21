"""Kata: Mutual Recursion.

#1 Best Practices Solution by daddepledge, anter69,
amarovita, Blind4Basics, kingcobra, simosini

def f(n): return n - m(f(n-1)) if n else 1

def m(n): return n - f(m(n-1)) if n else 0
"""


def f(n):
    """Return nth index in Hofstadter Female Sequence."""
    if n == 0:
        return 1
    else:
        return n - m(f(n - 1))


def m(n):
    """Return nth index in Hofstadter Male Sequence."""
    if n == 0:
        return 0
    else:
        return n - f(m(n - 1))
