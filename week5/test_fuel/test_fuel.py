import pytest
from fuel import convert, gauge

# Test convert implementation
def test_numeric():
    with pytest.raises(ValueError):
        convert("a/2")
    with pytest.raises(ValueError):
        convert("2/a")


def test_num_large():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("3/2")


def test_div_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_no_error():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/5") == 20


# Test guage implementation
def test_empty():
    assert gauge(1) == "E"


def test_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_percentage():
    assert gauge(65) == "65%"
    assert gauge(32) == "32%"
