import re

# Todo List:
# - make tests & practice pytest


def main():
    print(validate(input("IPv4 Address: ")))


# Returns true or false if IPv4 address if valid or not
def validate(ip):
    if matches := re.search(
        r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip
    ):
        # Look through each group of the re and check for num > 225
        for i in range(len(matches.groups())):
            if int(matches.group(i + 1)) > 255:
                return False
        # If nothing is too large return true
        return True
    # Returns false if it fails the re
    else:
        return False


if __name__ == "__main__":
    main()
