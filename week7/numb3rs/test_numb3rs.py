from numb3rs import validate


def test_negative():
    assert validate("-2.-202.10.10") == False
    assert validate("-127.0.0.1") == False


def test_positive():
    assert validate("127.0.0.1") == True
    assert validate("512.512.512.512") == False
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.1000") == False
    assert validate("1.2") == False
    assert validate("1.2.2.2.2") == False
    assert validate("1.2.2.500") == False
    assert validate("1.300.2.2") == False


def test_words():
    assert validate("cat") == False
    assert validate("apple") == False
