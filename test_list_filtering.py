"""Test list_filtering module."""


import pytest

FILTER_LISTS = [
    ([1, 2, 'a', 'b'], [1, 2]),
    ([1, 'a', 'b', 0, 15], [1, 0, 15]),
    ([1, 2, 'aasf', '1', '123', 123], [1, 2, 123]),
    (['a', 'b', '1'], []),
    ([1, 2, 'a', 'b'], [1, 2]),
    # Below are my tests
    ([2, -5, True, '4', 'hello world'], [2, -5, True]),
    ([False, 'seven', [], 3], [False, [], 3]),
    ([('this', 'is', 'a', 'tuple'), 'should not return', -5],
        [('this', 'is', 'a', 'tuple'), -5]),
    ([{'some': 'object literal'}, 'a string', ('tuple', 5, True), False,
        ['a', 'list']], [{'some': 'object literal'}, ('tuple', 5, True), False,
                         ['a', 'list']])
]


@pytest.mark.parametrize('l, result', FILTER_LISTS)
def test_list_filtering(l, result):
    """Test for filtering strings out of list."""
    from list_filtering import filter_list
    assert filter_list(l) == result
