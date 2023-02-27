from seasons import check_DOB
from pytest import raises


def test_invalid():
    with raises(SystemExit):
        check_DOB("cat")
    with raises(SystemExit):
        check_DOB("July 3, 1998")


def test_valid():
    assert check_DOB("1923-02-02") == ["1923", "02", "02"]
    assert check_DOB("2007-03-22") == ["2007", "03", "22"]



