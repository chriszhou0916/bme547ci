import pytest


@pytest.mark.parametrize('s,expected', [
    ("taChycArdic", True),
    ("  tachycardic  ", True),
    ("..,,tachycardic...,", True),
    ("tachycar", False),
    ("cidrCC", False),
    ("..  ..  asssstachycardiC.. ", True)
])
def test_exact(s, expected):
    from tachycardia import is_tachycardic
    answer = is_tachycardic(s)
    assert answer == expected


@pytest.mark.parametrize('s,expected', [
    ("taChycArdie", True),
    ("  tachycadic  ", True),
    ("..,,tachycdic...,", True),
    ("tachycar", False),
    ("cidrCC", False),
    ("..  ..  chycardiC.. ", True),
    ("tachyaddic", True),
    ("echycardic", True),
    ("tachycardd", True),
    ("tachybdic", False),
    ("tycardic", False),
    ("tachyrdic", True)
])
def test_fuzzy(s, expected):
    from tachycardia import is_tachycardic
    answer = is_tachycardic(s)
    assert answer == expected
