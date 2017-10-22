"""Kata: Collatz.

#1 Best Practices Solution by misuburlacu

def collatz(n):
    l = [str(n)]
    while n > 1:
        n = 3 * n + 1 if n % 2 else n / 2
        l.append(str(n))
    return '->'.join(l)
"""


def collatz(n):
    """Call the collatz recursion with initialized results list."""
    return collatz_recur(n, [])


def collatz_recur(n, results):
    """Recursively compute collatz string."""
    if n == 1:
        results.append(str(int(n)))
        return '->'.join(results)
    elif n % 2:
        results.append(str(int(n)))
        return collatz_recur(3 * n + 1, results)
    elif not n % 2:
        results.append(str(int(n)))
        return collatz_recur(n / 2, results)
