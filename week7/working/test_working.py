from working import convert
from pytest import raises

# Wrong format/incorrect times
def test_invalid_input():
    with raises(ValueError):
        convert("cat")
    with raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with raises(ValueError):
        convert("9 AM - 5 PM")
    with raises(ValueError):
        convert("09:00 AM - 17:00 PM")


def test_AM():
    assert convert("12 AM to 3 AM") == "00:00 to 03:00"
    assert convert("4:23 AM to 6:55 AM") == "04:23 to 06:55"


def test_PM():
    assert convert("12 PM to 2 PM") == "12:00 to 14:00"
    assert convert("2:23 PM to 7:46 PM") == "14:23 to 19:46"


def test_MIX():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
