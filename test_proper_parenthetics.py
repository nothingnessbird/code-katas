"""Tests for proper parenthetics."""

import pytest
import os

INPUT_STRINGS = [
    ('((()))', 0),
    ('((())', 1),
    (')(', -1),
    ('(()))', -1),
    ('asd(skja) slkjads(lkjlasd)', 0),
    ('((((((((((((((((((((((((((((()))))))))))))))))))))))))))))', 0),
    ('((((((((((((((((((((((((((((())))))))))))))))))))))))))))', 1),
    ('((((((((((((((((((((()))))))))))))))))))))))))))))))))))', -1),
    ('((((((((', 1),
    ('))))', -1),
    ('', 0),
    ('kjshdf928yr9348', 0),
    (')))(((', -1),
    ('()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()', 0),
    ('(dfahsfaweijfoiwejdaweoifue),lkjcoifae(laskjf(sdfsdofu)dhfweiu)()', 0),
    ('''"""Create stack data structure."""

from linked_list import LinkedList


class Stack(object):
    """Create a stack class."""

    def __init__(self, iterable=()):
        """Initialize stack with a linked list."""
        self._stack = LinkedList(iterable)

    def push(self, val):
        """Push new value to stack."""
        self._stack.push(val)

    def pop(self):
        """Pop head node from stack."""
        return self._stack.pop()

    def __len__(self):
        """Return size of stack."""
        return self._stack.size()''', 0),
    ('''def proper_parenthetics(string):
    """."""
    from stack import Stack
    container = Stack()
    closed_parens_counter = 0
    for char in string:
        if char == '(':
            container.push(char)
        elif char == ')':
            closed_parens_counter += 1
            if closed_parens_counter > len(container):
                return -1
    if closed_parens_counter != len(container):
        return 1
    else:
        return 0''', 0)
]


@pytest.mark.parametrize('string, result', INPUT_STRINGS)
def test_string(string, result):
    """Test that proper parenthetics returns properly."""
    from proper_parenthetics import proper_parenthetics
    assert proper_parenthetics(string) == result


here = os.path.abspath(os.path.dirname(__file__))


def test_read_file():
    """Test that file read in is tested properly."""
    with open(os.path.join(here, 'proper_parenthetics.py')) as f:
        read_me = f.read()
        from proper_parenthetics import proper_parenthetics
        assert proper_parenthetics(read_me) == 0


def test_read_file_meta():
    """Test that file read in is tested properly."""
    with open(os.path.join(here, 'test_proper_parenthetics.py')) as f:
        read_me = f.read()
        from proper_parenthetics import proper_parenthetics
        assert proper_parenthetics(read_me) == -1
