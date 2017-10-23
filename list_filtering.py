"""Kata: List Filtering.

#1 Best Practices Solution by clawtros, jtcromwell, colbydauph, canibanoglu,
bilderbuchi, kasterma (plus 86 more warriors)

def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]
"""


def filter_list(l):
    """Filter strings out of given list."""
    return [item for item in l if type(item) is not str]
