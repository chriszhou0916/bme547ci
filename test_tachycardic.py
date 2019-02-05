import pytest


@pytest.mark.parametrize('s,expected', [
    ("taChycArdic", True),
    ("  tachycardic  ", True),
    ("..,,tachycardic...,", True),
    ("tachycard", False),
    ("cidrCC", False),
    ("..  ..  asssstachycardiC.. ", True)
])
def test_exact(s, expected):
    from tachycardia import is_tachycardic
    answer = is_tachycardic(s)
    assert answer == expected
