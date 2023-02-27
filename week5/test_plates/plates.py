def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("VALID")
    else:
        print("Invalid")


# Checks input against all requirements and returns apropriately
def is_valid(s):
    if requirement_3(s) and requirement_1(s) and requirement_2(s) and requirement_4(s):
        return True
    else:
        return False


# “All vanity plates must start with at least two letters.”
def requirement_1(s):
    if s[0:2].isalpha():
        return True
    else:
        return False


# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def requirement_2(s):
    if (len(s) >= 2) and (len(s) <= 6):
        return True
    else:
        return False


# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an
# acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def requirement_3(s):
    # Checks if the first number is a 0
    for i in range(len(s)):
        if s[i].isnumeric():
            if s[i] == "0":
                return False
            break
    # If there is a number -> checks to make sure everything after is also a number
    for i in range(len(s)):
        if s[i].isnumeric():
            if not s[i:].isnumeric():
                return False
    return True


# “No periods, spaces, or punctuation marks are allowed.”
def requirement_4(s):
    restricted_chars = [".", " ", ".", "!", "?"]
    for i in range(len(s)):
        if s[i] in restricted_chars:
            return False
    return True


if __name__ == "__main__":
    main()
