"""Tests for proper parenthetics."""

import pytest

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
    ('(dfahsfaweijfoiwejdaweoifue),lkjcoifae(laskjf(sdfsdofu)dhfweiu)()', 0)
]


@pytest.mark.parametrize('string, result', INPUT_STRINGS)
def test_string(string, result):
    """Test that proper parenthetics returns properly."""
    from proper_parenthetics import proper_parenthetics
    assert proper_parenthetics(string) == result
