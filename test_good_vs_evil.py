"""Test good_vs_evil module."""


import pytest

FORCES = [
    ('1 1 1 1 1 1', '1 1 1 1 1 1 1',
        'Battle Result: Evil eradicates all trace of Good'),
    ('0 0 0 0 0 10', '0 1 1 1 1 0 0',
        'Battle Result: Good triumphs over Evil'),
    ('1 0 0 0 0 0', '1 0 0 0 0 0 0',
        'Battle Result: No victor on this battle field'),
    # Below are my tests
    ('20 2 50 0 33 5', '0 9 99 20 12 2',
        'Battle Result: Good triumphs over Evil'),
    ('1 23 0 40 3 25', '67 2 49 1 0 70',
        'Battle Result: Evil eradicates all trace of Good'),
    ('20 0 8 28 10 13', '104 36 10 23 12 4',
        'Battle Result: No victor on this battle field'),
    ('0 1 0 1 0 1', '1 0 1 0 1 0',
        'Battle Result: Good triumphs over Evil')
]


@pytest.mark.parametrize('good, evil, result', FORCES)
def test_good_vs_evil(good, evil, result):
    """Test for good vs evil."""
    from good_vs_evil import good_vs_evil
    assert good_vs_evil(good, evil) == result
