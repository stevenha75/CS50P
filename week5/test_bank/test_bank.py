from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("hey") == 20

def test_else():
    assert value("Bob") == 100

def test_hello_caps():
    assert value("HELLO") == 0