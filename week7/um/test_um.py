from um import count

# Tests for words w/ um in it
def test_um_words():
    assert count("Album, instrument, circumvillation") == 0
    assert count("overconsumption, rheumatologists") == 0


# Regular tests for um and regular words
def test_regular():
    assert count("Um yo um my name is um david... Lol um") == 4
    assert count("I am um.. Kind of scared... to talked um.") == 2


# Complex tests for um-words, um itself, and regular words
def test_complex():
    assert count("Um... album my name is circumillation um??!! um...") == 3
    assert count("?...>um um um UM... UM... OVERCONSUMPTION BOB") == 5
