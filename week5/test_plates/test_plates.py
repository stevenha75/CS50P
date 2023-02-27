from plates import is_valid

# “All vanity plates must start with at least two letters.”
def test_requirement1():
    assert is_valid("AA") == True
    assert is_valid("00") == False

# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_requirement2():
    assert is_valid("A") == False
    assert is_valid("AA1234") == True
    assert is_valid("AA12345") == False

# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an
# acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def test_requirement3():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA222") == True

# “No periods, spaces, or punctuation marks are allowed.”
def test_requirement4():
    assert is_valid("AAA22.") == False
    assert is_valid("AAA22?") == False

