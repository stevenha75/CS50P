from twttr import shorten

def test_lower():
    assert shorten("this is a test sentence") == "ths s  tst sntnc"

def test_upper():
    assert shorten("THIS IS A TEST SENTENCE") == "THS S  TST SNTNC"

def test_num():
    assert shorten("12345") == "12345"

def test_mix_cap():
    assert shorten("tHiS iS a tEsT sEnTeNcE") == "tHS S  tsT snTNc"

def test_punctuation():
    assert shorten("!,?") == "!,?"


